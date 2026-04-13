# Connettersi a Internet tramite un cavo Ethernet

Collega il router a una rete a banda larga tramite un cavo Ethernet inserito nella porta WAN. Di solito acquisisce automaticamente un indirizzo IP, DHCP. Gli utenti possono anche configurare manualmente IP statico o PPPoE. Questo metodo offre elevata stabilita' e velocita' elevata, rendendolo ideale per ambienti domestici e d'ufficio con accesso a banda larga fissa.

Segui i passaggi sotto per collegare il router a Internet tramite un cavo Ethernet.

1. Collega la porta WAN del router al dispositivo a monte, ad esempio modem ISP, router, switch di rete o presa Ethernet, tramite un cavo Ethernet.

2. Accedi al pannello di amministrazione web del router e vai alla sezione **INTERNET** -> **Ethernet**.

    Se la connessione e' riuscita, la sezione Ethernet mostrera' i dettagli di rete, inclusi Protocol, IP Address, Gateway e DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Suggerimenti**: prima di inserire il cavo Ethernet nella porta WAN del router, puoi fare clic su **Change to LAN** per [impostare la porta WAN come porta LAN](../faq/change_wan_to_lan.md). Questo e' utile quando usi il router come [repeater](internet_repeater.md), dato che la porta WAN fisica e' inutilizzata. In questo modo puoi riutilizzare la porta WAN inutilizzata come porta LAN e avere quindi una porta LAN in piu'.

## Protocollo

Esistono 3 tipi di protocollo: DHCP, Static e PPPoE. Fai clic su **Modify** per cambiarlo.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP e' il protocollo predefinito e piu' comune e assegna automaticamente indirizzi IP e altri parametri di comunicazione ai dispositivi di rete tramite un'architettura client-server su reti IP.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static e' necessario se il tuo ISP, Internet Service Provider, fornisce un indirizzo IP fisso oppure se vuoi configurare manualmente le informazioni di rete, come indirizzo IP, Gateway e Netmask.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE e' un protocollo usato dalla maggior parte degli ISP. In genere forniscono un modem e un nome utente con password, necessari per la configurazione di Internet.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Avanzate

Oltre alle impostazioni essenziali, per i tre protocolli sopra sono disponibili anche alcune impostazioni avanzate opzionali.

* **VLAN ID**: questa impostazione e' necessaria solo se il server del provider richiede che l'interfaccia utilizzi uno specifico VLAN ID tagged.

* **TTL**: TTL, Time To Live, definisce il tempo massimo durante il quale i pacchetti possono sopravvivere nella rete. Per impostazione predefinita, il router decrementa di 1 il TTL dei pacchetti in ingresso dai dispositivi client prima di inoltrarli. Se hai bisogno di sovrascriverlo, puoi impostare qui un valore fisso. L'impostazione TTL e' valida solo per IPv4.

* **HL**: in IPv6, il campo HL, Hop Limit, limita il numero di hop di trasmissione dei pacchetti nella rete e corrisponde al TTL in IPv4.

* **MTU**: il valore MTU predefinito e' 1500 byte.

## Porta Ethernet

Fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro per accedere a [Ethernet Port](ethernet_port.md).

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

La pagina **WAN** mostra la funzione della porta, cioe' uso come WAN o LAN, MAC mode e MAC address, oltre alla velocita' negoziata della porta di rete.

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

La pagina **LAN** mostra la funzione della porta e la velocita' negoziata della porta di rete.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan.png){class="glboxshadow"}

Per i dettagli, fai riferimento a questo [link](ethernet_port.md).

## Risoluzione dei problemi

Se un cavo Ethernet e' inserito nella porta WAN ma Internet non e' disponibile, verra' visualizzato un messaggio giallo come mostrato di seguito.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Per risolvere il problema:

1. Controlla se il dispositivo a monte ha accesso a Internet.

2. Vai alla pagina [Multi-WAN](multi-wan.md) per controllare lo stato dell'interfaccia Ethernet.

---

Articoli correlati

- [Pagina Internet](internet.md)
- [Come impostare la priorita' di ciascun metodo di accesso a Internet?](multi-wan.md)
- [Come impostare il bilanciamento del carico quando vengono usati contemporaneamente piu' metodi di accesso a Internet?](multi-wan.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
