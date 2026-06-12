# Wireless (Firmware v4.9)

> Questa guida si applica al firmware v4.9 e successivi. Per le versioni precedenti, fai clic [qui](wireless.md).

Sul lato sinistro del pannello di amministrazione web, vai su **WIRELESS**.

La pagina Wireless ti consente di configurare varie reti Wi-Fi, tra cui MLO Wi-Fi, disponibile su alcuni modelli selezionati, Rete principale, Rete ospite e Rete IoT. Le bande Wi-Fi supportate variano a seconda del modello.

## Multi-Link Operation (MLO)

??? "Modelli supportati"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Modelli non supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) e' una delle funzionalita' principali del Wi-Fi 7 (802.11be), progettata per migliorare le prestazioni della rete, ridurre sensibilmente la latenza e aumentare la stabilita' della connessione sfruttando contemporaneamente piu' bande di frequenza, come 2.4 GHz, 5 GHz e 6 GHz.

Si consiglia ai client Wi-Fi 7 di connettersi a MLO Wi-Fi, che migliora notevolmente throughput e affidabilita' della rete tramite connessioni multi-banda.

Fai clic su **Add** per configurare una rete MLO Wi-Fi, quindi fai clic su **Apply**. Tieni presente che le bande Wi-Fi disponibili variano a seconda del modello.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- **Wi-Fi Band**: seleziona almeno due bande radio.
- **Wi-Fi Security**: se selezioni la banda 6 GHz, WPA3-SAE e' l'unica opzione disponibile ed e' quella consigliata. Funziona al meglio con la maggior parte dei dispositivi che supportano MLO.
- **Enable Randomized BSSID**: se selezioni la banda 6 GHz, il BSSID a 6 GHz della rete MLO Wi-Fi verra' sincronizzato con quello del Main Wi-Fi.

Una volta abilitata, la pagina verra' visualizzata come segue.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Rete principale

La Rete principale e' la rete Wi-Fi primaria e supporta la trasmissione simultanea su diverse bande radio, tutte abilitate per impostazione predefinita. Puoi configurare impostazioni separate per ogni banda, ad esempio Wi-Fi SSID, modalita' di sicurezza, password, randomized BSSID, potenza TX, larghezza di banda e canale.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

Fai clic sull'icona a forma di ingranaggio sulla destra per visualizzare o modificare le impostazioni Wi-Fi di ciascuna banda. Tieni presente che le bande Wi-Fi disponibili variano a seconda del modello.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Rete ospite

La Rete ospite e' una rete Wi-Fi dedicata ai visitatori, con tutte le bande disabilitate per impostazione predefinita. Puoi abilitare e configurare le impostazioni di base della rete per ogni banda, come Wi-Fi SSID, modalita' di sicurezza, password e attivazione del randomized BSSID.

Fai clic su **Add** per configurare una rete Guest Wi-Fi, quindi fai clic su **Apply**. Tieni presente che le bande Wi-Fi disponibili variano a seconda del modello.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

Una volta abilitata, la pagina verra' visualizzata come segue.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## Rete IoT

La Rete IoT e' una rete Wi-Fi dedicata ai dispositivi smart, con tutte le bande disabilitate per impostazione predefinita. Puoi abilitare e configurare le impostazioni di base della rete per ogni banda, come Wi-Fi SSID, modalita' di sicurezza, password e attivazione del randomized BSSID.

Fai clic su **Add** per configurare una rete IoT Wi-Fi, quindi fai clic su **Apply**. Tieni presente che questa rete non include la banda 6 GHz e che le bande Wi-Fi disponibili variano a seconda del modello.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

Una volta abilitata, la pagina verra' visualizzata come segue.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"}.
