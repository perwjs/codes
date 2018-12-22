'''
修改pymysql模块下connections.py文件下的init方法,charset设置为utf8
'''
import urllib.request
import re
import pymysql


'''
将小说写入数控库
'''
class Sql(object):
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="pass",db="mydb")

    def add_novels(self,title,url):
        cursor = self.conn.cursor()
        cursor.execute("insert into titles(title,url) values ('%s','%s')" %(title,url))
        self.conn.commit()
        cursor.close()

class spider:
    def get_urls(self):
        url = "http://www.quanshuwang.com/map/1.html"
        headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().decode('gbk','ignore')
        bt1 = '<a href=".*?" target=".*?">(.*?)</a>'
        bt2 = '<a href="/book(.*?)" target=".*?">.*?</a>'
        titles = re.compile(bt1,re.S).findall(data)
        urls = re.compile(bt2,re.S).findall(data)
        return titles,urls

if __name__ == '__main__':
    sql = Sql()
    spider = spider()
    target = "http://www.quanshuwang.com"
    titles,urls = spider.get_urls()
    # print(urls[0:])
    gg = []
    for url in urls:
        url = target +'/book'+ url
        gg.append(url)
    tu = (titles,gg)
    for i in range(len(tu[0])):
        sql.add_novels(tu[0][i],tu[1][i])
