"""Fing Agent API library."""

import httpx

from .models import ContactResponse, DeviceResponse, AgentInfoResponse


class FingAgent:
    """Fing Agent API class."""

    def __init__(self, ip: str, port: int, key: str) -> None:
        """Initialize Fing API object."""
        self._api_url = f"http://{ip}:{port}/1"
        self._agent_url = f"http://{ip}:44444/"
        self._key = key
        self._client: httpx.AsyncClient | None = None

    def _get_client(self) -> httpx.AsyncClient:
        """Return a reusable httpx client, creating one if needed."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient()
        return self._client

    async def close(self) -> None:
        """Close the underlying HTTP client."""
        if self._client is not None and not self._client.is_closed:
            await self._client.aclose()
            self._client = None

    async def __aenter__(self) -> "FingAgent":
        """Enter async context manager."""
        return self

    async def __aexit__(self, *args) -> None:
        """Exit async context manager."""
        await self.close()

    async def get_agent_info(self, timeout: float = 120) -> AgentInfoResponse:
        """Return Fing agent info (only for fingbox and agent)."""
        url = f"{self._agent_url}"
        client = self._get_client()
        response = await client.get(url, timeout=timeout)
        return AgentInfoResponse(response.raise_for_status().text)

    async def get_devices(self, timeout: float = 120) -> DeviceResponse:
        """Return devices discovered by Fing."""
        url = f"{self._api_url}/devices?auth={self._key}"
        client = self._get_client()
        response = await client.get(url, timeout=timeout)
        return DeviceResponse(response.raise_for_status().json())

    async def get_contacts(self, timeout: float = 120) -> ContactResponse:
        """Return information about Fing contacts."""
        url = f"{self._api_url}/people?auth={self._key}"
        client = self._get_client()
        response = await client.get(url, timeout=timeout)
        return ContactResponse(response.raise_for_status().json())