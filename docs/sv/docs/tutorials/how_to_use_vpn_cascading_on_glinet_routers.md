# Använda VPN Cascading på GL.iNet-routrar {#how-to-use-vpn-cascading-on-glinet-routers}

## Introduktion {#introduction}

VPN Cascading kallas ofta "Double VPN", men funktionen kan skilja sig något på GL.iNet-routrar. Grundprincipen visas nedan.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (routern som VPN-server)**: När routern fungerar som VPN-server kommer klienter som är anslutna till servern som standard åt internet via routerns internetleverantörsnätverk.

**VPN 2 (routern som VPN-klient)**: Routern fungerar även som VPN-klient och ansluter till en VPN-tjänst från tredje part.

**VPN Cascading**: Routern vidarebefordrar trafiken från VPN 1-tunneln till VPN 2-tunneln. Enheter som är anslutna till routern via VPN 1 kommer då åt internet via VPN-tjänsten från tredje part (VPN 2) i stället för routerns internetleverantörsnätverk.

## Aktivera VPN Cascading {#how-to-enable-vpn-cascading}

### För firmware v4.7 och tidigare {#for-firmware-v47-and-earlier}

1. Konfigurera först routern som VPN-server. WireGuard rekommenderas för högre hastighet. Följ [den här länken](../interface_guide/wireguard_server.md){target="_blank"}.
2. Exportera en konfigurationsfil från routern och ladda upp den till en klientenhet som ska ansluta till routern via VPN.
3. Konfigurera routern som VPN-klient och anslut den till en VPN-tjänst från tredje part. WireGuard rekommenderas för högre hastighet. Följ [den här länken](../interface_guide/wireguard_client.md){target="_blank"}.
4. När anslutningen har upprättats visas sidan **VPN Dashboard** enligt nedan. Routern har då konfigurerats som VPN-server och VPN-klient samtidigt.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Gå till avsnittet VPN Server på samma sida och klicka på **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Aktivera **VPN Cascading** och klicka på **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPN Cascading är aktiverat. Enheter som är anslutna till routern via VPN kommer åt internet genom VPN-tjänsten från tredje part i stället för routerns internetleverantörsnätverk.

### För firmware v4.8 och senare {#for-firmware-v48-and-higher}

1. Konfigurera först routern som VPN-server. WireGuard rekommenderas för högre hastighet. Följ [den här länken](../interface_guide/wireguard_server.md){target="_blank"}.
2. Exportera en konfigurationsfil från routern och ladda upp den till en klientenhet som ska ansluta till routern via VPN.
3. Konfigurera routern som VPN-klient och anslut den till en VPN-tjänst från tredje part. WireGuard rekommenderas för högre hastighet. Följ [den här länken](../interface_guide/wireguard_client.md){target="_blank"}.
4. Gå till **VPN Dashboard** i webbadministrationspanelen. Följ instruktionerna för ditt VPN-läge nedan.

    ??? "Global Mode"

        Om VPN-läget är Global Mode aktiveras VPN Cascading automatiskt när VPN-klienten aktiveras enligt nedan.

        Enheter som är anslutna till routern via VPN kommer åt internet genom VPN-tjänsten från tredje part i stället för routerns internetleverantörsnätverk.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        Om VPN-läget är Policy Mode måste du konfigurera VPN-tunnelregeln.

        Klicka på den nedtonade rutan till vänster.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-traffic_from_1.png){class="glboxshadow"}

        Välj trafikkällan som regeln ska gälla för. Aktivera VPN Cascading genom att välja **All Clients** eller **Specified Connection Types** och sedan **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: Omfattar alla LAN-enheter, enheter från Drop-in Gateway, enheter i gästnätverket och enheter som är anslutna till routern via VPN.

            Om trafiken från alla enheter ska följa samma tunnelregel väljer du **All Clients** och klickar på **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: Låter dig ange att enheter som ansluter till routern med en viss metod, till exempel via VPN, ska följa tunnelregeln.

            Om routerns VPN-klienter ska följa en annan regel än övriga enheter väljer du **WireGuard/OpenVPN Server** och klickar på **Apply**.

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            Detta är ett exempel på VPN-tunnelregler i Policy Mode.

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. VPN Cascading är aktiverat. Enheter som är anslutna till routern via VPN kommer åt internet genom VPN-tjänsten från tredje part i stället för routerns internetleverantörsnätverk.

6. **Anslutningstest**: Öppna en webbläsare på en bärbar dator som är ansluten till routern via VPN och besök [What Is My IP](https://whatismyipaddress.com/){target="_blank"} för att kontrollera den offentliga IP-adressen.

    Om den bärbara datorns IP-adress visas i regionen för VPN-servern från tredje part (Buenos Aires i den här guiden) fungerar VPN Cascading.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
