---
title: Wi-Fi-Abdeckung, Access Points und Sendeleistung verstehen
---

# Wi-Fi-Abdeckung, Access Points und Sendeleistung verstehen

Viele Benutzer gehen davon aus, dass eine höhere Sendeleistung eines Routers immer die Wi-Fi-Abdeckung und Leistung verbessert.

Eine höhere Sendeleistung vergrößert zwar in der Regel die Abdeckung eines einzelnen Routers, die maximale Sendeleistung ist in Netzwerken mit mehreren Access Points (APs), Mesh-Knoten oder Enterprise-Wi-Fi-Bereitstellungen jedoch nicht immer ideal.

Ein Verständnis von Abdeckungszellen, Roaming, Kanalplanung und Sendeleistung kann helfen, die WLAN-Leistung zu verbessern.

## Einzelner Router gegenüber mehreren Access Points

### Einzelner Router

Wenn nur ein Router die Wi-Fi-Abdeckung bereitstellt:

- Eine höhere Sendeleistung vergrößert in der Regel die Abdeckung.
- Client-Geräte können auch in größerer Entfernung eine nutzbare Verbindung aufrechterhalten.
- Eine geringere Sendeleistung reduziert normalerweise das empfangene Signal und das Downlink-Signal-Rausch-Verhältnis (SNR).

Für die meisten Benutzer mit einem einzelnen Router wird empfohlen, die Sendeleistung auf der Standard- oder Automatik-Einstellung zu belassen.

Das Verringern der Sendeleistung Ihres Routers reduziert nicht die HF-Energie, die von benachbarten Wi-Fi-Netzwerken ausgesendet wird. Deren Router und APs senden weiterhin mit derselben Leistung.

### Mehrere Access Points

Wenn mehrere APs bereitgestellt werden, besteht das Ziel nicht unbedingt darin, den Abdeckungsbereich jedes AP zu maximieren.

Stattdessen sollen mehrere kleinere, klar definierte Abdeckungszellen entstehen, die sich nur so weit überlappen, dass eine durchgehende Abdeckung und zuverlässiges Roaming möglich sind.

Geeignete AP-Positionierung, Sendeleistung und Kanalauswahl sind dabei gleichermaßen wichtig.

## Überlappung von Abdeckungszellen

Wenn jeder AP mit maximaler Leistung sendet, können sich die Abdeckungsbereiche zu stark überlappen.

Ein Client-Gerät kann mit einem entfernten AP verbunden bleiben, obwohl ein näherer AP ein stärkeres Signal bietet. Dies wird häufig als **Sticky Client** bezeichnet.

Ein Client, der mit dem falschen AP verbunden ist, kann Folgendes erleben:

- Niedrigeres SNR
- Niedrigere Modulations- und Codierungsraten
- Mehr Wiederholungsübertragungen
- Geringerer Durchsatz
- Höhere Latenz

Eine Reduzierung der AP-Sendeleistung kann die Abdeckungszellen verkleinern und Client-Geräte dazu anregen, früher zu roamen.

## Client-Roaming verstehen

In den meisten Wi-Fi-Netzwerken entscheidet das Client-Gerät, wann es roamt.

Der Router oder AP kann Roaming-Unterstützung bereitstellen, aber die endgültige Entscheidung, einen AP zu verlassen und sich mit einem anderen zu verbinden, trifft normalerweise das Telefon, der Laptop, das Tablet oder ein anderes Client-Gerät.

Verschiedene Client-Geräte verwenden unterschiedliche Roaming-Schwellenwerte und Algorithmen. Ein Gerät kann daher mit einem AP verbunden bleiben, solange es die Verbindung als nutzbar bewertet, selbst wenn ein anderer AP ein stärkeres Signal bietet.

Das Reduzieren übermäßiger Abdeckungsüberlappung kann Clients helfen, bessere Roaming-Entscheidungen zu treffen.

## Spatial Reuse

Wi-Fi ist ein gemeinsam genutztes Medium.

Vor dem Senden prüfen Wi-Fi-Geräte, ob der Kanal bereits genutzt wird. Wenn APs auf demselben Kanal einander über einen großen Bereich hören können, verbringen sie möglicherweise mehr Zeit damit, auf einen freien Kanal zu warten.

Dadurch verringern sich nutzbare Airtime und Gesamtdurchsatz.

Eine angemessene Reduzierung der Sendeleistung kann es APs auf demselben Kanal in unterschiedlichen physischen Bereichen ermöglichen, unabhängiger zu arbeiten. Dies wird als **Spatial Reuse** bezeichnet.

Spatial Reuse bedeutet nicht, dass eine geringere AP-Sendeleistung die von benachbarten Netzwerken ausgesendeten Störungen reduziert. Richtig dimensionierte Abdeckungszellen können stattdessen unnötige Kanalbelegung verringern und die Wiederverwendung desselben Kanals in ausreichend getrennten Bereichen ermöglichen.

## Kanalplanung

Sendeleistung und Kanalauswahl sollten gemeinsam betrachtet werden.

### 2,4 GHz

Das 2,4-GHz-Band hat relativ wenige überlappungsfreie Kanäle.

In vielen regulatorischen Regionen werden die Kanäle 1, 6 und 11 häufig mit einer Kanalbreite von 20 MHz verwendet.

