#coding=utf-8
import time
import threading
#from printers import printPink,printGreen
from multiprocessing.dummy import Pool
import MySQLdb

def mysql_connect(ip,username,password,port):
    crack =0
    try:
        db=MySQLdb.connect(ip,username,password,port=port)
        if db:
            crack=1
        db.close()
    except Exception, e:
        if e[0]==1045:
            print "%s mysql's %s:%s login fail" %(ip,username,password)
        else:
            print "connect %s mysql service at %s login fail " %(ip,port)
            crack=2
        pass
    return crack

def check(ip,port,time):
        results =[]
        try:
            d=open('plugins/conf/mysql.conf','r')
            data=d.readline().strip('\r\n')
            while(data):
                username=data.split(':')[0]
                password=data.split(':')[1]
                flag=mysql_connect(ip,username,password,port)
                if flag==2:
                    break
                if flag==1:
                    print("%s mysql at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))
                    results.append("%s mysql at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))
                data=d.readline().strip('\r\n')
        except Exception,e:
            print e
            pass
        if len(results) > 0:
            return 'YES|'+results
        else:
            return 'NO'

