# ExpressVPN Activation Guide {#expressvpn-activation-guide}

**Note:** This guide only applies to GL.iNet x ExpressVPN co-branded router **Fortify (GL-MT6000)**.

---

[ExpressVPN](https://www.expressvpn.com/){target="_blank"} är en ledande premium-VPN-tjänst som skyddar integriteten, säkrar internetanslutningen och möjliggör säker strömning. Den erbjuder hög hastighet, kraftfull kryptering och servrar i över 100 länder för säker surfning och skydd på offentligt Wi-Fi.

**Fortify (GL-MT6000)** är en gemensamt varumärkesprofilerad router från GL.iNet och ExpressVPN. Varje enhet innehåller en kostnadsfri ettårsprenumeration på ExpressVPN. Prenumerationen löses in och kontot ansluts direkt i webbadministrationspanelen. När en ExpressVPN-tunnel är ansluten krypterar och dirigerar routern trafik enligt VPN-principerna.

Guiden visar hur du löser in ExpressVPN-abonnemanget på 12 månader i webbadministrationspanelen och anpassar VPN-principer efter dina behov för krypterad och snabb internetanslutning.

## Redeem ExpressVPN Plan {#redeem-expressvpn-plan}

Logga in på webbadministrationspanelen för Fortify och öppna **VPN** -> **VPN Client Profile**.

![vpn client profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/vpn_client_profile.png){class="glboxshadow"}

Läs och godkänn **Terms of Service** och **Privacy Policy** och klicka på **Get Started**.

![get started](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/get_started.png){class="glboxshadow"}

Click **Claim 12-Month Plan**.

![claim 12-month plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/claim_plan.png){class="glboxshadow"}

Ange **Order ID** i popup-fönstret. Om routern köptes från GL.iNet Store krävs även **Order Email**. Klicka sedan på **Continue to ExpressVPN**.

![claim 12-month plan amazon](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/amazon_order.png){class="glboxshadow"}

![claim 12-month plan store](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/store_order_email.png){class="glboxshadow"}

ExpressVPN Checkout öppnas. En inlösenkod till höger aktiverar 12 månaders prenumeration utan extra kostnad.

Ange e-postadressen högst upp och lägg till en betalningsmetod för fortsatt VPN-åtkomst efter den första perioden. Klicka på **Subscribe with Card**.

![expressvpn checkout1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout1.png){class="glboxshadow"}

Abonnemanget är aktiverat. Återgå till Fortify-routerns webbadministrationspanel och logga in.

![expressvpn checkout2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_checkout2.png){class="glboxshadow"}

## Log in to ExpressVPN {#log-in-to-expressvpn}

On your Fortify's web Admin Panel, go to **VPN** -> **VPN Client Profile**.

Klicka på **Log in to ExpressVPN** för att öppna ExpressVPNs säkra inloggningssida.

![expressvpn login 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login1.png){class="glboxshadow"}

Ange e-postadressen och klicka på **Send Code**. En sexsiffrig verifieringskod skickas till adressen.

![expressvpn login 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login2.png){class="glboxshadow"}

Ange verifieringskoden och klicka på **Continue**.

![expressvpn login 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login3.png){class="glboxshadow"}

Change your password to activate your account.

![expressvpn login 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login4.png){class="glboxshadow"}

Klicka på **Yes** för att godkänna ExpressVPN-åtkomst på routern.

![expressvpn login 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login5.png){class="glboxshadow"}

Inloggningen lyckades. Stäng webbläsarfönstret och återgå till enheten.

![expressvpn login 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_login6.png){class="glboxshadow"}

On your Fortify's web Admin Panel, go to **VPN** -> **VPN Client Profile**.

Du är inloggad på ExpressVPN på routern. Klicka på **Go to ExpressVPN Dashboard**.

![expressvpn signed in](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_signed_in.png){class="glboxshadow"}

Nu kan du lägga till VPN-tunnlar och konfigurera VPN-principer efter behov.

![expressvpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/expressvpn_dashboard.png){class="glboxshadow"}

## Add VPN Tunnel {#add-vpn-tunnel}

### General Steps {#general-steps}

Följ stegen nedan för att lägga till en VPN-tunnel och konfigurera principer. Se [Exempel](#case-reference) vid behov.

1. On your Fortify's web Admin Panel, go to **VPN** -> **ExpressVPN Dashboard**. Click **Add VPN Tunnel**.

    ![dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/dashboard_initial.png){class="glboxshadow"}

2. Välj VPN-profil och klicka på **Next**.

    En lista över ExpressVPN-profiler visas. Välj en eller flera och ändra prioriteten till höger.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/select-profile.png){class="glboxshadow"}

    !!! note

        När flera profiler väljs försöker tunneln ansluta i prioritetsordning. Om alla profiler misslyckas avgör Kill Switch under [Tunnel Options](#tunnel-options) och [All Other Traffic](#all-other-traffic) om trafiken växlar till routerns lokala WAN.

3. Välj klientkälla och klicka på **Next**.

    There are four options:

    - **All Clients**: Trafik från alla enheter matchar regeln.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-clients.png){class="glboxshadow"}

    - **Specified Connection Types**: Trafik från angivna anslutningstyper, till exempel LAN-subnät, Drop-in Gateway och Guest Network, matchar regeln.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-connection.png){class="glboxshadow"}

    - **Specified Devices**: Trafik från angivna enheter, identifierade med MAC-adress, matchar regeln.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: Trafik från angivna enheter matchar inte regeln.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-devices.png){class="glboxshadow"}

