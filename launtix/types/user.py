#!/usr/bin/env python3

class User:
    def __init__(self, client: "launtix.client.Client", id: int):
        self.client = client
        self.id: int = id
        
        self.name: str = None
        self.display_name: str = None
        self.description: str = None
        self.created: str = None
        self.is_banned: bool = None
    
    """

    """
    async def update(self):
        response = await self.fetch()
        self.name = response["name"]
        self.display_name = response["displayName"]
        self.description = response["description"]
        self.created = response["created"]
        self.is_banned = response["isBanned"]

    """
    
    """
    async def fetch(self) -> dict:
        async with self.client.session.get(f"https://users.roblox.com/v1/users/{self.id}") as response:
           return await response.json()