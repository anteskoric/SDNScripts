import os

# This script will overload the link, a lot of "big" packages will be send

dest_ips_left = ["10.0.0.1", "10.0.0.2", "10.0.0.6", "10.0.0.8", "10.0.0.42"]
dest_ips_right = ["10.0.0.3", "10.0.0.4", "10.0.0.5"]
sudoPassword = ''

for i in range(0, len(dest_ips_left) - 1):
    # dest_io = dest_ips_right[i]
    dest_ip = dest_ips_left[i]
    os.system('echo %s|sudo -S %s' % (
    sudoPassword, "hping3 " + "--flood " + "--icmp " + "-p 7 " + dest_ip))
