#!/usr/bin/python
#_*_coding:utf-8_*_

import urllib
import re
import time
import os

##### http://blog.sina.com.cn/s/articlelist_1191258123_0_7.html

def gethtml(url) : 
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getallhtml() :
    page = 1
    urlpage = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_'+ str(page) +'.html'
    #while page <= 7 :
        #page = page + 1
    print 'page = ' , page, urlpage
    return gethtml(urlpage)

def getblogUrllist(html) :
    reg = r'a title.* href=.(http.*\.html)'
    urlreg = re.compile(reg)
    blogurllist = re.findall(urlreg, html)
    #print blogurllist
    return blogurllist

def getblog(blogurl) :
    blogcontent = urllib.urlopen(blogurl).read()
    reg = r'h2 id.*class=.*>(.*)<.h2>'
    titlereg = re.compile(reg)
    titles = re.findall(titlereg, blogcontent)
    print 'titles === ', titles
    filepath = os.path.join(os.path.dirname(__file__), 'blog')
    if os.path.exists(filepath):
        pass
    else :
        os.mkdir(filepath)
    ## 每次获取到的titles 都是一个值
    for filename in titles :
        if filename == '.' :
            pass
        else :
            print 'filename ==== ', unicode(filename, "utf-8")
            # reg2 = u'px.>\r\n([\u4e00-\u9fa5]+)<.DIV>'.encode('cp936')
            reg2 = u'(.*)<.DIV>'
            blogreg = re.compile(reg2)
            blog = re.findall(blogreg, blogcontent)
            print ' blogreg === ' , blogreg , ' == blog == ', blog
            content = ''
            for i in blog :
                content = content + i + '\r\n'
                print 'content === ',  content
                print 'downloading...', blog
                open(filepath + os.path.sep + unicode(filename, "utf-8")   + '.txt', 'w+').write(content)
        #time.sleep(10)    

if __name__ == '__main__' :
    blogurls = getblogUrllist(getallhtml())
    for blogurl in blogurls :
        print 'blogurl == ', blogurl
        print '*' * 40
        getblog(blogurl)
