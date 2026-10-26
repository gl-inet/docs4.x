# Regels voor domein- en IP-filtering via een online tekstbestand configureren {#how-to-configure-domain-and-ip-filtering-rules-for-glinet-routers-via-an-online-text-file}

Vanaf firmware v4.7 kunnen de volgende functies regels uit de URL van een online tekstbestand importeren:

- VPN Policy Based on Target Domains or IP Addresses (under VPN)
- Add a New Ruleset (under Parental Control)

Deze handleiding beschrijft hoe je met een online tekstbestand domein- en IP-filterregels importeert.

## Supported URL & File Formats {#supported-url-file-formats}

De volgende URL-indelingen worden ondersteund:

- Plain text file URLs (HTTP/HTTPS)
- GitHub Raw content URL

Ondersteunde bestandstypen zijn `.txt`, `.conf`, `.log` en andere indelingen met platte tekst.

**Opmerking**: binaire bestanden zoals `.exe`, `.zip`, `.jpg` en `.png` worden niet ondersteund.

## Use GitHub to Host Text File {#use-github-to-host-text-file}

Gebruik bij een openbaar GitHub-repository de URL van de onbewerkte inhoud en niet de gewone GitHub-URL.

De volgende GitHub-URL verwijst bijvoorbeeld naar de webpagina en niet naar de onbewerkte inhoud:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

To ensure the router downloads the correct content, use the raw content URL in the following format:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Zo kan de router de platte tekst van het bestand ophalen.

## Filter Formats for VPN Policy (Domain/IP) {#filter-formats-for-vpn-policy-domainip}

The "VPN Policy Based on Target Domain or IP Address" feature supports the following filter formats in the online text file:

* Domain name: Use the domain name, such as `netflix.com` (matches all subdomains).
* Subdomein: geef het volledige subdomein op, zoals `www.netflix.com` (alleen dit subdomein komt overeen).
* CIDR range: Use CIDR notation to specify IP address ranges, such as `192.168.10.0/24`.
* IPv4 address: Specify individual IPv4 addresses, such as `192.168.10.10`.

## Filter Formats for Parental Control (Ruleset) {#filter-formats-for-parental-control-ruleset}

The "Add a New Ruleset" feature in Parental Control supports the following filter formats in the online text file:

* Domain name: Use the domain name, such as `instagram.com` (matches all subdomains).
* Subdomein: geef het volledige subdomein op, zoals `www.instagram.com` (alleen dit subdomein komt overeen).

Plaats bij het maken van het online tekstbestand één filter per regel. De router verwerkt elke regel volgens de opgegeven indeling en past de regel toe op VPN of Parental Control.

Met deze filterindelingen kun je eenvoudig een online tekstbestand voor VPN en Parental Control maken en onderhouden.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
