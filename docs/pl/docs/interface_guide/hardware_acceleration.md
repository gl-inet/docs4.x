# Akceleracja sprzętowa

**Uwaga**: Ten przewodnik dotyczy firmware v4.2 i wcześniejszych wersji. W przypadku nowszych wersji zapoznaj się z [Network Acceleration](network_acceleration.md).

---

Akceleracja sprzętowa (czasem nazywana *hardware NAT*, *flow offloading* lub po prostu *offloading*) zmniejsza obciążenie CPU, przenosząc przekazywanie pakietów z procesora do sprzętu SoC/NIC routera. Zwykle zwiększa to maksymalną przepustowość i obniża użycie CPU, ale wiąże się też z istotnymi ograniczeniami, szczególnie w przypadku funkcji opartych na stosie sieciowym Linuksa (netfilter/iptables/nftables) lub dyscyplinach kolejkowania jądra (qdisc) używanych przez SQM (Smart Queue Management).

Po włączeniu akceleracji sprzętowej następujące funkcje nie będą działać prawidłowo: **Client Speed and Traffic Statistics** oraz **Client Speed Limit**.

## Obsługiwane modele

??? "Obsługiwane modele"
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

??? "Nieobsługiwane modele"
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

## Szybka konfiguracja

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Hardware Acceleration**.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Włącz przełącznik i kliknij **Apply**.

---

## Hardware NAT a Software NAT

* Jeśli najbardziej zależy Ci na przepustowości (np. przy wielogigabitowym łączu szerokopasmowym) i nie potrzebujesz SQM na routerze ani kształtowania ruchu dla poszczególnych klientów → włącz Hardware NAT / Network Acceleration. Zapewnia to najwyższą przepustowość i najniższe użycie CPU.

* Jeśli zależy Ci na niskich opóźnieniach, stabilnym QoS, limitach dla poszczególnych klientów albo korzystasz z SQM (cake/fq_codel) → użyj Software NAT (wyłącz offload sprzętowy). SQM i QoS wymagają, aby pakiety przechodziły przez stos qdisc jądra — pakiety objęte offloadem omijają tę ścieżkę, więc nie podlegają kształtowaniu.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
