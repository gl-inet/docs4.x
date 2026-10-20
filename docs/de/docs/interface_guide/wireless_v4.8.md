# WLAN (Firmware v4.8 und früher) {#wireless-firmware-v48-and-earlier}

Der Inhalt dieser Seite basiert auf Firmwareversion v4.8.x und früher. Wenn auf Ihrem Gerät eine andere Firmwareversion ausgeführt wird, verwenden Sie die folgende Auswahl, um zur entsprechenden Anleitung zu wechseln.

<div class="gl-link-select" data-label="Firmwareversion" data-placeholder="Firmware v4.8 und früher" markdown="1">

- [Firmware v4.9 und höher](wireless.md)

</div>

---


Gehen Sie in der Web-Adminoberfläche auf der linken Seite zu **WIRELESS**.

Auf der Seite "Wireless" können Sie separate Wi‑Fi-Netzwerke konfigurieren, einschließlich 2,4 GHz, 5 GHz, 6 GHz und MLO Wi‑Fi (die Verfügbarkeit variiert je nach Modell). Jedes Band kann flexibel als Main Wi‑Fi oder Gastnetzwerk eingerichtet werden.

**Hinweis**: Einige Modelle unterstützen kein 5-GHz-Wi‑Fi, z. B. GL-MT300N-V2 (Mango), GL-X300B (Collie) und GL-XE300 (Puli); einige verfügen über keine Wi‑Fi-Funktion, z. B. GL-MT5000 (Brume 3) und GL-MT2500/GL-MT2500A (Brume 2).

## MLO Wi‑Fi {#mlo-wi-fi}

| Unterstützte Modelle            |           |
| :------------------------------ | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)        | √         |
| Beryl 7 (GL-MT3600BE)           | √         |
| Flint 3e (GL-BE6500)            | √         |
| Flint 3 (GL-BE9300)             | √         |
| Slate 7 (GL-BE3600)             | √         |

MLO (Multi-Link Operation) ist eine der Kernfunktionen von Wi‑Fi 7 (802.11be). Es wurde entwickelt, um die Netzwerkleistung zu verbessern, die Latenz deutlich zu verringern und die Verbindungsstabilität zu erhöhen, indem mehrere Frequenzbänder wie 2,4 GHz, 5 GHz und 6 GHz gleichzeitig genutzt werden.

Klicken Sie auf die folgenden Tabs, um mehr über die Einstellungen für MLO Main Wi‑Fi und MLO Guest Wi‑Fi zu erfahren.

=== "MLO Wi‑Fi"

    Das MLO Main Wi‑Fi ermöglicht die Konfiguration verschiedener Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, die Auswahl von Funkbändern (mindestens zwei), das Aktivieren/Deaktivieren von **Randomized BSSID**, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Wi‑Fi-Passworts und der SSID-Sichtbarkeit.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Wenn die Funkbänder des MLO Wi‑Fi 6 GHz enthalten, wird die MLO-Wi‑Fi-BSSID synchronisiert, wenn sich die 6GHz-Wi‑Fi-BSSID ändert.

    - Die Standard-Wi‑Fi-Sicherheit für MLO Wi‑Fi ist WPA3-SAE und eignet sich für die meisten Geräte, die MLO unterstützen.

=== "MLO Guest Wi‑Fi"

    Das MLO Guest Wi‑Fi ermöglicht die Konfiguration vereinfachter Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, die Auswahl von Funkbändern (mindestens zwei), das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Passworts und der SSID-Sichtbarkeit.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## 6-GHz-Wi‑Fi {#6-ghz-wi-fi}

| Unterstützte Modelle            |           |
| :------------------------------ | :-------: |
| Slate 7 Pro (GL-BE10000)        | √         |
| Mudi 7 (GL-E5800)               | √         |
| Flint 3 (GL-BE9300)             | √         |

6-GHz-Wi‑Fi bietet im Vergleich zu den Bändern 2,4 GHz und 5 GHz eine schnellere und stabilere Wireless-Konnektivität mit geringerer Auslastung.

Klicken Sie auf die folgenden Tabs, um mehr über die Einstellungen für 6 GHz Main Wi‑Fi und 6 GHz Guest Wi‑Fi zu erfahren.

=== "6 GHz Wi‑Fi"

    Das 6 GHz Main Wi‑Fi ermöglicht die Konfiguration verschiedener Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen der TX-Leistung, das Aktivieren/Deaktivieren von **Randomized BSSID**, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Wi‑Fi-Passworts, der SSID-Sichtbarkeit, des Wi‑Fi-Modus, der **Bandwidth** und des **Channel**.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - **Enable PSC**: Wenn PSC (Preferred Scanning Channel) aktiviert ist, werden nur Kanäle mit besserer Konnektivität reserviert, um Verbindungen von 6-GHz-Geräten sicherzustellen.

=== "6 GHz Guest Wi‑Fi"

    Das 6 GHz Guest Wi‑Fi ermöglicht die Konfiguration vereinfachter Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Passworts und der SSID-Sichtbarkeit.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## 5-GHz-Wi‑Fi {#5-ghz-wi-fi}

Klicken Sie auf die folgenden Tabs, um mehr über die Einstellungen für 5 GHz Main Wi‑Fi und 5 GHz Guest Wi‑Fi zu erfahren.

=== "5 GHz Wi‑Fi"

    Das 5 GHz Main Wi‑Fi ermöglicht die Konfiguration verschiedener Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen der TX-Leistung, das Aktivieren/Deaktivieren von **Randomized BSSID**, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Wi‑Fi-Passworts, der SSID-Sichtbarkeit, des Wi‑Fi-Modus, der **Bandwidth** und des **Channel**.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi‑Fi"

    Das 5 GHz Guest Wi‑Fi ermöglicht die Konfiguration vereinfachter Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Passworts und der SSID-Sichtbarkeit.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## 2,4-GHz-Wi‑Fi {#24-ghz-wi-fi}

