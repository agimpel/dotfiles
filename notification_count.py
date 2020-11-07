#!/usr/bin/env python3
import sys
import socket
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect("/tmp/rofi_notification_daemon")
client.sendall(bytes("num",'utf-8'))

val = client.recv(32)
val = val.decode('utf-8')
l = val.split('\n',2)
result = str(l[0])

if result == "0":
    print("")
    exit()

print(" "+result)

