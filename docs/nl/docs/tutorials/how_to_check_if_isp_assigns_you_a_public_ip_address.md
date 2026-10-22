# Controleren of je een openbaar IP-adres hebt {#how-to-check-if-you-have-a-public-ip-address}

Een openbaar IP-adres is, in tegenstelling tot een privé-IP-adres, een unieke numerieke identificatie voor apparaten die met internet zijn verbonden. Je hebt dit nodig om een website te hosten, een VPN-server in te stellen of online diensten aan te bieden. Je internetprovider wijst het doorgaans toe.

Gebruik een van de volgende methoden om te controleren of je een openbaar IP-adres hebt.

**Method 1: Contact your internet service provider directly**

**Method 2: Check your IP address in your router admin panel and on the internet**

1. Log in to your router's admin panel.
    * Voer voor GL.iNet-routers `192.168.8.1` in een webbrowser in en meld je aan.
    * Als je meerdere routers hebt, meld je je aan bij het beheerpaneel van de primaire router.
2. Zoek in het beheerpaneel het WAN-IP-adres, bijvoorbeeld 42.XXX.XX.
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. In a web browser, search `what is my ip`.
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Als de twee IP-adressen overeenkomen, heb je een openbaar IP-adres.
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Als je geen openbaar IP-adres hebt, kun je een tool voor intranetpenetratie gebruiken. Hiermee maak je een website, VPN-server of andere dienst via internet bereikbaar zonder openbaar IP-adres.

---

Related Articles

- [Set Up WireGuard Server on GL.iNet Router](../interface_guide/wireguard_server.md)
- [Set Up OpenVPN Server on GL.iNet Router](../interface_guide/openvpn_server.md)
- [Port Forwarding](../interface_guide/port_forwarding.md)

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
