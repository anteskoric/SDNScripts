import os
#import random as rm
#import socket
#import struct

#This script is working
#TODO test it with 1500 packages
call_size = 50
packages = "1"
data_size = "5"
dest_ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5", "10.0.0.6", "10.0.0.8", "10.0.0.18", "10.0.0.42", "10.0.0.43",
       "10.0.0.44"]
sudoPassword = ''

for x in range(0, call_size):
    #random_src_ip = socket.inet_ntoa(struct.pack('>I', rm.randint(1, 0xffffffff)))
    for i in range(0, 10):
        dest_ip = dest_ips[i]
        os.system('echo %s|sudo -S %s' % (sudoPassword, "hping3 -c " + packages + " --icmp -p 7 " + "-d " + data_size + " --rand-source " + dest_ip))