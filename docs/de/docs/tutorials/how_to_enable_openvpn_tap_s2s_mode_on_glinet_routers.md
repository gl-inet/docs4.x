# So aktivieren Sie den OpenVPN-TAP-S2S-Modus auf GL.iNet-Routern

## Einsatzszenarien

Nach dem Aktivieren des TAP-S2S-Modus kann das OpenVPN-Client-Gerät per Fernzugriff auf das OpenVPN-Server-Gerät zugreifen, und das OpenVPN-Server-Gerät kann ebenfalls per Fernzugriff auf das OpenVPN-Client-Gerät zugreifen. Der Nachteil dabei ist jedoch, dass die vom OpenVPN-Client selbst festgelegten VPN-Regeln nach dem Aktivieren des TAP-S2S-Modus nicht mehr wirksam sind.

## TAP-S2S- vs. TUN-Modus

Netzwerktopologie

![tap_s2s_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![tun_topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

TAP-S2S- und TUN-Modus verwenden dieselbe physische Verbindungsmethode, unterscheiden sich jedoch in ihrer logischen Verbindung. Die Unterschiede sind wie folgt:

1. Wenn Geräte auf der LAN-Seite des GL-X3000 auf das Verwaltungs-Backend des GL-MT6000 zugreifen, verwendet der TAP-S2S-Modus keine virtuelle Client-IP, der TUN-Modus jedoch schon.
2. Wenn Geräte auf der LAN-Seite des GL-X3000 auf das Verwaltungs-Backend des GL-X3000 zugreifen, verwendet der TAP-S2S-Modus eine virtuelle Client-IP, der TUN-Modus jedoch nicht.
3. Wenn ein Gerät auf der LAN-Seite des GL-X3000 die IP-Adresse eines Geräts auf der LAN-Seite des GL-MT6000 kennt, ist im TAP-S2S-Modus ein direkter Fernzugriff möglich. Im TUN-Modus ist dies ohne zusätzliche Einstellungen nicht direkt möglich.
4. Im TAP-S2S-Modus muss der GL-X3000 über den GL-MT6000 auf das Internet zugreifen, während der GL-X3000 im TUN-Modus direkt auf das Internet zugreifen kann. Daher sind im TAP-S2S-Modus die auf dem GL-X3000 festgelegten VPN-Regeln nicht wirksam und es müssen die VPN-Regeln des GL-MT6000 befolgt werden.

## Anleitung

Verwenden Sie zunächst einen Router mit öffentlicher IP-Adresse (angenommen GL-MT6000), um den **OpenVPN Server** zu öffnen, setzen Sie den Gerätemodus auf **TAP-S2S**, klicken Sie auf **Apply** und anschließend auf **Export Client Configuration**.

![tutorials_select_mode](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![tutorials_export](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

Verwenden Sie außerdem einen Router mit öffentlicher IP-Adresse (angenommen GL-X3000), öffnen Sie den OpenVPN-Client, importieren Sie die in den obigen Schritten heruntergeladene Konfigurationsdatei, klicken Sie auf **Apply** und aktivieren Sie anschließend die Funktion.

![tutorials_select_file](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![tutorials_start](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

Anschließend ändert sich die IP-Adresse des Routers GL-X3000. Sie können sich im Verwaltungs-Dashboard des GL-MT6000 anmelden, **Clients** öffnen und dort die neue IP-Adresse des GL-X3000 finden.

![tutorials_new_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Wenn der GL-MT6000 die Netzwerkverbindung verliert oder den OpenVPN-Server ausschaltet oder wenn der GL-X3000 den OpenVPN-Client ausschaltet, wird die IP-Adresse des GL-X3000 wiederhergestellt.

Wichtige Hinweise:

- Beide Geräte müssen auf Version v4.5 aktualisiert werden, andernfalls können sie keine Verbindung herstellen.
- TAP-S2S funktioniert nur mit dem Global Proxy Mode; bei aktiviertem OpenVPN wird dies automatisch angepasst.
- Nach dem Aktivieren dieser Funktion können die folgenden Funktionen nicht verwendet werden: VPN-Server, AdGuard Home, Kindersicherung, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping usw.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
