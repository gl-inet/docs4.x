# Über Repeater mit einem vorhandenen Wi-Fi eine Internetverbindung herstellen

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Die Verwendung von Repeater bedeutet, dass der Router mit einem anderen vorhandenen Drahtlosnetzwerk verbunden wird, z. B. wenn Sie kostenloses Wi-Fi in einem Hotel oder Café nutzen.

Standardmäßig arbeitet dies im WISP-Modus (Wireless Internet Service Provider). Das bedeutet, dass der Router ein eigenes Subnetz erstellt und als Firewall fungiert, um Sie vor dem öffentlichen Netzwerk zu schützen.

## Grundlegende Schritte

Melden Sie sich im Web-Admin-Panel des Routers an, öffnen Sie den Bereich **INTERNET** -> **Repeater** und klicken Sie auf **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Wählen Sie das Wi-Fi-Netzwerk, mit dem Sie sich verbinden möchten, aus der Liste der verfügbaren Netzwerke aus.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Hinweis**: Auf der Seite werden die Wi-Fi-Kanäle angezeigt, die Ihr Router unterstützt. Stellen Sie bitte sicher, dass das Wi-Fi-Netzwerk, mit dem Sie sich verbinden, einen dieser Kanäle verwendet, andernfalls wird es möglicherweise nicht in der Liste der verfügbaren Netzwerke angezeigt.

