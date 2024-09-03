from typing import Any
from .contact_info import ContactInfo

class Contact:
    """Class representing a Fing contact."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize Contact."""
        self._contact_json = json

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
        return (
            str(self._contact_json.get("currentState"))
            if self._contact_json.get("currentState") is not None
            else None
        )

    @property
    def presence_device_details(self) -> str | None:
        """Return presence device details."""
        return (
            str(self._contact_json.get("presenceDeviceDetails"))
            if self._contact_json.get("presenceDeviceDetails") is not None
            else None
        )
