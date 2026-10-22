# VPN-obfuscatie instellen op GL.iNet-routers {#how-to-set-up-vpn-obfuscation-on-glinet-routers}

**Opmerking**: GL.iNet-routers ondersteunen AmneziaWG met firmware v4.9 of nieuwer. Upgrade je router eerst naar een ondersteunde firmwareversie.

In deze handleiding worden twee scenario's beschreven voor het instellen van AmneziaWG-obfuscatie op GL.iNet-routers.

## Scenario 1. Twee GL.iNet-routers gebruiken {#scenario-1-using-two-glinet-routers}

In dit scenario worden twee GL.iNet-routers gebruikt om via het AmneziaWG-protocol een VPN-verbinding met obfuscatie tot stand te brengen.

- Brume 3 (GL-MT5000): een VPN-server voor thuisgebruik.
- Beryl AX (GL-MT3000): een draagbare VPN-client voor onderweg.

### De VPN-server instellen {#set-up-vpn-server}

1. Meld je aan bij het webbeheerpaneel van de Brume 3.

    Verbind een apparaat, zoals je laptop of pc, via een ethernetkabel met de LAN-poort van de Brume 3. Open een browser, voer het standaardbeheeradres in, doorgaans `192.168.8.1`, en meld je aan met je beheerderswachtwoord.

2. Voltooi de eerste configuratie van de Brume 3 voor internettoegang.

    Als de Brume 3 als primaire router wordt gebruikt, verbind je de WAN-poort met het upstream netwerk, zoals een ISP-modem.

    Als de Brume 3 niet de primaire router is, en dus een ander upstream apparaat zoals een ISP-router als primaire router fungeert, moet je **port forwarding** op je primaire router instellen. Raadpleeg [deze handleiding](how_to_set_up_port_forwarding.md).

3. Schakel DDNS in (optioneel).

    Schakel de DDNS-functie in als je openbare IP-adres dynamisch is in plaats van statisch.

    Ga in de linkerzijbalk naar **APPLICATIONS** -> **Dynamic DNS**. Schakel **Enable DDNS** in, accepteer de **Terms of Service & Privacy Policy** en klik op **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/enable_ddns.png){class="glboxshadow"}