4. Välj destination och klicka på **Apply**.

    There are three options:

    - **All Targets**: Matchande trafik dirigeras till alla mål.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all-targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Matchande trafik dirigeras till manuellt angivna domäner eller IP-adresser.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/specified-domain-ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Matchande trafik dirigeras inte till manuellt angivna domäner eller IP-adresser.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/exclude-specified-domain-ip.png){class="glboxshadow"}

5. VPN-tunneln har lagts till och **ExpressVPN Dashboard** öppnas. Lägg till fler tunnlar vid behov.

### Case Reference {#case-reference}

Nedan visas två vanliga VPN-principer med stegvisa anvisningar.

??? note "Case 1: Route only specified devices over VPN."

    **Requirements:**

    1. Endast vissa anslutna enheter använder VPN för internet. Övriga använder lokalt WAN.

    2. Valda enheter måste endast använda VPN. Om VPN kopplas från blockeras deras internetåtkomst för att förhindra DNS-läckor och IP-spårning.

    **Configuration Steps:**

    1. Select VPN profile.

        Välj en eller flera profiler, ändra prioriteten till höger och klicka på **Next**.

        ![case 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-select-profiles.png){class="glboxshadow"}

    2. Select client source.

        Klicka på fliken **Specified Devices**, välj enheterna som ska använda VPN och klicka på **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-specified-devices.png){class="glboxshadow"}

    3. Select target destination.

        Klicka på fliken **All Targets**, ange den som trafikdestination och klicka på **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-all-targets.png){class="glboxshadow"}

    4. ExpressVPN Dashboard öppnas och VPN-tunneln har lagts till.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-tunnel-apply.png){class="glboxshadow"}

    5. Kontrollera att **Kill Switch** är aktiverad för tunneln. Vid oväntad frånkoppling blockeras matchande trafik för att förhindra DNS-läckor och IP-spårning.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-killswitch2.png){class="glboxshadow"}

    6. Kontrollera att **Allow Non-VPN Traffic** är aktiverat. Det är standard och låter icke-matchande trafik använda lokalt WAN.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-allow-non-vpn.png){class="glboxshadow"}

    7. Klicka på mittknappen för att aktivera tunneln.

        ![case 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-start-vpn.png){class="glboxshadow"}

    8. Efter anslutning visas VPN-princip, klientens virtuella IP-adress, serveradress, lyssningsport och trafikstatistik.

        ![case 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case1-connected.png){class="glboxshadow"}

        Endast de två angivna enheterna använder VPN. Om VPN kopplas från blockeras deras internetåtkomst; övriga enheter använder lokalt WAN.

