# AstroWarp

**Nota**: questa guida presenta la nuova versione di AstroWarp, integrata nel pannello di amministrazione web GL.iNet.

Per la documentazione relativa ad AstroWarp legacy, fai riferimento [a questo link](https://docs.astrowarp.net/){target="_blank"}.

---

AstroWarp e' una funzione di rete avanzata integrata nei router GL.iNet. Consente l'accesso remoto senza interruzioni alla rete domestica senza registrazione ne' accesso. Utilizzando il protocollo AmneziaWG con offuscamento del traffico integrato, mantiene la connessione stabile e sicura, risultando ideale per un accesso remoto affidabile ovunque ti trovi.

Gli utenti possono configurare una rete AstroWarp direttamente dal pannello di amministrazione del router GL.iNet. Basta associare i router tramite un codice di accesso per collegare in modo sicuro il router da viaggio alla rete domestica in pochi secondi.

**Nota:**

1. Non e' consigliabile usare AstroWarp contemporaneamente a una delle seguenti funzioni, poiche' potrebbe causare conflitti di instradamento: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Quando AstroWarp e' abilitato, non e' possibile usare Network Mode.

## Modelli supportati

??? "Modelli supportati"

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Nota**: i modelli contrassegnati con ※ supportano AstroWarp integrato nel firmware Beta.

??? "Modelli non supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Configurazione rapida

Nell'esempio seguente, useremo **Flint 3 (GL-BE9300)** e **Slate 7 (GL-BE3600)** per configurare una rete AstroWarp.

Flint 3 funzionera' come router di casa, mentre Slate 7 funzionera' come router da viaggio che instrada il traffico di rete verso Flint 3 per l'accesso a Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Nota**: ogni router GL.iNet include **10 GB di dati gratuiti al mese** per la rete AstroWarp. I dispositivi in una rete AstroWarp useranno i dati del router domestico per accedere a Internet. Se necessario, puoi effettuare l'upgrade al piano AstroWarp+ per avere dati illimitati.

1. Configura Flint 3 per Internet.

    Accedi al pannello di amministrazione web di Flint 3 e vai alla pagina **INTERNET**. Connettilo a Internet utilizzando uno dei metodi di connessione supportati: Ethernet, Repeater, Tethering e Cellular.

    Come mostrato di seguito, il router domestico Flint 3 e' collegato al modem dell'ISP (Hong Kong Broadband Network Ltd) tramite un cavo Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Genera il codice di accesso.

    Nel pannello di amministrazione web di Flint 3, vai su **CLOUD SERVICES** -> **AstroWarp**. Fai clic su **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Verra' generato un **Access Code**. Copia questo codice per usarlo in seguito.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configura Slate 7 per Internet.

    Accedi al pannello di amministrazione web di Slate 7 e vai alla pagina **INTERNET**. Connettilo a Internet utilizzando uno dei metodi di connessione supportati: Ethernet, Repeater, Tethering e Cellular.

    Come mostrato di seguito, il router da viaggio Slate 7 e' collegato all'hotspot personale di un iPhone 15 Pro (situato a Shenzhen, sulla rete China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Inserisci il codice di accesso.

    Nel pannello di amministrazione web di Slate 7, vai su **CLOUD SERVICES** -> **AstroWarp**. Fai clic su **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Inserisci l'Access Code ottenuto al passaggio 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Attendi il completamento della verifica.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    A questo punto si connettera' correttamente al router domestico Flint 3. Ora puoi navigare in Internet in modo sicuro tramite la rete di casa.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    Anche nel pannello di amministrazione web di Flint 3 verra' mostrato lo stato della connessione, come illustrato di seguito.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Test della connettivita'

1. Collega un laptop o uno smartphone al Wi-Fi del router da viaggio Slate 7.

2. Apri un browser e visita [ipcheck.ing](https://ipcheck.ing/){target="_blank"} o un altro sito per verificare l'indirizzo IP.

    Verra' mostrato l'indirizzo IP pubblico di Flint 3, a indicare che Slate 7 sta accedendo a Internet tramite il router domestico Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Disconnetti la connessione AstroWarp su Slate 7, quindi aggiorna la pagina web per inviare di nuovo la richiesta di verifica IP.

    Verra' mostrato l'indirizzo IP pubblico di Slate 7, a indicare che Slate 7 sta accedendo a Internet tramite la propria rete locale.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Upgrade del piano

Ogni router GL.iNet include **10 GB di dati gratuiti al mese** per la rete AstroWarp. I dispositivi in una rete AstroWarp useranno i dati del router domestico per accedere a Internet.

Se necessario, puoi effettuare l'upgrade al piano **AstroWarp+** per avere dati illimitati.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
