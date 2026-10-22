# Så konfigurerar du portvidarebefordran på din primära router {#how-to-set-up-port-forwarding-on-your-primary-router}

Om du konfigurerar en server (till exempel en [OpenVPN-server](how_to_set_up_openvpn_server.md) eller [WireGuard-server](build_your_own_wireguard_home_server_with_two_glinet_routers.md)) på din GL.iNet-router och den är ansluten till en primär router måste du konfigurera portvidarebefordran på den primära routern. Detta säkerställer att servern är korrekt åtkomlig.

Observera att om det finns andra routrar mellan den primära routern och GL.iNet-routern måste du konfigurera portvidarebefordran på samtliga föregående routrar.

## Förberedelser {#preparation}

Innan du konfigurerar portvidarebefordran rekommenderar vi att du **reserverar en statisk IP-adress** för GL.iNet-routern på den primära routern. Det säkerställer att GL.iNet-routern alltid tilldelas en fast IP-adress.

Om den primära routern eller GL.iNet-routern annars startas om kan den primära routern tilldela GL.iNet-routern en ny IP-adress, vilket gör att regeln för portvidarebefordran slutar fungera.

Konfigurera därefter portvidarebefordran för GL.iNet-routern på din primära router.

Stegen för att konfigurera portvidarebefordran varierar mellan olika routermärken och modeller. Se relevant avsnitt nedan.

## Använda en GL.iNet-router som primär router {#using-a-glinet-router-as-your-primary-router}

Se [den här länken](../interface_guide/port_forwarding.md){target="_blank"}.

## Använda en router av ett annat märke som primär router {#using-another-router-brand-as-your-primary-router}

!!! note "Ange följande information när du konfigurerar portvidarebefordran"

    När du konfigurerar portvidarebefordran ska du ange följande information. Observera att terminologin kan variera mellan olika routermärken och modeller.

    * **External port/Internal port:** Ange porten som du använder. Standardportarna är till exempel **1194** (för OpenVPN-servrar) och **51820** (för WireGuard-servrar).
    * **Protocol:** Välj **All** eller **UDP/TCP**.
    * **Internal IP** (kan även visas som **Host IP**): Ange den sekundära routerns WAN-IP-adress eller välj den sekundära routern i listrutan, om den finns där.

Här följer stegvisa instruktioner för att konfigurera portvidarebefordran på vanliga märken och modeller av primära routrar.

Om din primära routers märke eller modell inte finns med nedan kan du läsa routerns dokumentation eller kontakta tillverkarens support för mer hjälp.

### AT&T {#att}

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Pace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity) {#comcast-xfinity}

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link {#tp-link}

* [Deco-serien](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Serien med trådlösa routrar](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero {#eero}

Se [den här länken](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys {#linksys}

Se [den här länken](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear {#netgear}

Se [den här länken](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
