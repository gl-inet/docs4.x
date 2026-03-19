# So richten Sie Portweiterleitung auf Ihrem primären Router ein

Wenn Sie auf Ihrem GL.iNet-Router einen Server einrichten (z. B. einen [OpenVPN-Server](how_to_set_up_openvpn_server.md) oder einen [WireGuard-Server](build_your_own_wireguard_home_server_with_two_glinet_routers.md)) und dieser mit einem primären Router verbunden ist, müssen Sie auf dem primären Router eine Portweiterleitung einrichten. So wird sichergestellt, dass der Server ordnungsgemäß erreichbar ist.

Beachten Sie, dass Sie die Portweiterleitung auf allen vorgeschalteten Routern einrichten müssen, wenn sich zwischen dem primären Router und dem GL.iNet-Router weitere Router befinden.

## Vorbereitung

Bevor Sie die Portweiterleitung konfigurieren, empfehlen wir, **eine statische IP-Adresse** für den GL.iNet-Router auf Ihrem primären Router zu reservieren. Dadurch wird sichergestellt, dass dem GL.iNet-Router immer eine feste IP-Adresse zugewiesen wird.

Andernfalls kann der primäre Router dem GL.iNet-Router nach einem Neustart des primären Routers oder des GL.iNet-Routers eine neue IP-Adresse zuweisen, wodurch die Portweiterleitungsregel nicht mehr funktioniert.

Richten Sie als Nächstes die Portweiterleitung auf Ihrem primären Router für den GL.iNet-Router ein.

Die Schritte zum Konfigurieren der Portweiterleitung unterscheiden sich je nach Routermarke und -modell. Siehe dazu den entsprechenden Abschnitt unten.

## Einen GL.iNet-Router als primären Router verwenden

Bitte lesen Sie [diesen Link](../interface_guide/port_forwarding.md){target="_blank"}.

## Eine andere Routermarke als primären Router verwenden

!!! note "Achten Sie darauf, beim Einrichten der Portweiterleitung die folgenden Informationen einzugeben"

    Stellen Sie beim Konfigurieren der Portweiterleitung sicher, dass die folgenden Informationen angegeben werden. Beachten Sie, dass die Bezeichnungen je nach Routermarke und -modell variieren können.
    
    * **External port/Internal port:** Geben Sie den verwendeten Port ein. Beispielsweise sind die Standardports **1194** (für OpenVPN-Server) und **51820** (für WireGuard-Server).
    * **Protocol:** Wählen Sie **All** oder **UDP/TCP**.
    * **Internal IP** (oder als **Host IP** angezeigt): Geben Sie die WAN-IP-Adresse Ihres sekundären Routers ein oder wählen Sie Ihren sekundären Router aus der Dropdown-Liste aus, falls verfügbar.

Hier finden Sie Schritt-für-Schritt-Anleitungen zum Einrichten der Portweiterleitung bei gängigen primären Routermarken und -modellen.

Wenn Ihre primäre Routermarke oder Ihr primäres Routermodell unten nicht aufgeführt ist, lesen Sie die Dokumentation Ihres Routers oder wenden Sie sich für weitere Unterstützung an das Support-Team.

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity)

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero

Siehe [diesen Link](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys

Siehe [diesen Link](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear

Siehe [diesen Link](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
