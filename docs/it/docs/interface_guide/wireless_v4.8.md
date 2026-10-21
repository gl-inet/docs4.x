# Wireless (firmware v4.8 e precedenti) {#wireless-firmware-v48-and-earlier}

Il contenuto di questa pagina si basa sulla versione firmware v4.8.x e precedenti. Se il dispositivo usa una versione firmware diversa, usa il selettore seguente per passare alla guida corrispondente.

<div class="gl-link-select" data-label="Versione firmware" data-placeholder="Firmware v4.8 e precedenti" markdown="1">

- [Firmware v4.9 e successivi](wireless.md)

</div>

---


Sul lato sinistro del pannello di amministrazione web, vai su **WIRELESS**.

La pagina Wireless consente di configurare reti Wi-Fi separate, incluse 2.4 GHz, 5 GHz, 6 GHz e Wi-Fi MLO, a seconda del modello. Ogni banda può essere configurata come Main Wi-Fi oppure Guest Wi-Fi per una gestione wireless flessibile.

**Nota**: alcuni modelli non supportano il Wi-Fi a 5 GHz, come GL-MT300N-V2 (Mango), GL-X300B (Collie) e GL-XE300 (Puli); alcuni invece non hanno alcuna funzione Wi-Fi, come GL-MT5000 (Brume 3) e GL-MT2500/GL-MT2500A (Brume 2).

## MLO Wi-Fi {#mlo-wi-fi}

| Modelli supportati              |           |
| :------------------------------ | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)        | √         |
| Beryl 7 (GL-MT3600BE)           | √         |
| Flint 3e (GL-BE6500)            | √         |
| Flint 3 (GL-BE9300)             | √         |
| Slate 7 (GL-BE3600)             | √         |

MLO (Multi-Link Operation) è una delle funzionalità chiave del Wi-Fi 7 (802.11be), progettata per migliorare le prestazioni della rete, ridurre sensibilmente la latenza e aumentare la stabilità della connessione utilizzando contemporaneamente più bande di frequenza, come 2.4 GHz, 5 GHz e 6 GHz.

Fai clic sulle schede qui sotto per conoscere le impostazioni di MLO Main Wi-Fi e MLO Guest Wi-Fi.

=== "MLO Wi-Fi"

    MLO Main Wi-Fi consente di configurare diverse impostazioni, tra cui abilitazione/disabilitazione del Wi-Fi, selezione delle bande radio, almeno due, abilitazione/disabilitazione del BSSID casuale, nome Wi-Fi SSID, sicurezza Wi-Fi, password Wi-Fi e visibilità dell'SSID.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Se le bande radio del Wi-Fi MLO includono 6 GHz, il BSSID del Wi-Fi MLO verrà sincronizzato quando cambia il BSSID del Wi-Fi a 6 GHz.

    - La sicurezza Wi-Fi predefinita per MLO Wi-Fi è WPA3-SAE, adatta alla maggior parte dei dispositivi che supportano MLO.

=== "MLO Guest Wi-Fi"

    MLO Guest Wi-Fi consente di configurare impostazioni semplificate, tra cui abilitazione/disabilitazione del Wi-Fi, selezione delle bande radio, almeno due, nome Wi-Fi SSID, sicurezza Wi-Fi, password e visibilità dell'SSID.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## Wi-Fi a 6 GHz {#6-ghz-wi-fi}

| Modelli supportati              |           |
| :------------------------------ | :-------: |
| Slate 7 Pro (GL-BE10000)        | √         |
| Mudi 7 (GL-E5800)               | √         |
| Flint 3 (GL-BE9300)             | √         |

Il Wi-Fi a 6 GHz offre connettività wireless più veloce e stabile, con minore congestione rispetto alle bande 2.4 GHz e 5 GHz.

Fai clic sulle schede qui sotto per conoscere le impostazioni di 6 GHz Main Wi-Fi e 6 GHz Guest Wi-Fi.

=== "6 GHz Wi-Fi"

    6 GHz Main Wi-Fi consente di configurare diverse impostazioni, tra cui abilitazione/disabilitazione del Wi-Fi, potenza TX, abilitazione/disabilitazione del BSSID casuale, nome Wi-Fi SSID, sicurezza Wi-Fi, password Wi-Fi, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - Enable PSC: quando PSC, Preferred Scanning Channel, è abilitato, verranno riservati solo i canali con migliore connettività per garantire la connessione dei dispositivi a 6 GHz.

=== "6 GHz Guest Wi-Fi"

    6 GHz Guest Wi-Fi consente di configurare impostazioni semplificate, tra cui abilitazione/disabilitazione del Wi-Fi, nome Wi-Fi SSID, sicurezza Wi-Fi, password e visibilità dell'SSID.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## Wi-Fi a 5 GHz {#5-ghz-wi-fi}

Fai clic sulle schede qui sotto per conoscere le impostazioni di 5 GHz Main Wi-Fi e 5 GHz Guest Wi-Fi.

