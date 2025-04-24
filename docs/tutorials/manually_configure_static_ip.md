# How to manually configure static IP on the client devices?

=== "Windows 11"

    On Windows 11, you can set a static IP address configuration from the Settings app for wireless and wired adapters.

    **Set static IP address on Wi-Fi adapter**

    To assign a static IP address configuration to a Wi-Fi adapter, use these steps:

    1. Open Settings on Windows 11 -> Network & Internet ->  the Wi-Fi tab ->  Select the current network connection.

    2. Under the “IP settings” section, click the Edit button.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. Follow the steps below to set it up:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Select the Manual option,Turn on the IPv4 toggle switch.

        - Set a static IP address for Windows 11 – for example, 10.1.4.119.

        - Specify a Subnet mask – for example, 255.255.255.0.

        - Specify a Default Gateway address.

        - Specify a Preferred DNS address (required).

        - (Optional) Specify an “Alternate DNS” address.

        - Use the “DNS over HTTPS” drop-down menu and select the Off option for the preferred and alternate addresses, but you can enable DoH with these options:

            - Off: Transmits all DNS traffic without encryption.

            - On (automatic template): Sends all DNS traffic with encryption.

            - On (manual template): Allows you to specify a specific template. It is only required if the DNS service doesn't work automatically or has a template that works as expected.

        - Turn off the “Fallback to plaintext” toggle switch (if you enable DoH).

            - Quick tip: If you enable this feature, the system will encrypt DNS traffic, but it allows queries to be sent without encryption.

    4. Click the Save button.

        Once you complete the steps, the static network configuration will apply to the computer. You can test the new settings by opening the web browser and loading a website.


    ## **Set static IP address on Ethernet adapter**

    To assign a static IP address to an Ethernet (wired) adapter on Windows 11, use these steps:

    1. Open Settings -> Network & Internet ->  Ethernet tab.
    
    2. Under the “IP settings” section, click the Edit button.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. Follow the steps below to set it up:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}
        
        - Select the Manual option.

        - Turn on the IPv4 toggle switch.

        - Set a static IP address for Windows 11 – for example, 10.1.4.119.

        - Specify a Subnet mask – for example, 255.255.255.0.

        - Specify a Default Gateway address.

        - Specify a Preferred DNS address (required).

        - (Optional) Specify an “Alternate DNS” address.

        - Use the “DNS over HTTPS” drop-down menu and select the Off option for the preferred and alternate addresses, but you can enable DoH with these options:

            * Off: Transmits all DNS traffic without encryption.

            * On (automatic template): Sends all DNS traffic with encryption.

            * On (manual template): Allows you to specify a specific template. It is only required if the DNS service doesn't work automatically or has a template that works as expected.
            
        - Turn off the “Fallback to plaintext” toggle switch (if you enable DoH).

    4. Click the Save button.

        After you complete the steps, you can test your settings using your web browser to open a website.


=== "macOS"

    Here's how to set a static IP address in macOS:

    If you own a MacBook, you may want to create a new network location. This will allow you to use the static IP address for certain networks and not others. 

    From the Apple menu, select System Preferences.

    Select Network. The window shown below appears.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    From the sidebar, select an active network interface. In this example, I'm connected to a wireless network, so I'll select Wi-Fi.

    Make a note of the current IP address assigned to your Mac. You'll need to select a new IP address from within the private IP address range listed. More on that in a minute.

    Click Advanced.

    Select TCP/IP. The window shown below appears.
    
    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    From the Configure IPv4 menu, select Manually.

    Enter a static IP address in the IPv4 Address field. What number should you enter? One method is to take your current IP address and change the last part of the number. In this example, I could have picked any address between 192.168.7.0 and 192.168.7.255, as long as the address was not already assigned to another device.

    Click OK -> Click Apply.
   

=== "Android"

    The steps will vary with different versions of Android. This documentation is based on Android version 11.

    1. Go to Settings -> Select Network & Internet, then Wi-Fi -> Tap on the network currently connected to open the settings menu.
    
    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. To set a static IP address, do the following:

    - Select the pencil icon in the top right to access the network settings.
        
        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Select Advanced Options.
        
        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Select IP Settings.
        
    - Change the setting from DHCP to Static.
        
        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - When using static IP addresses on home and other private networks, they should be chosen from within the standard private IP address ranges listed:10.0.0.0 through 10.255.255.255,172.16.0.0 through 172.31.255.255,192.168.0.0 through 192.168.255.255

    - Now enter the IP address.
        -This step is specific to each network. ex: 192.168.1.128
        
    - The Gateway should fill in automatically based on the IP address. If not, copy the IP address and replace the last number with a 1. 
        -ex. Based on the previous example: 192.168.1.1

    3. Tap Save and let the network reconnect.

=== "iOS"

    When using static IP addresses on home and other private networks, they should be chosen from within the standard private IP address ranges listed:

    10.0.0.0 through 10.255.255.255
    172.16.0.0 through 172.31.255.255
    192.168.0.0 through 192.168.255.255

    To set a static IP address, do the following:

    - Tap on the Settings icon.

    - Go to Wi-Fi.

    - Tap on the blue information icon (i) next to the name of the Wi-Fi network
         - This may be a blue error if you are using something older than iOS 7.

    - Go to the Static tab, pictured below.

        
    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - Tap on the IP Address field.

    - Enter the static IP address that you want to use on your iPhone/iPad.

    - Tap on the Router field.

    - Enter the routers IP address.
        
    - Tap on Subnet Mask and enter your information

        - Usually, it will be 225.225.0.0.

    - Tap on the Wi-Fi button, in the upper left corner of the screen, to save settings.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
    