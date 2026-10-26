# Securing RDP from an External Network with WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

You may need to remotely access your PC from an external network, or vice versa. The most secure way is to do so through your own WireGuard tunnel. This provides better security than port forwarding and accessing your PC directly through your public IP address. After setting up the tunnel, you can use **Windows Remote Desktop** to access your PC from anywhere.

This tutorial takes two GL.iNet routers as an example to demonstrate how to secure Windows RDP over a WireGuard network.

## Topology {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Setup steps {#setup-steps}

1. Build your WireGuard network.

    First, set up your own WireGuard server and WireGuard client using two GL.iNet routers. See [Build your own WireGuard server with two GL.iNet routers](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Allow your WireGuard server to access the client LAN.

    To enable bidirectional access between the server and client, please first allow the server to access the client LAN side. See [How to access WireGuard client LAN side from Server](wireguard_server_access_to_client_lan_side.md). 
    
    The steps may vary due to differences in firmware versions.

3. Allow your WireGuard client to access the server LAN.

    This step may vary due to differences in firmware versions. Select the firmware version of the router you set as WireGuard client below for reference.
    
    ??? note "For firmware v4.7 and earlier"
    
        Log in to your WireGuard client and go to **VPN** -> **VPN Dashboard**. Locate the **VPN Server** and click the gear icon on the right. 

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        In the pop-up window, enable **Remote Access LAN** and click **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "For firmware v4.8 and above"

        Log in to your WireGuard client and go to **VPN** -> **WireGuard Server**. Click **Options** in the upper-right. 

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        In the pop-up window, enable **Allow Remote Access to the LAN Subnet** and click **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Connect the computer to be accessed to the VPN server and find its LAN IP address.

    In the following example, the IP address of the server-side PC is **192.168.29.123**.

5. Configure the server-side PC to be accessible.
    
    On the server-side PC, go to the **System Settings** and click **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Enable **Remote Desktop** and click **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Remote access from the client-side laptop.

    Search **Remote Desktop Connection** in the search bar.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Launch the app and enter the IP address of the server-side PC, e.g., **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Enter the credentials of your server-side PC to connect.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    You will then be able to remotely control your PC on the server side.

    If you want to do it vice versa, simply reverse the steps of server-side PC and client-side laptop.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.