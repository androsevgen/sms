import cx_Oracle
import os
import cx_Oracle
os.chdir('C://Users/AndrosE/PycharmProjects/conn/')

file = open("conf.py", "r")
print(file.read())




con = cx_Oracle.connect('login/passwords@ip/date_name')
print (con.version)
con.close()



