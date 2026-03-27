# Einführung in die AmneziaWG-Verschleierungsparameter

AmneziaWG ist ein WireGuard-basiertes VPN-Protokoll mit integrierter Verschleierung des Datenverkehrs. Seine Verschleierungsparameter steuern, wie der Datenverkehr getarnt wird, um einer Erkennung durch strenge Netzwerkkontrollen zu entgehen. Nachfolgend finden Sie eine detaillierte Erläuterung der Versionsunterschiede von AmneziaWG, der Verschleierungsparameter, ihrer Einschränkungen und der empfohlenen Einstellungen.

## AmneziaWG V2.0

Im Vergleich zu AmneziaWG v1.0 bietet v2.0 eine stärkere Verschleierung, indem neue Parameter (**S3~S4**) hinzugefügt und dynamische Header für Pakettypen verwendet werden (**H1~H4** als Bereiche statt als feste Werte). Darüber hinaus unterstützt AmneziaWG 2.0 die Parameter **I1~I5**, die vor jedem Handshake formatierte UDP-Pakete senden, um AmneziaWG-Datenverkehr als gewöhnlichen Nicht-VPN-Datenverkehr zu tarnen. So lässt sich Deep Packet Inspection wirksam umgehen und die Konnektivität in eingeschränkten Netzwerken verbessern.

Diese Erweiterungen erschweren die Erkennung des VPN-Datenverkehrs und bewahren gleichzeitig die hohe Geschwindigkeit und geringe Latenz von WireGuard.

So erkennen Sie die AmneziaWG-Version:

- **V1.0**: Keine Parameter S3~S4; H1~H4 sind einzelne feste Ganzzahlen.
- **V2.0**: Enthält die Parameter **S3~S4**; **H1~H4** sind als Zahlenbereiche definiert; unterstützt die Parameter **I1~I5**.

**Hinweis**: Die Parameter I1-I5 werden nicht automatisch generiert. Benutzer können sie manuell als zusätzliche Zeilen in der VPN-Konfigurationsdatei ergänzen, damit AmneziaWG-Datenverkehr wie andere gängige Protokolle wie QUIC oder WebRTC aussieht.

## Überblick über die Parameter {#parameter-overview}

| Parameter | Beschreibung | Einschränkungen | Automatisch generiert |
| --------- | ------------ | --------------- | --------------------- |
| Jc | Anzahl der Junk-Pakete, bevor der Client den Handshake initiiert (zur Störung der Erkennung von Verkehrsmustern) | 1~128 | 4~12 |
| Jmin | Mindestgröße zufälliger Junk-Pakete (Bytes); muss zusammen mit Jmax konfiguriert werden, um die Größe der Junk-Pakete festzulegen | 0 ≤ Jmin < Jmax < 65535 | 0 <= jmin < jmax < 1280 |
| Jmax | Maximale Größe zufälliger Junk-Pakete | 0 ≤ Jmin < Jmax < 65535 | 0≤ Jmin < Jmax < 1280 |
| S1 | Zufällige Präfixe für Init-Pakete | 0 ≤ S1 ≤ 1132 | 15~150 |
| S2 | Zufällige Präfixe für Response-Pakete | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3 | Zufällige Präfixe für Cookie-Pakete | 0 ≤ S3 ≤ 1216 | 15~150 |
| S4 | Zufällige Präfixe für Datenpakete | 0 ≤ S4 ≤ 32 | 0~32 |
| H1~H4 | Dynamische Header für Pakettypen; Zufallswerte (v1.0) oder Bereiche (v2.0) | 5~2147483647; H1, H2, H3 und H4 müssen unterschiedlich sein | 5~2147483647 |
| I1~I5 | Signaturpakete zur Protokollimitierung | beliebiger Hex-Blob | N/A |

Referenzen: [Offizielle AmneziaWG-Dokumentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.