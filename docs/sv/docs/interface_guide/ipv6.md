# IPv6 {#ipv6}

IPv6 (Internet Protocol version 6) är det senaste internetprotokollet och är avsett att ersätta IPv4. Det erbjuder fler unika IP-adresser, löser adressbristen i IPv4 och stöder det växande antalet anslutna enheter globalt.

Öppna **NETWORK** -> **IPv6** på vänster sida i webbadministrationspanelen.

På sidan kan du aktivera och konfigurera IPv6 på routern.

![ipv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6.png){class="glboxshadow"}

När IPv6 är aktiverat hämtar WAN-gränssnitt som Ethernet sina IPv6-adresser via DHCPv6. Du kan även ändra IPv6-adressen manuellt på sidan med Ethernet-inställningar.

**Obs!** Vissa funktioner, till exempel brandvägg, GoodCloud och OpenVPN DCO, stöder ännu inte IPv6. Om dessa funktioner och IPv6 används samtidigt kan anslutningsproblem uppstå.

Aktivera **Enable IPv6**, välj läge för huvudnätverket och metod för DNS-hämtning och klicka sedan på **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: Four modes are available: **Native**, **Passthrough**, **NAT6** and **Static IPv6**.

- Native: Använd läget när routern hämtar en offentlig IPv6-adress direkt och automatiskt tilldelar IPv6-adresser till anslutna enheter. Läget uppfyller de flesta användares behov av IPv6-åtkomst.

- Passthrough: Använd läget när IPv6-paket måste skickas igenom direkt utan bearbetning eller konvertering. Vissa nätverksprogram eller tjänster kan till exempel kräva att hela innehållet i IPv6-paketen bevaras för vidare bearbetning eller analys vid nätverksfelsökning eller säkerhetsanalys.

- NAT6: Läget passar när routern används som hanteringsgateway och tilldelar dynamiska interna IPv6-adresser till varje enhet i nätverket. Slutenheterna ansluter via en Optical Network Terminal och får en IPv6-adress för det lokala nätverket.

- Static IPv6: Läget passar enheter eller tjänster som kräver en fast IPv6-adress, till exempel servrar och nätverksskrivare. Enheten använder alltid samma IPv6-adress, vilket förenklar hantering och åtkomst.

**DNS acquisition method**: Anger hur routern hämtar IPv6 DNS-serveradresser. Två alternativ finns: **Automatic** och **Manual**.

- Automatic: The router will obtain IPv6 DNS server addresses dynamically (e.g., via DHCPv6).

- Manual: Ange egna IPv6 DNS-serveradresser. Eftersom DNS används för att slå upp domännamn till motsvarande IP-adresser kan manuell DNS-serverkonfiguration orsaka misslyckade DNS-uppslagningar. Använd alternativet försiktigt.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
