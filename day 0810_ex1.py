import urllib.request as req
import urllib.parse
from bs4 import BeautifulSoup


# 파이썬, 자바, 자바스크립트 출력
# search_addr = "http://book.daum.net/search/bookSearch.do?query="
# src=["자바","파이썬","자바스크립트"]
#
# for word in src:
#     search_word = input("검색어를 입력하세요 : ")
#     if word == search_word :
#         search_word = urllib.parse.quote(search_word)
#         url = search_addr + search_word
#         myreq = req.Request(url)
#         html_data = req.urlopen(url).read()
#         data = BeautifulSoup(html_data, "html.parser")
#         print(data)
#         print("=" * 50 + "검색완료" + "=" * 50)


search_addr = "http://book.daum.net/search/bookSearch.do?query="
src = ["자바", "파이썬", "자바스크립트"]
for word in src:
    search_word = input("검색어를 입력하세요(자바,파이썬,자바스크립트) : ")
    if word == search_word :
        search_word = urllib.parse.quote(search_word)
        url = search_addr + search_word
        myreq = req.Request(url)
        html_data = req.urlopen(url).read()
        data = BeautifulSoup(html_data, "html.parser")
        price=data.select("#page_body > form > ul > li > dl > dd.price > div > span.prc > strong")
        for p in price:
            mp=p.string
        title = data.select("#page_body > form > ul > li > dl > dt > a")
        for t in title:
            mt=t.string

            print(mt, mp)
        # for r in myres:
        #    print(r)
    print("=" * 50 + "검색완료" + "=" * 50)


        # price=data.select("#page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dd.price > div > span.prc")
        # print(price)

# http://book.daum.net/search/bookSearch.do?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC
# http://book.daum.net/search/bookSearch.do?query=%EC%9E%90%EB%B0%94

# 파이썬
# page_body > form > ul > li > dl > dd.price > div > span.prc > strong
# page_body > form:nth-child(6) > ul > li:nth-child(2) > dl > dd.price > div > span.prc > strong


# 자바
# page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dd.price > div > span.prc
# page_body > form:nth-child(6) > ul > li:nth-child(2) > dl > dd.price > div > span.prc > strong
# page_body > form:nth-child(6) > ul > li:nth-child(3) > dl > dd.price > div > span.prc > strong


# 자바스크립트

# page_body > form:nth-child(6) > ul > li:nth-child(1) > dl > dd.price > div > span.prc > strong
# page_body > form:nth-child(6) > ul > li:nth-child(2) > dl > dd.price > div > span.prc > strong
# page_body > form:nth-child(6) > ul > li:nth-child(5) > dl > dd.price > div > span.prc > strong

