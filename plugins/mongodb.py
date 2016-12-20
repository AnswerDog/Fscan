#coding=utf-8
import time
import threading
#from printers import printPink,printRed,printGreen
from multiprocessing.dummy import Pool
import socket
socket.setdefaulttimeout(8)
import pymongo


results = []

def mongoDB_connect(ip,username,password,port):
    crack=0
    try:
        connection=pymongo.Connection(ip,port)
        db=connection.admin
        db.collection_names()
        results.append('%s mongodb service at %s allow login Anonymous login!!\r\n' %(ip,port))
        crack=1

    except Exception,e:
        if e[0]=='database error: not authorized for query on admin.system.namespaces':
            try:
                db.authenticate(username,password)
                crack=2
            except Exception,e:
                crack=3

        else:
            print('%s mongodb service at %s not connect' %(ip,port))
            crack=4
    return crack



def check(ip,port):
        try:
            d=open('plugins/conf/mongodb.conf','r')
            data=d.readline().strip('\r\n')
            while(data):
                username=data.split(':')[0]
                password=data.split(':')[1]
                flag=mongoDB_connect(ip,username,password,port)
                if flag==2:
                    print("%s mongoDB at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))
                    _ = "%s mongoDB at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password)
                    results.append(_)
                data=d.readline().strip('\r\n')
        except Exception,e:
            print e
            pass
        if len(results) > 0:
            return 'YES|'+results
        else:
            return 'NO'

