# Build Your Own OpenVPN Home Server with two GL-iNet Routers

This article will introduce how to set up your home router as the OpenVPN server and your travel router as the OpenVPN client to connect together remotely, so that you can use your home IP address with the travel router anywhere.

Here we use our GL-MT6000 as the example to run OpenVPN server at the home site, and you can also choose other models such as MT2500 if you don’t require the wireless capacity. As for the travel router, we use our GL-MT3000 as the example, and you can choose others as well.

## Why you need to build own your OpenVPN home server

1. Use your home IP address as the Internet address, acting as that you are just at home.
2. No need to pay the monthly fee when comparing with the 3rd parties VPN service.
3. Route all the Internet traffic to your home network via encrypted VPN tunnel and secure your privacy.
4. Easy access to your internal resources and local streaming.

## Topology

![topologyovpn](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/topologyovpn.jpg){class="glboxshadow"}

## Check if you have a Public IP address

First, you shall make sure the GL-MT6000 has a Public IP address on its WAN side, so that it can be globally accessed. Otherwise your travel router cannot build up a VPN connection with it while you are traveling.

To check if you have the Public IP address, please open a web browser and type in [ip.gs](https:ip.gs) in the address bar.

![myip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/myip.jpg){class="glboxshadow"}

It will show your public IP address, if it matches with your WAN IP from your ISP, you are granted a Public IP Address.

If you don’t have a Public IP address, here are some methods for your reference.

1. if you have a main router, you shall login to it and check if it gets the Public IP from your ISP.
2. if you can ask your ISP to give you a Public IP address, she may charge an extra fee for it.
3. if both the above two ways don’t work. For example, if you are in a CGNAT, you can take the reverse proxy method such as [Astrorelay](how_to_set_up_openvpn_server_via_astrorelay.md).

## Scenario 1: Your GL-MT6000 connects to an upper router

Connect to your home router’s WiFi or LAN, then login the web admin panel. Check the IP address it obtains from your ISP. Here you can see it is your Public IP **42.200.00.00**.

**Example: A TP-Link Router**

![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tp_home.jpg){class="glboxshadow"}

### Set up the Port Forwarding on your main router

1. Login to the web control page of your main router 
2. Find out where is the function of port forwarding, different brands may call it by different names
3. Find the IP address assigned to GL-MT6000

**Example: A TP-Link Router**

1. Go to “Advanced” and click “virtual Server”, then “Add”.
2. Internal IP (Device IP): It is the IP address assigned to GL-MT6000, you can find it in the client list of TP-Link
3. External/Internal port:  Please fill both are "1194"
4. Protocol:  You can choose "All or UDP or TCP/UDP"

![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tp_port1.jpg){class="glboxshadow"}

## Scenario 2: Your MT3000 connects to the ISP modem directly

![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/mt6000_home.jpg){class="glboxshadow"}

You can see your Public IP shows on the IP Address and you have **No Need** to do port forwarding.

## Set up the OpenVPN server on GL-MT6000

### Enable DDNS (Optional)

Enable the DDNS function if you do not have a Public Static IP but only have a Public Dynamic IP.

Go to the admin panel >Applications>Dynamic DNS and slide to enable

![serverddns](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/serverddns.jpg){class="glboxshadow"}

Check the box below and click **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ddnsapply.jpg){class="glboxshadow"}

Then Go to OpenVPN server, make sure the Listen Port is 1194 and click **Export Client Configuration**.

![ovpnserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ovpnserver.jpg){class="glboxshadow"}

## Generate a Configuration

Slide to use DDNS Domain (Optional if you have dynamic IP only) or click **Download** directly.

![ovpnddnsn](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ovpnddns.jpg){class="glboxshadow"}

## Output a text format configuration for Client Installation

Copy the Configuration file for the client or download and save it then drag it to the client later.

![ovpnconfigload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ovpnconfigload.jpg){class="glboxshadow"}

Use the OpenVPN [mobile app](https://openvpn.net/client/) upload the file to test the server.For details please click [here](../interface_guide/openvpn_server.md#to-check-if-openvpn-server-is-working-properly).


## Set up the WireGuard Client on GL-MT3000

Login to the admin panel of GL-MT3000 and go to the OpenVPN Client and click **Add Manually**.

![addovpnclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/addovpnclient1.jpg){class="glboxshadow"}

Create a name for the connection and drag the configuration downloaded to the box.

![addovpnclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/addovpnclient2.jpg){class="glboxshadow"}

You will see **Upload successful** then please click **Apply**.

![addovpnclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/addovpnclient3.jpg){class="glboxshadow"}

## Connect your Client GL-MT3000 to your GL-MT6000 Server

Click the name you just created, and it will show you the configuration you just loaded then click **Start**.

![ovpnstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ovpnstart.jpg){class="glboxshadow"}

You will see your client is connecting to the server now with your Home Public IP or your DDNS address enabled.

![ovpnconnect](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/ovpnconnect.jpg){class="glboxshadow"}

## Use GoodCloud to manage the routers remotely in case of any problems when you are traveling

Sometimes your server may be down due to a power outage or other reasons, in order to maintain the accessibility of your server, please bind it our GoodCloud also. 

---

Related Articles

- [The GoodCloud](../interface_guide/cloud.md)
