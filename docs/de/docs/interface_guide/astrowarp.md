# AstroWarp

**Hinweis**: Dieser Leitfaden behandelt die neue Version von AstroWarp.

Das ältere AstroWarp war zwar im Web-Admin-Panel sichtbar, nutzte jedoch eine eigenständige AstroWarp-Plattform, um Remote-Netzwerkverbindungen herzustellen. Die Dokumentation zum älteren AstroWarp finden Sie [hier](https://docs.astrowarp.net/){target="_blank"}.

Im Gegensatz dazu ist das neue AstroWarp in das GL.iNet Router SDK integriert. Es verwendet das AmneziaWG-Protokoll mit integrierter Datenverkehrsverschleierung und bietet dadurch stabile und sichere Verbindungen für zuverlässigen Fernzugriff jederzeit und überall.

Diese Funktion ermöglicht nahtlosen Fernzugriff auf Ihr Heimnetzwerk. Sie können Geräte direkt im Web-Admin-Panel über einen dynamischen Zugriffscode einrichten und koppeln, sodass in nur wenigen Sekunden eine sichere Verbindung zwischen Ihrem Reiserouter und Ihrem Heimnetzwerk hergestellt wird – ganz ohne Registrierung oder Anmeldung.

**Hinweis:**

1. Es wird nicht empfohlen, AstroWarp gleichzeitig mit einer der folgenden Funktionen zu verwenden, da dies zu Routing-Konflikten führen kann: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Wenn AstroWarp aktiviert ist, kann der `Network Mode` nicht verwendet werden.

## Unterstützte Modelle

??? "Unterstützte Modelle"

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Hinweis**: Mit ※ gekennzeichnete Modelle unterstützen das integrierte AstroWarp in Beta-Firmware.

??? "Nicht unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Schnelleinrichtung

Im folgenden Beispiel verwenden wir **Flint 3 (GL-BE9300)** und **Slate 7 (GL-BE3600)**, um ein AstroWarp-Netzwerk einzurichten.

Flint 3 fungiert als Heimrouter, während Slate 7 als Reiserouter arbeitet, der den Netzwerkverkehr für den Internetzugang zurück zu Flint 3 leitet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Hinweis**: Jeder GL.iNet-Router verfügt für AstroWarp-Netzwerke über **10 GB kostenlose Daten pro Monat**. Geräte in einem AstroWarp-Netzwerk verwenden die Daten des Heimrouters für den Internetzugang. Bei Bedarf können Sie auf den Tarif AstroWarp+ mit unbegrenztem Datenvolumen upgraden.

1. Konfigurieren Sie Flint 3 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Flint 3 an und wechseln Sie zur Seite **INTERNET**. Verbinden Sie den Router über eine der unterstützten Methoden mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

    Wie unten gezeigt, ist der Heimrouter Flint 3 per Ethernet-Kabel mit dem ISP-Modem (Hong Kong Broadband Network Ltd) verbunden.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Generieren Sie einen Zugriffscode.

    Navigieren Sie im Web-Admin-Panel von Flint 3 zu **CLOUD SERVICES** -> **AstroWarp**. Klicken Sie auf **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Dadurch wird ein **Access Code** generiert. Kopieren Sie diesen Code für die spätere Verwendung.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Konfigurieren Sie Slate 7 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Slate 7 an und wechseln Sie zur Seite **INTERNET**. Verbinden Sie den Router über eine der unterstützten Methoden mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

    Wie unten gezeigt, ist der Reiserouter Slate 7 mit dem persönlichen Hotspot eines iPhone 15 Pro verbunden (Standort Shenzhen, über das Netz von China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Geben Sie den Zugriffscode ein.

    Navigieren Sie im Web-Admin-Panel von Slate 7 zu **CLOUD SERVICES** -> **AstroWarp**. Klicken Sie auf **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Geben Sie den in Schritt 2 erhaltenen Zugriffscode ein.

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

    Es wird die öffentliche IP-Adresse von Flint 3 angezeigt. Das bedeutet, dass Slate 7 über Ihren Heimrouter Flint 3 auf das Internet zugreift.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Trennen Sie die AstroWarp-Verbindung auf Slate 7 und aktualisieren Sie anschließend die Webseite, um die IP-Abfrage erneut auszuführen.

    Es wird die öffentliche IP-Adresse von Slate 7 angezeigt. Das bedeutet, dass Slate 7 über sein lokales Netzwerk auf das Internet zugreift.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Tarif upgraden

Jeder GL.iNet-Router verfügt für AstroWarp-Netzwerke über **10 GB kostenlose Daten pro Monat**. Geräte in einem AstroWarp-Netzwerk verwenden die Daten des Heimrouters für den Internetzugang.

Bei Bedarf können Sie auf den Tarif **AstroWarp+** mit unbegrenztem Datenvolumen upgraden.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
