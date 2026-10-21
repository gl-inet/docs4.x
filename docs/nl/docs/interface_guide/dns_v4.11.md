# DNS {#dns}

**Opmerking**: de inhoud van deze pagina is voor het eerst geïntroduceerd in firmware v4.11.

Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 en ouder](dns.md)

</div>

---

Ga links in het webbeheerpaneel naar **DNS**.

De DNS-instellingen van je router bepalen hoe domeinnamen in IP-adressen worden omgezet. Op deze pagina kun je automatisch van upstream apparaten verkregen DNS-server(s) gebruiken of aangepaste servers instellen. Je kunt ook DNS-opties configureren en statische hostregels bewerken.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

DNS-query's voor verkeer dat met het VPN-beleid overeenkomt, gebruiken standaard de DNS-server(s) van de VPN-tunnel. DNS-query's voor niet-VPN-verkeer gebruiken de DNS-server(s) van de actieve WAN-interface. Als je aangepaste DNS-server(s) instelt, kun je deze toepassen op VPN-tunnels, de router zelf of beide. Wanneer deze opties zijn ingeschakeld, worden DNS-query's binnen het geselecteerde bereik via de opgegeven server(s) verwerkt in plaats van via de servers van de relevante netwerkinterfaces. Als er geen aangepaste DNS-server(s) zijn ingesteld, gebruikt de router de DNS-server(s) van de relevante netwerkinterfaces.

## WAN DNS {#wan-dns}

WAN DNS toont de DNS-servers van elke WAN-uplink, waaronder Ethernet, Repeater, Tethering en Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Als een WAN-uplink actief is, worden de bijbehorende DNS-serveradressen rechts weergegeven, zoals hieronder.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## VPN DNS {#vpn-dns}

VPN DNS toont de DNS-servers van elke actieve VPN-tunnel.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Als een VPN-tunnel actief is, volgen DNS-query's van VPN-verkeer de VPN DNS-configuratie, zoals hieronder weergegeven.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## Manual DNS {#manual-dns}

Manual DNS ondersteunt twee configuratietypen: **Static DNS** en **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: wanneer deze optie is ingeschakeld, gebruiken pakketten via de VPN-tunnel de aangepaste Manual DNS in plaats van de DNS-instellingen van de VPN.

- **Apply Manual DNS to Router Itself**: deze optie is standaard ingeschakeld. De ingebouwde diensten van de router, zoals GoodCloud, gebruiken dan de aangepaste Manual DNS-instellingen.

### Static DNS {#static-dns}

Met Static DNS kun je handmatig IPv4- of IPv6-adressen van DNS-servers invoeren. Je kunt adressen rechtstreeks invoeren of vooraf ingestelde openbare DNS-servers uit de vervolgkeuzelijst selecteren.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Je kunt maximaal vier DNS-serveradressen invoeren. Klik op **Apply** om de wijzigingen op te slaan.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Encrypted DNS {#encrypted-dns}

De modus Encrypted DNS ondersteunt meerdere DNS-providers, waaronder Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS en OpenDNS. Je kunt zo nodig ook handmatig een versleutelde DNS-server opgeven.

Selecteer eerst DNS Provider. De overige opties worden aan je selectie aangepast.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Als je een specifieke DNS-provider selecteert, zoals NextDNS, kies je een versleutelingstype uit DNS over TLS (DoT), DNS over HTTPS (DoH) en DNS over QUIC (DoQ). DNS over QUIC (DoQ) is geïntroduceerd in firmware v4.9 en is alleen beschikbaar wanneer Control D, NextDNS of AdGuard DNS als DNS-provider wordt gebruikt.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Als je Manual als DNS-provider selecteert, kies je een versleutelingstype uit DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS en DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Klik vervolgens op **Add a Server** om ten minste één DNS-server toe te voegen. Je kunt rechtstreeks de URL of stamp-indeling van de versleutelde DNS invoeren. Raadpleeg [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"} voor een lijst met openbare servers.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Vergelijking van versleutelingstypen"

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

## DNS-opties {#dns-options}

Klik rechtsboven op **Options** om geavanceerde DNS-instellingen te configureren.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Je kunt deze opties naar behoefte in- of uitschakelen.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: het inschakelen van deze optie kan ervoor zorgen dat privé-DNS-query's mislukken. Schakel de optie uit als je netwerk een captive portal heeft.

- **Override DNS Settings of All Clients**: wanneer deze optie is ingeschakeld, overschrijft de router niet-versleutelde DNS-instellingen voor alle clients.

## Hosts bewerken {#edit-hosts}

Klik rechtsboven op **Edit Hosts** om statische hostregels aan te passen.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

De router geeft deze hostregels voorrang bij het verwerken van verzoeken van verbonden clients.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
