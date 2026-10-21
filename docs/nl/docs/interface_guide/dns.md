# DNS {#dns}

**Opmerking**: de inhoud van deze pagina is gebaseerd op firmwareversie v4.10 en ouder.

Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.10 en ouder" markdown="1">

- [Firmware v4.11](dns_v4.11.md)

</div>

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **DNS**.

De DNS-instellingen van je router bepalen hoe domeinnamen in IP-adressen worden omgezet. Op deze pagina kun je automatisch van upstream apparaten verkregen DNS-server(s) gebruiken, aangepaste DNS-servers instellen en DNS-prioriteiten configureren.

Als je aangepaste DNS-server(s) instelt, worden alle DNS-query's via de opgegeven server(s) verwerkt in plaats van via de DNS-servers van de afzonderlijke netwerkinterfaces. Anders worden de DNS-instellingen van elke interface gebruikt.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** het inschakelen van deze optie kan ervoor zorgen dat privé-DNS-query's mislukken. Schakel de optie uit als je netwerk een captive portal heeft.

- **Override DNS Settings for All Clients:** wanneer dit is ingeschakeld, overschrijft je router niet-versleutelde DNS-instellingen voor alle clients.

- **Allow Custom DNS to Override VPN DNS:** wanneer dit is ingeschakeld en je aangepaste DNS hebt ingesteld, worden pakketten die via de VPN-tunnel worden verzonden met de aangepaste DNS verwerkt in plaats van met de DNS-serverinstellingen van de VPN-verbindingen.

## DNS-serverinstellingen {#dns-server-settings}

Er zijn vier modi: Automatic, Encrypted DNS, Manual DNS en DNS Proxy.

### Automatic {#automatic}

In deze modus gebruikt de router automatisch de DNS-server van het upstream apparaat, zoals een internetmodem of primaire router, of de DNS-instellingen van elke netwerkinterface.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS {#encrypted-dns}

Volg de onderstaande instructies voor je firmwareversie.

#### Voor firmware v4.8 en ouder {#for-firmware-v48-and-earlier}

Er zijn vier versleutelingstypen beschikbaar: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS en Oblivious DNS over HTTPS.

Selecteer eerst **Encryption Type**. De overige opties worden aan je selectie aangepast.

![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

- Kies voor **DNS over TLS (DoT)** een DNS-provider uit **Control D**, **NextDNS** en **Cloudflare**.

    ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

- Selecteer voor de overige drie typen, DNSCrypt-Proxy, DNS over HTTPS en Oblivious DNS over HTTPS, ten minste één DNS-server uit de opslagplaats.

    ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

#### Voor firmware v4.9 tot v4.10 {#for-firmware-v49-to-v410}

Naast Control D, NextDNS en Cloudflare zijn in de modus Encrypted DNS meer DNS-providers beschikbaar, waaronder **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** en **OpenDNS**. Je kunt zo nodig ook handmatig een versleutelde DNS-server opgeven.

Selecteer eerst **DNS Provider**. De overige opties worden aan je selectie aangepast.

![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

- Als je een specifieke DNS-provider selecteert, zoals NextDNS, kies je een versleutelingstype uit **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** en **DNS over QUIC (DoQ)**. DNS over QUIC (DoQ) is geïntroduceerd in firmware v4.9 en is alleen beschikbaar wanneer Control D, NextDNS of AdGuard DNS als DNS-provider wordt gebruikt.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

- Als je **Manual** als DNS-provider selecteert, kies je een versleutelingstype uit **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** en **DNSCrypt**.

    ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

    Klik vervolgens op **Add a Server** om ten minste één DNS-server toe te voegen. Je kunt rechtstreeks de URL of stamp-indeling van de versleutelde DNS invoeren. Raadpleeg [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"} voor een lijst met openbare servers.

    ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Vergelijking van versleutelingstypen {#encryption-type-comparison}

1. **DNS over TLS (DoT)**

    Versleutelt DNS-query's via een speciale TLS-poort. DNS-verkeer wordt van normaal webverkeer gescheiden en kan eenvoudig door netwerkoperators worden herkend.

2. **DNS over HTTPS (DoH)**

    Verzendt DNS-gegevens binnen standaard HTTPS-verkeer. DNS-verzoeken worden voor betere privacy met normaal webverkeer gemengd en eenvoudige verkeersfiltering wordt omzeild.

3. **DNS over QUIC (DoQ)**

    Kapselt DNS in het QUIC-protocol in. Dit biedt lage latentie, snel opnieuw verbinden en stabiele prestaties op instabiele netwerken.

4. **Oblivious DNS over HTTPS (ODoH)**

    Een verbeterde versie van DoH. Het IP-adres van de gebruiker wordt van DNS-query's gescheiden, zodat zowel server- als netwerkproviders je browseactiviteiten niet kunnen volgen.

5. **DNSCrypt**

    Een volwassen versleutelingsprotocol voor DNS. Het verifieert en versleutelt DNS-verkeer en richt zich op bescherming tegen manipulatie en compatibiliteit met oudere netwerkomgevingen.

### Manual DNS {#manual-dns}

In deze modus kun je de DNS-server van je router aanpassen. Selecteer ten minste één DNS Server voor je router in de vervolgkeuzelijst.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy {#dns-proxy}

In deze modus routeert de router alle DNS-query's van het LAN naar het opgegeven proxyserveradres, bijvoorbeeld 8.8.8.8#53. Dit kan nuttig zijn als je een andere DNS-server of Pi-hole in je netwerk gebruikt.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Hosts bewerken {#edit-hosts}

Klik rechtsboven op **Edit Hosts** om statische hostregels aan te passen.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

De router geeft deze hostregels voorrang bij het verwerken van verzoeken van verbonden clients.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
