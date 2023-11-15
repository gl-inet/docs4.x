# How can I know my device's WAN, LAN, 2.4G, 5G Mac addresses

The Mac addresses of our devices are unique for each connecting port, they can be found in WAN 1, WAN 2, LAN ports, 2.4G WiFi and 5G WiFi.

You can look up them by the following methods.

**Method 1**

## Finding the WAN Mac address from the label

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

You can find the WAN address on the back label of our device. For example the WAN Mac is: E4:95:6E:40:DB:A9 here.

**Method 2**

## Check them up in SSH cell

Please check [here](remote_ssh_to_router.md) for how to use SSH cell.

Please type **ifconfig** in the SSH cell.

### Find the ethernet ports

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

**eth0** is the WAN, which Mac Address is **94:83:C4:19:19:08**. 

If there is one more WAN port, there will be one more WAN Mac Address. For example, our GL-MT6000.

**eth1**, **eth2**, etc, are the LANs, which Mac Address is **94:83:C4:19:19:09**. 

There would be only one Mac Address even there are more than one LAN ports. For example, our GL-AXT1800, GL-AX1800, GL-MT6000.

### Find the wireless ports

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

**wlan0-1** is the 2.4G WiFi, which Mac Address is **96:83:C4:19:19:0B**.

**wlan1** is the 5G WiFi, which Mac Address is **94:83:C4:19:19:0A**.

## Usage Scenario

When you connect to some hotels, camping sites, campus, the network manager may ask your device's Mac address to register into his whitelist before.
You need to tell him the exact Mac address or addressed of your device in order for network access. You can use the above logic to tell him exactly all your Mac addresses of your device immediately.