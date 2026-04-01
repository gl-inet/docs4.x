# Accélération matérielle

**Note**: Ce guide s'applique au firmware v4.2 et aux versions antérieures. Pour les versions plus récentes, veuillez consulter [Network Acceleration](network_acceleration.md). 

---

L'accélération matérielle (parfois appelée *hardware NAT*, *flow offloading* ou *offloading*) réduit la charge du processeur en déplaçant le transfert des paquets du CPU vers le matériel SoC/NIC du routeur. Cela augmente généralement le débit maximal et réduit l'utilisation du CPU, mais cela implique des compromis importants, en particulier pour les fonctionnalités qui reposent sur la pile réseau Linux (netfilter/iptables/nftables) ou sur les disciplines de mise en file d'attente du noyau (qdisc) utilisées par SQM (Smart Queue Management).

Lorsque l'accélération matérielle est activée, les fonctions suivantes ne fonctionnent pas correctement : les statistiques de vitesse et de trafic des clients, ainsi que la limitation de vitesse par client.

## Modèles pris en charge

??? "Modèles pris en charge"
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

??? "Modèles non pris en charge"
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

## Configuration rapide

Dans le panneau d'administration web, accédez à **NETWORK** -> **Hardware Acceleration**.

![Hardware Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/hardware_acceleration/hardware_acceleration.png){class="glboxshadow"}

Activez l'interrupteur, puis cliquez sur **Apply**.

---

## NAT matériel ou NAT logiciel

* Si votre priorité est le débit (par exemple une connexion Internet multi-gigabit) et que vous n'avez pas besoin de SQM sur le routeur ni de limitation par client, activez **Hardware NAT / Network Acceleration**. C'est ce qui offre le débit le plus élevé et la plus faible utilisation du CPU.

* Si votre priorité est une faible latence, une QoS stable, des limites par client, ou si vous utilisez SQM (`cake`/`fq_codel`), utilisez **Software NAT** (désactivez l'offload matériel). SQM et la QoS exigent que les paquets traversent la pile qdisc du noyau ; les paquets déchargés contournent ce chemin et ne sont donc pas régulés.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
