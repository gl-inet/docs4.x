# Multi-WAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Öffnen Sie auf der linken Seite des Web-Admin-Panels **NETWORK** -> **Multi-WAN**.

Sie können den Router mit mehreren Internetzugangsmethoden konfigurieren. Wenn eine Internetzugangsart nicht verfügbar ist, kann der Router in kurzer Zeit automatisch auf eine andere umschalten. Alternativ können Sie mehrere Internetzugangsmethoden gleichzeitig verwenden und Netzwerkverbindungen in einem festgelegten Verhältnis auf verschiedene Verbindungsarten verteilen.

GL.iNet-Router können auf verschiedene Arten mit dem Internet verbunden werden, z. B. über [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md) und [Cellular](internet_cellular.md).

!!! Note

    1. Modelle ohne Wi-Fi-Funktionalität (z. B. GL-MT2500/GL-MT2500A) unterstützen nur den Netzwerkzugang über Ethernet, Tethering und Cellular.

    2. Modelle ohne USB-Port (z. B. GL-B3000) unterstützen nur den Netzwerkzugang über Ethernet und Repeater.

    3. Einige Modelle unterstützen [Dual-Ethernet WAN](ethernet_port.md#dual-ethernet-wan); in der Benutzeroberfläche wird dann eine zusätzliche Ethernet-Schnittstelle angezeigt.

## Schnittstellen-Statusüberwachung

GL.iNet-Router unterstützen bis zu 5 virtuelle Netzwerkschnittstellen, wobei die genaue Anzahl je nach Modell variieren kann. Beispielsweise verfügt der GL-MT6000 über **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** und **Cellular**, die jeweils unterschiedliche Netzwerkfunktionen in softwaredefinierten Konfigurationen übernehmen.

Die Router verwenden den Befehl **ping** oder **httping** (nur für v4.3 und älter), um den Status der Verbindung zur Ziel-IP zu überwachen und festzustellen, ob die Schnittstelle verfügbar ist.

Wenn die Schnittstelle verfügbar ist, wird links ein grüner Punkt angezeigt, andernfalls ein grauer.

![interface status track 1](https://static.gl-inet.com/docs/router/de/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Einstellungen für die Statusüberwachung

Klicken Sie auf das Zahnradsymbol, um die Einstellungen für die Statusüberwachung jeder Netzwerkschnittstelle aufzurufen.

Dies ist beispielsweise die Einstellung für die Statusüberwachung der Ethernet-Schnittstelle; für andere Schnittstellen gilt dasselbe.

![interface status track 2](https://static.gl-inet.com/docs/router/de/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track**: Diese Option ist standardmäßig aktiviert. Sie können die Schnittstellen-Statusüberwachung deaktivieren. In diesem Fall bestimmt der Router den Schnittstellenstatus anhand des physischen Status, z. B. ob das Netzwerkkabel eingesteckt ist oder nicht.

- **Detection Mode**: Diese Funktion wurde in v4.5 als Low Data Mode eingeführt und in v4.7 in Detection Mode umbenannt. Es stehen drei Modi zur Verfügung: Normal Mode, Low Data Mode und Strict Mode.

    Normal Mode wird standardmäßig verwendet. Low Data Mode prüft nur dann, wenn ein Netzfehler auf einer Schnittstelle auftritt, und Strict Mode bestimmt den Schnittstellenstatus ausschließlich anhand der Ergebnisse eines Prüfbefehls gegen eine öffentliche IP.
    
    Sie können Low Data Mode verwenden, wenn Sie einen begrenzten Datentarif haben. Ein Nachteil besteht jedoch darin, dass die Wiederverbindung nach einem Netzwerkausfall im Vergleich zum normalen Modus etwas langsamer sein kann. Standardmäßig wird dann nur die Cellular-Schnittstelle eingeschaltet.

- **Track Command**: Der Befehl ping wird verwendet, um den Status der Verbindung zur Ziel-IP zu überwachen und festzustellen, ob die Schnittstelle verfügbar ist. Für Firmware v4.3 und älter steht zusätzlich der Befehl httping zur Verfügung.

- **IPv4 Track IP**: Hier können Sie die IPv4 Track IP anpassen.

!!! Note

    Ältere Firmware-Versionen wie v4.3 bieten Einstellungen wie **Track Interval**, **Change to Failure Condition** und **Change to Available Condition**. Diese Einstellungen wurden seit v4.5 entfernt und durch Detection Mode sowie Sensitivity Options ersetzt.

### Sensitivity Options

Diese Funktion ist seit v4.5 verfügbar.

![Sensitivity Options](https://static.gl-inet.com/docs/router/de/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Diese Empfindlichkeit bestimmt das Zeitintervall für die Erkennung des Internetstatus.

- Wenn das Netzwerk stabil ist und Sie z. B. Videos oder Livestreams ansehen oder Spiele spielen, empfiehlt sich eine hohe Empfindlichkeit, damit bei einer Netzwerkunterbrechung schnell umgeschaltet wird.
- Wenn das Netzwerk instabil ist und Sie zwischengespeicherte Dateien herunterladen, empfiehlt sich eine niedrige Empfindlichkeit, damit nicht ständig zwischen Netzwerken umgeschaltet und erfolglose Verbindungen erkannt werden.

**Tipps**: Das Umschalten auf hohe Empfindlichkeit kann zu Netzwerkunterbrechungen führen. Passen Sie diese Einstellung daher mit Vorsicht an.

## Multi-WAN-Modus

Für Multi-WAN stehen zwei Modi zur Verfügung: **Failover** und **Load Balance**. Sie schließen sich gegenseitig aus; es kann jeweils nur einer der beiden Modi verwendet werden.

### Failover

Failover ist der Standardmodus, wenn mehrere WAN-Verbindungen vorhanden sind. Fällt die aktive Verbindung aus, schaltet der Router für den Internetzugang automatisch auf eine andere Netzwerkschnittstelle um.

![multi-wan failover](https://static.gl-inet.com/docs/router/de/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Sie können die Priorität jeder Schnittstelle festlegen. Fällt die aktuell verwendete Schnittstelle aus, wechselt der Router zur nächsten verfügbaren Schnittstelle mit der höchsten Priorität. Sobald eine Verbindung mit höherer Priorität wiederhergestellt ist, schaltet der Router automatisch zu ihr zurück.

### Load Balance

Load Balance ermöglicht die gleichzeitige Nutzung mehrerer Netzwerkverbindungen, wodurch sich die Bandbreite und der Gesamtdurchsatz erhöhen.

Das **Load Ratio** bestimmt die Verteilung des Datenverkehrs auf die Schnittstellen. Das System weist neue Verbindungen entsprechend dem konfigurierten Verhältnis den einzelnen Schnittstellen zu.

Die folgenden zwei Lastverhältnisse können konfiguriert werden:

- **Default Load Ratio**

    Wenn der Router gleichzeitig mit vier Netzwerken (Ethernet, Repeater, Tethering und Cellular) verbunden ist und alle vier Schnittstellen auf das Internet zugreifen können, verteilt die Einstellung 1:1:1:1 neue Verbindungen entsprechend diesem Verhältnis gleichmäßig auf die vier Schnittstellen.

- **Customize Load Ratio**

    Wenn die Ethernet-Bandbreite 200 Mbit/s, die Repeater-Wi-Fi-Bandbreite 100 Mbit/s beträgt und keine Tethering- oder Cellular-Verbindung aktiv ist, können Sie das Verhältnis auf 2 für Ethernet, 1 für Repeater und 0 für Tethering/Cellular setzen. Das System weist neue Verbindungen entsprechend dem konfigurierten Verhältnis 2:1 zu. Dadurch verarbeitet Ethernet etwa doppelt so viele Verbindungen wie Repeater. Gegenüber dem Failover-Modus verbessert dies den Gesamtdurchsatz, indem die Last auf die verfügbaren Schnittstellen verteilt wird.

**Hinweis:** Bereits bestehende Verbindungen oder laufender Datenverkehr entsprechen nicht zwingend exakt dem Lastverhältnis. Über einen längeren Nutzungszeitraum nähert sich die Verteilung diesem Verhältnis an.

![multi-wan load balance](https://static.gl-inet.com/docs/router/de/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

## Anwendungsszenarien

* Das Kassensystem eines Geschäfts nutzt eine kabelgebundene Internetverbindung, während Repeater zu einem Wi-Fi in benachbarten Geschäften (oder das Einlegen einer SIM-Karte zur Aktivierung des Mobilfunknetzes) als Backup-Internetzugangsmethode dient, damit mobile Zahlungen weiterhin möglich sind, wenn das Netzwerkkabel nicht verfügbar ist.

* Der Router ist per Repeater mit öffentlichem Wi-Fi verbunden, aber die Netzwerkgeschwindigkeit ist nicht hoch genug. Dann können Sie gleichzeitig Mobile Tethering für Load Balance verwenden, um die Gesamtbandbreite zu verbessern.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
