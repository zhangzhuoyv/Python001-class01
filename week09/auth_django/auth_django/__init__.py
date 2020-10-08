# 项目内所有操作，都会先执行 项目的 __init__.py 内容
import pymysql
pymysql.install_as_MySQLdb() # pymysql 替换 默认的MySQLdb

# pip install pymysql