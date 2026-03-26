# Comment trouver toutes les adresses MAC de mon appareil ?

## Cas d'usage

Les adresses MAC d'un appareil GL.iNet sont uniques pour chaque interface réseau, par exemple WAN 1, WAN 2, les ports LAN, le Wi-Fi 2.4G et le Wi-Fi 5G.

Lorsque vous vous connectez dans certains hôtels, campings ou campus, l'administrateur réseau peut vous demander l'adresse MAC de votre appareil afin de l'ajouter à la liste blanche avant de vous autoriser l'accès à Internet.

Vous pouvez retrouver l'adresse MAC exacte de votre appareil en utilisant les méthodes suivantes.

## Méthode 1 : via l'étiquette du produit (adresse MAC WAN uniquement)

Relevez l'**adresse MAC WAN** sur l'étiquette située sous l'appareil.

Par exemple, l'adresse MAC WAN est E4:95:6E:40:DB:A9 dans l'image ci-dessous.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

## Méthode 2 : via SSH

Consultez [cette page](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) pour savoir comment utiliser SSH.

Saisissez **ifconfig** dans la session SSH ; vous obtiendrez alors des données affichant successivement des interfaces comme br-lan, ethx, wlanx, etc.

### Trouver l'adresse MAC des ports Ethernet

Prenons l'image suivante comme exemple.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

- **eth0** correspond au port WAN, avec l'adresse MAC **94:83:C4:19:19:08**. 

    S'il existe un port WAN supplémentaire (par exemple sur le GL-MT6000), il y aura une adresse MAC WAN supplémentaire.

- **eth1**, **eth2**, etc. correspondent aux ports LAN, avec l'adresse MAC **94:83:C4:19:19:09**. 

    Il n'y a qu'une seule adresse MAC, même s'il y a plusieurs ports LAN.

### Trouver l'adresse MAC des interfaces sans fil

Prenons l'image suivante comme exemple.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** correspond au Wi-Fi 2.4G, avec l'adresse MAC **96:83:C4:19:19:0B**.

- **wlan1** correspond au Wi-Fi 5G, avec l'adresse MAC **94:83:C4:19:19:0A**.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
