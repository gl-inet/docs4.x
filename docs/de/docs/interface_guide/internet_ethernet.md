# Mit einem Ethernet-Kabel eine Verbindung zum Internet herstellen

Verbinden Sie den Router über ein Ethernet-Kabel, das am WAN-Port angeschlossen ist, mit einem Breitbandnetzwerk. In der Regel erhält er automatisch eine IP-Adresse (DHCP). Benutzer können Static oder PPPoE auch manuell konfigurieren. Diese Methode bietet hohe Stabilität und schnelle Geschwindigkeiten und ist daher ideal für Wohn- und Büroumgebungen mit festem Breitbandzugang.

Führen Sie die folgenden Schritte aus, um Ihren Router über ein Ethernet-Kabel mit dem Internet zu verbinden.

1. Verbinden Sie den WAN-Port Ihres Routers über ein Ethernet-Kabel mit dem vorgeschalteten Gerät (z. B. einem ISP-Modem, Router, Netzwerkswitch oder einer Ethernet-Dose). 

2. Melden Sie sich im Web-Admin-Panel des Routers an und navigieren Sie zum Abschnitt **INTERNET** -> **Ethernet**. 

    Wenn die Verbindung erfolgreich ist, zeigt der Abschnitt Ethernet Netzwerkdetails an, darunter Protocol, IP Address, Gateway und DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Tipps**: Bevor Sie das Ethernet-Kabel in den WAN-Port des Routers einstecken, können Sie auf **Change to LAN** klicken, um [den WAN-Port als LAN-Port festzulegen](../faq/change_wan_to_lan.md). Das ist nützlich, wenn Sie den Router als [Repeater](internet_repeater.md) verwenden, da der physische WAN-Port dann ungenutzt bleibt. So können Sie den ungenutzten WAN-Port als LAN-Port umfunktionieren und erhalten einen zusätzlichen LAN-Port.

## Protokoll

Es gibt 3 Protokolltypen: DHCP, Static und PPPoE. Klicken Sie auf **Modify**, um den Typ zu ändern.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP ist das Standardprotokoll und am weitesten verbreitet. Es weist Netzwerkgeräten in IP-Netzwerken über eine Client-Server-Architektur automatisch IP-Adressen und andere Kommunikationsparameter zu.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static wird benötigt, wenn Ihr ISP (Internet Service Provider) eine feste IP-Adresse bereitstellt oder Sie Netzwerkinformationen wie IP-Adresse, Gateway und Netmask manuell konfigurieren möchten.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE ist ein Protokoll, das von den meisten ISPs verwendet wird. Typischerweise stellen sie ein Modem sowie einen Benutzernamen und ein Passwort bereit, die für die Interneteinrichtung erforderlich sind.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Erweitert

Zusätzlich zu den grundlegenden Einstellungen gibt es für die drei oben genannten Protokolle einige optionale erweiterte Einstellungen.

* **VLAN ID**: Dieser Einstellungseintrag ist nur erforderlich, wenn der Server des Anbieters verlangt, dass die Schnittstelle eine bestimmte getaggte VLAN-ID verwendet.

* **TTL**: TTL (Time To Live) definiert die maximale Zeit, die Pakete im Netzwerk überleben können. Standardmäßig verringert der Router den TTL-Wert eingehender Pakete von Client-Geräten vor der Weiterleitung um 1. Wenn Sie ihn überschreiben müssen, können Sie hier einen festen Wert festlegen. Die TTL-Einstellung gilt nur für IPv4.

* **HL**: In IPv6 begrenzt das Feld HL (Hop Limit) die Anzahl der Übertragungssprünge für Datenpakete im Netzwerk und ist das Gegenstück zu TTL in IPv4.

* **MTU**: Der Standardwert für MTU beträgt 1500 Byte.

## Ethernet Port

Klicken Sie oben rechts auf das Zahnradsymbol, um zu [Ethernet Port](ethernet_port.md) zu gelangen.

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

Auf der Seite **WAN** werden die Portrolle (also WAN oder LAN), MAC-Modus und MAC-Adresse sowie die ausgehandelte Geschwindigkeit des Netzwerkports angezeigt. 

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

Auf der Seite **LAN** werden die Portrolle und die ausgehandelte Geschwindigkeit des Netzwerkports angezeigt.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

Weitere Details finden Sie unter diesem [Link](ethernet_port.md). 

## Fehlerbehebung

Wenn ein Ethernet-Kabel am WAN-Port angeschlossen ist, aber kein Internet verfügbar ist, wird eine gelbe Meldung wie unten angezeigt.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

So beheben Sie das Problem:

1. Prüfen Sie, ob das vorgeschaltete Gerät Internetzugang hat.

2. Gehen Sie zur Seite [Multi-WAN](multi-wan.md), um den Status der Ethernet-Schnittstelle zu überprüfen.

---

Verwandte Artikel

- [Internet page](internet.md)
- [How to set the priority of each Internet access method?](multi-wan.md)
- [How to set the load balance when multiple Internet access methods are used at the same time?](multi-wan.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
