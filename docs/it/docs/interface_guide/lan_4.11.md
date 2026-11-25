# LAN {#lan}

**Nota**. Questa guida si riferisce al firmware v4.11 e versioni successive. Se il dispositivo usa una versione diversa, selezionarla qui sotto per consultare la guida corrispondente.

<div class="gl-link-select" data-label="Versione del firmware" data-placeholder="Firmware v4.11 e versioni successive" markdown="1">

- [Firmware v4.9 e versioni precedenti](lan.md)

</div>

---

Nel menu a sinistra del pannello di amministrazione web, andare a **NETWORK** -> **LAN**.

Questa pagina consente di configurare e gestire da un unico punto la rete principale (**Main Network**), la rete ospite (**Guest Network**), la rete IoT (**IoT Network**) e le reti VLAN personalizzate (**VLAN Networks**). È possibile creare e gestire più sottoreti per isolare diversi tipi di dispositivi o di traffico.

## Rete principale {#main-network}

La rete principale è quella a cui si collega il dispositivo tramite il Wi-Fi principale o un cavo Ethernet.

Nella sezione **Main Network** sono visibili lo stato di tutte le interfacce, l'ID VLAN, l'indirizzo IP del router e l'intervallo DHCP.

![Rete principale, panoramica](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-1.png){class="glboxshadow"}

Per configurare la rete principale, fare clic su **Edit** nell'angolo in basso a destra.

![Rete principale, pannello di configurazione](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-2.png){class="glboxshadow"}

La pagina di configurazione include le impostazioni di base, le impostazioni del server DHCP e la prenotazione degli indirizzi.

### Impostazioni di base {#basic-settings}

È possibile scegliere una sottorete all'interno degli intervalli di indirizzi IPv4 privati `192.168.0.0/16`, `172.16.0.0/12` e `10.0.0.0/8`.

![Rete principale, impostazioni di base](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-basic.png){class="glboxshadow" width=700}

- **Router IP Address**

    Inserire questo indirizzo nella barra degli indirizzi del browser per accedere alla pagina di amministrazione del router.

    L'indirizzo predefinito è **192.168.8.1**. È possibile modificarlo se entra in conflitto con la rete locale.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. Se occorrono più indirizzi IP, selezionare **255.255.0.0** per ottenere una sottorete più ampia.

- **VLAN ID**

    L'ID VLAN predefinito della rete principale è **1** e non può essere modificato.

- **AP Isolation**

    È possibile isolare i client in un segmento di rete separato. I client isolati non possono comunicare con gli altri dispositivi sulla stessa rete.

    **Nota.** La funzione **AP Isolation** si applica esclusivamente ai client Wi-Fi.

### Server DHCP {#dhcp-server}

Il server DHCP (**DHCP Server**) è attivo per impostazione predefinita. Assegna automaticamente gli indirizzi IP e gli altri parametri di comunicazione a ciascun client.

Se si disattiva il server DHCP, occorre configurare manualmente le impostazioni di rete dei client. Consultare la guida per [configurare manualmente un indirizzo IP statico](../tutorials/manually_configure_static_ip.md).

È possibile modificare gli indirizzi IP iniziale e finale se cambiano le dimensioni della rete o l'intervallo definito dalla maschera di sottorete, oppure se si verificano conflitti tra indirizzi IP.

![Rete principale, impostazioni di base del server DHCP](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-1.png){class="glboxshadow" width=700}

Per accedere alle impostazioni avanzate, fare clic su **Advanced**.

