# Varför är min VPN-hastighet lägre än väntat? {#why-is-my-vpn-speed-slower-than-expected}

Om VPN-anslutningens hastighet är lägre än den teoretiska maxhastigheten (som testats i ett optimalt lokalt nätverk) är det normalt vid verklig användning.

VPN är utformat för att prioritera säkerhet och integritet, vilket i sig påverkar hastigheten. Under vanliga nätverksförhållanden är det normalt att VPN-hastigheten ligger på 30-50% av den angivna maxhastigheten. Skillnaden beror på flera faktorer som påverkar prestandan. De förklaras nedan tillsammans med några tips som kan förbättra upplevelsen.

**Obs!** Metoderna nedan kan förbättra VPN-hastigheten men kan inte garantera att den angivna hastigheten uppnås, eftersom prestandan i verkligheten beror på flera faktorer.

## Routerns processorhastighet {#router-cpu-speed}

VPN krypterar dina data för att skydda din integritet, vilket kräver ytterligare databearbetning. Krypteringen och dekrypteringen kan göra anslutningen långsammare. Välj en router med en snabbare processor för att höja VPN-hastigheten.

Vi har angett de testade VPN-hastigheterna för alla modeller på vår [produktsida](https://www.gl-inet.com/products/). Observera dock följande:

* Testerna utförs i ett lokalt nätverk. Verkliga hastigheter kan variera beroende på nätverkskonfigurationen.
* OpenVPN- och WireGuard-hastigheterna blir lägre när routern används som server. Resultaten ovan gäller klientläget.

## Avstånd till servern {#server-distance}

Om VPN-servern är långt från din fysiska plats måste data färdas en längre sträcka, vilket leder till högre latens och lägre hastighet.

Exemplet nedan visar klienthastigheter vid anslutning till olika serverplatser vid samma tid på dagen.

![hk](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/hkserver.jpg){class="glboxshadow"}

![canada](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/canadaserver.jpg){class="glboxshadow"}

## Serverbelastning {#server-load}

Om många användare är anslutna till samma VPN-server kan den bli överbelastad, vilket ger alla användare lägre hastighet.

## Serverns uppladdningshastighet {#server-upload-speed}

Om du använder en privat VPN-tunnel blir internetleverantörens uppladdningshastighet på serversidan flaskhalsen för nedladdningshastigheten på klientsidan, eftersom VPN-klienten hämtar data via servern.

![tunnel](https://static.gl-inet.com/docs/router/en/4/faq/vpn_speed/tunnel.png){class="glboxshadow"}

## Protokollskillnader {#protocol-differences}

Olika VPN-protokoll, till exempel OpenVPN och WireGuard, skiljer sig åt vad gäller säkerhet och hastighet. Vissa kan vara långsammare på grund av sina krypteringsmetoder.

## Hastighetsbegränsning från internetleverantören {#isp-throttling}

Vissa internetleverantörer kan begränsa hastigheten för användare som använder VPN, särskilt om de misstänker hög dataförbrukning. Det är särskilt vanligt i vissa utvecklingsländer och mindre orter där många användare delar på en begränsad internetinfrastruktur.

## DNS {#dns}

Vissa internetleverantörer kanske inte kan slå upp VPN-domäner. Prova att använda [Encrypted DNS](../interface_guide/dns.md#dns-server-settings) i routerns nätverksinställningar.

## MTU {#mtu}

Vissa internetleverantörer, särskilt mobiloperatörer, kan begränsa datapaketens storlek. Prova att ändra standardvärdet för MTU från 1420 till 1380 eller 1280 i VPN Client Options.

För firmware v4.8 och senare finns mer information [här](../interface_guide/vpn_dashboard_v4.8.md#tunnel-options).

För firmware v4.7 och tidigare finns mer information [här](../interface_guide/vpn_dashboard_v4.7.md#client-options).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
