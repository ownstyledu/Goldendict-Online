#!/usr/bin/env python
# coding:utf-8
# @author:dudapeng

import sys
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding('utf-8')

def searchword(word):
    # url = 'http://dict.youdao.com/w/eng/marina'
    url = 'http://dict.youdao.com/w/eng/' + word
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    delDiv = soup.find('div', id='doc')
    scontainer = soup.find('div', id='scontainer')

    # 删除广告，删除上方空白
    delDiv2 = scontainer.contents[1]
    del delDiv2.contents[1]
    del scontainer['id']
    # 删除搜索框
    del delDiv.contents[1]


    # 去掉更多短语的按钮
    try:
        p_collapse = soup.select('.wordGroup.collapse')
        w_collapse = soup.select('.wt-container.wt-collapse')
        for i in p_collapse:
            i['class'] = 'wordGroup'
        for i in w_collapse:
            i['class'] = '.wt-container'
        soup.select('div.more')[0].clear()
    except:
        pass

    # 展示例句
    # example_tag1 = soup.select("a[rel='#bilingual']")
    try:
        example_tag2 = soup.select("a[rel='#originalSound']")[0]
        example_tag3 = soup.select("a[rel='#authority']")[0]
        example_tag2['class'] = 'tab-current'
        example_tag3['class'] = 'tab-current'
    except:
        pass

    # 广告
    try:
        ads = soup.select("#ads")
        footer = soup.select("#c_footer")
        ads[0].clear()
        footer[0].clear()
    except:
        pass

    print soup

if __name__ == '__main__':

    searchword(sys.argv[1])
    # searchword('marina')


