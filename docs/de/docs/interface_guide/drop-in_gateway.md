# Drop-in Gateway

Gehen Sie auf der linken Seite des webbasierten Admin Panels zu **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway ist eine Erweiterungsfunktion, mit der sich ein vorhandener Hauptrouter erweitern lässt, ohne ihn ersetzen oder neu konfigurieren zu müssen. Wenn der GL.iNet-Router per Ethernet-Kabel mit dem Hauptrouter verbunden wird, können Benutzer dem bestehenden Netzwerk zum Beispiel erweiterte Funktionen hinzufügen:

- Werbung mit AdGuard Home filtern
- VPN-Client aktivieren
- Verschlüsseltes DNS verwenden

Es wird empfohlen, einen leistungsstärkeren Router oder ein Sicherheits-Gateway mit ausreichend Arbeitsspeicher zu verwenden (z. B. GL-MT2500, GL-MT5000) und bei Bedarf zusätzliche Werkzeuge für Traffic-Weiterleitung und -Steuerung zu installieren.

## Netzwerktopologie

Drop-in Gateway arbeitet als zwischengeschaltetes Netzwerksystem und leitet den Datenverkehr der Client-Geräte zunächst zur Verarbeitung durch den GL.iNet-Router, bevor er über den Hauptrouter weitergeleitet wird. Dabei bleiben bestehende Netzwerkeinstellungen wie SSID und Passwort erhalten, sodass alle verbundenen Geräte ohne Unterbrechung online bleiben. Gleichzeitig können Sie den Netzwerkverkehr für alle oder nur bestimmte Client-Geräte nach Bedarf verwalten.

