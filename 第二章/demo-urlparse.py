from    urllib.parse import  urlparse



result = urlparse(
    'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E8%AF%95&fenlei=256&rsv_pq=d19b4ef40000ad56&rsv_t=8ca6U35KfteXNpXTy0djqGTWdRMiwFU%2FWLwXv1HQfLzebLGfNf8IjoXM8mY&rqlang=cn&rsv_enterhttps://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E6%B5%8B%E8%AF%95&fenlei=256&rsv_pq=d19b4ef40000ad56&rsv_t=8ca6U35KfteXNpXTy0djqGTWdRMiwFU%2FWLwXv1HQfLzebLGfNf8IjoXM8mY&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E6%25B5%258B%25E8%25AF%2595&rsp=6&inputT=1324&rsv_sug4=1324=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=%25E6%25B5%258B%25E8%25AF%2595&rsp=6&inputT=1324&rsv_sug4=1324')
print(type(result))
print(result)
