# WireGuard-Client auf GL.iNet-Routern einrichten (Firmware v4.6 und früher)

**Hinweis**: Diese Anleitung gilt für Firmware v4.6 und früher. Für neuere Versionen siehe [hier](wireguard_client.md).

---

WireGuard® ist ein äußerst einfaches und dennoch schnelles, modernes VPN, das modernste Kryptografie verwendet. Es wurde entwickelt, um schneller, einfacher, schlanker und nützlicher als IPsec zu sein, ohne den üblichen großen Aufwand zu verursachen. Zudem bietet es eine deutlich höhere Leistung als OpenVPN.

Wenn Sie bereits einen WireGuard-Dienst bei einem Anbieter gebucht haben, aber nicht wissen, wie Sie die Konfigurationsdateien erhalten, lesen Sie bitte [Konfigurationsdateien von WireGuard-Dienstanbietern abrufen](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oder wenden Sie sich an den Support des Anbieters.

Sie können den WireGuard-Client über das web Admin Panel oder die [mobile app](../faq/mobile_app.md) einrichten. 

- Die mobile App ist in mehrere WireGuard-Dienstanbieter integriert, darunter AzireVPN, Mullvad, OVPN, StrongVPN und PIA VPN.

- Das web Admin Panel unterstützt weniger WireGuard-Dienstanbieter (z. B. AzireVPN und Mullvad), bietet dafür aber übersichtlichere und detailliertere Seiten.

Im Folgenden finden Sie die Schritte für die Einrichtung über das web Admin Panel.

---

Melden Sie sich im web Admin Panel an und wechseln Sie zu **VPN** -> **WireGuard Client**.

Wenn Sie ein Abonnement bei **AzireVPN** oder **Mullvad** haben, können Sie sich direkt mit Ihren Zugangsdaten anmelden. Alternativ klicken Sie auf **Add Manually**, um die WireGuard-Profile manuell hochzuladen.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## AzireVPN einrichten

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} ist ein datenschutzorientierter VPN-Dienst, der sichere, moderne und robuste Tunnel wie WireGuard bereitstellt.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save Credentials & Get Servers**. Dadurch werden Konfigurationsdateien für alle Server erstellt.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Wechseln Sie zum VPN Dashboard, um die Verbindung zu aktivieren.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung werden Ihre Benutzer-IP-Adresse und die Anzahl der gesendeten/empfangenen Bytes angezeigt.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Server aktualisieren

    AzireVPN kann Server warten oder abschalten, wodurch Verbindungen fehlschlagen können. Mit **Update Servers** rufen Sie die aktuell verfügbaren Server ab.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Zugangsdaten bearbeiten

    Klicken Sie auf das Zahnradsymbol, um die Zugangsdaten zu bearbeiten.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Mullvad einrichten

[Mullvad](https://mullvad.net/){target="_blank"} ist ein VPN-Dienst, der Ihre Online-Aktivitäten, Ihre Identität und Ihren Standort privat hält.

Die Firmware 4.x hat den Mullvad-WireGuard-Dienst integriert.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Geben Sie **Account** ein und klicken Sie dann auf **Save Credentials & Get Servers**.

    Die Mullvad-Kontonummer ist eine 16-stellige Dezimalzahl im Bereich von "1000 0000 0000 0000" bis "9999 9999 9999 9999".

    Daraufhin wird ein Dialog zur Auswahl eines Standorts geöffnet.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Anschließend werden die Konfigurationsdateien des Servers am ausgewählten Standort erstellt.
    
    Der **Public Key** ist der öffentliche WireGuard-Schlüssel, der an den Mullvad-Server gesendet wird. Sie können bis zu fünf Schlüssel gleichzeitig haben. Verwalten können Sie die WireGuard-Schlüssel auf [der Seite von Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Wechseln Sie zum VPN Dashboard, um die Verbindung zu aktivieren.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Nach erfolgreicher Verbindung werden Ihre Benutzer-IP-Adresse und die Anzahl der gesendeten/empfangenen Bytes angezeigt.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Server aktualisieren

    Mullvad kann Server warten oder abschalten, wodurch Verbindungen fehlschlagen können. Mit **Update Servers** rufen Sie die aktuell verfügbaren Server ab.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Zugangsdaten bearbeiten

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Kontoinformationen löschen

    Wenn Sie auf **Delete** klicken, werden die Kontozugangsdaten, der private Schlüssel, der öffentliche Schlüssel und die Konfigurationsdateien **auf dem Router** gelöscht.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Löschen

    Damit können Sie alle Konfigurationsdateien mit einem Klick löschen. Zusätzlich erscheint eine Abfrage, ob auch der private und der öffentliche Schlüssel gelöscht werden sollen.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## WireGuard-Client einrichten

Seit Firmware 4.0 gibt es eine Gruppierung zum Verwalten von WireGuard-Profilen.

1. Klicken Sie auf **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Dadurch wird eine Gruppe erstellt.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Geben Sie der Gruppe einen aussagekräftigen Namen, z. B. azirevpn. Anschließend können Sie Konfigurationsdateien hochladen oder die Konfiguration manuell hinzufügen.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Konfigurationsdateien hochladen**

        Laden Sie Ihre WireGuard-Konfigurationsdatei hoch und klicken Sie auf **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration** – diese Option ist dafür gedacht, die WireGuard-Konfiguration einzufügen oder die einzelnen Einträge manuell auszufüllen.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Geben Sie einen aussagekräftigen Namen ein, fügen Sie die Konfiguration ein und klicken Sie auf **Apply**, um fortzufahren.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Oder Sie fügen die Konfiguration hinzu, indem Sie jeden Eintrag einzeln ausfüllen. Klicken Sie dazu auf **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Klicken Sie auf das Symbol mit den drei Punkten, um das Profil zu starten, zu bearbeiten oder zu löschen.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Prüfen Sie den Verbindungsstatus auf der Seite [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® ist eine eingetragene Marke von Jason A.Donenfeld.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
