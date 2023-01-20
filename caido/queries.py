from typing import Protocol, List, Dict
from .models import Project, Runtime


class CaidoClientProtocol(Protocol):
    """Protocol for CaidoClient.

    This protocol creates type stubs for the CaidoClient class so we can properly
    do type hints on our Mixin classes
    """

    def _query(self, payload: Dict) -> Dict:
        ...


class CaidoQueryMixin(Protocol):
    """Queries that can be performed by Caido.

    This class is intended to be used as a Mixin by CaidoClient and is automatically generated from the graphql schema.
    """

    def query_projects(
        self: CaidoClientProtocol,
    ) -> List[Project]:
        """Queries projects."""
        payload = {
            "query": """
            {
                projects {
                    id
                    name
                    version
                    updatedAt
                    createdAt
                    path
                    size
                }
            }
        """
        }
        response = self._query(payload)

        return [Project.from_graphql(project) for project in response["projects"]]

    def query_current_project(
        self: CaidoClientProtocol,
    ) -> Project:
        """Queries current project."""
        payload = {
            "query": """
            {
                currentProject {
                    id
                    name
                    version
                    updatedAt
                    createdAt
                    path
                    size
                }
            }
        """
        }
        response = self._query(payload)
        return Project.from_graphql(response["currentProject"])

    def query_runtime(
        self: CaidoClientProtocol,
    ) -> Runtime:
        """Queries runtime."""
        payload = {
            "query": """
            {
                runtime {
                    version
                    platform
                    availableUpdate {
                        version
                        links {
                            display
                            platform
                            link
                        }
                        releasedAt
                    }
                }
            }
        """
        }
        response = self._query(payload)
        return Runtime.from_graphql(response["runtime"])
