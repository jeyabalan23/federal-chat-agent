# Shared async helper functions
import asyncio
import aiohttp

async def fetch_async(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
