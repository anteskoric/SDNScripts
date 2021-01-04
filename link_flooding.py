import os

# This script is working, needs to be tested
# This rout needs to exist before the script can be executed
# sudo route -n add -net 224.0.2.4 netmask 255.255.255.255 dev eno1
packages = "2000"
data_size = "120"
sourc_ip = "10.0.0.42"
dest_ip = "224.0.2.4"
sudoPassword = ''

#sudo hping3 -2 --destport 51004 --baseport 50005 -k -I eno1 --fast -c 10 -d 120 -a 10.0.0.42 224.0.2.4
os.system('echo %s|sudo -S %s' % (
sudoPassword, "hping3 -2 --destport 51004 --baseport 50005 -k -I eno1 --fast -c " + packages + "-d " + data_size + " -a " + sourc_ip + " " + dest_ip))
