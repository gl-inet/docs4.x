# Come posso trovare tutti gli indirizzi MAC del mio dispositivo?

## Scenario d'uso

Gli indirizzi MAC dei dispositivi GL.iNet sono univoci per ogni interfaccia di rete, come WAN 1, WAN 2, porte LAN, Wi-Fi 2.4G e Wi-Fi 5G.

Quando ti colleghi ad alcuni hotel, campeggi o campus, l'amministratore della rete potrebbe chiederti l'indirizzo MAC del dispositivo per registrarlo nella whitelist prima di concedere l'accesso a Internet.

Puoi trovare l'indirizzo o gli indirizzi MAC esatti del dispositivo con i seguenti metodi.

## Metodo 1. Tramite etichetta del prodotto (solo per il MAC WAN)

Trova il **WAN MAC address** sull'etichetta inferiore.

Ad esempio, nell'immagine seguente il WAN MAC è E4:95:6E:40:DB:A9.

![wan_lan_wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/wan_lan_wifi.png){class="glboxshadow"}

## Metodo 2. Tramite SSH

Consulta [qui](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/) come usare SSH.

Digita **ifconfig** nella sessione SSH. Riceverai un output con alcune informazioni, che mostrano in sequenza interfacce come br-lan, ethx, wlanx e così via.

### Trovare il MAC delle porte Ethernet

Prendi come esempio l'immagine seguente.

![ifconfigwan](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwan.jpg){class="glboxshadow"}

- **eth0** è la porta WAN, con indirizzo MAC **94:83:C4:19:19:08**.

    Se è presente un'altra porta WAN (ad esempio GL-MT6000), ci sarà un altro indirizzo WAN MAC.

- **eth1**, **eth2** e così via sono le porte LAN, con indirizzo MAC **94:83:C4:19:19:09**.

    Anche se le porte LAN sono più di una, ci sarà un solo indirizzo MAC.

### Trovare il MAC delle porte wireless

Prendi come esempio l'immagine seguente.

![ifconfigwifi](https://static.gl-inet.com/docs/router/en/4/tutorials/where_to_find_the_device_id_mac_sn/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** è il Wi-Fi 2.4G, con indirizzo MAC **96:83:C4:19:19:0B**.

- **wlan1** è il Wi-Fi 5G, con indirizzo MAC **94:83:C4:19:19:0A**.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
