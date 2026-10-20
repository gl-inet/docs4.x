# Guida utente di Slate (GL-AR750S) {#slate-gl-ar750s-user-guide}

## Panoramica del prodotto {#product-overview}

Slate (GL-AR750S) e il nostro primo router da viaggio AC Gigabit dual-band. Con 3 porte Ethernet Gigabit, puo offrire velocita piu elevate durante i viaggi. Inoltre, la memoria Flash da 128 MB fornisce dual flash per maggiore spazio di archiviazione e una velocita operativa superiore. Dispone di uno slot MicroSD (TF) che espande lo spazio di archiviazione fino a 128 GB.

![gl-ar750sinterface](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/hardware_info/ar750s_interface.jpg){class="glboxshadow"}

## Contenuto della confezione {#package-contents}

Tieni presente che l'adattatore incluso nella confezione dipende dal Paese di spedizione.

La confezione include:

- 1 x Manuale utente
- 1 x Slate (GL-AR750S)
- 1 x Cavo Ethernet
- 1 x Biglietto di ringraziamento
- 1 x Scheda di garanzia
- 1 x Alimentatore, tipo di spina selezionato

![gl-ar750s unboxing](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/first_time_setup/ar750s_unboxing.jpg){class="glboxshadow"}

## Specifiche {#specifications}

