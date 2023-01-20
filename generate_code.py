#!/usr/bin/env python3

"""Generate Python class definitions from the GraphQL schema of Caido.

It's a rough implementation only intended to quickly generate some boiler code which will
likely be tweaked a lot before the models and functions get implemented in the actual python
caido library.
"""
import httpx
from typing import Dict, Tuple
import re
from pathlib import Path
import shutil
import json
import black
from os import environ

DATETIME_FORMAT = r"%Y-%m-%dT%H:%M:%S.%fz"
AUTH_TOKEN = environ.get("CAIDO_AUTH_TOKEN")


BASE_URL = "http://127.0.0.1:8080/graphql"

SCALAR_TYPE_MAPPING = {
    "String": "str",
    "Boolean": "bool",
    "ID": "str",
    "Int": "int",
    "LIST": "List",
    "JSON": "Any",
    "DateTime": "datetime",
    "Float": "float",
    # NOTE: These are special Scalars created by Caido. For now we just convert to native python types
    "Url": "str",
    "Uri": "str",
    "Blob": "str",
    "Rank": "str",
    "Snapshot": "str",
    "Timestamp": "int",
    "Token": "str",
    "Upload": "str",
}


def write_model(model_name, definition, folder=Path("generated_models")):
    """Write a model definition to file."""

    definition = black.format_str(definition, mode=black.Mode())  # type: ignore

    folder.mkdir(exist_ok=True)

    filename = model_name.lower().strip()
    model_path = Path(f"{folder}/{filename}.py")
    print(f"Writing {model_name} to {model_path}...")
    with open(model_path, "w") as f:
        f.write(definition)

    init_path = Path(f"{folder}/__init__.py")
    if init_path.exists():
        with open(init_path, "a") as f:
            f.write(f"from .{filename} import {model_name}\n")
    else:
        with open(init_path, "w") as f:
            f.write('"""Caido models."""\n\nfrom .basemodel import BaseModel\n')
            f.write(f"from .{filename} import {model_name}\n")


def camel_to_snake_case(string: str) -> str:
    """Converts camelCase to snake_case."""
    string = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", string).lower()


def get_schema():
    """Retrieve schema from GraphQL."""
    headers = {
        "User-Agent": "Python Caido Client",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "Authorization": f"Bearer {AUTH_TOKEN}",
    }
    with httpx.Client(headers=headers) as client:  # type: ignore
        response = client.post(BASE_URL, json=full_schema())

    return response.json()["data"]["__schema"]


def main():
    """Script entrypoint."""
    schema = get_schema()

    folder = Path("caido/models")
    print(f"Remove any old generated models from folder {folder}...")
    shutil.rmtree(folder, ignore_errors=True)

    print(f"Generating BaseModel")
    write_model("BaseModel", generate_base_model_definition(), folder)

    print("Generating models from schema")
    for item in schema["types"]:
        if item["name"].startswith("__"):
            continue

        # TODO: Do we want to create classes for the Caido specific SCALAR definitions?
        # if item["kind"] == "SCALAR" and item["name"] not in SCALAR_TYPE_MAPPING.keys():
        #     scalars.append(generate_scalar_definition(item))

        if item["kind"] == "OBJECT":

            # TODO: Generate client functions from query root
            if item["name"] in (
                "QueryRoot",  # This provides insight into the queries you can perform
                "MutationRoot",  # This provides insight into the mutations you can perform
                "SubscriptionRoot",  # This provides insight into what subscriptions you can register to
            ):
                continue

            print(f"Generating definiton for {item['name']}")
            class_definition = generate_class_definition(item)
            write_model(item["name"], class_definition, folder)

        elif item["kind"] == "ENUM":
            enum_definition = generate_enum_definition(item)
            write_model(item["name"], enum_definition, folder)

        elif item["kind"] == "UNION":
            union_definition = generate_union_definition(item)
            write_model(item["name"], union_definition, folder)


