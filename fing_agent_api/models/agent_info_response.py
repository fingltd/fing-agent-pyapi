from __future__ import annotations

import xml.etree.ElementTree as ET


class AgentInfoResponse:
    """Class representing the AgentInfo response data."""

    def __init__(self, response: str) -> None:
        """Initialize the AgentInfo response object."""
        self._ip: str | None = None
        self._friendly_name: str | None = None
        self._model_name: str | None = None
        self._device_type: str | None = None
        self._manufacturer: str | None = None
        self._agent_id: str | None = None
        self._agent_state: str | None = None

        ns = {'upnp': 'urn:schemas-upnp-org:device-1-0'}
        response_xml = ET.fromstring(response)

        ip_element = response_xml.find('upnp:URLBase', ns)
        if ip_element is not None and ip_element.text is not None:
            self._ip = ip_element.text.rsplit(':', 1)[0]

        device = response_xml.find('upnp:device', ns)
        if device is None:
            return

        friendly_name_element = device.find('upnp:friendlyName', ns)
        if friendly_name_element is not None:
            self._friendly_name = friendly_name_element.text

        model_name_element = device.find('upnp:modelName', ns)
        if model_name_element is not None:
            self._model_name = model_name_element.text

        device_type_element = device.find('upnp:deviceType', ns)
        if device_type_element is not None and device_type_element.text is not None:
            self._device_type = device_type_element.text.removeprefix('urn:fing:').removeprefix('urn:domotz:')

        manufacturer_element = device.find('upnp:manufacturer', ns)
        if manufacturer_element is not None:
            self._manufacturer = manufacturer_element.text

        service_list = device.find('upnp:serviceList', ns)
        if service_list is None:
            return

        for s in service_list.findall('upnp:service', ns):
            stype_element = s.find('upnp:serviceType', ns)
            if stype_element is None or stype_element.text is None:
                continue

            if stype_element.text.startswith('urn:fing:device:fingagent:mac:'):
                self._agent_id = stype_element.text.removeprefix('urn:fing:device:fingagent:mac:')
            elif stype_element.text.startswith('urn:domotz:device:fingbox:mac:'):
                self._agent_id = stype_element.text.removeprefix('urn:domotz:device:fingbox:mac:')
            elif ':active:1' in stype_element.text:
                self._agent_state = 'active'
            elif ':inactive:' in stype_element.text:
                self._agent_state = 'inactive'
            elif ':unknown:1' in stype_element.text:
                self._agent_state = 'unknown'

    @property
    def ip(self) -> str | None:
        """Return network IP."""
        return self._ip

    @property
    def model_name(self) -> str | None:
        """Return model name."""
        return self._model_name

    @property
    def state(self) -> str | None:
        """Return state."""
        return self._agent_state

    @property
    def agent_id(self) -> str | None:
        """Return agent id."""
        return self._agent_id

    @property
    def friendly_name(self) -> str | None:
        """Return friendly name."""
        return self._friendly_name

    @property
    def device_type(self) -> str | None:
        """Return device type."""
        return self._device_type

    @property
    def manufacturer(self) -> str | None:
        """Return manufacturer."""
        return self._manufacturer