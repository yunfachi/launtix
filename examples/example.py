#!/usr/bin/env python3

import launtix
import asyncio
import aiohttp

client = launtix.Client(".ROBLOSECURITY cookie here")

async def main():
    print("CSRF token:", await client.csrf.get())

    print("Creator earnings for a 593 R$ sale:", launtix.utilities.creator_earnings.calculate(593))
    print("Creator earnings for a 4093 R$ sale:", launtix.utilities.calculate_creator_earnings(4093))

    print("User balance:", await client.fetch_user(466795326))
    print("Group balance:", await launtix.api.currency.group(client, 12601519))

    await client.close()

asyncio.get_event_loop().run_until_complete(main())