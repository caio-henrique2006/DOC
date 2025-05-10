from multiprocessing import Pool
import time
import requests

def f(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    start = time.time()
    urls = [
        'http://www.americanas.com',
        'http://www.submarino.com',
        'http://www.shoptime.com',
        'http://www.soubarato.com',
    ]
    with Pool(5) as p:
        print(p.map(f, urls))
    end = time.time()
    print("Time elapsed: ", end - start)