![Rete principale, impostazioni avanzate del server DHCP, schermata 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Rete principale, impostazioni avanzate del server DHCP, schermata 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/main-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica per quanto tempo è valido l'indirizzo IP assegnato a un dispositivo tramite DHCP.

- **Gateway** indica il dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server 1** indica il server DNS primario, che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2** indica il server DNS secondario, utilizzato per risolvere i nomi di dominio quando il server primario non è disponibile.

- **LPR Server** (Line Printer Remote Server) gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte di stampa LPR.

### Prenotazione degli indirizzi {#address-reservation}

Quando si riserva un indirizzo IP per un client della LAN, il server DHCP del router assegna sempre lo stesso indirizzo a quel client. È possibile riservare indirizzi IP per computer o server che richiedono impostazioni IP permanenti.

**Nota.** Per applicare la prenotazione, i client interessati devono riconnettersi al router.

Fare clic su **Add** per riservare un indirizzo IP.

![Rete principale, elenco delle prenotazioni degli indirizzi](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-1.png){class="glboxshadow" width=700}

Si apre una finestra di dialogo.

![Rete principale, finestra per la prenotazione di un indirizzo](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-2.png){class="glboxshadow" width=600}

Selezionare l'indirizzo **MAC** dall'elenco a discesa. Il campo **IP** viene compilato automaticamente con il corrispondente indirizzo disponibile. Per facilitare l'identificazione, è possibile inserire un nome host (**hostname**) e un nome personalizzato (**name**). Quindi fare clic su **Submit**.

![Rete principale, dati per la prenotazione di un indirizzo](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-3.png){class="glboxshadow" width=600}

Se la configurazione è riuscita, la nuova prenotazione compare nella pagina, come mostrato di seguito.

![Rete principale, elenco aggiornato delle prenotazioni](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/address-reservation-4.png){class="glboxshadow" width=700}

## Rete ospite {#guest-network}

La rete ospite (**Guest Network**) offre ai visitatori una rete Wi-Fi dedicata per accedere a Internet. L'isolamento dalla rete principale migliora la sicurezza.

**Nota.** Alcuni modelli, come GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono di Wi-Fi. Le impostazioni della rete ospite non sono disponibili nel pannello di amministrazione web di questi modelli.

Nella sezione **Guest Network** sono visibili lo stato dell'interfaccia, l'ID VLAN, il gateway e l'intervallo DHCP.

![Rete ospite, panoramica](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-1.png){class="glboxshadow"}

Fare clic su **Edit** nell'angolo in basso a destra per aprire il pannello di configurazione della rete ospite sul lato destro della pagina.

![Rete ospite, pannello di configurazione](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-2.png){class="glboxshadow"}

La pagina di configurazione include le impostazioni di base e quelle del server DHCP.

### Impostazioni di base {#guest-network-basic-settings}

È possibile scegliere una sottorete all'interno degli intervalli di indirizzi IPv4 privati `192.168.0.0/16`, `172.16.0.0/12` e `10.0.0.0/8`.

![Rete ospite, impostazioni di base](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Il **gateway predefinito** della rete ospite è **192.168.9.1**. Se entra in conflitto con la rete locale, impostare un altro indirizzo.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. Se occorrono più indirizzi IP, selezionare **255.255.0.0** per ottenere una sottorete più ampia.

- **VLAN ID**

    L'ID VLAN predefinito della rete ospite è **9**. È possibile modificarlo secondo necessità.

- **Associated LAN Ports**

    Selezionare le porte LAN da assegnare alla sottorete. I dispositivi collegati via cavo a queste porte faranno parte di questa rete.

- **AP Isolation**

    È possibile isolare i client in un segmento di rete separato. I client isolati non possono comunicare con gli altri dispositivi sulla stessa rete.

    **Nota.** La funzione **AP Isolation** si applica esclusivamente ai client Wi-Fi.

- **WAN Access Control**

    La funzione **WAN Access Control** gestisce l'accesso della sottorete locale a Internet e alle altre sottoreti sul lato WAN.

    Sono disponibili tre modalità di controllo dell'accesso tramite WAN.

    - **Unrestricted** consente alla sottorete di accedere a Internet e alle altre sottoreti sul lato WAN senza restrizioni.

    - **Block WAN Subnet** blocca l'accesso alle altre sottoreti sul lato WAN. L'accesso a Internet rimane disponibile.

    - **Block Internet Access** blocca tutto l'accesso in uscita, incluso quello a Internet e alle sottoreti sul lato WAN.

### Server DHCP {#guest-network-dhcp-server}

Il server DHCP (**DHCP Server**) è attivo per impostazione predefinita. Assegna automaticamente gli indirizzi IP e gli altri parametri di comunicazione a ciascun client.

Se si disattiva il server DHCP, occorre configurare manualmente le impostazioni di rete dei client. Consultare la guida per [configurare manualmente un indirizzo IP statico](../tutorials/manually_configure_static_ip.md).

È possibile modificare gli indirizzi IP iniziale e finale se cambiano le dimensioni della rete o l'intervallo definito dalla maschera di sottorete, oppure se si verificano conflitti tra indirizzi IP.

![Rete ospite, impostazioni di base del server DHCP](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-1.png){class="glboxshadow" width=700}

Per accedere alle impostazioni avanzate, fare clic su **Advanced**.

![Rete ospite, impostazioni avanzate del server DHCP, schermata 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Rete ospite, impostazioni avanzate del server DHCP, schermata 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/guest-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica per quanto tempo è valido l'indirizzo IP assegnato a un dispositivo tramite DHCP.

- **Gateway** indica il dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server 1** indica il server DNS primario, che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2** indica il server DNS secondario, utilizzato per risolvere i nomi di dominio quando il server primario non è disponibile.

- **LPR Server** (Line Printer Remote Server) gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte di stampa LPR.

## Rete IoT {#iot-network}

La rete IoT offre ai dispositivi IoT una rete Wi-Fi dedicata e isolata dalla rete principale, migliorando la compatibilità e la sicurezza.

**Nota.** Alcuni modelli, come GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono di Wi-Fi. Le impostazioni della rete IoT non sono disponibili nel pannello di amministrazione web di questi modelli.

Nella sezione **IoT Network** sono visibili lo stato dell'interfaccia, l'ID VLAN, il gateway e l'intervallo DHCP.

![Rete IoT, panoramica](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-1.png){class="glboxshadow"}

Fare clic su **Edit** nell'angolo in basso a destra per aprire il pannello di configurazione della rete IoT sul lato destro della pagina. Il pannello consente di modificare le impostazioni di base e quelle del server DHCP.

![Rete IoT, pannello di configurazione](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-2.png){class="glboxshadow"}

### Impostazioni di base {#iot-network-basic-settings}

È possibile scegliere una sottorete all'interno degli intervalli di indirizzi IPv4 privati `192.168.0.0/16`, `172.16.0.0/12` e `10.0.0.0/8`.

![Rete IoT, impostazioni di base](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-basic.png){class="glboxshadow" width=700}

- **Gateway**

    Il **gateway predefinito** della rete IoT è **192.168.10.1**. Se entra in conflitto con la rete locale, impostare un altro indirizzo.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. Se occorrono più indirizzi IP, selezionare **255.255.0.0** per ottenere una sottorete più ampia.

- **VLAN ID**

    L'ID VLAN predefinito della rete IoT è **10**. È possibile modificarlo secondo necessità.

- **Associated LAN Ports**

    Selezionare le porte LAN da assegnare alla sottorete. I dispositivi collegati via cavo a queste porte faranno parte di questa rete.

- **AP Isolation**

    È possibile isolare i client in un segmento di rete separato. I client isolati non possono comunicare con gli altri dispositivi sulla stessa rete.

    **Nota.** La funzione **AP Isolation** si applica esclusivamente ai client Wi-Fi.

- **WAN Access Control**

    La funzione **WAN Access Control** gestisce l'accesso della sottorete locale a Internet e alle altre sottoreti sul lato WAN.

    Sono disponibili tre modalità di controllo dell'accesso tramite WAN.

    - **Unrestricted** consente alla sottorete di accedere a Internet e alle altre sottoreti sul lato WAN senza restrizioni.

    - **Block WAN Subnet** blocca l'accesso alle altre sottoreti sul lato WAN. L'accesso a Internet rimane disponibile.

    - **Block Internet Access** blocca tutto l'accesso in uscita, incluso quello a Internet e alle sottoreti sul lato WAN.

### Server DHCP {#iot-network-dhcp-server}

Il server DHCP (**DHCP Server**) è attivo per impostazione predefinita. Assegna automaticamente gli indirizzi IP e gli altri parametri di comunicazione a ciascun client.

Se si disattiva il server DHCP, occorre configurare manualmente le impostazioni di rete dei client. Consultare la guida per [configurare manualmente un indirizzo IP statico](../tutorials/manually_configure_static_ip.md).

È possibile modificare gli indirizzi IP iniziale e finale se cambiano le dimensioni della rete o l'intervallo definito dalla maschera di sottorete, oppure se si verificano conflitti tra indirizzi IP.

![Rete IoT, impostazioni di base del server DHCP](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-1.png){class="glboxshadow" width=700}

Per accedere alle impostazioni avanzate, fare clic su **Advanced**.

![Rete IoT, impostazioni avanzate del server DHCP, schermata 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-2.png){class="glboxshadow" width=700}

![Rete IoT, impostazioni avanzate del server DHCP, schermata 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/iot-network-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica per quanto tempo è valido l'indirizzo IP assegnato a un dispositivo tramite DHCP.

- **Gateway** indica il dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server 1** indica il server DNS primario, che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2** indica il server DNS secondario, utilizzato per risolvere i nomi di dominio quando il server primario non è disponibile.

- **LPR Server** (Line Printer Remote Server) gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte di stampa LPR.

## Reti VLAN {#vlan-networks}

Nella parte superiore della pagina è possibile creare altre **reti VLAN** per isolare diversi tipi di dispositivi o il traffico dei visitatori.

![Reti VLAN, panoramica](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-1.png){class="glboxshadow"}

Fare clic su **+ Add** sul lato destro della pagina per configurare una nuova rete.

![Reti VLAN, pannello di configurazione](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-2.png){class="glboxshadow"}

### Impostazioni di base {#vlan-networks-basic-settings}

In questa pagina è possibile configurare i parametri di base delle reti VLAN.

![Reti VLAN, impostazioni di base](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-basic-settings.png){class="glboxshadow" width=700}

- **Name**

    Assegnare un nome alla nuova sottorete per identificarla.

- **Gateway**

    Configurare manualmente il gateway della nuova sottorete. Se entra in conflitto con il segmento LAN esistente, impostare un altro indirizzo.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. Se occorrono più indirizzi IP, selezionare **255.255.0.0** per ottenere una sottorete più ampia.

- **VLAN ID**

    Per creare una sottorete, assegnare un ID VLAN compreso tra **9** e **4000**. Per evitare conflitti di rete, scegliere un ID VLAN ancora libero.

- **Associated LAN Ports**

    Selezionare le porte LAN da assegnare alla sottorete. I dispositivi collegati via cavo a queste porte faranno parte di questa rete.

- **AP Isolation**

    È possibile isolare i client in un segmento di rete separato. I client isolati non possono comunicare con gli altri dispositivi sulla stessa rete.

    **Nota.** La funzione **AP Isolation** si applica esclusivamente ai client Wi-Fi.

- **WAN Access Control**

    La funzione **WAN Access Control** gestisce l'accesso della sottorete locale a Internet e alle altre sottoreti sul lato WAN.

    Sono disponibili tre modalità di controllo dell'accesso tramite WAN.

    - **Unrestricted** consente alla sottorete di accedere a Internet e alle altre sottoreti sul lato WAN senza restrizioni.

    - **Block WAN Subnet** blocca l'accesso alle altre sottoreti sul lato WAN. L'accesso a Internet rimane disponibile.

    - **Block Internet Access** blocca tutto l'accesso in uscita, incluso quello a Internet e alle sottoreti sul lato WAN.

### Server DHCP {#vlan-networks-dhcp-server}

Il server DHCP (**DHCP Server**) è attivo per impostazione predefinita. Assegna automaticamente gli indirizzi IP e gli altri parametri di comunicazione a ciascun client.

Se si disattiva il server DHCP, occorre configurare manualmente le impostazioni di rete dei client. Consultare la guida per [configurare manualmente un indirizzo IP statico](../tutorials/manually_configure_static_ip.md).

È possibile modificare gli indirizzi IP iniziale e finale se cambiano le dimensioni della rete o l'intervallo definito dalla maschera di sottorete, oppure se si verificano conflitti tra indirizzi IP.

![Reti VLAN, impostazioni di base del server DHCP](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=700}

Per accedere alle impostazioni avanzate, fare clic su **Advanced**.

![Reti VLAN, impostazioni avanzate del server DHCP, schermata 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=700}

![Reti VLAN, impostazioni avanzate del server DHCP, schermata 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan_4.11/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=700}

- **Lease Time** indica per quanto tempo è valido l'indirizzo IP assegnato a un dispositivo tramite DHCP.

- **Gateway** indica il dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server 1** indica il server DNS primario, che traduce i nomi di dominio in indirizzi IP.

- **DNS Server 2** indica il server DNS secondario, utilizzato per risolvere i nomi di dominio quando il server primario non è disponibile.

- **LPR Server** (Line Printer Remote Server) gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte di stampa LPR.

Una volta configurata, la nuova rete VLAN compare nella pagina con le informazioni sulla sottorete.

---

Per altre domande, consultare il [forum della community](https://forum.gl-inet.com){target="_blank"} o [contattare GL.iNet](https://www.gl-inet.com/contacts/){target="_blank"}.
