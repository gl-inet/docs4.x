# VPN Client Profile {#vpn-client-profile}

**Opmerking**: deze pagina is geïntroduceerd in firmware v4.9.

---

Ga links in het webbeheerpaneel naar **VPN** -> **VPN Client Profile**.

Sinds firmware v4.9 zijn [OpenVPN Client](openvpn_client.md) en [WireGuard Client](wireguard_client.md) samengevoegd op de pagina **VPN Client Profile**. De indeling is aangepast, maar de kernfuncties zijn gelijk gebleven. Raadpleeg zo nodig de afzonderlijke handleidingen.

Op deze pagina kun je je aanmelden bij geïntegreerde VPN-diensten en profielen downloaden, of configuratiebestanden van andere providers handmatig uploaden. Rechtsboven kun je zo nodig van VPN-protocol wisselen.

## WireGuard {#wireguard}

WireGuard® is een lichte, krachtige moderne VPN met geavanceerde cryptografie. Het biedt meer snelheid, eenvoud en gebruiksgemak dan IPsec en presteert aanzienlijk beter dan OpenVPN.

GL.iNet-routers bieden ingebouwde WireGuard-ondersteuning voor de volgende VPN-providers. Voer bij een actief abonnement je aanmeldingsgegevens op **VPN Client Profile** in om de installatie te voltooien.

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

Download bij een andere WireGuard-provider een configuratiebestand van de website en klik op **Add Manually** om het naar de router te uploaden.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

Raadpleeg [deze handleiding](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) of de ondersteuning van de provider als je niet weet hoe je configuratiebestanden downloadt.

---

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} wordt als voorbeeld gebruikt.

1. Klik op de pagina **VPN Client Profile** op **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Voer **Username** en **Password** in en klik op **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    Het systeem genereert configuratiebestanden voor alle beschikbare servers.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Volg de onderstaande instructies die bij je behoeften passen.

    !!! note "Situatie 1. Alle verbonden clients gebruiken VPN voor internettoegang"

        1. Selecteer de gewenste server en klik rechts op het pictogram met drie stippen om verbinding te maken.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Nadat de verbinding tot stand is gebracht, verschijnt een groene stip naast het configuratiebestand.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            De VPN-verbinding is actief en alle clients op deze router gebruiken VPN voor beveiligde internettoegang.

        3. Optioneel: ga naar **VPN Dashboard** en schakel **Kill Switch** in als het systeem bij onverwachte VPN-uitval automatisch alle internettoegang voor het lokale netwerk moet blokkeren om je IP-adres en gegevens te beschermen.

            * Raadpleeg [deze instructies](vpn_dashboard.md#tunnel-options) om Kill Switch per VPN-tunnel in te stellen.

            * Raadpleeg [deze instructies](vpn_dashboard.md#all-other-traffic) om Enhanced Kill Switch voor de globale VPN-verbinding in te stellen.

    !!! note "Situatie 2. Aangepast VPN-beleid configureren"

        1. Klik onderaan op **Go to Dashboard**.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. **VPN Dashboard** wordt geopend om VPN-beleid te configureren. Klik [hier](vpn_dashboard.md#add-vpn-tunnel) voor meer informatie.

## OpenVPN {#openvpn}

OpenVPN is een opensource-VPN-protocol voor beveiligde site-to-site- of point-to-pointverbindingen.

GL.iNet-routers bieden ingebouwde OpenVPN-ondersteuning voor [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Voer bij een actief abonnement je aanmeldingsgegevens op **VPN Client Profile** in.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Download bij een andere OpenVPN-provider een configuratiebestand van de website en klik op **Add Manually** om het naar de router te uploaden.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

Raadpleeg [deze instructies](openvpn_client.md#get-configuration-files-from-openvpn-service-providers) of de ondersteuning van de provider als je niet weet hoe je configuratiebestanden downloadt.

---

Gerelateerde artikelen

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [WireGuard Client instellen op GL.iNet-routers](wireguard_client.md)
- [OpenVPN Client instellen op GL.iNet-routers](openvpn_client.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
