# Datenstatistiken

**Hinweis**: Diese Funktion wurde mit Firmware v4.9 eingeführt. Einige Modelle, z. B. Mango 2 (GL-MG1300), unterstützen Data Statistics wegen unzureichenden Speichers auch mit Firmware v4.9 oder höher nicht.

---

Navigieren Sie im linken Menü des webbasierten Admin-Panels zu **FLOW CONTROL** -> **Data Statistics**.

Die Datenstatistiken bieten ein intuitives Dashboard für den Datenverkehr, das die Netzwerknutzung nach Anwendungen und Protokollen erkennt. Es unterstützt historische Trends für 1 Stunde, 1 Tag und 7 Tage, zeigt Nutzungsrankings an, überwacht den Datenverkehr pro Gerät und erlaubt das Blockieren unerwünschter Apps mit einem Klick.

**Hinweis**:

1. Datenstatistiken wirken nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.
2. Datenstatistiken können nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren der Datenstatistiken wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.
3. Die Datenstatistiken erfassen nur die Datennutzung von Geräten, die auf der Seite **Clients** aufgeführt sind. Wenn ein Gerät über eine Tunnelschnittstelle (z. B. VPN-Client, Tailscale oder AstroWarp) mit dem Router verbunden ist, wird der von diesem Gerät ausgehende und über den Router weitergeleitete Datenverkehr nicht in diesen Statistiken erfasst.

## Für Firmware v4.11 und höher

Aktivieren Sie den Schalter oben rechts, um **Application Total Data** anzuzeigen.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Die Seite besteht aus zwei Bereichen:

- **Top 10 Apps by Bandwidth Usage**: Ein zeitbasiertes Trenddiagramm zeigt den Bandbreitenverbrauch der zehn am stärksten genutzten Anwendungen im ausgewählten Zeitraum.

    Bewegen Sie den Mauszeiger über das Diagramm, um den Datenverbrauch dieser Anwendungen zu einem bestimmten Zeitpunkt anzuzeigen.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Zeigt für jede Anwendung detaillierte Datenverkehrswerte einschließlich Download, Upload und Total Bandwidth an. Über die Suchleiste können Sie nach bestimmten Apps suchen.

    Klicken Sie neben einer Spaltenüberschrift auf den Sortierpfeil, um die Liste auf- oder absteigend zu sortieren.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Regeln zur Datenspeicherung

1. Datenverkehrsstatistiken werden alle 15 Sekunden im RAM und jede Stunde im Flash-Speicher gespeichert. Zum Schutz der Lebensdauer des Flash-Speichers werden häufige Schreibvorgänge vermieden.
2. Bei einem Soft-Reboot gehen keine Daten verloren. Das System schreibt die Daten vor dem Neustart aus dem RAM in den Flash-Speicher.
3. Bei einem Hard-Reboot oder einem Firmware-Upgrade mit beibehaltenen Einstellungen können Daten der letzten Stunde verloren gehen.

### Client-Auswahl

Mit der Client-Auswahl können Sie einen bestimmten Client auswählen oder die Standardeinstellung All clients beibehalten. Diagramm und Statistiktabelle werden automatisch aktualisiert und zeigen nur die Daten des ausgewählten Geräts an.

**Hinweis**: Diese Funktion wurde mit Firmware v4.11 eingeführt.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Diagrammansicht wechseln

Beim Anzeigen der App Traffic Statistics können Sie den Diagrammtyp nach Bedarf wechseln.

**Hinweis**: Diese Funktion wurde mit Firmware v4.11 eingeführt.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Liniendiagramm**: Zeigt den Bandbreitenverbrauch im ausgewählten Zeitraum. Durchgehende Kurven verdeutlichen Änderungen im Zeitverlauf.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Balkendiagramm**: Vergleicht den Bandbreitenverbrauch der Anwendungen direkt miteinander.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Kreisdiagramm**: Teilt den gesamten Bandbreitenverbrauch in prozentuale Anteile auf.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Zeitbereich wechseln

