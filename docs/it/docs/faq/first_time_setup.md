# Configurazione iniziale

La configurazione iniziale del router GL.iNet è molto simile per la maggior parte dei modelli. La maggior parte dei modelli dispone di un modulo Wi-Fi, mentre alcuni no.

Per questo motivo, la guida seguente è suddivisa in due casi in base alla presenza del modulo Wi-Fi.

* [Per i modelli dotati di Wi-Fi](#per-i-modelli-dotati-di-wi-fi)
* [Per i modelli senza Wi-Fi](#per-i-modelli-senza-wi-fi)

## Per i modelli dotati di Wi-Fi

Qui viene usato come esempio il GL-AXT1800 (Slate AX).

Prepara i seguenti elementi inclusi nella confezione.

- GL-AXT1800
- Un alimentatore
- Un cavo Ethernet

Guarda questa videoguida oppure segui i passaggi seguenti.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Questo video usa un router GL.iNet diverso per dimostrare la configurazione, poiché i passaggi sono gli stessi per la maggior parte dei modelli.)</small>

1. Accensione

    Se vuoi usare una scheda TF, inseriscila prima di accendere il router. L'hot-swap delle schede TF non è supportato.

    Collega un'estremità dell'alimentatore al router e l'altra a una presa di corrente. Il router si accenderà automaticamente.

2. Collegamento al router

    Puoi collegarti al router tramite cavo Ethernet oppure tramite Wi-Fi.

    * Collegamento via cavo

        Collega il computer alla porta LAN del router tramite un cavo Ethernet.

    * Collegamento via Wi-Fi

        L'SSID Wi-Fi è stampato sull'etichetta inferiore del router nei seguenti formati:

        **GL-AXT1800-XXX** oppure **GL-AXT1800-XXX-5G**

        La Wi-Fi Key predefinita si trova sotto l'SSID.

        Cerca l'SSID del router sul computer, telefono o tablet, quindi inserisci la Wi-Fi Key. Per alcuni modelli, se la password Wi-Fi non compare sull'etichetta, prova con "**goodlife**".

        **Suggerimento:** il codice QR sull'etichetta inferiore contiene le informazioni Wi-Fi predefinite. Puoi collegarti rapidamente scansionandolo con il lettore di codici QR del telefono.

        **Nota:** dopo esserti collegato al Wi-Fi, potresti non avere accesso immediato a Internet. Segui prima il passaggio successivo per configurare la rete.

3. Accedi al pannello di amministrazione web

    Apri un browser web (consigliamo Chrome, Edge o Safari) e visita [http://192.168.8.1](http://192.168.8.1). Verrai indirizzato alla configurazione iniziale del pannello di amministrazione web.

    Se non riesci ad accedere al pannello di amministrazione web, controlla [qui](cannot_access_web_admin_panel.md).

    Scegli una lingua e fai clic su **Next** per continuare.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Imposta la password amministratore. Ti consigliamo di usare una password robusta. Fai clic su **Apply** per continuare.

    **Nota**: durante l'inizializzazione il Wi-Fi potrebbe spegnersi. Assicurati di ricollegarti al router.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Al termine della configurazione iniziale, entrerai nel pannello di amministrazione web del router.

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Connettiti a Internet

    * [Connettiti a Internet tramite un cavo Ethernet](../interface_guide/internet_ethernet.md)
    * [Connettiti a Internet tramite una rete Wi-Fi esistente](../interface_guide/internet_repeater.md)
    * [Connettiti a Internet tramite USB Tethering](../interface_guide/internet_tethering.md)
    * [Connettiti a Internet tramite modem USB](../interface_guide/internet_cellular.md)

## Per i modelli senza Wi-Fi

Qui viene usato come esempio il GL-MT2500A (Brume 2).

1. Accensione

    Collega un'estremità dell'alimentatore al router e l'altra a una presa di corrente. Il router si accenderà automaticamente.

2. Collegamento al router

    Possiamo collegarci al router tramite cavo Ethernet oppure tramite il Wi-Fi di un altro router.

    * Collegamento diretto tramite cavo Ethernet

        Collega il computer alla porta LAN del router usando un cavo Ethernet. È il metodo di configurazione consigliato perché semplice e diretto.

    * Collegamento tramite il Wi-Fi di un altro router

        Poiché il GL-MT2500A non ha un modulo Wi-Fi integrato, possiamo usare un altro router con funzionalità Wi-Fi per inizializzare il GL-MT2500A.

        * Metodo 1: imposta il secondo router in modalità AP (Access Point), quindi collega la porta LAN del GL-MT2500A alla porta WAN del secondo router.

        * Metodo 2: lascia il secondo router nella modalità router predefinita, ma con un indirizzo IP del router diverso e non in conflitto con 192.168.8.1/24, ad esempio 192.168.10.1. Poi collega la porta LAN del GL-MT2500A alla porta WAN del secondo router.

        Usa il computer o lo smartphone per collegarti al Wi-Fi del secondo router.

        !!! Note

            Il secondo router citato qui è un normale router, come GL.iNet GL-AXT1800, TP-LINK o Netgear. Modem, terminali di rete ottica o dispositivi forniti dagli ISP potrebbero non funzionare in questo scenario.

3. Accedi al pannello di amministrazione web

    Apri un browser web (consigliamo Chrome, Edge, Safari) e visita [http://192.168.8.1](http://192.168.8.1). Verrai indirizzato alla configurazione iniziale del pannello di amministrazione web. Se non riesci ad accedere al pannello di amministrazione web, controlla [qui](cannot_access_web_admin_panel.md).

    Scegli una lingua e fai clic su **Next** per continuare.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Imposta la password amministratore. Ti consigliamo di usare una password robusta. Fai clic su **Submit** per continuare.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Al termine della configurazione iniziale, entrerai nel pannello di amministrazione web del router.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Connettiti a Internet

    * [Connettiti a Internet tramite un cavo Ethernet](../interface_guide/internet_ethernet.md)
    * [Connettiti a Internet tramite USB Tethering](../interface_guide/internet_tethering.md)
    * [Connettiti a Internet tramite modem USB](../interface_guide/internet_cellular.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
