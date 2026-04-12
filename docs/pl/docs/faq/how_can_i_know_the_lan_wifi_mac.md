# Jak znaleźć wszystkie adresy MAC mojego urządzenia?

## Scenariusz użycia

Adresy MAC urządzenia GL.iNet są unikalne dla każdego interfejsu sieciowego, takiego jak WAN 1, WAN 2, porty LAN, Wi-Fi 2.4G i Wi-Fi 5G.

Podczas łączenia się z siecią w hotelu, na kempingu lub na terenie kampusu administrator sieci może poprosić o adres MAC urządzenia, aby dodać go do białej listy przed przyznaniem dostępu do Internetu.

Dokładne adresy MAC urządzenia możesz sprawdzić na następujące sposoby.

## Metoda 1. z etykiety produktu (tylko WAN MAC)

Znajdź **adres WAN MAC** na etykiecie znajdującej się na spodzie urządzenia.

Na przykład na poniższej ilustracji adres WAN MAC to E4:95:6E:40:DB:A9.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

## Metoda 2. przez SSH

Instrukcję korzystania z SSH znajdziesz [tutaj](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

Wpisz w sesji SSH polecenie **ifconfig**, a otrzymasz dane wyjściowe z listą interfejsów, takich jak br-lan, ethx, wlanx itd.

### Znajdowanie adresu MAC portów Ethernet

Posłużmy się poniższym przykładem.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

- **eth0** to port WAN z adresem MAC **94:83:C4:19:19:08**.

    Jeśli router ma dodatkowy port WAN (np. GL-MT6000), będzie miał również dodatkowy adres WAN MAC.

- **eth1**, **eth2** itd. to porty LAN z adresem MAC **94:83:C4:19:19:09**.

    Nawet jeśli portów LAN jest więcej niż jeden, wszystkim będzie przypisany jeden adres MAC.

### Znajdowanie adresu MAC interfejsów bezprzewodowych

Posłużmy się poniższym przykładem.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** to Wi-Fi 2.4G z adresem MAC **96:83:C4:19:19:0B**.

- **wlan1** to Wi-Fi 5G z adresem MAC **94:83:C4:19:19:0A**.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
