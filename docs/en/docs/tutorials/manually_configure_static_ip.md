# How to manually configure static IP on the client devices? {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    On Windows 11, you can set a static IP address for your wireless and wired adapters.

    **Set static IP address on Wi-Fi adapter**

    1. On a Windows 11 PC, go to **Settings** -> **Network & internet** -> **Wi-Fi** and select the current Wi-Fi connection.

    2. Find **IP assignment** and click the **Edit** button.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. In the pop-up window, select **Manual** and enable **IPv4**.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}
    
    4. Follow the steps below to edit IP settings.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Set a static IP address, for example, `10.1.4.119`.

        - Subnet mask: Specify a Subnet mask, for example, `255.255.255.0`.

        - Gateway: Enter the gateway address, usually your router's LAN IP on the same subnet. For example, if your IP is `10.1.4.119`, the gateway is typically `10.1.4.1`.

        - Preferred DNS: Specify a Preferred DNS address (required). You may enter the public DNS server such as Google's DNS server `8.8.8.8`.

        - Alternate DNS: Specify an Alternate DNS address (optional).

        - DNS over HTTPS: Select "Off". There are three options:

            - Off: Transmits all DNS traffic without encryption.

            - On (automatic template): Sends all DNS traffic with encryption.

            - On (manual template): Allows you to specify a specific template. It is only required if the DNS service does not work automatically or has a template that works as expected.

        - Turn off "Fallback to plaintext" toggle switch if you enable DNS over HTTPS.

            **Tip**: If you enable this feature, the system will encrypt DNS traffic, but it allows queries to be sent without encryption.

    5. Click **Save** to apply the settings.

        Once you complete the above steps, the static network configuration will apply to the computer. You can test the new settings by opening the web browser and loading a website.

    ---

    **Set static IP address on Ethernet adapter**

    1. On a Windows 11 PC, go to **Settings** -> **Network & internet** -> **Ethernet**.
    
    2. Find **IP assignment** and click the **Edit** button.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. In the pop-up window, select **Manual** and enable **IPv4**.

        ![manual](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}
    
    4. Follow the steps below to edit IP settings.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: Set a static IP address, for example, `10.1.4.119`.

        - Subnet mask: Specify a Subnet mask, for example, `255.255.255.0`.

        - Gateway: Enter the gateway address, usually your router's LAN IP on the same subnet. For example, if your IP is `10.1.4.119`, the gateway is typically `10.1.4.1`.

        - Preferred DNS: Specify a Preferred DNS address (required). You may enter the public DNS server such as Google's DNS server `8.8.8.8`.

        - Alternate DNS: Specify an Alternate DNS address (optional).

        - DNS over HTTPS: Select "Off". There are three options:

            - Off: Transmits all DNS traffic without encryption.

            - On (automatic template): Sends all DNS traffic with encryption.

            - On (manual template): Allows you to specify a specific template. It is only required if the DNS service does not work automatically or has a template that works as expected.

        - Turn off "Fallback to plaintext" toggle switch if you enable DNS over HTTPS.

            **Tip**: If you enable this feature, the system will encrypt DNS traffic, but it allows queries to be sent without encryption.

    5. Click **Save** to apply the settings.

        Once you complete the above steps, the static network configuration will apply to the computer. You can test the new settings by opening the web browser and loading a website.

=== "macOS"

    Here's how to set a static IP address on macOS.

    From the Apple menu, select **System Preferences**.

    Select **Network**, and the following page appears. Select an active network interface from the sidebar, such as **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Note down the current IP address assigned to your Mac. You'll need to select a new IP address within the private IP address range listed.

    Click **Advanced** in the bottom-right corner.

    Then select **TCP/IP**, and the following page appears.
    
    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: Select "Manually".

    - IPv4 Address: Enter a static IP address. Keep the first three octets of your current IP and change the last octet to an unused value. For example, on the `192.168.7.0/24` network, choose an address from `192.168.7.2` to `192.168.7.254` that is not already in use (avoid `.1`, which is the router). Do not use `192.168.7.0` or `192.168.7.255`.

    - Subnet Mask: Enter `255.255.255.0` (or the subnet mask provided by your network administrator).
    
    - Router: Enter your router's LAN IP address, e.g., `192.168.7.1`.

    Click **OK**, then click **Apply**.

=== "iOS"

    The steps may vary depending on your iOS version. The following steps are based on iOS version 26.2.2.

    1. Go to **Settings** -> **WLAN**. Tap on the blue information icon (i) next to the current connected Wi-Fi network.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}
    
    2. Scroll down to find **IPv4 Address** and select **Configure IP** as **Manual**.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Specify the **IP Address**, **Subnet Mask** and **Router IP** that you want to use on your iPhone/iPad, then tap **Save** in the upper right corner.

        ![ios static ip](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    The steps may vary depending on your Android version. The following steps are based on Android version 11.

    1. Go to **Settings** -> **Network & Internet** -> **Wi-Fi**. Tap on the currently connected network to open the settings menu.
    
        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Tap the pencil icon in the top right corner to access the network settings.
        
        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Tap **Advanced options**.
        
        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Tap **IP Settings** and select **Static**.
        
        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Enter the **IP address**, and the **Gateway** should fill in automatically based on the IP address. If not, enter your network gateway. The gateway is usually your router's LAN IP on the same subnet.

        **Tip**: When using static IP addresses on home and other private networks, choose an unused host address within your current network subnet. The standard private IP address ranges are as follows:
        
        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Tap **Save** and wait for the network to reconnect.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
    