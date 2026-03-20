# So richten Sie Spitz AX (GL-X3000) in Ihrem Wohnmobil ein und nutzen ihn

Diese Anleitung zeigt Ihnen, wie Sie Spitz AX in Ihrem Wohnmobil einrichten und verwenden. Bevor Sie beginnen, benötigen Sie je nach Einsatz möglicherweise folgende zusätzliche Geräte und Dienste:

- SIM-Karte(n) oder ein USB-Kabel (für Tethering), je nachdem, welche Methode Sie für die Internetverbindung verwenden. Wenn Sie SIM-Karten verwenden, fragen Sie Ihren Anbieter nach dem APN.
- Eine Dachantenne, wenn Sie eine bessere Abdeckung wünschen.
- [Ein Starlink-Abonnement](https://www.starlink.com/roam), falls Sie in Gebiete ohne Mobilfunkabdeckung fahren.

---

## 1. Installieren Sie Ihren Spitz AX und weiteres Zubehör

Richten Sie Ihren Spitz AX vor Reisebeginn mit den folgenden Schritten ein.

### Schritt 1: Wählen Sie einen Standort für Ihren Spitz AX

Es wird empfohlen, einen zentralen und freien Standort zu wählen, um eine maximale Abdeckung zu erzielen. Stellen Sie sicher, dass sich der Standort innerhalb von 1 Meter von der Stromquelle befindet, da dies der Länge des Netzkabels entspricht.

![Standort](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Sie können Ihren Spitz AX auf einer ebenen Fläche platzieren oder an der Wand montieren. Wenn Sie ihn an der Wand montieren möchten, folgen Sie dem nächsten Schritt.

### (Optional) Schritt 2: Installieren Sie Ihren Spitz AX an der Wand

Es gibt zwei Möglichkeiten, Ihren Spitz AX an der Wand zu montieren:
- Verwenden Sie das mitgelieferte Klebepad.
- Verwenden Sie die Wandhalterungen.

Wandhalterungen sind im Lieferumfang enthalten. Um Ihren Spitz AX an der Wand zu befestigen, gehen Sie wie folgt vor:

1.	Befestigen Sie die Halterung mit Schrauben an der Wand.
2.	Rasten Sie Ihren Spitz AX in die Halterung ein.

![Wandhalterung](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Optional) Schritt 3: Installieren Sie die Wohnmobil-Dachantenne

![Dachantenne](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Für ein besseres Signal verwenden Sie eine Dachantenne für Ihren Spitz AX. Empfohlen wird die [LTMG942-Multibandantenne von MobileMark](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/), die optimale Netzwerksignale bietet. Wenn Sie Dachantennen anderer Marken verwenden möchten, achten Sie darauf, dass sie die folgenden Anforderungen erfüllen:

- 4 Mobilfunkantennen, Empfangsfrequenzbereich 600M~6GHz.
- 2 Wi-Fi-Antennen, Empfangsfrequenzbereich: 2.4G~2.5GHz, 5.15~5.84GHz

![Antennen](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Hinweis:** Sie können eine 7-in-1-Antenne verwenden (einschließlich GPS-Antenne), müssen an Ihrem Spitz AX jedoch nur sechs Antennen anschließen. Die DIV/GNSS-Schnittstelle des Spitz AX unterstützt GPS-Signale, da die Mobilfunkantenne (Empfangsfrequenz 600M~6GHz) auch den GPS-Frequenzbereich abdeckt. Spitz AX unterstützt die Anzeige Ihres GPS-Standorts über die Befehlszeile, zeigt Ihren Standort derzeit jedoch nicht auf der Karte an.

Um eine Signaldämpfung zu vermeiden, sollte das HF-Kabel von der Dachantenne zu Ihrem Spitz AX nicht länger als 5 Meter sein. (Wenn das HF-Kabel von MobileMark beispielsweise 5 Meter lang ist, wird die Signalstärke bei 3000 MHz um 3 dB reduziert, also auf die Hälfte. Je höher die Signalfrequenz, desto größer die Dämpfung.)

[Erfahren Sie, wie Sie die Antennen am Spitz AX austauschen.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/)

---

## 2. Richten Sie das Internet für Ihren Spitz AX ein

Damit Sie während Ihrer Reise Internetzugang haben, richten Sie die Internetverbindung über SIM-Karten ein.

Spitz AX verfügt über ein integriertes 5GNR-Modul und unterstützt Dual-SIM-Karten. Verschiedene Mobilfunkanbieter bieten unterschiedliche Tarife für SIM-Karten an und verwenden unterschiedliche APNs. Sie müssen den APN in den Einstellungen eingeben. Klären Sie daher mit Ihrem Anbieter, wie der APN lautet.

Gehen Sie wie folgt vor, um Ihre SIM-Karten einzurichten:

1. Setzen Sie Ihre SIM-Karte(n) ein.
![SIM einsetzen](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Schließen Sie das Netzteil an und schalten Sie den Router ein.

Gehen Sie wie folgt vor, um Ihren APN einzugeben:

1. Geben Sie `192.168.8.1` in einem Webbrowser ein und melden Sie sich an.
2. Oben links sollte der Name Ihres Anbieters angezeigt werden. Klicken Sie auf **Manual Setup**.
3. Geben Sie neben **APN** den APN ein.
4. Klicken Sie auf **Apply**.

Wenn Sie zwei SIM-Karten verwenden, beachten Sie bitte, dass immer nur eine SIM-Karte gleichzeitig aktiv ist. Sie können jedes Mal manuell auswählen, welche SIM-Karte verwendet werden soll. Alternativ können Sie die Funktion [Auto Switch](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models) aktivieren. Wenn der Router erkennt, dass eine der SIM-Karten nicht ordnungsgemäß auf das Internet zugreifen kann, wechselt er automatisch zur anderen SIM-Karte. Der Wechsel dauert etwa 1 Minute.

---

## 3. Verwenden Sie Spitz AX in verschiedenen Szenarien

### Unterwegs

![Unterwegs](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Während der Fahrt sollten Sie über die SIM-Karte(n), die Sie im vorherigen Schritt eingerichtet haben, eine Internetverbindung herstellen können.

### Auf dem Campingplatz

![Campingplatz](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Wenn Sie während Ihrer Reise auf einem Campingplatz anhalten, können Sie das dort bereitgestellte öffentliche WLAN nutzen und Ihre Mobilfunkdaten sparen. [Erfahren Sie, wie Sie sich mit einem vorhandenen WLAN-Netzwerk verbinden.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/)

Nachdem Sie sich einmal mit dem WLAN verbunden haben, kann Spitz AX den Netzwerknamen und das Passwort speichern. Beim nächsten Aufenthalt in der Nähe verbindet sich das Gerät automatisch mit dem Netzwerk.

### In Gebieten ohne Mobilfunkabdeckung

![Mobilfunk](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Wenn Sie in ein Gebiet ohne Mobilfunkabdeckung fahren (z. B. in eine dünn besiedelte Wüstenregion), verwenden Sie Starlink, einen satellitengestützten Internetdienst. So nutzen Sie in Gebieten mit guter Mobilfunkabdeckung das vom Spitz AX empfangene 5G-Signal und in Gebieten ohne Mobilfunkabdeckung Starlink.

Wenn Sie die Starlink-Antenne einrichten, achten Sie darauf, dass sie nicht verdeckt ist. Hindernisse auf beiden Seiten der Straße (z. B. Bäume) beeinträchtigen den Empfang. Parken Sie daher möglichst fern von Hindernissen.

---

## 4. Legen Sie Failover-Prioritäten fest
Spitz AX unterstützt Multi-WAN (Failover und Load Balance). Sie können für unterschiedliche Netzwerke je nach Szenario Failover-Prioritäten festlegen.

| Szenario| Priorität |
| --------| ------- |
| Auf dem Campingplatz (über Repeater mit dem WLAN des Platzes verbunden)    | <p>Weisen Sie dem Repeater eine höhere Priorität als Mobilfunk zu.</p> <p>Sobald Sie den Campingplatz verlassen, wechselt Ihr Router automatisch zurück auf Mobilfunk.</p>|
| Starlink (Ethernet) + Mobilfunk | <p>Weisen Sie Mobilfunk eine höhere Priorität als Ethernet zu.</p> <p>In Gebieten mit Mobilfunkabdeckung nutzt Ihr Router Ihr Mobilfunknetz.</p> <p>Wenn Sie in Gebiete ohne Mobilfunkabdeckung kommen, wechselt Ihr Router automatisch über Ethernet zu Starlink.</p>|

Informationen zum Einrichten von Failover finden Sie im Abschnitt [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
