# How can I know my device's WAN, LAN, 2.4G, 5G Mac addresses

The Mac addresses of our devices are unique for each connecting port, they are arranging in sequence of hexadecimal order.

The sequence is 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E.

## Finding the WAN Mac address

![wan_lan_wifi](https://static.gl-inet.com/docs/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

You can find the WAN address on the back label of our device. For example the WAN Mac is: E4:95:6E:40:DB:A9 here.

## Calculate the LAN, 2.4G and 5G Mac addresses

The LAN Mac address is the WAN +1, therefore the result is E4:95:6E:40:DB:AA  (9 + 1 =A)

The 2.4G Mac address is the WAN +2 therefore the result is E4:95:6E:40:DB:AB (9 + 2 =B)

The 5G Mac address is the WAN +3 therefore the result is E4:95:6E:40:DB:AC (9 + 3 =C)

## Usage Scenario

When you connect to some hotels, camping sites, campus, the network manager may ask your device's Mac address to register into his whitelist before.
You need to tell him the exact Mac address or addressed of your device in order for network access. You can use the above logic to tell him exactly all your Mac addresses of your device immediately.