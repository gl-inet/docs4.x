# GoodPAS

**Hinweis**: Diese Funktion wurde mit Firmware v4.10 eingeführt; dabei wurde AstroWarp in GoodPAS umbenannt. Wenn auf Ihrem Gerät eine ältere Firmwareversion ausgeführt wird, lesen Sie [AstroWarp](./astrowarp.md).

---

Navigieren Sie auf der linken Seite des Web-Admin-Panels zu **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS ist eine erweiterte Fernzugriffslösung, die in das GL.iNet Router SDK integriert ist. Sie verwendet das AmneziaWG-Protokoll mit integrierter Datenverkehrsverschleierung und stellt stabile, sichere Verbindungen für zuverlässigen Fernzugriff jederzeit und überall bereit.

Diese Funktion ermöglicht nahtlosen Fernzugriff auf Ihr Heimnetzwerk. Sie können Geräte direkt im Web-Admin-Panel über einen dynamischen Zugriffscode einrichten und koppeln. Dadurch wird in wenigen Sekunden eine sichere Verbindung zwischen Ihrem Reiserouter und Ihrem Heimnetzwerk hergestellt, ohne dass eine Registrierung oder Anmeldung erforderlich ist.

**Hinweis**:

1. Es wird nicht empfohlen, GoodPAS gleichzeitig mit einer der folgenden Funktionen zu verwenden, da dies zu Routing-Konflikten führen kann: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.

2. Wenn GoodPAS aktiviert ist, kann Network Mode nicht verwendet werden.

## Schnelleinrichtung

Im folgenden Beispiel verwenden wir **Flint 3 (GL-BE9300)** und **Mango 2 (GL-MG1300)**, um ein GoodPAS-Netzwerk einzurichten.

Flint 3 fungiert als Heimrouter, während Mango 2 als Reiserouter arbeitet und den Netzwerkverkehr für den Internetzugang zurück zu Flint 3 leitet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Konfigurieren Sie Flint 3 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Flint 3 an und öffnen Sie die Seite INTERNET. Verbinden Sie den Router über eine der unterstützten Methoden mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

    Wie unten gezeigt, ist der Heimrouter Flint 3 über ein Ethernet-Kabel mit dem Modem des Internetanbieters (Hong Kong Broadband Network Ltd) verbunden.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Generieren Sie einen Zugriffscode.

    Navigieren Sie im Web-Admin-Panel von Flint 3 zu **CLOUD SERVICES** -> **GoodPAS**. Klicken Sie auf **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Ein Access Code wird generiert. Kopieren Sie diesen Code zur späteren Verwendung.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Konfigurieren Sie Mango 2 für den Internetzugang.

    Melden Sie sich im Web-Admin-Panel von Mango 2 an und öffnen Sie die Seite INTERNET. Verbinden Sie den Router über eine der unterstützten Methoden mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

    Wie unten gezeigt, ist der Reiserouter Mango 2 mit dem persönlichen Hotspot eines iPhone 17 verbunden (Standort Shenzhen, über das Netz von China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Geben Sie den Zugriffscode ein.

    Navigieren Sie im Web-Admin-Panel von Mango 2 zu **CLOUD SERVICES** -> **GoodPAS**. Klicken Sie auf **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Geben Sie den in Schritt 2 erhaltenen Zugriffscode ein.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Warten Sie, bis die Überprüfung abgeschlossen ist.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    Anschließend wird die Verbindung zum Heimrouter Flint 3 erfolgreich hergestellt. Sie können nun sicher über Ihr Heimnetzwerk im Internet surfen.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Im Web-Admin-Panel von Flint 3 wird ebenfalls der Verbindungsstatus angezeigt, wie unten dargestellt.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Konnektivität testen

1. Verbinden Sie einen Laptop oder ein Smartphone mit dem WLAN des Reiserouters Mango 2.

2. Öffnen Sie einen Browser und rufen Sie [ipcheck.ing](https://ipcheck.ing/){target="_blank"} oder eine andere Website zur IP-Adressabfrage auf.

    Die öffentliche IP-Adresse von Mango 2 wird angezeigt. Dies weist darauf hin, dass Mango 2 über Ihren Heimrouter Flint 3 auf das Internet zugreift.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Trennen Sie die GoodPAS-Verbindung auf Mango 2 und aktualisieren Sie anschließend die Webseite, um die IP-Abfrage erneut zu senden.

    Die öffentliche IP-Adresse von Mango 2 wird angezeigt. Dies weist darauf hin, dass Mango 2 über sein lokales Netzwerk auf das Internet zugreift.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **F: Welches Format hat der dynamische Zugriffscode und wie lange ist er gültig?**

    A: Er besteht aus acht Zeichen, einer Kombination aus Zahlen und Großbuchstaben, und ist zehn Minuten lang gültig.

2. **F: Was geschieht mit dem Reiserouter, wenn ich die Verbindung auf dem Heimrouter beende?**

    A: Der Reiserouter wird getrennt und verbleibt ohne Netzwerkzugang im Status „Ausstehend“. Sobald der Heimrouter die Verbindung wieder aufnimmt, kann sich der Reiserouter automatisch erneut verbinden, ohne dass der Zugriffscode erneut eingegeben werden muss.

3. **F: In welchen Situationen wechselt der Reiserouter in den Status „Ausstehend“?**

    A: Der Reiserouter wechselt in den Status „Ausstehend“, wenn beim Heimrouter eine der folgenden Bedingungen eintritt:

    - Die GoodPAS-Verbindung wird beendet.
    - Die Internetverbindung fällt aus.

4. **F: Was bewirkt die Schaltfläche Reset oben rechts?**

    A: Sie löscht alle autorisierten Geräte und kehrt zur Seite zur Auswahl der Routerrolle zurück, damit die Rolle erneut ausgewählt werden kann.

5. **F: Was geschieht mit dem Reiserouter, wenn ich GoodPAS auf dem Heimrouter zurücksetze?**

    A: Sobald der Heimrouter zurückgesetzt wird, werden die aus der Ferne verbundenen Geräte vom GoodPAS-Netzwerk getrennt und verwenden für den Internetzugang wieder ihr lokales Netzwerk.

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
