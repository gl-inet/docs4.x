# Datenstatistiken

Die Datenstatistiken bieten ein intelligentes Dashboard zur Analyse des Datenverkehrs, das die Netzwerknutzung nach Anwendungen kategorisiert und visualisiert. So können Sie den aktuellen und den historischen Datenverkehr besser überwachen und kontrollieren.

**Hinweis**:

1. Diese Funktion ist derzeit nur auf **GL-MT5000 (Brume 3)** verfügbar.

2. Diese Funktion kann nicht zusammen mit Network Acceleration verwendet werden. Wenn Sie sie aktivieren, wird Network Acceleration automatisch deaktiviert, um einen ordnungsgemäßen Betrieb sicherzustellen.

---

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** > **Data Statistics**.

Aktivieren Sie den Schalter oben rechts, um **Application Total Data** anzuzeigen.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage**: Zeigt ein zeitbasiertes Trenddiagramm an, z. B. für den vergangenen Tag, um den Bandbreitenverbrauch der 10 am stärksten genutzten Anwendungen im ausgewählten Zeitraum darzustellen. 

    Wechseln Sie bei Bedarf die Zeitleiste zwischen Past Hour, Past Day und Past Week. 

- **App Traffic Statistics**: Zeigt detaillierte Verkehrsmetriken für jede Anwendung an, einschließlich Download-, Upload- und Total-Bandwidth-Daten. 

    Suchen Sie bei Bedarf über die Suchleiste nach bestimmten Apps.

## Regeln zur Datenspeicherung

1. Datenverkehrsstatistiken werden alle 15 Sekunden im RAM gespeichert und jede Stunde in den Flash geschrieben. Häufige Schreibzugriffe auf den Flash werden vermieden, um dessen Lebensdauer zu schützen.

2. Ein Soft-Reboot führt nicht zu Datenverlust. Das System schreibt die Daten zunächst aus dem RAM in den Flash, bevor es neu startet.

3. Ein Hard-Reboot (Netzstecker ziehen und wieder einstecken) oder ein Firmware-Upgrade (bei Beibehaltung der Einstellungen) kann zu einem Datenverlust von bis zu einer Stunde der zuletzt erfassten Daten führen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
