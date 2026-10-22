# Toegang tot WAN toestaan wanneer de VPN-client is ingeschakeld {#how-to-allow-access-to-wan-when-vpn-client-is-enabled}

Wanneer de VPN-client op GL.iNet-routers is ingeschakeld, hebben LAN-apparaten in de standaard globale modus geen toegang tot lokale WAN-apparaten of -services. Al het verkeer vanaf het LAN wordt namelijk via de VPN-tunnel geleid in plaats van via het upstream netwerk (WAN), om DNS-lekken te voorkomen.

In deze handleiding lees je hoe je lokale WAN-services, zoals een printer of NAS, toegankelijk maakt voor de LAN-apparaten van de VPN-client.

![allow access wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Voor firmware v4.7 en ouder {#for-firmware-v47-and-earlier}

Meld je aan bij het webbeheerpaneel van je VPN-client en ga naar **VPN** -> **VPN Dashboard** -> **VPN Client**. Klik rechtsboven op **Global Options**.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Schakel **Allow Access WAN** in en klik op **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Als deze optie is ingeschakeld, kunnen clientapparaten terwijl de VPN verbonden is nog steeds WAN-services in het bovenliggende subnet bereiken, zoals je printer of NAS.

## Voor firmware v4.8 en nieuwer {#for-firmware-v48-and-higher}

De optie **Allow Access WAN** is in firmware v4.8 uit het VPN Dashboard verwijderd. Je kunt echter met VPN-beleid toegang tot het lokale WAN instellen.

Volg de onderstaande stappen.

1. Meld je aan bij het webbeheerpaneel van je VPN-client en ga naar **VPN** -> **VPN Dashboard**.

    Klik rechtsboven op de modus.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Schakel over naar **Policy Mode** en klik op **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    De pagina wordt vernieuwd en ziet er als volgt uit.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Klik op het middelste vak om het doel van de tunnel in te stellen.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Selecteer **Exclude specified Domain / IP List**, voer het WAN-subnet van je router in en klik op **Apply**.

    Hierdoor wordt al het verkeer naar het WAN-subnet via het lokale WAN geleid in plaats van via de VPN-tunnel.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    We gebruiken hier het subnet 192.168.0.1/24 als voorbeeld. Voer dit subnet in en pas de instelling toe. De VPN-tunnel wordt vervolgens weergegeven zoals hieronder.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Hoe vind ik het WAN-subnet van mijn GL.iNet-router?"

        Je vindt het WAN-subnet van een GL.iNet-router doorgaans op de pagina INTERNET. Het wordt bepaald door het upstream apparaat waarop de WAN-interface van de router is aangesloten, zoals een ISP-modem of upstream gateway.

        Stel bijvoorbeeld dat je router als secundaire router werkt, waarbij de WAN-poort is aangesloten op een ander lokaal netwerk, zoals een ISP-modem of de LAN-poort van een hoofdrouter. Als het WAN-IP-adres van de router 192.168.1.165 is, de Gateway 192.168.1.1 is en de Subnet Mask 255.255.255.0 is (een gangbaar masker voor kleine netwerken), dan is het bijbehorende WAN-subnet 192.168.1.0/24. Dit is ook het LAN-subnet van het upstream apparaat.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Opmerking**: de prefixlengte van 192.168.1.0/24 is 24 en komt overeen met het subnetmasker 255.255.255.0. Als de WAN Subnet Mask van je router niet 255.255.255.0 is, is de prefixlengte van je WAN-subnet niet "/24". Bepaal het WAN-subnet op basis van de werkelijke WAN-configuratie.

3. Klik op het rechtervak om de tunnelactie in te stellen, dus wel of geen VPN gebruiken.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Selecteer **Use VPN**, kies een VPN-configuratiebestand en klik op **Apply**.

    Als er geen configuratie beschikbaar is, upload dan eerst een configuratie om je router als VPN-client in te stellen. Ga vervolgens terug naar deze pagina, selecteer Use VPN, kies een VPN-configuratiebestand en klik op Apply.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Schakel de optie rechtsboven in om deze VPN-tunnel te activeren. De verbinding wordt gestart.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Wacht enkele minuten. Na een geslaagde verbinding wordt de indicator groen.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Zoek je openbare IP-adres op om de VPN-verbinding te testen. Open bijvoorbeeld een browser en ga naar [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Je openbare IP-adres en locatie worden weergegeven, zoals hieronder.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Open apparaten of services in het WAN-subnet en controleer of dit lukt.

    Je kunt de ping-opdracht gebruiken om de verbinding te testen.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
