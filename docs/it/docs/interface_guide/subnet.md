# Sottorete

**Nota**: Questa pagina è attualmente disponibile su Flint 4 (GL-BE14000) e verrà distribuita ad altri modelli con il firmware v4.10.

---

Sul lato sinistro del pannello di amministrazione web, andare a **NETWORK** -> **Subnet**.

La pagina riunisce la configurazione di **LAN**, **Guest Network**, **IoT Network** e delle **VLAN Networks** personalizzate in un'unica vista. Offre un'interfaccia di gestione centralizzata per tutte le impostazioni relative alle sottoreti, consentendo di creare e gestire più sottoreti per isolare diversi tipi di dispositivi o traffico.

## Rete principale

**Main Network** è la rete a cui il dispositivo è connesso tramite il Wi-Fi principale o tramite un cavo Ethernet.

In Main Network è possibile visualizzare direttamente tutti gli stati delle interfacce, il VLAN ID, l'indirizzo IP del router e l'intervallo DHCP.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Fare clic su **Edit** nell'angolo in basso a destra per configurare Main Network.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

La pagina di configurazione include le impostazioni di base, le impostazioni del server DHCP e la prenotazione degli indirizzi.

### Impostazioni di base

È possibile impostare la sottorete entro gli intervalli di indirizzi IPv4 privati: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Questo è l'indirizzo da inserire nella barra degli indirizzi del browser per accedere alla pagina di amministrazione del router.

    Per impostazione predefinita è **192.168.8.1**. È possibile modificarlo se entra in conflitto con la rete.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. È anche possibile selezionare **255.255.0.0** se serve una sottorete più grande con più indirizzi IP.

- **VLAN ID**

    Il VLAN ID predefinito di Main Network è **1** e non può essere modificato.

- **AP Isolation**

    È possibile isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

### Server DHCP

Il **DHCP Server** è abilitato per impostazione predefinita. Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client.

Se il server DHCP è disabilitato, sarà necessario configurare manualmente le impostazioni di rete dei dispositivi client. Fare clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

È possibile modificare gli indirizzi IP iniziale e finale in base alle proprie esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP o se viene modificato l'intervallo della maschera di sottorete.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Fare clic su **Advanced** per ulteriori configurazioni, se necessario.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: periodo di validità di un indirizzo IP assegnato da DHCP per un dispositivo.

- **Gateway**: dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server**: sono disponibili due campi DNS per configurare il resolver primario e quello secondario.

    **Nota**: il DNS primario viene inserito nel campo superiore e il secondario nel campo inferiore. Se il server primario non è disponibile, i dispositivi client passano automaticamente al resolver secondario, garantendo la continuità della risoluzione dei nomi di dominio.

- **LPR Server** (Line Printer Remote Server): servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte stampante LPR.

### Prenotazione degli indirizzi

Quando si specifica un indirizzo IP riservato per un client nella LAN, il client riceve sempre lo stesso indirizzo IP ogni volta che accede al server DHCP del router. È possibile assegnare indirizzi IP riservati a computer o server che richiedono impostazioni IP permanenti.

**Nota:** I client configurati devono riconnettersi al router per attivare l'impostazione.

Fare clic su **Add** per riservare un IP.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Verrà visualizzata una finestra pop-up.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Selezionare **MAC** dall'elenco a discesa. La **IP** disponibile corrispondente verrà compilata automaticamente. È anche possibile inserire un **hostname** e un **name** personalizzato per facilitarne l'identificazione. Quindi fare clic su **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Dopo aver aggiunto una nuova prenotazione di indirizzo IP, verrà visualizzata la pagina seguente, che indica che la configurazione è riuscita.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Rete ospite

**Guest Network** fornisce una rete Wi-Fi dedicata ai visitatori. Isolata dalla rete principale, migliora la sicurezza offrendo al tempo stesso un accesso Internet comodo.

**Nota**: alcuni modelli, ad esempio GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono della funzione Wi-Fi; pertanto le impostazioni di Guest Network non sono disponibili nel loro pannello di amministrazione web.

In Guest Network è possibile visualizzare direttamente lo stato dell'interfaccia, il VLAN ID, il gateway e l'intervallo DHCP.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Fare clic su **Edit** nell'angolo in basso a destra; il pannello di configurazione di Guest Network si aprirà sul lato destro della pagina.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

La pagina di configurazione include impostazioni di base e impostazioni del server DHCP.

