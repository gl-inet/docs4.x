# AmneziaWG-obfuskering {#amneziawg-obfuscation}

AmneziaWG är ett WireGuard-baserat VPN-protokoll med inbyggd trafikobfuskering. Obfuskeringsparametrarna styr hur trafiken döljs för att undvika identifiering vid restriktiv nätverksinspektion.

Nedan följer en detaljerad introduktion till AmneziaWG, versionsskillnader, AmneziaWG på GL.iNet-routrar och en parameteröversikt.

## Varför AmneziaWG? {#why-amneziawg}

Föregångaren WireGuard har etablerat sig som ett snabbt och tillförlitligt VPN-protokoll tack vare sin kompakta kodbas och höga effektivitet. Dess fasta pakethuvuden och förutsägbara paketstorlekar skapar dock ett mönster som är lätt att känna igen. DPI-system kan utan problem identifiera paketen och omedelbart avsluta anslutningarna, vilket är ett allvarligt problem i länder med strikt internetcensur.

AmneziaWG behåller den ursprungliga WireGuard-implementationens enkla arkitektur och höga prestanda men lägger till en särskild obfuskeringsmodul som döljer VPN-trafikens mönster. Det hjälper privat- och företagsanvändare att skydda sin integritet på internet och behålla stabila anslutningar i restriktiva nätverksmiljöer.

Kortfattat:

- Protokollet maskerar VPN-egenskaper så att internetleverantörer, brandväggar och Deep Packet Inspection (DPI) inte kan identifiera dem.

- VPN-anslutningen ser ut som vanlig webbtrafik, vilket förbättrar stabiliteten och anslutningsgraden i begränsade nätverk.

## AmneziaWG V2.0 {#amneziawg-v20}

Jämfört med AmneziaWG v1.0 ger v2.0 starkare obfuskering genom nya parametrar (**S3~S4**) och dynamiska huvuden för olika pakettyper (**H1~H4** som intervall i stället för fasta värden). AmneziaWG 2.0 stöder dessutom parametrarna **I1~I5**, som skickar formaterade UDP-paket före varje handskakning för att få AmneziaWG-trafik att se ut som vanlig trafik utan VPN. Det kringgår effektivt djup paketinspektion och förbättrar anslutningen i begränsade nätverk.

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

Förbättringarna gör VPN-trafiken svårare att identifiera samtidigt som WireGuards höga hastighet och låga latens behålls.

!!! Tip "Hur identifierar jag AmneziaWG-versionen?"

    **V1.0**: Inga S3-S4-parametrar. H1-H4 är fasta heltal.

    **V2.0**: Det är V2.0 om något av följande villkor är uppfyllt:

    - Parametrarna S3-S4 ingår
    - H1-H4 är angivna som numeriska intervall
    - Anpassade I1-I5-parametrar ingår.

    > Obs! I1-I5 genereras inte automatiskt. Du kan lägga till dem manuellt som extra rader i konfigurationsfilen för att få AmneziaWG-trafiken att likna andra vanliga protokoll, till exempel QUIC eller WebRTC.

## Modeller som stöds {#supported-model}

AmneziaWG 2.0 är tillgängligt på GL.iNet-routrar med firmware v4.9 eller senare.

Information om hur du konfigurerar VPN-obfuskering på GL.iNet-routrar finns i [den här guiden](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md).

## Parameteröversikt {#parameter-overview}

| Parameter    | Beskrivning                    | Begränsningar     | Genereras automatiskt   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Antalet skräppaket innan klienten inleder handskakningen (för att störa identifiering av trafikegenskaper) | 1~128 | 4~12 |
| Jmin         | Minsta storlek för slumpmässiga skräppaket (byte). Måste konfigureras tillsammans med Jmax för att definiera skräppaketens storlek | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Största storlek för slumpmässiga skräppaket     | 0 ≤ Jmin < Jmax < 1280         | 0≤ Jmin < Jmax < 1280 |
| S1           | Slumpmässiga prefix för Init-paket         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Slumpmässiga prefix för Response-paket     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Slumpmässiga prefix för Cookie-paket       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Slumpmässiga prefix för Data-paket         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamiska huvuden för pakettyper, med slumpmässiga värden (v1.0) eller intervall (v2.0)   | 5~2147483647; H1, H2, H3, and H4 must be different | 5~2147483647 |
| I1~I5        | Signaturpaket för protokollimitation | arbitrary hex-blob             | N/A |

Referens: [Officiell AmneziaWG-dokumentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Relaterad artikel:

- [Konfigurera VPN-obfuskering på GL.iNet-routrar](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