[Specifiche GL-AR750S](https://www.gl-inet.com/products/gl-ar750s/#specs){target="_blank"}

## Configurazione iniziale {#first-time-setup}

Tutti i router GL.iNet hanno un processo di configurazione simile. [Fai clic qui per conoscere la configurazione iniziale](../../faq/first_time_setup.md).

## INTERNET {#internet}

Accedi al pannello di amministrazione web del router e vai su **INTERNET** dal menu laterale sinistro.

Questa pagina ti consente di selezionare il tipo di connessione Internet, ad esempio Ethernet, Repeater, Tethering e Cellular.

### Ethernet {#ethernet}

Collega il router a un modem attivo o a un dispositivo di rete attivo tramite un cavo Ethernet per accedere a Internet. Questo metodo di solito offre la connessione Internet piu veloce e affidabile.

[Fai clic qui per scoprire come collegarti a Internet tramite cavo Ethernet](../../interface_guide/internet_ethernet.md)

![Ethernet Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Configura il router come repeater per estendere la copertura Wi-Fi di una rete Wi-Fi esistente. Come repeater, riceve e ritrasmette i segnali wireless all'interno del proprio raggio d'azione, estendendone cosi la copertura. Questo metodo e utile quando un solo router non riesce a coprire l'intera area di utilizzo.

[Fai clic qui per scoprire come collegarti a Internet tramite una rete Wi-Fi esistente](../../interface_guide/internet_repeater.md)

![Repeater Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_repeater.png){class="glboxshadow"}

### Tethering {#tethering}

Collega la porta USB del router a uno smartphone con dati mobili attivi tramite un cavo USB per accedere a Internet. Questo metodo consente a piu dispositivi collegati al router di accedere a Internet usando i dati mobili dello smartphone.

[Fai clic qui per scoprire come collegarti a Internet tramite USB tethering](../../interface_guide/internet_tethering.md)

![Tethering Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_tethering.png){class="glboxshadow"}

### Cellular {#cellular}
 
Collega il router a Internet inserendo un modem USB con supporto cellulare nella porta USB del router. Questo metodo e utile per condividere la connessione Internet di un modem USB con tutti i dispositivi collegati.

[Fai clic qui per scoprire come collegarti a Internet tramite modem USB](../../interface_guide/internet_cellular.md)

![Cellular Connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ar750s/internet/ar750s_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN e una funzione di rete che consente di configurare il router con piu connessioni Internet, ad esempio Ethernet e Repeater, contemporaneamente. Se la connessione Internet con priorita piu alta si interrompe, il router passera automaticamente a un'altra connessione Internet. Questa funzione e chiamata anche Failover e garantisce un accesso a Internet fluido e ininterrotto.

Vai a [Multi-WAN](../../interface_guide/multi-wan.md) per impostare la priorita di ciascuna connessione Internet.

In alternativa, puoi cambiare la modalita Multi-WAN da Failover a Load Balance, che ti consente di usare piu interfacce di rete contemporaneamente per aumentare la larghezza di banda totale del router.

---

## WIRELESS {#wireless}

Le impostazioni wireless consentono agli utenti di gestire la sicurezza di rete del Wi-Fi principale e del Wi-Fi ospite. Sono accessibili andando su **WIRELESS** nel menu laterale.

[Fai clic qui per saperne di piu sulla configurazione wireless](../../interface_guide/wireless.md)

---

## CLIENTS {#clients}

I client sono dispositivi collegati al router. Puoi bloccarli o limitarne la velocita di rete. L'interfaccia e accessibile facendo clic su **CLIENTS** nel menu laterale del pannello di amministrazione del router.

[Fai clic qui per saperne di piu sulla gestione dei client del dispositivo.](../../interface_guide/clients.md)

---

## VPN {#vpn}

I router GL.iNet sono preinstallati con OpenVPN e WireGuard® e supportano oltre 30 servizi VPN. Quando il client VPN è abilitato, il router può crittografare il traffico dei dispositivi della rete, inclusi quelli che non possono eseguire app VPN, in base alle impostazioni dei criteri VPN. I nostri router possono anche agire da server VPN, reindirizzando il traffico dei dispositivi client in posizioni remote verso il server VPN tramite un tunnel VPN prima di accedere alla rete Internet pubblica.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Configurare il server OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Fai riferimento ai link seguenti per una guida di configurazione passo dopo passo:

- [**Configurare il client WireGuard**](../../interface_guide/wireguard_client.md)
- [**Configurare il server WireGuard**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## APPLICATIONS {#applications}

I router GL.iNet includono un'ampia gamma di funzioni aggiuntive che semplificano la gestione del dispositivo, migliorano l'esperienza Internet dell'utente, automatizzano l'aggiornamento firmware e altro ancora.

### Plug-ins {#plug-ins}

Visita il tutorial [**Plug-ins**](../../interface_guide/plugins.md).

### Dynamic DNS {#dynamic-dns}

Visita il tutorial [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Visita il tutorial [**GoodCloud**](../../interface_guide/cloud.md).

### Network Storage {#network-storage}

Visita il tutorial [**Network Storage**](../../interface_guide/network_storage.md).

### Parental Control {#parental-control}

Visita il tutorial [**Parental Control**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Visita il tutorial [**ZeroTier**](../../interface_guide/zerotier.md).

---

## NETWORK {#network}

### Firewall {#firewall}

I router GL.iNet includono diverse funzioni firewall per garantire una connessione sicura e un controllo completo da parte degli utenti. Consentono di configurare regole firewall, tra cui Port Forwarding, Open Ports e DMZ.

[Fai clic qui per saperne di piu sul firewall dei router GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Visita il tutorial [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Visita il tutorial [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Visita il tutorial [**DNS**](../../interface_guide/dns.md).

### Network Mode {#network-mode}

Visita il tutorial [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Visita il tutorial [**IPv6**](../../interface_guide/ipv6.md).

### MAC Address {#mac-address}

La pagina Mac Address si chiamava in precedenza Mac Clone ed e stata rinominata Mac Address a partire dalla v4.2.

Visita il tutorial [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Visita il tutorial [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Visita il tutorial [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## SYSTEM {#system}

### Overview {#overview}

Visita il tutorial [**System Overview**](../../interface_guide/system_overview.md).

### Upgrade {#upgrade}

GL.iNet rilascia aggiornamenti regolari del firmware dei router per migliorare le prestazioni, risolvere bug e correggere vulnerabilita.

Visita il tutorial [**Upgrade**](../../interface_guide/upgrade.md).

### Scheduled Tasks {#scheduled-tasks}

Visita il tutorial [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Admin Password {#admin-password}

Questa funzione e stata spostata in [**Security**](../../interface_guide/security.md) a partire dalla v4.5.

Visita il tutorial [**Admin Password**](../../interface_guide/admin_password.md).

### Time Zone {#time-zone}

Visita il tutorial [**Time Zone**](../../interface_guide/time_zone.md).

### Toggle Button Settings {#toggle-button-settings}

Visita il tutorial [**Toggle Button Settings**](../../interface_guide/toggle_button_settings.md).

### Log {#log}

Visita il tutorial [**Log**](../../interface_guide/log.md).

### Security {#security}

Questa funzione e disponibile a partire dalla v4.5.

Visita il tutorial [**Security**](../../interface_guide/security.md).

### Reset Firmware {#reset-firmware}

Visita il tutorial [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Advanced Settings {#advanced-settings}

Visita il tutorial [**Advanced Settings**](../../interface_guide/advanced_settings.md).
