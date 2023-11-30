#!/usr/bin/env python3

async def user(client, user_id: int) -> int:
    async with client.session.get(f"https://economy.roblox.com/v1/users/{user_id}/currency") as response:
        return await (response.json())["robux"]

async def group(client, group_id: int) -> int:
    async with client.session.get(f"https://economy.roblox.com/v1/groups/{group_id}/currency") as response:
        return (await response.json())["robux"]