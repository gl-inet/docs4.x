# So verbinden Sie Surfshark mit einer dedizierten IP auf GL.iNet-Routern

Dieser Artikel beschreibt die Schritte zum Einrichten einer Surfshark-Verbindung mit dedizierter IP auf GL.iNet-Routern.

Als Beispiel verwenden wir den GL-AXT1800.

1. Melden Sie sich bei Ihrem Surfshark-Konto an und wählen Sie anschließend **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. Klicken Sie im Abschnitt Dedicated IP auf **Settings**.

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. Wählen Sie ein Protokoll (WireGuard oder OpenVPN) und laden Sie die Konfigurationsdateien für die manuelle Verbindung herunter.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}

    Bei der WireGuard-Konfiguration zeigt die Download-Seite die Server-IP und den öffentlichen Serverschlüssel an, wie unten dargestellt.

    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

    Bei der OpenVPN-Konfiguration zeigt die Download-Seite die Server-IP und die Zugangsdaten (Benutzername und Passwort) an, wie unten dargestellt. Kopieren Sie die Zugangsdaten zur späteren Verwendung.

    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

4. Verwenden Sie die folgenden Links, um die Konfigurationsdateien auf Ihren GL.iNet-Router hochzuladen. Geben Sie die Zugangsdaten ein, falls sie abgefragt werden.

    - [WireGuard-Konfiguration hochladen](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [OpenVPN-Konfiguration hochladen](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.