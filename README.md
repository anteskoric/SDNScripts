## SDN Pen Testing HAW Hamburg

This scripts are used in the HAW Hamburg lab for pen testing of the HAW Hamburg networking test car.

## Usage

The scripts use [hping3](https://linux.die.net/man/8/hping3) to send the packages, therefore, you should install the tool on the machine where you run the scripts.

Use Python 2.7.17 or 3.6.9 to execute the scripts.

You should start the scripts on the core-NUC2, with sudo rights.

```python
sudo python3 {script_name}.py
```
Also see the comments in the scripts for more details, and be careful while using flood and faster!

## Documentation
flood_table.py:

The SDN controller creates a new reactive flow when a new connection between two IP addresses has been created, e.g. by a ping packet, as the white list only allows this.\
We know that the switch can have 2000 flows in the table at the same time, this means that an attack can be performed that "overfills" this table.\
Existing reactive flows will be dropped from the table, this will cause the communication from the remote reactive flows to stop working and the one reactive flow cannot be installed or created.

link_flooding.py:

There is a static flow in the network that allows UDP packages to be sent over port 6 to IP address 224.0.2.0.\
This rule is exploited to send a lot of packages over the link. These packets are not forwarded through the controller, which results in only the link being attacked in isolation. If many UDP packets are sent, this leads to utilization of the link.\
The packages can no longer be sent over the link.

controller_flooding.py:

An attempt is made to overload the controller, therefore many TCP packets are sent via the controller.\
Since the TCP packets are not forwarded by SDN controller, they are filtered. This means that the controller is busy with this process and we can send a lot of TCP packets, which leads to the overload of the controller.\
The Reactive flows will stop working.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)