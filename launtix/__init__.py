#!/usr/bin/env python3

__title__ = "launtix"
__author__ = "yunfachi"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2023 yunfachi"
__version__ = "0.1.0"

"""
from . import foo
=> import launtix.foo.bar

from .foo import *
=> import launtix.bar
"""

from .client import Client

from . import (
    api,
    utilities,
    types,
)