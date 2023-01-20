#!/usr/bin/env python3

from caido import CaidoClient
from caido.models import Project
from os import environ

# Get this from the browser local storage. Eventually should implement oauth2.0 flow

try:
    AUTH_TOKEN = environ.get("CAIDO_AUTH_TOKEN")
except KeyError:
    print(
        f"""
        Please set AUTH_TOKEN in script or environment variable called 'CAIDO_AUTH_TOKEN'.

        Authentication is not yet implemented, you can grab the authorization token from your browsers
        local storage.
        """
    )
    exit(-1)


def main():
    """Main entrypoint Caido test script."""
    client = CaidoClient(AUTH_TOKEN)

    projects = client.query_projects()
    print(f"{len(projects)} projects found")

    current_project = client.query_current_project()
    print(f"Current project: {current_project}")

    runtime = client.query_runtime()
    print(f"{runtime.version=} {runtime.platform=} {runtime.available_update=}")


if __name__ == "__main__":
    main()
