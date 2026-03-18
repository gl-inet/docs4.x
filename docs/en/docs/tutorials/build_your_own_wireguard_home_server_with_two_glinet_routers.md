# Build your own WireGuard home server with two GL.iNet routers

This article will introduce how to set up your home router as the WireGuard VPN server and your travel router as the WireGuard VPN client to connect together remotely, so that you can use your home IP address with the travel router anywhere.

Watch this video or refer to the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/v_DyRGicWco" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(This video uses GL-BE9300 (Flint 3) and GL-BE3600 (Slate 7) to demonstrate the VPN setup.)</small>

In the following steps, we take GL-MT6000 (Flint 2) and GL-MT3000 (Beryl AX) as examples:

- GL-MT6000, a home router, will be set up as a WireGuard VPN server. If wireless capacity is not required, our security gateway GL-MT2500 or other models can also be considered.

- GL-MT3000, a travel router, will be set up as a WireGuard VPN client to remotely connect to the VPN server at home.

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

    Connect to the Wi-Fi or LAN of your home router. Then login to the web Admin Panel. Check the WAN IP address it obtains from your ISP. In the image below, you can see that your public IP is **42.200.00.00**.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Before setting up port forwarding, we recommend reserving an IP address for the GL.iNet router on your Main router, so that a fixed IP can be assigned to the GL.iNet router.** Otherwise, once the Main router or GL.iNet router restarts, the main router may assign a different IP address to the GL.iNet router, causing the port forwarding rule to fail.

    Then set up the Port Forwarding on your Main router for the GL.iNet router.

    1. Go to “Advanced” and click “virtual Server”, then “Add”.
    
    2. Internal IP (Device IP): It is the IP address assigned to GL.iNet Router, you can find it in the client list of TP-Link
    
    3. External/Internal port:  Please fill both are "51820"
    
    4. Protocol:  You can choose "All or UDP or TCP/UDP"

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **More [Port Forward](how_to_set_up_port_forwarding.md) examples**

## Set up WireGuard server

### Enable DDNS (Optional)

Enable the DDNS function if you do not have a static public IP but only a dynamic public IP.

Log in to the web Admin Panel of GL-MT6000 and go to **APPLICATIONS** -> **Dynamic DNS**. Toggle on the switch for **Enable DDNS**.

Check the box for **Terms of Service & Privacy Policy** and click **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Then go to the **WireGuard Server** -> Configuration tab, make sure the Listen Port is 51820, then click **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Generate Configuration

In the same page, click **Profiles** tab next to the Configuration tab, then click **Add** (marked as 1 in the image below).

It will automatically generate a client configuration. Click the **forward icon** (marked as 2).

In the pop-up window, slide to enable DDNS Domain (marked as 3, which is optional and enable it only if you have dynamic public IP).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Then you can scan the QR using the WireGuard [mobile app](https://www.wireguard.com/install/) to test the server. For details please click [here](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

Alternatively, you can export a text format configuration for VPN client connetcion.

Switch the configuration from QR code to text format by clicking **Configuration File** tab. 

Copy the text for the client, or click the Download button and save it for later use.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Set up WireGuard Client

### Change the LAN IP

Since we use GL-MT6000 and GL-MT3000 as examples in this tutorial, whose default LAN IPs are both **192.168.8.1**, we need to change one of them to a different LAN IP to avoid conflict. 

Here are the steps to change the LAN IP of GL-MT3000 (the WireGuard client).

Log in to the web Admin Panel of GL-MT3000, then go to the **NETWORK** from the left side bar -> **LAN** to change the LAN IP. For example, you can change the LAN IP from the default 192.168.8.1 to `192.168.10.1`.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

For more details about the LAN interface, please click [here](../interface_guide/lan.md).

### Add the Configuration

On the web Admin Panel of GL-MT3000, go to **VPN** -> **WireGuard Client**, and click **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Create a group on the left and set a name, then select the configuration file to upload or drag it to the upload box on the right.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

After the file passes verification, click **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

You can also click **Manually Add Configuration** and paste the configuration text, then click **Apply**.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

The configuration file will be displayed on the WireGuard Client page once it is uploaded successfully.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Start the Connection

Click the three-dot icon and click **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Wait a few minutes. Once it is connected successfully, a green dot will light up.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Turn to **VPN Dashboard**, and you will see that your client is connecting to the server with your home public IP. The page may vary slightly depending on the firmware version.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Log in back to the web Admin Panel of GL-MT6000 (the WireGuard server), go to **VPN** -> **WireGuard Server** (or go to **VPN** -> **VPN Dashboard** if you use firmware v.4.7 and earlier), and you will also see the connnection status, indicating that the client is connected.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(WireGuard Server page in FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(VPN Dashboard page in FW v4.7 and earlier)</small>

## Prep for Remote VPN Fixes Ahead

In case of unforeseen issues while traveling, pre-bind both routers to your GoodCloud account for remote VPN troubleshooting.

Sometimes your server may be down due to a power outage or other reasons. In order to maintain the accessibility of your server, please bind it to GL.iNet GoodCloud. 

---

Related Articles

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
