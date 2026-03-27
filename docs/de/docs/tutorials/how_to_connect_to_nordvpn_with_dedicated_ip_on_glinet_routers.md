# So verbinden Sie NordVPN mit einer dedizierten IP auf GL.iNet-Routern

Dieser Artikel beschreibt die Schritte zum Einrichten einer NordVPN-Verbindung mit dedizierter IP auf GL.iNet-Routern.

Als Beispiel verwenden wir den GL-AXT1800.

1. Melden Sie sich in Ihrem Nord-Konto an und prüfen Sie die Details der dedizierten IP. Wie unten gezeigt, lautet die zugewiesene IP **193.32.211.142** und der Server ist **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Gehen Sie zu [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) und suchen Sie die Konfigurationsdatei für **United Kingdom #1625**. Laden Sie die UDP- oder TCP-Konfigurationsdatei herunter.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Kehren Sie zur Seite Ihres Nord-Kontos zurück, gehen Sie zu **Manual Setup** und klicken Sie auf **Set up NordVPN Manually**, um Ihre Service-Zugangsdaten zu erhalten.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Melden Sie sich am webbasierten Admin Panel Ihres Routers an und gehen Sie zu **VPN** > **OpenVPN Client**. Erstellen Sie eine neue Gruppe, um die in Schritt 2 heruntergeladene Konfigurationsdatei hochzuladen. Geben Sie anschließend die in Schritt 3 erhaltenen Service-Zugangsdaten ein.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    Es wurde 1 gültige Konfigurationsdatei erkannt. Bitte geben Sie Ihren Benutzernamen und Ihr Passwort ein. Wenn diese Konfigurationen unterschiedliche Passwörter verwenden, müssen Sie das jeweilige Passwort für jede Konfigurationsdatei eingeben.

5. Klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung herzustellen. Alternativ können Sie auch zum **VPN Dashboard** gehen, die Konfigurationsdatei auswählen und auf **Apply** klicken, um die Verbindung aufzubauen.

6. Prüfen Sie nach dem Verbindungsaufbau Ihre öffentliche IP [hier](https://whatismyipaddress.com/) und bestätigen Sie, dass sie mit Ihrer dedizierten IP von NordVPN übereinstimmt.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.