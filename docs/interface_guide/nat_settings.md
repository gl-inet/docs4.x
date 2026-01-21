# NAT Settings

This feature is available starting from v4.5.16.

On the left side of web Admin Panel -> NETWORK -> NAT Settings 

This page lets you enable Full Cone NAT to improve peer-to-peer connection stability for apps like gaming or streaming, and SIP ALG to fix compatibility issues with VoIP/SIP-based phone services.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Full Cone NAT

Full Cone NAT acts as a "direct shortcut" for devices like game consoles or phones when connecting to others online (e.g., in multiplayer games or video calls). 

By allowing external devices to directly reach local devices through the router — instead of hiding them behind multiple layers — it enhances peer-to-peer (P2P) connection stability, reduces latency, and resolves connection failures in P2P applications. 

**Note**: Enabling this feature may lower security compared to other NAT types, as it exposes device ports to the public network.

## SIP ALG

SIP ALG (Application Layer Gateway) functions as a router "translator" for VoIP/SIP-based communication services, such as business desk phones or app-based calls. 

Designed to address NAT traversal challenges, it adjusts call data to ensure seamless transmission through multiple NAT layers — common in networks with multiple routers (e.g., a primary router and a GL.iNet router) — thereby mitigating conflicts and preventing call disruptions. 

**Note**: Incompatible or poorly implemented SIP ALG may degrade call quality, leading to issues including one-way audio, unresponsive ringing, dropped calls, or calls being routed directly to voicemail.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
