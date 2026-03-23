# Wie reserviert man eine feste IP für einen OpenVPN-Client in einer selbst aufgebauten OpenVPN-Verbindung?

Dieses Tutorial zeigt Ihnen, wie Sie für Ihren OpenVPN-Client, der sich mit Ihrem Server verbindet, eine feste IP reservieren. Richten Sie zunächst einen GL.iNet-Router als OpenVPN-Server ein, bevor Sie die folgenden Schritte ausführen.

1. Melden Sie sich am webbasierten Admin Panel Ihres OpenVPN-Servers an und navigieren Sie in der linken Seitenleiste zu **VPN** -> **OpenVPN Server**.

    Notieren Sie sich auf der Registerkarte **Configuration** das **IPv4-Subnetz** (z. B. 10.8.0.0/24 wie im folgenden Bild) und stellen Sie den Authentication Mode auf **Username and Password Only** um.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Wechseln Sie zur Registerkarte **Users** und erstellen Sie einen Benutzernamen sowie ein Passwort, wie unten gezeigt.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Melden Sie sich per SSH am Router an und führen Sie den folgenden Befehl aus, um die Konfigurationsskriptdatei des OpenVPN-Servers zu öffnen:

    `vi /lib/netifd/proto/openserver.sh`

    Prüfen Sie in der geöffneten Datei, ob die Zeile "*client-config-dir /etc/openvpn/ccd*" im Skript vorhanden ist.

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Falls nicht, fügen Sie sie manuell hinzu, speichern Sie die Datei und schließen Sie sie.

4. Wechseln Sie nach `/etc/openvpn/` und erstellen Sie einen Ordner namens `ccd` mit `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Erstellen Sie eine Datei mit dem Namen `GLsupport`, tragen Sie `ifconfig-push 10.8.0.10 255.255.255.0` ein und speichern bzw. schließen Sie die Datei.

    Prüfen Sie den Inhalt mit `cat GLsupport`.

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Wenn Sie `GLsupport` verwenden, um sich mit Ihrem OpenVPN-Server zu verbinden, wird diesem Benutzer `GLsupport` die feste IP `10.8.0.10` zugewiesen.

    - `255.255.255.0` ist die Subnetzmaske. Sie können sie durch die Subnetzmaske Ihres OpenVPN-Servers ersetzen.

    **Hinweis**: Wenn Sie IP-Adressen für mehrere OpenVPN-Clients fest zuweisen möchten, erstellen Sie bitte in Schritt 2 mehrere Benutzernamen und Passwörter. Wiederholen Sie anschließend Schritt 5 und legen Sie im CCD-Ordner Dateien in der Reihenfolge der Benutzer an, z. B. `user_1`, `user_2`, `user_3`, jeweils mit dem Befehl `ifconfig-push` und der dazugehörigen festen IP-Adresse sowie Subnetzmaske.

    Zum Beispiel: `ifconfig-push 10.8.0.20 225.225.225.0`, `ifconfig-push 10.8.0.30 225.225.225.0`, `ifconfig-push 10.8.0.40 225.225.225.0`

6. Testen Sie abschließend mit Ihrem OVPN-Client und prüfen Sie, ob die virtuelle Client-IP (IPv4) die reservierte Adresse ist.

    Wenn Ihr OpenVPN-Client zum Beispiel ein GL.iNet-Router ist, können Sie sich am webbasierten Admin Panel des OpenVPN-Client-Routers anmelden und zum VPN Dashboard navigieren, um die virtuelle Client-IP (IPv4) zu prüfen.

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard in Firmware v4.7 und früher)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard in Firmware v4.8)</small>

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
