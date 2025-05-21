# Connecting to a Hotspot with a Captive Portal

## What is a captive portal?

A captive portal is a Web page where public hotspots require users to view and interact with the page before Internet access is granted.

## Why do I need to use a router to connect to a public hotspot?

* Public Wi-Fi is not safe

    We cannot put enough emphasis on how public Wi-Fi is not safe. By connecting your GL.iNet router to the public wifi, you can simply login to your VPN account directly through your router's Admin Panel, and it'll automatically encrypt all connected devices within the local network, saving you from the trouble of setting up VPN on every single device. 

* Use as a repeater to allow connections with multiple devices

    Besides that, some public Wi-Fi such as hotel complimentary Wi-Fi are limited to let's say 2 devices. When you're travelling in a group, that's just not going to work. Instead, you could connect a travel router to the hotel Wi-Fi, and use it as a hotspot to broadcast Wi-Fi to all your devices including laptops, smartphones, tablets…etc. The hotel Wi-Fi will only recognize the travel router as a single device, but you could enjoy the free Wi-Fi as many devices as you want. 

## How do I connect my router to a public hotspot via captive portal?

1. Connect your smartphone or computer to the router.

    Power on the router. On your smartphone or computer, connect WiFi to your travel router by searching its SSID, and enter the WiFi password. The default password indicated as “WIFI Key” on the bottom of your router.

2. Access your travel router's web Admin Panel.

    After successfully connecting to your router, go to the web Admin Panel of your router by visiting router IP address (default is `192.168.8.1`) on the Internet browser. If you are logging in for the first time, select a language and create a new password for the router's web Admin Panel.

3. Connect your router to the public hotspot's SSID using the [Repeater](../interface_guide/internet_repeater.md/) function.

4. Fill out the hotel's Captive Portal.

## Troubleshooting

However, you may find that you are unable to enter the captive portal, so you cannot connect to the hotspot or access the Internet. In this case, please try the following solutions one at a time.

---

### Solution 1: Change DNS settings

1. Go to web Admin Panel -> NETWORK -> DNS. Then, make sure the **DNS Rebinding Attack Protection** is disabled and the **Mode** is set to **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="580"}

2. Go to web Admin Panel -> VPN -> VPN Dashboard. Make sure the connection of OpenVPN and WireGuard client is disabled.

    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="580"}
    
    <small>(v4.7 and earlier)</small>

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.jpg){class="glboxshadow" width="580"}
    
    <small>(v4.8)</small>

3. Go to web Admin Panel -> APPLICATIONS -> AdGuard Home. Make sure the AdGuard Home is disabled.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Use your web browser to visit a webpage, it will be redirected to the captive portal of the hotspot automatically.

    If you are using a smartphone and your web browser doesn't redirect to the captive portal, please turn off your smartphone's Wi-Fi, turn it on, and reconnect to the router's Wi-Fi. The captive portal should pop up directly after you enter the Wi-Fi password.

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Solution 2：MAC Clone

Sometimes, [Solution 1](#solution-1-change-dns-settings) is not enough to solve this issue. Some hotels limit the number of devices each customer can access by MAC address, and they record the MAC address of your phone (or other device) when it first time accesses the hotel WiFi. In this case, we need to clone the MAC address that the your phone uses to connect to the hotel WiFi to the router.

1. Get your smartphone registered on the network.

2. Connect your phone to the hotel WiFi. Find the MAC address that your phone uses to connect to the hotel's WiFi. 

    Here is an example for iPhone (iOS 16.1.2): go to Settings -> Wi-Fi -> Select the hotel WiFi and you will find the Wi-Fi Address. Write down this address.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    For some old phones, the MAC address may not be found in WiFi settings, then it may use the real MAC address of the phone, which can be found in the phone's Settings -> About.

3. Connect your phone or computer to the router. Access the router's web Admin Panel, clone or manually input this MAC access.

    **For v4.5 and earlier**, please select NETWORK from the left side -> MAC Address.

    Select Manual Mode, fill in the MAC address you wrote down in step 2 into the input box and click Apply.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **For v4.6 and higher**, please select INTERNET from the left side -> Repeater section, click Modify.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    In the pop-up window, switch the MAC Mode to Clone, manually input the MAC address written down in step 2 and click Apply.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

4. It may be necessary to reboot the router to take effect.

---

### Solution 3：Seek help from hotel staff

Some hotels' networks have very strict verification policies. If neither solution 1 nor solution 2 works, you can ask the hotel staff to add the router's MAC address (the factory default one) to their whitelist directly.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
