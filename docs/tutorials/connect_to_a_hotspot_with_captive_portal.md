# Connect to a Hotspot with Captive Portal

Some public hotspots especially those in hotel, cafe or airport, require you to input your authentication information or agree the terms and conditions through a web page (Captive Portal) before you can connect to it or access the Internet.

However, you may find that you are not able to enter the captive portal so that you cannot connect to the hotspot or access the Internet. In this case, please follow the solutions below one by one.

---

## Solution 1：Change DNS settings

1. Visit the web Admin Panel (default is 192.168.8.1), use [Repeater](../internet_repeater/) to connect to the public hotspot which requires authentication through captive portal.

    Click **Connect** in the repeater sector.

    ![repeater](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_sector.png){class="glboxshadow"}

    Select the public network which you want to connect.

    ![join wlan](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_wlan.png){class="glboxshadow"}

    Click **Apply**. You can also enable the Remember button to save the current chose wireless network.

    ![join network](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_network.png){class="glboxshadow"}

    ![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_connected.png){class="glboxshadow"}

2. Go to web Admin Panel -> NETWORK -> DNS. Then, make sure the **DNS Rebinding Attack Protection** is disable and the **Mode** is **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="580"}

3. Go to web Admin Panel -> VPN -> VPN Dashboard. Make sure the connection of OpenVPN and WireGuard client is disable.

    ![vpn client is disable](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="572"}

4. Go to web Admin Panel -> APPLICATIONS -> AdGuard Home. Make sure the AdGuard Home is stopped.

    ![adguard home is stopped](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

5. Use your web browser to visit a webpage, it will be redirected to the captive portal of the hotspot automatically.

    If you are using smartphone but your web browser doesn't redirect to the captive portal. Please turn off the Wi-Fi of your smartphone and then turn it on and reconnect to the Wi-Fi of your router again. The captive portal should be popped up directly after you entered the Wi-Fi password.

    ![connected](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

## Solution 2：MAC Clone

Sometimes, [Solution 1](#solution-1change-dns-settings) is not enough to solve this issue. Then you need to try the **MAC Clone** based on the solution 1.

1. Got your smartphone registered on the network.

2. On the left side of web Admin Panel -> NETWORK -> MAC Clone.

3. Clone the MAC address of your smartphone to the router.

    ![MACCLONE](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_clone.png){class="glboxshadow"  width="400"}

4. It may need to reboot the router to take effect.

---

## Solution 3：Ask the help from the hotel staff

Some hotel's network has a very strict verification policy. Neither solution 1 nor 2 is unable to make it work, then you can consult with the hotel staff if they can add the router's MAC address(the Factory default one) to their "Whitelist" directly.

