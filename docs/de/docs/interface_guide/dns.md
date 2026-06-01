# DNS

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **DNS**.

Die DNS-Einstellungen Ihres Routers steuern, wie Domainnamen in IP-Adressen aufgelöst werden. Auf dieser Seite können Sie die DNS-Server verwenden, die automatisch von übergeordneten Geräten bezogen werden, oder eigene DNS-Server festlegen und DNS-Prioritäten konfigurieren.

Wenn Sie eigene DNS-Server festlegen, werden alle DNS-Anfragen über diese Server aufgelöst, anstatt die DNS-Server zu verwenden, die über die einzelnen Netzwerkschnittstellen bezogen wurden. Andernfalls werden die DNS-Einstellungen genutzt, die für jede Schnittstelle konfiguriert sind.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Das Aktivieren dieser Option kann dazu führen, dass private DNS-Auflösungen fehlschlagen. Wenn Ihr Netzwerk ein Captive Portal verwendet, deaktivieren Sie diese Option bitte.

- **Override DNS Settings for All Clients:** Wenn diese Option aktiviert ist, überschreibt Ihr Router unverschlüsselte DNS-Einstellungen für alle Clients.

- **Allow Custom DNS to Override VPN DNS:** Wenn diese Option aktiviert ist und Sie eigene DNS-Server festgelegt haben, werden Pakete, die über den VPN-Tunnel übertragen werden, mit dem benutzerdefinierten DNS-Override aufgelöst statt mit den DNS-Servereinstellungen aus den VPN-Verbindungen.

## DNS-Server-Einstellungen

Es gibt vier Modi: Automatic, Encrypted DNS, Manual DNS und DNS Proxy.

### Automatic

In diesem Modus verwendet der Router automatisch den DNS-Server, der vom Upstream-Gerät bereitgestellt wird (z. B. ISP-Modem oder primärer Router), oder die DNS-Einstellungen, die der jeweiligen Netzwerkschnittstelle entsprechen.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS

Bitte beachten Sie die folgenden Anweisungen entsprechend Ihrer Firmware-Version.

!!! note "Für Firmware v4.8 und früher"

    Es stehen vier Verschlüsselungstypen zur Verfügung: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS und Oblivious DNS over HTTPS.

    Wählen Sie zuerst den **Encryption Type** aus. Die übrigen Optionen ändern sich entsprechend Ihrer Auswahl.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - **Für DNS over TLS (DoT)** wählen Sie bitte einen DNS-Anbieter aus **Control D**, **NextDNS** und **Cloudflare**.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - **Für die anderen drei Typen (also DNSCrypt-Proxy, DNS over HTTPS und Oblivious DNS over HTTPS)** wählen Sie bitte mindestens einen DNS-Server aus dem Repository aus.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

!!! note "Für Firmware v4.9 und später"

    Zusätzlich zu Control D, NextDNS und Cloudflare stehen im Modus Encrypted DNS jetzt weitere DNS-Anbieter zur Verfügung, darunter **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** und **OpenDNS**. Sie können bei Bedarf auch manuell einen verschlüsselten DNS-Server angeben.

    Wählen Sie zuerst den **DNS Provider** aus. Die übrigen Optionen ändern sich entsprechend Ihrer Auswahl.

    ![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

    - Wenn Sie einen bestimmten DNS-Anbieter auswählen (z. B. NextDNS), wählen Sie bitte einen Verschlüsselungstyp aus **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** und **DNS over QUIC (DoQ)**. Beachten Sie, dass DNS over QUIC (DoQ) in Firmware v4.9 eingeführt wurde und nur verfügbar ist, wenn Sie Control D, NextDNS oder AdGuard DNS als DNS-Anbieter verwenden.

        ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

    - Wenn Sie **Manual** als DNS-Anbieter auswählen, wählen Sie bitte einen Verschlüsselungstyp aus **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** und **DNSCrypt**.

        ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

        Klicken Sie anschließend auf **Add a Server**, um mindestens einen DNS-Server hinzuzufügen. Sie können die URL oder das Stamp-Format des verschlüsselten DNS direkt eingeben. Eine Liste öffentlicher Server finden Sie unter [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

        ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Vergleich der Verschlüsselungstypen

1. **DNS over TLS (DoT)**

    Verschlüsselt DNS-Anfragen über einen dedizierten TLS-Port. Dadurch wird DNS-Datenverkehr vom regulären Webverkehr getrennt und kann von Netzbetreibern leicht erkannt werden.

2. **DNS over HTTPS (DoH)**

    Überträgt DNS-Daten innerhalb des normalen HTTPS-Datenverkehrs. Dadurch werden DNS-Anfragen mit gewöhnlichem Webverkehr vermischt, was für mehr Privatsphäre sorgt und einfache Verkehrsfilter umgeht.

3. **DNS over QUIC (DoQ)**

    Kapselt DNS im QUIC-Protokoll. Es bietet geringe Latenz, schnelle Wiederverbindungen und stabile Leistung in instabilen Netzwerken.

4. **Oblivious DNS over HTTPS (ODoH)**

    Eine erweiterte Version von DoH. Dabei wird die Benutzer-IP von den DNS-Anfragen getrennt, sodass weder Server noch Netzbetreiber Ihr Surfverhalten nachvollziehen können.

5. **DNSCrypt**

    Ein ausgereiftes Verschlüsselungsprotokoll für DNS. Es authentifiziert und verschlüsselt DNS-Datenverkehr und legt den Schwerpunkt auf Manipulationsschutz und Kompatibilität mit älteren Netzwerkumgebungen.

### Manual DNS

In diesem Modus können Sie den DNS-Server Ihres Routers individuell festlegen. Wählen Sie dazu mindestens einen DNS Server aus der Dropdown-Liste für Ihren Router aus.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy

In diesem Modus leitet der Router alle DNS-Anfragen aus dem LAN an die von Ihnen angegebene Proxy-Server-Adresse weiter (z. B. 8.8.8.8#53). Das kann nützlich sein, wenn in Ihrem Netzwerk ein anderer DNS-Server oder Pi-hole läuft.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Hosts bearbeiten

Sie können oben rechts auf die Schaltfläche **Edit Hosts** klicken, um statische Host-Regeln anzupassen.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Der Router priorisiert diese Host-Regeln bei der Auflösung von Anfragen verbundener Clients.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
