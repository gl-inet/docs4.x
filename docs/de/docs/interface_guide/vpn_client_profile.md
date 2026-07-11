# VPN-Client-Profil

> Diese Anleitung gilt für Firmware v4.9 und höher.

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **VPN** -> **VPN Client Profile**.

Seit Firmware v4.9 wurden [OpenVPN Client](openvpn_client.md) und [WireGuard Client](wireguard_client.md) auf einer gemeinsamen Seite **VPN Client Profile** zusammengeführt, um die Verwaltung zu vereinfachen. Das Layout wurde leicht angepasst, die Kernfunktionen bleiben jedoch unverändert. Bei Bedarf können Sie weiterhin die separaten Anleitungen verwenden.

Auf dieser Seite können Sie sich bei einigen integrierten VPN-Diensten anmelden und deren Profile einfach für die VPN-Verbindung herunterladen oder Ihre von der Website eines anderen VPN-Anbieters exportierten Konfigurationsdateien manuell hochladen. Bei Bedarf können Sie oben rechts zwischen den VPN-Protokollen wechseln.

## WireGuard

WireGuard® ist ein leichtgewichtiges, modernes Hochleistungs-VPN, das auf modernster Kryptografie basiert. Es bietet gegenüber IPsec deutlich bessere Geschwindigkeit, Einfachheit und Praxistauglichkeit und übertrifft OpenVPN spürbar in der Leistung.

GL.iNet-Router bieten integrierte WireGuard-Unterstützung für die folgenden VPN-Anbieter. Wenn Sie ein aktives Abonnement haben, geben Sie einfach Ihre Zugangsdaten auf der Seite **VPN Client Profile** ein, um die Einrichtung schnell abzuschließen.

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

Wenn Sie einen anderen WireGuard-Dienstanbieter verwenden, laden Sie eine Konfigurationsdatei von dessen Website herunter und klicken Sie anschließend auf **Add Manually**, um die Datei für die VPN-Verbindung auf Ihren Router hochzuladen. Falls Sie nicht wissen, wie Sie die Konfigurationsdateien herunterladen, lesen Sie bitte [hier](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) oder wenden Sie sich an den Support des Anbieters.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Nehmen Sie [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} als Beispiel.

1. Klicken Sie auf **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    Das System erstellt Konfigurationsdateien für alle verfügbaren Server.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Folgen Sie der entsprechenden Anleitung unten, je nach Ihrem tatsächlichen Bedarf.

    !!! note "Fall 1. Wenn Sie möchten, dass alle verbundenen Clients das VPN für den Internetzugang verwenden, führen Sie diese Schritte aus."

        1. Wählen Sie Ihren bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um eine Verbindung zu starten.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Nach erfolgreicher Verbindung erscheint neben der Konfigurationsdatei ein grüner Punkt.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            Jetzt ist die VPN-Verbindung aktiv, und alle mit diesem Router verbundenen Clients sollten das VPN für einen sicheren Internetzugang nutzen.

        3. (Optional) Wenn Sie möchten, dass das System automatisch den gesamten Internetzugang für Ihr lokales Netzwerk unterbricht, falls die VPN-Verbindung unerwartet abbricht, um zu verhindern, dass Ihre echte IP-Adresse und Ihre Online-Daten offengelegt werden, und um fortlaufende Privatsphäre und Sicherheit zu gewährleisten, gehen Sie zum **VPN Dashboard**, um den **Kill Switch** zu aktivieren.

            * Um den Kill Switch für jeden einzelnen VPN-Tunnel einzurichten, lesen Sie [hier](vpn_dashboard.md#tunnel-options).

            * Um den Kill Switch für die globale VPN-Verbindung (d. h. Enhanced Kill Switch) einzurichten, lesen Sie [hier](vpn_dashboard.md#all-other-traffic).

    !!! note "Fall 2. Wenn Sie stattdessen Ihre VPN-Richtlinie individuell anpassen möchten, führen Sie diese Schritte aus."

        1. Klicken Sie unten auf **Go to Dashboard**.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Sie werden dann zum **VPN Dashboard** weitergeleitet, um die VPN-Richtlinie zu konfigurieren. Details finden Sie [hier](vpn_dashboard.md#set-up-vpn-policy).

## OpenVPN

OpenVPN ist ein Open-Source-VPN-Protokoll, das Techniken virtueller privater Netzwerke verwendet, um sichere Site-to-Site- oder Point-to-Point-Verbindungen herzustellen.

GL.iNet-Router bieten integrierte OpenVPN-Unterstützung für [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Wenn Sie ein aktives Abonnement haben, geben Sie einfach Ihre Zugangsdaten auf der Seite **VPN Client Profile** ein, um die Einrichtung schnell abzuschließen.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Wenn Sie einen anderen OpenVPN-Dienstanbieter verwenden, laden Sie eine Konfigurationsdatei von dessen Website herunter und klicken Sie anschließend auf **Add Manually**, um die Datei für die VPN-Verbindung auf Ihren Router hochzuladen. Falls Sie nicht wissen, wie Sie die Konfigurationsdateien herunterladen, lesen Sie bitte [hier](openvpn_client.md#get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers) oder wenden Sie sich an den Support des Anbieters.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Verwandte Artikel

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [WireGuard-Client auf GL.iNet-Routern einrichten](wireguard_client.md)
- [OpenVPN-Client auf GL.iNet-Routern einrichten](openvpn_client.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
