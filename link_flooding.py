import os

packages = "2000"
data_size = "120"
sourc_ip = "10.0.0.42"
dest_ip = "224.0.2.0"
sudoPassword = ''

os.system('echo %s|sudo -S %s' % (
sudoPassword, "hping3 --fast -c " + packages + " -p 6 " + "-d " + data_size + " -a " + sourc_ip + " " + dest_ip))
