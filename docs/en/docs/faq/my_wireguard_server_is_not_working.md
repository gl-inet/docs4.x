# The WireGuard server on my GL.iNet router is not working properly

There are various reasons why the WireGuard server you have set up on your GL.iNet router is not working properly. 

If you encounter issues, follow these troubleshooting steps based on your specific situation.

#### Situation 1: The WireGuard server is starting but can't be connected

??? "Follow these steps"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    The port forwarding you have set up on your primary router connected to your secondary router (GL.iNet) may not be working properly. 
    To check if port forwarding is working properly, try to forward the primary router's HTTPS port to your WireGuard server. Follow these steps: 

    1. Forward your primary router's HTTPS port to your WireGuard server

        1. Sign in to your primary router's admin panel. 
        2. Go to the port forwarding screen. 
        3. Create a new port and name it **HTTPS**. 
        4. Enter the following information:
            * **External port/Internal port:** Enter **443**. 
            * **Protocol:** Choose **All** or **UDP/TCP**.
            * **Internal IP** (or shown as **Host IP**): Enter your secondary router's WAN IP address or select your secondary router from the dropdown if available.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Enable DDNS and HTTPS remote access (on the GL.iNet router)

        1. In a web browser, enter the URL to your GL.iNet router's admin panel (e.g., 192.168.8.1) and sign in.
        2. In the left sidebar, click **Applications** > **Dynamic DNS**. 
        3. Toggle **Enable DDNS** to on and check the box for **I have read and agree to the Terms of Service & Privacy Policy**. 
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Save the hostname somewhere as you will need it for later, then click **Apply**. 
        5. In the left sidebar, click **System** > **Security**. 
        6. Under **Remote Access Control**, toggle **HTTPS Remote Access** to on.  
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Click **Apply**. 

    3. Check if you can access the GL.iNet router's admin panel 

        1. On another device (e.g., laptop or mobile device), connect to a different Wi-Fi network or the cellular network. 
        2. In a web browser's address bar, enter the hostname you saved earlier (abcd123.glddns.com). 
        3. Click **Advanced**. 
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Click **Proceed to abcd123.glddns.com(unsafe)**. 
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    If you see the login screen of your GL.iNet router (secondary router), the port forwarding you set up on your primary router is working properly.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    If you do not see the login screen of your GL.iNet router (secondary router), port forwarding is not working properly. Set up port forwarding again or make sure to use a router with functioning port forwarding ability as your primary router. 

#### Situation 2: The WireGuard server shows that my VPN client is connected, but the VPN client cannot access the Internet

??? "Follow these steps"

    Follow the steps outlined for each possible cause below and check if the issue is resolved. If the issue is resolved, you can skip the rest of the section. 

    **Possible cause 1: You internet service provider may not be able to resolve GL.iNet's DNS servers**

    Try to manually configure the DNS server addresses by following these steps: 

    1. In a web browser, enter the URL to your GL.iNet router's admin panel (e.g., 192.168.8.1) and sign in.
    2. In the left sidebar, click **Network** > **DNS**. 
    3. For **Mode**, select **Manual DNS**. 
    4. For **DNS Server 1**, select **Google Public DNS**. 
    5. Click **Apply**. 

    **Possible cause 2: Your primary router's gateway IP is in conflict with the WireGuard server's IP address**

    Try to change the IPv4 address by following these steps: 

    1. In a web browser, enter the URL to your GL.iNet router's admin panel (e.g., 192.168.8.1) and sign in.
    2. In the left sidebar, click **VPN** > **WireGuard Server**. 
    3. In the **Configuration** tab, for the **IPv4 Address** field, enter a new IP address (e.g., 10.1.0.1/24). 
    4. Click **Apply**. 

    **Possible cause 3: If both your WireGuard server and WireGuard client were set up on GL.iNet routers, their LAN IP addersses are in conflict**

    Try to change the LAN IP address on either router by following these steps:     

    1. In a web browser, sign in to the admin panel of either GL.iNet router (e.g., 192.168.8.1). 
    2. In the left sidebar, click **Network** > **LAN**. 
    3. In the **Router IP address** field, enter a new LAN IP address (e.g., 192.168.10.1). 
    4. Click **Apply**. 

    **Possible cause 4: The WireGuard server's IP address was updated but the subnet is missing**

    Add a subnet to your WireGuard server IP address by following these steps: 

    1. In a web browser, enter the URL to your GL.iNet router's admin panel (e.g., 192.168.8.1) and sign in.
    2. In the left sidebar, click **VPN** > **WireGuard Server**. 
    3. In the **Configuration** tab, for the **IPv4 Address** field, add **/24** after **10.0.0.1**. 
    4. Click **Apply**. 

#### Situation 3: The WireGuard server is running but I can't connect my VPN client to it

??? "Follow these steps"

    Follow the steps outlined for each possible cause below and check if the issue is resolved. If the issue is resolved, you can skip the rest of the section. 

    **Possible cause 1: The port forwarding you have set up on your primary router may not be working properly**

    To check if port forwarding is working properly, try to forward the HTTPS port to your WireGuard server by following the resolution steps outlined in Situation 1. 

    **Possible cause 2: You may not have a public IP address**

    To check if you have one, follow this [page](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/). 

    **Possible cause 3: If both your WireGuard server and WireGuard client were set up on GL.iNet routers, their LAN IP addersses are in conflict**

    Change the LAN IP address on either router by following these steps: 

    1. In a web browser, sign in to the admin panel of either GL.iNet router (e.g., 192.168.8.1). 
    2. In the left sidebar, click **Network** > **LAN**. 
    3. In the **Router IP address** field, enter a new LAN IP address (e.g., 192.168.10.1). 
    4. Click **Apply**. 

    **Possible cause 4: The device you are using to connect to the WireGurad server is connected to its Wi-Fi network or its LAN port** 

    Connect your device to a different Wi-Fi network or its cellular network. 

    **Possible cause 5: Some lines may be missing in the configuration file you uploaded to your client device**

    Upload your configuration information again. 

#### Situation 4: The WireGuard server is connected but the connection is not stable

??? "Follow these steps"

    Follow the steps below to resolve the issue. After each step, check if the issue is resolved. If the issue is resolved, you can skip the rest of the steps.

    1. On your VPN client device, change the MTU from **1420** to a smaller value (e.g., 1380).
    2. On your primary router, enable the VPN passthrough feature if available. 
    3.  Try to manually configure DNS servers on your GL.iNet router by following these steps: 
        1. In a web browser, enter the URL to your GL.iNet router's admin panel (e.g., 192.168.8.1) and sign in.
        2. In the left sidebar, click **Network** > **DNS**. 
        3. For Mode, select **Manual DNS**. 
        4. For **DNS Server 1**, select **Google Public DNS**. 
        5. Click **Apply**. 

#### Situation 5: The WireGuard server suddenly stopped working

??? "Follow these steps"

    Follow the steps outlined for each possible cause below and check if the issue is resolved. If the issue is resolved, you can skip the rest of the section. 

    **Possible cause 1: There may be a power outage in where you set up your WireGuard server**

    Check whether your WireGuard server is still online by following the resolution steps in Situation 1 or via [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/) (if you previously connected your router to it).

    **Possible cause 2: You did not enable the Dynamic DNS (DDNS)**

    If you have a dynamic IP address (which you most likely do), you will need to enable DDNS. [Enable DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) and follow the rest of the steps to set up the WireGuard server again. 

    **Possible cause 3: The port forwarding stopped working for unknown reasons**

    [Set up port forwarding](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) again with another port. 

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
