import os
import requests
import time
import asyncio
 
urls = (
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
)
 
async def get_and_print(url):
    response = requests.get(url, timeout=5)
    print(response.text)
 
started = time.time()
for url in urls:
    asyncio.run(get_and_print(url))
end = time.time()
print("Time elapsed: ", end - started)

