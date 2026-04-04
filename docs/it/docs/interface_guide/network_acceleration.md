# Network Acceleration

L'accelerazione di rete riduce il carico della CPU e velocizza l'inoltro dei pacchetti di traffico, ma puo' entrare in conflitto con alcune funzioni.

Quando Network Acceleration e' abilitata, le seguenti funzioni non funzioneranno correttamente: Client Speed and Traffic Statistics, Client Speed Limit.

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
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Modelli non supportati"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Configurazione

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Network Acceleration**.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Sono disponibili tre modalita'.

- **Auto**

    La modalita' Auto passera' automaticamente tra le due modalita' di accelerazione in base all'uso effettivo.

- **Hardware Acceleration**

    L'accelerazione hardware funziona con <u>Ethernet</u> e <u>Repeater</u>.

    L'accelerazione hardware delega attivita' di rete ad alta frequenza, ad esempio NAT, inoltro dei pacchetti e verifica del checksum, a hardware dedicato come NPU o chip HWNAT. Funziona in particolare su connessioni Ethernet, WAN/LAN cablate, e Repeater, offrendo ottime prestazioni in scenari con percorsi fissi e regole semplici, con throughput elevato, bassa latenza e carico minimo della CPU per la trasmissione dati a velocita' di linea.

- **Software Acceleration**

    L'accelerazione software funziona con <u>Cellular</u>.

    L'accelerazione software si basa sulla CPU generale del router, affiancata da kernel o driver ottimizzati, ad esempio SWNAT. Funziona su accessi Cellular, 4G/5G, tipicamente lo scenario principale in cui l'accelerazione hardware non e' disponibile, offrendo una forte compatibilita' e supporto per protocolli complessi. Pur essendo flessibile, puo' raggiungere colli di bottiglia della CPU con carichi ad alta larghezza di banda, specialmente quando sono in uso funzioni avanzate come DPI, QoS o port forwarding.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
