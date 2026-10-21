# Tailscale {#tailscale}

Tailscale is een VPN-dienst waarmee je overal ter wereld veilig en eenvoudig toegang hebt tot je apparaten en toepassingen. Ga voor meer informatie naar de [officiële Tailscale-website](https://tailscale.com/){target="_blank"}.

De Tailscale-functie op GL.iNet-routers is beschikbaar sinds firmware v4.2 en laat de router deelnemen aan een virtueel Tailscale-netwerk. Daarna kun je op afstand de router en zijn WAN- en LAN-bronnen openen.

**Note**:

1. Omdat Tailscale op WireGuard is gebaseerd, wordt gelijktijdig gebruik met OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier of AstroWarp wegens mogelijke routeringsconflicten afgeraden.

2. Deze functie is momenteel in bèta en kan fouten bevatten.

3. Sommige modellen ondersteunen Tailscale wegens onvoldoende geheugen niet, ook niet met firmware v4.2 of hoger.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
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

??? "Niet-ondersteunde modellen"
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

## Tailscale-netwerk instellen {#set-up-tailscale-network}

GL-MT2500 wordt hieronder als voorbeeld gebruikt.

1. Koppel je apparaten.

    Maak eerst een Tailscale-account en koppel voor een test één of twee apparaten, zoals een smartphone of laptop.

    Na het koppelen zie je de apparaten en hun status in Tailscale Admin.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Schakel Tailscale op de GL.iNet-router in.

    Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Schakel Tailscale in en klik op **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Na korte tijd toont de interface een **Device Bind Link**. Klik op de link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    In het pop-upvenster verschijnt een Tailscale-link. Klik erop en meld je aan op de Tailscale-website.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Na het aanmelden wordt gevraagd het apparaat te bevestigen. Klik op **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Na een geslaagde verbinding wordt Tailscale Admin geopend. Het IP-adres van GL-MT2500 is `100.88.54.21`; gebruik dit om de router te openen.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Test de verbinding.

    Op apparaten in hetzelfde Tailscale-netwerk kun je de verbinding op drie manieren testen.

    * Gebruik de ping-opdracht

        ![ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * Meld je via SSH bij de router aan

        ![ssh](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Open het webbeheerpaneel

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Externe WAN-toegang toestaan {#allow-remote-access-wan}

**Opmerking**: deze functie heet in firmware v4.9 en hoger **Advertise WAN Subnets**.

Wanneer dit is ingeschakeld, zijn bronnen aan de WAN-zijde via het virtuele Tailscale-netwerk toegankelijk. Routes werken pas na goedkeuring in Tailscale Admin.

In de onderstaande topologie kun je na inschakeling vanaf `leo-phone` GL-AXT1800 via `192.168.29.1` openen. GL-AXT1800 is het upstream apparaat van GL-MT2500, die in hetzelfde Tailscale-netwerk zit.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Volg deze stappen om de functie in te stellen.

1. Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **Tailscale**.

    Schakel **Allow Remote Access WAN** in en klik op **Apply**.

    ![enable remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Open Tailscale Admin. Er verschijnt een melding dat GL-MT2500 subnets heeft.

    Klik rechts van GL-MT2500 op het pictogram met drie stippen en selecteer **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Schakel de subnetroutes in.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Je kunt GL-AXT1800 vanaf andere apparaten via `192.168.29.1` openen, evenals alle apparaten in `192.168.29.0/24`.

    ![tailscale access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Externe LAN-toegang toestaan {#allow-remote-access-lan}

**Opmerking**: deze functie heet in firmware v4.9 en hoger **Advertise LAN Subnets**.

Wanneer dit is ingeschakeld, zijn bronnen aan de LAN-zijde via het virtuele Tailscale-netwerk toegankelijk. Routes werken pas na goedkeuring in Tailscale Admin.

In de onderstaande topologie kun je vanaf `leo-phone` via SSH bij `Ubuntu` op `192.168.8.110` aanmelden. Ubuntu is een downstream apparaat van GL-MT2500 in hetzelfde Tailscale-netwerk.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Volg deze stappen om de functie in te stellen.

1. Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **Tailscale**.

    Schakel **Allow Remote Access LAN** in en klik op **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Open Tailscale Admin. Er verschijnt een melding dat GL-MT2500 subnets heeft.

    Klik rechts van GL-MT2500 op het pictogram met drie stippen en selecteer **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Schakel de subnetroutes in.

    ![tailscale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Je kunt vanaf andere apparaten Ubuntu op `192.168.8.110` pingen of via SSH openen, evenals alle apparaten in `192.168.8.0/24`.

    ![tailscale access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Aangepaste exit nodes {#custom-exit-nodes}

Tailscale werkt standaard als overlaynetwerk: het routeert alleen verkeer tussen Tailscale-apparaten en verwerkt geen openbaar internetverkeer.

Je kunt Tailscale openbaar internetverkeer laten routeren, bijvoorbeeld om in het buitenland diensten uit je thuisland te gebruiken. Stel je thuiscomputer met openbaar IP-adres als Exit Node in en laat apparaten in dezelfde Tailnet hun verkeer erdoor sturen.

![exitnode](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Wanneer al het verkeer via een Exit Node loopt, worden de standaardroutes 0.0.0.0/0 en ::/0 gebruikt, vergelijkbaar met een gewone VPN.

Een exit node routeert uitgaand internetverkeer van Tailnet-apparaten en werkt als VPN-server. Niet-Tailscale-internetverkeer lijkt vanaf de locatie van de exit node te komen, voor geografisch beperkte inhoud en meer privacy.

**Opmerking**: als de DNS-server een privé-IP-adres gebruikt dat alleen lokaal bereikbaar is, kan een exit node de internetverbinding verliezen. Stel onder **NETWORK** -> **DNS** handmatig een openbare DNS-server in, zoals 8.8.8.8.

---

In het volgende voorbeeld bevinden **GL-MT2500** en **Leo-Desktop** zich in dezelfde Tailnet.

Volg de stappen om Leo-Desktop als Exit Node in te stellen. Raadpleeg [IP Masquerading](#ip-masquerading) voor een alternatieve methode.

1. Schakel de subnetroutes van GL-MT2500 in Tailscale Admin in.

    Open Tailscale Admin, klik rechts van GL-MT2500 op het pictogram met drie stippen en selecteer **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    Schakel in het pop-upvenster de subnetroutes in.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Selecteer op het apparaat dat als exit node moet werken, hier Leo-Desktop, **Run exit node**. Windows wordt als voorbeeld gebruikt.

    ![tailscale windows run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Klik vervolgens op **Yes**.

    ![tailscale windows run exit ndoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Stel Leo-Desktop in Tailscale Admin als Exit Node in.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Meld je aan bij GL-MT2500, ga naar **APPLICATIONS** -> **Tailscale** en schakel **Custom Exit Nodes** in. Klik op vernieuwen, selecteer het IP-adres van Leo-Desktop en klik op **Apply**.

    ![glinet tailscale custom exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Verbonden apparaten routeren hun verkeer vervolgens via de Exit Node en internetverkeer lijkt vanaf de locatie daarvan te komen.

5. **Probleemoplossing**: als apparaten na het inschakelen van Custom Exit Node geen internet hebben, controleer je in Tailscale Admin of de subnetroutes zijn ingeschakeld.

    In het webbeheerpaneel kan de onderstaande melding verschijnen.

    ![exit node troubleshooting](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Schakel de subnetroutes in Tailscale Admin in zoals beschreven in **stap 1**.

## Als exit node werken {#run-exit-node}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Als de router als exit node werkt, kunnen andere Tailnet-apparaten al hun uitgaande internetverkeer via het openbare IP-adres van deze router sturen.

In de onderstaande topologie staat een laptop in Boston en GL-BE9300 in Hongkong, beide in dezelfde Tailnet. Met GL-BE9300 als exit node verlaat al het laptopverkeer internet via Hongkong en krijgt de laptop een openbaar IP-adres uit Hongkong.

![topology run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Tip**: schakel key expiry voor de exit node uit om onderbrekingen bij het verlopen van de verificatiesleutel te voorkomen.*

Volg deze stappen om GL-BE9300 als Exit Node in te stellen.

1. Voeg GL-BE9300 en de reislaptop aan dezelfde Tailscale Tailnet toe.

    ![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. Schakel in het webbeheerpaneel van GL-BE9300 **Run Exit Node** in en klik op **Apply**.

    ![run exit node1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. Open Tailscale Admin. Onder GL-BE9300 staat de tag "Exit Node".

    ![run exit node2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Klik rechts van GL-BE9300 op het pictogram met drie stippen en selecteer **Edit route settings**.

    ![run exit node3](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. Selecteer in het pop-upvenster **Use as exit node** en klik op **Save**.

    ![run exit node4](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Schakel het verlopen van sleutels uit.

    Gebruikers moeten zich periodiek opnieuw verifiëren. Schakel key expiry voor de exit node uit om onderbrekingen te voorkomen. Klik [hier](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"} voor meer informatie.

    Klik rechts van GL-BE9300 op het pictogram met drie stippen en selecteer **Disable key expiry**.

    ![disable key expiry1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    Daarna verschijnt onder GL-BE9300 de tag "Expiry disabled".

    ![disable key expiry2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Selecteer GL-BE9300 als exit node voor de reislaptop.

    Start Tailscale op de reislaptop. Het Tailscale-pictogram verschijnt rechtsonder in het systeemvak.

    Klik met rechts op het pictogram, klik op **Exit nodes** en selecteer **gl-be9300**.

    ![run exit node5](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    Al het uitgaande verkeer van de reislaptop loopt nu via GL-BE9300.

8. Test de verbinding.

    1. Open op de reislaptop [ipcheck.ing](https://ipcheck.ing/){target="_blank"} of een andere IP-zoeksite. Het openbare IP-adres van de Tailscale-exit node bevestigt dat de laptop via GL-BE9300 in Hongkong internet gebruikt.

        ![ip hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Druk op `Win+R`, voer `cmd` in en voer `tracert google.com` uit. De uitvoer toont alle routeringshops. Bij een juiste configuratie loopt de eerste externe hop via de exit node.

        ![tracert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Verbreek de exit node voor een vergelijkingstest.

        Klik met rechts op het Tailscale-pictogram, klik op **Exit nodes** en selecteer **None**.

        ![comparative test](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Open [ipcheck.ing](https://ipcheck.ing/){target="_blank"} opnieuw. Het eigen openbare IP-adres van de laptop toont dat de lokale verbinding wordt gebruikt.

        ![ip boston](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}


Raadpleeg [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"} voor meer informatie.

## IP Masquerading {#ip-masquerading}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

IP Masquerading herschrijft bron-IP-adressen van LAN-clients naar het Tailscale-interfaceadres van de router. Andere Tailscale-nodes zien doorgestuurd verkeer daardoor als afkomstig van de router en niet van de oorspronkelijke client.

IP Masquerading wordt aanbevolen wanneer:

- Je een aangepaste exit node instelt zonder subnetroutes in Tailscale Admin te configureren.

- LAN-apparaten Tailscale niet kunnen installeren maar via de router toegang nodig hebben.

In het onderstaande voorbeeld zitten GL‑BE9300 en GL-MG1300 in dezelfde Tailnet.

![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailnet.png){class="glboxshadow"}

Volg de onderstaande stappen om een **aangepaste exit node** op GL‑BE9300 te configureren.

1. Meld je aan bij GL-BE9300, ga naar **APPLICATIONS** -> **Tailscale**, schakel **IP Masquerading** in en klik op **Apply**.

    ![iP masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ip_masquerading.png){class="glboxshadow"}

    Met IP Masquerading hoeven geen subnetroutes in Tailscale Admin te worden ingesteld. LAN-clients hebben rechtstreeks via het virtuele Tailscale-IP van de router toegang.

    In dit voorbeeld hebben GL-BE9300 (100.115.61.35) en GL-MG1300 (100.113.50.89) een virtueel Tailscale-IP. Een pc op GL‑BE9300 kan het webbeheerpaneel van GL‑MG1300 rechtstreeks via dit netwerk openen.

    ![test iP masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/test_ip_masquerading.png){class="glboxshadow"}

2. Selecteer het apparaat dat als exit node moet werken, hier GL-MG1300, en schakel **Run exit node** in.

    ![run exit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_1.png){class="glboxshadow" width=600}

    Klik vervolgens op **Apply**.

    ![run exit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_2.png){class="glboxshadow"}

3. Stel GL-MG1300 in Tailscale Admin als Exit Node in.

    ![tailscale exit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_1.png){class="glboxshadow"}

    ![tailscale exit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_2.png){class="glboxshadow" width=500}

    Schakel **Disable Key Expiry** in om onderbrekingen bij het verlopen van de verificatiesleutel te voorkomen.

    ![disable key expirty 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_1.png){class="glboxshadow"}

    ![disable key expirty 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_2.png){class="glboxshadow"}

4. Ga terug naar GL-BE9300, ga naar **APPLICATIONS** -> **Tailscale** en schakel **Custom Exit Nodes** in. Klik op vernieuwen, selecteer het IP-adres van GL-MG1300 en klik op **Apply**.

    ![custom exit nodes 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes_1.png){class="glboxshadow"}

Na configuratie routeren apparaten op GL-BE9300 hun internetverkeer via exit node GL-MG1300 en lijkt het verkeer vanaf diens locatie te komen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
