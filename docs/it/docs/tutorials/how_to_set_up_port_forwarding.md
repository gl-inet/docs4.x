# Come configurare il port forwarding sul router principale

Se stai configurando un server, ad esempio un [server OpenVPN](how_to_set_up_openvpn_server.md) o un [server WireGuard](build_your_own_wireguard_home_server_with_two_glinet_routers.md), sul router GL.iNet e questo e' collegato a un router principale, dovrai configurare il port forwarding sul router principale. Questo garantisce che il server sia accessibile correttamente.

Tieni presente che, se tra il router principale e il router GL.iNet ci sono altri router, dovrai configurare il port forwarding anche su tutti questi router intermedi.

## Preparazione

Prima di configurare il port forwarding, consigliamo di **riservare un indirizzo IP statico** per il router GL.iNet sul router principale. In questo modo il router GL.iNet ricevera' sempre un indirizzo IP fisso.

In caso contrario, se il router principale o il router GL.iNet si riavvia, il router principale potrebbe assegnare un nuovo indirizzo IP al router GL.iNet, facendo fallire la regola di port forwarding.

Successivamente, configura il port forwarding sul router principale per il router GL.iNet.

I passaggi per configurare il port forwarding variano in base a marca e modello del router. Fai riferimento alla sezione appropriata riportata di seguito.

## Usare un router GL.iNet come router principale

Fai riferimento a [questo link](../interface_guide/port_forwarding.md){target="_blank"}.

## Usare un router di un'altra marca come router principale

!!! note "Assicurati di inserire le seguenti informazioni durante la configurazione del port forwarding"

    Quando configuri il port forwarding, assicurati di fornire le seguenti informazioni. Tieni presente che la terminologia puo' variare tra marche e modelli diversi di router.

    * **External port/Internal port:** inserisci la porta che stai usando. Ad esempio, le porte predefinite sono **1194** per i server OpenVPN e **51820** per i server WireGuard.
    * **Protocol:** scegli **All** oppure **UDP/TCP**.
    * **Internal IP**, oppure mostrato come **Host IP**: inserisci il WAN IP address del router secondario oppure seleziona il router secondario dal menu a discesa, se disponibile.

Di seguito trovi istruzioni passo passo per configurare il port forwarding su marche e modelli comuni di router principali.

Se la marca o il modello del tuo router principale non e' elencato di seguito, fai riferimento alla documentazione del router o contatta il relativo team di supporto per ulteriore assistenza.

### AT&T

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Peace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast, Xfinity

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link

* [Deco series](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Wireless router series](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero

Fai riferimento a [questo link](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys

Fai riferimento a [questo link](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear

Fai riferimento a [questo link](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
