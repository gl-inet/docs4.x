# Connettersi a Internet tramite una rete Wi-Fi esistente con Repeater

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Usare Repeater significa collegare il router a un'altra rete wireless esistente, ad esempio quando utilizzi il Wi-Fi gratuito in un hotel o in un cafe'.

Per impostazione predefinita funziona in modalita' WISP, Wireless Internet Service Provider, il che significa che il router creera' la propria subnet e agira' come firewall per proteggerti dalla rete pubblica.

## Passaggi di base

Accedi al pannello di amministrazione web del router, vai alla sezione **INTERNET** -> **Repeater** e fai clic su **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Scegli la rete Wi-Fi a cui vuoi connetterti dall'elenco delle reti disponibili.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

**Nota**: la pagina mostra i canali Wi-Fi supportati dal router. Assicurati che la rete Wi-Fi a cui ti stai collegando usi uno di questi canali, altrimenti potrebbe non essere visualizzata nell'elenco delle reti disponibili.

Inserisci la password Wi-Fi corretta e fai clic su **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Se l'SSID Wi-Fi a cui vuoi connetterti non e' presente nell'elenco Available Network, fai clic su **Join Other Network** nell'angolo superiore destro e inserisci manualmente l'SSID Wi-Fi e le altre informazioni richieste. Fai riferimento [qui](#join-other-network) per i passaggi dettagliati.

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Per connetterti a un hotspot pubblico, ad esempio quelli forniti da hotel, aeroporti o centri commerciali, fai riferimento a [For Public Hotspot](#for-public-hotspot).

Per altre impostazioni, fai riferimento a [Advanced Settings](#advanced-settings).

Dopo un po', se la password inserita e' corretta, la connessione avra' successo.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Per hotspot pubblici

Quando colleghi il router a un hotspot pubblico con captive portal, abilitare le seguenti funzioni puo' aiutare a migliorare il tasso di successo della connessione.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Questa funzione e' disponibile dalla v4.6.

    Se questa opzione e' abilitata, il router entrera' automaticamente in Login Mode for Public Hotspots quando e' collegato con successo a un hotspot ma non a Internet. **In questa modalita', alcuni servizi saranno sospesi mentre la modalita' DNS verra' impostata su automatica**, e questo potrebbe esporre la tua attivita' di rete al provider dell'hotspot, ad esempio hotel o centro commerciale.

    Anche se questa opzione non e' abilitata, il router ti chiedera' di entrare in questa modalita' quando rileva un captive portal nell'hotspot e non riesce ad accedere con successo.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Se abilitata, il router si mascherera' come il dispositivo client che usi per accedere al pannello di amministrazione, emulando l'indirizzo MAC di quel dispositivo.

- **MAC Mode**

    Puoi scegliere quale MAC il router usa per collegarsi all'hotspot pubblico.

    - **Factory**: usa l'indirizzo MAC originale assegnato in fabbrica al dispositivo.

    - **Clone**: clona l'indirizzo MAC di un dispositivo client per la connessione. Se il MAC desiderato non e' elencato, inserisci manualmente l'indirizzo che vuoi clonare.

        Nota: molti dispositivi moderni usano indirizzi MAC casuali, spesso chiamati Private Wi-Fi Address o random hardware address, quando si collegano alle reti Wi-Fi. Per questo motivo, l'indirizzo MAC mostrato qui potrebbe non corrispondere al vero MAC fisico del dispositivo.

    - **Random**: genera automaticamente un indirizzo MAC casuale per la connessione.

    Quando salvi la configurazione di rete, MAC Mode, inclusi eventuali MAC clonati o casuali, e' legato allo specifico SSID che salvi. Puoi modificare manualmente queste impostazioni per ciascun SSID in qualsiasi momento.

- **Auto Update MAC**: se questa opzione e' abilitata, il MAC puo' aggiornarsi automaticamente.

## Impostazioni avanzate

Quando ti unisci alla rete, sono disponibili alcune opzioni aggiuntive.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: abilita questa opzione per ricordare la rete Wi-Fi ripetuta attuale.

* **Lock BSSID**: quando e' abilitata, il router si connettera' solo allo specifico access point corrispondente al BSSID selezionato, anche quando altri AP condividono lo stesso SSID.

* **Manually Set Static IP**: quando e' abilitata, puoi configurare manualmente un indirizzo IPv4 fisso, netmask, gateway e server DNS per la connessione repeater del router, invece di ottenere automaticamente queste impostazioni.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL, Time To Live, imposta il tempo massimo di sopravvivenza dei pacchetti nella rete e viene compilato in base ai requisiti dell'operatore. Per impostazione predefinita, il router inoltra il TTL del dispositivo client in ingresso meno uno. Se hai bisogno di camuffarti, puoi impostare qui un valore fisso. TTL e' valido solo per IPv4.

* **HL**: in IPv6, il campo HL, Hop Limit, limita il numero di hop di trasmissione dei pacchetti nella rete, equivalente al TTL in IPv4.

* **MTU**: il valore predefinito e' 1500.

## Opzioni Repeater

Per visualizzare le opzioni Repeater, fai clic sull'icona a forma di ingranaggio nell'angolo superiore destro della sezione Repeater connessa.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

**Per firmware v4.8**, la pagina Repeater Options e' visualizzata come segue.

![v4.8 repeater options 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/4.8/repeater_options_1.png){class="glboxshadow"}

- **Allow Switching to Other Networks Mode**:

    - Modalita' No Switching: quando la modalita' No Switching e' abilitata, le altre reti salvate non verranno collegate automaticamente quando la rete Wi-Fi attuale viene disconnessa.

    - Modalita' Auto Switching: quando la modalita' Auto Switching e' abilitata, il router cerchera' di collegarsi ad altre reti salvate quando la rete Wi-Fi attuale viene disconnessa.

    - Auto Switching Without Network: quando la modalita' Auto-switching Without Network e' abilitata, il router non eseguira' automaticamente la scansione delle reti quando e' connesso con successo in modalita' diversa da repeater e tentera' di passare automaticamente ad altre reti salvate solo quando il router e' senza rete, evitando la perdita di pacchetti di comunicazione.

- **Band Selection**: puoi selezionare tra tre opzioni: Auto, 5 GHz e 2.4 GHz.

    Se selezioni manualmente una banda, il router non eseguira' la scansione e non si connettera' ad alcuna rete Wi-Fi che usa un'altra banda.

**Per firmware v4.7 e precedenti**, la pagina Repeater Options e' visualizzata come segue.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching To Other Saved Networks**. Se questa opzione e' abilitata, il router si connettera' automaticamente ad altre reti salvate quando non riesce a connettersi alla rete Wi-Fi attuale.

* **Band Selection**. Se selezioni manualmente una banda, il router non eseguira' la scansione e non si connettera' ad alcuna rete Wi-Fi su un'altra banda.

## Gestire le reti note

Per eliminare una rete nota, fai clic su **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Oppure fai clic su **Connect** nella sezione Repeater se non c'e' alcuna rete connessa.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Nella sezione **Known Networks**, fai clic sull'icona del cestino per eliminare una rete nota oppure sull'icona a forma di ingranaggio per configurare la rete.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Unirsi a un'altra rete

Se l'SSID non e' presente nell'elenco Available Networks oppure se l'SSID e' nascosto, puoi fare clic su **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Inserisci l'SSID, seleziona Security e inserisci la password, se richiesta.

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Per le impostazioni **Security**, sono disponibili due o tre opzioni, a seconda del modello.

* None, cioe' non e' richiesta alcuna password.
* WPA/WPA2/WPA3, comune e supportata da quasi tutte le reti Wi-Fi.
* WPA/WPA2/WPA3 Enterprise, che richiede Extensible Authentication Protocol, EAP, per l'autenticazione. Per collegarsi sono necessari nome utente e password validi, di solito in reti aziendali o universitarie.

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Per indicazioni dettagliate sulla ripetizione di reti EAP, fai clic [qui](../tutorials/eap.md){target="_blank"}.

## Riconnessione

Nei seguenti casi, il router tentera' automaticamente di riconnettersi al Wi-Fi di tanto in tanto. Se necessario, puoi disabilitare manualmente questa funzione. In caso di errori SSID/password, rimuovi la rete da Known Networks per risolvere.

1. SSID/password errati inseriti durante la configurazione Repeater.

2. Spostamento fuori portata del router a monte dopo la connessione iniziale.

3. Il router a monte cambia SSID/password oppure limita l'accesso dopo la connessione.

Il processo di riconnessione ha tre fasi distinte: fase di attesa, fase di scansione e fase di connessione.

1. Fase di attesa: nessun problema; il router attende le condizioni per la riconnessione.

2. Fase di scansione: puo' verificarsi perdita di pacchetti sulla banda di frequenza scansionata. I nuovi dispositivi potrebbero avere problemi di connessione. Per i modelli GL-AXT1800/GL-AX1800, il Guest Wi-Fi verra' temporaneamente disabilitato.

3. Fase di connessione: il Main Wi-Fi sulla banda di destinazione potrebbe interrompersi per alcuni secondi durante il ristabilimento.

**Nota**: in genere i problemi si verificano nelle fasi di scansione e connessione.

## Risoluzione dei problemi

Quando il router e' collegato a una rete Wi-Fi come repeater, se Internet non e' disponibile, verra' mostrato un messaggio giallo come illustrato di seguito.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Per risolvere il problema:

1. Controlla se il dispositivo a monte, cioe' la rete Wi-Fi a cui il router e' collegato, ha accesso a Internet.

2. Vai alla pagina [Multi-WAN](multi-wan.md) per controllare lo stato dell'interfaccia repeater.

## DFS

Quando ti colleghi a una rete Wi-Fi 5G a monte, il Wi-Fi del router seguira' la rete Wi-Fi a monte nel usare o non usare il canale DFS.

* Se la rete Wi-Fi a monte usa un canale DFS ed e' scansionabile, il Wi-Fi 5G del router usera' lo stesso canale.

* Il Wi-Fi 5G del router passera' a un canale non DFS se la rete Wi-Fi a monte non e' scansionabile oppure se la connessione non riesce.

??? "Modelli supportati"

    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Modelli non supportati"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Articoli correlati

- [Pagina Internet](internet.md)
- [Come impostare la priorita' di ciascun metodo di accesso a Internet?](multi-wan.md)
- [Come impostare il bilanciamento del carico quando vengono usati contemporaneamente piu' metodi di accesso a Internet?](multi-wan.md)
- [Come posso conoscere gli indirizzi MAC LAN e Wi-Fi?](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
