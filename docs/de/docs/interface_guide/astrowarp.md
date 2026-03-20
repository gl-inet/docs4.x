# AstroWarp

**Hinweis**: Dieser Leitfaden stellt die neue Version von AstroWarp vor, die derzeit auf **Flint 3 (GL-BE9300)** und **Slate 7 (GL-BE3600)** mit den Firmware-Versionen v4.8.4 bzw. v4.8.3 verfügbar ist. 

Für andere Modelle finden Sie weitere Informationen unter [diesem Link](https://docs.astrowarp.net/){target="_blank"}.

---

AstroWarp ist eine erweiterte Netzwerkfunktion, die in GL.iNet-Router integriert ist. Sie ermöglicht nahtlosen Fernzugriff auf Ihr Heimnetzwerk ohne Registrierung oder Anmeldung. Durch das AmneziaWG-Protokoll mit integrierter Datenverkehrsverschleierung bleibt Ihre Verbindung stabil und sicher, was AstroWarp ideal für zuverlässigen Fernzugriff unterwegs macht.

Benutzer können ein AstroWarp-Netzwerk direkt über das Admin-Panel des GL.iNet-Routers einrichten. Koppeln Sie Ihre Router einfach mit einem Zugangscode, und schon können Sie Ihren Reiserouter in wenigen Sekunden sicher mit Ihrem Heimnetzwerk verbinden.

**Hinweis:** 

1. Es wird nicht empfohlen, AstroWarp gleichzeitig mit einer der folgenden Funktionen zu verwenden, da dies zu Routing-Konflikten führen kann: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Wenn AstroWarp aktiviert ist, kann der `Network Mode` nicht verwendet werden.

## Schnelle Einrichtung

Im folgenden Beispiel verwenden wir **Flint 3 (GL-BE9300)** und **Slate 7 (GL-BE3600)**, um ein AstroWarp-Netzwerk einzurichten. 

Flint 3 fungiert als Heimrouter, während Slate 7 als Reiserouter arbeitet, der den Netzwerkverkehr für den Internetzugang zurück zu Flint 3 leitet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Hinweis**: Jeder GL.iNet-Router verfügt für AstroWarp-Netzwerke über **10 GB kostenlose Daten pro Monat**. Geräte in einem AstroWarp-Netzwerk verwenden die Daten des Heimrouters, um auf das Internet zuzugreifen. Bei Bedarf können Sie auf den AstroWarp+-Tarif mit unbegrenztem Datenvolumen upgraden.
 
1. Konfigurieren Sie Flint 3 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Flint 3 an und wechseln Sie zur Seite **INTERNET**. Verbinden Sie den Router über eine der unterstützten Internetzugangsmethoden mit dem Internet: Ethernet, Repeater, Tethering und Cellular.

    Wie unten gezeigt, ist der Heimrouter Flint 3 per Ethernet-Kabel mit dem ISP-Modem (Hong Kong Broadband Network Ltd) verbunden.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Zugangscode generieren.

    Navigieren Sie im Web-Admin-Panel von Flint 3 zu **CLOUD SERVICES** -> **AstroWarp**. Klicken Sie auf **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Es wird ein **Access Code** generiert. Kopieren Sie diesen Code zur späteren Verwendung.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Konfigurieren Sie Slate 7 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Slate 7 an und wechseln Sie zur Seite **INTERNET**. Verbinden Sie den Router über eine der unterstützten Internetzugangsmethoden mit dem Internet: Ethernet, Repeater, Tethering und Cellular.

    Wie unten gezeigt, ist der Reiserouter Slate 7 mit dem persönlichen Hotspot eines iPhone 15 Pro verbunden (Standort Shenzhen, unter Verwendung des Netzes von China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Zugangscode eingeben.

    Navigieren Sie im Web-Admin-Panel von Slate 7 zu **CLOUD SERVICES** -> **AstroWarp**. Klicken Sie auf **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Geben Sie den in Schritt 2 erhaltenen Zugangscode ein.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Warten Sie, bis die Verifizierung abgeschlossen ist.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    Anschließend wird erfolgreich eine Verbindung mit dem Heimrouter Flint 3 hergestellt. Sie können nun sicher über Ihr Heimnetzwerk im Internet surfen.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    Im Web-Admin-Panel von Flint 3 wird ebenfalls der Verbindungsstatus angezeigt, wie unten dargestellt.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Konnektivität testen

1. Verbinden Sie einen Laptop oder ein Smartphone mit dem Wi-Fi des Reiserouters Slate 7.

2. Öffnen Sie einen Browser und rufen Sie [ipcheck.ing](https://ipcheck.ing/){target="_blank"} oder eine andere Website zur IP-Adressabfrage auf.

    Es wird die öffentliche IP-Adresse von Flint 3 angezeigt. Das zeigt, dass Slate 7 über Ihren Heimrouter Flint 3 auf das Internet zugreift.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Trennen Sie die AstroWarp-Verbindung auf Slate 7 und aktualisieren Sie anschließend die Webseite, um die IP-Abfrage erneut auszuführen. 

    Es wird die öffentliche IP-Adresse von Slate 7 angezeigt. Das zeigt, dass Slate 7 über sein lokales Netzwerk auf das Internet zugreift.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Tarif upgraden

Jeder GL.iNet-Router verfügt für AstroWarp-Netzwerke über **10 GB kostenlose Daten pro Monat**. Geräte in einem AstroWarp-Netzwerk verwenden die Daten des Heimrouters, um auf das Internet zuzugreifen. 

Bei Bedarf können Sie auf den Tarif **AstroWarp+** mit unbegrenztem Datenvolumen upgraden.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
