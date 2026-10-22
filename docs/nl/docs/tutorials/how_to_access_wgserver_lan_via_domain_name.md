# Via domeinnamen toegang krijgen tot LAN-apparaten van de WireGuard-server vanaf de client {#how-to-access-wireguard-server-lan-devices-from-the-client-via-domain-names}

In deze handleiding lees je hoe je vanaf een client via domeinnamen toegang krijgt tot thuisapparaten, zoals een NAS of IP-camera, op het LAN van de WireGuard-server.

## Topologie {#topology}

Zoals hieronder weergegeven, kun je vanaf een pc op het LAN van de client via hun domeinnaam toegang krijgen tot apparaten zoals een NAS en IP-camera op het LAN van de WireGuard-server.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Configuratiestappen {#setup-steps}

### 1. Hosts op de server bewerken (optioneel) {#1-edit-hosts-on-server-optional}

Deze stap is van toepassing als je VPN-server lokale domeinnamen niet goed kan omzetten. Sla deze stap over als je het niet zeker weet.

Meld je aan bij het webbeheerpaneel van je VPN-serverrouter en ga naar **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Voer het IP-adres en de domeinnaam in van de thuisapparaten waartoe je toegang wilt en klik op **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Remote Access LAN op de server toestaan {#2-allow-remote-access-lan-on-server}

??? "Voor een serverrouter met firmware v4.8"

    Ga in het webbeheerpaneel van de server naar **VPN** -> **WireGuard Server**. Klik rechtsboven op **Options**.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Schakel **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Als deze optie is ingeschakeld, zijn deze router en LAN-apparaten op afstand toegankelijk via de VPN.**

??? "Voor een serverrouter met firmware v4.7 en ouder"

    Ga in het webbeheerpaneel van de server naar **VPN** -> **VPN Dashboard** -> het gedeelte **VPN Server**. Klik rechts van de WireGuard-server op het tandwielpictogram.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Schakel **Remote Access LAN** in en klik op **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Als deze optie is ingeschakeld, zijn deze router en LAN-apparaten op afstand toegankelijk via de VPN.**

### 3. De VPN-configuratie exporteren {#3-export-vpn-configuration}

Ga in het webbeheerpaneel van de server naar **VPN** -> **WireGuard Server** -> het tabblad **Profiles** en klik op **Add** om een configuratieprofiel te exporteren.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Je ontvangt vervolgens een **.conf**-bestand, zoals hieronder.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Open dit bestand. Controleer of het DNS-veld in het bestand verwijst naar het tunnel-IP-adres van de server. Dit adres staat op het tabblad **Configuration** van de pagina WireGuard Server, zoals hieronder. Verwijder ook eventueel aanwezige waarde "64.6.64.6" uit het DNS-veld om fouten bij de DNS-resolutie te voorkomen.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Opmerking**: het tunnel-IP-adres van de WireGuard-server verschilt per firmwareversie. Controleer het tunnel-IP-adres van je server.

### 4. De VPN-server inschakelen {#4-enable-vpn-server}

Klik op de pagina **WireGuard Server** rechtsboven op **Start** om de server te starten.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. De VPN-configuratie uploaden {#5-upload-vpn-configuration}

Meld je aan bij het webbeheerpaneel van je VPN-clientrouter, ga naar **VPN** -> **WireGuard Client** en klik op **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Geef deze groep een naam en upload het configuratiebestand.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Het uploaden is voltooid. Klik op **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Het configuratiebestand wordt hier weergegeven.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. De VPN-clientverbinding starten {#6-start-vpn-client-connection}

Klik op het pictogram met drie stippen om de VPN-verbinding te starten.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Wanneer de grijze stip groen wordt, heeft de WireGuard-client verbinding gemaakt met de server.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Je kunt nu vanaf de pc op het LAN van de client via hun domeinnaam toegang krijgen tot je thuisapparaten, zoals een NAS, op het LAN van de server.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
