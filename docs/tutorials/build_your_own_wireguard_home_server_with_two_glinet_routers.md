# Build your own WireGuard home server with two GL.iNet routers

This article will introduce how to set up your home router as the WireGuard VPN server and your travel router as the WireGuard VPN client to connect together remotely, so that you can use your home IP address with the travel router anywhere.

Here we use GL-MT6000 as the example to run WireGuard VPN server at the home site, and you can also choose other models such as GL-MT2500 if you don't require the wireless capacity. 

As for the travel router, we use GL-MT3000 as the example, and you can choose others as well.

## Why you need to build your own WireGuard home server

1. Use your home IP address as the Internet address, acting as that you are just at home.
2. No need to pay the monthly fee when comparing with the 3rd parties VPN service.
3. Route all the Internet traffic to your home network via encrypted VPN tunnel and secure your privacy.
4. Easy access to your internal resources and local streaming.

## Preparations

### Check if you have a Public IP

First, make sure the GL-MT6000 has a public IP address on its WAN side, so that it can be globally accessed. Otherwise your travel router cannot build up a VPN connection with it while you are traveling.

To check if you have the public IP address, please open a web browser and type in [what is my ip](https://whatismyipaddress.com/){target="_blank"} in the address bar.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

It will show your public IP address. If it matches the WAN IP provided by your ISP for the GL-MT6000, you have a public IP address.

If you don't have a public IP address, here are some methods for your reference.

1. If you have a main router, login to it and check if it gets the public IP from your ISP.
2. Ask your ISP for a public IP address. It may require an extra fee.
3. If the above two ways don't work, for example, if you are in a CGNAT, you can take the reverse proxy method such as [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md). Alternatively, you may try an SDWAN solution - [AstroWarp](https://www.astrowarp.net/). 

### Check if Port Forwarding is required

??? "GL.iNet as Main Router" 

    If your GL.iNet Router is directly connected to a ISP modem via an Ethernet cable, the GL.iNet Router is the Main Router.

    **How to check if your GL.iNet Router connects to the ISP modem directly?**

    Steps:
    
    1. Log in to the GL.iNet Admin Panel. 

    2. Select INTERNET from the left sidebar. Check the topology and connection details:

        If directly connected via Ethernet, you will see a section named "Ethernet" with details such as Protocol, IP address, Gateway, etc.

        Taking the following image as an example, the marked IP Address is the WAN IP provided by the ISP for this GL-iNet router. 

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        This WAN IP is a public IP address, thus this GL.iNet router, acting as a Main router, has a public IP and **no need to set a Port Forwarding for it**.

        You just need to set this GL.iNet router as WireGuard server, and a travel router as WireGuard Client connecting to the server. Then a VPN tunnel will be built between them.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}
    
??? "GL.iNet as Sub-Router"

    Set up the **Port Forwarding** on your Main router for the GL.iNet router if the latter is behind NAT.

    Topology

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Example: A TP-Link Router as your home main router.

    Connect to the WiFi or LAN of your home router. Then login to the web Admin Panel. Check the WAN IP address it obtains from your ISP. In the image below, you can see that your public IP is **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Before setting up port forwarding, we recommend reserving an IP address for the GL.iNet router on your Main router, so that a fixed IP can be assigned to the GL.iNet router.** Otherwise, once the Main router or GL.iNet router restarts, the main router may assign a different IP address to the GL.iNet router, causing the port forwarding rule to fail.

    Then set up the Port Forwarding on your Main router for the GL.iNet router.

    1. Go to “Advanced” and click “virtual Server”, then “Add”.
    
    2. Internal IP (Device IP): It is the IP address assigned to GL.iNet Router, you can find it in the client list of TP-Link
    
    3. External/Internal port:  Please fill both are "51820"
    
    4. Protocol:  You can choose "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **More [Port Forward](how_to_set_up_port_forwarding.md) examples**

## Set up the WireGuard server

### Enable DDNS (Optional)

Enable the DDNS function if you do not have a static public IP but only a dynamic public IP.

Go to the web Admin Panel -> **Applications** -> **Dynamic DNS** and enable it.

![serverddns](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/serverddns.jpg){class="glboxshadow"}

Check the **Terms of Service & Privacy Policy** below and click **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/ddnsapply.jpg){class="glboxshadow"}

Then go to the **WireGuard Server** -> Configuration tab, make sure the Listen Port is 51820 and click **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgsever.jpg){class="glboxshadow"}

### Generate Configuration

In the same page, click **Profiles** tab next to the Configuration tab, then click **Add** (marked as 1 in the image below).

It will automatically generate a client configuration. Click the **forward icon** (marked as 2).

In the pop-up window, slide to enable DDNS Domain (marked as 3, which is optional and enable it only if you have dynamic public IP).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Then you can scan the QR using the WireGuard [mobile app](https://www.wireguard.com/install/) to test the server. For details please click [here](../interface_guide/wireguard_server.md/#to-check-if-wireguard-server-is-working-properly).

Alternatively, you can output a text format configuration for VPN client connetcion.

Switch the configuration from QR code to text format by clicking **Configuration File** tab. 

Copy the text for the client, or click the Download button and save it for later use.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Set up the WireGuard Client

### Change the LAN IP

Since we use GL-MT6000 and GL-MT3000 as examples in this tutorial, whose default LAN IPs are both **192.168.8.1**, we need to change one of them to a different LAN IP to avoid conflict.

Login to the web Admin Panel of GL-MT3000, go to the **NETWORK** from the left side bar -> **LAN** to change the LAN IP.

[Change the LAN IP](../interface_guide/lan.md)

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Add the Configuration

Go to the **VPN** -> **WireGuard Client**, click **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient1.jpg){class="glboxshadow"}

Create a name for the connection, and drag the configuration file downloaded before to the uploading box, or click **Manually Add Configuration**.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient2.jpg){class="glboxshadow"}

Paste the Configuration Text onto it, then you can connect to the server.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient3.jpg){class="glboxshadow"}

### Start the Connection

Click the name you just created, and it shows the uploaded configuration. Click the three-dot icon and **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgstart.jpg){class="glboxshadow"}

You will see that your client is connecting to the server with your home public IP.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Login back to the web Admin Panel of GL-MT6000 (the WireGuard server), go to **VPN** -> **VPN Dashboard**, you will also see the connnection status, indicating that the client is connected.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon.jpg){class="glboxshadow"}

## Prep for Remote VPN Fixes Ahead

In case of unforeseen issues during travel, pre-bind both routers to GoodCloud for remote VPN troubleshooting.

Sometimes your server may be down due to a power outage or other reasons. In order to maintain the accessibility of your server, please bind it to GL.iNet GoodCloud. 

---

Related Articles

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
