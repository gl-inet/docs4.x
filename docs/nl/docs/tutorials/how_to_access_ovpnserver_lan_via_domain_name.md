# Via domeinnamen toegang krijgen tot LAN-apparaten van de OpenVPN-server vanaf de client {#how-to-access-openvpn-server-lan-devices-from-the-client-via-domain-names}

In deze handleiding lees je hoe je vanaf een client via domeinnamen toegang krijgt tot thuisapparaten, zoals een NAS of IP-camera, op het LAN van de OpenVPN-server.

## Topologie {#topology}

Zoals hieronder weergegeven, kun je vanaf een pc op het LAN van de client via hun domeinnaam toegang krijgen tot apparaten zoals een NAS en IP-camera op het LAN van de OpenVPN-server.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Configuratiestappen {#setup-steps}

### 1. Hosts op de server bewerken (optioneel) {#1-edit-hosts-on-server-optional}

Deze stap is van toepassing als je VPN-server lokale domeinnamen niet goed kan omzetten. Sla deze stap over als je het niet zeker weet.

Meld je aan bij het webbeheerpaneel van je VPN-serverrouter en ga naar **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Voer het IP-adres en de domeinnaam in van de thuisapparaten waartoe je toegang wilt en klik op **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Remote Access LAN op de server toestaan {#2-allow-remote-access-lan-on-server}

Ga in het webbeheerpaneel van de server naar **VPN** -> **OpenVPN Server**. Klik rechtsboven op **Options**.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Schakel **Allow Remote Access the LAN Subnet** in en klik op **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Als deze optie is ingeschakeld, zijn de router en LAN-apparaten op afstand toegankelijk via de VPN.

### 3. De VPN-configuratie exporteren {#3-export-vpn-configuration}

Ga in het webbeheerpaneel van de server naar **VPN** -> **OpenVPN Server** -> het tabblad **Configuration** en klik onderaan op **Export Client Configuration**.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

Klik in het pop-upvenster op **Export**.

**Opmerking**: als het openbare IP-adres van je server dynamisch is en af en toe verandert, ga je voordat je de clientconfiguratie exporteert naar **APPLICATIONS** -> **Dynamic DNS** om **DDNS** in te schakelen.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Je ontvangt vervolgens een **.ovpn**-bestand, zoals hieronder.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Als je serverrouter firmware v4.8 of nieuwer gebruikt, hoef je het configuratiebestand niet te bewerken. Ga verder met de volgende stap.

Als je serverrouter firmware v4.7 of ouder gebruikt, open je dit bestand. Voeg de volgende regel toe om de DNS-server in te stellen op het tunnel-IP-adres van je OpenVPN-server en sla de wijzigingen op.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Tip: je vindt het IPv4-subnet van de OpenVPN-servertunnel op het tabblad **Configuration** van de pagina OpenVPN Server, zoals hieronder. Dit verschilt per firmwareversie. Controleer het tunnel-IP-adres van je OpenVPN-server.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. De VPN-server inschakelen {#4-enable-vpn-server}

Klik op de pagina **OpenVPN Server** rechtsboven op **Start** om de server te starten.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. De VPN-configuratie uploaden {#5-upload-vpn-configuration}

Meld je aan bij het webbeheerpaneel van je VPN-clientrouter, ga naar **VPN** -> **OpenVPN Client** en klik op **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Geef deze groep een naam en upload het configuratiebestand.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Het uploaden is voltooid. Klik op **Apply**.

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Het configuratiebestand wordt hier weergegeven.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. De VPN-clientverbinding starten {#6-start-vpn-client-connection}

Klik op het pictogram met drie stippen om de VPN-verbinding te starten.

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Wanneer de grijze stip groen wordt, heeft de OpenVPN-client verbinding gemaakt met de server.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Je kunt nu vanaf de pc op het LAN van de client via hun domeinnaam toegang krijgen tot je thuisapparaten, zoals een NAS, op het LAN van de server.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
