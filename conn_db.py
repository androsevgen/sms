import cx_Oracle
import os, sys, json
import conf


j1 = json.loads(conf
                .logdate)
login = j1["login"]
passwords = j1["passwords"]
ip = j1["ip"]
date_name = j1["date_name"]

try:
    c_con = login + "/" + passwords + "@" + ip + "/" + date_name
    #con = cx_Oracle.connect('login/passwords@ip/date_name')
    con = cx_Oracle.connect(c_con)
    print("Connection successful")
except:
    print("Connection not successful")

