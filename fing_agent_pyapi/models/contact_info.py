from typing import Any

class ContactInfo:
    """Class representing contact's information."""

    def __init__(self, json: dict[str, Any]) -> None:
        """Initialize ContactInfo."""
        self._contact_info_json = json

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
        return (
            str(self._contact_info_json.get("pictureImageData"))
            if self._contact_info_json.get("pictureImageData") is not None
            else None
        )

    @property
    def picture_url(self) -> str | None:
        """Return picture url."""
        return (
            str(self._contact_info_json.get("pictureUrl"))
            if self._contact_info_json.get("pictureUrl") is not None
            else None
        )

