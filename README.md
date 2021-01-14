## SDN Pen Testing HAW Hamburg

The scripts are used in the HAW Hamburg lab for pen testing of the HAW Hamburg networking test car.

## Usage

The scripts use [hping3](https://linux.die.net/man/8/hping3) to send the packages, therefore, you should install the tool on the machine where you run the scripts. It should be inculed as standard in most distributions.

Use Python 2.7.17 or 3.6.9 to execute the scripts.

It is necessary to have sudo rights for script execution.
We recommend to run the scripts on the core-NUC2.

#### Usage example:
```python
sudo python3 {script_name}.py
```
For more details see the comments in the scripts, and be careful while using *faster* and *flood*!

## Documentation
*flood_table.py*:


### Scenario:
The SDN controller creates a new reactive flow when a new connection between two IP addresses has been requested, e.g. by a ping packet, as the white list only allows this.\
We know that the switch can have a maximum of 2000 flows in the table at the same time, this means that an attack can be performed that "overfills" this table.\
Existing reactive flows will be dropped from the table after 30 seconds of inactivity.
If the table is full, no new flows can be added.

### Observations:
An increase of entries on the "Reactive Flow Rules" table can be observed, quickly rising to a number beyond the maximum number of rules that can be processed by this system. Similarly the Topology view will show at first a strain on established connections before some of them fail, resulting in a loss of communication. After a small amount of time seemingly random connections can be seen being established, deviating from the pre-attack layout. New connections can only be established once there is actually room in the flow table again.\
Due to the load imposed on the system, the ONOS UI may lag or even crash and/or the browser may hang or crash.\
After either the reactive rules have timed out or have been manually cleared, the system will go  back to normal operation.

***
*link_flooding.py*:

### Scenario:
There is a static flow in the network that allows UDP packages to be sent over port 6 to IP address 224.0.2.0.\
This rule is exploited to send a lot of packages over the link. These packets are not forwarded through the controller, which results in only the link being attacked in isolation. If many UDP packets are sent, this leads to utilization of the link.\
The packages can no longer be sent over the link.

### Observations:
A traffic increase can be observed on both the link between switches, the connection between the sending network unit and the switch it is connected to as well as the receiving network unit and the switch it is connected to.
The more packages are send, the higher the load on these three connections. As such it its possible to overload or put a strain on the link if more than one network unit is sending an increased amount of traffic.

***
*controller_flooding.py*:

### Scenario:
An attempt is made to overload the controller, therefore many TCP packets are sent via the controller.\
Since TCP packets are not forwarded by the SDN controller, they are filtered. This means that the controller is busy with this process and if we can send a lot of TCP packets, this leads to overloading of the controller.\
As a result no new reactive flows will be created, limiting network ability.

### Observations:
Trying to establish a new reactive flow while the attack is active will be unsuccessful.
Existing reactive flows will keep working until they time out. Refreshing them is still possible.

It should be noted that the controller does not report the correct number of packages received when compared to the number of packages send by the script.
This is likely because of some internal filter that limits the amount of senseless TCP connection requests.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)