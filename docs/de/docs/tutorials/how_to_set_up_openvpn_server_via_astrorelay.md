# So richten Sie einen OpenVPN-Server über AstroRelay ein

Szenario: Sie möchten auf Ihrem GL.iNet-Router zu Hause oder im Büro einen OpenVPN-Server einrichten, um per Fernzugriff auf Ihren lokalen Dienst zuzugreifen, aber Ihr Internetanbieter stellt keine öffentliche IP-Adresse bereit.

[AstroRelay](https://www.astrorelay.com){target="_blank"} stellt einen sicheren Reverse-Proxy-Tunnel bereit, über den Sie sicher auf Ressourcen hinter NAT und Firewalls zugreifen können.

1. Folgen Sie der Anleitung [hier](../interface_guide/openvpn_server.md), um einen OpenVPN-Server einzurichten, auch wenn Sie keine öffentliche IP-Adresse haben. Aktivieren Sie dabei bitte **Allow Access Local Network**.

    ![set up openvpnd server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/start_ovpn_server4x.jpg){class="glboxshadow"}

    Exportieren Sie anschließend eine OpenVPN-Konfiguration. Die folgende Abbildung zeigt ein Beispiel.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

2. Registrieren Sie ein AstroRelay-Konto und folgen Sie diesem [Tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"}, um die Ersteinrichtung abzuschließen.

    Wählen Sie beim Hinzufügen einer neuen Domain den Server aus, der Ihrem Router am nächsten ist.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Geben Sie beim Hinzufügen eines neuen Links die **LAN-IP-Adresse** Ihres Routers in das Feld **Destination Host IP** ein. Geben Sie **1194** in das Feld **Destination Port** ein.

    ![link for openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnaddlink.jpg){class="glboxshadow"}

    Anschließend erhalten Sie einen Link wie **testforx3000.arlab1.cc:37202**. Klicken Sie darauf, um ihn zu kopieren.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpncopylink.jpg){class="glboxshadow"}

3. Öffnen Sie die OpenVPN-Konfiguration und ersetzen Sie die Daten nach **Remote** durch den Link aus dem vorherigen Schritt. Im folgenden Beispiel ersetzen wir „42.200.00.00 1194“ durch den Link „testforx3000.arlab1.cc:37202“.

    Ersetzen Sie danach den Doppelpunkt ":" durch ein Leerzeichen, also z. B. „testforx3000.arlab1.cc 37202“.

    ![openvpn config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnpastelink.jpg){class="glboxshadow"}

    ![replace link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnconfig.jpg){class="glboxshadow"}

    Danach können Sie die geänderte Konfigurationsdatei in einer OpenVPN-Client-App verwenden.

4. Wenn Sie nicht zu Hause oder im Büro sind, können Sie die geänderte Konfigurationsdatei in die OpenVPN-Client-App hochladen, um auf Ihren lokalen Dienst zu Hause oder im Büro zuzugreifen, als wären Sie vor Ort.

    ![openvpn up](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_server_via_astrorelay/astroovpnup.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
