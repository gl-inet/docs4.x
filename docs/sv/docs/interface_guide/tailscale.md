# Tailscale {#tailscale}

Tailscale är en VPN-tjänst som ger säker och enkel åtkomst till dina enheter och program var som helst. Mer information finns på [Tailscales webbplats](https://tailscale.com/){target="_blank"}.

Tailscale finns på GL.iNet-routrar från firmware v4.2 och låter routern ansluta till ett virtuellt nätverk för fjärråtkomst till WAN- och LAN-resurser.

**Note**:

1. Eftersom Tailscale bygger på WireGuard bör det inte användas samtidigt med OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier eller AstroWarp.

2. Funktionen är i beta och kan innehålla fel.

3. Some models, although running firmware v4.2 or higher, do not support Tailscale due to insufficient memory.

## Supported Models {#supported-models}

??? "Supported Models"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Unsupported Models"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Set up Tailscale network {#set-up-tailscale-network}

GL-MT2500 används som exempel.

1. Bind your devices.

    Registrera ett Tailscale-konto och koppla en eller två testenheter, till exempel telefon eller dator.

    Efter kopplingen visas enheterna och deras status i Tailscale Admin console.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Enable Tailscale on GL.iNet router.

    Logga in och öppna **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Aktivera Tailscale och klicka på **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Efter en stund visas **Device Bind Link**. Klicka på länken.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    Klicka på Tailscale-länken i popup-fönstret och logga in på webbplatsen.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Bekräfta enheten efter inloggning och klicka på **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    När anslutningen lyckas öppnas Tailscale Admin console. GL-MT2500 har IP-adressen `100.88.54.21`, som kan användas för åtkomst.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Test connectivity.

    Testa anslutningen från enheter i samma Tailscale-nätverk på följande tre sätt.

    * Use the ping command

        ![ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * SSH into the router

        ![ssh](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Access web Admin Panel

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Allow Remote Access WAN {#allow-remote-access-wan}

**Obs!** Funktionen heter **Advertise WAN Subnets** i firmware v4.9 och senare.

När alternativet är aktiverat kan WAN-resurser nås via Tailscale. Rutter gäller först efter godkännande i Tailscale Admin Console.

I topologin kan `leo-phone` nå `GL-AXT1800` via `192.168.29.1`, eftersom den är uppströms `GL-MT2500` i samma Tailscale-nätverk.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Följ stegen nedan.

1. Logga in och öppna **APPLICATIONS** -> **Tailscale**.

    Enable **Allow Remote Access WAN**, and click **Apply**.

    ![enable remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Öppna Tailscale Admin console. En varning visar att GL-MT2500 har subnät.

    Klicka på ikonen med tre punkter bredvid GL-MT2500 och välj **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Andra enheter kan nu nå GL-AXT1800 via `192.168.29.1` och alla enheter i `192.168.29.0/24`.

    ![tailscale access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN {#allow-remote-access-lan}

**Obs!** Funktionen heter **Advertise LAN Subnets** i firmware v4.9 och senare.

När alternativet är aktiverat kan LAN-resurser nås via Tailscale. Rutter gäller först efter godkännande i Tailscale Admin Console.

I topologin kan `leo-phone` SSH-logga in på `Ubuntu` via `192.168.8.110`, eftersom Ubuntu är nedströms GL-MT2500 i samma nätverk.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Följ stegen nedan.

1. Logga in och öppna **APPLICATIONS** -> **Tailscale**.

    Enable **Allow Remote Access LAN**, and click **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Öppna Tailscale Admin console. En varning visar att GL-MT2500 har subnät.

    Klicka på ikonen med tre punkter bredvid GL-MT2500 och välj **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Enable the subnet routes.

    ![tailscale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Andra enheter kan nu pinga eller SSH-logga in på Ubuntu via `192.168.8.110` och nå alla enheter i `192.168.8.0/24`.

    ![tailscale access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Custom Exit Nodes {#custom-exit-nodes}

Som standard är Tailscale ett overlay-nätverk som endast dirigerar trafik mellan Tailscale-enheter och inte offentlig internettrafik.

Om offentlig internettrafik ska dirigeras via Tailscale kan en hemdator med offentlig IP anges som Exit Node. Andra enheter i samma Tailnet, till exempel GL-AXT1800 och GL-MT3000, skickar då trafiken genom den.

![exitnode](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

När all trafik går via Exit Node används standardrutterna `0.0.0.0/0` och `::/0`, liknande en vanlig VPN-anslutning.

En Exit Node dirigerar utgående internettrafik från Tailnet-enheter och fungerar som VPN-server. Trafiken ser ut att komma från nodens plats, vilket hjälper med geografiskt begränsat innehåll och integritet.

**Obs!** Om routerns DNS-server har en privat IP-adress kan internet försvinna med Exit Node. Öppna **NETWORK** -> **DNS** och ange en offentlig DNS-server som 8.8.8.8.

---

I exemplet finns **GL-MT2500** och **Leo-Desktop** i samma Tailnet.

Följ stegen för att ange Leo-Desktop som Exit Node. Se [IP Masquerading](#ip-masquerading) för en alternativ metod.

1. Aktivera subnätsrutter för GL-MT2500 i Tailscale Admin console.

    Klicka på ikonen med tre punkter bredvid GL-MT2500 och välj **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    In the pop-up window, enable the subnet routes.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Välj **Run exit node** på enheten som ska vara Exit Node, här Leo-Desktop. Exemplet använder Windows.

    ![tailscale windows run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Then click **Yes**.

    ![tailscale windows run exit ndoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. In the Tailscale Admin console, set up the Leo-Desktop as an Exit node.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Logga in på GL-MT2500, öppna **APPLICATIONS** -> **Tailscale**, aktivera **Custom Exit Nodes**, uppdatera, välj Leo-Desktops IP-adress och klicka på **Apply**.

    ![glinet tailscale custom exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Anslutna enheter dirigerar då internettrafiken genom Exit Node och trafiken ser ut att komma från nodens plats.

5. **Felsökning**: Om internet saknas efter Custom Exit Node kontrollerar du routerns subnätsrutter i Tailscale Admin console.

    A corresponding prompt may appear in the router's web Admin Panel as shown below.

    ![exit node troubleshooting](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Aktivera subnätsrutterna enligt **Steg 1**.

## Run Exit Node {#run-exit-node}

**Note**: This feature was introduced in firmware v4.9.

En Exit Node på routern låter andra Tailnet-enheter dirigera all utgående trafik via routerns offentliga IP.

I topologin finns en dator i Boston och GL-BE9300 i Hongkong i samma Tailnet. Med GL-BE9300 som Exit Node går all utgående trafik via Hongkong och datorns offentliga IP blir en Hongkong-adress.

![topology run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Tip**: We recommend disabling key expiry for the exit node to prevent connectivity interruptions when the node authentication key expires.*

Följ stegen för att ange GL-BE9300 som Exit Node.

1. Lägg till GL-BE9300 och resedatorn i samma Tailnet.

    ![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. Aktivera **Run Exit Node** på GL-BE9300 och klicka på **Apply**.

    ![run exit node1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. I Tailscale Admin Console visas taggen "Exit Node" under GL-BE9300.

    ![run exit node2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Klicka på ikonen med tre punkter bredvid GL-BE9300 och välj **Edit route settings**.

    ![run exit node3](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. Markera **Use as exit node** och klicka på **Save**.

    ![run exit node4](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Disable key expiry.

    Av säkerhetsskäl krävs regelbunden omautentisering. Inaktivera nyckelutgång för Exit Node för att undvika avbrott. Mer information finns [här](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"}.

    Klicka på ikonen med tre punkter bredvid GL-BE9300 och välj **Disable key expiry**.

    ![disable key expiry1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    Once applied, a tag "Expiry disabled" will appear under the GL-BE9300.

    ![disable key expiry2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Välj GL-BE9300 som Exit Node för resedatorn.

    Starta Tailscale på resedatorn. Ikonen visas i systemfältet nere till höger.

    Högerklicka på ikonen, klicka på **Exit nodes** och välj **gl-be9300**.

    ![run exit node5](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    All utgående trafik från resedatorn går nu via GL-BE9300.

8. Test connectivity.

    1. Öppna [ipcheck.ing](https://ipcheck.ing/){target="_blank"} eller en annan IP-tjänst. Sidan ska visa Exit Nodes offentliga IP-adress, i exemplet GL-BE9300 i Hongkong.

        ![ip hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Tryck `Win+R`, skriv `cmd` och kör `tracert google.com`. Första externa hoppet ska gå via Exit Node.

        ![tracert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Disconnect the exit node for a comparative test.

        Högerklicka på Tailscale-ikonen, klicka på **Exit nodes** och välj **None** för att sluta använda noden.

        ![comparative test](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Öppna [ipcheck.ing](https://ipcheck.ing/){target="_blank"}. Datorns vanliga offentliga IP visas och bekräftar lokal internetanslutning.

        ![ip boston](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}


Mer information finns i [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}.

## IP Masquerading {#ip-masquerading}

**Note**: This feature was introduced in firmware v4.9.

IP Masquerading skriver om käll-IP från LAN-klienter till routerns Tailscale-gränssnittsadress. Andra noder ser då trafiken som om den kommer från routern.

IP Masquerading is recommended in the following scenarios:

- Vid egen Exit Node när du vill undvika subnätsrutter i Tailscale Admin console och vidarebefordra all klienttrafik enklare.

- När LAN-enheter inte kan installera Tailscale men behöver åtkomst via routern.

I exemplet finns GL‑BE9300 och GL-MG1300 i samma Tailnet.

![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailnet.png){class="glboxshadow"}

Follow the steps below to configure a **custom exit node** on the GL‑BE9300.

1. Log in to the GL-BE9300's web Admin Panel, go to **APPLICATIONS** -> **Tailscale**, enable **IP Masquerading**, then click **Apply**.

    ![iP masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ip_masquerading.png){class="glboxshadow"}

    Med IP Masquerading krävs inga subnätsrutter. LAN-klienter når nätverket via routerns virtuella Tailscale-IP.

    I det här exemplet har GL-BE9300 (`100.115.61.35`) och GL-MG1300 (`100.113.50.89`) virtuella Tailscale-IP-adresser. En dator ansluten till GL-BE9300 kan öppna webbadministrationspanelen på GL-MG1300 direkt med IP-adressen för GL-BE9300:s Tailscale-gränssnitt som källadress.

    ![test iP masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/test_ip_masquerading.png){class="glboxshadow"}

2. Välj enheten som Exit Node, här GL-MG1300, och aktivera **Run exit node**.

    ![run exit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_1.png){class="glboxshadow" width=600}

    Then click **Apply**.

    ![run exit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_2.png){class="glboxshadow"}

3. In the Tailscale Admin console, set up the GL-MG1300 as an Exit node.

    ![tailscale exit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_1.png){class="glboxshadow"}

    ![tailscale exit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_2.png){class="glboxshadow" width=500}

    Aktivera **Disable Key Expiry** för att undvika avbrott när autentiseringsnyckeln går ut.

    ![disable key expirty 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_1.png){class="glboxshadow"}

    ![disable key expirty 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_2.png){class="glboxshadow"}

4. Öppna **APPLICATIONS** -> **Tailscale** på GL-BE9300, aktivera **Custom Exit Nodes**, uppdatera, välj GL-MG1300:s IP och klicka på **Apply**.

    ![custom exit nodes 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes_1.png){class="glboxshadow"}

Efter konfiguration går trafik från enheter på GL-BE9300 via Exit Node GL-MG1300 och ser ut att komma från nodens plats.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
