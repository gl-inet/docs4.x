# AmneziaWG Obfuscation {#amneziawg-obfuscation}

AmneziaWG is a WireGuard-based VPN protocol featuring built-in traffic obfuscation. Its obfuscation parameters control how traffic is disguised to evade detection under restrictive network inspection.

Below is a detailed introduction to AmneziaWG and different versions.

## Why AmneziaWG? {#why-amneziawg}

The predecessor of AmneziaWG, WireGuard, has established itself as a fast and reliable VPN protocol thanks to its compact codebase and high efficiency. However, its fixed packet headers and predictable packet sizes create an easily recognizable signature. DPI systems can effortlessly identify these packets and immediately terminate connections — a critical issue in countries with strict internet censorship.

AmneziaWG inherits the architectural simplicity and high performance of the original WireGuard implementation, while adding a dedicated obfuscation module to hide VPN traffic patterns. This helps consumer and business users safeguard online privacy and maintain stable connections under restrictive network environments.

In short:

- It masks VPN characteristics to prevent detection by ISPs, firewalls, or Deep Packet Inspection (DPI).

- It makes your VPN connection appear as standard web traffic, improving connection stability and success rate in restricted networks.

## AmneziaWG V2.0 {#amneziawg-v20}

### Overview {#overview}

<font color="red">**Note**: AmneziaWG 2.0 is supported on GL.iNet routers running firmware v4.9 or later.</font>

Compared with AmneziaWG v1.0, v2.0 provides stronger obfuscation by adding new parameters (**S3~S4**) and using dynamic headers for packet types (**H1~H4** as ranges instead of fixed values). In addition, AmneziaWG 2.0 supports the **I1~I5** parameters, which send formatted UDP packets before each handshake to disguise AmneziaWG traffic as ordinary non‑VPN traffic, effectively bypassing deep packet inspection and enhancing connectivity in restricted networks. 

A typical obfuscation section of a v2.0 configuration looks like this:

![parameters](https://static.gl-inet.com/docs/router/en/4/faq/amneziawg_obfuscation_parameters/parameters.png){class="glboxshadow"}

These enhancements make VPN traffic more difficult to detect while preserving WireGuard's high speed and low latency.

!!! Tip "How to distinguish between AmneziaWG 1.0 and 2.0?"

    **V1.0**: No S3-S4 parameters; H1-H4 are fixed single integers.
    
    **V2.0**: It is V2.0 if any of the conditions below is met:
            
    - Includes S3-S4 parameters
    - H1-H4 are set as numeric ranges
    - Includes customized I1-I5 parameters.
            
    > Note: I1-I5 are not auto-generated. Users can manually add them as extra lines in the configuration file to make AmneziaWG traffic look like other common protocols, such as QUIC or WebRTC.

### Parameters {#parameters}

| Parameter    | Description                    | Constraints     | Auto-generated   |
| ------------ | ------------------------------ | --------------- | ---------------- |
| Jc           | The number of junk packets before the client initiating the handshake (for interference with traffic feature detection) | 1~128 | 4~12 |
| Jmin         | Minimum size for random junk packets (bytes); Must be configured with Jmax to define junk packets size | 0 ≤ Jmin < Jmax < 1280 | 0 <= jmin < jmax < 1280 |
| Jmax         | Maximum size for random junk packets     | 0 ≤ Jmin < Jmax < 1280         | 0≤ Jmin < Jmax < 1280 |
| S1           | Random prefixes for Init packets         | 0 ≤ S1 ≤ 1132                  | 15~150 |
| S2           | Random prefixes for Response packets     | 0 ≤ S2 ≤ 1188 <br> S1 + 56 ≠ S2 | 15~150 |
| S3           | Random prefixes for Cookie packets       | 0 ≤ S3 ≤ 1216                  | 15~150 |
| S4           | Random prefixes for Data packets         | 0 ≤ S4 ≤ 32                    | 0~32   |
| H1~H4        | Dynamic headers for packet types; Random values (v1.0) or ranges (v2.0)   | 5~2147483647; H1, H2, H3, and H4 must be different | 5~2147483647 |
| I1~I5        | Signature packets for protocol imitation | arbitrary hex-blob             | N/A |

References: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg){target="_blank"}

## AmneziaWG V3.1 {#amneziawg-v31}

### Overview {#overview_1}

<font color="red">**Note**: AmneziaWG 3.1 is supported on GL.iNet routers running firmware v4.12 or later.</font>

AmneziaWG 3.1 keeps the full v2.0 obfuscation set — random prefixes for every packet type (**S1–S4**), dynamic headers (**H1–H4**), the pre-handshake signature packets (**I1–I5**) and the junk train (**Jc**, **Jmin**, **Jmax**) — and adds mechanisms that give users more control over packet headers, packet lengths and handshake timing, making the traffic harder to fingerprint.

