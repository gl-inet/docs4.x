# Come configurare manualmente un IP statico sui dispositivi client?

=== "Windows 11"

    In Windows 11, puoi impostare un indirizzo IP statico dall'app Impostazioni sia per gli adattatori wireless sia per quelli cablati.

    **Impostare un indirizzo IP statico sull'adattatore Wi-Fi**

    Per assegnare una configurazione IP statica a un adattatore Wi-Fi, segui questi passaggi:

    1. Apri Impostazioni in Windows 11 -> Network & Internet -> scheda Wi-Fi -> seleziona la connessione di rete attuale.

    2. Nella sezione "IP settings", fai clic sul pulsante Edit.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.webp){class="glboxshadow"}

    3. Segui i passaggi sotto per configurarlo:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Seleziona l'opzione Manual e attiva l'interruttore IPv4.

        - Imposta un indirizzo IP statico per Windows 11, ad esempio 10.1.4.119.

        - Specifica una subnet mask, ad esempio 255.255.255.0.

        - Specifica l'indirizzo Default Gateway.

        - Specifica un indirizzo Preferred DNS, obbligatorio.

        - Facoltativo: specifica un indirizzo Alternate DNS.

        - Usa il menu a discesa "DNS over HTTPS" e seleziona Off per gli indirizzi preferito e alternativo, ma puoi abilitare DoH con queste opzioni:

            - Off: trasmette tutto il traffico DNS senza crittografia.

            - On (automatic template): invia tutto il traffico DNS con crittografia.

            - On (manual template): consente di specificare un template preciso. E richiesto solo se il servizio DNS non funziona automaticamente o dispone di un template che funziona come previsto.

        - Disattiva l'interruttore "Fallback to plaintext", se abiliti DoH.

            - Suggerimento rapido: se abiliti questa funzione, il sistema cifra il traffico DNS, ma consente comunque di inviare query senza crittografia.

    4. Fai clic sul pulsante Save.

        Una volta completati i passaggi, la configurazione di rete statica verra applicata al computer. Puoi testare le nuove impostazioni aprendo il browser e caricando un sito web.


    ## **Impostare un indirizzo IP statico sull'adattatore Ethernet**

    Per assegnare un indirizzo IP statico a un adattatore Ethernet cablato in Windows 11, segui questi passaggi:

    1. Apri Impostazioni -> Network & Internet -> scheda Ethernet.

    2. Nella sezione "IP settings", fai clic sul pulsante Edit.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.webp){class="glboxshadow"}

    3. Segui i passaggi sotto per configurarlo:

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.webp){class="glboxshadow"}

        - Seleziona l'opzione Manual.

        - Attiva l'interruttore IPv4.

        - Imposta un indirizzo IP statico per Windows 11, ad esempio 10.1.4.119.

        - Specifica una subnet mask, ad esempio 255.255.255.0.

        - Specifica l'indirizzo Default Gateway.

        - Specifica un indirizzo Preferred DNS, obbligatorio.

        - Facoltativo: specifica un indirizzo Alternate DNS.

        - Usa il menu a discesa "DNS over HTTPS" e seleziona Off per gli indirizzi preferito e alternativo, ma puoi abilitare DoH con queste opzioni:

            * Off: trasmette tutto il traffico DNS senza crittografia.

            * On (automatic template): invia tutto il traffico DNS con crittografia.

            * On (manual template): consente di specificare un template preciso. E richiesto solo se il servizio DNS non funziona automaticamente o dispone di un template che funziona come previsto.

        - Disattiva l'interruttore "Fallback to plaintext", se abiliti DoH.

    4. Fai clic sul pulsante Save.

        Dopo aver completato i passaggi, puoi verificare le impostazioni usando il browser per aprire un sito web.


