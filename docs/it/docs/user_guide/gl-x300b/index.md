# Guida utente di Collie (GL-X300B)

## Panoramica del prodotto

Collie (GL-X300B) è un gateway cellulare industriale progettato per funzionare ad alte temperature e in scenari con potenziali rischi fisici. Esistono tre versioni di Collie, progettate per operare in impianti fissi al chiuso (GL-X300B-RS485 / GL-X300B-BLE) oppure in veicoli di trasporto (GL-X300B-GPS). Collie è ideale per la comunicazione machine-to-machine tra dispositivi elettrici in ambienti con elevato rumore elettrico.

![gl-x300b interface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/gl-x300b_interface.jpg){class="glboxshadow"}

**Qual è la differenza tra GL-X300B-RS485, GL-X300B-BLE e GL-X300B-GPS?**

![gl-x300b series](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b_series.png){class="glboxshadow"}

![gl-x300b comparison](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/model_comparison.png){class="glboxshadow"}

- **GL-X300B-RS485** include un chip RS485 con interfaccia RS485. Il modulo supporta la trasmissione dati bidirezionale di vari dispositivi nel campo dell'automazione industriale e dell'IoT, realizzando così funzioni di acquisizione dati, controllo e monitoraggio.

- **GL-X300B-BLE** è dotato di tre antenne omnidirezionali esterne per comunicazioni Wi-Fi 2.4GHz, 4G LTE e BLE, in grado di ricevere segnali da tutte le direzioni e offrire grande flessibilità di installazione in ambienti industriali.

- **GL-X300B-GPS** è dotato di cinque antenne esterne, tra cui due antenne Wi-Fi 2.4GHz, due antenne 4G LTE e un'antenna GPS. Le antenne cablate estendibili sono ideali per avere più posizioni di ricezione all'interno di un veicolo, riducendo al minimo i punti ciechi di ricezione durante gli spostamenti in città ad alta densità di rete.

!!! Note

    Le versioni BLE e GPS sono disponibili con quantitativo minimo d'ordine.

## Contenuto della confezione

La confezione include:

- 1 x Manuale utente
- 1 x Collie (GL-X300B-RS485) (garanzia di 2 anni)
- 1 x Cavo Ethernet
- 1 x Antenna esterna 4G
- 2 x Antenne esterne Wi-Fi
- 1 x Morsettiera (verde)
- 1 x Kit per montaggio a parete
- 1 x Kit per guida DIN
- 1 x Alimentatore
- 4 x Adattatori (spine US, UK, EU e AU) (garanzia di tre mesi)

![gl-x300b package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/hardware_info/x300b-rs485_package.jpg){class="glboxshadow"}

## Specifiche

[Specifiche di GL-X300B](https://www.gl-inet.com/products/gl-x300b/#specs){target="_blank"}

## Configurazione iniziale

Tutti i router GL.iNet seguono un processo di configurazione simile. [Fai clic qui per sapere come eseguire la configurazione iniziale](../../faq/first_time_setup.md/).

## INTERNET

Accedi al pannello di amministrazione web del router e, dal menu laterale, vai a **INTERNET**.

Questa pagina consente di selezionare il tipo di connessione Internet, ad esempio Ethernet, Repeater, Tethering e Cellular, in base al modello.

Per Collie (GL-X300B) sono supportati tre tipi di connessione: Ethernet, Repeater e Cellular.

### Ethernet

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. In genere questo metodo offre la connessione Internet più veloce e affidabile.

[Fai clic qui per scoprire come connetterti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_ethernet.png){class="glboxshadow"}

### Repeater

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. In qualità di repeater, riceve e ritrasmette i segnali wireless entro il proprio raggio d'azione, estendendone così la copertura. Questo metodo è utile quando un singolo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come connetterti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_repeater.png){class="glboxshadow"}

### Cellular

Inserisci una SIM nello slot SIM del router per connetterlo a Internet. Questo metodo è utile per condividere l'accesso a Internet di una singola SIM con tutti i dispositivi collegati.

[Fai clic qui per scoprire come connetterti a Internet tramite rete cellulare](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-x300b/internet/x300b_cellular.png){class="glboxshadow"}

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
