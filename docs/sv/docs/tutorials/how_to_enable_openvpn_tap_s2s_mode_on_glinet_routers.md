# Aktivera OpenVPN TAP-S2S-läge på GL.iNet-routrar {#how-to-enable-openvpn-tap-s2s-mode-on-glinet-routers}

## Användningsscenarier {#usage-scenarios}

När TAP-S2S-läget har aktiverats kan OpenVPN-klientenheten fjärransluta till OpenVPN-serverenheten, och OpenVPN-serverenheten kan även fjärransluta till OpenVPN-klientenheten. Nackdelen är att VPN-reglerna som har angetts av OpenVPN-klienten inte gäller när TAP-S2S-läget har aktiverats.

## TAP-S2S jämfört med TUN-läge {#tap-s2s-vs-tun-mode}

Nätverkstopologi

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2S- och TUN-läget använder samma fysiska anslutningsmetod men olika logiska anslutningsmetoder. Skillnaderna är följande:

1. När enheter på GL-X3000-enhetens LAN-sida öppnar administrationsgränssnittet för GL-MT6000 använder TAP-S2S-läget ingen virtuell IP-adress, men TUN-läget gör det.
2. När enheter på GL-X3000-enhetens LAN-sida öppnar administrationsgränssnittet för GL-X3000 använder TAP-S2S-läget en virtuell IP-adress, men TUN-läget gör det inte.
3. När en enhet på GL-X3000-enhetens LAN-sida känner till IP-adressen för en enhet på GL-MT6000-enhetens LAN-sida tillåter TAP-S2S-läget direkt fjärråtkomst. TUN-läget kan inte ge direkt åtkomst utan ytterligare inställningar.
4. I TAP-S2S-läget måste GL-X3000 gå via GL-MT6000 för att komma åt internet, medan GL-X3000 kan komma åt internet direkt i TUN-läget. Därför gäller inte VPN-reglerna som har angetts på GL-X3000 i TAP-S2S-läget. VPN-reglerna på GL-MT6000 måste följas.

## Guide {#tutorials}

Använd först en router med en offentlig IP-adress (i exemplet GL-MT6000), öppna OpenVPN Server, ställ in enhetsläget på **TAP-S2S**, klicka på Apply och klicka sedan på **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Använd dessutom en router med en offentlig IP-adress (i exemplet GL-X3000), öppna OpenVPN-klienten, importera konfigurationsfilen som laddades ned i stegen ovan, klicka på **Apply** och aktivera sedan funktionen.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

IP-adressen för GL-X3000 ändras nu. Logga in på administrationspanelen för GL-MT6000, öppna **Clients** och leta reda på den nya IP-adressen för GL-X3000.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Om GL-MT6000 förlorar nätverksanslutningen eller stänger av OpenVPN-servern, eller om GL-X3000 stänger av OpenVPN-klienten, återställs IP-adressen för GL-X3000.

Observera följande:

- Båda enheterna måste uppgraderas till version v4.5. Annars kan de inte ansluta.
- TAP-S2S fungerar endast med Global Proxy Mode och justeras automatiskt när OpenVPN aktiveras.
- När funktionen har aktiverats kan följande funktioner inte användas: VPN-server, AdGuard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping osv.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
