# GL.iNet OpenThread Border Router Codelabs

## **Application Scenario**

GL.iNet OTBR is factory-configured with Scenario 1 by default. Users need to configure the upstream interface for the backbone router according to their own application scenarios on the web Admin Panel -> THREAD MESH -> Advanced -> Backbone Routers.

### Direct Connection.

Scenario 1:  PC/mobile phone connects OTBR directly.

![direct connection](https://static.gl-inet.com/docs-iot/en/tutorials/openthread_border_router_codelabs/direct_connection.png){class="glboxshadow"}

### Indirect Connection

Scenario 2: PC/mobile phone and OTBR connect to the same upstream WiFi AP.

![indirect connection](https://static.gl-inet.com/docs-iot/en/tutorials/openthread_border_router_codelabs/indirect_connection.png){class="glboxshadow"}

## **Bi-directional IPv6 connectivity and DNS-based service discovery.**

This experiment uses the following topology diagram

- Ubuntu 20.04.4
- NRF52840 USB dongle（[ot-nrf52840 - 2023-02-15-d88076e](https://github.com/openthread/ot-nrf528xx/commit/c00d1812d3494c6a2f4f074685341e6e30195e9d)）
- ot-br-posix - 2022-11-08-d910392

![direct connection](https://static.gl-inet.com/docs-iot/en/tutorials/openthread_border_router_codelabs/direct_connection.png){class="glboxshadow"}

### Step 1: Create a Thread network.

```
root@GL-S200:~# uci set glipv6.lan.mode='relay'
root@GL-S200:~# uci commit glipv6
root@GL-S200:~# /etc/init.d/gl_ipv6 restart
root@GL-S200:~# uci set otbr.otbr.enable=1
root@GL-S200:~# uci commit otbr

echo "net.ipv6.conf.wpan0.accept_ra=1" >>/etc/sysctl.conf
sysctl -p /etc/sysctl.conf

root@GL-S200:~# ot-ctl dataset init new
Done
root@GL-S200:~# ot-ctl dataset commit active
Done
root@GL-S200:~# ot-ctl dataset active
Active Timestamp: 1
Channel: 18
Channel Mask: 0x07fff800
Ext PAN ID: a1fce8946f2f9b1d
Mesh Local Prefix: fd50:5ff6:fd1b:325b::/64
Network Key: e67446d4e450ad76cd3ad5472530d410
Network Name: OpenThread-ee97
PAN ID: 0xee97
PSKc: 42743e8b67c06353cd038520a0ab8b7f
Security Policy: 672 onrc
Done
root@GL-S200:~# ot-ctl ifconfig up
Done
root@GL-S200:~# ot-ctl thread start
Done
root@GL-S200:~# ot-ctl state
leader
Done
root@GL-S200:~# ot-ctl dataset active -x
0e080000000000010000000300001235060004001fffe00208a1fce8946f2f9b1d0708fd505ff6fd1b325b0510e67446d4e450ad76cd3ad5472530d410030f4f70656e5468726561642d656539370102ee97041042743e8b67c06353cd038520a0ab8b7f0c0402a0f7f8
Done
root@GL-S200:~# ot-ctl netdata show
Prefixes:
fd15:5b2d:647f:1::/64 paos low c400
Routes:
fd15:5b2d:647f:2:0:0::/96 sn low c400
fda1:fce8:946f:9b1d::/64 s med c400
Services:
44970 5d fd505ff6fd1b325b84ab8a51482f2df7d11f s c400
44970 01 31000500000e10 s c400
Done
root@GL-S200:~# ot-ctl ipaddr
fd50:5ff6:fd1b:325b:0:ff:fe00:fc11
fd50:5ff6:fd1b:325b:0:ff:fe00:fc38
fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4
fd50:5ff6:fd1b:325b:0:ff:fe00:fc10
fd50:5ff6:fd1b:325b:0:ff:fe00:fc00
fd50:5ff6:fd1b:325b:0:ff:fe00:c400
fd50:5ff6:fd1b:325b:84ab:8a51:482f:2df7
fe80:0:0:0:3488:80b2:ca62:867d
Done
```

Check the connectivity of OTBR on your phone/PC.

```
$ ping -6 -c1 fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4
PING fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4(fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4) 56 data bytes
64 bytes from fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4: icmp_seq=1 ttl=64 time=0.996 ms

--- fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.996/0.996/0.996/0.000 ms
```

### Step 2: Configure the SRP client terminal device.

To be executed on NRF52840.

```
> dataset set active 0e080000000000010000000300001235060004001fffe00208a1fce8946f2f9b1d0708fd505ff6fd1b325b0510e67446d4e450ad76cd3ad5472530d410030f4f70656e5468726561642d656539370102ee97041042743e8b67c06353cd038520a0ab8b7f0c0402a0f7f8
Done
> ifconfig up
Done
> thread start
Done
> state
child
Done
> netdata show
Prefixes:
fd15:5b2d:647f:1::/64 paos low fffe
Routes:
fd15:5b2d:647f:2:0:0::/96 sn low fffe
fda1:fce8:946f:9b1d::/64 s med fffe
Services:
44970 5d fd505ff6fd1b325b84ab8a51482f2df7d11f s fc10
44970 01 31000500000e10 s fc11
Done
> ipaddr
fd15:5b2d:647f:1:75cd:be97:fd26:f3b9
fd50:5ff6:fd1b:325b:0:ff:fe00:c401
fd50:5ff6:fd1b:325b:27af:b1fc:9225:4134
fe80:0:0:0:3873:7703:285d:38eb
Done
```

Check the Thread Device connectivity on the mobile phone/PC.

```
$ ping -6 -c1 fd15:5b2d:647f:1:75cd:be97:fd26:f3b9
PING fd15:5b2d:647f:1:75cd:be97:fd26:f3b9(fd15:5b2d:647f:1:75cd:be97:fd26:f3b9) 56 data bytes
64 bytes from fd15:5b2d:647f:1:75cd:be97:fd26:f3b9: icmp_seq=1 ttl=63 time=41.1 ms

--- fd15:5b2d:647f:1:75cd:be97:fd26:f3b9 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 41.148/41.148/41.148/0.000 ms
```

### Step 3: Publish SRP service on the terminal device.

```
> srp client autostart enable
Done
> srp client host name ot-host
Done
> srp client host address fd15:5b2d:647f:1:75cd:be97:fd26:f3b9
Done
> srp client service add ot-service _ipps._tcp 12345
Done
> srp client service
instance:"ot-service", name:"_ipps._tcp", state:Registered, port:12345, priority:0, weight:0
Done
```

### Step 4: Discover services on OTBR.

```
root@GL-S200:~# ot-ctl srp server service
ot-service._ipps._tcp.default.service.arpa.
    deleted: false
    subtypes: (null)
    port: 12345
    priority: 0
    weight: 0
    ttl: 7200
    lease: 7200
    key-lease: 1209600
    TXT: []
    host: ot-host.default.service.arpa.
    addresses: [fd15:5b2d:647f:1:75cd:be97:fd26:f3b9]
Done
root@GL-S200:~# dns-sd -B _ipps._tcp
Browsing for _ipps._tcp
DATE: ---Wed 15 Mar 2023---
 8:41:10.598  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
 8:41:10.600  Add        3   6 local.               _ipps._tcp.          ot-service
 8:41:10.602  Add        2   7 local.               _ipps._tcp.          ot-service
^C
root@GL-S200:~# dns-sd -L ot-service _ipps._tcp.
Lookup ot-service._ipps._tcp..local
DATE: ---Wed 15 Mar 2023---
 8:41:16.522  ...STARTING...
 8:41:16.666  ot-service._ipps._tcp.local. can be reached at ot-host.local.:12345 (interface 6) Flags: 1
 8:41:16.668  ot-service._ipps._tcp.local. can be reached at ot-host.local.:12345 (interface 7)
^C
root@GL-S200:~# dns-sd -G -v6 ot-host.local.
DATE: ---Wed 15 Mar 2023---
 8:41:21.478  ...STARTING...
Timestamp     A/R    Flags if Hostname                               Address                                      TTL
 8:41:21.653  Add        3  6 ot-host.local.                         FD15:5B2D:647F:0001:75CD:BE97:FD26:F3B9%<0>  120
 8:41:21.656  Add        2  7 ot-host.local.                         FD15:5B2D:647F:0001:75CD:BE97:FD26:F3B9%<0>  120
^C
root@GL-S200:~# ping -6 -c1 fd15:5b2d:647f:1:75cd:be97:fd26:f3b9
PING fd15:5b2d:647f:1:75cd:be97:fd26:f3b9 (fd15:5b2d:647f:1:75cd:be97:fd26:f3b9): 56 data bytes
64 bytes from fd15:5b2d:647f:1:75cd:be97:fd26:f3b9: seq=0 ttl=64 time=33.375 ms

--- fd15:5b2d:647f:1:75cd:be97:fd26:f3b9 ping statistics ---
1 packets transmitted, 1 packets received, 0% packet loss
round-trip min/avg/max = 33.375/33.375/33.375 ms
```

### Step 5: Discover services on PC.

Use **`dns-sd`**on macOS system.

```
$ dns-sd -B _ipps._tcp
Browsing for _ipps._tcp
DATE: ---Wed 15 Mar 2023---
16:42:03.955  ...STARTING...
Timestamp     A/R    Flags  if Domain               Service Type         Instance Name
16:42:03.958  Add        2   2 local.               _ipps._tcp.          ot-service

$ dns-sd -L ot-service _ipps._tcp.
Lookup ot-service._ipps._tcp..local
DATE: ---Wed 15 Mar 2023---
16:42:13.192  ...STARTING...
16:42:13.193  ot-service._ipps._tcp.local. can be reached at ot-host.local.:12345 (interface 2)

$ dns-sd -G -v6 ot-host.local.
DATE: ---Wed 15 Mar 2023---
16:42:18.168  ...STARTING...
Timestamp     A/R    Flags if Hostname                               Address                                      TTL
16:42:18.169  Add 40000002  2 ot-host.local.                         FD15:5B2D:647F:0001:75CD:BE97:FD26:F3B9%<0>  120
```

Use **`avahi-browser`** on Linux system.

```
$ avahi-browse -rt _ipps._tcp
+  ens33 IPv6 ot-service                                    Secure Internet Printer local
+  ens33 IPv4 ot-service                                    Secure Internet Printer local
=  ens33 IPv6 ot-service                                    Secure Internet Printer local
   hostname = [ot-host.local]
   address = [fd15:5b2d:647f:1:75cd:be97:fd26:f3b9]
   port = [12345]
   txt = []
=  ens33 IPv4 ot-service                                    Secure Internet Printer local
   hostname = [ot-host.local]
   address = [fd15:5b2d:647f:1:75cd:be97:fd26:f3b9]
   port = [12345]
   txt = []
```

### Step 6: Ping the terminal device's local domain name on PC.

```
$ ping -6 -c1 ot-host.local
PING ot-host.local(fd15:5b2d:647f:1:75cd:be97:fd26:f3b9 (fd15:5b2d:647f:1:75cd:be97:fd26:f3b9)) 56 data bytes
64 bytes from fd15:5b2d:647f:1:75cd:be97:fd26:f3b9 (fd15:5b2d:647f:1:75cd:be97:fd26:f3b9): icmp_seq=1 ttl=63 time=30.4 ms

--- ot-host.local ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 30.360/30.360/30.360/0.000 ms
```

If the ping command returns `Name or service not known` , modify `/etc/nsswitch.conf` as follows and try again. The domain name should be resolvable on both OTBR and PC.

```
hosts:          files mdns4_minimal mdns6_minimal dns
```

## Providing Internet access via NAT64.

Nat64 is enabled by default. After creating a Thread network and joining Thread devices to the network according to the instructions for the experiment on bi-directional IPv6 connectivity and DNS-based service discovery,

- Accessing Local Area Network.

```
> ping 192.168.8.233
Pinging synthesized IPv6 address: fdf8:7dfb:4d50:2:0:0:c0a8:8e9
16 bytes from fdf8:7dfb:4d50:2:0:0:c0a8:8e9: icmp_seq=3 hlim=63 time=15ms
1 packets transmitted, 1 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 15/15.0/15 ms.
Done
```

- Accessing the Internet.

```
> ping 8.8.8.8
Pinging synthesized IPv6 address: fdf8:7dfb:4d50:2:0:0:808:808
16 bytes from fdf8:7dfb:4d50:2:0:0:808:808: icmp_seq=4 hlim=47 time=75ms
1 packets transmitted, 1 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 75/75.0/75 ms.
Done
> dns resolve4 google.com 8.8.8.8
Synthesized IPv6 DNS server address: fdf8:7dfb:4d50:2:0:0:808:808
DNS response for google.com. - fdf8:7dfb:4d50:2:0:0:8efb:dc4e TTL:127
Done
> ping fdf8:7dfb:4d50:2:0:0:8efb:dc4e
16 bytes from fdf8:7dfb:4d50:2:0:0:8efb:dc4e: icmp_seq=5 hlim=106 time=96ms
1 packets transmitted, 1 packets received. Packet loss = 0.0%. Round-trip min/avg/max = 96/96.0/96 ms.
Done
```

## Matter Over Thread

The topology of this experiment is shown in the following diagram, where the Matter Controller runs on a PC, and the Matter Light and Matter Light Switch both use the Silicon Labs EFR32MG24 Breakout Board REV 1.1 as the Matter device.

![matter over thread](https://static.gl-inet.com/docs-iot/en/tutorials/openthread_border_router_codelabs/matter_over_thread.png){class="glboxshadow"}

### Step 1: Create a Thread network.

```
root@GL-S200:~# ot-ctl dataset init new
Done
root@GL-S200:~# ot-ctl dataset commit active
Done
root@GL-S200:~# ot-ctl dataset active
Active Timestamp: 1
Channel: 18
Channel Mask: 0x07fff800
Ext PAN ID: a1fce8946f2f9b1d
Mesh Local Prefix: fd50:5ff6:fd1b:325b::/64
Network Key: e67446d4e450ad76cd3ad5472530d410
Network Name: OpenThread-ee97
PAN ID: 0xee97
PSKc: 42743e8b67c06353cd038520a0ab8b7f
Security Policy: 672 onrc
Done
root@GL-S200:~# ot-ctl ifconfig up
Done
root@GL-S200:~# ot-ctl thread start
Done
root@GL-S200:~# ot-ctl state
leader
Done
root@GL-S200:~# ot-ctl dataset active -x
0e080000000000010000000300001235060004001fffe00208a1fce8946f2f9b1d0708fd505ff6fd1b325b0510e67446d4e450ad76cd3ad5472530d410030f4f70656e5468726561642d656539370102ee97041042743e8b67c06353cd038520a0ab8b7f0c0402a0f7f8
Done
root@GL-S200:~# ot-ctl netdata show
Prefixes:
fd15:5b2d:647f:1::/64 paos low c400
Routes:
fd15:5b2d:647f:2:0:0::/96 sn low c400
fda1:fce8:946f:9b1d::/64 s med c400
Services:
44970 5d fd505ff6fd1b325b84ab8a51482f2df7d11f s c400
44970 01 31000500000e10 s c400
Done
root@GL-S200:~# ot-ctl ipaddr
fd50:5ff6:fd1b:325b:0:ff:fe00:fc11
fd50:5ff6:fd1b:325b:0:ff:fe00:fc38
fd15:5b2d:647f:1:4e73:fe27:fcad:9eb4
fd50:5ff6:fd1b:325b:0:ff:fe00:fc10
fd50:5ff6:fd1b:325b:0:ff:fe00:fc00
fd50:5ff6:fd1b:325b:0:ff:fe00:c400
fd50:5ff6:fd1b:325b:84ab:8a51:482f:2df7
fe80:0:0:0:3488:80b2:ca62:867d
Done
```

### Step 2: Commissioning

Command format:

```
chip-tool pairing ble-thread ${NODE_ID} hex:${DATASET} ${PIN_CODE} ${DISCRIMINATOR}
```

- `${NODE_ID}`：Assign an ID to the commissioned device. It can be any non-zero value that has not been used after RCP initialization, and it is used by the chip-tool to operate on this Matter device.
- `${DATASET}`： Obtained by running the command `ot-ctl dataset active -x`
- `${PIN_CODE}`：If the pairing code has not been configured in the flash memory, use the default pairing code.
- `${DISCRIMINATOR}`：If pairing code is not configured in flash yet, use the default pairing code.

When you long-press the BT0 button on the Matter Light for more than 6 seconds, it enters commissioning mode.

```
sudo ./out/chip-tool/chip-tool pairing ble-thread 1001 hex:0e080000000000010000000300001235060004001fffe00208a1fce8946f2f9b1d0708fd505ff6fd1b325b0510e67446d4e450ad76cd3ad5472530d410030f4f70656e5468726561642d656539370102ee97041042743e8b67c06353cd038520a0ab8b7f0c0402a0f7f8 20202021 3840
```

Press and hold the BT0 button of the Matter Light Switch for more than 6 seconds to enter commissioning mode.

```
sudo ./out/chip-tool/chip-tool pairing ble-thread 1002 hex:0e080000000000010000000300001235060004001fffe00208a1fce8946f2f9b1d0708fd505ff6fd1b325b0510e67446d4e450ad76cd3ad5472530d410030f4f70656e5468726561642d656539370102ee97041042743e8b67c06353cd038520a0ab8b7f0c0402a0f7f8 20202021 3840
```

If there is no error, the output of the command should look like the following:

```
[1678871136.912386][3259774:3259774] CHIP:DL: Inet Layer shutdown
[1678871136.912404][3259774:3259774] CHIP:DL: BLE shutdown
[1678871136.913326][3259774:3259774] CHIP:DL: System Layer shutdown
```

Discovery Matter device from PC,

```
$ avahi-browse -rt _matter._tcp
+ enp0s31f6 IPv6 65D508548AF4E6CD-00000000000003EA             _matter._tcp         local
+ enp0s31f6 IPv6 65D508548AF4E6CD-00000000000003E9             _matter._tcp         local
+ enp0s31f6 IPv4 65D508548AF4E6CD-00000000000003EA             _matter._tcp         local
+ enp0s31f6 IPv4 65D508548AF4E6CD-00000000000003E9             _matter._tcp         local
= enp0s31f6 IPv6 65D508548AF4E6CD-00000000000003EA             _matter._tcp         local
   hostname = [DEE6259B059B0BB6.local]
   address = [fd15:5b2d:647f:1:25b3:9abe:d387:e9aa]
   port = [5540]
   txt = ["T=0" "SAI=2000" "SII=5000"]
= enp0s31f6 IPv6 65D508548AF4E6CD-00000000000003E9             _matter._tcp         local
   hostname = [3EF840EF1D01024D.local]
   address = [fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc]
   port = [5540]
   txt = ["T=0" "SAI=2000" "SII=5000"]
= enp0s31f6 IPv4 65D508548AF4E6CD-00000000000003EA             _matter._tcp         local
   hostname = [DEE6259B059B0BB6.local]
   address = [fd15:5b2d:647f:1:25b3:9abe:d387:e9aa]
   port = [5540]
   txt = ["T=0" "SAI=2000" "SII=5000"]
= enp0s31f6 IPv4 65D508548AF4E6CD-00000000000003E9             _matter._tcp         local
   hostname = [3EF840EF1D01024D.local]
   address = [fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc]
   port = [5540]
   txt = ["T=0" "SAI=2000" "SII=5000"]

$ avahi-browse -rt _matterc._udp
+ enp0s31f6 IPv6 18D347F0BB27870E                              _matterc._udp        local
+ enp0s31f6 IPv4 18D347F0BB27870E                              _matterc._udp        local
= enp0s31f6 IPv6 18D347F0BB27870E                              _matterc._udp        local
   hostname = [DEE6259B059B0BB6.local]
   address = [fd15:5b2d:647f:1:25b3:9abe:d387:e9aa]
   port = [5540]
   txt = ["PI=" "PH=36" "CM=0" "D=3840" "T=0" "SAI=2000" "SII=5000" "VP=65521+32772"]
= enp0s31f6 IPv4 18D347F0BB27870E                              _matterc._udp        local
   hostname = [DEE6259B059B0BB6.local]
   address = [fd15:5b2d:647f:1:25b3:9abe:d387:e9aa]
   port = [5540]
   txt = ["PI=" "PH=36" "CM=0" "D=3840" "T=0" "SAI=2000" "SII=5000" "VP=65521+32772"]

$ ping -6 -c1 3EF840EF1D01024D.local
PING 3EF840EF1D01024D.local(fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc (fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc)) 56 data bytes
64 bytes from fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc (fd15:5b2d:647f:1:b5be:90a6:6fde:a8dc): icmp_seq=1 ttl=63 time=82.9 ms

--- 3EF840EF1D01024D.local ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 82.865/82.865/82.865/0.000 ms

$ ping -6 -c1 DEE6259B059B0BB6.local
PING DEE6259B059B0BB6.local(fd15:5b2d:647f:1:25b3:9abe:d387:e9aa (fd15:5b2d:647f:1:25b3:9abe:d387:e9aa)) 56 data bytes
64 bytes from fd15:5b2d:647f:1:25b3:9abe:d387:e9aa (fd15:5b2d:647f:1:25b3:9abe:d387:e9aa): icmp_seq=1 ttl=63 time=69.3 ms

--- DEE6259B059B0BB6.local ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 69.331/69.331/69.331/0.000 ms
```

### Step 3: Control the Light

1. Toggle the Light

Command Format : `chip-tool onoff toggle ${NODE_ID} 1`

Example：

```
sudo ./out/chip-tool/chip-tool onoff toggle 1001 1
```

2. Turn On the Light

Command Format : `chip-tool onoff on ${NODE_ID} 1`

Example：

```
sudo ./out/chip-tool/chip-tool onoff on 1001 1
```

3. Turn Off the Light

Command Format : `chip-tool onoff off ${NODE_ID} 1`

Example：

```
sudo ./out/chip-tool/chip-tool onoff off 1001 1
```

4. Read the State of the Light

Command Format : `chip-tool onoff read on-off ${NODE_ID} 1`

Example：

```
sudo ./out/chip-tool/chip-tool onoff read on-off 1001 1
```

### Step 4: Use the Matter Switch to Control the Light

1. Set the ACL of the Light to Allow the Switch to Control It

For ACL parameter explanation, please refer to **Matter Core Specification - 9.10.5.3. ACL Attribute**

Command Format :

```
sudo ./out/chip-tool/chip-tool accesscontrol write acl '[{"fabricIndex":1, "privilege":5, "authMode":2, "subjects":[112233, ${switch_node_id}], "targets":null}]' ${lighting_node_id} 0
```

Example：

```
sudo ./out/chip-tool/chip-tool accesscontrol write acl '[{"fabricIndex":1, "privilege":5, "authMode":2, "subjects":[112233, 1002], "targets":null}]' 1001 0
```

2. Bind the Switch to the Light

Command Format :

```
sudo ./out/chip-tool/chip-tool binding write binding '[{"fabricIndex":1, "node":${lighting_node_id}, "endpoint":1, "cluster":6}]' ${switch_node_id} 1
```

Example：

```
sudo ./out/chip-tool/chip-tool binding write binding '[{"fabricIndex":1, "node":1001, "endpoint":1, "cluster":6}]' 1002 1
```

After completing the above steps, you can use Matter Switch BTN1 to control the on/off state of Matter Light.

## Connect to Home Assistant

Test environment

   - Raspberrypi 4B
   - Debian GNU/Linux 11 (bullseye)

In progress …