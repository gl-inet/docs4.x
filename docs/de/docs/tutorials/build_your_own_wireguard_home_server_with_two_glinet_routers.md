# Eigenen WireGuard-Heimserver mit zwei GL.iNet-Routern aufbauen

Dieser Artikel zeigt, wie Sie Ihren Heimrouter als WireGuard-VPN-Server und Ihren Reiserouter als WireGuard-VPN-Client einrichten, damit beide sich aus der Ferne miteinander verbinden. So können Sie überall mit dem Reiserouter Ihre Heim-IP-Adresse verwenden.

Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/v_DyRGicWco" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(In diesem Video werden GL-BE9300 (Flint 3) und GL-BE3600 (Slate 7) verwendet, um die VPN-Einrichtung zu demonstrieren.)</small>

In den folgenden Schritten verwenden wir GL-MT6000 (Flint 2) und GL-MT3000 (Beryl AX) als Beispiele:

- GL-MT6000, ein Heimrouter, wird als WireGuard-VPN-Server eingerichtet. Wenn keine WLAN-Kapazität benötigt wird, kann auch unser Sicherheits-Gateway GL-MT2500 oder ein anderes Modell verwendet werden.

- GL-MT3000, ein Reiserouter, wird als WireGuard-VPN-Client eingerichtet, um sich aus der Ferne mit dem VPN-Server zu Hause zu verbinden.

## Warum Sie Ihren eigenen WireGuard-Heimserver aufbauen sollten

1. Verwenden Sie Ihre Heim-IP-Adresse als Internetadresse, als wären Sie direkt zu Hause.
2. Im Vergleich zu VPN-Diensten von Drittanbietern fallen keine monatlichen Gebühren an.
3. Leiten Sie den gesamten Internetverkehr über einen verschlüsselten VPN-Tunnel in Ihr Heimnetzwerk und schützen Sie so Ihre Privatsphäre.
4. Erhalten Sie einfachen Zugriff auf interne Ressourcen und lokales Streaming.

## Vorbereitungen

### Prüfen, ob Sie eine öffentliche IP haben

Stellen Sie zunächst sicher, dass der GL-MT6000 auf seiner WAN-Seite eine öffentliche IP-Adresse hat, damit er weltweit erreichbar ist. Andernfalls kann Ihr Reiserouter während der Reise keine VPN-Verbindung mit ihm aufbauen.

