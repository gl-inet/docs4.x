# Come bloccare dispositivi client specifici su un router GL.iNet

Questo tutorial mostra come bloccare dispositivi client specifici su un router GL.iNet. Bloccando i dispositivi client, impedisci accessi non autorizzati alla rete. Questo aiuta a migliorare la sicurezza della rete o a controllare l'accesso a Internet della tua famiglia.

I router GL.iNet bloccano i dispositivi client in base ai loro indirizzi MAC, un identificatore univoco di 12 caratteri assegnato ai singoli dispositivi in rete. Questo metodo e' chiamato anche filtro degli indirizzi MAC.

Esistono due metodi per bloccare i dispositivi client sul router GL.iNet: tramite [pannello di amministrazione del router](#bloccare-i-dispositivi-client-tramite-il-pannello-di-amministrazione) oppure tramite [app mobile GL.iNet](#bloccare-i-dispositivi-client-tramite-lapp-mobile-glinet).

## Bloccare i dispositivi client tramite il pannello di amministrazione

### 1. Accedi al pannello di amministrazione

In un browser web, inserisci `192.168.8.1`. Inserisci la password, poi fai clic su **Login**.

### 2. Blocca i dispositivi client

Esistono due modi per bloccare i dispositivi client, a seconda che tu abbia o meno i loro indirizzi MAC:

* Se non hai i loro indirizzi MAC, usa il [primo metodo](#metodo-1-bloccare-dispositivi-senza-conoscere-i-loro-indirizzi-mac), che consente di bloccare i dispositivi che appaiono negli elenchi.
* Se hai i loro indirizzi MAC, usa il [secondo metodo](#metodo-2-bloccare-dispositivi-con-i-loro-indirizzi-mac).

#### Metodo 1: bloccare dispositivi senza conoscere i loro indirizzi MAC

1. Nella barra laterale sinistra, fai clic su **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Accanto al dispositivo, attiva l'interruttore.
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Se non vedi negli elenchi i dispositivi che vuoi bloccare, dovrai bloccarli [aggiungendo i loro indirizzi MAC alla blocklist](#metodo-2-bloccare-dispositivi-con-i-loro-indirizzi-mac).

#### Metodo 2: bloccare dispositivi con i loro indirizzi MAC

Per usare questo metodo, devi prima ottenere l'indirizzo MAC del dispositivo. Fai riferimento alle istruzioni fornite dal produttore del dispositivo.
Una volta ottenuto l'indirizzo MAC del dispositivo, segui questi passaggi:

1. Nella barra laterale sinistra, fai clic su **Clients**.
2. In alto, fai clic su **Blocklist**.
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Segui uno dei due metodi per bloccare i dispositivi:
    - Per inserire gli indirizzi MAC singolarmente, inseriscili nel campo vuoto.
    - Per importare un elenco di indirizzi MAC, fai clic su **Import Clients**. Importa un file, poi fai clic su **Import**.
4. Fai clic su **Apply**.
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Bloccare i dispositivi client tramite l'app mobile GL.iNet

**Nota**: prima di iniziare, installa e configura l'app mobile GL.iNet sul tuo dispositivo.

Esistono due modi per bloccare i dispositivi client, a seconda che tu abbia o meno i loro indirizzi MAC:

* Se non hai i loro indirizzi MAC, usa il [primo metodo](#mobile-1), che consente di bloccare i dispositivi che appaiono nell'elenco.
* Se hai i loro indirizzi MAC, usa il [secondo metodo](#mobile-2).

### Metodo 1: bloccare dispositivi senza conoscere i loro indirizzi MAC {#mobile-1}

1. Nella schermata principale dell'app, tocca il dispositivo che vuoi bloccare sotto **Connected Clients** e **Office Clients**.
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. In **Settings**, attiva l'interruttore **Block**.
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Se non vedi negli elenchi i dispositivi che vuoi bloccare, dovrai bloccarli [aggiungendo i loro indirizzi MAC alla blocklist](#method-2-block-devices-with-their-mac-addresses-1)

### Metodo 2: bloccare dispositivi con i loro indirizzi MAC {#mobile-2}

Per usare questo metodo, devi ottenere l'indirizzo MAC del dispositivo che vuoi bloccare. Fai riferimento alle istruzioni fornite dal produttore.
Una volta ottenuto l'indirizzo MAC del dispositivo, segui questi passaggi:

1. Nella schermata principale dell'app, tocca l'icona Settings > **Access Control**.
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Tocca **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Segui uno dei due metodi per bloccare i dispositivi:
    - Per inserire gli indirizzi MAC singolarmente, tocca **Add MAC address**. Inserisci l'indirizzo MAC, poi tocca **Done**.
    - Per importare un elenco di indirizzi MAC, fai clic su **Import Clients** > **Import Clients**. Tocca un file.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
