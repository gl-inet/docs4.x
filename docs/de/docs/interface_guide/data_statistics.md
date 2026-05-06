# Datenstatistiken

Die Datenstatistiken bieten ein intuitives Dashboard für den Datenverkehr, das die Netzwerknutzung nach Anwendungen und Protokollen erkennt. Es unterstützt historische Trends für 1 Stunde, 1 Tag und 7 Tage, zeigt Nutzungsrankings an, überwacht den Datenverkehr pro Gerät und erlaubt das Blockieren unerwünschter Apps mit einem Klick.

**Hinweis**:

1. Datenstatistiken wirken nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.
2. Datenstatistiken können nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren der Datenstatistiken wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle

!!! note "Unterstützte Modelle"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **Data Statistics**.

Schalten Sie den Schalter oben rechts ein, um **Application Total Data** anzuzeigen.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Diese Seite besteht aus zwei Bereichen:

- **Top 10 Apps by Bandwidth Usage**: Dieser Bereich zeigt ein zeitbasiertes Trenddiagramm (z. B. für den vergangenen Tag), um den Bandbreitenverbrauch der 10 am stärksten genutzten Anwendungen im ausgewählten Zeitraum darzustellen.

    Bewegen Sie den Mauszeiger über das Diagramm, um den Datenverbrauch der 10 bandbreitenintensivsten Apps zu einem bestimmten Zeitpunkt anzuzeigen.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Dieser Bereich zeigt detaillierte Verkehrsmetriken für jede Anwendung an, einschließlich Download, Upload und Total Bandwidth. Suchen Sie bei Bedarf über die Suchleiste nach bestimmten Apps.

    Klicken Sie auf den Sortierpfeil neben der Spaltenüberschrift, um die Liste auf- oder absteigend zu sortieren.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Regeln zur Datenspeicherung

1. Verkehrsstatistiken werden alle 15 Sekunden im RAM gespeichert und jede Stunde im Flash abgelegt. Häufige Flash-Schreibvorgänge werden vermieden, um die Lebensdauer des Flash-Speichers zu schützen.

2. Ein Soft-Reboot führt nicht zu Datenverlust. Vor dem Neustart schreibt das System die Daten zuerst aus dem RAM in den Flash.

3. Ein Hard-Reboot (Netzstecker ziehen und wieder einstecken) oder ein Firmware-Upgrade (bei Beibehaltung der Einstellungen) kann zu Datenverlust von bis zu einer Stunde führen.

## Zeitbereich wechseln

Sie können den Zeitbereich je nach Bedarf zwischen Past Hour, Past Day und Past Week umschalten.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

Der gewählte Zeitbereich bestimmt, wie die Daten dargestellt werden:

- **Für eine detaillierte Ansicht (z. B. Past Hour)**: Das Diagramm zeigt feingranulare Schwankungen nahezu in Echtzeit. Spitzen wirken höher und Einbrüche steiler, sodass plötzliche Bandbreitenspitzen leichter zu erkennen sind.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Für einen allgemeinen Überblick (z. B. Past Day oder Past Week)**: Das Diagramm verdichtet die Daten über einen längeren Zeitraum. Die Kurven werden glatter und zeigen eher den allgemeinen Verkehrstrend als jede kleine Änderung.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

## Statistiken löschen

Klicken Sie oben links auf das Besensymbol, um die Statistiken bei Bedarf zu löschen.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Nach dem Löschen wird die Seite wie unten gezeigt aktualisiert. Möglicherweise müssen Sie einen Moment warten, bis neue Statistiken geladen werden.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
