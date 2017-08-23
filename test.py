# coding=utf-8
#!/usr/local/bin/python3.6
import  pymysql

#打开数据库链接
db = pymysql.connect("localhost","root","","test")

#使用cursor 方法创建一个游标对象 cursor
cursor = db.cursor()

#使用execute() 方法执行sql查询 VERSION()查询数据库版本
cursor.execute("SELECT VERSION()")

#使用fetchone() 方法获取单条数据
data = cursor.fetchone()

print("Database version : %s " % data)

db.close()