- **Header Protection**: Uses ChaCha20 to hide fields in WireGuard packet headers that would otherwise remain unencrypted.
- **Content Padding**: Adds a randomly selected amount of padding to transport data packets, subject to the available MTU space.
- **Custom Timings**: Allows configurable values or ranges for rekeying, handshake retries, keepalives, and related connection behavior.
- **Random Trailers**: Adds variable-length trailers to handshake and transport data packets to further vary packet sizes.
- **Disable Cookies**: Allows a device to stop sending handshake cookie replies while retaining cookie-reply reception and other handshake processing.

### Parameters {#parameters_1}

The following parameters are introduced in AmneziaWG V3.1. For V2.0 parameters, refer to the AmneziaWG V2.0 parameters above.

| Parameter | Description | Constraints | GL.iNet Range/Value |
| --------- | ----------- | ----------- | ----------- |
| `HeaderProtectionKey` | Enables ChaCha20-based protection of otherwise unencrypted packet-header fields | Exactly 32 bytes. When enabled, S1, S2, S3 and S4 must all be set and each must be ≥ 12. `H1=1`, `H2=2`, `H3=3`, `H4=4` is the recommended combination: the custom header mechanism is switched off and the message type is hidden by Header Protection instead | 32-byte key |
| `ContentPaddingAddition` | Adds a random number of bytes to transport data packets, drawn from the configured range for each packet | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` disables it. | 0–65535 (example: `10-50`)                        |
| `RekeyAfterTime` | How long the current key is used before an active rekey is initiated (seconds) | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` falls back to the WireGuard default | 100–150 (WireGuard default 120) |
| `RekeyTimeout` | How long a single handshake request waits for a response before retrying (seconds) | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` falls back to the WireGuard default | 4–7 (WireGuard default 5) |
| `RejectAfterTime` | How long without receiving data before the connection initiates a new handshake (seconds) | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` falls back to the WireGuard default | 180–240 (WireGuard default 180) |
| `KeepaliveTimeout` | How long without sending data before an internal keepalive is sent (seconds) | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` falls back to the WireGuard default | 8–20 (WireGuard default 10) |
| `MaxHandshakeAttempts` | Maximum number of handshake retries | `range<uint16>`, 0–65535, min ≤ max; `0` or `0-0` falls back to the WireGuard default | 12–18 (WireGuard default 18); minimum must be ≥ 3 |
| `RandomTrailers` | Appends a variable number of bytes to the end of packets: random data for handshake packets, zeros after the inner IP packet for transport packets. Trailer length is dynamically selected so that neither side's MTU is exceeded | `off` disables it. `S1 = S2 = S3 = S4` is recommended when enabled, to reduce the risk of incorrect packet-type detection caused by random packet sizes | `on` / `off` |
| `DisableCookies` | Stops the local device from sending Handshake Cookie Replies. Cookie replies received from the peer and the rest of the handshake handling are unaffected | `off` disables it. S3/H3 must still be kept valid, because the receive path may still use them | `on` / `off` |

**Notes**

* Ranges in the last column can be left to the router to generate. `HeaderProtectionKey` must be identical on the client and the server. `RandomTrailers` and `DisableCookies` are switches set per device.
* Ranges are resolved at runtime: a valid in-range value is kept as is, while a fixed value or a range with either end outside the GL.iNet ranges — including a mixed `0-X` range — is replaced by a randomly generated value inside that range. Malformed input (bad syntax, a value beyond uint16, an inverted range, a missing range end) is rejected instead of being replaced. The client and the server do not need identical timing values.
* `ContentPaddingAddition` and `S4` both change the transport packet length but act on different parts of the packet, and they are not mutually exclusive.
* Header Protection and dynamic `H` are not strictly mutually exclusive; `H1–H4` can stay dynamic, although `1/2/3/4` is the recommended setting.

---

An example v3.1 obfuscation section:

```ini
[Interface]
Address = 10.1.0.2/24
PrivateKey = <client private key>
DNS = 10.1.0.1
MTU = 1420

Jc = 11
Jmin = 472
Jmax = 1277
S1 = 122
S2 = 134
S3 = 13
S4 = 13
H1 = 1
H2 = 2
H3 = 3
H4 = 4

HeaderProtectionKey = <32-byte key>
ContentPaddingAddition = 10-50
RekeyAfterTime = 100-150
RekeyTimeout = 4-7
RejectAfterTime = 180-240
KeepaliveTimeout = 8-20
MaxHandshakeAttempts = 12-18
```

References: [AmneziaWG Official Documentation](https://docs.amnezia.org/documentation/amnezia-wg/){target="_blank"}

---

Related Article:

- [How to set up VPN Obfuscation on GL.iNet routers](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md){target="_blank"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
