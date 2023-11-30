#!/usr/bin/env python3

class CSRF:
    def __init__(self, client: "launtix.client.Client"):
        self.csrf_token = None
        # Don't use `self.session = client.session` because it creates a new object instead of referencing the existing one.
        self.client = client

    """
    Get the current CSRF token or fetch a new one if it is not set.
    """
    async def get(self) -> str:
        if self.csrf_token is None:
            await self.update()
        return self.csrf_token
    
    """
    Update the CSRF token by fetching a new one.
    """
    async def update(self):
        self.csrf_token = await self.fetch()

    """
    Fetch a new CSRF token.
    """
    async def fetch(self) -> str:
        async with self.client.session.post("https://catalog.roblox.com/") as response:
            return response.headers["X-CSRF-TOKEN"]