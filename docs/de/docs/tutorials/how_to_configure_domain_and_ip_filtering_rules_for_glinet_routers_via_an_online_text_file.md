# So konfigurieren Sie Domain- und IP-Filterregeln für GL.iNet-Router über eine Online-Textdatei

Ab Firmware v4.7.0 unterstützen die Funktion „VPN-Richtlinie basierend auf Ziel-Domain oder IP“ im VPN-Feature und die Funktion „Add a New Ruleset“ im Feature **Parental Control** den Import von Regeln über einen Link zu einer Online-Textdatei. Dieser Artikel beschreibt das Format dieser Textdatei.

## Beschreibung des URL-Formats

### Unterstützte und nicht unterstützte URL-Formate

- Unterstützte Dateiformate für die Textdatei: `.txt`, `.conf`, `.log` usw.
- Nicht unterstützte Dateiformate: Binärdateien wie `.exe`, `.zip`, `.jpg` usw.

### GitHub zum Hosten der Textdatei verwenden

Wenn Sie die Textdatei in einem öffentlichen GitHub-Repository hosten, stellen Sie sicher, dass Sie die URL des Rohinhalts statt der normalen GitHub-URL verwenden.

Beispielsweise verweist die folgende GitHub-URL auf den Webinhalt und nicht auf den Rohinhalt:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Damit der Router den richtigen Inhalt herunterlädt, verwenden Sie die Rohinhalts-URL im folgenden Format:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Auf diese Weise kann der Router den Klartextinhalt der Datei abrufen.

## Filterformate für die VPN-Richtlinie basierend auf Ziel-Domain oder IP

Die Funktion „VPN-Richtlinie basierend auf Ziel-Domain oder IP“ unterstützt in der Online-Textdatei die folgenden Filterformate:

* Domainnamenformat: Verwenden Sie den Domainnamen, z. B. `netflix.com`, um alle Subdomains von `netflix.com` abzugleichen.
* Subdomain-Format: Geben Sie die vollständige Subdomain an, z. B. `www.netflix.com`, um nur diese bestimmte Subdomain abzugleichen.
* CIDR-Format: Verwenden Sie die CIDR-Notation, um IP-Adressbereiche anzugeben, z. B. `192.168.10.0/24`.
* IPv4-Adressformat: Geben Sie einzelne IPv4-Adressen an, z. B. `192.168.10.10`.

## Filterformate für „Parental Control Add a New Ruleset“

Die Funktion „Add a New Ruleset“ in **Parental Control** unterstützt in der Online-Textdatei die folgenden Filterformate:

* Domainnamenformat: Verwenden Sie den Domainnamen, z. B. `instagram.com`, um alle Subdomains von `instagram.com` abzugleichen.
* Subdomain-Format: Geben Sie die vollständige Subdomain an, z. B. `www.instagram.com`, um nur diese bestimmte Subdomain abzugleichen.

Verwenden Sie beim Erstellen der Online-Textdatei pro Zeile genau einen Filter. Der Router verarbeitet jede Zeile entsprechend dem angegebenen Format und wendet die zugehörigen Regeln auf die VPN- oder Parental-Control-Funktion an.

## Beispiele

Für „VPN-Richtlinie basierend auf Ziel-Domain oder IP“:

```
netflix.com
www.hulu.com
192.168.10.0/24
192.168.10.10
```

Für „Parental Control Add a New Ruleset“:

```
instagram.com
facebook
x.com
snapchat
```

Wenn Sie diese Filterformate befolgen, können Sie die Online-Textdatei für die Konfiguration der VPN- und Parental-Control-Funktionen auf Ihrem Router einfach erstellen und pflegen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
