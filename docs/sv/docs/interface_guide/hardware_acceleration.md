# Hardware Acceleration {#hardware-acceleration}

**Obs!** Den här guiden gäller firmware v4.2 och tidigare. För senare versioner, se [Network Acceleration](network_acceleration.md).

---

Maskinvaruacceleration (ibland kallad *hardware NAT, flow offloading eller offloading*) minskar processorbelastningen genom att flytta paketvidarebefordran från processorn till routerns SoC/NIC-maskinvara. Det ökar vanligtvis maximal kapacitet och minskar processoranvändningen, men medför viktiga kompromisser, särskilt för funktioner som använder Linux nätverksstack (netfilter/iptables/nftables) eller kärnans ködiscipliner (qdisc) som används av SQM (Smart Queue Management).

När maskinvaruacceleration är aktiverad fungerar följande funktioner inte korrekt: Client Speed and Traffic Statistics samt Client Speed Limit.

## Supported Models {#supported-models}

??? "Supported Models"
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

??? "Unsupported Models"
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

## Quick Setup {#quick-setup}

Öppna **NETWORK** -> **Hardware Acceleration** på vänster sida i webbadministrationspanelen.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/interface_guide/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Aktivera med reglaget och klicka på Apply.

---

## Hardware NAT vs. Software NAT {#hardware-nat-vs-software-nat}

* Om kapacitet är viktigast (t.ex. multigigabitbredband) och du inte behöver SQM på routern eller trafikformning per klient aktiverar du Hardware NAT/Network Acceleration. Det ger högsta kapacitet och lägsta processoranvändning.

* Om låg latens, konsekvent QoS eller gränser per klient är viktigt, eller om du använder SQM (cake/fq_codel), använder du Software NAT och inaktiverar maskinvaruavlastning. SQM och QoS kräver att paket passerar kärnans qdisc-stack. Avlastade paket kringgår denna väg och trafikformas därför inte.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
