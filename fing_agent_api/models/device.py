from typing import Any

class Device:
    """Class representing a device found by Fing."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize Device."""
        self._device_json = json

    @property
    def mac(self) -> str:
        """Return mac address."""
        return str(self._device_json["mac"])

    @property
    def ip(self) -> list[str]:
        """Return ip address."""
        return list[str](self._device_json["ip"])

    @property
    def active(self) -> bool:
        """Return state."""
        return self._device_json["state"] == "UP"

    @property
    def name(self) -> str | None:
        """Return name."""
        return (
            str(self._device_json.get("name"))
            if self._device_json.get("name") is not None
            else None
        )

    @property
    def type(self) -> str | None:
        """Return device type."""
        return (
            str(self._device_json.get("type"))
            if self._device_json.get("type") is not None
            else None
        )

    @property
    def make(self) -> str | None:
        """Return device maker."""
        return (
            str(self._device_json.get("make"))
            if self._device_json.get("make") is not None
            else None
        )

    @property
    def model(self) -> str | None:
        """Return device model."""
        return (
            str(self._device_json.get("model"))
            if self._device_json.get("model") is not None
            else None
        )

    @property
    def contactId(self) -> str | None:
        """Return contactId."""
        return (
            str(self._device_json.get("contactId"))
            if self._device_json.get("contactId") is not None
            else None
        )

    @property
    def first_seen(self) -> str | None:
        """Return first seen date-time."""
        return (
            str(self._device_json.get("first_seen"))
            if self._device_json.get("first_seen") is not None
            else None
        )

    @property
    def last_changed(self) -> str | None:
        """Return last changed date-time."""
        return (
            str(self._device_json.get("last_changed"))
            if self._device_json.get("last_changed") is not None
            else None
        )
