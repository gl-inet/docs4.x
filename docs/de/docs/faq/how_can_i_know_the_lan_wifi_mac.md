# Wie finde ich alle MAC-Adressen meines Geräts?

## Einsatzszenario

Die MAC-Adressen eines GL.iNet Geräts sind für jede Netzwerkschnittstelle eindeutig, z. B. WAN 1, WAN 2, LAN-Ports, 2,4G Wi-Fi und 5G Wi-Fi.

Wenn Sie sich mit bestimmten Hotels, Campingplätzen oder Campus-Netzwerken verbinden, kann es sein, dass der Netzwerkadministrator die MAC-Adresse Ihres Geräts benötigt, um es vor dem Internetzugang auf die Whitelist zu setzen.

Sie können die genaue(n) MAC-Adresse(n) Ihres Geräts mit den folgenden Methoden nachschlagen.

## Methode 1: über das Produktetikett (nur für WAN-MAC)

Suchen Sie die **WAN-MAC-Adresse** auf dem Etikett an der Unterseite.

Im folgenden Bild ist die WAN-MAC beispielsweise **E4:95:6E:40:DB:A9**.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

## Methode 2: per SSH

Wie Sie SSH verwenden, erfahren Sie [hier](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

Geben Sie in SSH **ifconfig** ein. Anschließend erhalten Sie eine Datenausgabe, in der nacheinander Schnittstellen wie br-lan, ethx, wlanx usw. angezeigt werden.

### Die MAC-Adresse der Ethernet-Ports finden

Nehmen Sie das folgende Bild als Beispiel.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

- **eth0** ist der WAN-Port mit der MAC-Adresse **94:83:C4:19:19:08**.

    Wenn es einen weiteren WAN-Port gibt (z. B. beim GL-MT6000), gibt es auch eine weitere WAN-MAC-Adresse.

- **eth1**, **eth2** usw. sind die LAN-Ports mit der MAC-Adresse **94:83:C4:19:19:09**.

    Es gibt nur eine MAC-Adresse, auch wenn mehr als ein LAN-Port vorhanden ist.

### Die MAC-Adresse der WLAN-Schnittstellen finden

Nehmen Sie das folgende Bild als Beispiel.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** ist das 2,4G Wi-Fi mit der MAC-Adresse **96:83:C4:19:19:0B**.

- **wlan1** ist das 5G Wi-Fi mit der MAC-Adresse **94:83:C4:19:19:0A**.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
