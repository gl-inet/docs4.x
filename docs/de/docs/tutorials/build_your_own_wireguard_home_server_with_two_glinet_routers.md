# Eigenen WireGuard-Heimserver mit zwei GL.iNet-Routern aufbauen {#build-your-own-wireguard-home-server-with-two-glinet-routers}

Dieser Artikel zeigt, wie Sie Ihren Heimrouter als WireGuard-VPN-Server und Ihren Reiserouter als WireGuard-VPN-Client einrichten, damit beide sich aus der Ferne miteinander verbinden. So können Sie überall mit dem Reiserouter Ihre Heim-IP-Adresse verwenden.

Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In diesem Video werden GL-MT5000 (Brume 3) und GL-MT3600BE (Beryl 7) verwendet, um die VPN-Einrichtung zu demonstrieren.)</small>

In den folgenden Schritten verwenden wir GL-MT6000 (Flint 2) und GL-MT3000 (Beryl AX) als Beispiele:

- GL-MT6000, ein Heimrouter, wird als WireGuard-VPN-Server eingerichtet. Wenn keine WLAN-Kapazität benötigt wird, kann auch unser Sicherheits-Gateway GL-MT2500 oder ein anderes Modell verwendet werden.

- GL-MT3000, ein Reiserouter, wird als WireGuard-VPN-Client eingerichtet, um sich aus der Ferne mit dem VPN-Server zu Hause zu verbinden.

## Vorteile eines eigenen WireGuard-Heimservers {#why-build-your-own-wireguard-home-server}

1. Verwenden Sie die öffentliche IP-Adresse Ihres Heimanschlusses, sodass Ihr Datenverkehr von dort zu stammen scheint.
2. Sparen Sie sich die monatlichen Gebühren für VPN-Dienste von Drittanbietern.
3. Schützen Sie Ihre Privatsphäre, indem Sie den gesamten Internetverkehr durch einen verschlüsselten Tunnel in Ihr Heimnetzwerk leiten.
4. Greifen Sie von überall auf Ihre Geräte zu Hause und auf lokale Streaming-Dienste zu.

## Vorbereitungen {#preparations}

### Prüfen, ob Sie eine öffentliche IP haben {#check-if-you-have-a-public-ip}

Stellen Sie zunächst sicher, dass der GL-MT6000 auf seiner WAN-Seite eine öffentliche IP-Adresse hat, damit er weltweit erreichbar ist. Andernfalls kann Ihr Reiserouter während der Reise keine VPN-Verbindung mit ihm aufbauen.

