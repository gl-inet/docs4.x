# Guida utente di Spitz (GL-X750)

## Panoramica del prodotto

Spitz è un router wireless dual-band 3G/4G, ampiamente utilizzato in ambito smart home e IoT. Basato su OpenWRT OS, consente di compilare un firmware personalizzato adatto a diversi scenari applicativi. Integra un modulo mini PCIe 3G/4G per supportare operatori differenti e può essere utilizzato in tutto il mondo.

Spitz V2 (GL-X750V2) è la versione avanzata di Spitz (GL-X750). Include una PCBA riprogettata e antenne ottimizzate per migliorare le prestazioni 4G.

![gl-x750 interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/hardware_info/x750v2_interface.jpg){class="glboxshadow"}

## Specifiche

[Specifiche di GL-X750](https://www.gl-inet.com/products/gl-x750/#specs){target="_blank"}

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

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_ethernet.png){class="glboxshadow"}

### Repeater

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. In qualità di repeater, riceve e ritrasmette i segnali wireless entro il proprio raggio d'azione, estendendone così la copertura. Questo metodo è utile quando un singolo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come connetterti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_repeater.png){class="glboxshadow"}

### Tethering

Collega la porta USB del router a uno smartphone con dati mobili attivi tramite un cavo USB per accedere a Internet. Questo metodo consente a più dispositivi collegati al router di usare la connessione dati mobile dello smartphone per accedere a Internet.

[Fai clic qui per scoprire come connetterti a Internet tramite tethering USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_tethering.png){class="glboxshadow"}

### Cellular
 
Inserisci una SIM nello slot SIM del router per connetterlo a Internet. Questo metodo è utile per condividere l'accesso a Internet di una singola SIM con tutti i dispositivi collegati.

[Fai clic qui per scoprire come connetterti a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x750/internet/x750_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet contemporaneamente, ad esempio Ethernet, Repeater e Cellular. Se la connessione Internet con priorità più alta si interrompe, il router passerà automaticamente a un'altra connessione Internet. Questa funzione è chiamata anche failover e garantisce un accesso a Internet fluido e senza interruzioni.

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorità di ciascuna connessione Internet.

In alternativa, puoi cambiare la modalità Multi-WAN da Failover a Load Balance, così da utilizzare più interfacce di rete contemporaneamente per aumentare la larghezza di banda totale del router.

---

## Wi-Fi

Le impostazioni wireless consentono agli utenti di gestire la sicurezza della rete Wi-Fi principale e del Wi-Fi ospite. È possibile accedervi andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di più sulla configurazione wireless](../../interface_guide/wireless.md)

---

## Client

I client sono i dispositivi collegati al router; puoi bloccarli o limitarne la velocità di rete. L'interfaccia è accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di più sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano più di 30 servizi VPN. Il router crittografa automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi i dispositivi ospiti e i dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche funzionare come server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima dell'accesso a Internet pubblico.

### Dashboard VPN

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN

Fai riferimento ai link seguenti per una guida passo dopo passo:

- [**Configurare il client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurare il server OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard

Fai riferimento ai link seguenti per una guida passo dopo passo:

- [**Configurare il client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurare il server WireGuard**](../../interface_guide/wireguard_server.md)

---

## Applicazioni

I router GL.iNet includono un'ampia gamma di funzioni aggiuntive che semplificano la gestione dei dispositivi, migliorano l'esperienza Internet dell'utente, automatizzano l'aggiornamento del firmware e molto altro.

### Plug-in

Consulta la guida [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS

Consulta la guida [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud

Consulta la guida [**GoodCloud**](../../interface_guide/cloud.md).

### Controllo genitori

Consulta la guida [**Parental Control**](../../interface_guide/parental_control.md).

---

## Rete

### Firewall

I router GL.iNet includono numerose funzioni firewall per garantire una connessione sicura e un controllo completo da parte dell'utente. Consentono di configurare regole firewall, tra cui port forwarding, porte aperte e DMZ.

[Fai clic qui per saperne di più sul firewall dei router GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN

Consulta la guida [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN

Consulta la guida [**LAN**](../../interface_guide/lan.md).

### DNS

Consulta la guida [**DNS**](../../interface_guide/dns.md).

### Modalità di rete

Consulta la guida [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6

Consulta la guida [**IPv6**](../../interface_guide/ipv6.md).

### Indirizzo MAC

La pagina Mac Address in precedenza si chiamava Mac Clone ed è stata rinominata Mac Address dalla versione v4.2.

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

GL.iNet fornisce aggiornamenti regolari del firmware dei propri router per migliorare le prestazioni, risolvere bug e correggere vulnerabilità.

Consulta la guida [**Upgrade**](../../interface_guide/upgrade.md).

### Attività pianificate

Consulta la guida [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Password amministratore

Questa funzione è stata spostata in [**Security**](../../interface_guide/security.md) dalla versione v4.5.

Consulta la guida [**Admin Password**](../../interface_guide/admin_password.md).

### Fuso orario

Consulta la guida [**Time Zone**](../../interface_guide/time_zone.md).

### Log

Consulta la guida [**Log**](../../interface_guide/log.md).

### Sicurezza

Questa funzione è disponibile dalla versione v4.5.

Consulta la guida [**Security**](../../interface_guide/security.md).

### Ripristino firmware

Consulta la guida [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Impostazioni avanzate

Consulta la guida [**Advanced Settings**](../../interface_guide/advanced_settings.md).