Um zu prüfen, ob Sie eine öffentliche IP-Adresse haben, öffnen Sie bitte einen Webbrowser und geben Sie [what is my ip](https://whatismyipaddress.com/){target="_blank"} in die Adresszeile ein.

![whatismyip](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Dort wird Ihre öffentliche IP-Adresse angezeigt. Wenn sie mit der WAN-IP übereinstimmt, die Ihr ISP dem GL-MT6000 zuweist, verfügen Sie über eine öffentliche IP-Adresse.

Wenn Sie keine öffentliche IP-Adresse haben, finden Sie hier einige mögliche Lösungen.

1. Wenn Sie einen Hauptrouter haben, melden Sie sich dort an und prüfen Sie, ob er die öffentliche IP von Ihrem ISP erhält.
2. Fragen Sie Ihren ISP nach einer öffentlichen IP-Adresse. Dies kann zusätzliche Kosten verursachen.
3. Wenn die beiden oben genannten Wege nicht funktionieren, z. B. wenn Sie sich hinter CGNAT befinden, können Sie eine Reverse-Proxy-Methode wie [Astrorelay](how_to_set_up_wireguard_server_via_astrorelay.md) verwenden. Alternativ können Sie auch eine SD-WAN-Lösung wie [AstroWarp](https://www.astrowarp.net/) ausprobieren.

### Prüfen, ob eine Portweiterleitung erforderlich ist

??? "GL.iNet als Hauptrouter"

    Wenn Ihr GL.iNet-Router per Ethernet-Kabel direkt mit einem ISP-Modem verbunden ist, ist der GL.iNet-Router der Hauptrouter.

    **Wie prüfen Sie, ob Ihr GL.iNet-Router direkt mit dem ISP-Modem verbunden ist?**

    Schritte:
    
    1. Melden Sie sich am GL.iNet Admin Panel an.

    2. Wählen Sie in der linken Seitenleiste INTERNET. Prüfen Sie dort die Topologie und die Verbindungsdetails:

        Bei einer direkten Ethernet-Verbindung sehen Sie einen Abschnitt mit dem Namen „Ethernet“ samt Details wie Protokoll, IP-Adresse, Gateway usw.

        Im folgenden Bild ist die markierte IP Address die WAN-IP, die der ISP diesem GL.iNet-Router zuweist.

        ![mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Diese WAN-IP ist eine öffentliche IP-Adresse. Daher hat dieser GL.iNet-Router als Hauptrouter eine öffentliche IP und **es ist keine Portweiterleitung erforderlich**.

        Sie müssen diesen GL.iNet-Router lediglich als WireGuard-Server einrichten und einen Reiserouter als WireGuard-Client damit verbinden. Dann wird zwischen beiden ein VPN-Tunnel aufgebaut.

        ![topologywg](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}
    
??? "GL.iNet als Unterrouter"

    Richten Sie auf Ihrem Hauptrouter eine **Port Forwarding**-Regel für den GL.iNet-Router ein, wenn dieser sich hinter NAT befindet.

    Topologie

    ![togologywgtp](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    Beispiel: Ein TP-Link-Router als Hauptrouter zu Hause.

    Verbinden Sie sich mit dem Wi-Fi oder LAN Ihres Heimrouters. Melden Sie sich dann am webbasierten Admin Panel an und prüfen Sie die WAN-IP-Adresse, die er von Ihrem ISP erhält. Im folgenden Bild sehen Sie, dass Ihre öffentliche IP **42.200.00.00** ist.

    ![tp_home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}
    
    **Bevor Sie die Portweiterleitung einrichten, empfehlen wir, auf Ihrem Hauptrouter eine IP-Adresse für den GL.iNet-Router zu reservieren, damit diesem eine feste IP zugewiesen wird.** Andernfalls kann der Hauptrouter dem GL.iNet-Router nach einem Neustart eine andere IP zuweisen, wodurch die Portweiterleitungsregel ungültig wird.

    Richten Sie anschließend die Portweiterleitung auf Ihrem Hauptrouter für den GL.iNet-Router ein.

    1. Gehen Sie zu „Advanced“, klicken Sie auf „virtual Server“ und dann auf „Add“.
    
    2. Internal IP (Device IP): Das ist die dem GL.iNet-Router zugewiesene IP-Adresse; Sie finden sie in der Client-Liste von TP-Link.
    
    3. External/Internal port: Tragen Sie in beide Felder `51820` ein.
    
    4. Protocol: Sie können „All“ oder „UDP“ oder „TCP/UDP“ wählen.

    ![tp_port1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Weitere Beispiele für [Port Forward](how_to_set_up_port_forwarding.md)**

## WireGuard-Server einrichten

### DDNS aktivieren (optional)

Aktivieren Sie die DDNS-Funktion, wenn Sie keine statische öffentliche IP, sondern nur eine dynamische öffentliche IP haben.

Melden Sie sich am webbasierten Admin Panel des GL-MT6000 an und gehen Sie zu **APPLICATIONS** -> **Dynamic DNS**. Aktivieren Sie den Schalter für **Enable DDNS**.

Aktivieren Sie das Kontrollkästchen für **Terms of Service & Privacy Policy** und klicken Sie auf **Apply**.

![ddnsapply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Gehen Sie dann zu **WireGuard Server** -> Registerkarte Configuration, stellen Sie sicher, dass der Listening-Port 51820 ist, und klicken Sie auf **Apply**.

![wgserver](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Konfiguration erzeugen

Klicken Sie auf derselben Seite auf die Registerkarte **Profiles** neben Configuration und dann auf **Add** (im folgenden Bild mit 1 markiert).

Dadurch wird automatisch eine Client-Konfiguration erzeugt. Klicken Sie auf das **Weiterleitungs-Symbol** (mit 2 markiert).

Aktivieren Sie im Pop-up-Fenster per Schieberegler die DDNS-Domain (mit 3 markiert; dies ist optional und nur bei dynamischer öffentlicher IP erforderlich).

![wgservergen](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Anschließend können Sie den QR-Code mit der WireGuard-[Mobil-App](https://www.wireguard.com/install/) scannen, um den Server zu testen. Details finden Sie [hier](../interface_guide/wireguard_server.md/#check-if-wireguard-server-is-working-properly).

Alternativ können Sie eine Konfiguration im Textformat für die VPN-Client-Verbindung exportieren.

Wechseln Sie von der QR-Code-Ansicht zur Textansicht, indem Sie auf die Registerkarte **Configuration File** klicken.

Kopieren Sie den Text für den Client oder klicken Sie auf Download und speichern Sie die Datei zur späteren Verwendung.

![configload](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## WireGuard-Client einrichten

### LAN-IP ändern

Da in diesem Tutorial GL-MT6000 und GL-MT3000 verwendet werden und beide standardmäßig die LAN-IP **192.168.8.1** haben, müssen wir eine davon auf eine andere LAN-IP ändern, um Konflikte zu vermeiden.

Hier sind die Schritte zum Ändern der LAN-IP des GL-MT3000 (des WireGuard-Clients).

Melden Sie sich am webbasierten Admin Panel des GL-MT3000 an und gehen Sie in der linken Seitenleiste zu **NETWORK** -> **LAN**, um die LAN-IP zu ändern. Zum Beispiel können Sie die LAN-IP von der Standardadresse `192.168.8.1` auf `192.168.10.1` ändern.

![change lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Weitere Informationen zur LAN-Schnittstelle finden Sie [hier](../interface_guide/lan.md).

### Konfiguration hinzufügen

Gehen Sie im webbasierten Admin Panel des GL-MT3000 zu **VPN** -> **WireGuard Client** und klicken Sie auf **Add Manually**.

![addwgclient1](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Erstellen Sie links eine Gruppe und vergeben Sie einen Namen. Wählen Sie dann die hochzuladende Konfigurationsdatei aus oder ziehen Sie sie in das Upload-Feld auf der rechten Seite.

![addwgclient2](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Sobald die Datei die Prüfung bestanden hat, klicken Sie auf **Apply**.

![addwgclient3](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Sie können auch auf **Manually Add Configuration** klicken, den Konfigurationstext einfügen und dann auf **Apply** klicken.

![addwgclient4](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![addwgclient5](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Die Konfigurationsdatei wird auf der Seite WireGuard Client angezeigt, sobald sie erfolgreich hochgeladen wurde.

![addwgclient6](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Verbindung starten

Klicken Sie auf das Drei-Punkte-Symbol und dann auf **Start**.

![wgstart](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Warten Sie einige Minuten. Sobald die Verbindung erfolgreich hergestellt ist, leuchtet ein grüner Punkt auf.

![wgconnected](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Wechseln Sie zum **VPN Dashboard**. Dort sehen Sie, dass Ihr Client sich mit Ihrer öffentlichen Heim-IP-Adresse mit dem Server verbindet. Die Seite kann je nach Firmware-Version leicht abweichen.

![clientup](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Melden Sie sich erneut am webbasierten Admin Panel des GL-MT6000 (dem WireGuard-Server) an und gehen Sie zu **VPN** -> **WireGuard Server** (oder zu **VPN** -> **VPN Dashboard**, wenn Sie Firmware v4.7 oder älter verwenden). Dort sehen Sie ebenfalls den Verbindungsstatus, der anzeigt, dass der Client verbunden ist.

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(WireGuard-Server-Seite in FW v4.8)</small>

![servercon](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(VPN-Dashboard-Seite in FW v4.7 und früher)</small>

## Vorbereitung für spätere VPN-Fehlerbehebung aus der Ferne

Für den Fall unvorhergesehener Probleme während der Reise sollten Sie beide Router vorab mit Ihrem GoodCloud-Konto verknüpfen, damit eine VPN-Fehlerbehebung aus der Ferne möglich ist.

Manchmal kann Ihr Server aufgrund eines Stromausfalls oder aus anderen Gründen ausfallen. Um die Erreichbarkeit Ihres Servers zu erhalten, verknüpfen Sie ihn bitte mit GL.iNet GoodCloud.

---

Verwandte Artikel

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
