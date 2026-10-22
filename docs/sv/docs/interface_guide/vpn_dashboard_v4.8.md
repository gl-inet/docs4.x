# VPN Dashboard (Firmware v4.8) {#vpn-dashboard-firmware-v48}

Innehållet bygger på firmware v4.8.x. Använd väljaren för en annan version.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.8" markdown="1">

- [Firmware v4.7 and earlier](vpn_dashboard_v4.7.md)
- [Firmware v4.9 and above](vpn_dashboard.md)

</div>

Öppna **VPN** -> **VPN Dashboard**.

VPN Dashboard visar tunnelregler, serveradress, trafikstatistik, klientens virtuella IP och logg samt Kill Switch, IP Masquerading och MTU.

Du kan aktivera flera VPN-anslutningar för flera tunnlar.

## Setup Wizard {#setup-wizard}

Klicka på bokikonen uppe till vänster och följ VPN Setup Wizard.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Obs!** VPN Setup Wizard gäller endast AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA och Surfshark. För andra tjänster använder du [OpenVPN Client](openvpn_client.md){target="_blank"} eller [WireGuard Client](wireguard_client.md){target="_blank"}.

Here's an example with **Hide.me**. Log in with Hide.me credentials.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Välj en VPN-server och klicka på **Apply**. Den offentliga IP-adressen ser då ut att komma från serverns plats.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

Anslutningen sker automatiskt. Efter anslutning visas en aktiverad VPN Tunnel på VPN Dashboard.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Sidan visar VPN-protokoll, konfigurationsfil, serveradress, lyssningsport, trafikstatistik och klientens virtuella IP. Loggen finns nere till höger.

Alla anslutna klienter använder tunneln för internet.

