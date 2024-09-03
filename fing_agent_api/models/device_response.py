from typing import Any
from .device import Device

class DeviceResponse:
    """Class representing the Device response data."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize the Device response object."""
        self._network_id = str(json.get("networkId")) if json.get("networkId") is not None else None
        self._devices = [Device(device_json) for device_json in json["devices"]]

    @property
    def network_id(self) -> str | None:
        """Return network ID."""
        return self._network_id

    @property
    def devices(self) -> list[Device]:
        """Return all the device found by Fing."""
        return self._devices
