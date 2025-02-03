# Build Your Own WireGuard Home Server with two GL.iNet Routers

This article will introduce how to set up your home router as the WireGuard VPN server and your travel router as the WireGuard VPN client to connect together remotely, so that you can use your home IP address with the travel router anywhere.

Here we use our GL-MT6000 as the example to run WireGuard VPN server at the home site, and you can also choose other models such as MT2500 if you don't require the wireless capacity. As for the travel router, we use our GL-MT3000 as the example, and you can choose others as well.

## Why you need to build own your WireGuard home server

1. Use your home IP address as the Internet address, acting as that you are just at home.
2. No need to pay the monthly fee when comparing with the 3rd parties VPN service.
3. Route all the Internet traffic to your home network via encrypted VPN tunnel and secure your privacy.
4. Easy access to your internal resources and local streaming.

## Preparations

### Check if you have a Public IP address

First, you shall make sure the GL-MT6000 has a Public IP address on its WAN side, so that it can be globally accessed. Otherwise your travel router cannot build up a VPN connection with it while you are traveling.

To check if you have the Public IP address, please open a web browser and type in [ip.gs](https://ip.gs){target="_blank"} in the address bar.

![myip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/myip.jpg){class="glboxshadow"}

It will show your public IP address, if it matches with your WAN IP from your ISP, you are granted a Public IP Address.

If you don't have a Public IP address, here are some methods for your reference.

1. if you have a main router, you shall login to it and check if it gets the Public IP from your ISP.
2. if you can ask your ISP to give you a Public IP address, she may charge an extra fee for it.
3. if both the above two ways don't work. For example, if you are in a CGNAT, you can take the reverse proxy method such as [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md).

### Confirm you need to do a Port Forwarding or not?

??? "GL.iNet as Main Router"

    Topology

    GLiNet Router is directly connect to ISP modem

    ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

    How to confirm your GL.iNet Router connects to the ISP modem directly?

    ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.jpg){class="glboxshadow gl-80-desktop"}

    Login GL.iNet Admin Panel, you can see your Public IP shows on the IP Address and you have **No Need** to do **Port Forwarding**.

??? "GL.iNet as Sub-Router"

    Topology

    Set the **Port Forward** on your Main Router if GL.iNet router sits behind NAT

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Connect to your home router's WiFi or LAN, then login to the web admin panel. Check the WAN IP address it obtains from your ISP. Here you can see it is your Public IP **42.200.00.00**.

    Example: A TP-Link Router

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.jpg){class="glboxshadow"}

    1. Go to “Advanced” and click “virtual Server”, then “Add”.
    
    2. Internal IP (Device IP): It is the IP address assigned to GL.iNet Router, you can find it in the client list of TP-Link
    
    3. External/Internal port:  Please fill both are "51820"
    
    4. Protocol:  You can choose "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **More [Port Forward](how_to_set_up_port_forwarding.md) examples**
   
## Set up the WireGuard server on GL.iNet Router

### Enable DDNS (Optional)

Enable the DDNS function if you do not have a Public Static IP but only have a Public Dynamic IP.

Go to the admin panel >Applications>Dynamic DNS and slide to enable

![serverddns](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/serverddns.jpg){class="glboxshadow"}

Check the box below and click **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/ddnsapply.jpg){class="glboxshadow"}

Then Go to WireGuard VPN server, make sure the Listen Port is 51820 and click “Apply.”

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgsever.jpg){class="glboxshadow"}

### Generate a Configuration

Click **Profiles** and **Add** a Client then it will automatically generate a client configuration. Click the **square icon** (point 2) and slide to use DDNS Domain. (point 3, Optional if you have dynamic IP only).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Use the WireGuard [mobile app](https://www.wireguard.com/install/) scan the QR to test the server.For details please click [here](../interface_guide/wireguard_server.md/#to-check-if-wireguard-server-is-working-properly).

### Output a text format configuration for Client Installation

Change the configuration to text format by click **Configuration File**. Copy the text for the client or download and save it then drag it to the client later.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Set up the WireGuard Client on GL-MT3000

### Change the LAN IP

Login to the admin panel of GL-MT3000 and go to the **Network** on the side bar and change the LAN IP.

[Change the LAN IP](../interface_guide/lan.md)

### Add the Configuration

Go to the WireGuard Client and click **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient1.jpg){class="glboxshadow"}

Create a name for the connection and drag the configuration downloaded before or click **Manually Add Configuration**.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient2.jpg){class="glboxshadow"}

Paste the Configuration Text onto it and then you can connect to the server now.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient3.jpg){class="glboxshadow"}

## Connect GL-MT3000 to your GL-MT6000 Server

Click the name you just created, and it will show you the configuration you just loaded then click **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgstart.jpg){class="glboxshadow"}

You will see your client is connecting to the server now with your Home Public IP.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Go back to the VPN DashBoard of GL-MT6000, you will also see the client is connected.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon.jpg){class="glboxshadow"}

## Use GoodCloud to manage the routers remotely in case of any problems when you are traveling

Sometimes your server may be down due to a power outage or other reasons, in order to maintain the accessibility of your server, please bind it our GoodCloud also. 

---

Related Articles

- [The GoodCloud](../interface_guide/cloud.md)
