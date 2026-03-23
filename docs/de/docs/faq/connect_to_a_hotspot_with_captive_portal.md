# Einen GL.iNet-Router mit öffentlichen Hotspots über ein Captive Portal verbinden







## Was ist ein Captive Portal?







Ein Captive Portal ist eine Webseite, bei der öffentliche Hotspots verlangen, dass Benutzer die Seite ansehen und mit ihr interagieren, bevor der Internetzugang freigeschaltet wird.







## Warum einen Router für öffentliche Hotspots verwenden?







* Öffentliches Wi-Fi ist nicht sicher







    Die Risiken von öffentlichem Wi-Fi können kaum überschätzt werden. Wenn Sie Ihren GL.iNet-Router mit öffentlichem Wi-Fi verbinden, können Sie sich direkt über das Admin-Panel des Routers bei Ihrem VPN-Konto anmelden. Dadurch werden alle verbundenen Geräte im lokalen Netzwerk automatisch verschlüsselt, sodass Sie nicht auf jedem einzelnen Gerät ein VPN einrichten müssen.







* Als Repeater verwenden, um Verbindungen mit mehreren Geräten zu ermöglichen







    Außerdem begrenzen manche öffentlichen Wi-Fi-Netzwerke (z. B. Hotel-Wi-Fi) den Zugriff beispielsweise auf zwei Geräte. Wenn Sie in einer Gruppe reisen, ist das unpraktisch. Stattdessen können Sie einen Reiserouter mit dem Hotel-Wi-Fi verbinden und ihn als Repeater verwenden, um ein Wi-Fi-Signal für alle Ihre Geräte auszustrahlen, einschließlich Laptops, Smartphones, Tablets usw. Das Hotel-Wi-Fi erkennt dann nur den Reiserouter als einzelnes Gerät, Sie können aber beliebig viele Geräte mit dem freien Wi-Fi verbinden.







## Wie verbindet man einen Router mit öffentlichen Hotspots über ein Captive Portal?







Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.







<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>







1. Verbinden Sie ein Smartphone oder einen Computer mit dem Router.







    Schalten Sie den Router ein. Suchen Sie auf Ihrem Smartphone oder Computer nach der SSID des Routers und geben Sie das Wi-Fi-Passwort ein. Die Standard-SSID und das Passwort sind auf der Unterseite des Routers aufgedruckt.







2. Melden Sie sich im Web-Admin-Panel Ihres Routers an.







    Öffnen Sie auf Ihrem Smartphone oder Computer einen Webbrowser und geben Sie die IP-Adresse des Routers (Standard-IP: `192.168.8.1`) in die Adressleiste ein. Sie können dann auf das Web-Admin-Panel des Routers zugreifen.







    Wenn Sie sich zum ersten Mal anmelden, wählen Sie eine Sprache aus und erstellen Sie ein Anmeldepasswort für das Web-Admin-Panel des Routers.







3. Verbinden Sie Ihren Router mit dem öffentlichen Hotspot. Lesen Sie dazu die Anleitung [Repeater](../interface_guide/internet_repeater.md/).







## Fehlerbehebung







Wenn Sie das Captive Portal nicht aufrufen können, hat Ihr Router möglicherweise keinen Zugriff auf das Internet. Versuchen Sie zur Fehlerbehebung bitte die folgenden Methoden.







### Methode 1: Public Hotspot Login Mode & Camouflage aktivieren







**Hinweis**: Diese beiden Funktionen sind nur in Firmware v4.6 und höher verfügbar.







Wenn Sie den Router mit einem öffentlichen Hotspot verbinden, kann das Aktivieren der folgenden Funktionen auf der Seite **Join Network** helfen, die Erfolgsrate der Verbindung zu verbessern.







![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}







- Auto-Enable Login Mode for Public Hotspots







    Wenn diese Option aktiviert ist, wechselt dieser Router automatisch in den Login Mode for Public Hotspots, wenn er erfolgreich mit einem Hotspot, aber nicht mit dem Internet verbunden ist. In diesem Modus werden einige Dienste angehalten und der DNS-Modus wird auf automatisch umgestellt, wodurch Ihre Netzwerkaktivitäten an den Hotspot-Anbieter (z. B. Hotel oder Einkaufszentrum) weitergegeben werden könnten.







- Enable Camouflage







    Wenn diese Option aktiviert ist, tarnt sich der Router als das Client-Gerät, mit dem Sie auf das Admin-Panel zugreifen, indem er die MAC-Adresse dieses Geräts emuliert.







