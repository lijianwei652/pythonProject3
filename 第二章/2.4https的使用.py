import httpx
import requests
# response1=requests.get('https://spa16.scrape.center')
# print(response1.text)

# headers={
#
#    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
#
# response=httpx.get('https://spa16.scrape.center',headers=headers)
# print(response.status_code)
# print(response.headers)
# print(response.text)

import  httpx
# url='https://spa16.scrape.center'
# client = httpx.Client(http2=True)
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# response = client.get(url,headers=headers)
# print(response.status_code)
# print(response.text)

#Client对象

# headers={'User-agent':'my-app/0.0.1'}
# with httpx.Client(headers=headers) as client:
#     response =client.get('https://www.httpbin.org/get')
#     print(response.json())
#     print(response.json()['headers']['User-Agent'])

# 等价于
# client=httpx.Client()
# try:
#     response=client.get('https://www.httpbin.org/get')
# finally:
#     client.close()

# 支持HTTP/2.0
# import httpx
#
# client = httpx.Client(http2=True)
# response = client.get('https://www.httpbin.org/get')
# print(response.text)
# print(response.http_version)

#6.支持异步请求
import httpx
import asyncio

async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response=await client.get(url)
        print(response.text)
print("执行完毕")
if __name__=='__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://httpbin.org/get'))