Um zu prüfen, ob Sie eine öffentliche IP-Adresse haben, öffnen Sie bitte einen Webbrowser und geben Sie [what is my ip](https://whatismyipaddress.com/){target="_blank"} in die Adresszeile ein.

![whatismyip](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Dort wird Ihre öffentliche IP-Adresse angezeigt. Wenn sie mit der WAN-IP übereinstimmt, die Ihr ISP dem GL-MT6000 zuweist, verfügen Sie über eine öffentliche IP-Adresse.

Wenn Sie keine öffentliche IP-Adresse haben, finden Sie hier einige mögliche Lösungen.

1. Wenn Sie einen Hauptrouter haben, melden Sie sich dort an und prüfen Sie, ob er die öffentliche IP von Ihrem ISP erhält.
2. Fragen Sie Ihren ISP nach einer öffentlichen IP-Adresse. Dies kann zusätzliche Kosten verursachen.
3. Wenn die beiden oben genannten Methoden nicht funktionieren (z. B. wenn sich Ihr Netzwerk hinter CGNAT befindet), können Sie unsere SD-WAN-Lösung [AstroWarp](../interface_guide/astrowarp.md){target="_blank"} ausprobieren.

### Prüfen, ob eine Portweiterleitung erforderlich ist {#check-if-port-forwarding-is-required}

??? "GL.iNet als Hauptrouter"

    Wenn Ihr GL.iNet-Router per Ethernet-Kabel direkt mit einem ISP-Modem verbunden ist, ist der GL.iNet-Router der Hauptrouter.

    **Wie prüfen Sie, ob Ihr GL.iNet-Router direkt mit dem ISP-Modem verbunden ist?**

    Melden Sie sich im GL.iNet-Admin-Panel an. Wählen Sie links **INTERNET** und prüfen Sie die Netzwerktopologie und die Verbindungsdetails.

    Bei einer direkten Ethernet-Verbindung sehen Sie einen Abschnitt mit dem Namen „Ethernet“ samt Details wie Protokoll, IP-Adresse, Gateway usw.

    Im folgenden Bild ist die markierte IP Address die WAN-IP, die der ISP diesem GL.iNet-Router zuweist.

    ![mt6000-home](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Diese WAN-IP ist eine öffentliche IP-Adresse. Daher hat dieser GL.iNet-Router als Hauptrouter eine öffentliche IP und **es ist keine Portweiterleitung erforderlich**.

    Sie müssen diesen GL.iNet-Router lediglich als WireGuard-Server einrichten und einen Reiserouter als WireGuard-Client damit verbinden. Dann wird zwischen beiden ein VPN-Tunnel aufgebaut.

    ![topologywg](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet als Unterrouter"

    Richten Sie auf Ihrem Hauptrouter eine **Port Forwarding**-Regel für den GL.iNet-Router ein, wenn dieser sich hinter NAT befindet.

    ![togologywgtp](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Beispiel: Ein TP-Link-Router als Hauptrouter zu Hause.

    Verbinden Sie sich mit dem Wi-Fi oder LAN Ihres Heimrouters. Melden Sie sich dann am webbasierten Admin Panel an und prüfen Sie die WAN-IP-Adresse, die er von Ihrem ISP erhält. Im folgenden Bild sehen Sie, dass Ihre öffentliche IP **42.200.00.00** ist.

    ![tp_home](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Bevor Sie die Portweiterleitung einrichten, empfehlen wir, auf Ihrem Hauptrouter eine IP-Adresse für den GL.iNet-Router zu reservieren, damit diesem eine feste IP zugewiesen wird.** Andernfalls kann der Hauptrouter dem GL.iNet-Router nach einem Neustart eine andere IP zuweisen, wodurch die Portweiterleitungsregel ungültig wird.

    Richten Sie anschließend die Portweiterleitung auf Ihrem Hauptrouter für den GL.iNet-Router ein.

    1. Gehen Sie zu „Advanced“, klicken Sie auf „virtual Server“ und dann auf „Add“.
    
    2. Internal IP (Device IP): Das ist die dem GL.iNet-Router zugewiesene IP-Adresse; Sie finden sie in der Client-Liste von TP-Link.
    
    3. External/Internal port: Tragen Sie in beide Felder `51820` ein.
    
    4. Protocol: Sie können „All“ oder „UDP“ oder „TCP/UDP“ wählen.

    ![tp_port1](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Weitere Beispiele für [Port Forward](how_to_set_up_port_forwarding.md)**

## WireGuard-Server einrichten {#set-up-wireguard-server}

1. Melden Sie sich im Web-Admin-Panel an und öffnen Sie **VPN** -> **WireGuard Server**. Klicken Sie auf **Generate Configuration**. Dieser Schritt ist nur bei der Ersteinrichtung des VPN-Servers erforderlich.

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Prüfen Sie die Konfiguration.

    Die unten gezeigte Standardkonfiguration funktioniert in den meisten Fällen.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address** ist die Tunnel-IP des WireGuard-Servers. Sie können die Adresse beibehalten, sofern kein Konflikt mit dem Gateway des vorgeschalteten Routers besteht.

        Ändern Sie die Adresse bei einem Konflikt beispielsweise in **10.1.0.1/24** und klicken Sie auf **Apply**. Geben Sie die CIDR-Notation „/24“ mit an, um Verbindungsprobleme zu vermeiden.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Ein vorgeschalteter Xfinity-Router kann beispielsweise die IP-Adresse 10.0.0.1 haben. Wenn Sie einen GL.iNet-Router als WireGuard-Server einrichten, kann diese IP-Adresse bei einigen Modellen mit der Tunnel-IP in Konflikt stehen. Ändern Sie die Adresse nur bei einem Konflikt.

        ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**. IPv6 ist auf GL.iNet-Routern standardmäßig deaktiviert. Wenn Sie eine IPv6-Adresse verwenden möchten, aktivieren Sie [IPv6](../interface_guide/ipv6.md) auf Ihrem Router.

    - **Listen Port**. Der WireGuard-Server verwendet standardmäßig den UDP-Port `51820`. Wenn Sie diesen Port ändern und Portweiterleitung verwenden, passen Sie die Regel auf dem vorgeschalteten Router so an, dass sie auf den neuen Port des Servers weiterleitet. Tragen Sie den externen Port der Weiterleitung im Feld `Endpoint` jedes Client-Profils ein. Wenn der Server direkt erreichbar ist, verwenden Sie dort den Port, auf dem der Server Verbindungen annimmt.

    - **Enable Obfuscation**. Wenn diese Option aktiviert ist, verschleiert der VPN-Server den Datenverkehr mit dem AmneziaWG-Protokoll. Behalten Sie die Standardeinstellungen bei und ändern Sie sie nur, wenn Sie mit den Parametern vertraut sind.

        - [AmneziaWG-Verschleierung auf GL.iNet-Routern](../faq/amneziawg_obfuscation.md)
        - [VPN-Verschleierung auf GL.iNet-Routern einrichten](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Fügen Sie ein Profil hinzu.

    Wechseln Sie zur Registerkarte **Profiles** und klicken Sie auf **Add**, um ein Profil für Ihr Gerät zu erstellen.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Vergeben Sie einen aussagekräftigen Namen und klicken Sie auf **Apply**.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Klicken Sie bei Bedarf auf **Set More**, um weitere Einstellungen vorzunehmen. Klicken Sie anschließend auf **Apply**.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Bei Bedarf Routing-Regeln hinzufügen"

        In den meisten Fällen sind keine Routing-Regeln erforderlich.

        Wenn Sie vom Server aus auf Geräte im LAN des WireGuard-Clients zugreifen möchten, wechseln Sie auf der Seite **WireGuard Server** zur Registerkarte **Route Rules** und richten Sie dort die Regeln ein. Folgen Sie der [Anleitung für den Zugriff auf das Client-LAN](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Andernfalls fahren Sie mit Schritt 4 fort, um die Client-Konfiguration herunterzuladen.

4. Laden Sie die Konfiguration herunter.

    Nachdem Sie ein Profil hinzugefügt und auf **Apply** geklickt haben, stellt der Router die Konfiguration als QR-Code, als Klartext oder als herunterladbare `.conf`-Datei bereit.

    - **QR-Code**. Scannen Sie den Code in der WireGuard-App, um ein reguläres WireGuard-Profil zu importieren. Wenn Sie die Verschleierung aktiviert haben, verwenden Sie die AmneziaWG-App oder einen anderen Client, der AmneziaWG-Verschleierung unterstützt.

        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Klartext**. Sie können die Konfigurationsdetails im Klartext prüfen und für eine manuelle Einrichtung kopieren, etwa in die WireGuard-App oder auf einen GL.iNet-Router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf-Datei**. Klicken Sie auf **Download**, um die Datei auf Ihrem Gerät zu speichern. Sie können die Datei direkt in die WireGuard-App oder auf einen GL.iNet-Router hochladen.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    Ab Firmware v4.8 können Sie bei Bedarf als Serveradresse die öffentliche IP-Adresse, die DDNS-Domain oder die aktuelle WAN-IP-Adresse wählen. Bei einer Änderung wird die Serveradresse in der Konfigurationsdatei gleichzeitig aktualisiert.

    Wenn sich die öffentliche IP-Adresse Ihres Netzwerks beispielsweise häufig ändert, aktivieren Sie [DDNS](../interface_guide/ddns.md) und verwenden Sie die DDNS-Domain als Serveradresse.

    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Klicken Sie oben rechts auf **Start**, um den WireGuard-Server zu starten. Der Verbindungsstatus wird auf derselben Seite angezeigt.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## WireGuard-Client einrichten {#set-up-wireguard-client}

### LAN-IP ändern {#change-the-lan-ip}

Da in diesem Tutorial GL-MT6000 und GL-MT3000 verwendet werden und beide standardmäßig die LAN-IP **192.168.8.1** haben, müssen wir eine davon auf eine andere LAN-IP ändern, um Konflikte zu vermeiden.

So ändern Sie die LAN-IP-Adresse des GL-MT3000, der als WireGuard-Client dient.

Melden Sie sich im Web-Admin-Panel des GL-MT3000 an und öffnen Sie **NETWORK** -> **LAN**. Ändern Sie die LAN-IP-Adresse beispielsweise von der Standardadresse 192.168.8.1 in `192.168.20.1`.

![change lan](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

### Konfiguration hinzufügen {#add-the-configuration}

Gehen Sie im webbasierten Admin Panel des GL-MT3000 zu **VPN** -> **WireGuard Client** und klicken Sie auf **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Erstellen Sie links eine Gruppe und vergeben Sie einen Namen. Wählen Sie dann die hochzuladende Konfigurationsdatei aus oder ziehen Sie sie in das Upload-Feld auf der rechten Seite.

![addwgclient2](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Sobald die Datei die Prüfung bestanden hat, klicken Sie auf **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Sie können auch auf **Manually Add Configuration** klicken, den Konfigurationstext einfügen und dann auf **Apply** klicken.

![addwgclient4](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Die Konfigurationsdatei wird auf der Seite WireGuard Client angezeigt, sobald sie erfolgreich hochgeladen wurde.

![addwgclient6](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Verbindung starten {#start-the-connection}

Klicken Sie auf das Drei-Punkte-Symbol und dann auf **Start**.

![wgstart](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Warten Sie einige Minuten. Sobald die Verbindung erfolgreich hergestellt ist, leuchtet ein grüner Punkt auf.

![wgconnected](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Wechseln Sie zum **VPN Dashboard**. Dort sehen Sie, dass Ihr Client sich mit Ihrer öffentlichen Heim-IP-Adresse mit dem Server verbindet. Die Seite kann je nach Firmware-Version leicht abweichen.

![clientup](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Melden Sie sich erneut am webbasierten Admin Panel des GL-MT6000 (dem WireGuard-Server) an und gehen Sie zu **VPN** -> **WireGuard Server** (oder zu **VPN** -> **VPN Dashboard**, wenn Sie Firmware v4.7 oder älter verwenden). Dort sehen Sie ebenfalls den Verbindungsstatus, der anzeigt, dass der Client verbunden ist.

![servercon](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(WireGuard-Server-Seite in FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/de/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(VPN-Dashboard-Seite in FW v4.7 und früher)</small>

## Vorbereitung für spätere VPN-Fehlerbehebung aus der Ferne {#prep-for-remote-vpn-fixes-ahead}

Verknüpfen Sie beide Router vor der Reise mit Ihrem GoodCloud-Konto. So können Sie Fehler aus der Ferne beheben, wenn Ihre VPN-Verbindung aufgrund von Konfigurations- oder anderen Netzwerkproblemen ausfällt. Der Fernzugriff funktioniert nur, solange die Router eingeschaltet und mit dem Internet verbunden sind.

---

Verwandte Artikel

- [WireGuard-Server auf GL.iNet-Routern einrichten](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