Sie können zwischen Past hour, Past day und Past week wechseln.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

Der ausgewählte Zeitraum bestimmt die Darstellung:

- **Detailansicht (z. B. Past Hour)**: Das Diagramm zeigt feine Schwankungen in Echtzeit, sodass plötzliche Bandbreitenspitzen leicht zu erkennen sind.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **Gesamtübersicht (z. B. Past Day oder Past Week)**: Das Diagramm fasst die Daten auf einer längeren Zeitachse zusammen und zeigt den allgemeinen Datenverkehrstrend.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Statistiken löschen

Klicken Sie oben links auf das Besensymbol, um die Statistiken zu löschen.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Nach dem Löschen wird die Seite wie unten dargestellt aktualisiert. Es kann einen Moment dauern, bis neue Statistiken geladen werden.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Für Firmware v4.9 bis v4.10

Schalten Sie den Schalter oben rechts ein, um **Application Total Data** anzuzeigen.

![data statistics](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Diese Seite besteht aus zwei Bereichen:

- **Top 10 Apps by Bandwidth Usage**: Dieser Bereich zeigt ein zeitbasiertes Trenddiagramm (z. B. für den vergangenen Tag), um den Bandbreitenverbrauch der 10 am stärksten genutzten Anwendungen im ausgewählten Zeitraum darzustellen.

    Bewegen Sie den Mauszeiger über das Diagramm, um den Datenverbrauch der 10 bandbreitenintensivsten Apps zu einem bestimmten Zeitpunkt anzuzeigen.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Dieser Bereich zeigt detaillierte Verkehrsmetriken für jede Anwendung an, einschließlich Download, Upload und Total Bandwidth. Suchen Sie bei Bedarf über die Suchleiste nach bestimmten Apps.

    Klicken Sie auf den Sortierpfeil neben der Spaltenüberschrift, um die Liste auf- oder absteigend zu sortieren.

    ![app traffic stat](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Regeln zur Datenspeicherung

1. Verkehrsstatistiken werden alle 15 Sekunden im RAM gespeichert und jede Stunde im Flash abgelegt. Häufige Flash-Schreibvorgänge werden vermieden, um die Lebensdauer des Flash-Speichers zu schützen.

2. Ein Soft-Reboot führt nicht zu Datenverlust. Vor dem Neustart schreibt das System die Daten zuerst aus dem RAM in den Flash.

3. Ein Hard-Reboot (Netzstecker ziehen und wieder einstecken) oder ein Firmware-Upgrade (bei Beibehaltung der Einstellungen) kann zu Datenverlust von bis zu einer Stunde führen.

### Zeitbereich wechseln

Sie können den Zeitbereich je nach Bedarf zwischen Past Hour, Past Day und Past Week umschalten.

![select time range](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

Der gewählte Zeitbereich bestimmt, wie die Daten dargestellt werden:

- **Für eine detaillierte Ansicht (z. B. Past Hour)**: Das Diagramm zeigt feingranulare Schwankungen nahezu in Echtzeit. Spitzen wirken höher und Einbrüche steiler, sodass plötzliche Bandbreitenspitzen leichter zu erkennen sind.

    ![past hour](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Für einen allgemeinen Überblick (z. B. Past Day oder Past Week)**: Das Diagramm verdichtet die Daten über einen längeren Zeitraum. Die Kurven werden glatter und zeigen eher den allgemeinen Verkehrstrend als jede kleine Änderung.

    ![past week](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Statistiken löschen

Klicken Sie oben links auf das Besensymbol, um die Statistiken bei Bedarf zu löschen.

![clear data](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Nach dem Löschen wird die Seite wie unten gezeigt aktualisiert. Möglicherweise müssen Sie einen Moment warten, bis neue Statistiken geladen werden.

![clear data](https://static.gl-inet.com/docs/router/de/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
