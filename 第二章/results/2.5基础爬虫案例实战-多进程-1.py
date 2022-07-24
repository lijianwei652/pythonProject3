import requests
import logging
import re
from urllib.parse import urljoin

#配置日志-复习
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s:%(message)s')

BASE_URL='https://ssr1.scrape.center'
TOTAL_PAGE=10

#实现爬虫
def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,exc_info=True)

#定义列表页爬取
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

#解析列表页
def parse_index(html):
    pattern = re.compile('<a*?href="(.*?)".*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s',detail_url)
        yield  detail_url

    