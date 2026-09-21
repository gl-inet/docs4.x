# DNS

**Hinweis**: Der Inhalt dieser Seite wurde erstmals mit Firmware v4.11 eingeführt.

Wenn auf Ihrem Gerät eine andere Firmwareversion ausgeführt wird, wechseln Sie über die Auswahl unten zur entsprechenden Anleitung.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 und früher](dns.md)

</div>

---

Navigieren Sie im linken Menü des webbasierten Admin-Panels zu **DNS**.

Die DNS-Einstellungen Ihres Routers steuern, wie Domainnamen in IP-Adressen übersetzt werden. Auf dieser Seite können Sie die automatisch von vorgeschalteten Geräten bezogenen DNS-Server verwenden oder benutzerdefinierte Server festlegen. Außerdem können Sie DNS-Optionen konfigurieren und statische Hostregeln bearbeiten.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

Standardmäßig verwenden DNS-Abfragen für Datenverkehr, der der VPN-Richtlinie entspricht, die vom VPN-Tunnel bereitgestellten DNS-Server. Andere DNS-Abfragen verwenden die DNS-Server der aktiven WAN-Schnittstelle. Wenn Sie benutzerdefinierte DNS-Server festlegen, können Sie sie auf VPN-Tunnel, den Router selbst oder beide anwenden. Ist eine dieser Optionen aktiviert, werden DNS-Abfragen im ausgewählten Geltungsbereich über die angegebenen Server aufgelöst und nicht über die Server der jeweiligen Netzwerkschnittstelle. Sind keine benutzerdefinierten DNS-Server festgelegt, verwendet der Router die DNS-Server der jeweiligen Netzwerkschnittstelle.

## WAN-DNS

WAN DNS zeigt die DNS-Server an, die von den einzelnen WAN-Uplinks bezogen wurden, darunter Ethernet, Repeater, Tethering und Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Wenn ein WAN-Uplink aktiv ist, werden dessen DNS-Serveradressen wie unten dargestellt rechts angezeigt.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## VPN-DNS

VPN DNS zeigt die DNS-Server an, die von jedem aktiven VPN-Tunnel bezogen wurden.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Wenn ein VPN-Tunnel aktiv ist, folgen DNS-Abfragen des VPN-Datenverkehrs der VPN-DNS-Konfiguration, wie unten dargestellt.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## Manuelles DNS

Manual DNS unterstützt zwei Konfigurationstypen: **Static DNS** und **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: Ist diese Option aktiviert, wird für Pakete durch den VPN-Tunnel das benutzerdefinierte manuelle DNS anstelle der VPN-DNS-Einstellungen verwendet.

- **Apply Manual DNS to Router Itself**: Diese Option ist standardmäßig aktiviert. Ist sie eingeschaltet, verwenden integrierte Dienste des Routers (z. B. GoodCloud) die benutzerdefinierten manuellen DNS-Einstellungen.

### Statisches DNS

Mit Static DNS können Sie IPv4- oder IPv6-Adressen von DNS-Servern manuell eingeben. Sie können Adressen direkt eingeben oder voreingestellte öffentliche DNS-Server aus der Dropdown-Liste auswählen.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Sie können bis zu vier DNS-Serveradressen eingeben. Klicken Sie auf **Apply**, um die Änderungen zu speichern.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Verschlüsseltes DNS

Der Modus Encrypted DNS unterstützt mehrere DNS-Anbieter, darunter Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS und OpenDNS. Bei Bedarf können Sie auch manuell einen verschlüsselten DNS-Server angeben.

Wählen Sie zuerst den DNS Provider aus. Die übrigen Optionen ändern sich entsprechend Ihrer Auswahl.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Wenn Sie einen bestimmten DNS-Anbieter auswählen (z. B. NextDNS), wählen Sie als Verschlüsselungstyp DNS over TLS (DoT), DNS over HTTPS (DoH) oder DNS over QUIC (DoQ). DNS over QUIC (DoQ) wurde mit Firmware v4.9 eingeführt und ist nur verfügbar, wenn Control D, NextDNS oder AdGuard DNS als DNS-Anbieter verwendet wird.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Wenn Sie Manual als DNS-Anbieter auswählen, können Sie DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS oder DNSCrypt als Verschlüsselungstyp wählen.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Klicken Sie anschließend auf **Add a Server**, um mindestens einen DNS-Server hinzuzufügen. Sie können die URL oder das Stamp-Format des verschlüsselten DNS direkt eingeben. Eine Liste öffentlicher Server finden Sie unter [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Vergleich der Verschlüsselungstypen"

    1. **DNS over TLS (DoT)**

        Verschlüsselt DNS-Abfragen über einen dedizierten TLS-Port. Dadurch wird DNS-Datenverkehr vom normalen Web-Datenverkehr getrennt und kann von Netzbetreibern leicht erkannt werden.

    2. **DNS over HTTPS (DoH)**

        Überträgt DNS-Daten innerhalb des normalen HTTPS-Datenverkehrs. DNS-Abfragen vermischen sich mit gewöhnlichem Web-Datenverkehr, was einen hohen Datenschutz bietet und einfache Datenverkehrsfilter umgeht.

    3. **DNS over QUIC (DoQ)**

        Kapselt DNS im QUIC-Protokoll. Es bietet geringe Latenz, schnelle Wiederherstellung der Verbindung und stabile Leistung in instabilen Netzwerken.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Eine erweiterte Version von DoH. Sie trennt die IP-Adresse des Benutzers von den DNS-Abfragen und verhindert, dass Server und Netzwerkanbieter Ihre Browseraktivitäten verfolgen.

    5. **DNSCrypt**

        Ein ausgereiftes Verschlüsselungsprotokoll für DNS. Es authentifiziert und verschlüsselt DNS-Datenverkehr und legt den Schwerpunkt auf Manipulationsschutz und Kompatibilität mit älteren Netzwerkumgebungen.

## DNS-Optionen

Klicken Sie oben rechts auf **Options**, um erweiterte DNS-Einstellungen zu konfigurieren.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Sie können diese Optionen nach Bedarf ein- oder ausschalten.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: Das Aktivieren dieser Option kann dazu führen, dass private DNS-Abfragen fehlschlagen. Wenn Ihr Netzwerk ein Captive Portal verwendet, deaktivieren Sie diese Option.

- **Override DNS Settings of All Clients**: Ist diese Option aktiviert, überschreibt der Router die unverschlüsselten DNS-Einstellungen aller Clients.

## Hosts bearbeiten

Klicken Sie oben rechts auf **Edit Hosts**, um statische Hostregeln anzupassen.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Der Router priorisiert diese Hostregeln beim Auflösen von Anfragen verbundener Clients.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