def generate_scalar_definition(item) -> str:
    """Generate a definition of custom defined scalar types in GraphQL schema."""
    SCALAR_MAPPING = {
        "Url": "str",
        "Uri": "str",
        "Blob": "str",
        "Rank": "str",
        "Snapshot": "str",
        "Timestamp": "int",
        "Token": "str",
        "Upload": "str",
    }

    for scalar, type_name in SCALAR_MAPPING.items():
        if scalar == item["name"]:
            description = item.get(
                "description", f"GraphQL Scalar {scalar} mapping to type {type_name}."
            ).strip()
            return f'class {scalar}()\n    """{description}"""'

    raise ValueError(f"Could not find mapping for scalar: {json.dumps(item, indent=2)}")


def generate_base_model_definition() -> str:
    """Generates the BaseModel definition."""
    return """
from typing import Dict

class BaseModel:
    \"""Base model representing objects in Caido GraphQL API.\"""

    @classmethod
    def from_graphql(cls, response: Dict):
        \"""Convert GraphQL response to model.\"""
        raise NotImplementedError

    def to_graphql(self):
        \"""Convert class instance to GraphQL model.\"""
        raise NotImplementedError
    """


def generate_class_definition(item: Dict) -> str:
    """Generate a python Class definition from a GraphQL item."""

    definition = f"""
class {item['name']}(BaseModel):
    """
    if item["description"]:
        definition += f'"""{item["description"].strip().strip(".")}."""\n'
    else:
        definition += f'"""Class definition for {item["name"]}."""\n'

    # Gather all class arguments
    parsed_fields = []
    for field in item["fields"]:
        if field["isDeprecated"] is True:
            continue

        if field["name"] in ("AND", "OR"):
            # TODO: How to handle special field names like AND and OR
            # black doesn't like them and they use the NON_NULL field
            continue

        parsed_fields.append(convert_graphql_field(field))

    # Sort by optional fields
    parsed_fields.sort(key=lambda field: field[3])

    # Generate __init__.py
    init_function_signature = "\n    def __init__(self"
    for python_name, _, type_name, is_optional in parsed_fields:
        if is_optional == False:
            init_function_signature += f", {python_name}: {type_name}"
        else:
            init_function_signature += f", {python_name}: Optional[{type_name}]"

    init_function_signature += (
        f'):\n        """Initialize {item["name"]} class instance."""\n'
    )
    definition += init_function_signature
    for python_name, _, _, _ in parsed_fields:
        definition += f"        self.{python_name} = {python_name}\n"

    # Generate prettier repr
    # TODO: instead of doing the if condition in __repr__
    # iterate over the available fields in the class to determine the
    # best __repr__ method
    definition += f"""
    
    def __repr__(self) -> str:
        \"""Pretty class representation when printing.\"""
        if hasattr(self, "name"):
            return f"<{item['name']} {{self.name}}>"
        elif hasattr(self, "id"):
            return f"<{item['name']} {{self.id}}>"
        else:
            return f"<{item['name']}>"
    """

    # Generate from_graphql() classmethod
    from_graphql_function_signature = f"""

    @classmethod
    def from_graphql(cls, response: Dict):
        \"""Generate {item['name']} instance from GraphQL query result.\"""
        instance = cls(\n"""
    definition += from_graphql_function_signature

    for python_name, graphql_name, type_name, is_optional in parsed_fields:
        if is_optional is False:
            if type_name == "datetime":
                definition += f"            {python_name}=datetime.strptime(response['{graphql_name}'], '{DATETIME_FORMAT}'),\n"
            else:
                definition += f"            {python_name}=response['{graphql_name}'],\n"
        else:
            # TODO: Convert optional datetimes. Will require refactor outside of cls() init
            definition += f"            {python_name}=response.get('{graphql_name}'),\n"

    definition += "        )\n\n        return instance"

    # Add relevant imports
    import_definition = f"""
#!/usr/bin/env python3
        
from .basemodel import BaseModel
"""
    python_type_hints = {
        type_name
        for _, _, type_name, _ in parsed_fields
        if type_name in ("List", "Dict", "Optional", "Set", "Union", "Any")
    }
    python_type_hints.update({"Dict", "Optional"})
    import_definition += f"from typing import {', '.join(python_type_hints)}\n"

    type_hints = {
        type_name
        for _, _, type_name, _ in parsed_fields
        if type_name not in python_type_hints
        and type_name
        not in (
            "str",
            "int",
            "float",
            "bool",
        )
    }

    for type_name in type_hints:
        if type_name == "datetime":
            import_definition += f"from datetime import datetime\n"
        else:
            # Assume we're dealing with Caido generated models
            import_definition += f"from .{type_name.lower()} import {type_name}\n"

    return import_definition + definition


