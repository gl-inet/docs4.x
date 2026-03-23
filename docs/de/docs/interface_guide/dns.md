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

- **Automatic**: Der Router verwendet automatisch den DNS-Server, der vom Upstream-Gerät bereitgestellt wird (z. B. ISP-Modem oder primärer Router), oder die DNS-Einstellungen, die der jeweiligen Netzwerkschnittstelle entsprechen.

    ![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

- **Encrypted DNS**: Es stehen vier Verschlüsselungstypen zur Verfügung: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS und Oblivious DNS over HTTPS.

    ![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

    - Wählen Sie für DNS over TLS einen DNS-Anbieter aus Control D, NextDNS und Cloudflare aus.

        ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

    - Für die anderen drei Typen, also DNSCrypt-Proxy, DNS over HTTPS und Oblivious DNS over HTTPS, wählen Sie mindestens einen DNS Server aus dem Repository aus.

        ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

- **Manual DNS**: Wählen Sie aus der Dropdown-Liste mindestens einen DNS Server für Ihren Router aus.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

- **DNS Proxy**: Der Router leitet alle DNS-Anfragen aus dem LAN an die von Ihnen angegebene Proxy-Server-Adresse weiter (z. B. 8.8.8.8#53). Das kann nützlich sein, wenn in Ihrem Netzwerk ein anderer DNS-Server oder Pi-hole läuft.

    ![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Hosts bearbeiten

Anfragen von Clients werden bevorzugt mithilfe der statischen DNS-Regeln aufgelöst, die Sie in Hosts festlegen.

![hosts](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
