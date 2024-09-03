from typing import Any
from .contact import Contact

class ContactResponse:
    """Class representing the People response data."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize the People response object."""
        self._network_id = str(json["networkId"])
        self._last_change_time = str(json["lastChangeTime"])
        self._contacts = [Contact(contact_json) for contact_json in json["people"]]

    @property
    def network_id(self) -> str:
        """Return network ID."""
        return self._network_id

    @property
    def last_change_time(self) -> str:
        """Return the last change time."""
        return self._last_change_time

    @property
    def contacts(self) -> list[Contact]:
        """Return Fing's contacts."""
        return self._contacts
