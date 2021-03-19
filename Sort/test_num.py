import numpy
from bs4 import BeautifulSoup
from lxml.html import parse
from urllib.request import urlopen
import pandas

if __name__ == '__main__':
    # 测试打开html文件
    with open('./test.html', 'r', encoding='utf-8') as f:
        Soup = BeautifulSoup(f.read(), 'html.parser')
        test_text = Soup.text