=== "macOS"

    Ecco come impostare un indirizzo IP statico in macOS:

    Se possiedi un MacBook, potresti voler creare una nuova posizione di rete. In questo modo potrai usare l'indirizzo IP statico per alcune reti e non per altre.

    Dal menu Apple, seleziona System Preferences.

    Seleziona Network. Apparira la finestra mostrata sotto.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.webp){class="glboxshadow"}

    Dalla barra laterale, seleziona un'interfaccia di rete attiva. In questo esempio sei connesso a una rete wireless, quindi seleziona Wi-Fi.

    Annota l'indirizzo IP attualmente assegnato al Mac. Dovrai scegliere un nuovo indirizzo IP all'interno dell'intervallo di indirizzi IP privati indicato. Maggiori dettagli tra poco.

    Fai clic su Advanced.

    Seleziona TCP/IP. Apparira la finestra mostrata sotto.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.webp){class="glboxshadow"}

    Nel menu Configure IPv4, seleziona Manually.

    Inserisci un indirizzo IP statico nel campo IPv4 Address. Quale numero inserire? Un metodo consiste nel prendere l'indirizzo IP corrente e cambiare l'ultima parte del numero. In questo esempio, potresti scegliere qualsiasi indirizzo tra 192.168.7.0 e 192.168.7.255, purche l'indirizzo non sia gia assegnato a un altro dispositivo.

    Fai clic su OK -> fai clic su Apply.


=== "Android"

    I passaggi variano a seconda della versione di Android. Questa documentazione si basa su Android 11.

    1. Vai su Impostazioni -> seleziona Network & Internet, poi Wi-Fi -> tocca la rete attualmente connessa per aprire il menu delle impostazioni.

    ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
    {class="glboxshadow"}

    2. Per impostare un indirizzo IP statico, procedi come segue:

    - Seleziona l'icona della matita in alto a destra per accedere alle impostazioni di rete.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Seleziona Advanced Options.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Seleziona IP Settings.

    - Cambia l'impostazione da DHCP a Static.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    - Quando usi indirizzi IP statici su reti domestiche e altre reti private, devono essere scelti all'interno dei seguenti intervalli di indirizzi IP privati standard: 10.0.0.0 fino a 10.255.255.255, 172.16.0.0 fino a 172.31.255.255, 192.168.0.0 fino a 192.168.255.255.

    - Ora inserisci l'indirizzo IP.
        - Questo passaggio dipende dalla rete in uso. Ad esempio: 192.168.1.128.

    - Gateway dovrebbe essere compilato automaticamente in base all'indirizzo IP. In caso contrario, copia l'indirizzo IP e sostituisci l'ultimo numero con 1.
        - Ad esempio, in base all'esempio precedente: 192.168.1.1.

    3. Tocca Save e lascia che la rete si ricolleghi.

=== "iOS"

    Quando usi indirizzi IP statici su reti domestiche e altre reti private, devono essere scelti all'interno dei seguenti intervalli di indirizzi IP privati standard:

    10.0.0.0 fino a 10.255.255.255
    172.16.0.0 fino a 172.31.255.255
    192.168.0.0 fino a 192.168.255.255

    Per impostare un indirizzo IP statico, procedi come segue:

    - Tocca l'icona Settings.

    - Vai su Wi-Fi.

    - Tocca l'icona blu delle informazioni, i, accanto al nome della rete Wi-Fi.
         - Se usi una versione precedente a iOS 7, potrebbe apparire come un errore blu.

    - Vai alla scheda Static, mostrata sotto.

    ![IP_Settings_Screen_iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/IP_Settings_Screen_iOS.png){class="glboxshadow"}

    - Tocca il campo IP Address.

    - Inserisci l'indirizzo IP statico che vuoi usare sul tuo iPhone o iPad.

    - Tocca il campo Router.

    - Inserisci l'indirizzo IP del router.

    - Tocca Subnet Mask e inserisci le informazioni richieste.

        - Di solito sara 225.225.0.0.

    - Tocca il pulsante Wi-Fi nell'angolo in alto a sinistra dello schermo per salvare le impostazioni.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
