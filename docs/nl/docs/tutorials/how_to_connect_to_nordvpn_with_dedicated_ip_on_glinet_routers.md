# Verbinding maken met NordVPN Dedicated IP op GL.iNet-routers {#how-to-connect-to-nordvpn-with-a-dedicated-ip-on-glinet-routers}

Dit artikel beschrijft hoe je NordVPN met een vast IP-adres op GL.iNet-routers instelt.

We use the GL-AXT1800 as an example.

1. Meld je aan bij je Nord Account en controleer de gegevens van het vaste IP-adres. In dit voorbeeld is het toegewezen IP **193.32.211.142** en de server **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Ga naar [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/){target="_blank"} en zoek het configuratiebestand voor **United Kingdom #1625**. Download het UDP- of TCP-configuratiebestand.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Ga terug naar Nord Account, open **Manual Setup** en klik op **Set up NordVPN Manually** om je **service credentials** op te halen.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Meld je aan bij het webbeheerpaneel en ga naar **VPN** > **OpenVPN Client**. Maak een groep, upload het bestand uit stap 2 en voer de servicegegevens uit stap 3 in.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    Er is een geldig configuratiebestand gedetecteerd. Voer je NordVPN-servicegegevens in.

5. Klik rechts op het pictogram met drie puntjes om verbinding te maken. Je kunt ook op **VPN Dashboard** het configuratiebestand selecteren en op **Apply** klikken.

6. Controleer na verbinding [hier](https://whatismyipaddress.com/){target="_blank"} je openbare IP-adres en vergelijk dit met je vaste NordVPN-IP.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
