from __future__ import annotations

from homeassistant.components.text import TextEntity
from homeassistant.components.number import NumberEntity
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

import time
import requests
api_url = "http://10.100.100.17:1025/"

DOMAIN = "ProPresenter"

def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([Slide_Notes()])


class Slide_Notes(TextEntity):
    """Representation of a text_input."""

    def __init__(self):
        self._attr_name = "Slide Notes"
        self._attr_unique_id = "text.propresenter_slide_notes"
        self.entity_id = "text.propresenter_slide_notes"
        self._attr_native_value = ""
        self._attr_device_class = "ProPresenter"

    def update(self) -> None:
        """
        Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        try:
            response = requests.get(api_url+"v1/status/slide",timeout=0.01)
            self._attr_native_value = str(response.json()['current']['notes'])
        except:
            pass
            
