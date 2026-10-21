# Hardware Acceleration {#hardware-acceleration}

**Opmerking**: deze handleiding geldt voor firmware v4.2 en ouder. Raadpleeg voor nieuwere versies [Network Acceleration](network_acceleration.md).

---

Hardwareversnelling, soms *hardware NAT*, *flow offloading* of *offloading* genoemd, verlaagt de CPU-belasting door het doorsturen van pakketten van de CPU naar de SoC/NIC-hardware van de router te verplaatsen. Dit verhoogt doorgaans de maximale doorvoer en verlaagt het CPU-gebruik, maar heeft belangrijke nadelen, vooral voor functies die afhankelijk zijn van de Linux-netwerkstack (netfilter/iptables/nftables) of de wachtrijdisciplines van de kernel (qdisc) die door SQM (Smart Queue Management) worden gebruikt.

Wanneer hardwareversnelling is ingeschakeld, werken de volgende functies niet goed: Client Speed and Traffic Statistics en Client Speed Limit.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Niet-ondersteunde modellen"
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

## Snelle installatie {#quick-setup}

Ga links in het webbeheerpaneel naar **NETWORK** -> **Hardware Acceleration**.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/interface_guide/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Zet de schakelaar om om de functie in te schakelen en klik op Apply.

---

## Hardware NAT versus Software NAT {#hardware-nat-vs-software-nat}

* Als doorvoer het belangrijkst is, bijvoorbeeld bij multi‑gigabitbreedband, en je geen SQM op de router of regeling per client nodig hebt, schakel je Hardware NAT/Network Acceleration in. Dit levert de hoogste doorvoer en het laagste CPU-gebruik.

* Als lage latentie, consistente QoS of limieten per client belangrijk zijn, of als je SQM (cake/fq_codel) gebruikt, gebruik je Software NAT en schakel je hardware-offload uit. Voor SQM en QoS moeten pakketten de qdisc-stack van de kernel doorlopen. Offloaded pakketten omzeilen dit pad en worden daarom niet geregeld.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
