#coding=utf-8
import time
import threading
from printers import printPink,printGreen
from multiprocessing.dummy import Pool
import socket
socket.setdefaulttimeout(8)
import pymssql



def mssql_connect(ip,username,password,port):
    crack =0
    try:
        db=pymssql.connect(host=str(ip)+','+str(port),user=username,password=password)
        if db:
            crack=1
        db.close()
    except Exception, e:
        print "%s sql service 's %s:%s login fail " %(ip,username,password)
    return crack


def check(ip,port):
        results = []
        try:
            d=open('conf/mssql.conf','r')
            data=d.readline().strip('\r\n')
            while(data):
                username=data.split(':')[0]
                password=data.split(':')[1]
                flag=mssql_connect(ip,username,password,port)
                if flag==1:
                    print("%s mssql at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))
                    results.append("%s mssql at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))

                data=d.readline().strip('\r\n')
        except Exception,e:
            print e
            pass
        if len(results) > 0:
            return 'YES|'+results
        else:
            return 'NO'