Wenn möglich, sollten nahe beieinanderliegende APs unterschiedliche, überlappungsfreie Kanäle verwenden.

### 5 GHz und 6 GHz

Die 5-GHz- und 6-GHz-Bänder bieten mehr verfügbare Kanäle, sodass sich nahe beieinanderliegenden APs leichter unterschiedliche Kanäle zuweisen lassen.

Überlappungsfreie Kanäle reduzieren Gleichkanal-Konkurrenz, obwohl eine übermäßige Abdeckungsüberlappung das Roaming-Verhalten weiterhin beeinflussen kann.

Verfügbare Kanäle hängen vom Routermodell, Land oder Region, der Kanalbreite und lokalen Vorschriften ab.

## Kabelgebundene APs und Mesh-Netzwerke

### Kabelgebundene Access Points

Eine kabelgebundene Ethernet-Verbindung zwischen dem Hauptrouter und zusätzlichen APs ist im Allgemeinen die bevorzugte Bereitstellung.

Da die kabelgebundene Verbindung den Backhaul-Datenverkehr überträgt, kann die Wi-Fi-Sendeleistung vor allem für Client-Abdeckung, Roaming und Spatial Reuse angepasst werden.

### Mesh mit kabelgebundenem Backhaul

Mesh-Knoten mit kabelgebundenem Backhaul können ähnlich wie kabelgebundene APs optimiert werden.

Die Sendeleistung kann angepasst werden, um übermäßige Zellüberlappung zu reduzieren und gleichzeitig eine durchgehende Abdeckung beizubehalten.

### Mesh mit drahtlosem Backhaul

In einer drahtlosen Mesh-Bereitstellung können die Wi-Fi-Funkmodule auch den Datenverkehr zwischen Mesh-Knoten übertragen.

Eine zu starke Reduzierung der Sendeleistung kann die drahtlose Backhaul-Verbindung schwächen und die Gesamtleistung verringern.

Stellen Sie bei drahtlosem Backhaul sicher, dass Mesh-Knoten eine starke und stabile Verbindung zueinander aufrechterhalten.

## Beispiel für eine Multi-AP-Bereitstellung

Betrachten Sie zwei per Ethernet verbundene GL.iNet-Router:

- Der primäre Router stellt Routing, DHCP, NAT und Firewall-Dienste bereit.
- Der zweite Router arbeitet im Access-Point-Modus.
- Beide Geräte senden denselben Wi-Fi-Netzwerknamen und dieselben Sicherheitseinstellungen.
- Nahe beieinanderliegende APs verwenden unterschiedliche, überlappungsfreie Kanäle.
- Die Sendeleistung wird so angepasst, dass sich die Abdeckungszellen ausreichend für Roaming überlappen, aber nicht übermäßig.

Die ideale Sendeleistung hängt von Baumaterialien, AP-Positionierung, Client-Geräten, benachbarten Wi-Fi-Netzwerken und dem gewünschten Abdeckungsbereich ab.

Es gibt keinen einzelnen Sendeleistungswert, der für jede Bereitstellung richtig ist.

## Häufige Missverständnisse

### Maximale Sendeleistung bietet immer das beste Wi-Fi

Maximale Leistung bietet in der Regel den größten Abdeckungsbereich, kann in Multi-AP-Bereitstellungen jedoch übermäßige Überlappung und schlechtes Roaming-Verhalten verursachen.

### Geringere Sendeleistung reduziert eingehende Störungen

Das Verringern der Sendeleistung Ihres AP reduziert das von Ihrem eigenen AP erzeugte Signal. Es reduziert nicht die Leistung, mit der benachbarte Router oder APs senden.

### Geringere Sendeleistung macht den AP-Empfänger empfindlicher

Sendeleistung und Empfängerempfindlichkeit sind getrennte Eigenschaften. Eine geringere Sendeleistung verbessert nicht grundsätzlich die Fähigkeit des AP, Client-Übertragungen zu empfangen.

### Client-Geräte verbinden sich immer mit dem nächsten AP

Client-Geräte wählen APs normalerweise mithilfe eigener interner Algorithmen aus und roamen zwischen ihnen. Sie können mit einem weiter entfernten AP verbunden bleiben, selbst wenn ein näherer AP verfügbar ist.

## Empfohlene Ausgangspunkte

| Bereitstellung | Empfehlung |
| --- | --- |
| Einzelner Router | Belassen Sie die Sendeleistung auf der Standard- oder Automatik-Einstellung. |
| Zwei oder mehr kabelgebundene APs | Verwenden Sie überlappungsfreie Kanäle und passen Sie die Sendeleistung an, um übermäßige Überlappung zu reduzieren. |
| Mesh mit kabelgebundenem Backhaul | Optimieren Sie Abdeckungszellen für zuverlässiges Roaming. |
| Mesh mit drahtlosem Backhaul | Vermeiden Sie eine Leistungsreduzierung, die die Backhaul-Verbindung schwächen könnte. |

Testen Sie nach Änderungen die Leistung an mehreren Standorten und prüfen Sie:

- Signalstärke
- Upload- und Download-Durchsatz
- Latenz
- Roaming zwischen APs
- Qualität des drahtlosen Backhauls, falls zutreffend

Ändern Sie jeweils nur eine Einstellung, damit deren Wirkung genau gemessen werden kann.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com) oder [kontaktieren Sie uns](https://www.gl-inet.com/contact-us/).
