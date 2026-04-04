# Guida utente di Puli (GL-XE300)

## Panoramica del prodotto

Puli (GL-XE300) è un router smart 4G portatile, perfetto per la casa, i viaggi, il lavoro e le soluzioni IoT. Grazie al supporto OpenWrt e alla compatibilità con grandi capacità di archiviazione, è progettato per consentirti di sviluppare progetti IoT fai-da-te. Inoltre è dotato di una batteria ricaricabile, che ne permette l'uso portatile in diversi ambienti.

![gl-xe300 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/hardware_info/gl-xe300_interface.jpg){class="glboxshadow"}

## Contenuto della confezione

Tieni presente che l'adattatore incluso nella confezione dipende dal Paese di spedizione.

La confezione include:

- 1 x Manuale utente
- 1 x Puli (GL-XE300)
- 1 x Cavo Ethernet
- 1 x Biglietto di ringraziamento
- 1 x Scheda di garanzia
- 1 x Alimentatore (tipo di spina selezionato)

![gl-xe300 unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/first_time_setup/xe300_unboxing.jpg){class="glboxshadow"}

Guarda il [video di unboxing](../../video_library/unboxing_first_set_up.md/#gl-xe300-puli) di Puli.

## Specifiche

[Specifiche di GL-XE300](https://www.gl-inet.com/products/gl-xe300/#specs){target="_blank"}

---

## Configurazione iniziale

Tutti i router GL.iNet seguono un processo di configurazione simile. [Fai clic qui per sapere come eseguire la configurazione iniziale](../../faq/first_time_setup.md/).

---

## INTERNET

Accedi al pannello di amministrazione web del router e, dal menu laterale, vai a **INTERNET**.

Questa pagina consente di selezionare il tipo di connessione Internet, ad esempio Ethernet, Repeater, Tethering e Cellular.

### Ethernet

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. In genere questo metodo offre la connessione Internet più veloce e affidabile.

[Fai clic qui per scoprire come connetterti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_ethernet.png){class="glboxshadow"}

### Repeater

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. In qualita di repeater, riceve e ritrasmette i segnali wireless entro il proprio raggio d'azione, estendendone cosi la copertura. Questo metodo e utile quando un singolo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come connetterti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_repeater.png){class="glboxshadow"}

### Tethering

Collega la porta USB del router a uno smartphone con dati mobili attivi tramite un cavo USB per accedere a Internet. Questo metodo consente a piu dispositivi collegati al router di usare la connessione dati mobile dello smartphone per accedere a Internet.

[Fai clic qui per scoprire come connetterti a Internet tramite tethering USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_tethering.png){class="glboxshadow"}

### Cellular
 
Inserisci una SIM nello slot SIM per connetterti a Internet. Questo metodo e utile per condividere l'accesso a Internet di una singola SIM con tutti i dispositivi collegati.

[Fai clic qui per scoprire come connetterti a Internet tramite rete cellulare o modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-xe300/internet/xe300_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet contemporaneamente, ad esempio Ethernet e Repeater. Se la connessione Internet con priorita piu alta si interrompe, il router passera automaticamente a un'altra connessione Internet. Questa funzione e chiamata anche failover e garantisce un accesso a Internet fluido e senza interruzioni.

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorita di ciascuna connessione Internet.

In alternativa, puoi cambiare la modalita Multi-WAN da Failover a Load Balance, cosi da utilizzare piu interfacce di rete contemporaneamente per aumentare la larghezza di banda totale del router.

---

## Wi-Fi

Le impostazioni wireless consentono agli utenti di gestire la sicurezza della rete Wi-Fi principale e del Wi-Fi ospite. E possibile accedervi andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di piu sulla configurazione wireless](../../interface_guide/wireless.md)

---

## Client

I client sono i dispositivi collegati al router; puoi bloccarli o limitarne la velocita di rete. L'interfaccia e accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di piu sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano piu di 30 servizi VPN. Il router crittografa automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi i dispositivi ospiti e i dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche funzionare come server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima dell'accesso a Internet pubblico.

### Dashboard VPN

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard.md)

### OpenVPN

Fai riferimento ai link seguenti per una guida passo dopo passo:

- [**Configurare il client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurare il server OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Fai riferimento ai link seguenti per una guida passo dopo passo:

- [**Configurare il client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurare il server WireGuard**](../../interface_guide/wireguard_server.md)

### Tor

- [**Tor**](../../interface_guide/tor.md)

---

## Applicazioni

I router GL.iNet includono un'ampia gamma di funzioni aggiuntive che semplificano la gestione dei dispositivi, migliorano l'esperienza Internet dell'utente, automatizzano l'aggiornamento del firmware e molto altro.

### Plug-in

Consulta la guida [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Consulta la guida [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Consulta la guida [**GoodCloud**](../../interface_guide/cloud.md).

### Archiviazione di rete

Consulta la guida [**Network Storage**](../../interface_guide/network_storage.md).

### AdGuard Home

Consulta la guida [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Controllo genitori

Consulta la guida [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier

Consulta la guida [**ZeroTier**](../../interface_guide/zerotier.md).

---

## Rete

### Firewall

I router GL.iNet includono numerose funzioni firewall per garantire una connessione sicura e un controllo completo da parte dell'utente. Consentono di configurare regole firewall, tra cui port forwarding, porte aperte e DMZ.

[Fai clic qui per saperne di piu sul firewall dei router GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Consulta la guida [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Consulta la guida [**LAN**](../../interface_guide/lan.md).

### DNS

Consulta la guida [**DNS**](../../interface_guide/dns.md).

### Modalita di rete

Consulta la guida [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Consulta la guida [**IPv6**](../../interface_guide/ipv6.md).

### Indirizzo MAC

La pagina Mac Address in precedenza si chiamava Mac Clone ed e stata rinominata Mac Address dalla versione v4.2.

Consulta la guida [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway

Consulta la guida [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping

Consulta la guida [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## Sistema

### Panoramica

Consulta la guida [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade

GL.iNet fornisce aggiornamenti regolari del firmware dei propri router per migliorare le prestazioni, risolvere bug e correggere vulnerabilita.

Consulta la guida [**Upgrade**](../../interface_guide/upgrade.md).

### Attivita pianificate

Consulta la guida [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Password amministratore

Questa funzione e stata spostata in [**Security**](../../interface_guide/security.md) dalla versione v4.5.

Consulta la guida [**Admin Password**](../../interface_guide/admin_password.md).

### Fuso orario

Consulta la guida [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Consulta la guida [**Log**](../../interface_guide/log.md).

### Sicurezza

Questa funzione e disponibile dalla versione v4.5.

Consulta la guida [**Security**](../../interface_guide/security.md).

### Ripristino firmware

Consulta la guida [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Impostazioni avanzate

Consulta la guida [**Advanced Settings**](../../interface_guide/advanced_settings.md).
