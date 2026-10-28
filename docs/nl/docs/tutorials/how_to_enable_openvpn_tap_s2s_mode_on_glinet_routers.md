# How to enable OpenVPN TAP-S2S mode on GL.iNet routers? {#how-to-enable-openvpn-tap-s2s-mode-on-glinet-routers}

## Usage Scenarios {#usage-scenarios}

Na inschakeling op de OpenVPN-client van TAP-S2S kunnen de OpenVPN-client en -server elkaar op afstand bereiken. VPN-regels die op de OpenVPN-client zijn ingesteld, worden in deze modus echter niet toegepast.

## TAP-S2S vs TUN mode {#tap-s2s-vs-tun-mode}

Network Topology

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2S en TUN gebruiken dezelfde fysieke verbinding, maar verschillen logisch als volgt:

1. Wanneer apparaten aan de LAN-zijde van GL-X3000 het beheer van GL-MT6000 openen, gebruikt TAP-S2S geen virtueel IP-adres en TUN wel.
2. Wanneer apparaten aan de LAN-zijde van GL-X3000 het beheer van GL-X3000 openen, gebruikt TAP-S2S wel een virtueel IP-adres en TUN niet.
3. Als een apparaat aan de GL-X3000-LAN-zijde het IP-adres van een apparaat aan de GL-MT6000-LAN-zijde kent, biedt TAP-S2S rechtstreeks externe toegang. Bij TUN zijn aanvullende instellingen nodig.
4. In TAP-S2S gebruikt GL-X3000 GL-MT6000 voor internettoegang. In TUN kan GL-X3000 rechtstreeks internet gebruiken. Daarom gelden in TAP-S2S de VPN-regels van GL-MT6000 en niet die van GL-X3000.

## Tutorials {#tutorials}

Gebruik eerst een router met een openbaar IP-adres, in dit voorbeeld GL-MT6000. Open OpenVPN Server, stel de apparaatmodus in op **TAP-S2S**, klik op Apply en daarna op **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Open vervolgens op een tweede router, in dit voorbeeld GL-X3000, de OpenVPN-client. Importeer het gedownloade configuratiebestand, klik op **Apply** en schakel de functie in.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

Het IP-adres van GL-X3000 verandert. Meld je aan bij het beheer van GL-MT6000 en open **Clients** om het nieuwe adres te vinden.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Als GL-MT6000 de netwerkverbinding verliest of OpenVPN Server uitschakelt, of GL-X3000 de OpenVPN-client uitschakelt, wordt het oorspronkelijke IP-adres van GL-X3000 hersteld.

Points to Note:

- Beide apparaten moeten zijn bijgewerkt naar v4.5, anders kunnen ze geen verbinding maken.
- TAP-S2S only works with Global Proxy Mode, it will adjust automatically with OpenVPN on.
- Na inschakeling op de OpenVPN-client zijn de volgende functies niet beschikbaar: VPN server, AdGuard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway en IGMP Snooping.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
