# DNS {#dns}

**Obs!** Innehållet på sidan bygger på firmware v4.10 och tidigare.

Om enheten kör en annan firmwareversion använder du väljaren nedan för att byta till motsvarande guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10 and earlier" markdown="1">

- [Firmware v4.11](dns_v4.11.md)

</div>

---

Öppna **NETWORK** -> **DNS** på vänster sida i webbadministrationspanelen.

Routerns DNS-inställningar styr hur domännamn översätts till IP-adresser. På sidan kan du använda DNS-servrar som automatiskt hämtas från uppströms enheter eller ange egna och konfigurera DNS-prioriteter.

Om du anger egna DNS-servrar löses DNS-frågor via dessa i stället för servrarna som hämtas via enskilda nätverksgränssnitt. Annars används DNS-inställningarna för respektive gränssnitt.

![dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Alternativet kan göra att privata DNS-uppslagningar misslyckas. Inaktivera det om nätverket har en captive portal.

- **Override DNS Settings for All Clients:** Routern åsidosätter okrypterade DNS-inställningar för alla klienter när alternativet är aktiverat.

- **Allow Custom DNS to Override VPN DNS:** När alternativet är aktiverat och egen DNS har angetts används denna för paket genom VPN-tunneln i stället för VPN-anslutningarnas DNS-inställningar.

## DNS Server Settings {#dns-server-settings}

There are four modes: Automatic, Encrypted DNS, Manual DNS, and DNS Proxy.

### Automatic {#automatic}

I detta läge använder routern automatiskt DNS-servern från den uppströms enheten, till exempel internetleverantörens modem eller den primära routern, eller DNS-inställningarna för respektive nätverksgränssnitt.

![automatic](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Encrypted DNS {#encrypted-dns}

Följ anvisningarna nedan för din firmwareversion.

#### För firmware v4.8 och tidigare {#for-firmware-v48-and-earlier}

Four encryption types are available: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS, and Oblivious DNS over HTTPS.

Välj först **Encryption Type**. Övriga alternativ ändras efter ditt val.

![encrypted dns types](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

- **För DNS over TLS (DoT)** väljer du **Control D**, **NextDNS** eller **Cloudflare** som DNS-leverantör.

    ![dns over tls](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

- **För de övriga tre (DNSCrypt-Proxy, DNS over HTTPS och Oblivious DNS over HTTPS)** väljer du minst en DNS-server från lagringsplatsen.

    ![dnscrypt-proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

#### For Firmware v4.9 to v4.10 {#for-firmware-v49-to-v410}

Utöver Control D, NextDNS och Cloudflare finns fler DNS-leverantörer för Encrypted DNS, däribland **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** och **OpenDNS**. Du kan även ange en krypterad DNS-server manuellt.

Välj först **DNS Provider**. Övriga alternativ ändras efter ditt val.

![encrypted dns providers](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

- Om du väljer en viss DNS-leverantör, till exempel NextDNS, väljer du krypteringstypen **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** eller **DNS over QUIC (DoQ)**. DNS over QUIC introducerades i firmware v4.9 och är endast tillgängligt med Control D, NextDNS eller AdGuard DNS.

    ![nextdns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

- Om du väljer **Manual** som DNS-leverantör väljer du **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** eller **DNSCrypt**.

    ![encrypted manual1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

    Klicka sedan på **Add a Server** och lägg till minst en DNS-server. Du kan ange URL- eller stamp-formatet för krypterad DNS direkt. En lista över offentliga servrar finns på [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![encrypted manual2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Encryption Type Comparison {#encryption-type-comparison}

1. **DNS over TLS (DoT)**

    Krypterar DNS-frågor via en särskild TLS-port. DNS-trafiken isoleras från vanlig webbtrafik och är lätt för nätoperatörer att identifiera.

2. **DNS over HTTPS (DoH)**

    Överför DNS-data inuti vanlig HTTPS-trafik. DNS-förfrågningar blandas med webbtrafik för stark integritet och kringgår enkel trafikfiltrering.

3. **DNS over QUIC (DoQ)**

    Encapsulates DNS over QUIC protocol. It features low latency, fast reconnection and stable performance on unstable networks.

4. **Oblivious DNS over HTTPS (ODoH)**

    En förbättrad version av DoH. Användarens IP skiljs från DNS-frågorna, vilket hindrar server- och nätverksleverantörer från att spåra surfaktiviteten.

5. **DNSCrypt**

    Ett etablerat krypteringsprotokoll för DNS som autentiserar och krypterar DNS-trafik med fokus på manipuleringsskydd och kompatibilitet med äldre nätverksmiljöer.

### Manual DNS {#manual-dns}

I detta läge kan du anpassa routerns DNS-server. Välj minst en DNS Server i listrutan.

![manual dns](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### DNS Proxy {#dns-proxy}

I detta läge dirigerar routern alla DNS-frågor från LAN till den angivna proxyserveradressen, till exempel 8.8.8.8#53. Det kan vara användbart om en annan DNS-server eller Pi-hole körs i nätverket.

![dns proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Edit Hosts {#edit-hosts}

Klicka på **Edit Hosts** uppe till höger för att anpassa statiska värdregler.

![edit hosts1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Routern prioriterar värdreglerna när den löser förfrågningar från anslutna klienter.

![edit hosts2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
