from bs4 import BeautifulSoup
import urllib.request as req
import re

url1="http://www.m-i.kr/news/articleView.html?idxno=444122"
url2="http://www.m-i.kr/news/articleView.html?idxno=443984"
src_file_name1=open('url1.txt')
src_file_name2=open('url2.txt')


def get_text(url):
    src=req.urlopen(url)
    bs=BeautifulSoup(src, "lxml", from_encoding='utf-8')
    text=""
    for item in bs.find_all('div', id='articleBody'):
        text = text + str(item.find_all(text=True))
    print(text)
    return text

def main1():
    open(src_file_name1, 'w')
    open(src_file_name2, 'w')
    text1=get_text(url1)
    text2=get_text(url2)
    src_file_name1.write(text1)
    src_file_name2.write(text2)
    src_file_name1.close()
    src_file_name2.close()


def clean_text(urlText):
    cleaned_text=re.sub('[a-zA-Z]', "", urlText)
    cleaned_text=re.sub('[<>\'\{\}\(\).;:+\-_]', "", cleaned_text)
    return cleaned_text

input_text1=open('url1.txt', 'r')
input_text2=open('url2.txt', 'r')
output_text1=open('url1_cleaned.txt')
output_text2=open('url2_cleaned.txt')

def main2():


    return

if __name__ == "__main__":
    main1()
    main2()