Geben Sie das richtige Wi-Fi-Passwort ein und klicken Sie auf **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Wenn die Wi-Fi-SSID, mit der Sie sich verbinden möchten, nicht in der Liste **Available Network** enthalten ist, klicken Sie oben rechts auf **Join Other Network** und geben Sie die Wi-Fi-SSID sowie die weiteren erforderlichen Informationen manuell ein. Detaillierte Schritte finden Sie [hier](#join-other-network).

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Informationen zur Verbindung mit einem öffentlichen Hotspot, z. B. in Hotels, Flughäfen oder Einkaufszentren, finden Sie unter [Für öffentliche Hotspots](#for-public-hotspot).

Weitere Einstellungen finden Sie unter [Erweiterte Einstellungen](#advanced-settings).

Nach kurzer Zeit ist die Verbindung erfolgreich, wenn das Passwort korrekt eingegeben wurde.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Für öffentliche Hotspots {#for-public-hotspot}

Wenn Sie den Router mit einem öffentlichen Hotspot mit Captive Portal verbinden, können die folgenden Funktionen helfen, die Erfolgsquote der Verbindung zu verbessern.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Diese Funktion ist seit v4.6 verfügbar.

    Wenn diese Option aktiviert ist, wechselt dieser Router automatisch in den Login-Modus für öffentliche Hotspots, wenn er erfolgreich mit einem Hotspot, aber nicht mit dem Internet verbunden ist. **In diesem Modus werden einige Dienste ausgesetzt, während der DNS-Modus auf automatisch umgestellt wird**, wodurch Ihre Netzwerkaktivitäten möglicherweise für den Hotspot-Anbieter sichtbar werden (z. B. Hotel oder Einkaufszentrum).

    Auch wenn diese Option nicht aktiviert ist, fordert der Router Sie zum Wechsel in diesen Modus auf, wenn er in einem Hotspot ein Captive Portal erkennt und die Anmeldung nicht erfolgreich abschließen kann.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Wenn diese Option aktiviert ist, tarnt sich der Router als das Client-Gerät, mit dem Sie auf das Admin-Panel zugreifen, indem er dessen MAC-Adresse emuliert.

- **MAC Mode**

    Sie können auswählen, welche MAC-Adresse der Router für die Verbindung mit dem öffentlichen Hotspot verwendet.

    - **Factory**: Verwendet die ursprüngliche werkseitig vergebene MAC-Adresse des Geräts.

    - **Clone**: Klont die MAC-Adresse eines Client-Geräts für die Verbindung. Wenn die gewünschte MAC-Adresse nicht aufgeführt ist, geben Sie die zu klonende Adresse manuell ein.
    
        Hinweis: Viele moderne Geräte verwenden beim Verbinden mit Wi-Fi-Netzwerken zufällige MAC-Adressen (oft auch Private Wi-Fi Address oder random hardware address genannt). Deshalb stimmt die hier angezeigte MAC-Adresse möglicherweise nicht mit der tatsächlichen physischen MAC-Adresse des Geräts überein.
  
    - **Random**: Erzeugt automatisch eine zufällige MAC-Adresse für die Verbindung.

    Beim Speichern der Netzwerkkonfiguration wird der **MAC Mode** (einschließlich geklonter oder zufälliger MAC-Adresse) an die jeweilige gespeicherte SSID gebunden. Sie können diese Einstellungen für jede SSID jederzeit manuell ändern.

- **Auto Update MAC**: Wenn diese Option aktiviert ist, kann die MAC-Adresse automatisch aktualisiert werden.

## Erweiterte Einstellungen {#advanced-settings}

Beim Verbinden mit dem Netzwerk stehen einige zusätzliche Optionen zur Verfügung.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: Aktivieren Sie diese Option, um sich das aktuell wiederholte Wi-Fi-Netzwerk zu merken.

* **Lock BSSID**: Wenn diese Option aktiviert ist, verbindet sich der Router nur mit dem spezifischen Access Point (AP), der zur ausgewählten BSSID gehört, auch wenn andere APs dieselbe SSID verwenden.

* **Manually Set Static IP**: Wenn diese Option aktiviert ist, können Sie für die Repeater-Verbindung des Routers manuell eine feste IPv4-Adresse, Netzmaske, ein Gateway und DNS-Server konfigurieren, anstatt diese Einstellungen automatisch beziehen zu lassen.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live) legt fest, wie lange Pakete maximal im Netzwerk bestehen bleiben dürfen, und wird entsprechend den Anforderungen des Betreibers eingetragen. Standardmäßig leitet der Router die TTL des eingehenden Client-Geräts minus eins weiter. Wenn Sie die Verbindung tarnen möchten, können Sie hier einen festen Wert festlegen. TTL ist nur für IPv4 gültig.

* **HL**: In IPv6 wird das Feld HL (Hop Limit) verwendet, um die Anzahl der Übertragungssprünge von Datenpaketen im Netzwerk zu begrenzen; es entspricht der TTL in IPv4.

* **MTU**: Der Standardwert ist 1500.

## Repeater-Optionen

Um die Repeater-Optionen anzuzeigen, klicken Sie oben rechts im verbundenen Repeater-Bereich auf das Zahnradsymbol.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**Für Firmware v4.8** wird die Seite Repeater Options wie folgt angezeigt.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**:

    - **No Switching mode**: Wenn der No Switching mode aktiviert ist, werden andere gespeicherte Netzwerke nicht automatisch verbunden, wenn die aktuelle Wi-Fi-Verbindung getrennt wird.
  
    - **Auto Switching mode**: Wenn der Auto Switching mode aktiviert ist, versucht der Router, sich mit anderen gespeicherten Netzwerken zu verbinden, wenn die aktuelle Wi-Fi-Verbindung getrennt wird.
  
    - **Auto Switching Without Network**: Wenn der Modus Auto Switching Without Network aktiviert ist, scannt der Router nicht automatisch nach Netzwerken, wenn er in einem Nicht-Repeater-Modus erfolgreich mit einem Netzwerk verbunden ist. Er versucht nur dann automatisch zu anderen gespeicherten Netzwerken zu wechseln, wenn der Router ohne Netzwerk ist, wodurch Paketverluste in der Kommunikation vermieden werden können.

- **Band Selection**: Sie können zwischen drei Optionen wählen: Auto, 5 GHz und 2.4 GHz.

    Wenn Sie ein Band manuell auswählen, scannt oder verbindet sich der Router nicht mit Wi-Fi-Netzwerken, die ein anderes Band verwenden.

**Für Firmware v4.7 und früher** wird die Seite Repeater Options wie folgt angezeigt.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. Wenn diese Option aktiviert ist, verbindet sich der Router automatisch mit anderen gespeicherten Netzwerken, wenn er keine Verbindung mit dem aktuellen Wi-Fi-Netzwerk herstellen kann.

* **Band Selection**. Wenn Sie ein Band manuell auswählen, scannt oder verbindet sich der Router nicht mit Wi-Fi-Netzwerken eines anderen Bandes.

## Bekannte Netzwerke verwalten

Um bekannte Netzwerke zu löschen, klicken Sie auf **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Oder klicken Sie im Bereich Repeater auf **Connect**, wenn aktuell kein Netzwerk verbunden ist.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Klicken Sie im Bereich **Known Networks** auf das Papierkorbsymbol, um ein bekanntes Netzwerk zu löschen, oder auf das Zahnradsymbol, um das Netzwerk zu konfigurieren.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Anderes Netzwerk hinzufügen {#join-other-network}

Wenn die SSID nicht in der Liste **Available Networks** enthalten ist oder wenn die SSID verborgen ist, können Sie auf **Join Other Network** klicken.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Geben Sie die SSID ein, wählen Sie **Security** und geben Sie das Passwort ein (falls erforderlich).

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Für die **Security**-Einstellungen gibt es je nach Modell zwei oder drei Optionen.

* **None**, das heißt, es ist kein Passwort erforderlich.
* **WPA/WPA2/WPA3**, dies ist üblich und wird von nahezu allen Wi-Fi-Netzwerken unterstützt.
* **WPA/WPA2/WPA3 Enterprise**, hierfür ist das Extensible Authentication Protocol (EAP) zur Authentifizierung erforderlich. Für die Verbindung werden ein gültiger Benutzername und ein Passwort benötigt (typischerweise in Unternehmens- oder Campus-Netzwerken).

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Eine ausführliche Anleitung zum Repeater-Betrieb in EAP-Netzwerken finden Sie [hier](../tutorials/eap.md){target="_blank"}.

## Erneute Verbindung

In den folgenden Fällen versucht der Router in regelmäßigen Abständen automatisch, die Wi-Fi-Verbindung erneut herzustellen. Sie können dies bei Bedarf manuell deaktivieren. Bei SSID-/Passwortfehlern entfernen Sie das Netzwerk aus **Known Networks**, um das Problem zu beheben.

1. Bei der Repeater-Einrichtung wurde eine falsche SSID bzw. ein falsches Passwort eingegeben.

2. Nach der ersten Verbindung wurde der Router außerhalb der Reichweite des Upstream-Routers bewegt.

3. Der Upstream-Router ändert nach der Verbindung SSID/Passwort oder beschränkt den Zugriff.

Der Wiederverbindungsprozess hat drei unterschiedliche Phasen: Wartephase, Scanphase und Verbindungsphase.

1. **Wartephase**: Es liegen keine Probleme vor – der Router wartet auf Bedingungen für eine erneute Verbindung.

2. **Scanphase**: Auf dem gescannten Frequenzband kann Paketverlust auftreten. Neue Geräte können Verbindungsprobleme haben. Bei den Modellen GL-AXT1800/GL-AX1800 wird das Gast-Wi-Fi vorübergehend deaktiviert.

3. **Verbindungsphase**: Das Haupt-Wi-Fi auf dem Zielband kann während der Wiederherstellung für einige Sekunden ausfallen.

**Hinweis**: Probleme treten typischerweise in der Scanphase und in der Verbindungsphase auf.

## Fehlerbehebung

Wenn der Router als Repeater mit einem Wi-Fi-Netzwerk verbunden ist, aber kein Internet verfügbar ist, wird wie unten gezeigt eine gelbe Meldung angezeigt.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

So beheben Sie dieses Problem:

1. Prüfen Sie, ob das Upstream-Gerät (also das Wi-Fi-Netzwerk, mit dem Ihr Router verbunden ist) Internetzugang hat.

2. Öffnen Sie die Seite [Multi-WAN](multi-wan.md), um den Status der Repeater-Schnittstelle zu prüfen.

## DFS

Wenn eine Verbindung zu einem Upstream-5G-Wi-Fi hergestellt wird, übernimmt das Wi-Fi des Routers vom Upstream-Wi-Fi, ob ein DFS-Kanal verwendet wird oder nicht.

* Wenn das Upstream-Wi-Fi einen DFS-Kanal verwendet und gescannt werden kann, verwendet das 5G-Wi-Fi des Routers denselben Kanal.

* Das 5G-Wi-Fi des Routers wechselt auf einen Nicht-DFS-Kanal, wenn das Upstream-Wi-Fi nicht gescannt werden kann oder die Verbindung fehlschlägt.

??? "Unterstützte Modelle"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Nicht unterstützte Modelle"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Verwandte Artikel

- [Internetseite](internet.md)
- [Wie legt man die Priorität der einzelnen Internetzugangsmethoden fest?](multi-wan.md)
- [Wie richtet man den Lastenausgleich ein, wenn mehrere Internetzugangsmethoden gleichzeitig verwendet werden?](multi-wan.md)
- [Wie kann ich die LAN- und Wi-Fi-MAC-Adressen herausfinden](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
