from urllib.parse import urlunparse
from urllib.parse import urlsplit,urljoin

# data=['https:','www.baidu.com','index.html','user','a=6','comment']
# print(urlunparse(data))

#urlsplit
# result=urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
# print(type(result))
# print(result.scheme,result[0])

#urljoin
# print(urljoin('https://www.baidu.com','FAQ.html'))
# print(urljoin('https://www.baidu.com','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('https://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
# print(urljoin('https://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('https://www.baidu.com?wd=abc','https://cuiqingcai.com/index.php'))
# print(urljoin('https://www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com','?category=2#comment'))
# print(urljoin('www.baidu.com#comment','?category=2'))

# urlencode
# from urllib.parse import urlencode
# params={
#     'name':'germey',
#     'age':25
# }
# base_ur='https://www.baidu.com?'
# url=base_ur+urlencode(params)
# print(url)
# print(type(url))

#parse_qs
# from urllib.parse import  parse_qs
#
# query = 'name=germey&age=25'
# print(parse_qs(query))
# print(type(parse_qs(query)))

#parse_qsl
# from    urllib.parse import  parse_qsl
#
# query = 'name=germey&age=25'
# print(parse_qsl(query))

#quote

# from urllib.parse import quote
# keyword='壁纸'
# url='https://www.baidu.com/?wd='+quote(keyword)
# print(url)
#
#unquote
# from urllib.parse import unquote
#
# url = 'https://www.baidu.com/?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url))

import re
# content='            abcd          a '
# print(content)
# result=re.sub('\s+','',content)
# print(result.strip())
# # result.strip() //去除首位指定字符串，留空则去掉空格。

#complie 将字符串编译成表达式

content1='2019-12-15 12:00'
content2='2019-12-22 13:00'
content3='2019-12-15 14:20'

pattern=re.compile('\d{2}:\d{2}')
result1=re.sub(pattern,'',content1)
result2=re.sub(pattern,'',content2)
result3=re.sub(pattern,'',content3)
print(result1)
print(result2)
print(result3)