---







### Methode 2: Router-Einstellungen ändern







1. Melden Sie sich im Web-Admin-Panel an und navigieren Sie zu NETWORK -> DNS. Stellen Sie sicher, dass **DNS Rebinding Attack Protection** deaktiviert ist und **Mode** auf **Automatic** gesetzt ist.







    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}







2. Navigieren Sie im Web-Admin-Panel zu VPN -> VPN Dashboard. Stellen Sie sicher, dass alle VPN-Verbindungen deaktiviert sind.







    **Für Firmware v4.7 und früher** wird die Seite wie unten dargestellt angezeigt.







    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}







    **Für Firmware v4.8 und höher** wird die Seite wie unten dargestellt angezeigt.







    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}







3. Navigieren Sie im Web-Admin-Panel zu APPLICATIONS -> AdGuard Home. Stellen Sie sicher, dass AdGuard Home deaktiviert ist.







    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}







4. Öffnen Sie einen Webbrowser und rufen Sie die Webseite des Captive Portals erneut auf oder aktualisieren Sie sie. Warten Sie eine Minute und prüfen Sie, ob automatisch zur Authentifizierungsseite des Captive Portals weitergeleitet wird.







    Wenn Sie ein Smartphone verwenden und Ihr Webbrowser nicht zum Captive Portal weiterleitet, schalten Sie das Wi-Fi Ihres Smartphones aus und wieder ein und verbinden Sie sich dann erneut mit dem Wi-Fi des Routers. Das Captive Portal sollte direkt nach Eingabe des Wi-Fi-Passworts erscheinen.







    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}







---







### Methode 3：MAC Clone







Einige Hotels begrenzen die Anzahl der Geräte, die jeder Gast mit dem Hotel-Wi-Fi verbinden kann, indem sie deren MAC-Adressen erkennen, und sie speichern die MAC-Adresse des Geräts, wenn es sich zum ersten Mal verbindet. In diesem Fall können Sie die MAC-Adresse, die Ihr Telefon für die Verbindung mit dem Hotel-Wi-Fi verwendet, auf den Router klonen, damit der Router diese MAC-Adresse für den Zugriff auf das Hotel-Wi-Fi nutzt.







1. Verbinden Sie Ihr Telefon mit dem Hotel-Wi-Fi. Suchen Sie die MAC-Adresse, die Ihr Telefon für die Verbindung mit dem Hotel-Wi-Fi verwendet.







    Hier ist ein Beispiel für ein iPhone (iOS 16.1.2): Gehen Sie zu Settings -> Wi-Fi -> Wählen Sie das Hotel-Wi-Fi aus, und Sie finden dort die Wi-Fi Address. Notieren Sie sich diese Adresse.







    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}







    Bei einigen älteren Modellen ist die MAC-Adresse möglicherweise nicht in den Wi-Fi-Einstellungen verfügbar. In diesem Fall verwendet das Gerät bei der Verbindung mit öffentlichem Wi-Fi möglicherweise seine echte MAC-Adresse. Diese finden Sie unter Settings > About (oder "About Phone").







2. Verbinden Sie Ihr Telefon oder Ihren Computer mit dem Router. Melden Sie sich im Web-Admin-Panel des Routers an und klonen Sie dann diese MAC-Adresse oder geben Sie sie manuell ein.







    **Für Firmware v4.5 und früher** wählen Sie bitte auf der linken Seite NETWORK -> MAC Address aus.







    Wählen Sie Manual Mode, geben Sie die in Schritt 1 ermittelte MAC-Adresse ein und klicken Sie auf Apply.







    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}







    **Für Firmware v4.6 und höher** wählen Sie bitte auf der linken Seite INTERNET -> Repeater und klicken Sie auf Modify.







    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}







    Wechseln Sie im Pop-up-Fenster **MAC Mode** zu Clone, geben Sie die MAC-Adresse manuell ein und klicken Sie auf Apply.







    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}







3. Möglicherweise ist ein Neustart des Routers erforderlich, damit die Änderung wirksam wird.







---







### Methode 4：Bitten Sie das Hotelpersonal um Hilfe







Einige Hotels haben sehr strenge Verifizierungsrichtlinien für ihre Netzwerke. Wenn keine der oben genannten Methoden funktioniert, bitten Sie das Hotelpersonal, die MAC-Adresse Ihres Routers (verwenden Sie die werkseitige Standard-MAC-Adresse, nicht eine zufällige) direkt zur Whitelist des Hotelnetzwerks hinzuzufügen.







---







Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.



