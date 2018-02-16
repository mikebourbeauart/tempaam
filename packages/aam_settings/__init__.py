import os
import sys
import logging


import utils

DEFAULT_FILE_TYPE = "mayaBinary"
SETTINGS_PATH = utils.localPath("LibraryItem.json")

_settings = None

def readSettings():
    """
    Return the local settings from the location of the SETTING_PATH.

    :rtype: dict
    """
    return utils.readJson(SETTINGS_PATH)

def settings():
    """
    Return the local settings for importing and exporting an animation.

    :rtype: studiolibrary.Settings
    """
    global _settings

    if not _settings:
        _settings = readSettings()

    # Shared options
    _settings.setdefault("namespaces", [])
    _settings.setdefault("namespaceOption", "file")

    _settings.setdefault("iconToggleBoxChecked", True)
    _settings.setdefault("infoToggleBoxChecked", True)
    _settings.setdefault("optionsToggleBoxChecked", True)
    _settings.setdefault("namespaceToggleBoxChecked", True)

    # Anim options
    _settings.setdefault('byFrame', 1)
    _settings.setdefault('fileType', DEFAULT_FILE_TYPE)
    _settings.setdefault('currentTime', False)
    _settings.setdefault('connectOption', False)
    _settings.setdefault('showHelpImage', False)
    _settings.setdefault('pasteOption', "replace")

    # Pose options
    _settings.setdefault("keyEnabled", False)
    _settings.setdefault("mirrorEnabled", False)

    # Mirror options
    #_settings.setdefault("mirrorOption", mutils.MirrorOption.Swap)
    _settings.setdefault("mirrorAnimation", True)

    return _settings