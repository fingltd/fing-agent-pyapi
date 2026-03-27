"""Fing Agent API library."""

from __future__ import annotations

import httpx

from .models import ContactResponse, DeviceResponse, AgentInfoResponse


class FingAgent:
    """Fing Agent API class.

    Accepts an optional httpx.AsyncClient for connection reuse.
    When no client is provided, a temporary one is created per request.
    """

    def __init__(
        self,
        ip: str,
        port: int,
        key: str,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        """Initialize Fing API object."""
        self._api_url = f"http://{ip}:{port}/1"
        self._agent_url = f"http://{ip}:44444/"
        self._key = key
        self._client = client

    async def _get(self, url: str, timeout: float) -> httpx.Response:
        """Perform a GET request, reusing the injected client if available."""
        if self._client is not None:
            response = await self._client.get(url, timeout=timeout)
        else:
            async with httpx.AsyncClient() as client:
                response = await client.get(url, timeout=timeout)
        return response.raise_for_status()

    async def get_agent_info(self, timeout: float = 120) -> AgentInfoResponse:
        """Return Fing agent info (only for fingbox and agent)."""
        response = await self._get(self._agent_url, timeout)
        return AgentInfoResponse(response.text)

    async def get_devices(self, timeout: float = 120) -> DeviceResponse:
        """Return devices discovered by Fing."""
        url = f"{self._api_url}/devices?auth={self._key}"
        response = await self._get(url, timeout)
        return DeviceResponse(response.json())

    async def get_contacts(self, timeout: float = 120) -> ContactResponse:
        """Return information about Fing contacts."""
        url = f"{self._api_url}/people?auth={self._key}"
        response = await self._get(url, timeout)
        return ContactResponse(response.json())

