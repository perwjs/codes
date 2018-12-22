import urllib.request
import re
import random
'''
将聚美优品的图片下载
'''

class spider:
    uapools = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        " Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        ""

    ]
    def ua(self):
        headers  = ("User-Agent",random.choice(self.uapools))
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)


    def get_pictures(self):

        try:
            key = "口红"
            keycode = urllib.request.quote(key)
            for i in range(1,45):
                url = "http://search.jumei.com/?filter=0-11-"+str(i)+"&search="+keycode
                self.ua()
                data = urllib.request.urlopen(url=url).read().decode('utf-8','ignore')
                reg = '<img original="(.*?)"'
                imglist = re.compile(reg,re.S).findall(data)
                for j in range(8,len(imglist)):
                    try:
                        imgurl = imglist[j]
                        localfile = "C:/Users/user/Desktop/spiders/spideer/淘宝爬取/聚美优品/"+str(i)+"-"+str(j)+".jpg"
                        urllib.request.urlretrieve(imgurl,filename=localfile)
                    except Exception as err:
                        pass
        except Exception as err:
            pass





if __name__ == '__main__':
    spider = spider()
    spider.get_pictures()