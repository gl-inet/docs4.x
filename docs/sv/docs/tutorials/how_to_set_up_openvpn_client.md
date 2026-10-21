# Konfigurera en OpenVPN-klient på GL.iNet-routrar {#how-to-set-up-openvpn-client-on-glinet-routers}

Den här guiden visar hur du konfigurerar en OpenVPN-klient på GL.iNet-routrar.

Titta på videon eller följ stegen nedan.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Kontrollera innan du börjar att du har en aktiv prenumeration hos en VPN-tjänsteleverantör som stöder manuell OpenVPN-konfiguration. Klicka [här](https://www.gl-inet.com/solutions/vpn/){target="_blank"} för att se vilka OpenVPN-leverantörer som är kompatibla med GL.iNet.

Följ stegen nedan för att konfigurera en OpenVPN-klient via routerns webbadministrationspanel.

## 1. Logga in på routern {#1-log-in-to-your-router}

Öppna en webbläsare och gå till routerns webbadministrationspanel (standard-IP: 192.168.8.1). Logga in med administratörslösenordet.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/router-login.jpeg){class="glboxshadow"}

## 2. Konfigurera VPN-klienten {#2-set-up-vpn-client}

Följ avsnittet för den VPN-tjänsteleverantör som du använder.

??? "NordVPN"

    1. Gå till **VPN** > **OpenVPN Client** i routerns webbadministrationspanel.

    2. Klicka på **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Ange tjänstens inloggningsuppgifter och klicka sedan på **Save and Continue**.

        Obs! Det är inte kontots e-postadress och lösenord, utan de tjänsteuppgifter som hämtas från NordVPN website -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. Välj VPN-platserna som du vill ansluta till i dialogrutan och klicka sedan på **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Välj VPN-servern som du vill ansluta till, klicka på ikonen med tre punkter och välj **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Andra VPN-tjänsteleverantörer (t.ex. Surfshark)"

    1. Gå till **VPN** > **OpenVPN Client** i routerns webbadministrationspanel.

    2. Klicka på **Add Manually**.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Ange ett namn. Du kan ange VPN-tjänsteleverantörens namn och sedan klicka på bockikonen.

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Kontrollera att du har laddat ned konfigurationsfilen från VPN-tjänsteleverantören och eventuella tjänsteuppgifter.
    5. Ladda upp konfigurationsfilen som du hämtade.

        Ange tjänstens inloggningsuppgifter om de krävs och klicka sedan på **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Klicka på ikonen med tre punkter bredvid VPN-serveradressen och välj **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Verifiera VPN-anslutningen {#3-verify-vpn-connection}

Öppna en webbläsare och sök efter din IP-adress och plats. Om de stämmer överens med VPN-serverns IP-adress och plats i stället för internetleverantörens har VPN-anslutningen upprättats.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
