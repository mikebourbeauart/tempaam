
import os
import sys


__version__ = "1.0.0"

_resource = None
_publish

PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
PACKAGES_PATH = os.path.join(DIRNAME, "packages")
RESOURCE_PATH = os.path.join(DIRNAME, "resource")
HELP_URL = "http://www.studiolibrary.com"


LIBRARY_WIDGET_CLASS = None


def setup(path):
    """
    Setup the packages that have been decoupled from the Studio Library.

    :param path: The folder location that contains all the packages.
    :type path: str

    :rtype: None
    """
    if os.path.exists(path) and path not in sys.path:
        sys.path.append(path)


setup(PACKAGES_PATH)


import mbqt


#from figuringoutapp.main import main


# Wrapping the following functions for convenience
app = studioqt.app


def version():
    """
    Return the current version of the Studio Library

    :rtype: str
    """
    return __version__


def resource():
    """
    Return a resource object for getting content from the resource folder.

    :rtype: studioqt.Resource
    """
    global _resource

    if not _resource:
        _resource = studioqt.Resource(RESOURCE_PATH)

    return _resource
