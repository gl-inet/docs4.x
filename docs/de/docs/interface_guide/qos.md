# QoS (Quality of Service)

**Hinweis**: Diese Funktion wurde mit Firmware v4.9 eingeführt. Einige Modelle, z. B. Mango 2 (GL-MG1300), unterstützen QoS wegen unzureichenden Speichers auch mit Firmware v4.9 oder höher nicht.

---

Navigieren Sie im linken Menü des webbasierten Admin-Panels zu **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service) optimiert die Bandbreitenzuweisung, indem kritische Aktivitäten (z. B. Videoanrufe oder Gaming) bei Netzwerküberlastung priorisiert werden. Dadurch werden Latenzen reduziert und die allgemeine Netzwerkleistung verbessert.

**Hinweis**:

1. Diese Funktion wirkt sich nur auf Datenverkehr aus, der den Router passiert, wenn er als Gateway arbeitet, einschließlich lokalem Client-Datenverkehr und VPN-Client-Datenverkehr. Auf eingehenden Datenverkehr wirkt sie nicht, wenn der Router als VPN-Server arbeitet.
2. QoS wirkt nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.
3. QoS und SQM können nicht gleichzeitig aktiviert werden.
4. QoS kann nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren von QoS wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Für Firmware v4.11 und höher

Aktivieren Sie QoS mit dem Schalter und führen Sie anschließend die folgenden Schritte aus.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Geben Sie die Upload- und Download-Geschwindigkeit des WAN manuell ein (Eingabebereich: 1–10000) oder klicken Sie auf **Run Speedtest**, um sie zu messen und die Felder automatisch auszufüllen. Für den Geschwindigkeitstest ist eine aktive Internetverbindung erforderlich.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Hinweis**: Die Werte werden in **Mbps** (Megabit pro Sekunde) eingegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

2. **Scheduling Policy**

    Sie können einen Richtlinienmodus auswählen. Erweiterte Regeln haben für übereinstimmenden Datenverkehr Vorrang vor der grundlegenden Richtlinie.

    - **Device Priority**

        In diesem Modus erhalten ausgewählte lokale Clients bei ausgelasteter WAN-Verbindung eine höhere Netzwerkpriorität. Klicken Sie auf **Add Device** und wählen Sie die zu priorisierenden Geräte aus.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Sie können nach Clientname, MAC- oder IP-Adresse suchen. Wählen Sie die gewünschten Geräte aus und klicken Sie auf **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        In diesem Modus können Sie Prioritäten für verschiedene Anwendungen festlegen. Der Router weist die Bandbreite entsprechend zu.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Wählen Sie zum Anpassen **Customize** aus und klicken Sie auf **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        Im Pop-up-Fenster sind standardmäßig alle Kategorien auf Medium Priority gesetzt.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Ziehen Sie die Kategorien auf die gewünschte Prioritätsstufe und klicken Sie auf **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        In diesem Modus können Sie erweiterte QoS-Regeln für Datenverkehr mit hoher Priorität erstellen. Klicken Sie auf **Add Rule**, um Regeln anhand von Protokoll, Port und Quell-IP festzulegen.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Geben Sie Name, Protocol, Source Address und Destination Port an und klicken Sie auf **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Für Firmware v4.9 bis v4.10

Schalten Sie den Schalter um, um QoS zu aktivieren. Die Seite wird dann wie unten dargestellt angezeigt.

![qos](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/qos.png){class="glboxshadow"}

Legen Sie Ihre maximale Upload- und Download-Geschwindigkeit fest (Eingabebereich: 1 - 10000), damit der Datenverkehr geplant werden kann. Stimmen Sie die Werte für optimale Ergebnisse auf Ihre tatsächliche Internetbandbreite ab.

![qos speed](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Hinweis**: Die im Eingabefeld eingegebenen Werte sind in **Mbps** (Megabit pro Sekunde) angegeben. Der entsprechende Wert in **MB/s** (Megabyte pro Sekunde) wird als Referenz angezeigt.

Legen Sie anschließend Prioritäten für verschiedene Anwendungen fest. Der Router weist die Bandbreite entsprechend zu.

![app priority](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

Um die Priorität von Anwendungen anzupassen, wählen Sie **Customize** aus und klicken Sie auf **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

Im Pop-up-Fenster sind standardmäßig alle Kategorien auf mittlere Priorität gesetzt.

![customize priority2](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Ziehen Sie die Kategorien per Drag-and-drop, um ihre Priorität nach Bedarf anzupassen, und klicken Sie dann auf **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/de/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
