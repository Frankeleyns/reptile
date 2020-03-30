# demo 1
import os
from urllib import request
from bs4 import BeautifulSoup


# 爬取装备图片
if not os.path.exists('ItemImage'):
    os.mkdir('ItemImage')

currpath = os.path.realpath(__file__)
dir = os.path.dirname(currpath)
igm_dir = os.path.join(dir,'ItemImage')


html = request.urlopen('https://pvp.qq.com/web201605/item.shtml').read().decode('gbk')
print('爬取装备图片')
soup = BeautifulSoup(html,'lxml')
ul = soup.find_all('ul',{'class','clearfix herolist'})


for li in ul:
    imgs = li.find_all('img')
    for img in imgs:
        local = igm_dir+'\\'+img['alt']
        request.urlretrieve('https:'+img['src'], local +'.jpg' )
        print(local)



# 爬取英雄图片
if not os.path.exists('HeroImage'):
    os.mkdir('HeroImage')

currpath = os.path.realpath(__file__)
dir = os.path.dirname(currpath)
igm_dir = os.path.join(dir,'HeroImage')


html = request.urlopen('https://pvp.qq.com/web201605/herolist.shtml').read().decode('gbk')
print('爬取英雄图片')
soup = BeautifulSoup(html,'lxml')
ul = soup.find_all('ul',{'class','herolist clearfix'})


for li in ul:
    imgs = li.find_all('img')
    for img in imgs:
        local = igm_dir+'\\'+img['alt']
        request.urlretrieve('https:'+img['src'], local +'.jpg' )
        print(local)

