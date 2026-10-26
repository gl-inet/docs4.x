# Network Mode {#network-mode}

Öppna **NETWORK** -> **Network Mode**.

Nätverksläge anger routerns roll för olika nätverksbehov, från Wi-Fi-täckning i hemmet till multilänknätverk på företagsnivå. Varje läge aktiverar eller inaktiverar funktioner för optimal prestanda.

!!! note

    1. När nätverksläget ändras kan alla klientenheter behöva återanslutas.

    2. **I Access Point/WDS/Bridge-läge kan webbadministrationspanelen inte öppnas med den ursprungliga LAN-IP-adressen.** Hitta adressen som den uppströms routern har tilldelat och använd den. Om du saknar åtkomst till den uppströms routern håller du återställningsknappen intryckt i 4 sekunder för Router-läge.

    3. **In Non-Router mode, the following features will be unavailable**: Access Control (Allowlist and Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## För modeller med Wi-Fi {#for-models-with-wi-fi}

Except for specific models, most GL.iNet wireless routers have Wi-Fi functionality.

Wi-Fi-modeller stöder vanligtvis Router, Access Point, Extender och WDS. Vissa stöder inte WDS.

![network mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: Standardläge som skapar ett privat LAN och fungerar som gateway mellan internet och anslutna enheter.

    Router Mode aktiverar NAT, DHCP och inbyggd brandvägg, ansluter till en uppströms linje och tilldelar privata IP-adresser.

    ---

- **Access Point**: Ansluter routern till ett kabelnätverk och sänder trådlöst för utökad Wi-Fi-täckning.

    Access Point inaktiverar NAT och DHCP och fungerar som trådlös sändare och switch.

    Efter byte till Access Point använder du IP-adressen som den uppströms routern tilldelat för webbadministrationspanelen. Håll annars återställningsknappen i 4 sekunder för Router-läge.

    Se [Mesh kontra Extender kontra Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode) för en jämförelse.

    !!! tip

        Placering, kanalval, överlappande täckning och sändningseffekt påverkar roaming och prestanda. Se [Förstå Wi-Fi-täckning, åtkomstpunkter och sändningseffekt](../tutorials/understanding_wifi_coverage_access_points_and_transmit_power.md).

    ---

- **Extender**: Utökar ett befintligt Wi-Fi-nätverk och minskar döda zoner.

    Extender ansluter till befintligt Wi-Fi och vidarebefordrar trafik utan Ethernet. Delat radio- och kanalutrymme kan minska kapaciteten.

    Se [Mesh kontra Extender kontra Access Point](mesh.md#mesh-vs-extender-vs-access-point-mode) för en jämförelse.

    I Extender-läge kan webbadministrationspanelen fortfarande öppnas med ursprunglig LAN-IP-adress.

    ---

- **WDS**: Wireless Distribution System utökar Wi-Fi trådlöst och stöder bryggning mellan kompatibla routrar. Rekommenderas när den uppströms routern har WDS.

    Läget passar flervåningsbyggnader och mindre kontorsområden där flera routrar bildar ett enhetligt nätverk. WDS låter sammankopplade routrar både sända och ta emot signaler.

    Efter byte till WDS använder du IP-adressen som den uppströms routern tilldelat. Håll annars återställningsknappen i 4 sekunder för Router-läge.

## For models without Wi-Fi {#for-models-without-wi-fi}

Modeller utan Wi-Fi, till exempel GL-MT5000, GL-MT2500 och GL-MT2500A, stöder Router och Bridge men inte Access Point, Extender eller WDS.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: Standardläge som skapar ett privat LAN och fungerar som gateway mellan internet och anslutna enheter.

    Router Mode aktiverar NAT, DHCP och inbyggd brandvägg, ansluter till en uppströms linje och tilldelar privata IP-adresser.

    ---

- **Bridge**: Ansluter routern till ett kabelnätverk som brygga mellan nätverksenheter.

    Routern fungerar som switch och vidarebefordrar data utan NAT, brandvägg eller DHCP.

    Efter byte till Bridge använder du IP-adressen som den uppströms routern tilldelat. Håll annars återställningsknappen i 4 sekunder för Router-läge.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
