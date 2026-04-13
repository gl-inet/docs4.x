# So konfigurieren Sie Domain- und IP-Filterregeln für GL.iNet-Router über eine Online-Textdatei

Ab Firmware v4.7 unterstützen die folgenden Funktionen den Import von Regeln über eine Online-Textdatei-URL:

- VPN-Richtlinie basierend auf Ziel-Domain oder IP (unter VPN)
- Add a New Ruleset (unter Parental Control)

Dieses Tutorial erklärt, wie Sie eine Online-Textdatei verwenden, um Domain- und IP-Filterregeln für GL.iNet-Router zu importieren.

## Unterstützte URL- und Dateiformate

Die unterstützten URL-Formate sind die folgenden:

- Klartext-Datei-URLs (HTTP/HTTPS)
- GitHub Raw Content URL

Die unterstützten Dateitypen sind `.txt`, `.conf`, `.log` und andere Klartextformate.

**Hinweis**: Binärdateien werden nicht unterstützt, z. B. `.exe`, `.zip`, `.jpg`, `.png` usw.

## GitHub zum Hosten der Textdatei verwenden

Wenn Sie die Textdatei in einem öffentlichen GitHub-Repository hosten, stellen Sie sicher, dass Sie die Raw-Content-URL anstelle der normalen GitHub-URL verwenden.

Beispielsweise verweist die folgende GitHub-URL auf den Webinhalt und nicht auf den Rohinhalt:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Damit der Router den richtigen Inhalt herunterlädt, verwenden Sie die Raw-Content-URL im folgenden Format:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Auf diese Weise kann der Router den Klartextinhalt der Datei abrufen.

## Filterformate für VPN-Richtlinie (Domain/IP)

Die Funktion „VPN-Richtlinie basierend auf Ziel-Domain oder IP“ unterstützt in der Online-Textdatei die folgenden Filterformate:

* Domainname: Verwenden Sie den Domainnamen, z. B. `netflix.com` (gleicht alle Subdomains ab).
* Subdomain: Geben Sie die vollständige Subdomain an, z. B. `www.netflix.com` (gleicht nur diese Subdomain ab).
* CIDR-Bereich: Verwenden Sie die CIDR-Notation, um IP-Adressbereiche anzugeben, z. B. `192.168.10.0/24`.
* IPv4-Adresse: Geben Sie einzelne IPv4-Adressen an, z. B. `192.168.10.10`.

## Filterformate für Parental Control (Ruleset)

Die Funktion „Add a New Ruleset“ in Parental Control unterstützt in der Online-Textdatei die folgenden Filterformate:

* Domainname: Verwenden Sie den Domainnamen, z. B. `instagram.com` (gleicht alle Subdomains ab).
* Subdomain: Geben Sie die vollständige Subdomain an, z. B. `www.instagram.com` (gleicht nur diese Subdomain ab).

Verwenden Sie beim Erstellen der Online-Textdatei einen Filter pro Zeile. Der Router verarbeitet jede Zeile entsprechend dem angegebenen Format und wendet die zugehörigen Regeln auf die VPN- oder Parental-Control-Funktion an.

Wenn Sie diese Filterformate befolgen, können Sie die Online-Textdatei für die Konfiguration der VPN- und Parental-Control-Funktionen auf Ihrem Router einfach erstellen und pflegen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
