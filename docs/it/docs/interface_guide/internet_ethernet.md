# Connettersi a Internet tramite un cavo Ethernet {#connect-to-the-internet-via-an-ethernet-cable}

Collega il router a una rete a banda larga tramite un cavo Ethernet inserito nella porta WAN. Di solito acquisisce automaticamente un indirizzo IP, DHCP. Gli utenti possono anche configurare manualmente IP statico o PPPoE. Questo metodo offre elevata stabilità e velocità elevata, rendendolo ideale per ambienti domestici e d'ufficio con accesso a banda larga fissa.

Segui i passaggi sotto per collegare il router a Internet tramite un cavo Ethernet.

1. Collega la porta WAN del router al dispositivo a monte, ad esempio modem ISP, router, switch di rete o presa Ethernet, tramite un cavo Ethernet.

2. Accedi al pannello di amministrazione web del router e vai alla sezione **INTERNET** -> **Ethernet**.

    Se la connessione è riuscita, la sezione Ethernet mostrerà i dettagli di rete, inclusi Protocol, IP Address, Gateway e DNS Server.

    ![ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Suggerimento**: se necessario, puoi cambiare il ruolo della porta WAN per usarla come porta LAN. È utile quando usi il router come [ripetitore](internet_repeater.md), dato che la porta WAN fisica è inutilizzata. Convertendo la porta WAN in LAN, avrai una porta LAN in più.

## Protocollo {#protocol}

Esistono 3 tipi di protocollo: DHCP, Static e PPPoE. Fai clic su **Modify** per cambiarlo.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP è il protocollo predefinito e più comune e assegna automaticamente indirizzi IP e altri parametri di comunicazione ai dispositivi di rete tramite un'architettura client-server su reti IP.

    ![ethernet dhcp](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static è necessario se il tuo ISP, Internet Service Provider, fornisce un indirizzo IP fisso oppure se vuoi configurare manualmente le informazioni di rete, come indirizzo IP, Gateway e Netmask.

    ![ethernet static](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE è un protocollo usato dalla maggior parte degli ISP. In genere forniscono un modem e un nome utente con password, necessari per la configurazione di Internet.

    ![ethernet pppoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Avanzate {#advanced}

Oltre alle impostazioni essenziali, per i tre protocolli sopra sono disponibili anche alcune impostazioni avanzate opzionali.

* **VLAN ID**: questa impostazione è necessaria solo se il server del provider richiede che l'interfaccia utilizzi uno specifico VLAN ID tagged.

* **TTL**: TTL (Time To Live) definisce il tempo massimo per cui i pacchetti possono rimanere nella rete. Per impostazione predefinita, il router riduce di 1 il TTL dei pacchetti in ingresso dai dispositivi client prima di inoltrarli. L'impostazione TTL è valida solo per IPv4.

    **Nota**: se devi sovrascrivere o falsificare il TTL, imposta qui un valore fisso. Per la maggior parte dei modelli, inserisci il TTL effettivo desiderato più 1 per compensare la riduzione automatica. Mudi 7 (GL-E5800) applica il valore inserito senza modificarlo.

* **HL**: in IPv6, il campo HL, Hop Limit, limita il numero di hop di trasmissione dei pacchetti nella rete e corrisponde al TTL in IPv4.

* **MTU**: il valore MTU predefinito è 1500 byte.

## Porta Ethernet {#ethernet-port}

Fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro per accedere alla pagina [Ethernet Port](ethernet_port.md) e gestire le porte Ethernet del router.

![ethernet port 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

La pagina **WAN** mostra la funzione della porta, cioè uso come WAN o LAN, MAC mode e MAC address, oltre alla velocità negoziata della porta di rete.

![ethernet port 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

La pagina **LAN** mostra la funzione della porta e la velocità negoziata della porta di rete.

![ethernet port 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/lan.png){class="glboxshadow"}

Per i dettagli, consulta [Ethernet Port](ethernet_port.md).

## Risoluzione dei problemi {#troubleshooting}

Se un cavo Ethernet è inserito nella porta WAN ma Internet non è disponibile, verrà visualizzato un messaggio giallo come mostrato di seguito.

**"The interface is connected, but the Internet can't be accessed."**

![ethernet caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Per risolvere il problema:

1. Controlla se il dispositivo a monte ha accesso a Internet.

2. Vai alla pagina [Multi-WAN](multi-wan.md) per controllare lo stato dell'interfaccia Ethernet.

---

Articoli correlati

- [Pagina Internet](internet.md)
- [Come impostare la priorità di ciascun metodo di accesso a Internet?](multi-wan.md)
- [Come impostare il bilanciamento del carico quando vengono usati contemporaneamente più metodi di accesso a Internet?](multi-wan.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
