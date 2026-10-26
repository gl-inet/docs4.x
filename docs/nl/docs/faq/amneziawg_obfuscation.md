# AmneziaWG Obfuscation {#amneziawg-obfuscation}

AmneziaWG is a WireGuard-based VPN protocol featuring built-in traffic obfuscation. Its obfuscation parameters control how traffic is disguised to evade detection under restrictive network inspection.

Below is a detailed introduction of AmneziaWG, version differences, AmneziaWG on GL.iNet routers, and parameters overview.

## Why AmneziaWG? {#why-amneziawg}

De voorloper van AmneziaWG, WireGuard, is dankzij de compacte code en hoge efficiëntie een snel en betrouwbaar VPN-protocol. De vaste pakketheaders en voorspelbare pakketgrootten vormen echter een gemakkelijk herkenbaar patroon. DPI-systemen kunnen deze pakketten eenvoudig herkennen en verbindingen direct beëindigen, wat een ernstig probleem is in landen met strenge internetcensuur.

AmneziaWG behoudt de eenvoudige architectuur en hoge prestaties van WireGuard en voegt een speciale obfuscatiemodule toe om patronen in VPN-verkeer te verbergen. Hierdoor kunnen particuliere en zakelijke gebruikers hun onlineprivacy beschermen en stabiele verbindingen behouden in beperkende netwerkomgevingen.

In short:

- It masks VPN characteristics to prevent detection by ISPs, firewalls, or Deep Packet Inspection (DPI).

- De VPN-verbinding lijkt op normaal webverkeer, waardoor de stabiliteit en slagingskans in beperkte netwerken verbeteren.

## AmneziaWG V2.0 {#amneziawg-v20}

Vergeleken met AmneziaWG v1.0 biedt v2.0 sterkere obfuscatie met nieuwe parameters (**S3~S4**) en dynamische headers voor pakkettypen (**H1~H4** als bereiken in plaats van vaste waarden). AmneziaWG 2.0 ondersteunt daarnaast **I1~I5**. Deze parameters verzenden vóór elke handshake geformatteerde UDP-pakketten om AmneziaWG-verkeer op normaal niet-VPN-verkeer te laten lijken. Dit omzeilt deep packet inspection en verbetert verbindingen in beperkte netwerken.

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

These enhancements make VPN traffic more difficult to detect while preserving WireGuard's high speed and low latency.

!!! Tip "How to identify the AmneziaWG version?"

    **V1.0**: No S3-S4 parameters; H1-H4 are fixed single integers.

    **V2.0**: het is V2.0 als aan een van de onderstaande voorwaarden wordt voldaan:

    - Includes S3-S4 parameters
    - H1-H4 are set as numeric ranges
    - Includes customized I1-I5 parameters.

    > Opmerking: I1-I5 worden niet automatisch gegenereerd. Je kunt ze handmatig als extra regels aan het configuratiebestand toevoegen om AmneziaWG-verkeer op andere veelgebruikte protocollen zoals QUIC of WebRTC te laten lijken.

## Supported Model {#supported-model}

AmneziaWG 2.0 is available on GL.iNet routers with firmware v4.9 or later.

To set up VPN obfuscation on GL.iNet routers, refer to [this tutorial](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md).

## Parameter Overview {#parameter-overview}

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | Het aantal junkpakketten voordat de client de handshake start (om detectie van verkeerskenmerken te verstoren) | 1~128 | 4~12 |
| Jmin         | Minimale grootte van willekeurige junkpakketten in bytes; moet samen met Jmax worden ingesteld om de pakketgrootte te bepalen | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maximum size for random junk packets     | 0 ≤ Jmin < Jmax < 1280         | 0≤ Jmin < Jmax < 1280 |
| S1           | Random prefixes for Init packets         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Random prefixes for Response packets     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Random prefixes for Cookie packets       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Random prefixes for Data packets         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamische headers voor pakkettypen; willekeurige waarden (v1.0) of bereiken (v2.0) | 5~2147483647; H1, H2, H3 en H4 moeten verschillend zijn | 5~2147483647 |
| I1~I5        | Signature packets for protocol imitation | arbitrary hex-blob             | N/A |

References: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Gerelateerd artikel:

- [How to set up VPN Obfuscation on GL.iNet routers](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
