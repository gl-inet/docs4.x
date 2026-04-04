# Accelerazione hardware

**Nota**: questa guida si applica al firmware v4.2 e precedenti. Per le versioni piu' recenti, fai riferimento a [Network Acceleration](network_acceleration.md).

---

L'accelerazione hardware, a volte chiamata *hardware NAT, flow offloading o offloading*, riduce il carico della CPU spostando l'inoltro dei pacchetti dalla CPU all'hardware SoC/NIC del router. In genere questo aumenta il throughput massimo e riduce l'utilizzo della CPU, ma comporta compromessi importanti, soprattutto per le funzioni che si basano sullo stack di rete Linux, netfilter/iptables/nftables, oppure sulle discipline di coda del kernel, qdisc, usate da SQM (Smart Queue Management).

Quando l'accelerazione hardware e' abilitata, le seguenti funzioni non funzioneranno correttamente: Client Speed, Traffic Statistics e Client Speed Limit.

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

## Configurazione rapida

Sul lato sinistro del pannello di amministrazione web, vai su **NETWORK** -> **Hardware Acceleration**.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Attiva l'interruttore per abilitarla, quindi fai clic su Apply.

---

## Hardware NAT vs. Software NAT

* Se per te conta soprattutto il throughput, ad esempio con banda larga multi-gigabit, e non hai bisogno di SQM sul router o di limitazioni per client, abilita Hardware NAT / Network Acceleration. Questo garantisce il massimo throughput e il minor uso della CPU.

* Se per te contano bassa latenza, QoS coerente, limiti per client oppure fai affidamento su SQM (cake/fq_codel), usa Software NAT, quindi disabilita l'offload hardware. SQM e QoS richiedono che i pacchetti attraversino lo stack qdisc del kernel; i pacchetti offloaded saltano questo percorso e quindi non vengono modellati.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
