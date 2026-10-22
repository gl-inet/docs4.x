# VPN Client Profile {#vpn-client-profile}

**Note**: This page was introduced in firmware v4.9.

---

Öppna **VPN** -> **VPN Client Profile**.

Från firmware v4.9 är [OpenVPN Client](openvpn_client.md) och [WireGuard Client](wireguard_client.md) samlade på **VPN Client Profile**. Kärnfunktionerna är oförändrade.

På sidan kan du logga in på integrerade VPN-tjänster och hämta profiler eller ladda upp konfigurationsfiler manuellt. Byt protokoll uppe till höger.

## WireGuard {#wireguard}

WireGuard® är ett resurssnålt och högpresterande modernt VPN med avancerad kryptografi och högre hastighet än OpenVPN.

GL.iNet-routrar har inbyggt WireGuard-stöd för följande leverantörer. Ange tjänstens inloggningsuppgifter på **VPN Client Profile**.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

För andra WireGuard-leverantörer hämtar du en konfigurationsfil och klickar på **Add Manually** för att ladda upp den.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

Se [den här guiden](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) eller kontakta leverantörens support om du behöver hjälp.

---

Take [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} as an example.

1. Klicka på **AzireVPN** på sidan **VPN Client Profile**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Ange **Username** och **Password** och klicka på **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    The system will generate configuration files for all available servers.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Följ anvisningarna nedan efter behov.

    !!! note "Case 1. If you want all connected clients to use VPN for internet access, follow these steps."

        1. Välj server och klicka på ikonen med tre punkter till höger för att ansluta.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Once connected, a green dot will appear next to the configuration file.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            VPN-anslutningen är aktiverad och alla anslutna klienter använder VPN.

        3. (Valfritt) Aktivera **Kill Switch** på **VPN Dashboard** för att blockera internet om VPN misslyckas och förhindra IP- och dataläckor.

            * To set up Kill Switch for each individual VPN tunnel, refer to [here](vpn_dashboard.md#tunnel-options).

            * To set up Kill Switch for the global VPN connection (i.e., Enhanced Kill Switch), refer to [here](vpn_dashboard.md#all-other-traffic).

    !!! note "Case 2. If you prefer to customize VPN policy instead, follow these steps."

        1. Klicka på **Go to Dashboard** längst ned.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. **VPN Dashboard** öppnas för VPN-principer. Klicka [här](vpn_dashboard.md#add-vpn-tunnel) för mer information.

## OpenVPN {#openvpn}

OpenVPN is an open‑source VPN protocol that uses virtual private network techniques to establish secure site‑to‑site or point‑to‑point connections.

GL.iNet-routrar har inbyggt OpenVPN-stöd för [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Ange tjänstens inloggningsuppgifter på **VPN Client Profile**.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

För andra OpenVPN-leverantörer hämtar du en konfigurationsfil och klickar på **Add Manually** för att ladda upp den.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

Se [den här guiden](openvpn_client.md#get-configuration-files-from-openvpn-service-providers) eller kontakta leverantörens support.

---

Related Articles

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [Set Up WireGuard Client on GL.iNet Routers](wireguard_client.md)
- [Set Up OpenVPN Client on GL.iNet Routers](openvpn_client.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
