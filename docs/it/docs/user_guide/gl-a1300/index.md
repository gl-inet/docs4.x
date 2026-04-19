# Guida utente di Slate Plus (GL-A1300)

## Panoramica del prodotto

Slate Plus (GL-A1300) e un router da viaggio tascabile con una CPU potente, ottimizzata per la stabilita di rete e per l'elaborazione efficiente della crittografia VPN. Include le nostre piu recenti funzioni di sicurezza e utilizza l'ultima versione del sistema operativo OpenWrt. E progettato per viaggiatori frequenti che fanno un uso intensivo delle reti VPN.

![GL-A1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/hardware_info/gl-a1300_interface.jpg){class="glboxshadow"}

## Contenuto della confezione

Tieni presente che l'adattatore incluso nella confezione dipende dal Paese di spedizione.

La confezione include:

- 1 x Manuale utente
- 1 x Slate Plus (GL-A1300)
- 1 x Cavo Ethernet
- 1 x Scheda di garanzia
- 1 x Alimentatore, tipo di spina selezionato

![gl-a1300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/first_time_setup/gl-a1300_unboxing.jpg){class="glboxshadow"}

## Indicazioni LED

[Indicazioni LED](../../faq/led.md#gl-a1300)

## Specifiche

[Specifiche GL-A1300](https://www.gl-inet.com/products/gl-a1300/#specs){target="_blank"}

## Configurazione iniziale

Tutti i router GL.iNet hanno un processo di configurazione semplice e quasi identico. [Fai clic qui per conoscere la configurazione iniziale](../../faq/first_time_setup.md/).

Per configurare Slate Plus, puoi usare uno dei quattro metodi di connessione Internet supportati: Ethernet, Repeater, Tethering e Cellular. Fai riferimento a questo video di configurazione.

<iframe width="560" height="315" src="https://www.youtube.com/embed/zhY7AqmKJAc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

## INTERNET

L'interfaccia di configurazione Internet consente agli utenti di scegliere il tipo di connessione Internet supportato dal router.

Configura la rete Internet selezionando **INTERNET** nel menu laterale del pannello di amministrazione web del router.

Supporta quattro modalita di connessione a Internet, elencate di seguito:

### Ethernet

Trasmette i dati tramite un cavo Ethernet, collegando il router a un modem attivo o a un dispositivo di rete attivo. Questo metodo di solito offre la connessione Internet piu veloce e affidabile.

[Fai clic qui per scoprire come collegarti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_ethernet.png){class="glboxshadow"}

### Repeater

Estende l'area di copertura Wi-Fi di una rete Wi-Fi esistente usando il router per ricevere i segnali wireless nel raggio di copertura e inoltrarli piu lontano. Questo metodo e molto utile quando un singolo router non ha una copertura sufficiente per l'intera area di utilizzo.

[Fai clic qui per scoprire come collegarti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_repeater.png){class="glboxshadow"}

### Tethering

Stabilisce l'accesso a Internet con i dispositivi collegati condividendo tramite cavo i dati mobili di uno smartphone con il router. Questo metodo e utile quando gli utenti vogliono usare i dati del telefono per accedere a Internet.

[Fai clic qui per scoprire come collegarti a Internet tramite USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_tethering.png){class="glboxshadow"}

### Cellular

Collega il router a Internet inserendo un modem USB con supporto cellulare nella porta USB del router. Questo metodo e utile per condividere l'accesso a Internet di un modem USB con tutti i dispositivi collegati.

[Fai clic qui per scoprire come collegarti a Internet tramite modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-a1300/internet/a1300_cellular.png){class="glboxshadow"}

### Priorita e bilanciamento del carico

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorita di ciascun metodo di accesso a Internet o il bilanciamento del carico quando vengono usati contemporaneamente piu metodi di accesso.

---

## WIRELESS

Le impostazioni wireless consentono agli utenti di gestire la sicurezza di rete del Wi-Fi principale e del Wi-Fi ospite. Sono accessibili andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di piu sulla configurazione wireless](../../interface_guide/wireless.md)

---

## CLIENTS

I client sono i dispositivi collegati al router. Puoi bloccarli o limitarne la velocita di rete. L'interfaccia e accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di piu sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano oltre 30 servizi VPN. Crittografano automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi i dispositivi ospiti e i dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche agire da server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima di accedere alla rete Internet pubblica.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurare il server OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurare il server WireGuard**](../../interface_guide/wireguard_server.md)

---

## APPLICATIONS

I router GL.iNet includono un'ampia gamma di funzioni aggiuntive che semplificano la gestione del dispositivo, migliorano l'esperienza Internet dell'utente, automatizzano l'aggiornamento firmware e altro ancora.

### Plug-ins

Visita il tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Visita il tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Visita il tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage

Visita il tutorial [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home

Visita il tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Parental Control

Visita il tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier

Visita il tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale

Visita il tutorial [**Tailscale**](../../interface_guide/tailscale.md).

---

## NETWORK

### Firewall

I router GL.iNet includono piu funzioni firewall per garantire una connessione sicura e un controllo completo da parte degli utenti. Consentono di configurare regole firewall, incluse Port Forwarding, Open Ports e DMZ.

[Fai clic qui per saperne di piu sul firewall dei router GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Visita il tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Visita il tutorial [**LAN**](../../interface_guide/lan.md).

### DNS

Visita il tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode

Visita il tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Visita il tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address

La pagina MAC Address era precedentemente chiamata Mac Clone ed e stata rinominata in MAC Address dalla v4.2.

Visita il tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Visita il tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Visita il tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Visita il tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet fornisce aggiornamenti regolari del firmware dei router per migliorare le prestazioni, risolvere bug e correggere vulnerabilita.

Visita il tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks

Visita il tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Questa funzione e stata spostata in [**Security**](../../interface_guide/security.md) dalla v4.5.

Visita il tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Visita il tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings

Visita il tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Visita il tutorial [**Log**](../../interface_guide/log.md).

### Security

Questa funzione e disponibile dalla v4.5.

Visita il tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware

Visita il tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Visita il tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
