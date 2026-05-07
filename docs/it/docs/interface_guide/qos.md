# QoS (Quality of Service)

QoS, Quality of Service, ottimizza l'allocazione della larghezza di banda dando priorità alle attività critiche, ad esempio videochiamate o gaming, durante la congestione della rete, riducendo la latenza e migliorando le prestazioni complessive.

**Nota**:

1. Questa funzione influisce solo sul traffico che attraversa il router quando opera come gateway, incluso il traffico dei client locali e quello del client VPN. Non si applica al traffico in ingresso quando il router agisce come server VPN.
2. QoS non ha effetto quando il router è in modalità Drop-in Gateway.
3. QoS e SQM non possono essere abilitati contemporaneamente.
4. QoS non può funzionare con Network Acceleration. L'abilitazione di QoS disattiva automaticamente Network Acceleration per garantire prestazioni stabili.

## Modelli supportati

!!! note "Modelli supportati"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Nota: i modelli contrassegnati con ※ supportano QoS a partire dal firmware v4.9.

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **FLOW CONTROL** -> **QoS**.

Attiva l'interruttore per abilitare QoS; la pagina verrà mostrata come segue.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow"}

Imposta la velocità massima di upload e download, intervallo di input 1 - 10000, per la pianificazione del traffico. Per ottenere i migliori risultati, falle corrispondere alla tua effettiva larghezza di banda Internet.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow"}

**Nota**: i valori inseriti nel campo di input sono espressi in **Mbps** (megabit al secondo). L'equivalente in **MB/s** (megabyte al secondo) viene mostrato come riferimento.

Imposta quindi le priorità per le diverse applicazioni. Il router allocherà la larghezza di banda di conseguenza.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow"}

## Personalizzare la priorità delle app

Per personalizzare la priorità delle applicazioni, seleziona **Customize** e fai clic su **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow"}

Nella finestra pop-up, tutte le categorie sono impostate su Medium Priority per impostazione predefinita.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow"}

Trascina le categorie per regolarne la priorità secondo necessità, quindi fai clic su **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"}

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
