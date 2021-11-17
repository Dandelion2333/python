#!/usr/bin/env python2.7
#-*- coding: UTF-8 -*-

#功能：输入n则获取编号，输入其他则不处理

import socket
import string

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 6000))
print(s.recv(1024).decode())

data = "client"
while True:
    data = raw_input("client_input:")
    if data == "n":
        data = "client_need_new_number"
        s.send(data.encode())
        print(s.recv(1024).decode())
    else:
        if data == "exit":
            s.send(data.encode())
            break  
        continue  

if s.recv(1024).decode() == "recv_exit":
    s.close()