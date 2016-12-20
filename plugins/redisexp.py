#coding=utf-8
import time
import threading
from threading import Thread
from Queue import Queue
import redis

def check(ip,port,timeout):
        try:
            r=redis.Redis(host=ip,port=port,db=0,socket_timeout=timeout)
            r.dbsize()
            print "ok"
            return 'YES|'+'redis vul'+ip
        except Exception,e:
            print e
            pass