4. Schakel VPN-obfuscatie in.

    Ga in de linkerzijbalk naar **VPN** > **WireGuard Server** -> het tabblad **Configurations**, schakel **Enable Obfuscation** in en klik op **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Je kunt de obfuscatieparameters naar wens aanpassen. Klik [hier](../faq/amneziawg_obfuscation.md#parameter-overview) voor meer informatie.

    We raden aan de standaardinstellingen te behouden.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Exporteer het configuratiebestand.

    Ga op de pagina **WireGuard Server** naar het tabblad **Profiles** en klik op **Add** om een configuratiebestand te maken waarmee Beryl AX verbinding kan maken.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Voer een herkenbare naam in, bijvoorbeeld Travel Router, en klik op **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    Klik in het pop-upvenster op **Export** om het configuratiebestand naar je apparaat te downloaden voor later gebruik.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Start de VPN-server.

    Klik bovenaan de pagina **WireGuard Server** op **Start** om de server te starten.

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    Je VPN-server met AmneziaWG-obfuscatie is nu ingeschakeld. Je kunt via de AmneziaWG-app of een GL.iNet-router met firmware die AmneziaWG-obfuscatie ondersteunt verbinding maken met deze VPN-server op de Brume 3.

    **Opmerking: clients die AmneziaWG-obfuscatie niet ondersteunen, kunnen geen verbinding maken.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

### De VPN-client instellen {#set-up-vpn-client}

1. Meld je aan bij het webbeheerpaneel van de Beryl AX.

    Verbind een apparaat, zoals je laptop of pc, via het Wi-Fi-netwerk of met een ethernetkabel via de LAN-poort met de Beryl AX. Open een browser, voer het standaardbeheeradres in, doorgaans `192.168.8.1`, en meld je aan met je beheerderswachtwoord.

2. Voltooi de eerste configuratie van de Beryl AX voor internettoegang.

    **Tips**: verbind de Beryl AX met een ander netwerk dan de Brume 3. Je kunt bijvoorbeeld een mobiele hotspot inschakelen waarmee de Beryl AX verbinding kan maken.

3. Upload het configuratiebestand.

    Ga in de linkerzijbalk naar **VPN** > **WireGuard Client**. Voeg een nieuwe groep toe en geef deze een herkenbare naam, bijvoorbeeld Home Router.

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Upload aan de rechterkant het eerder geëxporteerde configuratiebestand.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Klik op **Apply** nadat het configuratiebestand is geüpload en geverifieerd.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    De pagina wordt vernieuwd en één configuratiebestand wordt in de lijst weergegeven.

4. Start de VPN-verbinding.

    Klik op het pictogram met drie stippen en selecteer **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Wacht ongeveer 1 minuut. Als de statusindicator groen wordt, is de VPN-verbinding geslaagd.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Ga naar **VPN Dashboard**. Je ziet dat de Beryl AX is verbonden met de Brume 3-thuisrouter.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Controleer dit nogmaals (optioneel).

    Meld je aan bij het webbeheerpaneel van de Brume 3 en ga naar **VPN** -> **WireGuard Server**. Hier zie je ook een online client: Beryl AX, die momenteel met deze VPN-server op de Brume 3 is verbonden.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    De VPN-verbinding is voltooid. Alle apparaten op de Beryl AX gebruiken nu de gateway van de Brume 3 voor internettoegang, met een VPN-verbinding waarop obfuscatie is toegepast.

## Scenario 2. Eén GL.iNet-router gebruiken {#scenario-2-using-a-single-glinet-router}

In dit scenario wordt één GL.iNet-router, **Brume 3 (GL-MT5000)**, gebruikt als VPN-client die verbinding maakt met een AmneziaVPN-server.

In dit geval hoef je geen eigen server te implementeren. Download een AmneziaWG-configuratiebestand van de [officiële Amnezia-website](https://amnezia.org/){target="_blank"} of van een VPN-serviceprovider met AmneziaWG-integratie en upload het bestand naar je GL.iNet-router. Je kunt vervolgens een VPN-verbinding met obfuscatie tot stand brengen.

### De configuratie downloaden {#download-configuration}

<u>Optie 1</u>: download een configuratie van Amnezia Official (Premium-abonnement vereist).

1. Meld je met je Subscription Key aan bij het [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"}.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Ga in het Amnezia Dashboard naar **Connection Assets** -> **Configuration Files**, selecteer een land en download een configuratiebestand naar je lokale apparaat voor later gebruik.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Optie 2</u>: download een configuratie van een andere VPN-provider met AmneziaWG-integratie.

We gebruiken StarVPN als voorbeeld.

1. Ga naar de [abonnementen van StarVPN](https://www.starvpn.com/#pricing){target="_blank"} en kies een VPN-abonnement dat bij je behoeften past. Je kunt bij het afrekenen of rechtstreeks [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"} een StarVPN-account registreren.

2. Meld je aan bij het [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"}, zoek **VPN Configuration** en klik op **AmneziaWG Config** om het configuratiebestand te downloaden.

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. De configuratie kan een IPv6-adres bevatten. Open het .conf-bestand en verwijder het IPv6-adres zoals hieronder om compatibiliteits- en verbindingsproblemen te voorkomen.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Volg vervolgens de onderstaande stappen om de VPN-client in te stellen.

### De VPN-client instellen {#set-up-vpn-client_1}

1. Meld je aan bij het webbeheerpaneel van de Brume 3.

    Verbind een apparaat, zoals je laptop of pc, via een ethernetkabel met de LAN-poort van de Brume 3. Open een browser, voer het standaardbeheeradres in, doorgaans `192.168.8.1`, en meld je aan met je beheerderswachtwoord.

2. Voltooi de eerste configuratie van de Brume 3 voor internettoegang.

3. Upload het configuratiebestand.

    Ga in de linkerzijbalk naar **VPN** > **WireGuard Client**. Voeg een nieuwe groep toe en geef deze een herkenbare naam, bijvoorbeeld AmneziaVPN.

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Upload aan de rechterkant het eerder geëxporteerde AmneziaVPN-configuratiebestand.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Klik op **Apply** nadat het configuratiebestand is geüpload en geverifieerd.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    De pagina wordt vernieuwd en één configuratiebestand wordt in de lijst weergegeven.

4. Start de VPN-verbinding.

    Klik op het pictogram met drie stippen en selecteer **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Wacht ongeveer 1 minuut. Als de statusindicator groen wordt, is de VPN-verbinding geslaagd.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Ga naar **VPN Dashboard**. Je ziet dat de Brume 3 is verbonden met een AmneziaVPN-server.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    De VPN-verbinding is voltooid. Alle apparaten op de Brume 3 gebruiken nu de AmneziaVPN-server voor internettoegang, met een VPN-verbinding waarop obfuscatie is toegepast.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