def generate_enum_definition(item: Dict) -> str:
    """Generate a python Enum definition from a GraphQL item."""
    definition = f"""
#!/usr/bin/env python3
        
from enum import Enum
        
class {item['name']}(Enum):
"""

    if item["description"]:
        definition += f'    """{item["description"].strip().strip(".")}."""\n\n'
    else:
        definition += f'    """Enum definition for {item["name"]}."""\n\n'

    for value in item["enumValues"]:
        if value["isDeprecated"] is True:
            continue

        definition += f'    {value["name"]} = "{value["name"]}"\n'

    return definition


def generate_union_definition(item: Dict) -> str:
    """Generate a python definition from a GraphQL Union item."""
    # TODO: Figure out a nice way to parse these things, for now we'll
    # just create an empty class with optional types
    definition = f"""
#!/usr/bin/env python3

from typing import Optional

class {item['name']}:
"""

    if item["description"]:
        definition += f'    """{item["description"].strip().strip(".")}."""\n\n'
    else:
        definition += f'    """Union definition for {item["name"]}."""\n\n'

    for value in item["possibleTypes"]:
        definition += f'    {camel_to_snake_case(value["name"])}: Optional = None  # {value["name"]}\n'

    return definition


def convert_graphql_field(field: Dict) -> Tuple[str, str, str, bool]:
    """Converts a GraphQL field into the variable name and type hint."""
    field_name = camel_to_snake_case(field["name"])

    is_optional = field["type"].get("kind") != "NON_NULL"

    # Parse out the argument type
    type_name = ""
    if field["type"].get("name"):
        type_name = field["type"]["name"]
    else:
        if field["type"]["ofType"].get("name"):
            type_name = field["type"]["ofType"]["name"]
        else:
            type_name = field["type"]["ofType"]["kind"]

    # Convert GraphQL types to their Python equivalent
    for graphql_type_name, python_type_name in SCALAR_TYPE_MAPPING.items():
        if graphql_type_name == type_name:
            type_name = python_type_name
            break

    return field_name, field["name"], type_name, is_optional


def full_schema():
    """Retrieve the full schema definition using introspection.

    Taken from:
    https://stackoverflow.com/questions/37397886/get-graphql-whole-schema-query
    """
    query = {
        "query": """
    query IntrospectionQuery {
    __schema {
        queryType {
        name
        }
        mutationType {
        name
        }
        subscriptionType {
        name
        }
        types {
        ...FullType
        }
        directives {
        name
        description
        locations
        args {
            ...InputValue
        }
        }
    }
    }

    fragment FullType on __Type {
    kind
    name
    description
    fields(includeDeprecated: true) {
        name
        description
        args {
        ...InputValue
        }
        type {
        ...TypeRef
        }
        isDeprecated
        deprecationReason
    }
    inputFields {
        ...InputValue
    }
    interfaces {
        ...TypeRef
    }
    enumValues(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
    }
    possibleTypes {
        ...TypeRef
    }
    }

    fragment InputValue on __InputValue {
    name
    description
    type {
        ...TypeRef
    }
    defaultValue
    }

    fragment TypeRef on __Type {
    kind
    name
    ofType {
        kind
        name
        ofType {
        kind
        name
        ofType {
            kind
            name
            ofType {
            kind
            name
            ofType {
                kind
                name
                ofType {
                kind
                name
                ofType {
                    kind
                    name
                }
                }
            }
            }
        }
        }
    }
    }
    """
    }
    return query


if __name__ == "__main__":
    main()
