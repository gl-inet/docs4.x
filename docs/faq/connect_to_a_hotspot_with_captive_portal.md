# Connecting to a Hotspot with a Captive Portal

## What is a captive portal?

A captive portal is a Web page where public hotspots require users obligated to view and interact with before Internet access is granted.

## Why do I need to use my router to connect to a public hotspot?

* Public Wi-Fi is not safe

    We cannot put enough emphasis on how public Wi-Fi is not safe. By connecting your GL.iNet router to the public wifi, you can simply login to your VPN account directly through your router's Admin Panel, and it’ll automatically encrypt all connected devices within the local network, saving you from the trouble of setting up VPN on every single device. 

* Use as a repeater to allow connections with multiple devices

    Besides that, some public Wi-Fi such as hotel complimentary Wi-Fi are limited to let’s say 2 devices. When you’re travelling in a group, that’s just not going to work. Instead, you could connect a travel router to the hotel Wi-Fi, and use it as a hotspot to broadcast Wi-Fi to all your devices including laptops, smartphones, tablets…etc. The hotel Wi-Fi will only recognize the travel router as a single device, but you could enjoy the free Wi-Fi as many devices as you want. 

## How do I connect my router to a public hotspot via captive portal?

1. Connect your smartphone or computer to the router.

    Power on the router. On your smartphone or computer, connect WiFi to your travel router by searching its SSID, and enter the WiFi password. The default password indicated as “WIFI Key” on the bottom of your router.

2. Access your travel router's web admin panel.

    After successfully connecting to your router, go to the web admin panel of your router by visiting router IP address (default is `192.168.8.1`) on the Internet browser. If you are logging in for the first time, select a language and create a new password for the router's web admin panel.

3. Connect your router to the public hotspot's SSID using the [Repeater](../internet_repeater/) function.

4. Fill out the hotel's Captive Portal.

## Troubleshooting

However, you may find that you are unable to enter the captive portal, so you cannot connect to the hotspot or access the Internet. In this case, please try the following solutions one at a time.

---

### Solution 1: Change DNS settings

1. Go to web Admin Panel -> NETWORK -> DNS. Then, make sure the **DNS Rebinding Attack Protection** is disable and the **Mode** is **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="580"}

2. Go to web Admin Panel -> VPN -> VPN Dashboard. Make sure the connection of OpenVPN and WireGuard client is disable.

    ![vpn client is disable](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="572"}

3. Go to web Admin Panel -> APPLICATIONS -> AdGuard Home. Make sure the AdGuard Home is stopped.

    ![adguard home is stopped](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Use your web browser to visit a webpage, it will be redirected to the captive portal of the hotspot automatically.

    If you are using smartphone but your web browser doesn't redirect to the captive portal. Please turn off the Wi-Fi of your smartphone and then turn it on and reconnect to the Wi-Fi of your router again. The captive portal should be popped up directly after you entered the Wi-Fi password.

    ![connected](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Solution 2：MAC Clone

Sometimes, [Solution 1](#solution-1-change-dns-settings) is not enough to solve this issue. Some hotels limit the number of devices each customer can access by MAC address, and they record the MAC address of your phone (or other device) when it first time accesses the hotel WiFi. In this case, we need to clone the MAC address that the your phone uses to connect to the hotel WiFi to the router.

1. Got your smartphone registered on the network.

2. Make sure your phone is connected to the hotel WiFi. Find the MAC address that your phone uses to connect to the hotel's WiFi. Here is an example for iPhone (iOS 16.1.2), go to settings -> Wi-Fi -> Select the hotel WiFi. You will find the Wi-Fi Address, write down this address.

    ![iphone wifi private address](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    For some old phones, the MAC address is not found there in WiFi, then it uses the real MAC address of the phone. This can be found in the phone's **Settings** -> **About** where you can find the phone's MAC address.

3. Use your phone or computer to connect to router, access web admin panel. On the left side of web Admin Panel -> NETWORK -> MAC Address.

    Select Manual Mode, fill in the MAC address you wrote down in step 2 into the input box and click Apply.

    ![MAC manual](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

4. It may need to reboot the router to take effect.

---

### Solution 3：Ask the help from the hotel staff

Some hotel's network has a very strict verification policy. Neither solution 1 nor 2 is unable to make it work, then you can consult with the hotel staff if they can add the router's MAC address(the Factory default one) to their "Whitelist" directly.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
