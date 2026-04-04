# NAT Settings

Questa funzione e' disponibile dalla v4.5.16.

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **NAT Settings**.

Questa pagina consente di abilitare **Full Cone NAT** per migliorare la stabilita' delle connessioni peer-to-peer per app come gaming o streaming, e **SIP ALG** per risolvere problemi di compatibilita' con servizi telefonici VoIP/SIP.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Modelli supportati

??? "Modelli supportati"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Nota**: GL-SFT1200 (Opal) e GL-E750/E750V2 (Mudi) supportano questa funzione con firmware v4.7 e successivi.

??? "Modelli non supportati"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT

Full Cone NAT agisce come una "scorciatoia diretta" per dispositivi come console di gioco o telefoni quando si collegano ad altri dispositivi online, ad esempio in giochi multiplayer o videochiamate.

Consentendo ai dispositivi esterni di raggiungere direttamente i dispositivi locali attraverso il router, invece di nasconderli dietro piu' livelli, migliora la stabilita' delle connessioni peer-to-peer (P2P), riduce la latenza e risolve i fallimenti di connessione nelle applicazioni P2P.

**Nota**: abilitare questa funzione puo' ridurre la sicurezza rispetto ad altri tipi di NAT, poiche' espone le porte del dispositivo alla rete pubblica.

## SIP ALG

SIP ALG (Application Layer Gateway) funziona come un "traduttore" del router per i servizi di comunicazione basati su VoIP/SIP, ad esempio telefoni da ufficio o chiamate tramite app.

Progettato per affrontare le difficolta' di attraversamento del NAT, regola i dati delle chiamate per garantire una trasmissione senza interruzioni attraverso piu' livelli NAT, situazione comune nelle reti con piu' router, ad esempio un router principale e un router GL.iNet, mitigando cosi' i conflitti e prevenendo interruzioni nelle chiamate.

**Nota**: un'implementazione SIP ALG incompatibile o poco curata puo' peggiorare la qualita' delle chiamate, causando problemi tra cui audio unidirezionale, squillo senza risposta, chiamate interrotte o chiamate inoltrate direttamente alla segreteria.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
