# Porta Ethernet

**Nota**: questa pagina e' disponibile come **Port Management** dal firmware v4.7 ed e' stata rinominata in **Ethernet Port** nel firmware v4.8.3.

---

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Port Management** oppure **Ethernet Port**.

Questa pagina consente di gestire le funzioni delle porte Ethernet, WAN/LAN, e di visualizzare i dettagli della porta, come indirizzo MAC e velocita' negoziata.

## WAN

Questa sezione mostra la funzione della porta, WAN o LAN, l'indirizzo MAC e la velocita' negoziata.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN**: la modalita' operativa corrente della porta WAN fisica. Se necessario, puoi impostarla su LAN.

- **MAC Mode**: per impostazione predefinita e' Factory Mode. Puoi cambiarla in Clone Mode oppure Random Mode.

- **Mac Address**: l'indirizzo MAC dell'interfaccia WAN.

- **Negotiated Network Port Rate**: la velocita' di collegamento negoziata dell'interfaccia WAN, mostrata solo quando viene rilevato un collegamento valido.

## LAN

Questa sezione mostra la velocita' negoziata della porta LAN. Viene visualizzata solo quando viene rilevato un collegamento valido.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Alcuni modelli supportano la commutazione di LAN 1 in una porta WAN per scenari Dual-Ethernet WAN. Fai clic su [Dual-Ethernet WAN](#dual-ethernet-wan) per i dettagli.

## Dual-Ethernet WAN

La funzione Dual-Ethernet WAN consente di trasformare una porta Ethernet LAN predefinita in una porta WAN secondaria per l'accesso Internet tramite doppia Ethernet. Offre una connettività di backup affidabile e supporta l'aggregazione della banda, dove compatibile, per carichi di lavoro che richiedono molta banda. Consente inoltre di collegarsi contemporaneamente a due reti indipendenti, ad esempio una di lavoro e una personale, aumentando la flessibilità senza hardware aggiuntivo.

??? "Modelli supportati"
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

    **Nota**: GL-E5800 (Mudi 7) è dotato di una porta Ethernet (LAN per impostazione predefinita, commutabile in WAN) e di una **porta USB-C con supporto OTG**. Per aggiungere una seconda porta Ethernet per Dual-Ethernet WAN, collega alla porta USB-C un adattatore USB-C-Ethernet venduto separatamente.

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

Segui i passaggi seguenti per commutare una porta LAN in una porta WAN.

1. Nella pagina **Port Management** o **Ethernet Port**, fai clic sulla scheda **LAN**, cambia il ruolo della porta in WAN, quindi fai clic su **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. Nella finestra pop-up, fai clic su **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. La porta selezionata ora funzionerà come porta WAN. Puoi quindi configurare Multi-WAN [qui](multi-wan.md).

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
