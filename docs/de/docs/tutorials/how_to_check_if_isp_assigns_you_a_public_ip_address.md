# So prüfen Sie, ob Sie eine öffentliche IP-Adresse haben

Eine öffentliche Adresse ist im Gegensatz zu einer privaten IP-Adresse eine eindeutige numerische Kennung, die Ihren mit dem Internet verbundenen Geräten zugewiesen wird. Sie benötigen eine öffentliche IP-Adresse, wenn Sie eine Website hosten, einen VPN-Server einrichten oder andere Onlinedienste bereitstellen möchten. In der Regel wird sie Ihnen von Ihrem Internetanbieter zur Verfügung gestellt.

Wenn Sie nicht sicher sind, ob Sie eine öffentliche IP-Adresse haben, können Sie dies mit einer der folgenden Methoden prüfen.

**Methode 1: Wenden Sie sich direkt an Ihren Internetanbieter**

**Methode 2: Prüfen Sie Ihre IP-Adresse im Admin-Panel Ihres Routers und im Internet**

1. Melden Sie sich im Admin-Panel Ihres Routers an.
    * Geben Sie bei GL.iNet-Routern `192.168.8.1` in einen Webbrowser ein und melden Sie sich an.
    * Wenn Sie in Ihrer Einrichtung mehr als einen Router verwenden, melden Sie sich im Admin-Panel des primären Routers an.
2. Suchen Sie im Admin-Panel des Routers nach Ihrer WAN-IP-Adresse (z. B. 42.XXX.XX.)
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. Suchen Sie in einem Webbrowser nach „what is my ip“.
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Wenn die beiden IP-Adressen übereinstimmen, haben Sie eine öffentliche IP-Adresse.
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Wenn Sie keine öffentliche IP-Adresse haben, können Sie die Verwendung eines Intrant-Penetration-Tools in Betracht ziehen. Damit sind Ihre Website, Ihr VPN-Server oder Ihre Dienste auch dann über das Internet erreichbar, wenn Sie keine öffentliche IP-Adresse haben.

---

Verwandte Artikel

- [WireGuard-Server auf einem GL.iNet-Router einrichten](../interface_guide/wireguard_server.md)
- [OpenVPN-Server auf einem GL.iNet-Router einrichten](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

Noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
