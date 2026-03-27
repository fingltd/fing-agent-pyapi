from __future__ import annotations

from typing import Any


class Device:
    """Class representing a device found by Fing."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize Device."""
        self._device_json = json

    def _get_str(self, key: str) -> str | None:
        """Return a string value from the JSON data, or None if missing."""
        value = self._device_json.get(key)
        return str(value) if value is not None else None

    @property
    def mac(self) -> str:
        """Return mac address."""
        return str(self._device_json["mac"])

    @property
    def ip(self) -> list[str]:
        """Return ip address."""
        return list(self._device_json["ip"])

    @property
    def active(self) -> bool:
        """Return state."""
        return self._device_json["state"] == "UP"

    @property
    def name(self) -> str | None:
        """Return name."""
        return self._get_str("name")

    @property
    def type(self) -> str | None:
        """Return device type."""
        return self._get_str("type")

    @property
    def make(self) -> str | None:
        """Return device maker."""
        return self._get_str("make")

    @property
    def model(self) -> str | None:
        """Return device model."""
        return self._get_str("model")

    @property
    def contact_id(self) -> str | None:
        """Return contact ID."""
        return self._get_str("contactId")

    @property
    def first_seen(self) -> str | None:
        """Return first seen date-time."""
        return self._get_str("first_seen")

    @property
    def last_changed(self) -> str | None:
        """Return last changed date-time."""
        return self._get_str("last_changed")
