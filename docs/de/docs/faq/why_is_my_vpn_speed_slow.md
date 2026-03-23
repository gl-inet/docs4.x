# Warum ist meine VPN-Geschwindigkeit langsamer als erwartet?

Wenn Ihnen aufgefallen ist, dass Ihre VPN-Verbindung langsamer ist als die theoretische Höchstgeschwindigkeit (gemessen in einem idealen lokalen Netzwerk), ist das im praktischen Einsatz völlig normal.

VPNs sind darauf ausgelegt, Sicherheit und Datenschutz zu priorisieren, was die Geschwindigkeit grundsätzlich beeinflusst. Unter typischen Netzwerkbedingungen ist es normal, dass die VPN-Geschwindigkeit etwa 30-50 % der angegebenen Maximalgeschwindigkeit erreicht. Diese Abweichung entsteht durch mehrere Faktoren, die die Leistung beeinflussen. Im Folgenden erklären wir diese Faktoren und geben Ihnen einige Tipps zur Optimierung.

**Hinweis**: Die folgenden Methoden können helfen, die VPN-Geschwindigkeit zu verbessern, garantieren jedoch nicht, dass die beworbenen Werte erreicht werden, da die tatsächliche Leistung von mehreren Faktoren abhängt.

## CPU-Geschwindigkeit des Routers

Ein VPN verschlüsselt Ihre Daten zum Schutz der Privatsphäre, was zusätzliche Datenverarbeitung erfordert. Diese Ver- und Entschlüsselung kann Ihre Verbindung verlangsamen. Bitte wählen Sie einen Router mit schnellerer CPU, um Ihre VPN-Geschwindigkeit zu verbessern.

Wir haben die getesteten VPN-Geschwindigkeiten aller Modelle auf unserer [Produktseite](https://www.gl-inet.com/products/) aufgeführt. Bitte beachten Sie jedoch:

* Die Tests werden in einem lokalen Netzwerk durchgeführt. Die tatsächlichen Geschwindigkeiten können je nach Ihrer Netzwerkkonfiguration abweichen.
* Die Geschwindigkeiten von OpenVPN und WireGuard sind langsamer, wenn der Router als Server verwendet wird. Die oben genannten Ergebnisse wurden im Client-Modus gemessen.

## Entfernung zum Server

Wenn der VPN-Server weit von Ihrem physischen Standort entfernt ist, müssen die Daten eine längere Strecke zurücklegen. Das führt zu höherer Latenz und geringeren Geschwindigkeiten.

Unten sehen Sie ein Beispiel, das die Client-Geschwindigkeiten bei Verbindungen zu verschiedenen Serverstandorten zur gleichen Tageszeit zeigt.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Serverauslastung

Wenn viele Benutzer mit demselben VPN-Server verbunden sind, kann dieser überlastet sein, was für alle zu geringeren Geschwindigkeiten führt.

## Upload-Geschwindigkeit des Servers

Wenn Sie einen privaten VPN-Tunnel verwenden, ist die Upload-Geschwindigkeit des Internetdienstanbieters (ISP) auf der Serverseite der Engpass für die Download-Geschwindigkeit auf der Client-Seite, da der VPN-Client die Daten über den Server herunterlädt.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Unterschiede zwischen Protokollen

Verschiedene VPN-Protokolle wie OpenVPN oder WireGuard unterscheiden sich hinsichtlich Sicherheit und Geschwindigkeit. Manche können aufgrund ihrer Verschlüsselungsmethoden langsamer sein.

## Drosselung durch den ISP

Einige Internetdienstanbieter (ISPs) drosseln möglicherweise die Geschwindigkeit von Benutzern, die VPNs verwenden, insbesondere wenn sie eine hohe Datennutzung vermuten. Das kommt besonders häufig in einigen Entwicklungsländern oder kleineren Städten vor, in denen sich viele Benutzer eine begrenzte Internetinfrastruktur teilen.

## DNS

Einige Internetdienstanbieter (ISPs) können VPN-Domains möglicherweise nicht auflösen. Versuchen Sie, in den Netzwerkeinstellungen Ihres Routers [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) zu verwenden.

## MTU

Einige Internetdienstanbieter (ISPs), insbesondere Mobilfunkanbieter, können die Größe von Datenpaketen begrenzen. Versuchen Sie, die standardmäßige MTU in den VPN-Client-Optionen von 1420 auf 1380 oder 1280 zu ändern.

Für Firmware v4.8 und höher siehe bitte [hier](../interface_guide/vpn_dashboard.md/#tunnel-options).

Für Firmware v4.7 und früher siehe bitte [hier](../interface_guide/vpn_dashboard_v4.7.md#vpn-client-options).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

