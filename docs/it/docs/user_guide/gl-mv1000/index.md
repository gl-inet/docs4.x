# Guida utente di Brume (GL-MV1000)

## Panoramica del prodotto

Brume (GL-MV1000) e Brume-W (GL-MV1000W) sono prodotti di rete potenti e stabili, progettati per offrire capacità di elaborazione avanzate. Grazie al chipset Marvell ad alte prestazioni, Brume e Brume-W* possono eseguire crittografia di ultima generazione a velocità impressionanti, offrendo un'eccellente esperienza di routing VPN. Con OpenWrt preinstallato e il supporto a Ubuntu, Brume e Brume-W* consentono sviluppi approfonditi per progetti IoT commerciali.

Brume-W (GL-MV1000W) è l'edizione speciale di Brume (GL-MV1000) con modulo Wi-Fi integrato, che offre connettività Wi-Fi ad alta velocità sulla banda 2,4 GHz fino a 300 Mbps.

## Specifiche

[Specifiche di GL-MV1000](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## Configurazione iniziale

Tutti i router GL.iNet seguono un processo di configurazione simile. [Fai clic qui per sapere come eseguire la configurazione iniziale](../../faq/first_time_setup.md/).

---

## INTERNET

Accedi al pannello di amministrazione web del router e, dal menu laterale, vai a **INTERNET**.

Questa pagina consente di selezionare il tipo di connessione Internet, ad esempio Ethernet, Repeater, Tethering e Cellular, in base al modello.

Per Brume (GL-MV1000), sono supportati tre tipi di connessione: Ethernet, Tethering e Cellular.

### Ethernet

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. In genere questo metodo offre la connessione Internet più veloce e affidabile.

[Fai clic qui per scoprire come connetterti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering

Collega la porta USB del router a uno smartphone con dati mobili attivi tramite un cavo USB per accedere a Internet. Questo metodo consente a più dispositivi collegati al router di usare la connessione dati mobile dello smartphone per accedere a Internet.

[Fai clic qui per scoprire come connetterti a Internet tramite tethering USB](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular
 
Collega il router a Internet inserendo un modem USB cellulare nella porta USB del router. Questo metodo è utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

[Fai clic qui per scoprire come connetterti a Internet tramite modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN

Multi-WAN è una funzione di rete che consente di configurare il router con più connessioni Internet contemporaneamente, ad esempio Ethernet e Repeater. Se la connessione Internet con priorità più alta si interrompe, il router passerà automaticamente a un'altra connessione Internet. Questa funzione è chiamata anche failover e garantisce un accesso a Internet fluido e senza interruzioni.

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorità di ciascuna connessione Internet.

In alternativa, puoi cambiare la modalità Multi-WAN da Failover a Load Balance, così da utilizzare più interfacce di rete contemporaneamente per aumentare la larghezza di banda totale del router.

---

## Client

I client sono i dispositivi collegati al router; puoi bloccarli o limitarne la velocità di rete. L'interfaccia è accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di più sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano più di 30 servizi VPN. Il router crittografa automaticamente tutto il traffico di rete all'interno della rete collegata, inclusi i dispositivi ospiti e i dispositivi client che non sono in grado di eseguire la crittografia VPN. I nostri router possono anche funzionare come server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima dell'accesso a Internet pubblico.

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

### Tailscale

Consulta la guida [**Tailscale**](../../interface_guide/tailscale.md).

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

### Impostazioni del pulsante di commutazione

Consulta la guida [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log

Consulta la guida [**Log**](../../interface_guide/log.md).

### Sicurezza

Questa funzione è disponibile dalla versione v4.5.

Consulta la guida [**Security**](../../interface_guide/security.md).

### Ripristino firmware

Consulta la guida [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Impostazioni avanzate

Consulta la guida [**Advanced Settings**](../../interface_guide/advanced_settings.md).
