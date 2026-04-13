# Come accedere ai dispositivi LAN di OpenVPN Server dal client tramite nomi di dominio?

Questo tutorial spiega come accedere ai dispositivi di casa, come NAS, telecamere IP e cosi' via, presenti nella LAN del server OpenVPN dal client usando nomi di dominio.

## Topologia

Come mostrato di seguito, puoi accedere ai dispositivi come NAS e telecamera IP presenti nella LAN del server OpenVPN da un PC nella LAN del client usando i rispettivi nomi di dominio.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Passaggi di configurazione

### 1. Modifica degli host sul server, opzionale

Questo passaggio si applica quando il server VPN non riesce a risolvere correttamente i nomi di dominio locali. Se non sei sicuro, salta questo passaggio.

Accedi al pannello di amministrazione web del router server VPN e vai su **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Inserisci l'IP e il nome di dominio dei dispositivi di casa a cui vuoi accedere, quindi fai clic su **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Abilitare l'accesso remoto LAN sul server

Nel pannello di amministrazione web del server, vai su **VPN** -> **OpenVPN Server**. Fai clic su **Options** nell'angolo in alto a destra.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Abilita **Allow Remote Access the LAN Subnet**, quindi fai clic su **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Quando e' abilitato, il router e i dispositivi LAN possono essere raggiunti da remoto tramite VPN.

### 3. Esportare la configurazione VPN

Nel pannello di amministrazione del server, vai su **VPN** -> **OpenVPN Server** -> scheda **Configuration**, quindi fai clic su **Export Client Configuration** in basso.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

Nella finestra pop-up, fai clic su **Export**.

**Nota**: se l'indirizzo IP pubblico del server e' dinamico e cambia nel tempo, vai prima su **APPLICATIONS** -> **Dynamic DNS** per abilitare **DDNS**, poi esporta la configurazione client.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Otterrai quindi un file **.ovpn**, come mostrato di seguito.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Se il router server usa firmware v4.8 o successivo, non e' necessario modificare il file di configurazione; passa al passaggio successivo.

Se il router server usa firmware v4.7 o precedente, apri questo file, aggiungi la riga seguente per impostare il server DNS sull'IP del tunnel del tuo server OpenVPN, quindi salva le modifiche.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Suggerimento: la subnet IPv4 del tunnel OpenVPN server si trova nella scheda **Configuration** della pagina OpenVPN Server, come mostrato di seguito. Varia a seconda della versione firmware. Controlla l'IP del tunnel del tuo server OpenVPN.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Abilitare il server VPN

Nella pagina **OpenVPN Server**, fai clic sul pulsante **Start** in alto a destra per avviare il server.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Caricare la configurazione VPN

Accedi al pannello di amministrazione web del router client VPN, vai su **VPN** -> **OpenVPN Client**, poi fai clic su **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Crea un nome per questo gruppo e carica il file di configurazione.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Caricamento riuscito. Fai clic su **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Qui vedrai il file di configurazione elencato.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Avviare la connessione VPN client

Fai clic sull'icona con tre puntini per avviare la connessione VPN.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Quando il punto grigio diventa verde, il client OpenVPN si e' connesso correttamente al server.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Ora puoi accedere ai dispositivi di casa, ad esempio il NAS, presenti nella LAN del server dal PC nella LAN del client usando i rispettivi nomi di dominio.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
