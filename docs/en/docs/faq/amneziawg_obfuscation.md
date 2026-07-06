# AmneziaWG Obfuscation

AmneziaWG is a WireGuard-based VPN protocol featuring built-in traffic obfuscation. Its obfuscation parameters control how traffic is disguised to evade detection under restrictive network inspection.

Below is a detailed breakdown of AmneziaWG, version differences, AmneziaWG on GL.iNet routers, and parameters overview.

## Why AmneziaWG?

The predecessor of AmneziaWG, WireGuard, has established itself as a fast and reliable VPN protocol thanks to its compact codebase and high efficiency. However, its fixed packet headers and predictable packet sizes create an easily recognizable signature. DPI systems can effortlessly identify these packets and immediately terminate connections — a critical issue in countries with strict internet censorship.

AmneziaWG inherits the architectural simplicity and high performance of the original implementation, but eliminates the identifiable network signatures that make WireGuard easily detectable by Deep Packet Inspection (DPI) systems.

In short:

- It masks VPN characteristics to prevent detection by ISPs, firewalls, or Deep Packet Inspection (DPI).

- It makes your VPN connection appear as standard web traffic, improving connection stability and success rate in restricted networks.

## AmneziaWG V2.0

Compared with AmneziaWG v1.0, v2.0 provides stronger obfuscation by adding new parameters (**S3~S4**) and using dynamic headers for packet types (**H1~H4** as ranges instead of fixed values). In addition, AmneziaWG 2.0 supports the **I1~I5** parameters, which send formatted UDP packets before each handshake to disguise AmneziaWG traffic as ordinary non‑VPN traffic, effectively bypassing deep packet inspection and enhancing connectivity in restricted networks. 

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

These enhancements make VPN traffic more difficult to detect while preserving WireGuard's high speed and low latency.

!!! Tip "How to identify the AmneziaWG version?"

    **V1.0**: No S3-S4 parameters; H1-H4 are fixed single integers.
    
    **V2.0**: It is V2.0 if any of the conditions below is met:
            
    - Includes S3-S4 parameters
    - H1-H4 are set as numeric ranges
    - Includes customized I1-I5 parameters.
            
    > Note: I1-I5 are not auto-generated. Users can manually add them as extra lines in the configuration file to make AmneziaWG traffic look like other common protocols, such as QUIC or WebRTC.

## AmneziaWG on GL.iNet routers

Currently, several GL.iNet routers (e.g., Brume 3, Flint 3, Flint 2, and Beryl AX) support the AmneziaWG protocol in select firmware versions. Full official support will be available in firmware ver.4.9 and gradually roll out to more models.

To set up VPN obfuscation on GL.iNet routers, please refer to [here](../tutorials/vpn_obfuscation.md).

## Parameter Overview

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | The number of junk packets before the client initiating the handshake (for interference with traffic feature detection) | 1~128 | 4~12 |
| Jmin         | Minimun size for random junk packets (bytes); Must be configured with Jmax to define junk packats size | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maximun size for random junk packets     | 0 ≤ Jmin < Jmax < 1280         | 0≤ Jmin < Jmax < 1280 |
| S1           | Random prefixes for Init packets         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Random prefixes for Response packets     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Random prefixes for Cookie packets       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Random prefixes for Data packets         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamic headers for packet types; Random values (v1.0) or ranges (v2.0)   | 5~2147483647; H1, H2, H3, and H4 must be different | 5~2147483647 |
| I1~I5        | Signature packets for protocol imitation | arbitrary hex-blob             | N/A |

References: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Related Article:

- [How to set up VPN Obfuscation on GL.iNet routers](../tutorials/vpn_obfuscation.md){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
