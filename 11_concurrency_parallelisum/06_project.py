import requests
from threading import Thread
import time

def download(url):
    print(f"Download of {url} started.")
    res = requests.get(url)
    print(f"{url} Downloaded. size : {len(res.content)} bytes.")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/jpg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

threads = []
start = time.time()

for url in urls:
    t = Thread(target=download,args=(url,))

    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print(f"total time taken is:{end-start:.2f} seconds.")

