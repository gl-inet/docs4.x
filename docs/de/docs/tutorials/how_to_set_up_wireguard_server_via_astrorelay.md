# So richten Sie einen WireGuard-Server über AstroRelay ein

Diese Anleitung beschreibt die Schritte zum Einrichten eines WireGuard-Servers über AstroRelay auf einem GL.iNet-Router. Sie eignet sich besonders für Benutzer, die aus der Ferne auf lokale Dienste zu Hause oder im Büro zugreifen möchten, aber von ihrem Internetanbieter keine öffentliche IP-Adresse erhalten.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} bietet einen sicheren Reverse-Proxy-Tunnel, über den Sie sicher auf Ressourcen hinter NAT und Firewalls zugreifen können.

1.  Folgen Sie [dieser Anleitung](../interface_guide/wireguard_server.md), um einen WireGuard-Server auf Ihrem GL.iNet-Router einzurichten, auch wenn Sie keine öffentliche IP-Adresse haben.

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Klicken Sie anschließend auf **Profiles**, um die WireGuard-Konfiguration zu exportieren. Unten sehen Sie eine Beispielkonfiguration.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2.  (Optional) Wenn Sie aus der Ferne auf das LAN des VPN-Servers zugreifen möchten, aktivieren Sie **Allow Remote Access LAN**. Andernfalls überspringen Sie diesen Schritt.

    ??? "Für Firmware v4.7 und früher"

        Gehen Sie im webbasierten Admin Panel des Servers zu **VPN** -> **VPN Dashboard** -> Bereich **VPN Server**. Klicken Sie rechts neben dem WireGuard-Server auf das Zahnradsymbol.

        ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

        Aktivieren Sie **Remote Access LAN** und klicken Sie auf **Apply**.

        ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

        **Wenn diese Option aktiviert ist, kann auf diesen Router und die LAN-Geräte über das VPN aus der Ferne zugegriffen werden.**

    ??? "Für Firmware v4.8 und neuer"

        Gehen Sie im webbasierten Admin Panel des Servers zu **VPN** -> **WireGuard Server**. Klicken Sie oben rechts auf **Options**.

        ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

        Aktivieren Sie **Allow Remote Access the LAN Subnet** und klicken Sie auf **Apply**.

        ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

        **Wenn diese Option aktiviert ist, kann auf diesen Router und die LAN-Geräte über das VPN aus der Ferne zugegriffen werden.**

3.  Registrieren Sie ein AstroRelay-Konto und folgen Sie dieser [Anleitung](https://www.astrorelay.com/tutorial.html){target="\_blank"}, um die Ersteinrichtung abzuschließen.

    Wählen Sie beim Hinzufügen einer neuen Domain den Server aus, der Ihrem Router am nächsten ist.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Wenn Sie einen neuen Link hinzufügen, tragen Sie die **LAN-IP-Adresse** Ihres Routers in das Feld **Destination Host IP** ein und **51820** in das Feld **Destination Port**.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Anschließend erhalten Sie einen Link wie **wg_server_test.arlab1.cc:33331**. Klicken Sie darauf, um ihn zu kopieren.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

4.  Öffnen Sie die WireGuard-Konfigurationsdatei, ersetzen Sie den Wert nach **Endpoint** durch den Link aus dem vorherigen Schritt und übernehmen Sie die Änderung.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

5.  Installieren Sie die [WireGuard-App](https://www.wireguard.com/install/){target="\_blank"} auf dem Gerät, das Sie als WireGuard-Client verwenden möchten. Laden Sie dann die geänderte Konfigurationsdatei in die App hoch und starten Sie die Verbindung. Alternativ können Sie die Datei auch auf einen anderen GL.iNet-Router hochladen und ihn als WireGuard-Client einrichten.

    Nach erfolgreicher Verbindung können Sie aus der Ferne auf Ihre lokalen Dienste zu Hause oder im Büro zugreifen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="\_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="\_blank"}.
