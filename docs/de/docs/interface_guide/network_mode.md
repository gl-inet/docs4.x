# Netzwerkmodus

Öffnen Sie auf der linken Seite des Web-Admin-Panels **NETWORK** -> **Network Mode**.

Der Netzwerkmodus bezeichnet die verschiedenen Betriebsrollen und Funktionen, die ein Router für unterschiedliche Netzwerkszenarien übernehmen kann. Diese Modi sind auf Einsatzfälle von der Wi-Fi-Abdeckung zu Hause bis hin zu Multi-Link-Netzwerken auf Unternehmensebene zugeschnitten. Je nach Modus werden bestimmte Routerfunktionen deaktiviert oder aktiviert, um die Leistung zu optimieren.

!!! note

    1. Wenn Sie den Netzwerkmodus des Routers ändern, müssen Sie möglicherweise alle Client-Geräte erneut verbinden.
    
    2. **Wenn sich Ihr Router im Modus Access Point / WDS / Bridge befindet, können Sie nicht über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen.** Stattdessen müssen Sie sich am Upstream-Router anmelden, um die IP-Adresse zu finden, die er diesem Router zugewiesen hat, und diese IP-Adresse anschließend für den Zugriff auf das Web-Admin-Panel verwenden. Wenn Sie keinen Zugriff auf den Upstream-Router haben, halten Sie die Reset-Taste 4 Sekunden lang gedrückt, um zum Standardmodus Router zurückzukehren.

    3. **Im Extender-Modus** können Sie weiterhin über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen.
    
    4. **Im Non-Router-Modus sind die folgenden Funktionen nicht verfügbar**: Access Control (Allowlist und Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Für Modelle mit Wi-Fi

Mit Ausnahme einiger spezieller Modelle verfügen die meisten GL.iNet-WLAN-Router über Wi-Fi-Funktionalität.

Modelle mit Wi-Fi-Funktion unterstützen in der Regel vier Netzwerkmodi: Router, Access Point, Extender und WDS. Beachten Sie, dass einige Modelle den WDS-Modus nicht unterstützen.

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: Dies ist der Standardbetriebsmodus für die meisten Router im Heim- und Kleinbürobereich. Er ist dafür ausgelegt, ein privates lokales Netzwerk zu erstellen und als dediziertes Gateway zwischen dem öffentlichen Internet und den verbundenen Geräten zu dienen.

    Im Router-Modus aktiviert das Gerät Kernfunktionen wie NAT, DHCP und eine integrierte Firewall. Es stellt die Verbindung zu einer Upstream-Leitung wie einem Glasfaser-Breitbandanschluss her, weist verbundenen Geräten automatisch private IP-Adressen zu und sorgt für Netzwerksicherheit für das gesamte private Netzwerk.
    
    ---

- **Access Point**: In diesem Modus kann ein Router über ein LAN-Kabel mit einem kabelgebundenen Netzwerk verbunden werden und drahtlose Signale aussenden. So wird die Wi-Fi-Abdeckung in großen Bereichen erweitert, damit mehr Geräte auf das Netzwerk zugreifen können.

    Im Access-Point-Modus deaktiviert der Router seine NAT- und DHCP-Funktionen und arbeitet ausschließlich als Sender für Funksignale und als Switch, nicht als eigenständiges Gateway.

    Nach dem Wechsel in den Access-Point-Modus können Sie nicht mehr über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen. Stattdessen müssen Sie sich am Upstream-Router anmelden, um die IP-Adresse zu finden, die er diesem AP zugewiesen hat, und diese IP-Adresse anschließend für den Zugriff auf das Web-Admin-Panel verwenden. Wenn Sie keinen Zugriff auf den Upstream-Router haben, halten Sie die Reset-Taste 4 Sekunden lang gedrückt, um zum Standardmodus Router zurückzukehren.

    ---

- **Extender**: Dieser Modus wurde entwickelt, um die Wi-Fi-Abdeckung eines bestehenden Drahtlosnetzwerks zu erweitern und Funklöcher in Bereichen mit schlechter Verbindung zu beseitigen.

    Er ermöglicht es dem Router, Signale vom Hauptrouter drahtlos zu empfangen, zu verstärken und erneut auszusenden. Im Gegensatz zum Access-Point-Modus ist dafür keine Kabelverbindung zum Hauptrouter erforderlich. Allerdings kann sich die verfügbare Bandbreite halbieren, da das Gerät gleichzeitig Signale empfangen und senden muss.

    Im Extender-Modus können Sie weiterhin über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen.

    ---

- **WDS**: Der Modus Wireless Distribution System (WDS) ähnelt dem Extender-Modus, da er die Wi-Fi-Abdeckung drahtlos erweitert. Zusätzlich unterstützt er jedoch eine drahtlose Bridge-Verbindung zwischen mehreren kompatiblen Routern. Er wird empfohlen, wenn der Upstream-Router über eine WDS-Funktion verfügt.
    
    Dieser Modus eignet sich ideal für Szenarien wie mehrstöckige Gebäude oder kleine Bürogelände, in denen mehrere Router zusammenarbeiten müssen, um ein einheitliches Drahtlosnetzwerk zu bilden. Im Gegensatz zum Extender-Modus, der Signale nur von einem Hauptrouter an einen einzelnen Extender weiterleitet, können im WDS-Modus verbundene Router sowohl senden als auch empfangen. Dadurch ist eine nahtlose Abdeckung über größere Bereiche mit mehreren Signalpunkten möglich.

    Nach dem Wechsel in den WDS-Modus können Sie nicht mehr über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen. Stattdessen müssen Sie sich am Upstream-Router anmelden, um die IP-Adresse zu finden, die er diesem WDS-Router zugewiesen hat, und diese IP-Adresse anschließend für den Zugriff auf das Web-Admin-Panel verwenden. Wenn Sie keinen Zugriff auf den Upstream-Router haben, halten Sie die Reset-Taste 4 Sekunden lang gedrückt, um zum Standardmodus Router zurückzukehren.

## Für Modelle ohne Wi-Fi

GL-MT2500/GL-MT2500A unterstützt weder Access Point, Extender noch WDS, da diese Modelle keine Wi-Fi-Funktion besitzen. Unterstützt werden jedoch Router und Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: Dies ist der Standardbetriebsmodus für die meisten Router im Heim- und Kleinbürobereich. Er ist dafür ausgelegt, ein privates lokales Netzwerk (LAN) zu erstellen und als dediziertes Gateway zwischen dem öffentlichen Internet und den verbundenen Geräten zu dienen.

    Im Router-Modus aktiviert das Gerät Kernfunktionen wie NAT, DHCP und eine integrierte Firewall. Es stellt die Verbindung zu einer Upstream-Leitung wie einem Glasfaser-Breitbandanschluss her, weist verbundenen Geräten automatisch private IP-Adressen zu und sorgt für Netzwerksicherheit für das gesamte private Netzwerk.
    
    ---

- **Bridge**: Ermöglicht dem Router, sich mit einem kabelgebundenen Netzwerk zu verbinden und als Bridge zwischen Netzwerkgeräten zu arbeiten.

    In diesem Modus arbeitet der Router im Wesentlichen als Switch und leitet Daten zwischen verbundenen Geräten weiter, ohne NAT-, Firewall- oder DHCP-Dienste auszuführen. Dadurch können Geräte im selben Netzwerk nahtlos miteinander kommunizieren, da der Router nur als Verbindungspunkt und nicht als Netzwerk-Gateway dient.

    Nach dem Wechsel in den Bridge-Modus können Sie nicht mehr über die ursprüngliche LAN-IP-Adresse auf das Web-Admin-Panel zugreifen. Stattdessen müssen Sie sich am Upstream-Router anmelden, um die IP-Adresse zu finden, die er diesem Bridge-Router zugewiesen hat, und diese IP-Adresse anschließend für den Zugriff auf das Web-Admin-Panel verwenden. Wenn Sie keinen Zugriff auf den Upstream-Router haben, halten Sie die Reset-Taste 4 Sekunden lang gedrückt, um zum Standardmodus Router zurückzukehren.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
