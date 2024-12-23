from enum import IntEnum, Enum

import xbmc


class _KodiMagicValues:
    WEATHER_WINDOW_ID = 12600  # see https://kodi.wiki/view/Weather_addons at "Required output"
    ADDON_INFO_PATH_ID = "path"
    ADDON_INFO_ADDON_ID = "id"
    ADDON_INFO_NAME_ID = "name"
    REGION_TEMPERATURE_UNIT_ID = "tempunit"
    REGION_WIND_SPEED_UNIT_ID = "windspeedunit"


class KodiAddonStrings(IntEnum):
    SETTINGS_REQUIRED = 30010
    HOMEASSISTANT_UNAUTHORIZED = 30011
    HOMEASSISTANT_UNREACHABLE = 30013
    HOMEASSISTANT_UNEXPECTED_RESPONSE = 30014
    ADDON_SHORT_NAME = 30200


class KodiLogLevel(Enum):
    DEBUG = xbmc.LOGDEBUG
    INFO = xbmc.LOGINFO
    WARNING = xbmc.LOGWARNING
    ERROR = xbmc.LOGERROR
    CRITICAL = xbmc.LOGFATAL
