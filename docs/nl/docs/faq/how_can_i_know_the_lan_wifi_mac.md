# Alle MAC-adressen van mijn apparaat vinden {#how-can-i-find-all-mac-addresses-of-my-device}

## Usage Scenario {#usage-scenario}

Een GL.iNet-apparaat heeft voor elke netwerkinterface een uniek MAC-adres, waaronder WAN 1, WAN 2, LAN-poorten, 2.4G-wifi en 5G-wifi.

Bij sommige hotels, campings of campussen moet de netwerkbeheerder het MAC-adres van je apparaat op een acceptatielijst zetten voordat je internettoegang krijgt.

Je kunt de exacte MAC-adressen van je apparaat als volgt opzoeken.

## Method 1. via Product Label (for WAN MAC only) {#method-1-via-product-label-for-wan-mac-only}

Zoek het **WAN MAC address** op het etiket aan de onderkant.

In de onderstaande afbeelding is het WAN-MAC-adres bijvoorbeeld E4:95:6E:40:DB:A9.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/wan_lan_wifi.png){class="glboxshadow"}

## Method 2. via SSH {#method-2-via-ssh}

Please check [here](../tutorials/ssh_log_in_to_the_router.md) for how to use SSH.

Voer via SSH **ifconfig** in. De uitvoer toont interfaces zoals br-lan, ethx en wlanx.

### MAC-adres van Ethernetpoorten vinden {#find-the-mac-of-ethernet-ports}

Taking the following image as an example.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwan.jpg){class="glboxshadow"}

- **eth0** is de WAN-poort met MAC-adres **94:83:C4:19:19:08**.

    Bij een extra WAN-poort, bijvoorbeeld op de GL-MT6000, is er ook een extra WAN-MAC-adres.

- **eth1**, **eth2** enzovoort zijn de LAN-poorten met MAC-adres **94:83:C4:19:19:09**.

    Ook bij meerdere LAN-poorten is er slechts één MAC-adres.

### MAC-adres van draadloze interfaces vinden {#find-the-mac-of-wireless-ports}

Taking the following image as an example.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** is 2.4G-wifi met MAC-adres **96:83:C4:19:19:0B**.

- **wlan1** is 5G-wifi met MAC-adres **94:83:C4:19:19:0A**.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
