# Come configurare Urban Shield VPN su un router GL.iNet

[Urban Shield VPN](https://urbanshieldvpn.com/) e' un provider VPN dedicato a offrire soluzioni VPN ad alta sicurezza e alte prestazioni agli utenti di tutto il mondo. Fornisce router VPN GL.iNet preconfigurati e piani di abbonamento flessibili, garantendo una navigazione sicura e privata. Basta attivare Urban Shield VPN sul router per essere protetti e ottenere accesso ai loro server globali, cosi' da navigare e guardare contenuti in streaming in tutta tranquillita'.

## Guida alla configurazione

Ecco un esempio con GL-B3000 per attivare Urban Shield VPN impostandolo come WireGuard Client.

### 1. Registrare Urban Shield VPN

Visita il [sito ufficiale di Urban Shield VPN](https://urbanshieldvpn.com/){class="_blank"} oppure fai clic [qui](https://payment.urbanshieldvpn.com/sign-up) per registrare un account Urban Shield VPN.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Accendere e collegare

Accendi il router. Collega un dispositivo al router tramite cavo Ethernet oppure tramite Wi-Fi.

### 3. Accedere al pannello di amministrazione web

Segui i passaggi sotto per accedere al pannello di amministrazione web. Se hai gia' effettuato l'accesso, passa alla [parte successiva](#4-network-setup).

Apri un browser web, si consigliano Chrome, Edge o Safari, e visita [192.168.8.1](http://192.168.8.1){target="_blank"}. Verrai indirizzato alla configurazione iniziale del pannello di amministrazione web, come mostrato di seguito. Imposta la password amministratore e fai clic su **Next** per continuare.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Configura la rete Wi-Fi. La pagina mostra i dettagli Wi-Fi di fabbrica, inclusi nome rete, SSID, e password, che puoi modificare oppure mantenere. Se modifichi i dettagli Wi-Fi, ricollega il dispositivo alla rete Wi-Fi aggiornata.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Poi fai clic su **Next** per accedere con la password amministratore.

### 4. Configurazione della rete {#4-network-setup}

Nell'angolo superiore destro e' presente un **Network Setup Wizard**, disponibile dal firmware v4.7 in poi. Segui la procedura guidata per configurare il router per l'accesso a Internet prima di configurare la VPN.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Attivare Urban Shield VPN

Seleziona **VPN** dal menu a sinistra -> **WireGuard Client**. Vedrai una pagina di accesso Urban Shield VPN integrata.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Inserisci **Email** e **Password**, quindi fai clic su **Save And Continue**. Verranno generati i file di configurazione per ciascun server.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Seleziona il server desiderato e fai clic su **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

I server disponibili appariranno quindi nell'elenco.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Fai clic sull'icona con i tre puntini per avviare la connessione.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Una volta connesso, apparira' un punto blu a indicare che la connessione e' stata stabilita correttamente.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Puoi anche controllare lo stato della connessione nel VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Modificare le informazioni dell'account o uscire

Fai clic sull'icona a forma di ingranaggio per modificare le informazioni dell'account oppure uscire.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Andare al rinnovo

Se fai clic su **Go Renew**, verrai reindirizzato al sito ufficiale per rinnovare l'abbonamento.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Eliminare

Puoi eliminare tutti i file di configurazione con un solo clic, insieme alla chiave privata e alla chiave pubblica.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
