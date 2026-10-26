# DNS {#dns}

**Obs!** Innehållet på sidan introducerades i firmware v4.11.

Om enheten kör en annan firmwareversion använder du väljaren nedan för att byta till motsvarande guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.11" markdown="1">

- [Firmware v4.10 and earlier](dns.md)

</div>

---

Öppna **DNS** på vänster sida i webbadministrationspanelen.

Routerns DNS-inställningar styr hur domännamn översätts till IP-adresser. Du kan använda DNS-servrar som automatiskt hämtas från uppströms enheter eller ange egna. Du kan även konfigurera DNS-alternativ och redigera statiska värdregler.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

Som standard använder DNS-frågor för trafik som matchar VPN-principen DNS-servrarna från VPN-tunneln. DNS-frågor utanför VPN använder servrarna från det aktiva WAN-gränssnittet. Egna DNS-servrar kan tillämpas på VPN-tunnlar, själva routern eller båda. När alternativen är aktiverade löses DNS-frågor inom valt område via angivna servrar i stället för dem från relevanta nätverksgränssnitt. Om inga egna servrar anges använder routern servrarna från relevanta gränssnitt.

## WAN DNS {#wan-dns}

WAN DNS visar DNS-servrar som hämtas från varje WAN-upplänk, däribland Ethernet, Repeater, Tethering och Cellular.

![wan dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Om en WAN-upplänk är aktiv visas dess DNS-serveradresser till höger enligt bilden nedan.

![wan dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## VPN DNS {#vpn-dns}

VPN DNS visar DNS-servrar som hämtas från varje aktiv VPN-tunnel.

![vpn dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

När en VPN-tunnel körs följer DNS-frågor från VPN-trafik VPN DNS-konfigurationen enligt bilden nedan.

![vpn dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## Manual DNS {#manual-dns}

Manual DNS supports two configuration types: **Static DNS** and **Encrypted DNS**.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: När alternativet är aktiverat används egen Manual DNS för paket genom VPN-tunneln i stället för VPN-anslutningens DNS-inställningar.

- **Apply Manual DNS to Router Itself**: Alternativet är aktiverat som standard. Routerns inbyggda tjänster, till exempel GoodCloud, använder då egna manuella DNS-inställningar.

### Static DNS {#static-dns}

Med Static DNS kan du ange IPv4- eller IPv6-adresser för DNS-servrar manuellt. Ange adresser direkt eller välj förinställda offentliga DNS-servrar i listrutan.

![static dns 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Du kan ange upp till fyra DNS-serveradresser. Klicka på **Apply** för att spara.

![static dns 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Encrypted DNS {#encrypted-dns}

Encrypted DNS stöder flera DNS-leverantörer, däribland Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS och OpenDNS. Du kan även ange en krypterad DNS-server manuellt.

Välj först DNS Provider. Övriga alternativ ändras efter ditt val.

![dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Om du väljer en viss DNS-leverantör, till exempel NextDNS, väljer du DNS over TLS (DoT), DNS over HTTPS (DoH) eller DNS over QUIC (DoQ). DNS over QUIC introducerades i firmware v4.9 och är endast tillgängligt med Control D, NextDNS eller AdGuard DNS.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Om du väljer Manual som DNS-leverantör väljer du DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS eller DNSCrypt.

    ![encrypted manual 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Klicka sedan på **Add a Server** och lägg till minst en DNS-server. Du kan ange URL- eller stamp-formatet för krypterad DNS direkt. En lista över offentliga servrar finns på [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Encryption Type Comparison"

    1. **DNS over TLS (DoT)**

        Krypterar DNS-frågor via en särskild TLS-port. DNS-trafiken isoleras från vanlig webbtrafik och är lätt för nätoperatörer att identifiera.

    2. **DNS over HTTPS (DoH)**

        Överför DNS-data inuti vanlig HTTPS-trafik. DNS-förfrågningar blandas med webbtrafik för stark integritet och kringgår enkel trafikfiltrering.

    3. **DNS over QUIC (DoQ)**

        Kapslar in DNS över QUIC-protokollet. Det ger låg latens, snabb återanslutning och stabil prestanda på instabila nätverk.

    4. **Oblivious DNS over HTTPS (ODoH)**

        En förbättrad version av DoH som skiljer användarens IP från DNS-frågor och hindrar server- och nätverksleverantörer från att spåra surfaktiviteten.

    5. **DNSCrypt**

        Ett etablerat krypteringsprotokoll för DNS som autentiserar och krypterar DNS-trafik med fokus på manipuleringsskydd och kompatibilitet med äldre nätverksmiljöer.

## DNS Options {#dns-options}

Klicka på **Options** uppe till höger för att konfigurera avancerade DNS-inställningar.

![dns options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Aktivera eller inaktivera alternativen efter behov.

![dns options 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: Alternativet kan göra att privata DNS-uppslagningar misslyckas. Inaktivera det om nätverket har en captive portal.

- **Override DNS Settings of All Clients**: När alternativet är aktiverat åsidosätter routern okrypterade DNS-inställningar för alla klienter.

## Edit Hosts {#edit-hosts}

Klicka på **Edit Hosts** uppe till höger för att anpassa statiska värdregler.

![edit hosts 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Routern prioriterar värdreglerna när den löser förfrågningar från anslutna klienter.

![edit hosts 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
