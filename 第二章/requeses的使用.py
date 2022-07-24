import requests



# r = requests.get('https://www.baidu.com')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text[:10])
# print(r.cookies)
# print(type(r.cookies))

#Get请求

# data={
#     'name':'germey',
#     'age':25
# }
# r = requests.get('https://www.httpbin.org/get',params=data)
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

#网页抓取
# import requests
#
#
# import re #regular expressions,正则表达式，RE
#
# pattern= re.compile('<h2.*?>(.*?)</h2>', re.S)
# r = requests.get('https://ssr1.scrape.center/')
# title = re.findall(pattern, r.text)
#
# print(title)
# print('正则表达式内容=','<h2.*?>(.*?)</h2>')
# print(type(title))

#抓取二进制数据
# import requests
#
# r = requests.get('https://scrape.center/favicon.ico')
# print(r.text)
# print(r.content)
#
# # 保存信息
# with open('favicon.ico','wb') as f:
#
#     f.write(r.content)

#添加请求头
# import requests
# header={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# r = requests.get('https://ssr1.scrape.center/', headers=header)
# print(r.text)

#post请求
# import requests
# data={'name':'lijianwei','age':'25'}
# r = requests.post('https://www.httpbin.org/post', data=data)
# print(r.text)

#响应
# import requests
#
#
#
# r = requests.get('https://ssr1.scrape.center/')
# print(type(r.status_code),r.status_code)
# print(type(r.headers),r.headers)
# print(type(r.cookies),r.cookies)
# print(type(r.history),r.history)

#高级用法-文件上传
# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('https://www.httpbin.org/post', files=files)
#
# print(r.text)

#cookie
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)
#
# print(r.cookies.items())

import requests


# headers={
#     'Cookie':'_octo=GH1.1.565412294.1657595649; tz=Asia/Shanghai; _device_id=453e52720a05e0f26b056a025d74489f; preferred_color_mode=light; has_recent_activity=1; user_session=xrJLCNBCe5rUakoteMng8LhqT46t_U7-4akcq1iTmFAO61SZ; __Host-user_session_same_site=xrJLCNBCe5rUakoteMng8LhqT46t_U7-4akcq1iTmFAO61SZ; tz=Asia/Shanghai; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=lijianwei652; _gh_sess=HjHyNdNwTUdWsFoi4EFcLOb1KZpTM1AgtvbRVCyQv5y46MCd810FfuwdqO5wYixDNhF6sJRjJpE8tMrpUg53CtKb2KFVJRQ771Xhovwwc7N0LbQbH008nV2NpJc4peyRv3TqiMjlwRgS+I0DAGZQkvBHCcF3JyuSLc/os3KMSqqt34YWsncDqAbQEbNnrr3yG5aqXUb+mCpWFnOgaZwOZqGjdVkBZGd6jX7W/u/VpjeNID5idlcK3iiWnXC+cRy5fJFRoPu4OJ41wggTEnMUIsYMdSPx6Svma8E0eNsRThmBxZI6ua8Rx5Ij15zQZl/BDbOVZcrybcdPvbxjADoIPClAaTfq+DwVfk93znJ0MBdiDSnF6qRtQB/qIwae07qZ8Pr+qQuumDTnl79DAIUfkiCN/Y/XpxNCgaVp62/toZcOcSG9KLjkj8w54/ZPZ/D533KFPQ==--TLOsH2Ki+j/K3mVX--VRP/nWPbRSsQdLQvR6ss/Q==',
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
# r = requests.get('https://github.com/',headers=headers)
#
# print(r.text)
# print(r.cookies)

# cookies='_octo=GH1.1.565412294.1657595649; tz=Asia/Shanghai; _device_id=453e52720a05e0f26b056a025d74489f; preferred_color_mode=light; has_recent_activity=1; user_session=xrJLCNBCe5rUakoteMng8LhqT46t_U7-4akcq1iTmFAO61SZ; __Host-user_session_same_site=xrJLCNBCe5rUakoteMng8LhqT46t_U7-4akcq1iTmFAO61SZ; tz=Asia/Shanghai; color_mode={"color_mode":"auto","light_theme":{"name":"light","color_mode":"light"},"dark_theme":{"name":"dark","color_mode":"dark"}}; logged_in=yes; dotcom_user=lijianwei652; _gh_sess=HjHyNdNwTUdWsFoi4EFcLOb1KZpTM1AgtvbRVCyQv5y46MCd810FfuwdqO5wYixDNhF6sJRjJpE8tMrpUg53CtKb2KFVJRQ771Xhovwwc7N0LbQbH008nV2NpJc4peyRv3TqiMjlwRgS+I0DAGZQkvBHCcF3JyuSLc/os3KMSqqt34YWsncDqAbQEbNnrr3yG5aqXUb+mCpWFnOgaZwOZqGjdVkBZGd6jX7W/u/VpjeNID5idlcK3iiWnXC+cRy5fJFRoPu4OJ41wggTEnMUIsYMdSPx6Svma8E0eNsRThmBxZI6ua8Rx5Ij15zQZl/BDbOVZcrybcdPvbxjADoIPClAaTfq+DwVfk93znJ0MBdiDSnF6qRtQB/qIwae07qZ8Pr+qQuumDTnl79DAIUfkiCN/Y/XpxNCgaVp62/toZcOcSG9KLjkj8w54/ZPZ/D533KFPQ==--TLOsH2Ki+j/K3mVX--VRP/nWPbRSsQdLQvR6ss/Q=='
# jar=requests.cookies.RequestsCookieJar()
# headers={
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
# }
#
# for cookie in cookies.split(';'):
#     key,value=cookie.split('=',1)
#     jar.set(key,value)
# r = requests.get('https://github.com/', cookies=jar, headers=headers)
# print(r.text)

 #--------------session维持

# import requests
# requests.get('https://www.httpbin.org/cookies/set/number/123456789')
# r=requests.get('https://www.httpbin.org/cookies')
# print(r.text)
#
# s = requests.Session()
# s.get('https://www.httpbin.org/cookies/set/number/1234567890')
# r=s.get('https://www.httpbin.org/cookies')
# print(r.text)

#--------SSL证书
# import requests
# import logging
#
# logging.captureWarnings(True)
#
# response = requests.get('https://ssr2.scrape.center/',verify=False)
#
#-------超时设置
# import requests
#
# c = requests.get('https://www.httpbin.org/get', timeout=(0.5))
# print(c.text)

#身份认证----
# import requests
# from requests_oauthlib import OAuth1
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('https://ssr3.scrape.center/', auth=HTTPBasicAuth('admin', 'admin'))
# print(r.status_code)

# import requests
# from requests_oauthlib import OAuth1
# url='https://api.twitter.com/1.1/account/verify_credentials.json'
# auth=OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET'
# )
# print(requests.get(url,auth=auth))

#----------代理设置
# import requests
# proxies={
#     'http':'http://10.10.10.10:1080',
#     'https':'https://user:password@10.10.10.10:1080'
# }
# requests.get('https://www.httpbin.org/get',proxies=proxies)

#----socks代理
# import requests
# proxies={
#     'http':'socks5://user:password@host:port'
# }
# requests.get('http://www.httpbin.org/get',proxies=proxies)

#---preparedRequest
from requests import  Request,Session

url = 'https://www.httpbin.org/post'
data={'name':'germey'}
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
req = Request('POST', url, data=data, headers=headers)
s=Session()
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
