# QoS (Quality of Service)

QoS (Quality of Service) optimiert die Bandbreitenzuweisung, indem kritische Aktivitäten (z. B. Videoanrufe oder Gaming) bei Netzwerküberlastung priorisiert werden. Dadurch werden Latenzen reduziert und die allgemeine Netzwerkleistung verbessert.

**Hinweis**:

1. Diese Funktion wirkt sich nur auf Datenverkehr aus, der den Router passiert, wenn er als Gateway arbeitet, einschließlich lokalem Client-Datenverkehr und VPN-Client-Datenverkehr. Auf eingehenden Datenverkehr wirkt sie nicht, wenn der Router als VPN-Server arbeitet.
2. QoS wirkt nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.
3. QoS und SQM können nicht gleichzeitig aktiviert werden.
4. QoS kann nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren von QoS wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle

!!! note "Unterstützte Modelle"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Hinweis: Mit ※ gekennzeichnete Modelle unterstützen QoS ab Firmware v4.9.

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **QoS**.

Schalten Sie den Schalter um, um QoS zu aktivieren. Die Seite wird dann wie unten dargestellt angezeigt.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Legen Sie Ihre maximale Upload- und Download-Geschwindigkeit fest (Eingabebereich: 1 - 10000), damit der Datenverkehr geplant werden kann. Stimmen Sie die Werte für optimale Ergebnisse auf Ihre tatsächliche Internetbandbreite ab.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Hinweis**: Die im Eingabefeld eingegebenen Werte sind in **Mbps** (Megabit pro Sekunde) angegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

Legen Sie anschließend Prioritäten für verschiedene Anwendungen fest. Der Router weist die Bandbreite entsprechend zu.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## App-Priorität anpassen

Um die Priorität von Anwendungen anzupassen, wählen Sie **Customize** aus und klicken Sie auf **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

Im Pop-up-Fenster sind standardmäßig alle Kategorien auf mittlere Priorität gesetzt.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Ziehen Sie die Kategorien per Drag-and-drop, um ihre Priorität nach Bedarf anzupassen, und klicken Sie dann auf **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
