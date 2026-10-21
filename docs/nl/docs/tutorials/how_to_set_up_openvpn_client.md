# Een OpenVPN-client instellen op GL.iNet-routers {#how-to-set-up-openvpn-client-on-glinet-routers}

In deze handleiding lees je hoe je een OpenVPN-client instelt op GL.iNet-routers.

Bekijk deze video of volg de onderstaande stappen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Zorg voordat je begint dat je een actief abonnement hebt bij een VPN-serviceprovider die handmatige OpenVPN-configuratie ondersteunt. Klik [hier](https://www.gl-inet.com/solutions/vpn/){target="_blank"} voor een overzicht van OpenVPN-providers die compatibel zijn met GL.iNet.

Hieronder vind je de stappen om een OpenVPN-client via het webbeheerpaneel van de router in te stellen.

## 1. Aanmelden bij je router {#1-log-in-to-your-router}

Open een webbrowser en ga naar het webbeheerpaneel van de router (standaard-IP-adres: 192.168.8.1). Meld je aan met je beheerderswachtwoord.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/router-login.jpeg){class="glboxshadow"}

## 2. De VPN-client instellen {#2-set-up-vpn-client}

Raadpleeg het gedeelte voor de VPN-serviceprovider die je gebruikt.

??? "NordVPN"

    1. Ga in het webbeheerpaneel van de router naar **VPN** > **OpenVPN Client**.

    2. Klik op **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Voer je serviceaanmeldgegevens in en klik op **Save and Continue**.

        Opmerking: dit zijn niet het e-mailadres en wachtwoord waarmee je je aanmeldt, maar de serviceaanmeldgegevens die je vindt op de NordVPN-website onder Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. Selecteer in het dialoogvenster de VPN-locaties waarmee je verbinding wilt maken en klik op **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Selecteer de VPN-server waarmee je verbinding wilt maken en klik op het pictogram met drie stippen en vervolgens op **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Andere VPN-serviceproviders (bijvoorbeeld Surfshark)"

    1. Ga in het webbeheerpaneel van de router naar **VPN** > **OpenVPN Client**.

    2. Klik op **Add Manually**.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Geef de configuratie een naam. Je kunt de naam van je VPN-serviceprovider invoeren. Klik vervolgens op het vinkje.

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Zorg dat je het configuratiebestand van je VPN-serviceprovider en eventuele serviceaanmeldgegevens hebt gedownload.
    5. Upload het gedownloade configuratiebestand.

        Voer indien nodig de serviceaanmeldgegevens in en klik op **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Klik naast het VPN-serveradres op het pictogram met drie stippen en vervolgens op **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. De VPN-verbinding controleren {#3-verify-vpn-connection}

Open een webbrowser en zoek je IP-adres en locatie op. Als deze overeenkomen met het IP-adres en de locatie van de VPN-server, in plaats van die van je internetprovider, is de VPN-verbinding geslaagd.

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
