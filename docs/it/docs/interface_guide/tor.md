# Tor

Tor, derivato da **The Onion Router**, e' un software gratuito e open-source per consentire comunicazioni anonime. Aiuta gli utenti a esplorare Internet con maggiore privacy. [Scopri di piu' su Tor](https://www.torproject.org/){target="_blank"}.

**Nota**: questa funzione e' attualmente in beta e puo' risultare problematica in alcuni paesi. Quando Tor e' abilitato, le seguenti funzioni non opereranno correttamente:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Modelli supportati

??? "Modelli supportati"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Nota**: i modelli contrassegnati con * non supportano Tor in modo nativo, ma gli utenti possono installare manualmente Tor tramite un plug-in. Fai clic [qui](#manual-install) per i dettagli.

??? "Modelli non supportati"
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **VPN** -> **Tor**.

Per il firmware ver.4.8.4 e successivi, vai su **APPLICATIONS** -> **Tor**.

Fai clic sull'interruttore per abilitarlo, abilita **Custom Exit Nodes** se necessario, quindi fai clic su **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

Iniziera' a connettersi. Se la tua rete soddisfa i requisiti, verra' mostrato lo stato di connessione riuscita.

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## Installazione manuale {#manual-install}

**Nota**: su alcuni modelli Tor puo' essere installato manualmente tramite plug-in, ma questo puo' aumentare il carico della CPU e rallentare la risposta del sistema.

Sul lato sinistro del pannello di amministrazione web, vai su **APPLICATIONS** -> **Plug-ins**.

Cerca **gl-sdk4-ui-torview** e installalo.

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
