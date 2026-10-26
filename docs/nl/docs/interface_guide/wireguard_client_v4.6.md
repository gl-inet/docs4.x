# WireGuard-client instellen op GL.iNet-routers {#set-up-wireguard-client-on-glinet-routers}

De inhoud van deze pagina is gebaseerd op firmware v4.6 en ouder. Als je apparaat een andere firmwareversie gebruikt, kies je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.6 and earlier" markdown="1">

- [Firmware v4.7 en hoger](wireguard_client.md)

</div>

---

WireGuard® is een zeer eenvoudige, snelle en moderne VPN die geavanceerde cryptografie gebruikt. Het is ontworpen om sneller, eenvoudiger, compacter en gebruiksvriendelijker te zijn dan IPsec, zonder de bijbehorende complexiteit. Het biedt doorgaans aanzienlijk betere prestaties dan OpenVPN.

Als je al een WireGuard-dienst bij een provider hebt gekocht maar niet weet hoe je de configuratiebestanden verkrijgt, raadpleeg je [configuratiebestanden van WireGuard-serviceproviders verkrijgen](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) of neem je contact op met de ondersteuning van de provider.

Je kunt WireGuard Client instellen via het webbeheerpaneel of de [mobiele app](../faq/mobile_app.md).

- De mobiele app is geïntegreerd met verschillende WireGuard-serviceproviders, waaronder AzireVPN, Mullvad, OVPN, StrongVPN en PIA VPN.

- Het webbeheerpaneel ondersteunt minder WireGuard-serviceproviders, zoals AzireVPN en Mullvad, maar biedt overzichtelijkere en gedetailleerdere pagina's.

Hieronder staan de stappen voor de installatie via het webbeheerpaneel.

---

Meld je aan bij het webbeheerpaneel en ga naar **VPN** -> **WireGuard Client**.

Als je een abonnement op **AzireVPN** of **Mullvad** hebt, kun je je rechtstreeks met de bijbehorende aanmeldgegevens aanmelden. Klik anders op **Add Manually** om de WireGuard-profielen handmatig te uploaden.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## AzireVPN instellen {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is een privacygerichte VPN-dienst die veilige, moderne en robuuste tunnels zoals WireGuard biedt.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Voer **Username** en **Password** in en klik op **Save Credentials & Get Servers**. Voor elke server wordt een configuratiebestand gegenereerd.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Ga naar VPN Dashboard om de verbinding in te schakelen.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, zie je jouw IP-adres en het aantal verzonden en ontvangen bytes.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Servers bijwerken

    AzireVPN kan servers onderhouden of uitschakelen, waardoor de verbinding kan mislukken. Klik op **Update Servers** om de nieuwste beschikbare servers op te halen.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Aanmeldgegevens bewerken

    Klik op het tandwielpictogram om de aanmeldgegevens te bewerken.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

5. Verwijderen

    Klik op **Delete All** om alle configuratiebestanden in één keer te verwijderen.

    ![azirevpn delete all configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_delete_all_configuration_file.png){class="glboxshadow"}

## Mullvad instellen {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} is een VPN-dienst die je onlineactiviteiten, identiteit en locatie privé helpt te houden.

Firmware 4.x bevat een geïntegreerde Mullvad WireGuard-dienst.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Voer **Account** in en klik op **Save Credentials & Get Servers**.

    Een Mullvad-accountnummer bestaat uit 16 cijfers en ligt tussen "1000 0000 0000 0000" en "9999 9999 9999 9999".

    Er verschijnt een dialoogvenster waarin je een locatie selecteert.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Vervolgens worden de configuratiebestanden voor de server op de geselecteerde locatie gegenereerd.

    De **Public Key** is de openbare WireGuard-sleutel die naar de Mullvad-server wordt verzonden. Je kunt maximaal vijf sleutels tegelijk hebben en je WireGuard-sleutels beheren op [de pagina van Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Ga naar VPN Dashboard om de verbinding in te schakelen.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Zodra de verbinding tot stand is gebracht, zie je jouw IP-adres en het aantal verzonden en ontvangen bytes.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Servers bijwerken

    Mullvad kan servers onderhouden of uitschakelen, waardoor de verbinding kan mislukken. Klik op **Update Servers** om de nieuwste beschikbare servers op te halen.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Aanmeldgegevens bewerken

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Accountgegevens verwijderen

    Als je op **Delete** klikt, worden de accountgegevens, privésleutel, openbare sleutel en configuratiebestanden **op de router** verwijderd.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Verwijderen

    Hiermee verwijder je alle configuratiebestanden in één keer. Je krijgt ook de vraag of de privé- en openbare sleutel moeten worden verwijderd.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## WireGuard Client instellen {#set-up-wireguard-client}

Vanaf firmware 4.0 kun je WireGuard-profielen in groepen beheren.

1. Klik op **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Er wordt een groep gemaakt.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Geef de groep een duidelijke naam, bijvoorbeeld azirevpn. Je kunt vervolgens configuratiebestanden uploaden of handmatig een configuratie toevoegen.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Configuratiebestanden uploaden**

        Upload je WireGuard-configuratiebestand en klik op **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. Met **Manually Add Configuration** kun je de WireGuard-configuratie plakken of elk veld afzonderlijk invullen.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Geef de configuratie een duidelijke naam, plak de configuratie en klik op **Apply** om door te gaan.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Je kunt de configuratie ook toevoegen door elk veld in te vullen. Klik hiervoor op **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Klik op het pictogram met drie puntjes om het profiel te starten, te bewerken of te verwijderen.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Controleer de verbindingsstatus op de pagina [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® is een geregistreerd handelsmerk van Jason A. Donenfeld.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
