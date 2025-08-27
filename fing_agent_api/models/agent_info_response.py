from typing import Any

import xml.etree.ElementTree as ET

class AgentInfoResponse:
    """Class representing the AgentInfo response data."""


    def __init__(self, response: str) -> None:
        """Initialize the AgentInfo response object."""

        ns = {'upnp': 'urn:schemas-upnp-org:device-1-0'}
        responseXml = ET.fromstring(response)

        if responseXml is None:
            return

        ip_element = responseXml.find('upnp:URLBase', ns)
        if ip_element != None:
            self._ip = ip_element.text.rsplit(':', 1)[0]
            
        device = responseXml.find('upnp:device', ns)

        friendly_name_element = device.find('upnp:friendlyName', ns)
        if friendly_name_element != None:
            self._friendly_name = friendly_name_element.text

        model_name_element = device.find('upnp:modelName', ns)
        if model_name_element != None:
            self._model_name = model_name_element.text

        device_type_element = device.find('upnp:deviceType', ns)
        if device_type_element != None:
            self._device_type = device_type_element.text.removeprefix('urn:fing:').removeprefix('urn:domotz:')

        manufacturer_element = device.find('upnp:manufacturer', ns)
        if manufacturer_element != None:
            self._manufacturer = manufacturer_element.text


        services = device.find('upnp:serviceList', ns).findall('upnp:service', ns)
        for s in services:
            stype_element = s.find('upnp:serviceType', ns)
            if stype_element is None:
                continue

            if stype_element.text.startswith('urn:fing:device:fingagent:mac:'):
                self._agent_id = stype_element.text.removeprefix('urn:fing:device:fingagent:mac:')
            elif stype_element.text.startswith('urn:domotz:device:fingbox:mac:'):
                self._agent_id = stype_element.text.removeprefix('urn:domotz:device:fingbox:mac:')
            elif stype_element.text.find(':active:1') != 0:
                self._agent_state = 'active'
            elif stype_element.text.find(':inactive:') != 0:
                self._agent_state = 'inactive'
            elif stype_element.text.find(':unknown:1') != 0:
                self._agent_state = 'unknown'

    @property
    def ip(self) -> str:
        """Return network ID."""
        return self._ip
    
    @property
    def model_name(self) -> str:
        """Return model name."""
        return self._model_name
    
    @property
    def state(self) -> str:
        """Return state."""
        return self._agent_state
    
    @property
    def agent_id(self) -> str:
        """Return agent id."""
        return self._agent_id
    
    @property
    def friendly_name(self) -> str:
        """Return friendly name."""
        return self._friendly_name
    
    @property
    def device_type(self) -> str:
        """Return device type."""
        return self._device_type
    
    @property
    def manufacturer(self) -> str:
        """Return manufacturer."""
        return self._manufacturer