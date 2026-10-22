# DNS-query's van de VPN-client routeren naar de upstream DNS-server van de VPN-server {#how-to-route-vpn-client-dns-queries-to-the-vpn-servers-upstream-dns}

In deze handleiding lees je hoe je alle DNS-query's van VPN-clients omleidt naar je zelfgehoste DNS-server aan de LAN-zijde van je primaire router, upstream van de VPN-server.

## Topologie {#topology}

In deze handleiding gebruiken we **Flint 3 (GL-BE9300)** en **Slate 7 (GL-BE3600)** als voorbeelden.

Flint 3 is de VPN-server, met een primaire router in het upstream netwerk. Slate 7 is de VPN-client die verbinding maakt met Flint 3.

Wanneer een VPN-tunnel tot stand is gebracht tussen de VPN-server en -client, worden DNS-query's van de VPN-client standaard eerst naar de VPN-server gestuurd, vervolgens doorgestuurd naar de primaire router en ten slotte omgezet door de door de ISP toegewezen DNS-servers die op de WAN-interface van de primaire router zijn ingesteld.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Als je echter een zelfgehoste DNS-server (IP-adres `192.168.1.13`) op de primaire router hebt geïmplementeerd, zijn aanvullende instellingen nodig om DNS-query's naar deze server te routeren.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Configuratie {#setup}

1. Meld je aan bij het webbeheerpaneel van Flint 3 en ga naar **NETWORK** -> **DNS**. Stel DNS Server Mode in op **Manual DNS** en voer het IP-adres van je DNS-server in.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Ga naar **VPN** -> **WireGuard Server** -> het tabblad **Configuration**. Noteer het IPv4 Address. Dit is doorgaans `10.0.0.1/24` of `10.1.0.1/24`, afhankelijk van het model en de firmwareversie.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Ga naar het tabblad **Profiles**, voeg een clientconfiguratie toe en exporteer een profiel voor Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Open het profiel en controleer of DNS is ingesteld op het IP-adres van de VPN-server dat je in stap 2 hebt gevonden.

    Verwijder eventueel aanwezige waarde "64.6.64.6" om fouten bij de DNS-resolutie te voorkomen en sla de wijzigingen op.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Klik in het webbeheerpaneel van Flint 3 bovenaan de pagina **WireGuard Server** op **Start** om de server te starten.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Meld je aan bij het webbeheerpaneel van Slate 7 en ga naar **VPN** -> **WireGuard Client**.

    Klik op **Add Manually** en upload het bewerkte profiel.

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Klik op het pictogram met drie stippen om de VPN-verbinding te starten. Als de statusindicator groen wordt, is de VPN-verbinding tot stand gebracht.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## DNS-resolutie controleren {#verify-dns-resolution}

Voer de volgende opdracht uit om DNS-verkeer op de VPN-client vast te leggen. Hieruit blijkt dat al het DNS-verkeer van de VPN-client naar de VPN-server gaat (in dit voorbeeld `10.0.0.1`).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Voer de volgende opdracht uit om DNS-verkeer op de VPN-server vast te leggen. Hieruit blijkt dat al het DNS-verkeer van de VPN-client uiteindelijk naar de zelfgehoste DNS-server gaat (in dit voorbeeld `192.168.1.13`).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
