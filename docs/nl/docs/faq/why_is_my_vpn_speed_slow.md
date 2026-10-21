# Why is my VPN speed slower than expected? {#why-is-my-vpn-speed-slower-than-expected}

Het is normaal dat de snelheid van je VPN-verbinding in de praktijk lager is dan de theoretische maximumsnelheid die in een ideaal lokaal netwerk is getest.

VPN's geven prioriteit aan beveiliging en privacy, wat de snelheid beïnvloedt. Onder normale netwerkomstandigheden ligt de VPN-snelheid vaak op 30–50% van het opgegeven maximum. Hieronder staan factoren die de prestaties beïnvloeden en tips om de snelheid te verbeteren.

**Note**: The methods below may help improve VPN speed but cannot guarantee matching advertised speeds, as real-world performance depends on multiple factors.

## Router CPU Speed {#router-cpu-speed}

Een VPN versleutelt je gegevens en vereist daardoor extra verwerking. Het versleutelen en ontsleutelen kan de verbinding vertragen. Kies een router met een snellere CPU voor een hogere VPN-snelheid.

Op onze [productpagina](https://www.gl-inet.com/products/) staan de geteste VPN-snelheden voor alle modellen. Let op:

* De tests zijn uitgevoerd in een lokaal netwerk. De werkelijke snelheid kan per netwerkconfiguratie verschillen.
* OpenVPN en WireGuard zijn langzamer wanneer de router als server wordt gebruikt. De bovenstaande resultaten gelden voor de clientmodus.

## Server Distance {#server-distance}

Als de VPN-server ver van je fysieke locatie staat, leggen gegevens een grotere afstand af. Dit verhoogt de latentie en verlaagt de snelheid.

Het onderstaande voorbeeld toont clientsnelheden bij verbinding met verschillende serverlocaties op hetzelfde tijdstip.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Server Load {#server-load}

Als veel gebruikers met dezelfde VPN-server zijn verbonden, kan overbelasting de snelheid voor iedereen verlagen.

## Server Upload Speed {#server-upload-speed}

Bij een privétunnel vormt de uploadsnelheid van de internetprovider aan de serverzijde de beperking voor de downloadsnelheid van de client, omdat de client gegevens via de server downloadt.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Protocol Differences {#protocol-differences}

VPN-protocollen zoals OpenVPN en WireGuard verschillen in beveiliging en snelheid. Sommige zijn door hun versleutelingsmethode langzamer.

## ISP Throttling {#isp-throttling}

Sommige internetproviders beperken de snelheid van VPN-gebruikers, vooral bij veel dataverkeer. Dit komt vaker voor waar veel gebruikers beperkte internetinfrastructuur delen.

## DNS {#dns}

Some Internet Service Providers (ISPs) may fail to resolve VPN domains. Try using [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) in your router's Network settings.

## MTU {#mtu}

Sommige internetproviders, vooral mobiele providers, beperken de pakketgrootte. Wijzig in VPN Client Options de standaard-MTU van 1420 naar 1380 of 1280.

Raadpleeg voor firmware v4.8 en hoger [deze pagina](../interface_guide/vpn_dashboard_v4.8.md#tunnel-options).

Raadpleeg voor firmware v4.7 en ouder [deze pagina](../interface_guide/vpn_dashboard_v4.7.md#client-options).

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
