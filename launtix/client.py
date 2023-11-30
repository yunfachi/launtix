#!/usr/bin/env python3

import asyncio
import aiohttp

from .types.csrf import CSRF

class Client:
    def __init__(self, cookie: str = None):
        self.cookie = cookie
        self.session = aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.cookie})
        self.csrf = CSRF(self)