??? note "Case 2: Route all devices over VPN 1 for specific websites, and route all remaining traffic over VPN 2."

    **Requirements:**

    1. Alla enheter använder VPN Tunnel 1 för angivna sociala medier och strömningstjänster och VPN Tunnel 2 för övrig internetåtkomst.

    2. Om tunnlarna kopplas från blockeras internetåtkomst för alla enheter för att förhindra DNS-läckor och IP-spårning.

    **Configuration Steps:**

    1. Select VPN profile for Tunnel 1.

        Välj en eller flera profiler, ändra prioriteten till höger och klicka på **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles1.png){class="glboxshadow"}

    2. Select client source.

        Klicka på fliken **All Clients**, ange den som klientkälla för Tunnel 1 och klicka på **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    3. Select target destination.

        Klicka på **Specified Domain / IP List**, ange domäner för sociala medier och strömningstjänster och klicka på **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-specified-domain.png){class="glboxshadow"}

    4. ExpressVPN Dashboard öppnas och VPN Tunnel 1 har lagts till.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel1.png){class="glboxshadow"}

    5. Kontrollera att **Kill Switch** för Tunnel 1 är aktiverad. Vid frånkoppling blockeras matchande trafik.

        ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch1.png){class="glboxshadow"}

        ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch2.png){class="glboxshadow"}

    6. Click **Add New Tunnel** to add Tunnel 2.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-add-tunnel2.png){class="glboxshadow"}

    7. Select VPN profile for Tunnel 2.

        Välj en eller flera profiler, ändra prioriteten till höger och klicka på **Next**.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-select-profiles2.png){class="glboxshadow"}

    8. Select client source.

        Klicka på fliken **All Clients**, ange den som klientkälla för Tunnel 2 och klicka på **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-clients.png){class="glboxshadow"}

    9. Select target destination.

        Klicka på fliken **All Targets**, ange den som trafikdestination för Tunnel 2 och klicka på **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-all-targets.png){class="glboxshadow"}

    10. VPN Dashboard öppnas och VPN Tunnel 2 har lagts till.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-tunnel2.png){class="glboxshadow"}

    11. Kontrollera att **Kill Switch** för Tunnel 2 är aktiverad. Vid frånkoppling blockeras matchande trafik.

        ![kill switch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch3.png){class="glboxshadow"}

        ![kill switch4](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-killswitch4.png){class="glboxshadow"}

    12. Klicka på kugghjulet uppe till höger, aktivera **Enhanced Kill Switch** och klicka på **Apply**. All trafik kan då endast nå internet via VPN.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch2.png){class="glboxshadow"}

        **Enhanced Kill Switch** visas högst upp på sidan.

        ![enhanced killswitch3](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-enhanced-killswitch3.png){class="glboxshadow"}

    13. Klicka på mittknappen för att aktivera Tunnel 1 och Tunnel 2.

        ![case 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-start-vpn.png){class="glboxshadow"}

    14. Efter anslutning visas VPN-princip, klientens virtuella IP-adress, serveradress, lyssningsport och trafikstatistik.

        ![case 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/case2-connected.png){class="glboxshadow"}

        Alla enheter använder **VPN Tunnel 1** för angivna domäner och **VPN Tunnel 2** för övrig internetåtkomst. Om tunnlarna kopplas från blockeras internetåtkomsten.

## Kill Switch {#kill-switch}

VPN Kill Switch förhindrar att trafik återgår till en okrypterad internetanslutning när VPN misslyckas.

För en enskild tunnel blockerar **Kill Switch** internetåtkomst för tilldelad trafik om anslutningen misslyckas. Övrig trafik följer **All Other Traffic**.

**Enhanced Kill Switch** blockerar internettrafik som inte matchar någon VPN-tunnel och åsidosätter inte tunnelns **Kill Switch**.

Fortify supports Kill Switch configuration for the global VPN connection, as well as for each individual VPN tunnel.

- To set up Kill Switch for the global VPN connection (i.e., Enhanced Kill Switch), refer to [All Other Traffic](#all-other-traffic).

- To set up Kill Switch for each individual VPN tunnel, refer to [Tunnel Options](#tunnel-options).

## All Other Traffic {#all-other-traffic}

Klicka på kugghjulet uppe till höger för att konfigurera principen för trafik som inte matchar en VPN-tunnel.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/all_other_traffic.png){class="glboxshadow"}

Principen styr om trafik som inte matchar en tunnelgrupp får internetåtkomst. Alternativen är **Allow Non-VPN Traffic** och **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Enabled by default to ensure normal internet access for non-VPN traffic.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Tvingar alla enheter att använda VPN. Trafik som inte matchar en VPN-tunnel blockeras. Inställningen åsidosätter inte Kill Switch för enskilda tunnlar.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel Options {#tunnel-options}

Du kan konfigurera avancerade inställningar för varje VPN-tunnel, till exempel VPN Kill Switch, IP Masquerading och MTU.

Klicka på kugghjulet i en tunnelgrupp och välj **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: När alternativet är aktiverat blockeras matchande trafik om VPN misslyckas. När det är inaktiverat växlar trafiken till **All Other Traffic**.

- **Services from GL.iNet Use VPN**: GoodCloud, DDNS och rtty skickar paket genom VPN-tunnlar när alternativet är aktiverat. Det är inaktiverat som standard eftersom tjänsterna normalt kräver enhetens verkliga IP-adress.

- **Allow Remote Access to the LAN Subnet**: Tillåter fjärråtkomst till routern och LAN-enheter via VPN. VPN-servern måste annonsera en returväg till LAN-subnätet.

- **IP Masquerading**: Skriver om LAN-klienternas käll-IP-adresser till routerns VPN-tunnel-IP. Inaktivera endast för Site-to-Site där fjärrpeeren känner till LAN-subnäten.

- **MTU**: Tunnelns MTU-värde åsidosätter konfigurationsfilens MTU.

## Tunnel Priority {#tunnel-priority}

Ändra tunnelprioritet genom att klicka på kugghjulet i tunnelgruppen och välja **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority1.png){class="glboxshadow"}

Håll ikonen med tre linjer till höger och dra tunnlarna till önskad ordning. Klicka på **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/expressvpn_dashboard/priority2.png){class="glboxshadow"}

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
