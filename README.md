# Python client for Caido web security auditing toolkit

This package allows you to communicate with a Caido instance from Python.

***IMPORTANT*** This is very much a work in progress, the API will change, things will break and at the moment
am still investigating if I will continue my efforts..


# Installation

Clone this github repository and install the library:

```sh
git clone https://github.com/thiezn/caido-python.git
cd caido-python
python3 -m pip install .
```

# Basic usage:

At the moment this is in very early stages and we can only fetch all projects, fetch the current project and fetch the runtime.

Check the run.py script in the root of the repo for an example. Make sure to set your Caido authentication token in an environment
variable called CAIDO_AUTH_TOKEN

```sh
export CAIDO_AUTH_TOKEN=<Grap auth token from logged in browser to caido>
chmod +x run.py
./run.py
```

# Approach to developing the Caido python client

I'm investigating if it's feasible to generate most, if not all of the client library from the graphql schema. The generate_code.py
function is my very naive implementation for doing so. At the moment it will communicate with your local caido instance, fetch
the schema and replaces all of the models in the caido/models directory.

For now I'm manually adding functions to the caido/queries.py file to perform queries against Caido. If you want to add a query, have
a look at this file yourself. You can leverage the generated caido/models for proper type completion.

To generate the models and test things out, I'm using this quick oneliner:
```
./generate_code.py && python3 -m pip install . && ./run.py
```
