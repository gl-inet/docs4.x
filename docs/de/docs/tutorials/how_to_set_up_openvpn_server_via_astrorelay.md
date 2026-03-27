# So richten Sie einen OpenVPN-Server über AstroRelay ein

Diese Anleitung beschreibt die Schritte zum Einrichten eines OpenVPN-Servers über AstroRelay auf einem GL.iNet-Router. Sie eignet sich besonders für Benutzer, die aus der Ferne auf lokale Dienste zu Hause oder im Büro zugreifen möchten, aber von ihrem Internetanbieter keine öffentliche IP-Adresse erhalten.

[AstroRelay](https://www.astrorelay.com){target="\_blank"} bietet einen sicheren Reverse-Proxy-Tunnel, über den Sie sicher auf Ressourcen hinter NAT und Firewalls zugreifen können.

1.  Folgen Sie [dieser Anleitung](../interface_guide/openvpn_server.md), um einen OpenVPN-Server auf Ihrem GL.iNet-Router einzurichten, auch wenn Sie keine öffentliche IP-Adresse haben.

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Exportieren Sie anschließend die OpenVPN-Konfiguration. Unten sehen Sie eine Beispielkonfiguration.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2.  (Optional) Wenn Sie aus der Ferne auf das LAN des VPN-Servers zugreifen möchten, aktivieren Sie **Allow Remote Access LAN**. Andernfalls überspringen Sie diesen Schritt.

    ??? "Für Firmware v4.7 und früher"

        1. Klicken Sie in der linken Seitenleiste auf **VPN** > **VPN Dashboard**.
        2. Klicken Sie auf das Optionssymbol.
        3. Aktivieren Sie den Schalter für **Remote Access LAN**.
        4. Klicken Sie auf **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    ??? "Für Firmware v4.8 und neuer"

        1. Klicken Sie in der linken Seitenleiste auf **VPN** > **OpenVPN Server**.
        2. Klicken Sie oben rechts auf **Options**.
        3. Aktivieren Sie den Schalter für **Allow Remote Access the LAN Subnet**.
        4. Klicken Sie auf **Apply**.

            ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}

3.  Registrieren Sie ein AstroRelay-Konto und folgen Sie dieser [Anleitung](https://www.astrorelay.com/tutorial.html){target="\_blank"}, um die Ersteinrichtung abzuschließen.

    Wählen Sie beim Hinzufügen einer neuen Domain den Server aus, der Ihrem Router am nächsten ist.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Wenn Sie einen neuen Link hinzufügen, tragen Sie die **LAN-IP-Adresse** Ihres Routers in das Feld **Destination Host IP** ein und **1194** in das Feld **Destination Port**.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Anschließend erhalten Sie einen Link wie **testforx3000.arlab1.cc:37202**. Klicken Sie darauf, um ihn zu kopieren.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

4.  Öffnen Sie die OpenVPN-Konfigurationsdatei und ersetzen Sie den Wert nach **Remote** durch den Link aus dem vorherigen Schritt. Im folgenden Beispiel wird „42.200.00.00 1194“ durch „testforx3000.arlab1.cc:37202“ ersetzt. Ersetzen Sie danach den Doppelpunkt ":" durch ein Leerzeichen und übernehmen Sie die Änderung.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

5.  Installieren Sie die [OpenVPN Connect App](https://openvpn.net/client/){target="\_blank"} auf dem Gerät, das Sie als OpenVPN-Client verwenden möchten. Laden Sie dann die geänderte Konfigurationsdatei in die App hoch und starten Sie die Verbindung. Alternativ können Sie die Datei auch auf einen anderen GL.iNet-Router hochladen und ihn als OpenVPN-Client einrichten.

    Nach erfolgreicher Verbindung können Sie aus der Ferne auf Ihre lokalen Dienste zu Hause oder im Büro zugreifen.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="\_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="\_blank"}.
