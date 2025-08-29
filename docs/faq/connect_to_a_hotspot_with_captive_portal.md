# Connecting to a Hotspot with a Captive Portal

## What is a captive portal?

A captive portal is a Web page where public hotspots require users to view and interact with the page before Internet access is granted.

## Why use a router for public hotspots?

* Public Wi-Fi is not safe

    We cannot put enough emphasis on how public Wi-Fi is not safe. By connecting your GL.iNet router to the public wifi, you can simply login to your VPN account directly through your router's Admin Panel, and it'll automatically encrypt all connected devices within the local network, saving you from the trouble of setting up VPN on every single device. 

* Use as a repeater to allow connections with multiple devices

    Besides that, some public Wi-Fi such as hotel complimentary Wi-Fi are limited to let's say 2 devices. When you're travelling in a group, that's just not going to work. Instead, you could connect a travel router to the hotel Wi-Fi, and use it as a hotspot to broadcast Wi-Fi to all your devices including laptops, smartphones, tablets…etc. The hotel Wi-Fi will only recognize the travel router as a single device, but you could enjoy the free Wi-Fi as many devices as you want. 

## How to connect router to public hotspot with captive portal?

Watch this video or follow the steps below.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Connect your smartphone or computer to the router.

    Power on the router. On your smartphone or computer, connect WiFi to your travel router by searching its SSID, and enter the WiFi password. The default password indicated as “WIFI Key” on the bottom of your router.

2. Access your travel router's web Admin Panel.

    After successfully connecting to your router, go to the web Admin Panel of your router by visiting router IP address (default is `192.168.8.1`) on the Internet browser. If you are logging in for the first time, select a language and create a new password for the router's web Admin Panel.

3. Connect your router to the public hotspot's SSID using the [Repeater](../interface_guide/internet_repeater.md/) function.

4. Fill out the hotel's Captive Portal.

## Troubleshooting

However, you may find that you are unable to enter the captive portal, so you cannot connect to the hotspot or access the Internet. In this case, please try the following solutions.

### Solution 1: Enable Public Hotspot Login Mode & Camouflage

**Note**: These two features are available only in firmware v4.6 and above.

When connecting the router to a public hotspot with a captive portal, on the Join Network page, enabling the following features can help improve the connection success rate.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    If this option is enabled, this router will automatically enter Login Mode for Public Hotspots when it is successfully connected to a hotspot but not the Internet. In this mode, some services will be suspended while the DNS mode will be switched to automatic, which may leak your network activity to the hotspot provider (e.g. hotel or shopping mall).

- Enable Camouflage

    If enabled, the router will masquerade as the client device you use to access the admin panel by emulating that device’s MAC address.

---

### Solution 2: Change DNS settings

1. Go to web Admin Panel -> NETWORK -> DNS. Then, make sure the **DNS Rebinding Attack Protection** is disabled and the **Mode** is set to **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Go to web Admin Panel -> VPN -> VPN Dashboard. Make sure the connection of OpenVPN and WireGuard client is disabled.

    **For firmware v4.7 and earlier**, the page is displayed as below. 
    
    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}
    
    **For firmware v4.8 and higher**, the page is displayed as below.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Go to web Admin Panel -> APPLICATIONS -> AdGuard Home. Make sure the AdGuard Home is disabled.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Use your web browser to visit a webpage, it will be redirected to the captive portal of the hotspot automatically.

    If you are using a smartphone and your web browser doesn't redirect to the captive portal, please turn off your smartphone's Wi-Fi, turn it on, and reconnect to the router's Wi-Fi. The captive portal should pop up directly after you enter the Wi-Fi password.

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Solution 3：MAC Clone

Sometimes, [Solution 1](#solution-1-change-dns-settings) is not enough to solve this issue. Some hotels limit the number of devices each customer can access by MAC address, and they record the MAC address of your phone (or other device) when it first time accesses the hotel WiFi. In this case, we need to clone the MAC address that the your phone uses to connect to the hotel WiFi to the router.

1. Get your smartphone registered on the network.

2. Connect your phone to the hotel WiFi. Find the MAC address that your phone uses to connect to the hotel's WiFi. 

    Here is an example for iPhone (iOS 16.1.2): go to Settings -> Wi-Fi -> Select the hotel WiFi and you will find the Wi-Fi Address. Write down this address.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    For some old phones, the MAC address may not be found in WiFi settings, then it may use the real MAC address of the phone, which can be found in the phone's Settings -> About.

3. Connect your phone or computer to the router. Access the router's web Admin Panel, clone or manually input this MAC access.

    **For firmware v4.5 and earlier**, please select NETWORK from the left side -> MAC Address.

    Select Manual Mode, fill in the MAC address you wrote down in step 2 into the input box and click Apply.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **For firmware v4.6 and higher**, please select INTERNET from the left side -> Repeater section, click Modify.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    In the pop-up window, switch the MAC Mode to Clone, manually input the MAC address written down in step 2 and click Apply.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

4. It may be necessary to reboot the router to take effect.

---

### Solution 4：Seek help from hotel staff

Some hotels' networks have very strict verification policies. If neither solution 1 nor solution 2 works, you can ask the hotel staff to add the router's MAC address (the factory default one) to their whitelist directly.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
