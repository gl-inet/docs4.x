# VPN Cascading gebruiken op GL.iNet-routers {#how-to-use-vpn-cascading-on-glinet-routers}

## Inleiding {#introduction}

VPN Cascading wordt soms "Double VPN" genoemd, maar de werking op GL.iNet-routers kan enigszins verschillen. Het basisconcept wordt hieronder weergegeven.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (router als VPN-server)**: wanneer de router als VPN-server werkt, maken clients die met deze server zijn verbonden standaard via het ISP-netwerk van de router verbinding met internet.

**VPN 2 (router als VPN-client)**: de router werkt ook als VPN-client en maakt verbinding met een VPN-service van derden.

**VPN Cascading**: de router stuurt verkeer vanuit de VPN 1-tunnel door naar de VPN 2-tunnel. Hierdoor krijgen apparaten die via VPN 1 met de router zijn verbonden via de VPN-service van derden (VPN 2) toegang tot internet, in plaats van via het ISP-netwerk van de router.

## VPN Cascading inschakelen {#how-to-enable-vpn-cascading}

### Voor firmware v4.7 en ouder {#for-firmware-v47-and-earlier}

1. Stel je router eerst in als VPN-server. Voor hogere snelheden wordt het WireGuard-protocol aanbevolen. Raadpleeg [deze handleiding](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exporteer een configuratiebestand uit je router en upload het naar een clientapparaat dat via VPN verbinding met de router maakt.

3. Stel je router in als VPN-client die verbinding maakt met een VPN-service van derden. Voor hogere snelheden wordt het WireGuard-protocol aanbevolen. Raadpleeg [deze handleiding](../interface_guide/wireguard_client.md){target="_blank"}.

4. Nadat verbinding is gemaakt, ziet de pagina **VPN Dashboard** eruit zoals hieronder. De router is nu tegelijkertijd als VPN-server en VPN-client ingesteld.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Ga op dezelfde pagina naar het gedeelte VPN Server en klik op **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Schakel **VPN Cascading** in en klik op **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPN Cascading is ingeschakeld. Apparaten die via VPN met je router zijn verbonden, krijgen via de VPN-service van derden toegang tot internet in plaats van via het ISP-netwerk van de router.

### Voor firmware v4.8 en nieuwer {#for-firmware-v48-and-higher}

1. Stel je router eerst in als VPN-server. Voor hogere snelheden wordt het WireGuard-protocol aanbevolen. Raadpleeg [deze handleiding](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exporteer een configuratiebestand uit je router en upload het naar een clientapparaat dat via VPN verbinding met de router maakt.

3. Stel je router in als VPN-client die verbinding maakt met een VPN-service van derden. Voor hogere snelheden wordt het WireGuard-protocol aanbevolen. Raadpleeg [deze handleiding](../interface_guide/wireguard_client.md){target="_blank"}.

4. Ga in het webbeheerpaneel naar **VPN Dashboard**. Volg hieronder de instructies voor je VPN-modus.

    ??? "Global Mode"

        Als je VPN-modus Global Mode is, wordt VPN Cascading automatisch ingeschakeld zodra de VPN-client wordt ingeschakeld, zoals hieronder.

        Apparaten die via VPN met je router zijn verbonden, krijgen via de VPN-service van derden toegang tot internet in plaats van via het ISP-netwerk van de router.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        Als je VPN-modus Policy Mode is, moet je de VPN-tunnelregel instellen.

        Klik op het grijze vak links.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-traffic_from_1.png){class="glboxshadow"}

        Selecteer de verkeersbron waarop deze regel moet worden toegepast. Selecteer **All Clients** om VPN Cascading in te schakelen, of selecteer **Specified Connection Types** en vervolgens **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: omvat alle LAN-apparaten, apparaten van Drop-in Gateway, apparaten van het gastnetwerk en apparaten die via VPN met je router zijn verbonden.

            Als je op het verkeer van alle apparaten dezelfde tunnelregel wilt toepassen, selecteer je **All Clients** en klik je op **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: hiermee kun je apparaten selecteren die via een specifieke methode met de router zijn verbonden, bijvoorbeeld via VPN, en de tunnelregel op deze apparaten toepassen.

            Als je op de VPN-clients van je router een andere regel wilt toepassen dan op andere apparaten, selecteer je **WireGuard/OpenVPN Server** en klik je op **Apply**.

            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            Dit is een voorbeeld van VPN-tunnelregels in Policy Mode.

            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. VPN Cascading is ingeschakeld. Apparaten die via VPN met je router zijn verbonden, krijgen via de VPN-service van derden toegang tot internet in plaats van via het ISP-netwerk van de router.

6. **Verbindingstest**: open een browser op een laptop die via VPN met de router is verbonden en ga naar [What Is My IP](https://whatismyipaddress.com/){target="_blank"} om het openbare IP-adres te controleren.

    Als wordt aangegeven dat het IP-adres van de laptop zich in de regio van de VPN-server van derden bevindt, in deze handleiding Buenos Aires, is VPN Cascading actief.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
