import requests
from config import URL_KEY
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
def fetch_notices():
    try:
        session=requests.session()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
        }

        session.headers.update(headers)
        retry = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[404,500,502,503,504],
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        response = session.get(url=URL_KEY, timeout=10)
        response.encoding = "utf-8"
        bs = BeautifulSoup(response.text, "lxml")
        items = bs.select("div.section3 ul.on li a")
        data = []
        for item in items[:6]:
            titles = item.select_one("h3").get_text(strip=True)
            urls = item.get("href")
            href = urljoin(URL_KEY, urls)
            times = item.select_one("span").get_text(strip=True)
            data.append({"title": titles, "url": href, "times": times})
        return data
    except Exception as e:
        print(f"爬取异常: {e}")
        return []
if __name__ == '__main__':
    res = fetch_notices()
    print(f"共抓取 {len(res)} 条公告")
    for idx, item in enumerate(res, 1):
        print(f"{idx}. {item['title']} | {item['times']} | {item['url']}")




