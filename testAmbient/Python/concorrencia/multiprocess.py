from multiprocessing import Pool
import time
import requests

def f(url):
    response = requests.get(url, timeout=5)
    return response.text

if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://www.example.com',
        'http://www.example.com',
        'http://www.example.com',
        'http://www.example.com',
    ]
    with Pool(5) as p: 
        print(p.map(f, urls))
    end = time.time()
    print("Time elapsed: ", end - start)