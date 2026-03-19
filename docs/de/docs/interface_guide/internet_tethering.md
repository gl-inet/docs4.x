# Verbindung zum Internet per USB-Tethering herstellen

Wenn Sie die Netzwerkverbindung Ihres Smartphones per USB-Kabel mit dem Router teilen, nennt man das Tethering. Ein hostloses Modem arbeitet während seiner Einrichtung ebenfalls im Tethering-Modus.

**Hinweis:** Einige Mobilfunkanbieter begrenzen Tethering oder berechnen dafür zusätzliche Gebühren. Wir empfehlen, dies bei Ihrem Anbieter zu prüfen.

## Einrichtung

=== "iPhone"

    1. Schließen Sie ein iPhone mit einem USB-Kabel an den USB-Port des Routers an. Ein Systemdialog fragt, ob dem Gerät vertraut werden soll. Tippen Sie auf **Trust**, um fortzufahren.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Gehen Sie auf dem iPhone zu **Settings** -> **Personal Hotspot**. Aktivieren Sie **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Verbinden Sie einen Computer oder ein anderes Telefon mit dem Router, melden Sie sich dann am webbasierten Admin Panel Ihres Routers an, gehen Sie zum Abschnitt **INTERNET** -> **Tethering** und klicken Sie auf **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        Wenn Sie erweiterte Einstellungen wie TTL, HL und MTU festlegen müssen, klicken Sie auf **Advanced**, passen Sie diese Einstellungen an und klicken Sie dann auf **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        Die Verbindung wird nun aufgebaut.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Sobald die Verbindung hergestellt ist, wird der Status des persönlichen Hotspots (z. B. die Anzahl verbundener Geräte) in der Statusleiste oben auf dem Telefon angezeigt.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Das webbasierte Admin Panel zeigt ebenfalls den Status der Tethering-Verbindung an.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Schließen Sie ein Android-Telefon mit einem USB-Kabel an den USB-Port des Routers an. Es kann ein Systemdialog erscheinen, der nach den USB-Einstellungen fragt. Wählen Sie bei entsprechender Aufforderung **USB Tethering** oder **File Transfer**.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Gehen Sie auf Ihrem Telefon zu **Settings** -> **Network & Internet** -> **Personal Hotspot**. Aktivieren Sie **Personal Hotspot** oder **USB Tethering**.
    
        (Die Schritte zum Aktivieren von USB Tethering unterscheiden sich je nach Marke. Prüfen Sie die Einstellungen Ihres Geräts, um die genaue Position zu finden, und wenden Sie sich bei Bedarf an den Support des Herstellers.)

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Verbinden Sie einen Computer oder ein anderes Telefon mit dem Router, melden Sie sich dann am webbasierten Admin Panel Ihres Routers an, gehen Sie zum Abschnitt **INTERNET** -> **Tethering** und klicken Sie auf **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        Wenn Sie erweiterte Einstellungen wie TTL, HL und MTU festlegen müssen, klicken Sie auf **Advanced**, passen Sie diese Einstellungen an und klicken Sie dann auf **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        Die Verbindung wird nun aufgebaut.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Sobald die Verbindung hergestellt ist, wird der Status des persönlichen Hotspots (z. B. die Anzahl verbundener Geräte) in der Statusleiste oben auf dem Telefon angezeigt.

        Das webbasierte Admin Panel zeigt ebenfalls den Status der Tethering-Verbindung an.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Die offizielle Android-Dokumentation finden Sie unter [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Warnung

Wenn kein Internetzugang verfügbar ist, wird der entsprechende Warnhinweis angezeigt:

**"The interface is connected, but the Internet can't be accessed."**

Lösungen:

1. Prüfen Sie, ob das Smartphone Internetzugang hat.

2. Gehen Sie zur Seite [Multi-WAN](multi-wan.md), um zu prüfen, ob der Internetzugang verfügbar ist.

## Fehlerbehebung

Wenn die Verbindung fehlschlägt, versuchen Sie die folgenden Schritte zur Fehlerbehebung:
    
- Verwenden Sie das originale Netzteil des Routers.
- Ziehen Sie das USB-Kabel ab und stecken Sie es erneut ein.
- Verwenden Sie ein anderes USB-Kabel. Achten Sie darauf, dass es Datenübertragung unterstützt (nicht nur Laden).
- Schalten Sie „USB Tethering“ mehrmals aus und wieder ein (bei Android-Telefonen).
- Schalten Sie „Allow Others to Join“ mehrmals aus und wieder ein (beim iPhone).
- Starten Sie Ihr Smartphone neu und versuchen Sie es erneut.

---

Verwandte Artikel

- [Internetseite](internet.md)
- [Wie legt man die Priorität der einzelnen Internetzugriffsmethoden fest?](multi-wan.md)
- [Wie richtet man den Lastenausgleich ein, wenn mehrere Internetzugriffsmethoden gleichzeitig verwendet werden?](multi-wan.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
