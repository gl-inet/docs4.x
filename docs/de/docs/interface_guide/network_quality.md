# Netzwerkqualität

**Hinweis**: Diese Funktion wurde mit Firmware v4.11 eingeführt.

---

Navigieren Sie im linken Menü des webbasierten Admin-Panels zu **FLOW CONTROL** -> **Network Quality**.

Das Dashboard Network Quality überwacht die Qualität Ihrer Internetverbindung in Echtzeit. Es bewertet Reaktionsfähigkeit, Latenz und DNS-Leistung und erkennt gleichzeitig Verbindungsabbrüche und Paketverluste. Anhand dieser Messwerte können Sie Netzwerkprobleme erkennen, die reine Bandbreitentests möglicherweise nicht aufdecken.

Auf dieser Seite können Sie Ihre Internetverbindung anhand des Network Quality Score bewerten und bei Bedarf lokale Geschwindigkeitstests ausführen.

**Hinweis**:

1. Der GL.iNet Network Quality Score wird nach folgender gewichteter Formel berechnet:

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest ist ein lokaler Geschwindigkeitstest auf dem Router und unterliegt den Geschwindigkeitsbegrenzungen von Funktionen wie SQM und QoS.

## Network Quality Score

Dieser Abschnitt zeigt den allgemeinen Network Quality Score, der aus Response Score und Reliable Score berechnet wird. Sie können jeden Wert separat anzeigen. Das Feld zeigt außerdem zugehörige Messwerte wie Latenz, Jitter und Paketverlust sowie die aktuellen Download- und Upload-Raten in KB/s an. Standardmäßig verwendet das Dashboard `google.com` als Ziel für Internetverbindungs- und DNS-Auflösungstests.

Klicken Sie auf das Einstellungssymbol, um die Prüfziele zu konfigurieren.

![probe_targets_setting 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Als Prüfziele für Internet Reachability und DNS Resolution können Sie Baidu, Tencent, Alibaba, Google, Microsoft oder Cloudflare auswählen. Sie können auch manuell eine benutzerdefinierte Domain eingeben.

Die konfigurierten Ziele werden für Verbindungs- und DNS-Tests sowie zur Berechnung des Network Quality Score verwendet.

![probe_targets_setting 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: Dient zum Prüfen der Internetverbindung und zum Messen der Ende-zu-Ende-Latenz (Hop2-Ping-Ziel).

- **DNS Resolution Target**: Die bei DNS-Abfragen aufgelöste Domain. Es werden sowohl A- (IPv4) als auch AAAA-Einträge (IPv6) abgefragt.

## Speedtest

Dieser integrierte Geschwindigkeitstest verwendet Cloudflare Speed Test, um Download- und Upload-Geschwindigkeit, Ping-Latenz und Bufferbloat zu messen. Während des Tests werden Geschwindigkeitsdiagramme in Echtzeit angezeigt.

Klicken Sie auf **Run Speedtest**, um den Geschwindigkeitstest zu starten.

![speedtest 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Nach Abschluss des Tests werden die Ergebnisse auf der Seite angezeigt.

![speedtest 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