### Impostazioni di base

È possibile impostare la sottorete entro gli intervalli di indirizzi IPv4 privati: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/gest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    Il **gateway predefinito** di Guest Network è **192.168.9.1**. Se entra in conflitto con la rete locale, cambiarlo con uno diverso.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. È anche possibile selezionare **255.255.0.0** se serve una sottorete più grande con più indirizzi IP.

- **VLAN ID**

    Il VLAN ID predefinito di Guest Network è **9** e può essere modificato secondo necessità.

- **AP Isolation**

    Questa funzione è disponibile dal firmware v4.5.

    È possibile isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

- **WAN Access Control**

    WAN Access Control gestisce l'accesso della sottorete locale alle reti lato WAN, inclusi Internet e altre sottoreti WAN.

    Sono disponibili tre modalità di controllo dell'accesso WAN:

    - **Unrestricted**: consente a questa sottorete di accedere a Internet e ad altre sottoreti lato WAN senza restrizioni.

    - **Block WAN Subnet**: blocca l'accesso ad altre sottoreti lato WAN. L'accesso a Internet resta disponibile.

    - **Block Internet Access**: blocca tutto l'accesso in uscita, inclusi Internet e le sottoreti lato WAN.

### Server DHCP

Il **DHCP Server** è abilitato per impostazione predefinita. Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client.

Se il server DHCP è disabilitato, sarà necessario configurare manualmente le impostazioni di rete dei dispositivi client. Fare clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

È possibile modificare gli indirizzi IP iniziale e finale in base alle proprie esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP o se viene modificato l'intervallo della maschera di sottorete.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Fare clic su **Advanced** per ulteriori configurazioni, se necessario.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: periodo di validità di un indirizzo IP assegnato da DHCP per un dispositivo.

- **Gateway**: dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server**: sono disponibili due campi DNS per configurare il resolver primario e quello secondario.

    **Nota**: il DNS primario viene inserito nel campo superiore e il secondario nel campo inferiore. Se il server primario non è disponibile, i dispositivi client passano automaticamente al resolver secondario, garantendo la continuità della risoluzione dei nomi di dominio.

- **LPR Server** (Line Printer Remote Server): servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte stampante LPR.

## IoT Network

IoT Network crea una rete Wi-Fi dedicata per dispositivi IoT. Isolata dalla rete principale, offre migliore compatibilità e maggiore sicurezza.

**Nota**: alcuni modelli, ad esempio GL-MT5000 e GL-MT2500/GL-MT2500A, non dispongono della funzione Wi-Fi; pertanto le impostazioni di IoT Network non sono disponibili nel loro pannello di amministrazione web.

In IoT Network è possibile visualizzare direttamente lo stato dell'interfaccia, il VLAN ID, il gateway e l'intervallo DHCP.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Fare clic su **Edit** nell'angolo in basso a destra; il pannello di configurazione di IoT Network si aprirà sul lato destro della pagina. In questo pannello è possibile configurare Basic Settings e DHCP Server Settings.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Impostazioni di base

