# Come accedere ai dispositivi LAN di WireGuard Server dal client tramite nomi di dominio?

Questo tutorial spiega come accedere ai dispositivi di casa, come NAS, telecamere IP e cosi' via, presenti nella LAN del server WireGuard dal client usando nomi di dominio.

## Topologia

Come mostrato di seguito, puoi accedere ai dispositivi come NAS e telecamera IP presenti nella LAN del server WireGuard da un PC nella LAN del client usando i rispettivi nomi di dominio.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Passaggi di configurazione

### 1. Modifica degli host sul server, opzionale

Questo passaggio si applica quando il server VPN non riesce a risolvere correttamente i nomi di dominio locali. Se non sei sicuro, salta questo passaggio.

Accedi al pannello di amministrazione web del router server VPN e vai su **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Inserisci l'IP e il nome di dominio dei dispositivi di casa a cui vuoi accedere, quindi fai clic su **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Abilitare l'accesso remoto LAN sul server

??? "Per router server con firmware v4.8"

    Nel pannello di amministrazione web del server, vai su **VPN** -> **WireGuard Server**. Fai clic su **Options** nell'angolo in alto a destra.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Abilita **Allow Remote Access the LAN Subnet**, quindi fai clic su **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Quando e' abilitato, questo router e i dispositivi LAN possono essere raggiunti da remoto tramite VPN.**

??? "Per router server con firmware v4.7 e precedenti"

    Nel pannello di amministrazione web del server, vai su **VPN** -> **VPN Dashboard** -> sezione **VPN Server**. Fai clic sull'icona a ingranaggio sul lato destro del server WireGuard.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Abilita **Remote Access LAN**, quindi fai clic su **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Quando e' abilitato, questo router e i dispositivi LAN possono essere raggiunti da remoto tramite VPN.**

### 3. Esportare la configurazione VPN

Nel pannello di amministrazione del server, vai su **VPN** -> **WireGuard Server** -> scheda **Profiles**, poi fai clic su **Add** per esportare un profilo di configurazione.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Otterrai quindi un file **.conf**, come mostrato di seguito.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Apri questo file. Assicurati che il campo DNS punti all'IP del tunnel del server, mostrato nella scheda **Configuration** della pagina WireGuard Server, come illustrato di seguito. Inoltre, elimina `"64.6.64.6"` dal campo DNS, se presente, per evitare errori di risoluzione DNS.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Nota**: l'IP del tunnel del server WireGuard varia a seconda della versione firmware. Controlla l'IP del tunnel del tuo server.

### 4. Abilitare il server VPN

Nella pagina **WireGuard Server**, fai clic sul pulsante **Start** in alto a destra per avviare il server.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Caricare la configurazione VPN

Accedi al pannello di amministrazione web del router client VPN, vai su **VPN** -> **WireGuard Client**, poi fai clic su **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Crea un nome per questo gruppo e carica il file di configurazione.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Caricamento riuscito. Fai clic su **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Qui vedrai il file di configurazione elencato.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Avviare la connessione VPN client

Fai clic sull'icona con tre puntini per avviare la connessione VPN.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Quando il punto grigio diventa verde, il client WireGuard si e' connesso correttamente al server.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Ora puoi accedere ai dispositivi di casa, ad esempio il NAS, presenti nella LAN del server dal PC nella LAN del client usando i rispettivi nomi di dominio.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
