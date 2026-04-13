# Guida utente di Mudi V2 (GL-E750V2)

**Note:** Mudi V2 (GL-E750V2) e Mudi (GL-E750) usano lo stesso firmware. Se stai usando Mudi (GL-E750), [aggiorna il firmware](https://dl.gl-inet.com/?model=e750) per usare le funzioni e le caratteristiche piu recenti.

## Panoramica del prodotto

Mudi V2 (GL-E750V2) e un router da viaggio 4G LTE portatile compatibile con operatori globali. E completamente open source su OpenWrt e sullo SDK 4.0 di GL.iNet, offrendo ampie possibilita di personalizzazione e numerose funzioni. Mudi V2 supporta velocita Wi-Fi di 300 Mbps (2,4 GHz) e 433 Mbps (5 GHz), una scheda MicroSD fino a 1 TB e integra una batteria da 7000 mAh. Supporta inoltre il multi-WAN, con failover e load balance, per garantire una connessione fluida a tutti i tuoi dispositivi.

![gl-e750v2 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/hardware_info/e750_interface.jpg){class="glboxshadow"}

## Pulsante

- Premi il pulsante di accensione per **3 secondi**: accende il dispositivo.

- Premi il pulsante di accensione per **3-5 secondi**: entra in Standby Mode.

- Premi il pulsante di accensione per **piu di 5 secondi**: spegne il dispositivo.

    Quando premi per 3 secondi, sullo schermo OLED verra prima mostrato "Standby Mode On". CONTINUA A TENERE PREMUTO il pulsante di accensione finche non vedi "Shut Down" sotto "Standby Mode On". Partira un conto alla rovescia di 3 secondi e il dispositivo si spegnera.

## Standby Mode

In Standby Mode, Mudi V2 disattiva Wi-Fi e 4G per risparmiare energia. In questa modalita non puoi collegarti a Mudi V2.

Per attivare o disattivare la Standby Mode, premi il pulsante di accensione per 3 secondi. Sullo schermo OLED verra mostrato "Standby Mode On" oppure "Standby Mode Off".

## Contenuto della confezione

![gl-e750v2 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/first_time_setup/e750v2_unboxing.jpg){class="glboxshadow"}

- 1 x Router portatile 4G LTE Mudi V2 (GL-E750V2)
- 1 x Alimentatore
- 4 x Convertitori (spine US, EU, UK e AU)
- 1 x Manuale utente
- 1 x Scheda di garanzia
- 1 x Cavo Ethernet
- 1 x Replicatore di porta USB-C
- 1 x Cavo USB-C to USB-C
- 1 x Cavo USB-A to USB-C
- 1 x Custodia
- 1 x Biglietto di ringraziamento

---

## Configurazione iniziale

Guarda questo video oppure segui i passaggi riportati di seguito per configurare Mudi V2.

<iframe width="560" height="315" src="https://www.youtube.com/embed/4FzEgmYyy7k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. Inserisci una scheda SIM

Inserisci una scheda SIM e, facoltativamente, una scheda MicroSD in Mudi V2.

Nota: se usi una scheda SIM, devi inserirla nel dispositivo prima di accenderlo.

1. Gira Mudi V2 sul lato posteriore.
2. Inserisci un dito nel foro vicino al bordo del coperchio.
3. Fai scorrere lungo il bordo.
4. Quando il coperchio si solleva leggermente, da circa 25 a 30 gradi, tiralo verso l'alto per aprirlo.
5. Inserisci la scheda nello slot come indicato dal simbolo vicino all'angolo.
6. Premi il coperchio verso il basso per richiuderlo.

### 2. Accensione

Premi il pulsante di accensione per accendere il dispositivo.

![gl-e750v2 poweron](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_power-on.png){class="glboxshadow"}

Quando Mudi V2 e spento, puoi comunque controllare lo stato della batteria premendo il pulsante di accensione. Lo schermo LED mostrera lo stato della batteria quando premi il pulsante.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_battery.png){class="glboxshadow"}

Assicurati di usare un alimentatore standard da 5V/2A. In caso contrario, il dispositivo potrebbe non funzionare correttamente.

![gl-e750v2 battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_charge.png){class="glboxshadow"}

---

## INTERNET

Accedi al pannello di amministrazione web del router e vai su **INTERNET** dal menu laterale sinistro.

Questa pagina consente di selezionare il tipo di connessione Internet, ad esempio Ethernet, Repeater, Tethering e Cellular.

### Ethernet

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. Questo metodo di solito offre la connessione Internet piu veloce e affidabile.

[Fai clic qui per scoprire come collegarti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_ethernet.png){class="glboxshadow"}

### Repeater

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. Come repeater, riceve e ritrasmette i segnali wireless all'interno del proprio raggio d'azione, estendendone cosi la copertura. Questo metodo e utile quando un solo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come collegarti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_repeater.png){class="glboxshadow"}

### Tethering

Collega la porta USB del router a uno smartphone con dati mobili attivi tramite un cavo USB per accedere a Internet. Questo metodo consente a piu dispositivi collegati al router di accedere a Internet usando i dati mobili dello smartphone.

[Fai clic qui per scoprire come collegarti a Internet tramite USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_tethering.png){class="glboxshadow"}

### Cellular

Rimuovi il coperchio posteriore di Mudi V2 e inserisci una scheda SIM nello slot per collegarti a Internet. Questo metodo e utile per condividere l'accesso a Internet di una singola scheda SIM con tutti i dispositivi collegati.

[Fai clic qui per scoprire come collegarti a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e750v2/internet/e750v2_cellular.png){class="glboxshadow"}

Per usare una scheda eSIM fisica sul tuo router GL.iNet, fai clic qui: [Come usare la scheda eSIM fisica con i router GL.iNet](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)

---

## WIRELESS

Le impostazioni wireless consentono agli utenti di gestire la sicurezza di rete del Wi-Fi principale e del Wi-Fi ospite. Sono accessibili andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di piu sulla configurazione wireless](../../interface_guide/wireless.md)

---

## CLIENTS

I client sono i dispositivi collegati al router. Puoi bloccare i client o limitarne la velocita di rete. L'interfaccia e accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di piu sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard e supportano oltre 30 servizi VPN. Crittografano automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi dispositivi ospiti e dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche agire da server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima di accedere alla rete Internet pubblica.

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

---

## NETWORK

### Firewall

I router GL.iNet includono diverse funzioni firewall per garantire una connessione sicura e un controllo completo da parte degli utenti. Consentono di configurare regole firewall, tra cui Port Forwarding, Open Ports e DMZ.

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

La pagina Mac Address si chiamava in precedenza Mac Clone ed e stata rinominata Mac Address a partire dalla v4.2.

Visita il tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### IGMP Snooping

Visita il tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM

### Overview

Visita il tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet rilascia aggiornamenti regolari del firmware dei router per migliorare le prestazioni, risolvere bug e correggere vulnerabilita.

Visita il tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### OLED Screen Settings

In questa pagina puoi regolare quali informazioni vengono mostrate sullo schermo OLED di Mudi V2.

### Scheduled Tasks

Visita il tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password

Questa funzione e stata spostata in [**Security**](../../interface_guide/security.md) a partire dalla v4.5.

Visita il tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone

Visita il tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings

Visita il tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Visita il tutorial [**Log**](../../interface_guide/log.md).

### Reset Firmware

Visita il tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings

Visita il tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
