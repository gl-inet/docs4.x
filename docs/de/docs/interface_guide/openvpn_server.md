# OpenVPN-Server auf GL.iNet-Routern einrichten

OpenVPN ist ein Open-Source-VPN-Protokoll, das Techniken virtueller privater Netzwerke nutzt, um sichere Site-to-Site- oder Punkt-zu-Punkt-Verbindungen herzustellen.

Um auf einem GL.iNet-Router einen OpenVPN-Server einzurichten, sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Stellen Sie sicher, dass Sie eine öffentliche IP-Adresse haben

Klicken Sie bitte [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), um zu prüfen, ob Ihr Internetdienstanbieter Ihnen eine öffentliche IP-Adresse zuweist.

**Falls nicht, kann Ihr Router nicht als OpenVPN-Server eingerichtet werden.**

Alternative Möglichkeiten:

1. Wenn Sie einen Hauptrouter haben, melden Sie sich dort an und prüfen Sie, ob er eine öffentliche IP von Ihrem ISP erhält.
2. Fragen Sie Ihren ISP nach einer öffentlichen IP-Adresse. Dies kann zusätzliche Kosten verursachen.
3. Wenn die beiden oben genannten Methoden nicht funktionieren (z. B. wenn sich Ihr Netzwerk hinter CGNAT befindet), können Sie unsere SD-WAN-Lösung [AstroWarp](https://www.astrowarp.net/){target="_blank"} ausprobieren.

## Prüfen, ob eine Portweiterleitung erforderlich ist

**Netzwerktopologie**

??? "GL.iNet ist der Hauptrouter"
    
    * Wenn der GL.iNet-Router der Hauptrouter in Ihrem Netzwerk ist, ist keine Portweiterleitung erforderlich. Fahren Sie mit dem [nächsten Schritt](#set-up-openvpn-server) fort.

??? "GL.iNet ist der Unterrouter"

    * Wenn bereits ein Hauptrouter verwendet wird und der GL.iNet-Router als sekundärer Router konfiguriert ist, müssen Sie auf dem Hauptrouter eine [Portweiterleitung](../tutorials/how_to_set_up_port_forwarding.md) einrichten.
    
    * Wenn bereits ein Hauptrouter verwendet wird und sich der GL.iNet-Router mehrere Ebenen unterhalb des Hauptrouters befindet, richten Sie auf jeder Zwischenebene eine [Portweiterleitung](../tutorials/how_to_set_up_port_forwarding.md) ein.

## OpenVPN-Server einrichten

Melden Sie sich am webbasierten Admin Panel an und navigieren Sie zu **VPN** -> **OpenVPN Server**.

1. Klicken Sie auf **Generate Configuration** (nur für die Erstkonfiguration des VPN-Servers).

    ![ovpn server generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_generate_config.png){class="glboxshadow"}

2. Übernehmen Sie die Konfiguration.

    Die Standardkonfiguration funktioniert in den meisten Fällen.

    Wenn Sie die Konfiguration nicht anpassen müssen, klicken Sie unten auf **Export Client Configuration** und fahren Sie mit Schritt 3 fort.

    Wenn Sie die Konfiguration geändert haben, klicken Sie vor dem Export der Client-Konfiguration auf **Apply**.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S oder Tun. Klicken Sie [hier](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md/#tap-s2s-vs-tun-mode), um die Unterschiede zu sehen.

    * **Protocol:** UDP oder TCP. Klicken Sie [hier](../faq/openvpn_tcp_udp.md), um die Unterschiede zu sehen.

    * **Authentication Mode:** Hiermit wird festgelegt, welche Authentifizierungsmethode verwendet wird, wenn sich der Client mit dem Server verbindet. Es gibt drei Optionen.

        - **Certificate Only**: Wenn diese Option ausgewählt ist, erzeugt der Router automatisch Zertifikatsschlüssel für Server und Client und bettet sie in die Client-Konfigurationsdatei ein. Beim Hochladen der Konfiguration auf den Client sind keine zusätzlichen Zugangsdaten erforderlich.

        - **Username/Password Only**: Wenn diese Option ausgewählt ist, erzeugt der Router eine Client-Konfiguration ohne Zertifikatsschlüssel. Sie müssen zunächst auf der Registerkarte Users einen Benutzernamen und ein Passwort hinzufügen, bevor Sie die Client-Konfiguration exportieren. Beim Hochladen der Konfiguration auf den Client müssen diese Zugangsdaten zur Authentifizierung eingegeben werden.

        - **Username/Password and Certificate**: Wenn diese Option ausgewählt ist, müssen Sie zuerst auf der Registerkarte Users einen Benutzernamen und ein Passwort hinzufügen, bevor Sie die Client-Konfiguration exportieren. Zusätzlich erzeugt der Router automatisch Zertifikatsschlüssel für Server und Client und bettet sie in die Konfigurationsdatei ein. Beim Hochladen der Konfiguration auf den Client wird zuerst der Zertifikatsschlüssel geprüft und danach die Benutzername-/Passwort-Authentifizierung durchgeführt, um eine Zwei-Faktor-Sicherheit zu erreichen.
    
        Hier sehen Sie ein Beispiel für das Anlegen eines Benutzers.

        ![openvpn server add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: Bei Bedarf können Sie weitere Servereinstellungen anpassen.
    
        ![openvpn server advancd configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Client-Konfiguration exportieren.

    Klicken Sie unten auf der Registerkarte Configuration auf **Export Client Configuration** (oder übernehmen Sie zuvor die geänderte Konfiguration). Anschließend wird ein Fenster wie unten dargestellt geöffnet.

    ![openvpn server configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_export_configuration.png){class="glboxshadow"}

    - Wenn sich die öffentliche IP Ihres Netzwerks häufig ändert, können Sie [DDNS](ddns.md) aktivieren, um die DDNS-Domain als Serveradresse zu verwenden.

    - Seit Firmware v4.8 können Sie die Serveradresse aus öffentlicher IP, DDNS-Domain und aktueller WAN-IP auswählen. Nach einer Änderung wird die Serveradresse in der Konfigurationsdatei gleichzeitig aktualisiert.

    Klicken Sie dann auf **Download**, um die Konfiguration zu exportieren.

4. OpenVPN-Server starten.

    Klicken Sie oben rechts auf der Seite OpenVPN Server auf die Schaltfläche **Start**, um den Server zu starten. Wechseln Sie anschließend zur Seite VPN Dashboard, um seinen Status und weitere Einstellungen zu prüfen.

    ![start openvpn server](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Prüfen, ob der OpenVPN-Server ordnungsgemäß funktioniert

### Serverstatus prüfen

Seit Firmware v4.8 können Sie den Verbindungsstatus des Servers auf der Seite **OpenVPN Server** prüfen.

Wenn Upload-/Download-Datenverkehrsstatistiken angezeigt werden, bedeutet das, dass der OpenVPN-Server läuft.

![openvpn server connected v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

Bei Firmware v4.7 und früher prüfen Sie den Verbindungsstatus des Servers bitte auf der Seite **VPN Dashboard**.

![openvpn server connected v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/openserverup.jpg){class="glboxshadow"}

### IP des Clients prüfen

So prüfen Sie, ob die Verbindung zum Server erfolgreich ist: Importieren Sie die zuvor exportierte OpenVPN-Konfiguration auf ein Gerät in einem anderen Netzwerk (nicht im selben lokalen Netzwerk wie der Server). Öffnen Sie dann einen Webbrowser und suchen Sie nach Ihrer IP-Adresse und Ihrem Standort. Wenn diese mit der IP-Adresse und dem Standort des VPN-Servers übereinstimmen (statt mit denen Ihres Internetdienstanbieters), ist die VPN-Verbindung erfolgreich.

Am einfachsten geht dies mit einem Smartphone, auf dem die offizielle [OpenVPN App](https://openvpn.net/vpn-client/){target="_blank"} installiert ist. Deaktivieren Sie zunächst das WLAN des Smartphones und verbinden Sie es ausschließlich über mobile Daten (4G/5G) mit dem Internet. Öffnen Sie dann die OpenVPN-App, importieren Sie die Konfigurationsdatei und starten Sie die Verbindung. Prüfen Sie, ob das Smartphone auf das Internet zugreifen kann und ob seine IP-Adresse mit der IP des OpenVPN-Servers übereinstimmt.

Beim Importieren der Konfigurationsdatei in die OpenVPN-App kann ein Hinweis wie unten dargestellt erscheinen. Klicken Sie auf **CONTINUE**, um fortzufahren, da das Zertifikat bereits in der Konfigurationsdatei eingebettet ist.

![openvpn app select certificate](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Wenn die Verbindung fehlschlägt, gibt es mehrere häufige Ursachen:

* Ihr Internetdienstanbieter weist Ihnen keine öffentliche IP-Adresse zu. Prüfen Sie dies [hier](#stellen-sie-sicher-dass-sie-eine-öffentliche-ip-adresse-haben).
* Möglicherweise müssen Sie eine Portweiterleitung einrichten. Prüfen Sie dies [hier](#prüfen-ob-eine-portweiterleitung-erforderlich-ist).
* Der vom OpenVPN-Server verwendete Port wird von Ihrem Internetdienstanbieter blockiert. Wechseln Sie zu einem anderen Port oder wenden Sie sich für weitere Unterstützung an Ihren Internetdienstanbieter.
* In manchen Ländern/Regionen kann die VPN-Verbindung blockiert werden.

## Zugriff von Client zu Client

**Netzwerktopologie**

![ptptopology](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/ptptopology.jpg){class="glboxshadow"}

Aktivieren Sie die Umschaltoption für den Client-zu-Client-Zugriff und exportieren Sie eine neue Konfiguration für die Clients. Danach können Ihre Clients untereinander aufeinander zugreifen.

![peertopeer](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server/peertopeer.jpg){class="glboxshadow"}

## OpenVPN-App installieren

Bitte laden Sie die OpenVPN-App von der [offiziellen OpenVPN-Website](https://openvpn.net/vpn-client/){target="_blank"} herunter.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
