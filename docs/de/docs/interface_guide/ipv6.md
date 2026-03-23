# IPv6

IPv6 (Internet Protocol Version 6) ist das neueste Internetprotokoll und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen deutlich größeren Pool an eindeutigen IP-Adressen, löst damit das Problem der Adressknappheit bei IPv4 und unterstützt die weltweit wachsende Zahl vernetzter Geräte.

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **IPv6**.

Auf dieser Seite können Sie IPv6 auf Ihrem Router aktivieren und konfigurieren.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

Wenn IPv6 aktiviert ist, erhalten WAN-Schnittstellen wie Ethernet ihre IPv6-Adressen über DHCPv6. Auf der Ethernet-Einstellungsseite können Sie die IPv6-Adresse auch manuell ändern.

**Hinweis**: Einige Funktionen (z. B. Firewall, GoodCloud, OpenVPN DCO) unterstützen IPv6 derzeit noch nicht. Wenn Sie diese Funktionen gleichzeitig mit IPv6 verwenden, kann dies zu Verbindungsproblemen führen.

Aktivieren Sie **Enable IPv6**, wählen Sie den Modus für Ihr Hauptnetzwerk und die Methode zur DNS-Erfassung aus und klicken Sie dann auf **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

Mit **Mode** stehen vier Modi zur Verfügung: **Native**, **Passthrough**, **NAT6** und **Static IPv6**.

- Native: Dieser Modus eignet sich, wenn der Router direkt eine öffentliche IPv6-Adresse erhält und automatisch IPv6-Adressen an die verbundenen Geräte vergibt. Dieser Modus deckt die IPv6-Zugriffsanforderungen der meisten Benutzer ab.

- Passthrough: Dieser Modus eignet sich, wenn IPv6-Pakete ohne Verarbeitung oder Umwandlung direkt durchgereicht werden müssen. Das ist beispielsweise bei bestimmten Netzwerkanwendungen oder Diensten der Fall, bei denen der Inhalt von IPv6-Paketen vollständig erhalten bleiben muss, damit sie weiterverarbeitet oder analysiert werden können. Er wird häufig von technischem Personal für Netzwerk-Debugging oder Sicherheitsanalysen verwendet.

- NAT6: Dieser Modus eignet sich für Szenarien, in denen ein Router als Verwaltungs-Gateway eingesetzt wird, um jedem Gerät im Netzwerk dynamische interne IPv6-Adressen zuzuweisen. In diesem Modus verbinden sich Endgeräte über ein Optical Network Terminal und erhalten eine IPv6-Adresse im lokalen Netzwerk.

- Static IPv6: Dieser Modus eignet sich für Geräte oder Dienste, die eine feste IPv6-Adresse benötigen, z. B. Server oder Netzwerkdrucker. Er stellt sicher, dass das Gerät immer dieselbe IPv6-Adresse verwendet, was Verwaltung und Zugriff erleichtert.

**DNS acquisition method** legt fest, wie der Router IPv6-DNS-Serveradressen erhält. Es gibt zwei Optionen: **Automatic** und **Manual**.

- Automatic: Der Router bezieht IPv6-DNS-Serveradressen dynamisch (z. B. über DHCPv6).

- Manual: Geben Sie benutzerdefinierte IPv6-DNS-Serveradressen ein. Da DNS jedoch zur Auflösung von Domainnamen in die zugehörigen IP-Adressen verwendet wird, kann eine manuelle DNS-Serverkonfiguration zu Problemen bei der Namensauflösung führen. Verwenden Sie diese Option daher mit Vorsicht.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
