# Een OpenVPN-server instellen op GL.iNet-routers {#how-to-set-up-openvpn-server-on-glinet-routers}

In deze handleiding lees je hoe je een OpenVPN-server instelt op GL.iNet-routers. Met een VPN-server kun je op afstand een beveiligde verbinding met je thuis- of kantoornetwerk tot stand brengen. Op een GL.iNet-router kun je binnen enkele minuten een OpenVPN-server instellen.

!!! note "Controleer voordat je begint of je aan de volgende vereisten voldoet"

    **Openbaar IP-adres**

    Voor het instellen van een OpenVPN-server is een openbaar IP-adres vereist. Raadpleeg [deze handleiding](how_to_check_if_isp_assigns_you_a_public_ip_address.md) om te controleren of je er een hebt.

    **Port forwarding**

    Als je GL.iNet-router achter een primaire router is aangesloten, moet je [port forwarding op de primaire router instellen](how_to_set_up_port_forwarding.md).

## 1. Aanmelden bij je router {#1-log-in-to-your-router}

Open een webbrowser en ga naar het webbeheerpaneel van de router (standaard-IP-adres: 192.168.8.1). Meld je aan met je beheerderswachtwoord.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Dynamic DNS inschakelen (optioneel) {#2-enable-dynamic-dns-optional}

Voor het instellen van een OpenVPN-server is doorgaans een **statisch openbaar IP-adres** vereist. Dit biedt een vast eindpunt waarmee andere apparaten toegang kunnen krijgen tot je VPN-server.

Als je geen statisch openbaar IP-adres hebt maar bijvoorbeeld een dynamisch adres, moet je mogelijk **Dynamic DNS (DDNS)** inschakelen op je GL.iNet-router. Hierdoor blijft de OpenVPN-server bereikbaar wanneer je openbare IP-adres dynamisch verandert.

Volg de onderstaande stappen om Dynamic DNS in te schakelen.

1. Ga in het webbeheerpaneel van de router naar **APPLICATIONS** > **Dynamic DNS**.
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Schakel **Enable DDNS** in, lees en accepteer de **Terms of Service & Privacy Policy** en klik op **Apply**.
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Het configuratiebestand downloaden {#3-download-configuration-file}

1. Ga in het webbeheerpaneel van de router naar **VPN** > **OpenVPN Server**.
2. Klik op **Generate Configuration**.
3. Behoud de standaardinstellingen en klik op **Export Client Configuration**.
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. Schakel in het pop-upvenster **Use DDNS Domain** in als je eerder **Dynamic DNS** hebt ingesteld.
5. Klik op **Download** en sla het bestand op.
6. Klik bovenaan de pagina **OpenVPN Server** op **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Optioneel) Schakel deze instellingen in om toegang te krijgen tot het lokale netwerk van de VPN-server:"

    Voor firmware v4.7 en ouder:

    1. Klik in de linkerzijbalk op **VPN** > **VPN Dashboard**.
    2. Klik op het pictogram Options.
    3. Schakel **Remote Access LAN** in.
    4. Klik op **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Voor firmware v4.8 en nieuwer:

    1. Klik in de linkerzijbalk op **VPN** > **OpenVPN Server**.
    2. Klik rechtsboven op **Options**.
    3. Schakel **Allow Remote Access the LAN Subnet** in.
    4. Klik op **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Verbinding maken met de OpenVPN-server {#4-connect-to-openvpn-server}

Je hebt een OpenVPN-client nodig om verbinding te maken met de OpenVPN-server. Je kunt deze met een van de onderstaande methoden instellen:

??? "Methode 1: een OpenVPN-clientapp van derden (gebruik deze methode als je geen extra router hebt die als OpenVPN-client kan worden ingesteld)"

    In deze handleiding gebruiken we OpenVPN Connect, de officiële app van OpenVPN Inc, als voorbeeld.

    1. Verbind een ander apparaat met een ander Wi-Fi-netwerk, of met een mobiel netwerk als je een mobiel apparaat gebruikt.
    2. Stuur het eerder gedownloade configuratiebestand naar het apparaat, bijvoorbeeld via e-mail, en download het bestand op dat apparaat.
    3. Download OpenVPN Connect voor het besturingssysteem van je apparaat:
        * [Windows](https://openvpn.net/client/)
        * [Mac](https://openvpn.net/client/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/client/)
    4. Lees de voorwaarden in de app en selecteer **Agree**.
    5. Selecteer **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Selecteer **Browse** en selecteer vervolgens het configuratiebestand dat je eerder hebt gedownload.
    7. Selecteer **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Selecteer **Connect** > **OK** > **Allow**.

    Bovenaan het VPN-profiel verschijnt het woord "Connected".
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Methode 2: een router die als OpenVPN-client kan worden ingesteld"

    Je kunt elke router gebruiken die handmatige OpenVPN-clientconfiguratie ondersteunt. In deze handleiding gebruiken we de GL.iNet-reisrouter [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/) als voorbeeld.

    1. Verbind een ander apparaat met een ander Wi-Fi-netwerk, of met een mobiel netwerk als je een mobiel apparaat gebruikt.
    2. Voer in de adresbalk van een webbrowser de URL van het webbeheerpaneel van je router in, bijvoorbeeld 192.168.8.1.
    3. Voer je wachtwoord in en klik op **Login**.
    4. Klik in de linkerzijbalk op **VPN** > **OpenVPN Client**.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Klik op **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Voer een naam in het veld in en klik op het vinkje.
    7. Upload het configuratiebestand dat je eerder hebt gedownload.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Klik op **Apply**.
    9. Klik op het pictogram met drie stippen en vervolgens op **Start**.
    10. Verbind een apparaat met de router waarop de OpenVPN-client wordt uitgevoerd.

## 5. De VPN-verbinding controleren {#5-verify-vpn-connection}

Open een webbrowser en zoek je IP-adres en locatie op. Als deze overeenkomen met het IP-adres en de locatie van de VPN-server, in plaats van die van je internetprovider, is de VPN-verbinding geslaagd.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
