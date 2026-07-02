# How to remotely access the web Admin Panel of a GL.iNet Router?

The following methods require pre-configuration while you are still physically beside the router.

## Method 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} is a platform designed to simplify the remote deployment and management of connected devices. It provides an easy way to remotely access and manage GL.iNet routers. Simply bind your GL.iNet router to GoodCloud, then you can remotely access the router's web Admin Panel anytime, anywhere. 

Please refer to [this guide](../interface_guide/cloud.md){target="_blank"} for details.

## Method 2. VPN

If your router has a **public IP**, you can remotely access its web Admin Panel through a VPN tunnel. Note that this method involves advanced configurations and will take extra time to set up.

1. Ensure your router has a public IP. [How can I check if I have a public IP address?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}
    
2. Set your router as a WireGuard Server. See [here](../interface_guide/wireguard_server.md){target="_blank"} for details.

3. Export a configuration file from your WireGuard Server for later use.

4. On the router's web Admin Panel, go to **VPN** -> **WireGuard Server** and click **Options** in the upper-right corner. Enable **Allow Remote Access to the LAN Subnet** then click **Apply**.

5. Set the device from which you want to remotely access your router as a WireGuard Client by importing the configuration file manually. 
    
    - If your WireGuard Client is a terminal device, such as smartphone or laptop, [install WireGuard App](https://www.wireguard.com/install){target="_blank"}, then import the file to start a connection.

    - If your WireGuard Client is another GL.iNet router, such as a GL.iNet travel router, refer to [this guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} to import the configuration file to it and start a connection.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