=== "5 GHz Wi-Fi"

    5 GHz Main Wi-Fi consente di configurare diverse impostazioni, tra cui abilitazione/disabilitazione del Wi-Fi, potenza TX, abilitazione/disabilitazione del BSSID casuale, nome Wi-Fi SSID, sicurezza Wi-Fi, password Wi-Fi, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi-Fi"

    5 GHz Guest Wi-Fi consente di configurare impostazioni semplificate, tra cui abilitazione/disabilitazione del Wi-Fi, nome Wi-Fi SSID, sicurezza Wi-Fi, password e visibilità dell'SSID.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## Wi-Fi a 2.4 GHz {#24-ghz-wi-fi}

Fai clic sulle schede qui sotto per conoscere le impostazioni di 2.4 GHz Main Wi-Fi e 2.4 GHz Guest Wi-Fi.

=== "2.4 GHz Wi-Fi"

    2.4 GHz Main Wi-Fi consente di configurare diverse impostazioni, tra cui abilitazione/disabilitazione del Wi-Fi, potenza TX, abilitazione/disabilitazione del BSSID casuale, nome Wi-Fi SSID, sicurezza Wi-Fi, password Wi-Fi, visibilità dell'SSID, modalità Wi-Fi, larghezza di banda e canale.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi-Fi"

    2.4 GHz Guest Wi-Fi consente di configurare impostazioni semplificate, tra cui abilitazione/disabilitazione del Wi-Fi, nome Wi-Fi SSID, sicurezza Wi-Fi, password e visibilità dell'SSID.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## Impostazioni Wi-Fi generali {#general-wi-fi-settings}

* Passa il cursore sull'icona del QR code accanto all'SSID Wi-Fi per visualizzare il relativo QR code. Puoi scansionarlo con telefono o tablet per connetterti rapidamente alla rete Wi-Fi corrispondente.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: abilitata per impostazione predefinita, impedisce di tracciare il router tramite un BSSID fisso. Per i dettagli, consulta [Randomized BSSID](#randomized-bssid).

* **Bandwidth** e **Channel** non possono essere modificati quando il router funziona come [repeater](internet_repeater.md), poiché seguono quelli della rete ripetuta.

* Quando **Channel** è impostato su **Auto**, il Wi-Fi del router non passerà automaticamente ai canali DFS.

* Quando si cambia **Channel** da un canale non-DFS a un canale DFS, verrà visualizzato un avviso come segue.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* Quando **Bandwidth** è impostata su **160 MHz**, disponibile solo su alcuni modelli, il Wi-Fi utilizzerà sempre un canale DFS, anche se nelle impostazioni del canale scegli un canale non-DFS oppure Auto.

## Randomized BSSID {#randomized-bssid}

Randomized BSSID è una funzione di protezione della privacy disponibile dal firmware v4.6 e abilitata per impostazione predefinita. Impedisce di localizzare e tracciare il router tramite un BSSID Wi-Fi fisso (l'indirizzo MAC dell'interfaccia wireless del router).

**Perché un BSSID fisso rappresenta un rischio per la privacy**

I sistemi operativi mobili, ad esempio Android e iOS, usano la localizzazione Wi-Fi basata sui dati raccolti dai dispositivi degli utenti per fornire servizi di posizione:

1. I dispositivi client, come telefoni e portatili, caricano periodicamente sui server del fornitore del sistema operativo o del dispositivo i BSSID rilevati, insieme alla propria posizione GPS.

2. I fornitori aggregano questi dati in un database globale che associa i BSSID alle posizioni.

3. Qualsiasi dispositivo con Wi-Fi abilitato, anche senza GPS, può interrogare quel database per stimare la propria posizione dai BSSID circostanti.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

Di conseguenza, un router con BSSID fisso agisce come un segnale di posizione stabile: può essere geolocalizzato da remoto e i suoi spostamenti, ad esempio durante un viaggio, possono essere tracciati nel tempo. Gli attaccanti possono anche interrogare questi database per localizzare i router o identificarne le caratteristiche tramite le informazioni sul produttore contenute nel BSSID (OUI).

**Come Randomized BSSID ti protegge**

Quando la funzione è abilitata, il router genera un BSSID casuale e lo rinnova a ogni avvio. Poiché il BSSID cambia continuamente, non può più essere associato a una posizione fissa nei database dei fornitori, interrompendo l'associazione tra BSSID e posizione usata per il tracciamento.

| Stato | Comportamento |
| ----------------- | ---------------------- |
| Abilitato (predefinito) | A ogni avvio viene generato un nuovo BSSID casuale |
| Disabilitato | Il router usa il proprio indirizzo MAC di fabbrica come BSSID |

**Note**:

1. Il BSSID cambia solo quando il router si riavvia; rimane invariato durante una sessione di funzionamento.
2. Per Guest Wi-Fi, il BSSID resta coerente con quello di Main Wi-Fi sulla stessa banda di frequenza.
3. Se le bande radio MLO Wi-Fi includono 6 GHz, il BSSID MLO Wi-Fi si sincronizza con quello del Wi-Fi a 6 GHz.
4. Randomized BSSID impedisce il tracciamento tramite il BSSID del router, ma non impedisce ai dispositivi client di comunicare la propria posizione e non offre una protezione completa della privacy: SSID, canale e caratteristiche del segnale restano osservabili.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"}.
