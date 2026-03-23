# Kein Zugriff auf das web Admin Panel

Manchmal können Sie [http://192.168.8.1](http://192.168.8.1) nicht aufrufen und sich daher nicht am web Admin Panel anmelden. Dafür kann es mehrere Gründe geben.

![can't access admin](https://static.gl-inet.com/docs/router/en/4/tutorials/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Mögliche Ursachen

* Ihr Computer oder Mobiltelefon ist nicht mit dem Router verbunden.
* `192.168.8.1` ist die Standard-IP-Adresse des Routers. Möglicherweise haben Sie diese IP geändert.
* Der Browser-Cache oder eine Browser-Erweiterung kann dazu führen, dass das Admin Panel nicht erreichbar ist.
* VPN- oder Proxy-Software verarbeitet Ihren Datenverkehr, wodurch das Admin Panel möglicherweise nicht erreichbar ist.
* Der Router ist beschädigt.

## Allgemeine Schritte für den Zugriff auf das web Admin Panel prüfen

1. Schalten Sie den Router ein, ohne ein Gerät damit zu verbinden.
2. Verbinden Sie Ihr Mobiltelefon oder Ihren Laptop mit dem Wi-Fi des Routers und geben Sie den auf dem Routeretikett aufgedruckten Wi-Fi Key ein.
3. Wenn Schritt 2 fehlschlägt, schalten Sie Wi-Fi auf Ihrem Computer oder Laptop aus. Verbinden Sie ihn stattdessen über ein Ethernet-Kabel mit dem LAN-Port des Routers.
4. Öffnen Sie einen Browser, geben Sie `192.168.8.1` in die Adressleiste ein und drücken Sie Enter. Sie sollten das GL.iNet web Admin Panel aufrufen können.

Oder Sie können [die App](mobile_app.md) verwenden, um auf den Router zuzugreifen.

## Weitere Schritte zur Behebung dieses Problems

1. [Verbindung prüfen](#verbindung-prüfen)
2. [IP-Adresse des Routers prüfen](#ip-adresse-des-routers-prüfen)
3. [Auf die IP-Adresse des Routers zugreifen](#auf-die-ip-adresse-des-routers-zugreifen)

---

### Verbindung prüfen

Wenn Sie über ein Ethernet-Kabel verbunden sind, stellen Sie sicher, dass die WAN/LAN-Port-Verbindung des Routers korrekt ist:

- Der WAN-Port ist mit einer Internetquelle verbunden, z. B. einem Modem oder einem primären Router.
- Der LAN-Port ist mit dem Endgerät verbunden, z. B. Ihrem Laptop.

Wenn Sie über Wi-Fi verbunden sind, stellen Sie sicher, dass Sie auf Ihrem Gerät die richtige SSID ausgewählt und das richtige Passwort eingegeben haben.

### IP-Adresse des Routers prüfen

Befolgen Sie die folgenden Schritte, um die IP-Adresse des Routers zu prüfen.

=== "Windows 10 / Windows 11"

    Öffnen Sie die Systemsteuerung und stellen Sie sicher, dass oben rechts die Ansicht Große Symbole oder Kleine Symbole ausgewählt ist.

    ![control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/control_panel_view_by.png){class="glboxshadow"}

    Systemsteuerung -> Netzwerk- und Freigabecenter -> Klicken Sie auf die Verbindung. Möglicherweise haben Sie mehrere Verbindungen; wählen Sie bitte die entsprechende Verbindung des Routers aus, den Sie prüfen möchten.

    ![network and sharing center, connections](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    Daraufhin wird ein Dialogfenster mit dem Status der Verbindung geöffnet. Klicken Sie auf die Schaltfläche "Details".

    ![network and sharing center, connections status](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    Daraufhin wird ein Dialogfenster mit den Details der Netzwerkverbindung geöffnet. Die IP-Adresse des Routers ist das **IPv4 Default Gateway**.

    ![network and sharing center, connections status detail](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Systemsteuerung -> Netzwerk und Internet -> Netzwerk- und Freigabecenter -> Adaptereinstellungen ändern

    Klicken Sie mit der rechten Maustaste auf das Netzwerk -> Status -> Details
    
    Die IP-Adresse des Routers ist das **IPv4 Default Gateway**
    
    ![property of network on windows 7](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. Systemeinstellungen -> Netzwerk

    2. Klicken Sie in der linken Spalte auf die Netzwerkverbindung. Bei einer Ethernet-Verbindung wird die IP-Adresse des Routers angezeigt.

    ![router ip of ethernet on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Bei einer Wi-Fi-Verbindung klicken Sie auf die Schaltfläche "Advanced..." und dann oben im Fenster auf die Registerkarte "TCP/IP". Die IP-Adresse des Routers wird angezeigt.

    ![router ip of Wi-Fi on mac os](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Einstellungen -> Wi-Fi
    2. Tippen Sie auf das Informationssymbol (blaues i in einem Kreis) des aktuell verbundenen Wi-Fi. Die IP-Adresse des Routers wird angezeigt.

    ![router ip address on iphone](https://static.gl-inet.com/docs/router/en/3/tutorials/cannot_access_web_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Dies variiert je nach Android-Gerät.

    1. Einstellungen -> Network & internet
    2. Tippen Sie auf Wi-Fi und suchen Sie das Netzwerk, mit dem Sie verbunden sind. Klicken Sie dann auf das Einstellungssymbol, um dessen Einstellungen zu verwalten.
    3. Tippen Sie auf das Dropdown-Menü Advanced. Wenn Ihnen dort Optionen für Static oder Dynamic IPs angeboten werden, wählen Sie Static.
    4. In jedem Fall sollten Sie die IP-Adresse Ihres Routers unter Gateway sehen.

### Auf die IP-Adresse des Routers zugreifen

1. Verwenden Sie für eine bessere Kompatibilität Chrome/Edge/Safari, um auf das Admin Panel Ihres Routers zuzugreifen.

2. Um Probleme durch Browser-Cache und Erweiterungen zu vermeiden, öffnen Sie bitte ein Inkognito-Fenster und versuchen Sie dann erneut, auf die IP-Adresse des Routers zuzugreifen.

3. Deaktivieren Sie sämtliche VPN- oder Proxy-Software, einschließlich Tailscale und ZeroTier.

4. Wenn Sie ein Mobiltelefon verwenden, schalten Sie bitte die mobilen Daten aus.

    Einige Smartphones trennen die Verbindung zum Wi-Fi des Routers und verwenden stattdessen mobile Daten, wenn sie erkennen, dass der Router kein Internet hat. Wenn die Verbindung zum Router getrennt wird, ist jedoch kein Zugriff auf das web Admin Panel möglich.

5. Wenn die oben genannten Schritte fehlschlagen, versuchen Sie, den Router über [Reset](repair_network_or_reset_firmware.md#reset-to-factory) auf die Werkseinstellungen zurückzusetzen.

6. Wenn das Zurücksetzen nicht funktioniert, versuchen Sie [Unbrick via uboot](debrick.md).

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
