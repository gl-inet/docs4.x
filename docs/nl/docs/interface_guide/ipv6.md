# IPv6 {#ipv6}

IPv6 (Internet Protocol version 6) is de nieuwste versie van het Internet Protocol en is ontwikkeld als opvolger van IPv4. Het biedt een grotere verzameling unieke IP-adressen, lost het tekort aan IPv4-adressen op en ondersteunt het wereldwijd groeiende aantal verbonden apparaten.

Ga links in het webbeheerpaneel naar **NETWORK** -> **IPv6**.

Op deze pagina kun je IPv6 op je router inschakelen en configureren.

![ipv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6.png){class="glboxshadow"}

Wanneer IPv6 is ingeschakeld, ontvangen WAN-interfaces zoals Ethernet hun IPv6-adres via DHCPv6. Je kunt het IPv6-adres ook handmatig wijzigen op de instellingenpagina van Ethernet.

**Opmerking**: sommige functies, zoals firewall, GoodCloud en OpenVPN DCO, ondersteunen IPv6 nog niet. Als je deze functies tegelijk met IPv6 gebruikt, kunnen verbindingsproblemen optreden.

Schakel **Enable IPv6** in, selecteer de modus voor je hoofdnetwerk en de methode om DNS te verkrijgen en klik op **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: er zijn vier modi beschikbaar: **Native**, **Passthrough**, **NAT6** en **Static IPv6**.

- Native: gebruik deze modus wanneer de router rechtstreeks een openbaar IPv6-adres ontvangt en automatisch IPv6-adressen aan online apparaten toewijst. Deze modus voldoet aan de IPv6-behoeften van de meeste gebruikers.

- Passthrough: gebruik deze modus wanneer IPv6-pakketten rechtstreeks en zonder verwerking of omzetting moeten worden doorgestuurd. Bepaalde netwerktoepassingen of diensten vereisen bijvoorbeeld dat de volledige inhoud van IPv6-pakketten behouden blijft voor verdere verwerking of analyse door technisch personeel.

- NAT6: deze modus is geschikt wanneer de router als beheergateway dynamische interne IPv6-adressen aan elk apparaat in het netwerk toewijst. Eindapparaten maken via een Optical Network Terminal verbinding en ontvangen een IPv6-adres voor het lokale netwerk.

- Static IPv6: deze modus is geschikt voor apparaten of diensten die een vast IPv6-adres vereisen, zoals servers of netwerkprinters. Het apparaat gebruikt altijd hetzelfde IPv6-adres, wat beheer en toegang vereenvoudigt.

**DNS acquisition method**: bepaalt hoe de router IPv6 DNS-serveradressen verkrijgt. Er zijn twee opties: **Automatic** en **Manual**.

- Automatic: de router verkrijgt dynamisch IPv6 DNS-serveradressen, bijvoorbeeld via DHCPv6.

- Manual: voer aangepaste IPv6 DNS-serveradressen in. Omdat DNS domeinnamen naar de bijbehorende IP-adressen omzet, kan handmatige DNS-serverconfiguratie tot mislukte DNS-query's leiden. Gebruik deze optie voorzichtig.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