![drop-in gateway mode typology](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

Die obige Abbildung besteht aus zwei Arten von Linien: grauen Linien sowie grünen Linien mit drei Pfeilen, die jeweils mit einer Nummer versehen sind.

1. **Gray lines** zeigen die physische Verbindungsstruktur: Client-Geräte (z. B. Computer oder Laptop) sind mit dem Hauptrouter verbunden, und der LAN-Port des Hauptrouters ist per Ethernet-Kabel mit dem WAN-Port des GL.iNet-Routers verbunden (auf dem Drop-in Gateway aktiviert ist).

2. **Green lines** zeigen den schrittweisen Übertragungsweg der Daten, wenn Drop-in Gateway aktiv ist. Die nummerierten Pfeile kennzeichnen die Reihenfolge des Datenflusses:

    1. Der Datenverkehr der Client-Geräte wird zunächst zum Hauptrouter geleitet.

    2. Der Hauptrouter leitet den Datenverkehr zur Verarbeitung an den GL.iNet-Router weiter (z. B. Werbefilterung oder VPN-Verschlüsselung).

    3. Nach der Verarbeitung wird der Datenverkehr zurück an den Hauptrouter gesendet, der die Daten dann entweder an die ursprünglichen Client-Geräte liefert oder ins Internet weiterleitet.

## Einrichtung

Für unterschiedliche Anwendungsszenarien gibt es zwei Bereitstellungsmodi: Entweder werden alle Client-Geräte über Drop-in Gateway ins Netzwerk eingebunden oder nur bestimmte Client-Geräte.

Im folgenden Beispiel lautet die Gateway-Adresse des Hauptrouters `192.168.1.1`.

### Alle Geräte werden über Drop-in Gateway ins Netzwerk eingebunden {all-devices-managed-by-the-drop-in-gateway}

1. Verbinden Sie den LAN-Port des Hauptrouters per Ethernet-Kabel mit dem WAN-Port des GL.iNet-Routers.

2. Melden Sie sich am webbasierten Admin Panel Ihres GL.iNet-Routers an, aktivieren Sie Drop-in Gateway, und das System erzeugt automatisch die passenden Konfigurationsparameter.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** bezeichnet die WAN-IP-Adresse Ihres GL.iNet-Routers, die dynamisch vom Hauptrouter vergeben wird. Diese WAN-IP finden Sie im Ethernet-Abschnitt der Seite [INTERNET](internet_ethernet.md).

    - Die Felder **Gateway** und **DNS Server 1** werden standardmäßig automatisch mit der IP-Adresse des Hauptrouters ausgefüllt. Falls diese Parameter falsch gesetzt sind, können Sie sie manuell anpassen.

    Notieren Sie sich diese IP-Adresse, da Sie sie in den folgenden Schritten benötigen.

    Wählen Sie die erste Konfigurationsmethode und klicken Sie auf **Apply**.

3. Melden Sie sich am webbasierten Admin Panel Ihres Hauptrouters an.

    ??? "GL.iNet"

        Wenn Ihr Hauptrouter ein GL.iNet-Router ist und Firmware v4.2 oder neuer verwendet, gehen Sie wie folgt vor.

        Gehen Sie im webbasierten Admin Panel zu NETWORK -> LAN -> DHCP Server -> Advanced

        ![glinet lan advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        Tragen Sie als DHCP Gateway die IP Address aus Schritt 2 ein, z. B. `192.168.1.23`, und klicken Sie dann auf **Apply**.

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![glinet lan, dhcp gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Wenn Ihr Hauptrouter ein TP-Link-Router ist, führen Sie die folgenden Schritte aus (hier am Beispiel eines TP-LINK Archer C3150).

        Melden Sie sich an der TP-Link-Administrationsseite an, gehen Sie zu **Advanced** -> **Network** -> **DHCP Server** und deaktivieren Sie anschließend **DHCP**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Klicken Sie anschließend auf **Save**.

        ![tplink admin, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Wenn Ihr Hauptrouter ein Linksys-Router ist, führen Sie die folgenden Schritte aus (hier am Beispiel eines Linksys WHW01).

        Melden Sie sich an der Linksys-Administrationsseite an und navigieren Sie zu **Router Settings** -> **Connectivity**.

        ![linksys admin, connectivity](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Klicken Sie auf die Registerkarte **Local Network**, deaktivieren Sie den **DHCP Server** und klicken Sie anschließend auf **OK**.

        ![linksys admin, local network, disable dhcp](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        Es erscheint ein Warnhinweis. Klicken Sie auf **OK**.

        ![linksys admin, apply changes](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Others"

        Melden Sie sich am Admin Panel des Hauptrouters an, um dessen DHCP-Server zu deaktivieren. Sie können dazu das Benutzerhandbuch des jeweiligen Herstellers verwenden oder den Support kontaktieren.

4. Kehren Sie zum GL.iNet-Router zurück und richten Sie Funktionen wie [AdGuard Home](adguardhome.md), [verschlüsseltes DNS](dns.md), [WireGuard Client](wireguard_client.md) und [OpenVPN Client](openvpn_client.md) ein.

### Bestimmte Geräte werden über Drop-in Gateway ins Netzwerk eingebunden {some-devices-managed-by-the-drop-in-gateway}

1. Verbinden Sie den LAN-Port des Hauptrouters per Ethernet-Kabel mit dem WAN-Port des GL.iNet-Routers.

2. Melden Sie sich am webbasierten Admin Panel Ihres GL.iNet-Routers an, aktivieren Sie Drop-in Gateway, und das System erzeugt automatisch die passenden Konfigurationsparameter.

    ![drop-in gateway generated settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** bezeichnet die WAN-IP-Adresse Ihres GL.iNet-Routers, die dynamisch vom Hauptrouter vergeben wird. Diese WAN-IP finden Sie im Ethernet-Abschnitt der Seite [INTERNET](internet_ethernet.md).

    - Die Felder **Gateway** und **DNS Server 1** werden standardmäßig automatisch mit der IP-Adresse des Hauptrouters ausgefüllt. Falls diese Parameter falsch gesetzt sind, können Sie sie manuell anpassen.

    Notieren Sie sich diese IP-Adresse, da Sie sie in den folgenden Schritten benötigen.

    Wählen Sie die zweite Konfigurationsmethode und klicken Sie auf **Apply**.

3. Legen Sie auf dem Gerät, das die Drop-in-Gateway-Funktion nutzen soll, Gateway und DNS auf die IP-Adresse fest, die auf der Drop-in-Gateway-Seite angezeigt wird.

    ??? "Windows"

        Hier ist ein Beispiel mit Windows 11; unter Windows 10 ist es ähnlich. Stellen Sie sicher, dass Ihr PC mit dem Hauptrouter verbunden ist. Es wird hier davon ausgegangen, dass Ihr Computer per Netzwerkkabel mit dem Hauptrouter verbunden ist; bei einer Wi-Fi-Verbindung ist die Einrichtung ähnlich.

        1. Öffnen Sie Settings.

        2. Klicken Sie auf **Network & Internet**.

        3. Klicken Sie auf die Registerkarte **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Dort finden Sie die IP-Adresse dieses PCs. Klicken Sie im Abschnitt „IP assignment“ auf die Schaltfläche **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Wählen Sie die Option **Manual**. Aktivieren Sie den **IPv4**-Schalter.

        6. Setzen Sie **IP address** auf die IP-Adresse aus Schritt 4, **Subnet mask** auf `255.255.255.0` und sowohl **Gateway** als auch **Preferred DNS** auf die IP-Adresse, die auf der Drop-in-Gateway-Seite angezeigt wird.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Klicken Sie auf die Schaltfläche **Save**.

    ??? "Android"

        Hier ist ein Beispiel mit einem Samsung S21. Stellen Sie sicher, dass Ihr Smartphone mit dem Hauptrouter verbunden ist.

        1. Öffnen Sie Settings und tippen Sie auf Connections.

            ![settings connections](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Tippen Sie auf Wi-Fi.

            ![connection wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Tippen Sie auf das Zahnradsymbol der aktuellen SSID.

            ![wifi setting](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Tippen Sie auf **View more**.

            ![wifi settings, view more](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Tippen Sie auf **IP settings** und wählen Sie **Static**.

            ![ip settings](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![IP settings, static](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. Setzen Sie **Gateway** und **DNS 1** auf die IP-Adresse, die auf der Drop-in-Gateway-Seite angezeigt wird, und tippen Sie anschließend auf **Save**.

            ![set gateway and dns ip](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Hier ist ein Beispiel mit iOS 16.3 auf einem iPhone 8. Stellen Sie sicher, dass Ihr Smartphone mit dem Hauptrouter verbunden ist.

        1. Öffnen Sie Settings und tippen Sie auf Wi-Fi.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Tippen Sie auf die SSID.

            ![settings wifi](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Scrollen Sie nach unten. Dort sehen Sie, dass **Configure IP** auf **Automatic** steht. Notieren Sie sich **IP Address** und **Subnet Mask** für den nächsten Schritt.

            ![wifi ipv4](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Ändern Sie **Configure IP** zu **Manual**, setzen Sie **IP Address** und **Subnet Mask** auf die Werte aus dem vorherigen Schritt und tragen Sie bei **Router** die IP-Adresse ein, die auf der Drop-in-Gateway-Seite angezeigt wird. Klicken Sie anschließend auf **Save**.

            ![wifi ipv4 manual](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Tippen Sie auf **Configure DNS** und stellen Sie auf **Manual** um. Tippen Sie auf **Add Server**, setzen Sie die DNS-Server-IP-Adresse auf die auf der Drop-in-Gateway-Seite angezeigte IP-Adresse und tippen Sie dann auf **Save**.

            ![wifi dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![wifi set dns](https://static.gl-inet.com/docs/router/en/4/tutorials/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Kehren Sie zum webbasierten Admin Panel des GL.iNet-Routers zurück und richten Sie die gewünschten Funktionen ein, z. B. [AdGuard Home](adguardhome.md), [verschlüsseltes DNS](dns.md), [WireGuard Client](wireguard_client.md) und [OpenVPN Client](openvpn_client.md).

## Hinweise

1. Das Aktivieren von Drop-in Gateway erhöht die Netzwerklatenz.

2. Wenn Drop-in Gateway aktiviert ist, wird auch die Datenübertragung zwischen ausgewählten LAN-Geräten über das Drop-in Gateway geleitet. Die Bandbreite zwischen Hauptrouter und Drop-in Gateway wirkt sich daher auf die gesamte LAN-Bandbreite aus.

---

Verwandter Artikel:

- [Wie richtet man Drop-in Gateway auf einem GL.iNet-Router ein?](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
