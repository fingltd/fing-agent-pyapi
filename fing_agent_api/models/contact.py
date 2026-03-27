from __future__ import annotations

from typing import Any

from .contact_info import ContactInfo


class Contact:
    """Class representing a Fing contact."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize Contact."""
        self._contact_json = json

    def _get_str(self, key: str) -> str | None:
        """Return a string value from the JSON data, or None if missing."""
        value = self._contact_json.get(key)
        return str(value) if value is not None else None

    @property
    def state_change_time(self) -> str:
        """Return state change time."""
        return str(self._contact_json.get("stateChangeTime"))

    @property
    def contact_info(self) -> ContactInfo:
        """Return contact info."""
        return ContactInfo(json=self._contact_json["contactInfo"])

    @property
    def current_state(self) -> str | None:
        """Return current state."""
        return self._get_str("currentState")

    @property
    def presence_device_details(self) -> str | None:
        """Return presence device details."""
        return self._get_str("presenceDeviceDetails")
