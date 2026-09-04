import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def watch(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36 Edg/152.0.0.0"}
        response=requests.get(url,headers=headers,timeout=10)
        response.encoding="utf-8"
        bs=BeautifulSoup(response.text,"lxml")
        items =bs.select("div.section3 ul.on li a")
        title =bs.select_one("div.section3 li.on a").get_text(strip=True)
        data=[]
        for item in items[:3]:
            titles = item.select_one("h3").get_text(strip=True)
            urls = item.get("href")
            href = urljoin(url,urls)
            times = item.select_one("span").get_text(strip=True)
            data.append({"title":titles,"url":href,"times":times})
        return {
            "first_title":title,
            "items":data
        }
    except Exception as e:
        return {"first_title": None, "items": [], "error": str(e)}
if __name__ == '__main__':
    res=watch("https://www.ahszu.edu.cn/")
    print(res.get("first_title"))
    for idx, item in enumerate(res.get('items', []), 1):
        print(idx,item)
