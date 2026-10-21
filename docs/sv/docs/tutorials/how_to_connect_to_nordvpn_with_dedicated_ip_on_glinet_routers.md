# Ansluta till NordVPN med en dedikerad IP-adress på GL.iNet-routrar {#how-to-connect-to-nordvpn-with-a-dedicated-ip-on-glinet-routers}

Artikeln beskriver hur du konfigurerar en NordVPN-anslutning med en dedikerad IP-adress på GL.iNet-routrar.

Vi använder GL-AXT1800 som exempel.

1. Logga in på ditt Nord Account och kontrollera uppgifterna för den dedikerade IP-adressen. I exemplet nedan är den tilldelade IP-adressen **193.32.211.142** och servern **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Gå till [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/){target="_blank"} och leta reda på konfigurationsfilen för **United Kingdom #1625**. Ladda ned UDP- eller TCP-konfigurationsfilen.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Gå tillbaka till Nord Account-sidan, öppna **Manual Setup** och klicka på **Set up NordVPN Manually** för att hämta dina **service credentials**.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Logga in på routerns webbadministrationspanel och gå till **VPN** > **OpenVPN Client**. Skapa en ny grupp och ladda upp konfigurationsfilen som du hämtade i steg 2. Ange sedan tjänstens inloggningsuppgifter från steg 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    En giltig konfigurationsfil har identifierats enligt bilden ovan. Ange inloggningsuppgifterna för NordVPN-tjänsten.

5. Klicka på ikonen med tre punkter till höger för att ansluta. Du kan även gå till **VPN Dashboard**, välja konfigurationsfilen och klicka på **Apply** för att upprätta en anslutning.

6. När anslutningen har upprättats kontrollerar du din offentliga IP-adress [här](https://whatismyipaddress.com/){target="_blank"} och bekräftar att den stämmer överens med den dedikerade IP-adressen från NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
