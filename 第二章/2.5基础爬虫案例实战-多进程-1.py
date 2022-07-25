import re

import requests
import logging
from urllib.parse import urljoin

#配置日志
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s --%(levelname)s:%(message)s')
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE=10


#抓取页面
def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        logging.info('get invalid status code %s while scraping %s',
                     response.status_code,url)
    except requests.RequestException:
        logging.info('error occurred while scraping %s',url,
                     exc_info=True)
#列表页爬取，page为页码
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url) #传入URL，返回爬取后的信息，文本信息。


#解析页面
#输入第一季页面信息，提炼二级页面链接。并返回链接。
#输入：一级页面，
#返回：一级页面内包含的二级页面的URL

def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?).*?class="name">')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s',detail_url)
        yield detail_url

if __name__ == '__main__':
    page_1_content=scrape_page(BASE_URL)
    for i in range(TOTAL_PAGE):
        scrape_index(i)
    for i in page_2_url:
        print(i)

