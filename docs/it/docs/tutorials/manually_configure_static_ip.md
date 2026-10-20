# Come configurare manualmente un IP statico sui dispositivi client?

=== "Windows 11"

    In Windows 11, puoi impostare un indirizzo IP statico sia per gli adattatori wireless sia per quelli cablati.

    **Impostare un indirizzo IP statico sull’adattatore Wi-Fi**

    1. Su un PC Windows 11, vai su **Settings** -> **Network & internet** -> **Wi-Fi** e seleziona la connessione Wi-Fi attuale.

    2. Individua **IP assignment** e fai clic sul pulsante **Edit**.

        ![Windows 11 edit IP address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. Nella finestra popup, seleziona **Manual** e attiva **IPv4**.

        ![Configurazione IP manuale](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Segui questi passaggi per modificare le impostazioni IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: imposta un indirizzo IP statico, ad esempio `10.1.4.119`.

        - Subnet mask: specifica una maschera di sottorete, ad esempio `255.255.255.0`.

        - Gateway: inserisci l’indirizzo del gateway, in genere l’IP LAN del router nella stessa sottorete. Ad esempio, se il tuo IP è `10.1.4.119`, il gateway è solitamente `10.1.4.1`.

        - Preferred DNS: specifica un indirizzo DNS preferito (obbligatorio). Puoi utilizzare un server DNS pubblico, ad esempio il server DNS di Google `8.8.8.8`.

        - Alternate DNS: specifica un indirizzo DNS alternativo (facoltativo).

        - DNS over HTTPS: seleziona "Off". Sono disponibili tre opzioni:

            - Off: trasmette tutto il traffico DNS senza crittografia.

            - On (automatic template): invia tutto il traffico DNS con crittografia.

            - On (manual template): consente di specificare un template preciso. È richiesto solo se il servizio DNS non funziona automaticamente o dispone di un template che funziona come previsto.

        - Disattiva l’interruttore "Fallback to plaintext" se abiliti DNS over HTTPS.

            **Suggerimento**: se abiliti questa funzione, il sistema cifra il traffico DNS, ma consente comunque di inviare query senza crittografia.

    5. Fai clic su **Save** per applicare le impostazioni.

        Una volta completati i passaggi, la configurazione di rete statica verrà applicata al computer. Puoi testare le nuove impostazioni aprendo il browser e caricando un sito web.

    ---

    **Impostare un indirizzo IP statico sull’adattatore Ethernet**

    1. Su un PC Windows 11, vai su **Settings** -> **Network & internet** -> **Ethernet**.

    2. Individua **IP assignment** e fai clic sul pulsante **Edit**.

        ![Edit_TCP/IP_Ethernet_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. Nella finestra popup, seleziona **Manual** e attiva **IPv4**.

        ![Configurazione IP manuale](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Segui questi passaggi per modificare le impostazioni IP.

        ![Settings_app_set_static_IP_address](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: imposta un indirizzo IP statico, ad esempio `10.1.4.119`.

        - Subnet mask: specifica una maschera di sottorete, ad esempio `255.255.255.0`.

        - Gateway: inserisci l’indirizzo del gateway, in genere l’IP LAN del router nella stessa sottorete. Ad esempio, se il tuo IP è `10.1.4.119`, il gateway è solitamente `10.1.4.1`.

        - Preferred DNS: specifica un indirizzo DNS preferito (obbligatorio). Puoi utilizzare un server DNS pubblico, ad esempio il server DNS di Google `8.8.8.8`.

        - Alternate DNS: specifica un indirizzo DNS alternativo (facoltativo).

        - DNS over HTTPS: seleziona "Off". Sono disponibili tre opzioni:

            - Off: trasmette tutto il traffico DNS senza crittografia.

            - On (automatic template): invia tutto il traffico DNS con crittografia.

            - On (manual template): consente di specificare un template preciso. È richiesto solo se il servizio DNS non funziona automaticamente o dispone di un template che funziona come previsto.

        - Disattiva l’interruttore "Fallback to plaintext" se abiliti DNS over HTTPS.

            **Suggerimento**: se abiliti questa funzione, il sistema cifra il traffico DNS, ma consente comunque di inviare query senza crittografia.

    5. Fai clic su **Save** per applicare le impostazioni.

        Una volta completati i passaggi, la configurazione di rete statica verrà applicata al computer. Puoi testare le nuove impostazioni aprendo il browser e caricando un sito web.

=== "macOS"

    Ecco come impostare un indirizzo IP statico in macOS.

    Dal menu Apple, seleziona **System Preferences**.

    Seleziona **Network** per visualizzare la pagina seguente. Dalla barra laterale, seleziona un’interfaccia di rete attiva, ad esempio **Wi-Fi**.

    ![Mac_network_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Annota l’indirizzo IP attualmente assegnato al Mac. Dovrai scegliere un nuovo indirizzo IP all’interno dell’intervallo di indirizzi IP privati indicato.

    Fai clic su **Advanced** nell’angolo in basso a destra.

    Seleziona quindi **TCP/IP** per visualizzare la pagina seguente.

    ![Mac_Wi-Fi_settings](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: seleziona "Manually".

    - IPv4 Address: inserisci un indirizzo IP statico. Mantieni i primi tre ottetti dell’IP attuale e cambia l’ultimo ottetto con un valore inutilizzato. Ad esempio, nella rete `192.168.7.0/24`, scegli un indirizzo da `192.168.7.2` a `192.168.7.254` che non sia già in uso (evita `.1`, che corrisponde al router). Non usare `192.168.7.0` o `192.168.7.255`.

    - Subnet Mask: inserisci `255.255.255.0` (o la maschera di sottorete fornita dall’amministratore di rete).

    - Router: inserisci l’indirizzo IP LAN del router, ad esempio `192.168.7.1`.

    Fai clic su **OK**, quindi su **Apply**.

=== "iOS"

    I passaggi possono variare a seconda della versione di iOS. I passaggi seguenti si basano su iOS 26.2.2.

    1. Vai su **Settings** -> **WLAN**. Tocca l’icona blu delle informazioni (i) accanto alla rete Wi-Fi attualmente connessa.

        ![IP statico su iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Scorri fino a **IPv4 Address** e imposta **Configure IP** su **Manual**.

        ![IP statico su iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Specifica i valori **IP Address**, **Subnet Mask** e **Router IP** da utilizzare sul tuo iPhone/iPad, quindi tocca **Save** nell’angolo in alto a destra.

        ![IP statico su iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    I passaggi possono variare a seconda della versione di Android. I passaggi seguenti si basano su Android 11.

    1. Vai su **Settings** -> **Network & Internet** -> **Wi-Fi**. Tocca la rete attualmente connessa per aprire il menu delle impostazioni.

        ![list_available_networks](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Tocca l’icona della matita nell’angolo in alto a destra per accedere alle impostazioni di rete.

        ![pencil_icon](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Tocca **Advanced options**.

        ![advanced_options](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Tocca **IP Settings** e seleziona **Static**.

        ![DHCP_to_Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Inserisci l’**IP address**. Il campo **Gateway** dovrebbe essere compilato automaticamente in base all’indirizzo IP. In caso contrario, inserisci il gateway della rete. Il gateway è in genere l’IP LAN del router nella stessa sottorete.

        **Suggerimento**: quando usi indirizzi IP statici su reti domestiche e altre reti private, scegli un indirizzo host inutilizzato nella sottorete corrente. Gli intervalli standard di indirizzi IP privati sono:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Tocca **Save** e attendi che la rete si riconnetta.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} oppure [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
