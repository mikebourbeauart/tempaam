
import os
import sys


__version__ = "1.0.0"

_resource = None

PATH = os.path.abspath(__file__)
DIRNAME = os.path.dirname(PATH)
PACKAGES_PATH = os.path.join(DIRNAME, "packages")
RESOURCES_PATH = os.path.join(DIRNAME, "resourceS")
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


def version():
    """
    Return the current version of the Studio Library

    :rtype: str
    """
    return __version__



