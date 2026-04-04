# Guida utente di Cirrus (GL-AP1300)

## Panoramica del prodotto

Cirrus (GL-AP1300), punto di accesso wireless da soffitto, e un gateway di livello business di fascia alta con soluzione Wi-Fi MU-MIMO. L'alimentazione PoE e la funzione integrata del timer Watchdog sono implementate per soddisfare la maggior parte degli scenari di utilizzo a livello enterprise. Con il sistema di gestione GoodCloud ben sviluppato, gestire il dispositivo e molto semplice e comodo. Puoi abilitare un accesso remoto e sicuro ovunque ti trovi e in qualsiasi momento.

![gl-ap1300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Specifiche

[Specifiche GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

---

## Configurazione iniziale

Tutti i router GL.iNet hanno un processo di configurazione simile. [Fai clic qui per conoscere la configurazione iniziale](../../faq/first_time_setup.md/).

---

## INTERNET

Accedi al pannello di amministrazione web del router e vai su **INTERNET** dal menu laterale sinistro.

Questa pagina ti consente di selezionare il tipo di connessione Internet, come Ethernet, Repeater, Tethering e Cellular, a seconda del modello.

Per Cirrus (GL-AP1300), sono supportati due tipi di connessione: Ethernet e Repeater.

### Ethernet

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. Questo metodo di solito offre la connessione Internet piu veloce e affidabile.

[Fai clic qui per scoprire come collegarti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

### Repeater

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. Come repeater, riceve e ritrasmette i segnali wireless all'interno del proprio raggio d'azione, estendendone cosi la copertura. Questo metodo e utile quando un solo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come collegarti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

### Multi-WAN

Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio Ethernet e Repeater, contemporaneamente. Se la connessione Internet con priorita piu alta si interrompe, il router passera automaticamente a un'altra connessione Internet. Questa funzione e chiamata anche Failover e garantisce un accesso a Internet fluido e ininterrotto.

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorita di ciascuna connessione Internet.

In alternativa, puoi cambiare la modalita Multi-WAN da Failover a Load Balance, che ti consente di usare piu interfacce di rete contemporaneamente per aumentare la larghezza di banda totale del router.

---

## WIRELESS

Le impostazioni wireless consentono agli utenti di gestire la sicurezza di rete del Wi-Fi principale e del Wi-Fi ospite. Sono accessibili andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di piu sulla configurazione wireless](../../interface_guide/wireless.md)

---

## CLIENTS

I client sono dispositivi collegati al router. Puoi bloccarli o limitarne la velocita di rete. L'interfaccia e accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di piu sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano oltre 30 servizi VPN. Crittografano automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi i dispositivi ospiti e i dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche agire da server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima di accedere alla rete Internet pubblica.

### VPN Dashboard

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurare il server OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurare il server WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS

I router GL.iNet includono un'ampia gamma di funzioni aggiuntive che semplificano la gestione del dispositivo, migliorano l'esperienza Internet dell'utente, automatizzano l'aggiornamento firmware e altro ancora.

### Plug-ins

Visita il tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Visita il tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Visita il tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home

Visita il tutorial [**AdGuard Home**](../../interface_guide/adguardhome.md).

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

### Log

Visita il tutorial [**Log**](../../interface_guide/log.md).

### Security

Questa funzione e disponibile dalla v4.5.

Visita il tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware

Visita il tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Visita il tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
