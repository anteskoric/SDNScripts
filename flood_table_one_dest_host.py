import os

packages = "1000"
data_size = "5"
dest_ip = "10.0.0.3"
sudoPassword = ''

os.system('echo %s|sudo -S %s' % (sudoPassword, "hping3 --fast " + " --icmp -p 7 " + "-d " + data_size + " --rand-source " + dest_ip))
