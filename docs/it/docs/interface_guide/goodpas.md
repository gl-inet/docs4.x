# GoodPAS

**Nota**: questa funzione è stata introdotta nel firmware v4.10, quando AstroWarp è stato rinominato GoodPAS. Se il dispositivo usa una versione firmware precedente, consulta [AstroWarp](./astrowarp.md).

---

Nel menu a sinistra del pannello di amministrazione web, vai su **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS è una soluzione avanzata di accesso remoto integrata nell'SDK dei router GL.iNet. Usa il protocollo AmneziaWG con offuscamento del traffico integrato, offrendo connessioni stabili e sicure per un accesso remoto affidabile in qualsiasi momento e luogo.

Questa funzione consente di accedere senza interruzioni alla rete domestica da remoto. Puoi configurare e associare direttamente i dispositivi tramite un codice di accesso dinamico nel pannello di amministrazione web, stabilendo in pochi secondi una connessione sicura tra il router da viaggio e la rete domestica, senza registrazione né accesso a un account.

**Nota**:

1. Non è consigliabile usare GoodPAS contemporaneamente a una delle seguenti funzioni, poiché potrebbero verificarsi conflitti di instradamento: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.

2. Quando GoodPAS è abilitato, Network Mode non può essere usato.

## Configurazione rapida

Nell'esempio seguente useremo **Flint 3 (GL-BE9300)** e **Mango 2 (GL-MG1300)** per configurare una rete GoodPAS.

Flint 3 fungerà da router domestico, mentre Mango 2 fungerà da router da viaggio e instraderà il traffico di rete verso Flint 3 per l'accesso a Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configura la connessione Internet di Flint 3.

    Accedi al pannello di amministrazione web di Flint 3 e vai alla pagina INTERNET. Connettilo a Internet usando uno dei metodi supportati: Ethernet, Repeater, Tethering o Cellular.

    Come mostrato di seguito, il router domestico Flint 3 è collegato tramite cavo Ethernet al modem dell'ISP (Hong Kong Broadband Network Ltd).

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Genera il codice di accesso.

    Nel pannello di amministrazione web di Flint 3, vai su **CLOUD SERVICES** -> **GoodPAS**. Fai clic su **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Verrà generato un Access Code. Copia il codice per usarlo in seguito.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configura la connessione Internet di Mango 2.

    Accedi al pannello di amministrazione web di Mango 2 e vai alla pagina INTERNET. Connettilo a Internet usando uno dei metodi supportati: Ethernet, Repeater, Tethering o Cellular.

    Come mostrato di seguito, il router da viaggio Mango 2 è collegato all'hotspot personale di un iPhone 17 (a Shenzhen, sulla rete China Unicom della provincia del Guangdong).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Inserisci il codice di accesso.

    Nel pannello di amministrazione web di Mango 2, vai su **CLOUD SERVICES** -> **GoodPAS**. Fai clic su **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Inserisci l'Access Code ottenuto al passaggio 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Attendi il completamento della verifica.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    La connessione al router domestico Flint 3 verrà stabilita. Ora puoi navigare in Internet in modo sicuro tramite la rete domestica.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Anche il pannello di amministrazione web di Flint 3 mostra lo stato della connessione, come illustrato di seguito.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Test della connettività

1. Collega un laptop o uno smartphone alla rete Wi-Fi del router da viaggio Mango 2.

2. Apri un browser e visita [ipcheck.ing](https://ipcheck.ing/){target="_blank"} o un altro sito per la verifica dell'indirizzo IP.

    Verrà mostrato l'indirizzo IP pubblico di Flint 3, a indicare che Mango 2 accede a Internet tramite il router domestico Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Disconnetti GoodPAS su Mango 2, quindi aggiorna la pagina per inviare nuovamente la richiesta di verifica IP.

    Verrà mostrato l'indirizzo IP pubblico di Mango 2, a indicare che Mango 2 accede a Internet tramite la propria rete locale.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **D: Qual è il formato del codice di accesso dinamico e per quanto tempo è valido?**

    R: È un codice di 8 caratteri composto da numeri e lettere maiuscole, valido per 10 minuti.

2. **D: Cosa succede al router da viaggio se termino la connessione sul router domestico?**

    R: Il router da viaggio si disconnette e rimane in attesa senza accesso alla rete. Quando il router domestico ripristina la connessione, il router da viaggio può riconnettersi automaticamente senza inserire nuovamente il codice di accesso.

3. **D: In quali casi il router da viaggio entra in stato di attesa?**

    R: Il router da viaggio entra in stato di attesa quando il router domestico si trova in una delle seguenti condizioni:

    - termina la connessione GoodPAS;
    - perde l'accesso a Internet.

4. **D: A cosa serve il pulsante Reset nell'angolo superiore destro?**

    R: Cancella tutti i dispositivi autorizzati e riporta alla pagina di selezione del ruolo del router, consentendo di sceglierlo nuovamente.

5. **D: Cosa succede al router da viaggio se ripristino GoodPAS sul router domestico?**

    R: Dopo il ripristino del router domestico, i dispositivi collegati da remoto vengono disconnessi dalla rete GoodPAS e tornano a usare la rete locale per l'accesso a Internet.

---

Hai ancora domande? Visita il nostro [Forum della community](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
