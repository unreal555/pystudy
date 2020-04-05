#!/bin/py
#   -*-coding:utf-8-*-
import  os
import 学习requests
import socket
import re
import threading


def checkProxy(address):
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((address[0],int(address[1])))
        print(address[0]+'代理有效')
        with open('proxy.txt', 'a') as f:
            f.write(address[0] + ':' + address[1] + '\n')
    except:
        print(address[0]+'代理失效')
    finally:
        sock.close()


def getList(url):
     page=学习requests.get(url).text

     reg='<td data-title="IP">(.*?)</td>.*?<td data-title="PORT">(.*?)</td>'

     for address in re.findall(reg, page, re.S):
         checkProxy(address)


getList('https://www.kuaidaili.com/free/inha/2/')
