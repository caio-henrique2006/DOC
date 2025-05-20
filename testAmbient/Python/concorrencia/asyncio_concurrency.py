import asyncio
import time
from aiohttp import ClientSession
import requests
 
urls = (
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
)
 
async def get_and_print(session, url):
    async with session.get(url) as response:
        print(await response.text())
 
async def fetch(loop, urls):
    async with ClientSession(loop=loop) as session:
        tasks = (get_and_print(session, url) for url in urls)
        await asyncio.gather(*tasks, return_exceptions=True)
 
started = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(fetch(loop, urls))
end = time.time()
print("Time elapsed: ", end - started)