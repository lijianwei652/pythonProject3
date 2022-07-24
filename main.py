import  requests
url="https://www.baidu.com/s?wd=镜像"
dic={
    
}
respo =requests.get(url)
print(respo.text)