Klicken Sie auf die folgenden Tabs, um mehr über die Einstellungen für 2,4 GHz Main Wi‑Fi und 2,4 GHz Guest Wi‑Fi zu erfahren.

=== "2.4 GHz Wi‑Fi"

    Das 2,4 GHz Main Wi‑Fi ermöglicht die Konfiguration verschiedener Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen der TX-Leistung, das Aktivieren/Deaktivieren von **Randomized BSSID**, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Wi‑Fi-Passworts, der SSID-Sichtbarkeit, des Wi‑Fi-Modus, der **Bandwidth** und des **Channel**.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi‑Fi"

    Das 2,4 GHz Guest Wi‑Fi ermöglicht die Konfiguration vereinfachter Einstellungen, darunter das Aktivieren/Deaktivieren von Wi‑Fi, das Festlegen des Wi‑Fi-Namens (SSID), der Wi‑Fi-Sicherheit, des Passworts und der SSID-Sichtbarkeit.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Allgemeine Wi‑Fi-Einstellungen {#general-wi-fi-settings}

* Bewegen Sie den Mauszeiger über das QR-Code-Symbol neben der Wi‑Fi-SSID, um den zugehörigen Wi‑Fi-QR-Code anzuzeigen. Sie können ihn mit Ihrem Telefon oder Tablet scannen, um sich schnell mit dem entsprechenden Wi‑Fi-Netzwerk zu verbinden.

    ![wifi qr code](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: Diese standardmäßig aktivierte Funktion verhindert die Verfolgung des Routers über eine feste BSSID. Weitere Informationen finden Sie unter [Randomized BSSID](#randomized-bssid).

* **Bandwidth** und **Channel** können nicht geändert werden, wenn der Router als [Repeater](internet_repeater.md) arbeitet, da sie dem wiederholten Netzwerk folgen.

* Wenn **Channel** auf **Auto** gesetzt ist, wechselt das Wi‑Fi des Routers nicht automatisch auf den DFS-Kanal.

* Wenn **Channel** von einem Nicht-DFS-Kanal auf einen DFS-Kanal umgestellt wird, erscheint die folgende Warnung.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* Wenn **Bandwidth** auf **160 MHz** eingestellt ist (nur bei einigen Modellen verfügbar), verwendet das Wi‑Fi immer den DFS-Kanal, selbst wenn Sie für **Channel** einen Nicht-DFS-Kanal oder **Auto** auswählen.

## Randomized BSSID {#randomized-bssid}

Randomized BSSID ist eine seit Firmware v4.6 verfügbare und standardmäßig aktivierte Datenschutzfunktion. Sie verhindert, dass Ihr Router über eine feste WLAN-BSSID (die MAC-Adresse der WLAN-Schnittstelle des Routers) geortet und verfolgt wird.

**Warum eine feste BSSID ein Datenschutzrisiko darstellt**

Mobile Betriebssysteme (z. B. Android und iOS) nutzen per Crowdsourcing erfasste WLAN-Positionsdaten für Standortdienste:

1. Client-Geräte wie Smartphones und Laptops laden regelmäßig die sichtbaren BSSIDs zusammen mit ihrer eigenen GPS-Position auf den Server des Betriebssystem- oder Geräteherstellers hoch.

2. Die Hersteller führen diese Daten in einer globalen Datenbank zusammen, die BSSIDs Standorten zuordnet.

3. Jedes Gerät mit aktiviertem WLAN kann diese Datenbank auch ohne GPS abfragen, um seinen Standort anhand der BSSIDs in seiner Umgebung zu schätzen.

![randomized bssid](https://static.gl-inet.com/docs/router/de/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

Ein Router mit fester BSSID wirkt dadurch wie eine ortsfeste Standortmarkierung: Er kann aus der Ferne geortet werden, und seine Bewegungen (etwa auf Reisen) lassen sich über längere Zeit verfolgen. Angreifer können solche Datenbanken auch abfragen, um Router zu orten oder sie anhand der Herstellerinformationen (OUI) in der BSSID wiederzuerkennen.

**Wie Randomized BSSID Sie schützt**

Wenn diese Funktion aktiviert ist, erzeugt der Router eine zufällige BSSID und erneuert sie bei jedem Start. Da sich die BSSID fortlaufend ändert, lässt sie sich in den Herstellerdatenbanken keinem festen Standort mehr zuordnen. Die zur Verfolgung verwendete Verknüpfung zwischen BSSID und Standort wird damit unterbrochen.

| Status | Verhalten |
| ----------------- | ---------------------- |
| Aktiviert (Standard) | Bei jedem Start wird eine neue zufällige BSSID erzeugt |
| Deaktiviert | Der Router verwendet seine tatsächliche werkseitige MAC-Adresse als BSSID |

**Hinweise**:

1. Die BSSID ändert sich nur beim Neustart des Routers; während einer laufenden Sitzung bleibt sie gleich.
2. Beim Gast-WLAN bleibt die BSSID im selben Frequenzband mit der BSSID des Haupt-WLANs identisch.
3. Wenn die Frequenzbänder des MLO-WLANs 6 GHz umfassen, wird die BSSID des MLO-WLANs mit der BSSID des 6-GHz-WLANs synchronisiert.
4. Randomized BSSID verhindert die Verfolgung über die BSSID des Routers, hindert Client-Geräte jedoch nicht daran, ihren eigenen Standort zu melden. Die Funktion bietet keinen vollständigen Datenschutz: SSID, Kanal und Signaleigenschaften bleiben beobachtbar.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"}.
