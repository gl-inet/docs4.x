# So richten Sie einen OpenVPN-Client auf GL.iNet-Routern ein

In diesem Tutorial erfahren Sie, wie Sie einen OpenVPN-Client auf GL.iNet-Routern einrichten.

Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Bevor Sie beginnen, stellen Sie sicher, dass Sie ein aktives Abonnement bei einem VPN-Dienstanbieter haben, der die manuelle OpenVPN-Konfiguration unterstützt. Klicken Sie [hier](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, um die mit GL.iNet kompatiblen OpenVPN-Anbieter anzuzeigen.

Im Folgenden finden Sie die Schritte zum Einrichten eines OpenVPN-Clients über das Web-Admin-Panel des Routers.

## 1. Am Router anmelden

Öffnen Sie einen Webbrowser und rufen Sie das Web-Admin-Panel des Routers auf (Standard-IP: 192.168.8.1). Melden Sie sich mit Ihrem Admin-Passwort an.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. VPN-Client einrichten

Wählen Sie den Abschnitt aus, der zu dem von Ihnen verwendeten VPN-Dienstanbieter passt.

??? "NordVPN"

    1. Gehen Sie im Web-Admin-Panel des Routers zu **VPN** > **OpenVPN Client**.

    2. Klicken Sie auf **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Geben Sie Ihre Service-Anmeldedaten ein und klicken Sie dann auf **Save and Continue**.

        Hinweis: Dies ist **NICHT** die E-Mail-Adresse bzw. das Passwort Ihres Login-Kontos, sondern die Service-Anmeldedaten, die Sie auf der NordVPN-Website unter Nord Dashboard erhalten.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. Wählen Sie im Dialogfeld die VPN-Standorte aus, mit denen Sie sich verbinden möchten, und klicken Sie dann auf **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Wählen Sie den VPN-Server aus, mit dem Sie sich verbinden möchten, klicken Sie auf das Symbol mit den drei Punkten und anschließend auf **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Andere VPN-Dienstanbieter (z. B. Surfshark)"

    1. Gehen Sie im Web-Admin-Panel des Routers zu **VPN** > **OpenVPN Client**.

    2. Klicken Sie auf **Add Manually**.

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Legen Sie einen Namen fest. Sie können den Namen Ihres VPN-Dienstanbieters eingeben und dann auf das Häkchensymbol klicken.

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Stellen Sie sicher, dass Sie die von Ihrem VPN-Dienstanbieter bereitgestellte Konfigurationsdatei sowie gegebenenfalls die Service-Anmeldedaten heruntergeladen haben.
    5. Laden Sie die zuvor heruntergeladene Konfigurationsdatei hoch.

        Geben Sie bei Bedarf die Service-Anmeldedaten ein und klicken Sie dann auf **Apply**.

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Klicken Sie neben der Adresse des VPN-Servers auf das Symbol mit den drei Punkten und anschließend auf **Start**.

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. VPN-Verbindung überprüfen

Öffnen Sie einen Webbrowser und suchen Sie nach Ihrer IP-Adresse und Ihrem Standort. Wenn beide mit der IP des VPN-Servers (und nicht mit der IP Ihres Internetdienstanbieters) sowie dessen Standort übereinstimmen, wurde die VPN-Verbindung erfolgreich hergestellt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
