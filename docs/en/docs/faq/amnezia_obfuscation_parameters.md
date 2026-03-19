# Introduction to AmneziaWG Obfuscation Parameters

AmneziaWG is a WireGuard-based VPN protocol with built-in traffic obfuscation. Its obfuscation parameters control how traffic is disguised to avoid detection by strict network controls. Below is a detailed breakdown of AmneziaWG version differences, obfuscation parameters, their constraints, and recommended settings.

## AmneziaWG V2.0

Compared with AmneziaWG v1.0, v2.0 provides stronger obfuscation by adding new parameters (**S3~S4**) and using dynamic headers for packet types (**H1~H4** as ranges instead of fixed values). In addition, AmneziaWG 2.0 supports the **I1~I5** parameters, which send formatted UDP packets before each handshake to disguise AmneziaWG traffic as ordinary non‑VPN traffic, effectively bypassing deep packet inspection and enhancing connectivity in restricted networks. 

These enhancements make VPN traffic more difficult to detect while preserving WireGuard's high speed and low latency.

Here is how to identify the AmneziaWG version:

- **V1.0**: No S3~S4 parameters; H1~H4 are single fixed integers.
- **V2.0**: Includes **S3~S4** parameters; **H1~H4** are defined as numeric ranges; supports **I1~I5** parameters.

**Note**: The parameters I1-I5 are not auto-generated. Users can manually add them as extra lines in the VPN configuration file to make AmneziaWG traffic look like other common protocols, such as QUIC or WebRTC.

## Parameter Overview

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | The number of junk packets before the client initiating the handshake (for interference with traffic feature detection) | 1~128 | 4~12 |
| Jmin         | Minimun size for random junk packets (bytes); Must be configured with Jmax to define junk packats size | 0 ≤ Jmin < Jmax < 65535 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maximun size for random junk packets     | 0 ≤ Jmin < Jmax < 65535        | 0≤ Jmin < Jmax < 1280 |
| S1           | Random prefixes for Init packets         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Random prefixes for Response packets     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Random prefixes for Cookie packets       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Random prefixes for Data packets         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamic headers for packet types; Random values (v1.0) or ranges (v2.0)   | 5~2147483647; H1, H2, H3, and H4 must be different | 5~2147483647 |
| I1~I5        | Signature packets for protocol imitation | arbitrary hex-blob             | N/A |

References: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
