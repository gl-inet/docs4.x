# Firewall {#firewall}

Guiden gäller firmware v4.5 och tidigare.

Från v4.6 är sidan Firewall uppdelad: Port Forwarding och DMZ har flyttats till [Port Forwarding](port_forwarding.md), medan Open Ports har flyttats till [Security](security.md).

---

Öppna **NETWORK** -> **Firewall** på vänster sida i webbadministrationspanelen.

På sidan Firewall kan du ange brandväggsregler som **Port Forwarding**, **Open Ports on Router** och **DMZ**.

## Port Forwards {#port-forwards}

Port Forwarding lets remote computers connect to a local computer or server behind the router's firewall in the LAN (such as web servers, FTP servers).

Konfigurera portvidarebefordran genom att klicka på fliken **Port Forwards** och sedan på **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

Lägg till en regel för portvidarebefordran i popup-fönstret och klicka på **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Enter a name for the rule.

**Protocol:** Select the protocol — TCP, UDP, or both.

**External Zone:** Välj gränssnittet som inkommande trafik anländer från. Alternativen är `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` och `wgserver`. VPN-alternativ visas först när en VPN-anslutning har konfigurerats.

**External Port:** Enter the external port number.

**Internal Zone:** Välj gränssnittet som trafiken vidarebefordras till. Alternativen är `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` och `wgserver`. VPN-alternativ visas först när en VPN-anslutning har konfigurerats.

**Internal IP:** Ange LAN-IP-adressen för enheten som du vill fjärransluta till.

**Internal Port:** Ange enhetens interna portnummer. Lämna fältet tomt om det är samma som den externa porten.

**Enable:** Toggle to enable or disable the rule.

## Open Ports on Router {#open-ports-on-router}

Routerns tjänster, till exempel webb och FTP, kräver att respektive port öppnas på routern för att vara offentligt åtkomliga.

Öppna en port genom att välja fliken **Open Ports on Router** och sedan klicka på **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

Öppna en ny port i popup-fönstret och klicka på **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** Regelns namn, som du kan ange.

**Protocol:** Välj TCP, UDP eller både TCP och UDP.

**Port:** Portnumret som du vill öppna.

**Enable:** Enable or disable the rule.

## DMZ {#dmz}

Med DMZ kan du exponera en dator mot internet så att alla inkommande paket omdirigeras till den.

Aktivera **Enable DMZ**. Välj den interna IP-adressen för värdenheten som ska ta emot alla inkommande paket.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
