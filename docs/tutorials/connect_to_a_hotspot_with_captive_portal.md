# Connect to a Hotspot with Captive Portal

Some public hotspots especially those in hotel, cafe or airport, require you to input your authentication information or agree the terms and conditions through a web page (Captive Portal) before you can connect to it or access the Internet.

However, you may find that you are not able to enter the captive portal so that you cannot connect to the hotspot or access the Internet. In this case, please the following solutions one by one.
 
## Solution 1：Disable the *DNS Rebinding Attack Protection*

1. Visit the web Admin Panel (192.168.8.1), use [repeater](../internet_repeater/) to connect to the public hotspot which requires authentication through captive portal.

    Click **Connect** under the repeater sector.

    ![repeater](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_sector.png){class="glboxshadow"}

    Select the public network which you want to connect.

    ![join wlan](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_wlan.png){class="glboxshadow"}

    Click **Apply**. You can also enable the Remember button to save the current chose wireless network.

    ![join network](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/join_network.png){class="glboxshadow"}

    ![repeater connected](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_connected.png){class="glboxshadow"}

2. Go to web Admin Panel -> MORE SETTINGS -> DNS. Then, disable **DNS Rebinding Attack Protection** then click **Apply**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow"}

3. Use your web browser to visit a webpage, it will be redirected to the captive portal of the hotspot automatically.

    If you are using smartphone but your web browser doesn't redirect to the captive portal. Please turn off the Wi-Fi of your smartphone and then turn it on and reconnect to the Wi-Fi of your router again. The captive portal should be popped up directly after you entered the Wi-Fi password.

    ![connected](https://static.gl-inet.com/docs/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png)

## Solution 2：MAC Clone

Sometimes, disable the *DNS Rebinding Attack Protection* is not enough to solve this issue. Then you need to try the **MAC Clone** based on the solution 1.

1. Got your smartphone registered on the network.

2. On the left side of web Admin Panel -> MORE SETTINGS -> MAC Clone.

3. Clone the MAC address of your smartphone to the router.

    ![MACCLONE](https://d2jbioc4ahy17s.cloudfront.net/docs/en/4/tutorials/mac_clone/macclone4.0.jpg){width="500"}

4. It may need to reboot the rooter to take effect.

## Solution 3：Ask the help from the hotel staff

Some hotel's network has a very strict verification policy. Neither solution 1 nor 2 is unable to make it work, then you can consult with the hotel staff if they can add the router's MAC address(the Factory default one) to their "Whitelist" directly.

