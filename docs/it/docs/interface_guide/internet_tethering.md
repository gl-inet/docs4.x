# Connettersi a Internet tramite USB tethering

Usare un cavo USB per condividere la rete dallo smartphone al router si chiama Tethering. Anche i modem host-less funzionano in modalita' Tethering durante la configurazione del modem.

**Nota:** alcuni operatori mobili limitano il tethering o applicano costi aggiuntivi. Ti consigliamo di verificarlo con il tuo operatore.

## Configurazione

=== "iPhone"

    1. Collega un iPhone alla porta USB del router tramite un cavo USB. Apparira' una finestra di sistema che chiede se fidarsi del dispositivo. Tocca **Trust** per procedere.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Vai su **Settings** -> **Personal Hotspot** dell'iPhone. Abilita **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Collega un computer o un altro telefono al router, quindi accedi al pannello di amministrazione web del router, vai alla sezione **INTERNET** -> **Tethering** e fai clic su **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connect.png){class="glboxshadow"}

        Se hai bisogno di impostazioni avanzate, ad esempio TTL, HL e MTU, fai clic su **Advanced** per personalizzarle, quindi fai clic su **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_advanced.png){class="glboxshadow"}

        Iniziera' la connessione.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Una volta connesso, lo stato dell'hotspot personale, ad esempio il numero di dispositivi collegati, appare nella barra di stato nella parte superiore dello schermo del telefono.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/3/setup/share/internet/tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Anche il pannello di amministrazione web mostrera' lo stato della connessione Tethering.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Collega un telefono Android alla porta USB del router tramite un cavo USB. Potrebbe apparire una finestra di sistema che chiede le preferenze USB. Se richiesto, seleziona **USB Tethering** oppure **File Transfer**.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Vai su **Settings** -> **Network & Internet** -> **Personal Hotspot** del telefono. Abilita **Personal Hotspot** oppure **USB Tethering**.

        I passaggi per abilitare USB Tethering variano in base alla marca. Controlla le impostazioni del dispositivo per la posizione esatta e contatta il supporto del produttore se necessario.

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Collega un computer o un altro telefono al router, quindi accedi al pannello di amministrazione web del router, vai alla sezione **INTERNET** -> **Tethering** e fai clic su **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connect.png){class="glboxshadow"}

        Se hai bisogno di impostazioni avanzate, ad esempio TTL, HL e MTU, fai clic su **Advanced** per personalizzarle, quindi fai clic su **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_advanced.png){class="glboxshadow"}

        Iniziera' la connessione.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Una volta connesso, lo stato dell'hotspot personale, ad esempio il numero di dispositivi collegati, appare nella barra di stato nella parte superiore dello schermo del telefono.

        Anche il pannello di amministrazione web mostrera' lo stato della connessione Tethering.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/tutorials/internet_tethering/android_connected.png){class="glboxshadow"}

    Per la documentazione ufficiale Android, fai riferimento a [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Avviso

Quando l'accesso a Internet non e' disponibile, verra' visualizzato il seguente avviso:

**"The interface is connected, but the Internet can't be accessed."**

Soluzioni:

1. Controlla se lo smartphone ha accesso a Internet.

2. Vai alla pagina [Multi-WAN](multi-wan.md) per determinare se puoi accedere a Internet oppure no.

## Risoluzione dei problemi

Se la connessione non riesce, prova questi passaggi di risoluzione dei problemi:

- Usa l'alimentatore originale del router.
- Scollega e ricollega il cavo USB.
- Usa un altro cavo USB. Assicurati che supporti il trasferimento dati, non solo la ricarica.
- Disattiva e riattiva "USB Tethering" alcune volte, per telefoni Android.
- Disattiva e riattiva "Allow Others to Join" alcune volte, per iPhone.
- Riavvia lo smartphone e riprova.

---

Articoli correlati

- [Pagina Internet](internet.md)
- [Come impostare la priorita' di ciascun metodo di accesso a Internet?](multi-wan.md)
- [Come impostare il bilanciamento del carico quando vengono usati contemporaneamente piu' metodi di accesso a Internet?](multi-wan.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