È possibile impostare la sottorete entro gli intervalli di indirizzi IPv4 privati: `192.168.0.0/16`, `172.16.0.0/12`, `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    Il **gateway predefinito** di IoT Network è **192.168.10.1**. Se entra in conflitto con la rete locale, cambiarlo con uno diverso.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. È anche possibile selezionare **255.255.0.0** se serve una sottorete più grande con più indirizzi IP.

- **VLAN ID**

    Il VLAN ID predefinito di IoT Network è **10** e può essere modificato secondo necessità.

- **AP Isolation**

    Questa funzione è disponibile dal firmware v4.5.

    È possibile isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

- **WAN Access Control**

    WAN Access Control gestisce l'accesso della sottorete locale alle reti lato WAN, inclusi Internet e altre sottoreti WAN.

    Sono disponibili tre modalità di controllo dell'accesso WAN:

    - **Unrestricted**: consente a questa sottorete di accedere a Internet e ad altre sottoreti lato WAN senza restrizioni.

    - **Block WAN Subnet**: blocca l'accesso ad altre sottoreti lato WAN. L'accesso a Internet resta disponibile.

    - **Block Internet Access**: blocca tutto l'accesso in uscita, inclusi Internet e le sottoreti lato WAN.

### Server DHCP

Il **DHCP Server** è abilitato per impostazione predefinita. Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client.

Se il server DHCP è disabilitato, sarà necessario configurare manualmente le impostazioni di rete dei dispositivi client. Fare clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

È possibile modificare gli indirizzi IP iniziale e finale in base alle proprie esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP o se viene modificato l'intervallo della maschera di sottorete.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Fare clic su **Advanced** per ulteriori configurazioni, se necessario.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: periodo di validità di un indirizzo IP assegnato da DHCP per un dispositivo.

- **Gateway**: dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server**: sono disponibili due campi DNS per configurare il resolver primario e quello secondario.

    **Nota**: il DNS primario viene inserito nel campo superiore e il secondario nel campo inferiore. Se il server primario non è disponibile, i dispositivi client passano automaticamente al resolver secondario, garantendo la continuità della risoluzione dei nomi di dominio.

- **LPR Server** (Line Printer Remote Server): servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte stampante LPR.

## VLAN Networks

Nella parte superiore della pagina principale è possibile creare ulteriori **VLAN networks** secondo necessità, per isolare diversi tipi di dispositivi o il traffico dei visitatori.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Fare clic sul pulsante **+ Add** sul lato destro della pagina per configurare una nuova rete.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Impostazioni di base

In questa pagina è possibile configurare le informazioni di base di **VLAN Networks**.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Personalizzare un nome per la sottorete appena creata, per identificarla.

- **Gateway**

    Configurare manualmente il gateway per la nuova sottorete. Sostituire questo gateway se entra in conflitto con il segmento LAN esistente.

- **Netmask**

    Il valore predefinito è **255.255.255.0**. È anche possibile selezionare **255.255.0.0** se serve una sottorete più grande con più indirizzi IP.

- **VLAN ID**

    Quando si crea una sottorete, è necessario assegnare un VLAN ID compreso tra **9** e **4000**. Evitare di usare un VLAN ID già occupato per prevenire conflitti di rete.

- **AP Isolation**

    Questa funzione è disponibile dal firmware v4.5.

    È possibile isolare i dispositivi client in un segmento di rete separato. Questi dispositivi non potranno comunicare con altri dispositivi sulla stessa rete.

- **WAN Access Control**

    WAN Access Control gestisce l'accesso della sottorete locale alle reti lato WAN, inclusi Internet e altre sottoreti WAN.

    Sono disponibili tre modalità di controllo dell'accesso WAN:

    - **Unrestricted**: consente a questa sottorete di accedere a Internet e ad altre sottoreti lato WAN senza restrizioni.

    - **Block WAN Subnet**: blocca l'accesso ad altre sottoreti lato WAN. L'accesso a Internet resta disponibile.

    - **Block Internet Access**: blocca tutto l'accesso in uscita, inclusi Internet e le sottoreti lato WAN.

### Server DHCP

Il **DHCP Server** è abilitato per impostazione predefinita. Il server DHCP assegna automaticamente indirizzi IP e altri parametri di comunicazione a ciascun dispositivo client.

Se il server DHCP è disabilitato, sarà necessario configurare manualmente le impostazioni di rete dei dispositivi client. Fare clic [qui](../tutorials/manually_configure_static_ip.md) per sapere come configurare manualmente un IP statico.

È possibile modificare gli indirizzi IP iniziale e finale in base alle proprie esigenze, ad esempio se la rete si espande o si riduce, se si verificano conflitti di indirizzi IP o se viene modificato l'intervallo della maschera di sottorete.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Fare clic su **Advanced** per ulteriori configurazioni, se necessario.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: periodo di validità di un indirizzo IP assegnato da DHCP per un dispositivo.

- **Gateway**: dispositivo che instrada il traffico tra la rete locale e le reti esterne, come Internet.

- **DNS Server**: sono disponibili due campi DNS per configurare il resolver primario e quello secondario.

    **Nota**: il DNS primario viene inserito nel campo superiore e il secondario nel campo inferiore. Se il server primario non è disponibile, i dispositivi client passano automaticamente al resolver secondario, garantendo la continuità della risoluzione dei nomi di dominio.

- **LPR Server** (Line Printer Remote Server): servizio che gestisce i processi di stampa e consente ai dispositivi di rete di inviare richieste di stampa a stampanti remote. È possibile configurare più porte stampante LPR.

Una volta configurata, la nuova rete VLAN apparirà nella pagina corrente con le informazioni della sottorete.

---

Ha ancora domande? Visiti il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o ci [contatti](https://www.gl-inet.com/contacts/){target="_blank"}.

