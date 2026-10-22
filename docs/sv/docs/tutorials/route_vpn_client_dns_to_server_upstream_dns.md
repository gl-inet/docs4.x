# Så dirigerar du VPN-klientens DNS-frågor till VPN-serverns uppströms DNS-server {#how-to-route-vpn-client-dns-queries-to-the-vpn-servers-upstream-dns}

Den här guiden beskriver hur du omdirigerar alla DNS-frågor från VPN-klienter till din egen DNS-server på LAN-sidan av den primära routern, uppströms från VPN-servern.

## Topologi {#topology}

I den här guiden använder vi **Flint 3 (GL-BE9300)** och **Slate 7 (GL-BE3600)** som exempel.

Flint 3 är VPN-servern och har en primär router i sitt uppströmsnätverk. Slate 7 är VPN-klienten som ansluter till Flint 3.

När en VPN-tunnel har upprättats mellan VPN-servern och klienten skickas VPN-klientens DNS-frågor som standard först till VPN-servern, sedan vidare till den primära routern och löses slutligen av de DNS-servrar som internetleverantören har tilldelat och som är konfigurerade på den primära routerns WAN.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Om du däremot har driftsatt en egen DNS-server (IP-adress `192.168.1.13`) på den primära routern krävs ytterligare inställningar för att dirigera DNS-frågorna till denna DNS-server.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Konfiguration {#setup}

1. Logga in på webb­administrationspanelen för Flint 3 och gå till **NETWORK** -> **DNS**. Ändra DNS-serverläget till **Manual DNS** och ange DNS-serverns IP-adress.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Gå till **VPN** -> **WireGuard Server** -> fliken **Configuration** och anteckna IPv4-adressen. Den är vanligtvis `10.0.0.1/24` eller `10.1.0.1/24`, beroende på modell och firmwareversion.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Växla till fliken **Profiles**, lägg till en klientkonfiguration och exportera en profil för Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Öppna profilen och kontrollera att DNS-adressen är VPN-serverns IP-adress som du hämtade i steg 2.

    Undvik DNS-upplösningsfel genom att ta bort "64.6.64.6" om adressen finns och spara ändringarna.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Klicka på knappen **Start** högst upp på sidan **WireGuard Server** i webb­administrationspanelen för Flint 3 för att starta servern.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Logga in på webb­administrationspanelen för Slate 7 och gå till **VPN** -> **WireGuard Client**.

    Klicka på **Add Manually** och ladda upp den redigerade profilen.

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Klicka på ikonen med tre punkter för att starta VPN-anslutningen. När statusindikatorn blir grön har VPN-anslutningen upprättats.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Verifiera DNS-upplösningen {#verify-dns-resolution}

Kör följande kommando för att registrera DNS-trafik på VPN-klienten. Resultatet visar att all DNS-trafik från VPN-klienten går till VPN-servern (i det här exemplet `10.0.0.1`).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Kör följande kommando för att registrera DNS-trafik på VPN-servern. Resultatet visar att all DNS-trafik från VPN-klienten slutligen går till den egna DNS-servern (i det här exemplet `192.168.1.13`).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
