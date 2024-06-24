import urllib.request as req
from bs4 import BeautifulSoup
import time

while(True):
    url = 'https://news.nate.com/rank/interest?sc=ent'
    res = req.urlopen(url)

    soup = BeautifulSoup(res, 'html.parser')

    # #newsContents > div > div.postRankSubjectList.f_clear > div > div > a > span.tb > h2
    h2_list = soup.select("#newsContents > div > div.postRankSubjectList.f_clear > div > div > a > span.tb > h2")

    # #postRankSubject > ul:nth-child(1) > li:nth-child(1) > a > h2
    h2_list += soup.select('#postRankSubject > ul > li > a > h2')

    for i, h2 in enumerate(h2_list):
        print(f"{i+1}. {h2.string}")

    time.sleep(60 * 60 * 24)