Konfigurera VPN-principer under [Policy Mode](#policy-mode).

## VPN Mode {#vpn-mode}

Klicka på knappen uppe till höger på VPN Dashboard för att byta läge.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Two modes are available: **Global Mode** and **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode {#global-mode}

All trafik dirigeras genom VPN-tunneln och endast en klientinstans kan aktiveras.

It is ideal for scenarios where all client traffic is routed through a single VPN server, such as unified network security or region‑specific content access.

I exemplet ansluter routern till en australisk server med WireGuard och all klienttrafik går genom tunneln.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

#### Tunnel Options {#tunnel-options}

Du kan konfigurera Kill Switch, IP Masquerading och MTU för tunneln.

Klicka på kugghjulet uppe till höger.

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options1.png){class="glboxshadow"}

![global mode options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options2.png){class="glboxshadow"}

- **Kill Switch**: Blockerar tunneltrafik när VPN misslyckas. Om inaktiverad växlar trafiken till lokalt WAN.

- **Services from GL.iNet Use VPN**: GoodCloud, DDNS och rtty skickar paket genom VPN-tunnlar när alternativet är aktiverat. Det är inaktiverat som standard eftersom tjänsterna normalt kräver enhetens verkliga IP-adress.

- **Allow Remote Access the LAN Subnet**: Tillåter fjärråtkomst till routern och LAN-enheter. Servern måste annonsera en väg till LAN-subnätet.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver reseroutern om Laptop-käll-IP `192.168.10.200` till tunneladressen `10.1.0.2` vid trafik till NAS `192.168.8.100`.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Tunnelns MTU åsidosätter konfigurationsfilens värde.

### Policy Mode {#policy-mode}

I detta läge kan routern ansluta till flera VPN-servrar med egna regler för klienter och destinationer.

It is suitable for use cases requiring flexible traffic management, such as routing different traffic to different destinations through multiple VPN servers.

Ändra VPN Mode till Policy Mode och klicka på **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Efter bytet visas Primary Tunnel, Add Tunnel och All Other Traffic om VPN inte är aktiverat.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Klicka på respektive avsnitt för mer information.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel {#primary-tunnel}

Primary Tunnel är en <u>förinställd</u> tunnel med högst prioritet. [Tunnelprioriteten](#tunnel-priority) kan ändras när flera tunnlar finns.

Tunnelregeln anpassas med tre faktorer:

1. **From**: Trafikkällan som ska dirigeras via tunneln.

    Klicka på den grå rutan och välj trafikkälla.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: Trafik från alla enheter matchar regeln.

        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: Trafik från angivna anslutningstyper, till exempel LAN-subnät, Drop-in Gateway och Guest Network, matchar regeln.

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Om OpenVPN Server eller WireGuard Server är aktiverad visas fler alternativ under Specified Connection Types, användbara för [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: Trafik från angivna enheter, identifierade med MAC-adress, matchar regeln.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: Trafik från angivna MAC-adresser matchar **INTE** regeln.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: It refers to the traffic destinations.

    Klicka på den grå rutan och välj destinationer.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: Matchande trafik dirigeras till alla mål.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Matchande trafik dirigeras till manuellt angivna domäner eller IP-adresser.

        En <u>rotdomän</u> omfattar alla underdomäner. `ubuntu.com` omfattar exempelvis `archive.ubuntu.com`, `security.ubuntu.com` och `old-releases.ubuntu.com`.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Du kan även ändra **Input Mode** från Manual till Subscription URL och ange URL Link.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specifying a root domain will cover all its subdomains.

            - Med Subscribe URL uppdateras domännamn eller IP automatiskt varje dag.

            - Ange rätt URL. Kontrollen verifierar domännamnet eller IP-adressen. [Läs mer](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: Matchande trafik dirigeras **INTE** till manuellt angivna domäner eller IP-adresser.

        En <u>rotdomän</u> omfattar alla underdomäner. `ubuntu.com` omfattar exempelvis `archive.ubuntu.com`, `security.ubuntu.com` och `old-releases.ubuntu.com`.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Du kan även ändra **Input Mode** från Manual till Subscription URL och ange URL Link.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Specifying a root domain will cover all its subdomains.

            - Med Subscribe URL uppdateras domännamn eller IP automatiskt varje dag.

            - Ange rätt URL. Kontrollen verifierar domännamnet eller IP-adressen. [Läs mer](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: It refers to the traffic routing method, i.e., whether to use VPN.

    Klicka på den grå rutan och välj routningsmetod.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: Matchande trafik dirigeras till valda destinationer via VPN.

        Konfigurera först routern som VPN-klient med [VPN Setup Wizard](#setup-wizard) eller OpenVPN Client/WireGuard Client.

        Välj sedan en VPN-konfigurationsfil för tunneln och klicka på **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: Matchande trafik dirigeras via lokalt WAN i stället för VPN.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. När källa, destination och metod har valts är regeln klar.

I exemplet använder alla klienter VPN för angivna domäner via den australiska servern.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Note**: For security, please go to [All Other Traffic](#all-other-traffic) and [Tunnel Options](#tunnel-options_1) to check other settings before enabling the tunnels.

#### Add Tunnel {#add-tunnel}

Klicka på **Add Tunnel** under Primary Tunnel för fler VPN-instanser.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Name the tunnel.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

En ytterligare tunnel visas på VPN Dashboard.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Upp till 5 tunnlar kan skapas, inklusive Primary Tunnel.

Anpassa regler med källa, destination och metod. Se [Primary Tunnel](#primary-tunnel).

**Note**: For security, please go to [All Other Traffic](#all-other-traffic) and [Tunnel Options](#tunnel-options_1) to check other settings before enabling the tunnels.

#### All Other Traffic {#all-other-traffic}

I Policy Mode visas en <u>föraktiverad</u> tunnel längst ned.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Tunneln styr internetåtkomst för trafik som inte matchar någon tunnelgrupp och är aktiverad som standard.

- När den är aktiverad får icke-matchande trafik internetåtkomst.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- När den är inaktiverad tillåts endast VPN-trafik. Övrig och failover-trafik blockeras. Alternativet åsidosätter inte tunnelns Kill Switch.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority {#tunnel-priority}

Primary Tunnel har högst prioritet, följd av manuella tunnlar och sedan All Other Traffic via lokalt WAN.

Klicka på **Modify Priority** eller tunnelns **prioritetsetikett** för att ändra prioritet.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Håll ikonen med tre linjer och dra tunnlarna till önskad ordning. Klicka på **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**When multiple tunnels are enabled, the router will route traffic in the following order**:

1. Trafik provas mot regeln med högst prioritet och därefter nästa tills All Other Traffic matchas.

2. Vid frånkoppling avgör tunnelns **Kill Switch** om trafiken växlar till nästa tunnel.

    - Med Kill Switch aktiverad blockeras trafiken utan failover.
    - Med Kill Switch inaktiverad växlar trafiken till nästa tunnel och dess regler.

3. **All Other Traffic** är aktiverad som standard för internetåtkomst för icke-matchande trafik.

    - När aktiverad dirigeras icke-matchande och failover-trafik via lokalt WAN.
    - När inaktiverad blockeras vanlig internetåtkomst för att förhindra IP-läckor.

#### Tunnel Options {#tunnel-options_1}

Du kan konfigurera avancerade inställningar för varje VPN-tunnel, till exempel VPN Kill Switch, IP Masquerading och MTU.

Klicka på kugghjulet bredvid tunnelns namn och välj **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: Blockerar tunneltrafik vid VPN-fel. Om inaktiverad växlar trafiken till nästa tunnel eller lokalt WAN.

- **Services from GL.iNet Use VPN**: GoodCloud, DDNS och rtty skickar paket genom VPN-tunnlar när alternativet är aktiverat. Det är inaktiverat som standard eftersom tjänsterna normalt kräver enhetens verkliga IP-adress.

- **Allow Remote Access the LAN Subnet**: Tillåter fjärråtkomst till routern och LAN-enheter. Servern måste annonsera en väg till LAN-subnätet.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

    Med IP-maskering skriver reseroutern om Laptop-käll-IP `192.168.10.200` till tunneladressen `10.1.0.2` vid trafik till NAS `192.168.8.100`.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Tunnelns MTU åsidosätter konfigurationsfilens värde.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
