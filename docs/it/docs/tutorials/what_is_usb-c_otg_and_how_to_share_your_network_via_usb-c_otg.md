# Che cos'è USB-C OTG e come condividere la rete tramite USB-C OTG

## USB OTG
**USB OTG** (On-The-Go) e uno standard USB che consente ai dispositivi compatibili, come i router, di passare tra i ruoli **Host** e **Device**. Permette la trasmissione diretta dei dati e l'interazione di alimentazione senza un dispositivo host separato.

Le due modalita seguenti possono essere selezionate tramite **USB OTG**:

- Quando un dispositivo passa alla **modalita Host** tramite USB OTG, agisce da host USB, avvia la trasmissione dei dati, fornisce alimentazione e controlla tutte le operazioni di lettura e scrittura tra i due dispositivi collegati.

- In **Device mode**, il dispositivo funziona da periferica, riceve alimentazione dall'host e risponde passivamente ai suoi comandi, senza poter avviare autonomamente la comunicazione.

## Condivisione di rete tramite USB-C OTG su Mudi 7

La porta USB-C con supporto OTG di Mudi 7 funziona in modalita **Device** oppure **Host** per consentire una condivisione flessibile della rete con dispositivi esterni.

### Connessione a un computer

La maggior parte dei computer funziona solo come host e non supporta OTG. Quando un computer viene collegato al router tramite USB, il router mostra una finestra di selezione della modalita. Puoi scegliere qualsiasi modalita: Mudi 7 negoziera automaticamente il ruolo. Il computer lo riconoscera quindi come adattatore USB per l'accesso diretto a Internet, senza driver aggiuntivi.

### Connessione a uno smartphone

- **Device Mode**: Mudi 7 agisce come dispositivo USB e condivide la propria rete con il telefono.

- **Host Mode**: quando abiliti USB Tethering sul telefono, questo puo condividere la propria rete cellulare con Mudi 7 tramite USB. Questo collegamento USB puo funzionare come interfaccia WAN indipendente, abilitando Multi-WAN.

!!! Note

    1. Quando usi la funzione OTG del telefono per l'interconnessione, verifica che il telefono supporti OTG e usa un cavo USB idoneo al trasferimento dati. I cavi solo per ricarica non possono trasmettere segnali di rete.

    2. Quando Device Mode e abilitato, il telefono non mostra una notifica di connessione di rete. Per verificarne il funzionamento, controlla lo stato della rete nelle impostazioni del telefono oppure esegui un test di connettivita.

        Ad esempio, se condividi la rete di Mudi 7 con un telefono tramite **Device Mode** (ad esempio iPhone 17 Pro), verifica che Device Mode sia attivo seguendo i passaggi seguenti.

        1. Usa un cavo USB che supporta OTG per collegare la porta USB 3.1 di Mudi 7 al tuo iPhone 17 Pro.

        2. Su Mudi 7, seleziona **Device Mode**.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. Nelle impostazioni del telefono vedrai che Mudi 7 sta fornendo accesso di rete al telefono, come mostrato nello screenshot seguente.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
