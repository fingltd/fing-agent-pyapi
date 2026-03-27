from __future__ import annotations

from typing import Any


class ContactInfo:
    """Class representing contact's information."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize ContactInfo."""
        self._contact_info_json = json

    def _get_str(self, key: str) -> str | None:
        """Return a string value from the JSON data, or None if missing."""
        value = self._contact_info_json.get(key)
        return str(value) if value is not None else None

    @property
    def contact_id(self) -> str:
        """Return contact ID."""
        return str(self._contact_info_json.get("contactId"))

    @property
    def display_name(self) -> str:
        """Return name."""
        return str(self._contact_info_json.get("displayName"))

    @property
    def contact_type(self) -> str:
        """Return type."""
        return str(self._contact_info_json.get("contactType"))

    @property
    def picture_image_data(self) -> str | None:
        """Return image (Base64 encoded)."""
        return self._get_str("pictureImageData")

    @property
    def picture_url(self) -> str | None:
        """Return picture url."""
        return self._get_str("pictureUrl")

