from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

# URL
base_url = ""
url = base_url + "https://finance.naver.com/news/mainnews.naver"

# URL Open
res = req.urlopen(url)

# BeautifulSoup
soup = BeautifulSoup(res, "html.parser")

# News link 
news = soup.select("#contentarea_left > div.mainNewsList._replaceNewsLink > ul.newsList > li.block1")
for i in news:
    sub = i.select_one("dl > dd.articleSubject > a")
    print(sub.text.strip())
    print("-" * 50)
    summary = i.select_one("dl > dd.articleSummary")
    print(summary.text.strip())
    print("=" * 50)
