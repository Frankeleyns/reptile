# demo 1
import os
from urllib import request

from bs4 import BeautifulSoup

if not os.path.exists('ItemImage'):
    os.mkdir('ItemImage')

currpath = os.path.realpath(__file__)
dir = os.path.dirname(currpath)
iI = os.path.join(dir,'ItemImage')


html = request.urlopen('https://pvp.qq.com/web201605/item.shtml').read().decode('gbk')
soup = BeautifulSoup(html,'lxml')
ul = soup.find_all('ul',{'class','clearfix herolist'})



for li in ul:
    imgs = li.find_all('img')
    for img in imgs:
        request.urlretrieve('https:'+img['src'], iI+'\\'+img['alt']+'.jpg' )
        print(iI+'\\'+img['alt'])
