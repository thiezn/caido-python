import httpx
from typing import Dict
from .queries import CaidoQueryMixin


class CaidoClient(CaidoQueryMixin):
    """Interact with a given Caido instance."""

    def __init__(
        self,
        auth_token: str,
        host: str = "127.0.0.1",
        port: int = 8080,
        scheme="http",
        graphql_path="graphql",
    ):
        self.host = host
        self.port = port

        if scheme not in ("http", "https"):
            raise ValueError(
                f"Scheme should be either http or https, got {scheme} instead."
            )
        self.scheme = scheme
        self.graphql_path = graphql_path

        self.auth_token = auth_token

    @property
    def base_url(self) -> str:
        """Generate base url to GraphQL endpoint."""
        return f"{self.scheme}://{self.host}:{self.port}/{self.graphql_path}"

    def _query(self, payload: Dict) -> Dict:
        """Run GraphQL query."""
        headers = {
            "User-Agent": "Python Caido Client",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip",
            "Authorization": f"Bearer {self.auth_token}",
        }
        with httpx.Client(headers=headers) as client:
            response = client.post(self.base_url, json=payload)

        return self._parse_response(response)

    def _parse_response(self, response: httpx.Response) -> Dict:
        """Parse a response coming back from GraphQL."""
        if not response.is_success:
            raise IOError(f"Oops: {response.status_code}\n{response.content}")

        json_response = response.json()
        if "errors" in json_response:
            raise IOError(f"Oops: {json_response['errors']}")

        return json_response["data"]

    def get_runtime_version(self):
        """Retrieve the Caido runtime version."""
        payload = {
            "query": """
            {
                runtime {
                    version
                }
            }
            """
        }

        response = self._query(payload)
        return response["runtime"]

    # def list_projects(self):
    #     """List all defined projects."""
    #     payload = {
    #         "query": """
    #         {
    #             projects {
    #                 id
    #                 name
    #                 version
    #                 updatedAt
    #                 createdAt
    #                 path
    #                 size
    #             }
    #         }
    #     """
    #     }
    #     response = self._query(payload)
    #     return response["projects"]
