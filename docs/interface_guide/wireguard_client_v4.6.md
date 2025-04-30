# How to Set Up WireGuard Client on GL.iNet Router (Firmware v4.6 and earlier)

!!! note

    This guide is based on firmware v4.6 and earlier. If you are using an latest firmware version, please visit [here](wireguard_client.md).

WireGuard® is an extremely simple yet fast and modern VPN that utilizes **state-of-the-art cryptography**. It aims to be [faster](https://www.wireguard.com/performance/){target="_blank"}, simpler, leaner, and more useful than IPSec, while avoiding the massive headache. It intends to be considerably more performant than OpenVPN.

If you have already bought WireGuard service from a provider, but you don't know how to get the configuration files, please refer to [get configuration files from WireGuard service providers](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) or ask its support.

You can set up WireGuard Client via web Admin Panel or [mobile app](../faq/mobile_app.md). For the mobile app, it has already integrated some WireGuard Service Providers, they are AzireVPN, Mullvad VPN, OVPN, StrongVPN, PIA VPN.

For set up via web Admin Panel, please follow the guide below.

You can log in by clicking the **AzireVPN** or **Mullvad** button if you have a their membership, or by clicking **Add Manually** to upload the WireGuard profiles.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Set Up AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} is privacy-minded VPN service providing secure, modern and robust tunnels such as WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Input **Username** and **Password**, then click **Save Credentials & Get Servers**. It will generate configuration files for each servers.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Update servers

    AzireVPN may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Edit credential

    Click the cog icon to edit the credential.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Set Up Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} is a VPN service that helps keep your online activity, identity, and location private.

Firmware 4.x has integrated Mullvad WireGuard service.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Input **Account**, then click **Save Credentials & Get Servers**.

    Mullvad account number is a 16-digit decimal in the "1000 0000 0000 0000" to "9999 9999 9999 9999" range.

    It will pop up a dialog to select a location.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Then it will generate the configuration files of the selected location server.
    
    The **Public Key** is the WireGuard public key to send to Mullvad server, you can have up to five keys at the same time, you can manage WireGuard keys on [Mullvad's page](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Go to VPN Dashboard to enable the connection.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Once connected, you should see your user IP address and the number of Bytes send/received.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Update servers

    Mullvad may maintain or shutdown some servers, it will make the connection failed, you can **Update Servers** to get the latest available servers.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Edit credential

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Delete account information

    If you click **Delete**, it will delete the account credential, private key, public key and configuration files **in the router**.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Delete 

    Allow deleting all configuration files with one click and provide a prompt to also delete private key and public key.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Set up WireGuard Client

As of firmware 4.0, it brings grouping to manage WireGuard profiles.

1. Click **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. It will create a group.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Give the group a descriptive name, e.g. azirevpn. Then you can choose to upload configuration files or manually add configuration.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        Upload your WireGuard configuration file, click **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration**, it is for if you want to paste the WireGuard configuration or fill in each item.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Give a descriptive name and paste the configuration, click **Apply** to continue.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Or you can add configuration by fill in each item, click **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Click the three dots icon to start / edit /delete the profile.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Check the connection status by go to [VPN Dashboard](vpn_dashboard_v4.7.md) page.

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® is a registered trademark of Jason A.Donenfeld.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.