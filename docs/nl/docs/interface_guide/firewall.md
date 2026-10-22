# Firewall {#firewall}

Deze handleiding geldt voor firmware v4.5 en ouder.

Sinds v4.6 is de pagina Firewall opgesplitst: Port Forwarding en DMZ zijn verplaatst naar [Port Forwarding](port_forwarding.md) en Open Ports is verplaatst naar [Security](security.md).

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **Firewall**.

Op de pagina Firewall kun je firewallregels instellen, zoals **Port Forwarding**, **Open Ports on Router** en **DMZ**.

## Port Forwards {#port-forwards}

Met Port Forwarding kunnen externe computers verbinding maken met een lokale computer of server achter de firewall van de router in het LAN, zoals web- en FTP-servers.

Klik op het tabblad **Port Forwards** en vervolgens op **Add** om port forwarding in te stellen.

![firewall page](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

Voeg in het pop-upvenster een regel voor port forwarding toe en klik op **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** voer een naam voor de regel in.

**Protocol:** selecteer TCP, UDP of beide.

**External Zone:** selecteer de interface waar het inkomende verkeer aankomt. De opties zijn `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` en `wgserver`. VPN-opties verschijnen pas nadat een VPN-verbinding is geconfigureerd.

**External Port:** voer het externe poortnummer in.

**Internal Zone:** selecteer de interface waarnaar het verkeer wordt doorgestuurd. De opties zijn `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` en `wgserver`. VPN-opties verschijnen pas nadat een VPN-verbinding is geconfigureerd.

**Internal IP:** voer het LAN-IP-adres in van het apparaat dat je op afstand wilt openen.

**Internal Port:** voer het interne poortnummer van het apparaat in. Laat dit leeg als het gelijk is aan de externe poort.

**Enable:** schakel de regel in of uit.

## Open Ports on Router {#open-ports-on-router}

Voor openbare bereikbaarheid moeten de bijbehorende poorten voor routerdiensten, zoals web en FTP, op de router worden geopend.

Open het tabblad **Open Ports on Router** en klik op **Add** om een poort te openen.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

Open in het pop-upvenster een nieuwe poort en klik op **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** de naam van de regel, die je zelf kunt opgeven.

**Protocol:** het gebruikte protocol. Je kunt TCP, UDP of beide kiezen.

**Port:** het poortnummer dat je wilt openen.

**Enable:** schakel de regel in of uit.

## DMZ {#dmz}

Met DMZ kun je één computer vanaf internet bereikbaar maken. Alle inkomende pakketten worden naar deze computer doorgestuurd.

Schakel **Enable DMZ** in. Selecteer het interne IP-adres van het hostapparaat dat alle inkomende pakketten ontvangt.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
