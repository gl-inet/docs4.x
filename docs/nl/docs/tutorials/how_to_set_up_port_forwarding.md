# Port forwarding op je primaire router instellen {#how-to-set-up-port-forwarding-on-your-primary-router}

Als je op een GL.iNet-router achter een primaire router een server instelt, zoals een [OpenVPN-server](how_to_set_up_openvpn_server.md) of [WireGuard-server](build_your_own_wireguard_home_server_with_two_glinet_routers.md), moet je port forwarding op de primaire router instellen zodat de server bereikbaar is.

Als er andere routers tussen de primaire router en GL.iNet-router staan, moet je port forwarding op al deze routers instellen.

## Preparation {#preparation}

Reserveer vóór de configuratie een **vast IP-adres** voor de GL.iNet-router op de primaire router. Zo behoudt de GL.iNet-router hetzelfde adres.

Anders kan de primaire router na een herstart een nieuw adres toewijzen, waardoor de regel niet meer werkt.

Stel vervolgens port forwarding op de primaire router in voor de GL.iNet-router.

De stappen verschillen per merk en model. Raadpleeg het juiste gedeelte hieronder.

## Een GL.iNet-router als primaire router gebruiken {#using-a-glinet-router-as-your-primary-router}

Please refer to [this link](../interface_guide/port_forwarding.md){target="_blank"}.

## Een router van een ander merk als primaire router gebruiken {#using-another-router-brand-as-your-primary-router}

!!! note "Make sure to enter the following information when setting up port forwarding"

    Geef bij het configureren de volgende informatie op. De termen kunnen per merk en model verschillen.

    * **External port/Internal port:** voer de gebruikte poort in, bijvoorbeeld standaard **1194** voor OpenVPN-servers en **51820** voor WireGuard-servers.
    * **Protocol:** Choose **All** or **UDP/TCP**.
    * **Internal IP** (of **Host IP**): voer het WAN-IP-adres van de secundaire router in of selecteer deze in de keuzelijst.

Hieronder staan stapsgewijze instructies voor gangbare merken en modellen.

Raadpleeg de documentatie of ondersteuning van je router als het merk of model niet wordt vermeld.

### AT&T {#att}

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Pace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity) {#comcast-xfinity}

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link {#tp-link}

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero {#eero}

Refer to [this link](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys {#linksys}

Refer to [this link](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear {#netgear}

Refer to [this link](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
