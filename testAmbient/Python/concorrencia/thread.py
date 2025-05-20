import os
import requests
import time
from multiprocessing.pool import ThreadPool as Pool
 
urls = (
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
    'http://www.example.com',
)
 
def get_and_print(url):
    response = requests.get(url, timeout=5)
    print(response.text)
 
started = time.time()
pool = Pool(processes=os.cpu_count())
pool.map(get_and_print, urls)
end = time.time()
print("Time elapsed: ", end - started)