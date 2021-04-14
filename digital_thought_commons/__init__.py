from . import *

with open("version", "r") as fh:
    version_info = fh.read()

__version__ = version_info
