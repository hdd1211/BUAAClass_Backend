import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
# 前面两行是重要的，后面这些是测试用的，这里打印出mysql的版本，显示在程序运行界面上

db = pymysql.connect(host='localhost', user='root', password='12345', db='test')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('DATABASE VERSION IS: %s' % data)

db.close()
