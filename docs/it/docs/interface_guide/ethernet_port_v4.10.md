# Porta Ethernet (firmware v4.10)

**Nota**: il contenuto di questa pagina è attualmente disponibile su Flint 4 (GL-BE14000) e verrà esteso ad altri modelli con il firmware v4.10.

Se il dispositivo utilizza una versione firmware diversa, usare il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Firmware v4.9 e precedenti](ethernet_port.md)

</div>

---

Nel menu a sinistra del pannello di amministrazione web, andare su **NETWORK** -> **Ethernet Port**.

Questa pagina mostra tutte le interfacce del router. È possibile visualizzare lo stato della connessione di ogni interfaccia, gestire il ruolo delle porte Ethernet (WAN o LAN) e consultare dettagli quali indirizzo MAC, velocità negoziata e stato corrente del collegamento. È inoltre possibile assegnare le interfacce fisiche a qualsiasi sottorete creata.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: quando l'icona della porta è evidenziata in blu, il collegamento fisico è attivo.

- **Link Down**: quando l'icona della porta è grigia, il collegamento fisico non è attivo.

- **Speed**: velocità di trasmissione negoziata della porta Ethernet.

- **MAC**: indirizzo MAC della porta.

- **VLAN Mode**: la modalità operativa delle porte LAN può essere impostata su Standard o Multiple VLANs.

- **Native Network**: sottorete predefinita senza tag assegnata alla porta LAN.

- **Allowed VLANs**: specifica le VLAN con tag autorizzate a transitare attraverso la porta in modalità Multiple VLANs.

- **Settings**: fare clic per accedere alla pagina di configurazione della singola porta.

## WAN

Questa sezione mostra il ruolo della porta (WAN o LAN), l'indirizzo MAC e la velocità negoziata.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: modalità operativa corrente della porta WAN fisica. Se necessario, può essere impostata su LAN.

- **MAC Mode**: l'impostazione predefinita è Factory Mode. È possibile passare a Clone Mode o Random Mode.

- **MAC Address**: indirizzo MAC dell'interfaccia WAN.

- **Negotiated Network Port Rate**: velocità di collegamento negoziata dell'interfaccia WAN, visualizzata solo quando viene rilevato un collegamento valido.

## LAN

Questa sezione mostra la configurazione della porta LAN. È possibile impostare Ethernet Mode su **Standard** o **Multiple VLANs**, in base alle esigenze.

### Modalità Standard

La modalità Standard consente una sola VLAN (Untagged) ed è utilizzata per collegare i dispositivi terminali.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: velocità di collegamento negoziata dell'interfaccia LAN, visualizzata solo quando viene rilevato un collegamento valido.

- **Ethernet Mode**: l'impostazione predefinita è Standard Mode.
  
- **Access Network**: consente di isolare le reti assegnando le porte LAN a sottoreti diverse.

Dopo la configurazione, tornare alla pagina Ethernet Port per verificare le impostazioni.

### Modalità Multiple VLANs

La modalità Multiple VLANs consente di utilizzare più VLAN (Tagged) su una porta, in genere per collegare access point o altri switch.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: velocità di collegamento negoziata dell'interfaccia LAN, visualizzata solo quando viene rilevato un collegamento valido.

- **VLAN Mode**: per passare alla modalità Multiple VLANs, fare clic sulla scheda Multiple VLANs.

- **Untagged Traffic Handling**: configurare la gestione dei pacchetti senza tag della porta. È possibile eliminarli direttamente oppure inoltrarli a un'altra sottorete, utilizzata come rete PVID nativa.

- **Allowed Tagged Networks**: specifica le VLAN che possono transitare attraverso la porta in modalità con tag. È possibile selezionare le reti VLAN dall'elenco; verrà inoltrato solo il traffico corrispondente.

Dopo la configurazione, tornare alla pagina Ethernet Port per verificare le impostazioni.

Alcuni modelli consentono di convertire LAN 1 in una porta WAN per utilizzare due connessioni Ethernet WAN. Per maggiori dettagli, consultare [Dual-Ethernet WAN](#dual-ethernet-wan).

## Dual-Ethernet WAN

La funzione Dual-Ethernet WAN consente di convertire una porta Ethernet LAN predefinita in una porta WAN secondaria per accedere a Internet tramite due connessioni Ethernet. Offre una connessione di backup affidabile e, dove compatibile, supporta l'aggregazione della larghezza di banda per i carichi che ne fanno un uso intensivo. Consente inoltre di collegarsi contemporaneamente a due reti indipendenti, ad esempio una di lavoro e una personale, aumentando la flessibilità senza hardware aggiuntivo.

??? "Modelli supportati"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Nota**: GL-E5800 (Mudi 7) è dotato di una porta Ethernet (LAN per impostazione predefinita, commutabile su WAN) e di una **porta USB-C con supporto OTG**. Per aggiungere una seconda porta Ethernet per Dual-Ethernet WAN, collegare alla porta USB‑C un adattatore da USB‑C a Ethernet venduto separatamente.

??? "Modelli non supportati"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Per convertire una porta LAN in una porta WAN, procedere come segue. Nell'esempio viene utilizzato Flint 3 (GL-BE9300).

1. Nella pagina **Ethernet Port**, fare clic sull'impostazione **LAN1** per aprire la pagina Configuration. Impostare quindi il ruolo della porta su WAN e fare clic su **Apply**.
   
    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Tornare alla pagina Ethernet Port per verificare che il ruolo della porta sia stato impostato su WAN.
   
    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. La porta selezionata funzionerà ora come porta WAN. È quindi possibile configurare Multi-WAN [qui](multi-wan.md).

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
