# Wie erlaubt man den Zugriff auf das WAN, wenn der VPN-Client aktiviert ist?

Wenn auf GL.iNet-Routern der VPN-Client aktiviert ist, können LAN-Geräte im standardmäßigen Global Mode nicht auf lokale WAN-Geräte oder -Dienste zugreifen. Der Grund ist, dass der gesamte Datenverkehr aus dem LAN über den VPN-Tunnel statt über das vorgelagerte Netzwerk (WAN) geleitet wird, um DNS-Lecks zu vermeiden.

Dieses Tutorial beschreibt die Schritte, mit denen lokale WAN-Dienste (z. B. Drucker, NAS usw.) für die LAN-Geräte des VPN-Clients erreichbar werden.

![allow acdess wan diagram](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Für Firmware v4.7 und früher

Melden Sie sich am webbasierten Admin Panel Ihres VPN-Clients an und gehen Sie zu **VPN** -> **VPN Dashboard** -> **VPN Client**. Klicken Sie oben rechts auf **Global Options**.

![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Aktivieren Sie **Allow Access WAN** und klicken Sie auf **Apply**.

![allow access](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Wenn diese Option aktiviert ist, können Client-Geräte auch bei aktiver VPN-Verbindung weiterhin auf WAN-Dienste im vorgelagerten Subnetz zugreifen, z. B. auf Drucker, NAS usw.

## Für Firmware v4.8 und höher

Die Option **Allow Access WAN** wurde in Firmware v4.8 aus dem VPN Dashboard entfernt. Der Zugriff auf das lokale WAN lässt sich jedoch weiterhin über eine VPN-Richtlinie umsetzen.

Führen Sie dazu die folgenden Schritte aus.

1. Melden Sie sich am webbasierten Admin Panel Ihres VPN-Clients an und gehen Sie zu **VPN** -> **VPN Dashboard**.

    Klicken Sie oben rechts auf den Modus.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Wechseln Sie zu **Policy Mode** und klicken Sie auf **Apply**.

    ![switch mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    Die Seite wird aktualisiert und anschließend wie unten dargestellt angezeigt.

    ![policy mode](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Klicken Sie auf das mittlere Feld, um das Tunnel-Ziel festzulegen.

    ![tunnel target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Wählen Sie **Exclude Speficied Domain / IP**, geben Sie das WAN-Subnetz Ihres Routers ein und klicken Sie dann auf **Apply**.

    Dadurch wird sichergestellt, dass der gesamte Datenverkehr zum WAN-Subnetz über das lokale WAN und nicht über den VPN-Tunnel geleitet wird.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    Hier verwenden wir das Subnetz `192.168.0.1/24` als Beispiel. Geben Sie dieses Subnetz ein und übernehmen Sie die Einstellung; der VPN-Tunnel wird dann wie unten dargestellt angezeigt.

    ![exclude target apply](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Wie erkenne ich das WAN-Subnetz meines GL.iNet-Routers?"
    
        Das WAN-Subnetz eines GL.iNet-Routers finden Sie normalerweise auf der Seite INTERNET. Es wird durch das vorgelagerte Gerät bestimmt, mit dem die WAN-Schnittstelle des Routers verbunden ist (z. B. ein ISP-Modem oder ein Upstream-Gateway).

        Wenn Ihr Router beispielsweise als sekundärer Router arbeitet (sein WAN-Port also mit einem anderen lokalen Netzwerk verbunden ist, etwa mit einem ISP-Modem oder dem LAN-Port eines Hauptrouters) und seine WAN-IP `192.168.1.165`, das Gateway `192.168.1.1` und die Subnetzmaske `255.255.255.0` lautet, dann ist das zugehörige WAN-Subnetz `192.168.1.0/24`. Das ist zugleich das LAN-Subnetz des vorgelagerten Geräts.

        ![check wan subnet](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Hinweis**: Die Präfixlänge von `192.168.1.0/24` ist `24` und entspricht der Subnetzmaske `255.255.255.0`. Wenn die WAN-Subnetzmaske Ihres Routers nicht `255.255.255.0` ist, lautet die Präfixlänge Ihres WAN-Subnetzes nicht `/24`. Ermitteln Sie das WAN-Subnetz daher bitte anhand der tatsächlichen WAN-Konfiguration.

3. Klicken Sie auf das rechte Feld, um die Tunnel-Aktion festzulegen (also ob das VPN verwendet wird oder nicht).

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Wählen Sie **Use VPN** und anschließend eine VPN-Konfigurationsdatei aus. Klicken Sie dann auf **Apply**.
    
    Wenn noch keine Konfiguration verfügbar ist, laden Sie zuerst eine hoch, um Ihren Router als VPN-Client einzurichten. Kehren Sie dann auf diese Seite zurück, wählen Sie Use VPN und eine VPN-Konfigurationsdatei aus und klicken Sie auf Apply.

    ![exclude target](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Schalten Sie den Schalter oben rechts ein, um diesen VPN-Tunnel zu aktivieren. Die Verbindung wird daraufhin aufgebaut.

    ![enable vpn](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Warten Sie einige Minuten. Sobald die Verbindung erfolgreich hergestellt wurde, wird die Anzeige grün.

    ![vpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Prüfen Sie Ihre öffentliche IP, um die VPN-Verbindung zu testen. Öffnen Sie dazu zum Beispiel einen Browser und rufen Sie [whatismyip](https://whatismyipaddress.com/){target="_blank"} auf. Dort werden Ihre öffentliche IP-Adresse und Ihr Standort angezeigt, wie unten dargestellt.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Greifen Sie auf Geräte oder Dienste im WAN-Subnetz zu und prüfen Sie, ob der Zugriff erfolgreich ist.

    Sie können die Erreichbarkeit mit dem Befehl `ping` testen.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
