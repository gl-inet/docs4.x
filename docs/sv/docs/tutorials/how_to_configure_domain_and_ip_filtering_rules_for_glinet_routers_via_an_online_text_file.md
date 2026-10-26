# Konfigurera regler för domän- och IP-filtrering på GL.iNet-routrar via en textfil online {#how-to-configure-domain-and-ip-filtering-rules-for-glinet-routers-via-an-online-text-file}

Från och med firmware v4.7 stöder följande funktioner import av regler från webbadressen till en textfil online:

- VPN Policy Based on Target Domains or IP Addresses (under VPN)
- Add a New Ruleset (under Parental Control)

Den här guiden beskriver hur du använder en textfil online för att importera regler för domän- och IP-filtrering till GL.iNet-routrar.

## URL- och filformat som stöds {#supported-url-file-formats}

Följande URL-format stöds:

- Webbadresser till vanliga textfiler (HTTP/HTTPS)
- GitHub Raw-webbadresser

Filtyperna `.txt`, `.conf`, `.log` och andra rena textformat stöds.

**Obs!** Binära filer som `.exe`, `.zip`, `.jpg`, `.png` osv. stöds inte.

## Använd GitHub som värd för textfilen {#use-github-to-host-text-file}

Om textfilen finns i ett offentligt GitHub-arkiv ska du använda webbadressen till råinnehållet i stället för den vanliga GitHub-webbadressen.

Följande GitHub-webbadress pekar till exempel på webbinnehållet, inte råinnehållet:

`https://github.com/SecOps-Institute/FacebookIPLists/blob/master/facebook_ipv4_cidr_blocks.lst`

Använd webbadressen till råinnehållet i följande format för att routern ska hämta rätt innehåll:

`https://raw.githubusercontent.com/SecOps-Institute/FacebookIPLists/master/facebook_ipv4_cidr_blocks.lst`

Routern kan då hämta filens rena textinnehåll.

## Filterformat för VPN Policy (domän/IP) {#filter-formats-for-vpn-policy-domainip}

Funktionen "VPN Policy Based on Target Domain or IP Address" stöder följande filterformat i textfilen online:

* Domännamn: Använd domännamnet, till exempel `netflix.com` (matchar alla underdomäner).
* Underdomän: Ange hela underdomänen, till exempel `www.netflix.com` (matchar endast denna underdomän).
* CIDR-intervall: Ange IP-adressintervall med CIDR-notation, till exempel `192.168.10.0/24`.
* IPv4-adress: Ange enskilda IPv4-adresser, till exempel `192.168.10.10`.

## Filterformat för Parental Control (regeluppsättning) {#filter-formats-for-parental-control-ruleset}

Funktionen "Add a New Ruleset" i Parental Control stöder följande filterformat i textfilen online:

* Domännamn: Använd domännamnet, till exempel `instagram.com` (matchar alla underdomäner).
* Underdomän: Ange hela underdomänen, till exempel `www.instagram.com` (matchar endast denna underdomän).

Använd ett filter per rad när du skapar textfilen online. Routern bearbetar varje rad enligt det angivna formatet och tillämpar motsvarande regler på VPN- eller Parental Control-funktionen.

Med dessa filterformat kan du enkelt skapa och underhålla textfilen online för att konfigurera VPN- och Parental Control-funktionerna på routern.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
