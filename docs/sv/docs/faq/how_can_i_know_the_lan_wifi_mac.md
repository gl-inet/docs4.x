# Hur hittar jag enhetens alla MAC-adresser? {#how-can-i-find-all-mac-addresses-of-my-device}

## Användningsscenario {#usage-scenario}

MAC-adresserna för en GL.iNet-enhet är unika för varje nätverksgränssnitt, till exempel WAN 1, WAN 2, LAN-portarna, 2.4G Wi-Fi och 5G Wi-Fi.

När du ansluter till nätverk på vissa hotell, campingplatser eller campus kan nätverksadministratören kräva enhetens MAC-adress för att registrera den i en tillåtelselista innan du får internetåtkomst.

Du kan ta reda på enhetens exakta MAC-adress eller MAC-adresser med följande metoder.

## Metod 1. Via produktetiketten (endast för WAN-MAC-adressen) {#method-1-via-product-label-for-wan-mac-only}

Leta reda på **WAN MAC address** på etiketten på undersidan.

I bilden nedan är WAN-MAC-adressen till exempel E4:95:6E:40:DB:A9.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/wan_lan_wifi.png){class="glboxshadow"}

## Metod 2. Via SSH {#method-2-via-ssh}

Information om hur du använder SSH finns [här](../tutorials/ssh_log_in_to_the_router.md).

Ange **ifconfig** i SSH. Du får då utdata där gränssnitt som br-lan, ethx och wlanx visas i ordning.

### Hitta Ethernet-portarnas MAC-adresser {#find-the-mac-of-ethernet-ports}

Utgå från följande bild som exempel.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwan.jpg){class="glboxshadow"}

- **eth0** är WAN-porten och har MAC-adressen **94:83:C4:19:19:08**.

    Om det finns ytterligare en WAN-port (t.ex. på GL-MT6000) finns det även ytterligare en WAN-MAC-adress.

- **eth1**, **eth2** osv. är LAN-portarna och har MAC-adressen **94:83:C4:19:19:09**.

    Det finns endast en MAC-adress även om routern har flera LAN-portar.

### Hitta de trådlösa portarnas MAC-adresser {#find-the-mac-of-wireless-ports}

Utgå från följande bild som exempel.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** är 2.4G Wi-Fi och har MAC-adressen **96:83:C4:19:19:0B**.

- **wlan1** är 5G Wi-Fi och har MAC-adressen **94:83:C4:19:19:0A**.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
