# So richten Sie einen WireGuard-Server über AstroRelay ein

Szenario: Sie möchten auf Ihrem GL.iNet-Router zu Hause oder im Büro einen WireGuard-Server einrichten, um per Fernzugriff auf Ihren lokalen Dienst zuzugreifen, aber Ihr Internetanbieter stellt keine öffentliche IP-Adresse bereit.

[AstroRelay](https://www.astrorelay.com){target="_blank"} stellt einen sicheren Reverse-Proxy-Tunnel bereit, über den Sie sicher auf Ressourcen hinter NAT und Firewalls zugreifen können.

1. Folgen Sie der Anleitung [hier](../interface_guide/wireguard_server.md), um einen WireGuard-Server einzurichten, auch wenn Sie keine öffentliche IP-Adresse haben. Aktivieren Sie dabei bitte **Allow Access Local Network**.

    ![set up wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/start_wg_server4x.jpg){class="glboxshadow"}

    Exportieren Sie anschließend eine WireGuard-Konfiguration. Die folgende Abbildung zeigt ein Beispiel.

    ![wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/wireguard_config.png){class="glboxshadow"}

2. Registrieren Sie ein AstroRelay-Konto und folgen Sie diesem [Tutorial](https://www.astrorelay.com/tutorial.html){target="_blank"}, um die Ersteinrichtung abzuschließen.

    Wählen Sie beim Hinzufügen einer neuen Domain den Server aus, der Ihrem Router am nächsten ist.

    ![astrorelay add a new domain](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_add_a_new_domain.png){class="glboxshadow"}

    Geben Sie beim Hinzufügen eines neuen Links die **LAN-IP-Adresse** Ihres Routers in das Feld **Destination Host IP** ein. Geben Sie **51820** in das Feld **Destination Port** ein.

    ![link for wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_wg_server.png){class="glboxshadow"}

    Anschließend erhalten Sie einen Link wie **wg_server_test.arlab1.cc:33331**. Klicken Sie darauf, um ihn zu kopieren.

    ![astrorelay link](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/astrorelay_link.png){class="glboxshadow"}

3. Öffnen Sie die WireGuard-Konfiguration und ersetzen Sie die Daten nach **Endpoint** durch den Link aus dem vorherigen Schritt. Danach können Sie die geänderte Konfiguration in einer WireGuard-Client-App verwenden.

    ![replace link in wireguard config](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_wireguard_server_via_astrorelay/replace_endpoint_in_wireguard_config.png){class="glboxshadow"}

4. Wenn Sie nicht zu Hause oder im Büro sind, können Sie die geänderte Konfigurationsdatei in die WireGuard-Client-App hochladen, um auf Ihren lokalen Dienst zu Hause oder im Büro zuzugreifen, als wären Sie vor Ort.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
