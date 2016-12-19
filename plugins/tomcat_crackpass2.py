__author__ = 'wilson'
import requests
import base64
import threading
import time
import socket
from multiprocessing.dummy import Pool
socket.setdefaulttimeout(8)

def tomcat_connect(ip,port,username,password):
    try:
        url='http://'+ip+':'+str(port)
        url_get=url+'/manager/html'
        creak=0
        r=requests.get(url_get,timeout=8)
        if r.status_code==401:
            header={}
            login_pass=username+':'+password
            header['Authorization']='Basic '+base64.encodestring(login_pass).strip()
            r=requests.get(url_get,headers=header,timeout=8)
            if r.status_code==200:
                print("%s tomcat service at %s has weaken password!!-------%s:%s\r\n" %(ip,port,username,password))
                creak=1
            else:
                print "%s tomcat service 's %s:%s login fail " %(ip,username,password)
        else:
            print 'not find tomcat login page!'
            creak=2

    except Exception,e:
        print e
        pass
    return creak


def check(ip,port,time):
    resluts=[]
    try:
        d=open('plugins/conf/tomcat.conf','r')
        data=d.readline().strip('\r\n')
        while(data):
            username=data.split(':')[0]
            password=data.split(':')[1]
            flag=tomcat_connect(ip,port,username,password)
            if flag==1:
                resluts.append(data)
            if flag==2:
                break
            data=d.readline().strip('\r\n')
    except Exception,e:
        print e
        pass
    if len(resluts) > 0:
        return 'YES|tomcat weak pass'+resluts
    else:
        return 'NO'



