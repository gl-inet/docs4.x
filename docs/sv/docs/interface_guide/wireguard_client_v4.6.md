# Set Up WireGuard Client on GL.iNet Routers {#set-up-wireguard-client-on-glinet-routers}

Innehållet bygger på firmware v4.6 och tidigare. Om enheten kör en annan version använder du väljaren nedan.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.6 and earlier" markdown="1">

- [Firmware v4.7 and above](wireguard_client.md)

</div>

---

WireGuard® är ett enkelt, snabbt och modernt VPN med avancerad kryptografi och högre prestanda än OpenVPN.

Om du behöver hjälp med konfigurationsfiler, se [hämta filer från WireGuard-leverantörer](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) eller kontakta supporten.

Konfigurera WireGuard Client via webbadministrationspanelen eller [mobilappen](../faq/mobile_app.md).

- Mobilappen är integrerad med AzireVPN, Mullvad, OVPN, StrongVPN och PIA VPN.

- Webbadministrationspanelen stöder färre leverantörer men har mer detaljerade sidor.

Följ stegen nedan för webbadministrationspanelen.

---

Logga in och öppna **VPN** -> **WireGuard Client**.

Med **AzireVPN** eller **Mullvad** kan du logga in direkt. Annars klickar du på **Add Manually** och laddar upp profiler.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Set Up AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Ange **Username** och **Password** och klicka på **Save Credentials & Get Servers**.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Efter anslutning visas användarens IP-adress och skickade/mottagna byte.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Update servers

    Om AzireVPN underhåller eller stänger servrar kan anslutningen misslyckas. Klicka på **Update Servers**.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Edit credential

    Klicka på kugghjulet för att ändra inloggningsuppgifterna.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

5. Delete

    Klicka på **Delete All** för att radera alla konfigurationsfiler.

    ![azirevpn delete all configuration files](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_delete_all_configuration_file.png){class="glboxshadow"}

## Set Up Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} är en VPN-tjänst som skyddar aktivitet, identitet och plats.

Firmware 4.x has integrated Mullvad WireGuard service.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Input **Account**, then click **Save Credentials & Get Servers**.

    Mullvad account number is a 16-digit decimal in the "1000 0000 0000 0000" to "9999 9999 9999 9999" range.

    It will pop up a dialog to select a location.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Konfigurationsfiler skapas för vald serverplats.

    **Public Key** skickas till Mullvad-servern. Upp till fem nycklar kan hanteras på [Mullvads sida](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Efter anslutning visas användarens IP-adress och skickade/mottagna byte.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Update servers

    Om Mullvad underhåller eller stänger servrar kan anslutningen misslyckas. Klicka på **Update Servers**.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Edit credential

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Delete account information

    **Delete** raderar inloggningsuppgifter, privata och offentliga nycklar samt konfigurationsfiler **i routern**.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Delete

    Radera alla konfigurationsfiler med ett klick och välj om nycklar också ska raderas.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Set up WireGuard Client {#set-up-wireguard-client}

As of firmware 4.0, it brings grouping to manage WireGuard profiles.

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. It will create a group.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Ge gruppen ett namn, till exempel azirevpn, och ladda upp eller lägg till konfiguration manuellt.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        Ladda upp WireGuard-konfigurationsfilen och klicka på **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration** används för att klistra in konfigurationen eller fylla i varje post.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Ange ett namn, klistra in konfigurationen och klicka på **Apply**.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Klicka på **Item Mode** för att fylla i varje post.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Klicka på ikonen med tre punkter för att starta, ändra eller radera profilen.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Check the connection status by go to [VPN Dashboard](vpn_dashboard_v4.7.md) page.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
