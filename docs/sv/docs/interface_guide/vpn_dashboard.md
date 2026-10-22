# VPN Dashboard {#vpn-dashboard}

Innehållet bygger på firmware v4.9.x och senare. Använd väljaren för en annan version.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.9 and above" markdown="1">

- [Firmware v4.7 and earlier](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

Öppna **VPN** -> **VPN Dashboard**.

VPN Dashboard visar routningsregler, server, trafikstatistik, klientens virtuella IP och logg samt inställningar för Kill Switch, IP Masquerading och MTU.

Compared to firmware v4.8, v4.9 includes the following improvements to the VPN Dashboard:

1. **Allow users to select multiple profiles within a tunnel group and set their priority**. The tunnel will attempt to connect using each profile in priority order until a connection is successfully established.

2. **Varje tunnelgrupp fungerar oberoende utan failover mellan grupper**. Om alla profiler misslyckas avgör Tunnel Kill Switch och All Other Traffic om trafiken växlar till lokalt WAN.

## Upload VPN Profile {#upload-vpn-profile}

Om inga tunnlar finns visas följande sida. Klicka på **Add VPN Tunnel**.

![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Sidan **VPN Client Profile** öppnas. Välj leverantör och logga in.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. Leverantörerna ovan är integrerade i webbadministrationspanelen. Ange inloggningsuppgifter med ett aktivt abonnemang för att hämta konfigurationsfiler.

    2. För andra leverantörer eller egna konfigurationer klickar du på **Add Manually**.

[PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} används som exempel. Klicka på PureVPN och logga in.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

En lista över VPN-profiler visas. Vissa leverantörer kräver att protokoll eller server/stad väljs först.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Klicka på **Go to Dashboard** för att lägga till tunneln och konfigurera principer.

## Add VPN Tunnel {#add-vpn-tunnel}

### General Steps {#general-steps}

Följ stegen nedan för att lägga till en VPN-tunnel och konfigurera principer. Se [Exempel](#case-reference) vid behov.

1. Klicka på **Add VPN Tunnel**. Konfigurationsguiden visas till höger.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Select VPN profile.

    Välj en eller flera profiler, ändra prioriteten och klicka på **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Obs!** Flera profiler provas i prioritetsordning. Om alla misslyckas avgör Kill Switch under [Tunnel Options](#tunnel-options) och [All Other Traffic](#all-other-traffic) om trafiken växlar till lokalt WAN.

3. Välj klientkälla och klicka på **Next**.

    There are four options:

    - **All Clients**: Trafik från alla enheter matchar regeln.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: Trafik från angivna anslutningstyper, till exempel LAN-subnät, Drop-in Gateway och Guest Network, matchar regeln.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: Trafik från angivna enheter, identifierade med MAC-adress, matchar regeln.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: Trafik från angivna enheter matchar inte regeln.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Välj destination och klicka på **Apply**.

    There are three options:

    - **All Targets**: Matchande trafik dirigeras till alla mål.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Matchande trafik dirigeras till manuellt angivna domäner eller IP-adresser.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Matchande trafik dirigeras inte till manuellt angivna domäner eller IP-adresser.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Tunneln har lagts till och **VPN Dashboard** öppnas.

    For security, please go to [All Other Traffic](#all-other-traffic) and [Tunnel Options](#tunnel-options) to check **Kill Switch** status before enabling your VPN tunnel.

### Case Reference {#case-reference}

Nedan visas två vanliga VPN-principer med stegvisa anvisningar.

??? note "Case 1: Route only specified devices over VPN."

    **Requirements:**

    1. Endast vissa anslutna enheter använder VPN för internet. Övriga använder lokalt WAN.

    2. Valda enheter måste endast använda VPN. Om VPN kopplas från blockeras deras internetåtkomst för att förhindra DNS-läckor och IP-spårning.

    **Configuration Steps:**

    1. Select VPN profile.

        Tillgängliga profiler visas om du har loggat in på en integrerad VPN-tjänst eller laddat upp en fil. Annars öppnar du **VPN Client Profile** och loggar in eller laddar upp en fil.

        [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} används som exempel. Välj en eller flera profiler och ändra prioriteten till höger.

        ![case 1 profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Select client source.

        Klicka på **Specified Devices**, välj enheterna som ska använda VPN och klicka på **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Select target destination.

        Klicka på fliken **All Targets**, ange den som trafikdestination och klicka på **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. VPN Dashboard öppnas och tunneln har lagts till enligt nedan.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Kontrollera att **Kill Switch** är aktiverad för tunneln. Vid oväntad frånkoppling blockeras matchande trafik för att förhindra DNS-läckor och IP-spårning.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

    6. Kontrollera att **Allow Non-VPN Traffic** är aktiverat så att icke-matchande trafik kan använda lokalt WAN.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Klicka på mittknappen för att aktivera tunneln.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Efter anslutning visas VPN-princip, trafikstatistik, serveradress, lyssningsport och virtuell IP-adress.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Endast de två angivna enheterna använder VPN. Vid frånkoppling blockeras deras internetåtkomst; övriga använder lokalt WAN.

??? note "Case 2: Route all devices over VPN 1 for specific websites, and route all remaining traffic over VPN 2."

    **Requirements:**

    1. Alla enheter använder **VPN Tunnel 1** för angivna sociala medier och strömningstjänster och **VPN Tunnel 2** för övrig internetåtkomst.

    2. Om tunnlarna kopplas från blockeras internetåtkomst för alla enheter för att förhindra DNS-läckor och IP-spårning.

    **Configuration Steps:**

    1. Select the VPN profile for Tunnel 1.

        Tillgängliga profiler visas om du har loggat in på en integrerad VPN-tjänst eller laddat upp en fil. Annars öppnar du **VPN Client Profile** och loggar in eller laddar upp en fil.

        [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} används som exempel. Välj en eller flera profiler, ändra prioriteten och klicka på **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Select client source.

        Klicka på fliken **All Clients**, ange den som klientkälla för Tunnel 1 och klicka på **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Select target destination.

        Klicka på **Specified Domain / IP List**, ange domänerna enligt nedan och klicka på **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. VPN Dashboard öppnas och VPN Tunnel 1 har lagts till.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Kontrollera att **Kill Switch** för Tunnel 1 är aktiverad. Vid frånkoppling blockeras matchande trafik.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

    6. Click **Add New Tunnel** to add Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Select VPN profile for Tunnel 2.

        [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} används som exempel. Välj en eller flera profiler och ändra prioriteten.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Select client source.

        Klicka på fliken **All Clients**, ange den som klientkälla för Tunnel 2 och klicka på **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Select target destination.

        Klicka på fliken **All Targets**, ange den som trafikdestination för Tunnel 2 och klicka på **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. VPN Dashboard öppnas och VPN Tunnel 2 har lagts till.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Kontrollera att **Kill Switch** för Tunnel 2 är aktiverad. Vid frånkoppling blockeras matchande trafik.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Klicka på kugghjulet uppe till höger och aktivera **Enhanced Kill Switch** så att all trafik måste använda VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Klicka på mittknappen för att aktivera Tunnel 1 och Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Efter anslutning visas VPN-princip, trafikstatistik, serveradress, lyssningsport och virtuell IP-adress.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Alla enheter använder **VPN Tunnel 1** för angivna domäner och **VPN Tunnel 2** för övrig trafik. Vid frånkoppling blockeras internetåtkomsten.

## Kill Switch {#kill-switch}

!!! Tip "What is Kill Switch?"

    VPN Kill Switch förhindrar att trafik återgår till en okrypterad internetanslutning när VPN misslyckas.

    För en enskild tunnel blockerar **Kill Switch** internetåtkomst för tilldelad trafik om anslutningen misslyckas. Övrig trafik följer **All Other Traffic**.

    **Enhanced Kill Switch** blockerar internettrafik som inte matchar någon VPN-tunnel och åsidosätter inte tunnelns **Kill Switch**.

Since firmware v4.8, GL.iNet routers support Kill Switch configuration for the global VPN connection, as well as for each individual VPN tunnel.

- To set up Kill Switch for the global VPN connection (i.e., Enhanced Kill Switch), refer to [All Other Traffic](#all-other-traffic).

- To set up Kill Switch for each individual VPN tunnel, refer to [Tunnel Options](#tunnel-options).

## All Other Traffic {#all-other-traffic}

Klicka på kugghjulet uppe till höger för principen för trafik som inte matchar en VPN-tunnel.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Principen styr internetåtkomst för trafik som inte matchar någon tunnelgrupp. Alternativen är **Allow Non-VPN Traffic** och **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Enabled by default to ensure normal internet access for non-VPN traffic.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Tvingar alla enheter att använda VPN. Trafik som inte matchar en VPN-tunnel blockeras. Inställningen åsidosätter inte Kill Switch för enskilda tunnlar.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Options {#tunnel-options}

Du kan konfigurera avancerade inställningar för varje VPN-tunnel, till exempel VPN Kill Switch, IP Masquerading och MTU.

Klicka på kugghjulet i en tunnelgrupp och välj **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: När alternativet är aktiverat blockeras matchande trafik om VPN misslyckas. När det är inaktiverat växlar trafiken till **All Other Traffic**.

- **Services from GL.iNet Use VPN**: GoodCloud, DDNS och rtty skickar paket genom VPN-tunnlar när alternativet är aktiverat. Det är inaktiverat som standard eftersom tjänsterna normalt kräver enhetens verkliga IP-adress.

- **Allow Remote Access to the LAN Subnet**: Tillåter fjärråtkomst till routern och LAN-enheter via VPN. VPN-servern måste annonsera en returväg till LAN-subnätet.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    När IP-maskering är aktiverad och Laptop (192.168.10.200) skickar trafik till hem-NAS (192.168.8.100) skriver reseroutern om käll-IP från `192.168.10.200` till VPN-klientens tunneladress `10.1.0.2`. Serversidan ser då trafiken som om den kommer från klienten i stället för klientens LAN.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Tunnelns MTU-värde åsidosätter konfigurationsfilens MTU.

## Tunnel Priority {#tunnel-priority}

Ändra tunnelprioritet genom att klicka på kugghjulet i tunnelgruppen och välja **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Håll ikonen med tre linjer till höger och dra tunnlarna till önskad ordning. Klicka på **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router routes traffic according to the following rules**:

1. Trafik matchas först mot tunnelregeln med högst prioritet. Om den inte matchar provas nästa tunnel.

2. Varje tunnelgrupp fungerar oberoende. När trafik matchar en regel dirigeras den genom tunneln utan failover mellan grupper.

3. Flera profiler kan väljas i en tunnelgrupp för intern failover. Om profilen med högst prioritet slutar fungera används nästa profil automatiskt.

4. Om en VPN-tunnel kopplas från avgör tunnelns **Kill Switch** om trafiken växlar till All Other Traffic.

    - Om Kill Switch är aktiverad blockeras trafiken och växlar inte till All Other Traffic.
    - Om Kill Switch är inaktiverad växlar trafiken till All Other Traffic.

5. Lägena i **All Other Traffic** avgör om trafik som inte matchar VPN-tunnlar får internetåtkomst.

    - **Allow Non-VPN Traffic**: Aktiverat som standard så att icke-matchande trafik kan använda lokalt WAN.

    - **Enhanced Kill Switch**: Tvingar alla enheter att använda VPN och blockerar icke-matchande trafik. Inställningen åsidosätter inte tunnelns Kill Switch utan förstärker skyddet och förhindrar IP-läckor.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
