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

    async def get_agent_info(self, timeout: float = 120) -> AgentInfoResponse:
        """Return Fing agent info (only for fingbox and agent)"""
        url = f"{self._agent_url}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout)
        return AgentInfoResponse(response.raise_for_status().text)


    async def get_devices(self, timeout: float = 120) -> DeviceResponse:
        """Return devices discovered by Fing."""
        url = f"{self._api_url}/devices?auth={self._key}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout)
        return DeviceResponse(response.raise_for_status().json())

    async def get_contacts(self, timeout: float = 120) -> ContactResponse:
        """Return information about Fing contacts."""
        url = f"{self._api_url}/people?auth={self._key}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=timeout)
        return ContactResponse(response.raise_for_status().json())

