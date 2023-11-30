#!/usr/bin/env python3

import asyncio
import aiohttp

from .types.csrf import CSRF
from .types.user import User

class Client:
    def __init__(self, cookie: str = None):
        self.cookie = cookie
        self.session = aiohttp.ClientSession(cookies={".ROBLOSECURITY": self.cookie})
        self.csrf = CSRF(self)
        self.user: User = self.fetch_user(466795326)

    async def fetch_user(self, id: int) -> User:
        return await User(self, id).update()

    async def close(self):
        await self.session.close()