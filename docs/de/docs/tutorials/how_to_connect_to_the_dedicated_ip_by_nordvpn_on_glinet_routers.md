# So stellen Sie auf GL.iNet-Routern eine Verbindung zur dedizierten IP von NordVPN her

Dieser Artikel beschreibt die Schritte zum Einrichten einer dedizierten IP von NordVPN.

Als Beispiel verwenden wir hier den GL-AXT1800.

1. Melden Sie sich bei Ihrem Nord-Konto an und prüfen Sie die Informationen zur dedizierten IP. Wie in der folgenden Abbildung gezeigt, lautet die zugewiesene IP **193.32.211.142** und die Serverinformation ist **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Öffnen Sie diesen Link: [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) und suchen Sie die Konfigurationsdatei für **United Kingdom #1625**. Laden Sie je nach Bedarf die UDP- oder TCP-Konfigurationsdatei herunter.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Kehren Sie zur Seite Ihres Nord-Kontos zurück, wechseln Sie zu Manual setup und klicken Sie auf **Set up NordVPN Manually**, um die Zugangsdaten für den Dienst zu erhalten.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Melden Sie sich am webbasierten Admin Panel Ihres Routers an, gehen Sie zu **VPN** > **OpenVPN Client** und erstellen Sie eine neue Gruppe, um die in Schritt 2 heruntergeladene Konfigurationsdatei hochzuladen. Geben Sie anschließend die in Schritt 3 erhaltenen Zugangsdaten ein.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

5. Gehen Sie zum **VPN Dashboard**, wählen Sie die Konfigurationsdatei aus und klicken Sie auf **Apply**, um die Verbindung herzustellen.

    ![connect nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/connect_nordvpn_on_glinet_router.png){class="glboxshadow"}

6. Sobald die Verbindung hergestellt ist, können Sie hier Ihre öffentliche IP prüfen: [https://whatismyipaddress.com/](https://whatismyipaddress.com/) und bestätigen, dass sie mit der dedizierten IP von NordVPN übereinstimmt.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
