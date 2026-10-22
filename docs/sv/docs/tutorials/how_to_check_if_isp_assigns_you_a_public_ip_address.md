# Kontrollera om du har en offentlig IP-adress {#how-to-check-if-you-have-a-public-ip-address}

En offentlig IP-adress är, till skillnad från en privat IP-adress, en unik numerisk identifierare som tilldelas dina enheter som är anslutna till internet. Du behöver en offentlig IP-adress om du vill vara värd för en webbplats, konfigurera en VPN-server eller tillhandahålla andra onlinetjänster. Den tillhandahålls vanligtvis av din internetleverantör.

Om du är osäker på om du har en offentlig IP-adress kan du kontrollera det med någon av följande metoder.

**Metod 1: Kontakta internetleverantören direkt**

**Metod 2: Kontrollera IP-adressen i routerns administrationspanel och på internet**

1. Logga in på routerns administrationspanel.
    * För GL.iNet-routrar anger du `192.168.8.1` i en webbläsare och loggar in.
    * Om konfigurationen innehåller flera routrar loggar du in på den primära routerns administrationspanel.
2. Leta reda på WAN-IP-adressen i routerns administrationspanel (t.ex. 42.XXX.XX.)
![locate ip address](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. Sök efter `what is my ip` i en webbläsare.
![what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Om de två IP-adresserna stämmer överens har du en offentlig IP-adress.
![two ip addresses match](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Om du saknar en offentlig IP-adress kan du överväga ett verktyg för intranätgenomträngning. Med ett sådant verktyg kan webbplatsen, VPN-servern eller tjänsterna göras tillgängliga på internet även utan en offentlig IP-adress.

---

Relaterade artiklar

- [Konfigurera en WireGuard-server på en GL.iNet-router](../interface_guide/wireguard_server.md)
- [Konfigurera en OpenVPN-server på en GL.iNet-router](../interface_guide/openvpn_server.md)
- [Portvidarebefordran](../interface_guide/port_forwarding.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
