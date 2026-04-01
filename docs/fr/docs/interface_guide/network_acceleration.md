# Network Acceleration

L'accélération réseau réduit la charge du CPU et accélère le transfert des paquets de trafic, mais peut entrer en conflit avec certaines fonctionnalités.

Lorsque l'accélération réseau est activée, les fonctions suivantes ne fonctionneront pas correctement : Client Speed and Traffic Statistics, Client Speed Limit.

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

## Configuration

Dans la partie gauche du panneau d'administration Web, allez dans **NETWORK** -> **Network Acceleration**.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/tutorials/network_acceleration/network_acceleration.png){class="glboxshadow"}

Trois modes sont disponibles.

- **Auto**
    
    Le mode Auto bascule automatiquement entre les deux modes d'accélération selon l'utilisation réelle.

- **Hardware Acceleration**

    L'accélération matérielle fonctionne avec <u>Ethernet</u> et <u>Repeater</u>. 
    
    L'accélération matérielle déporte les tâches réseau à haute fréquence (par exemple NAT, transfert de paquets, vérification de somme de contrôle) vers du matériel dédié, comme des NPU ou des puces HWNAT. Elle fonctionne spécifiquement sur les connexions Ethernet (WAN/LAN filaire) et Repeater, où elle excelle dans les scénarios à chemins fixes et règles simples pour offrir un débit élevé, une faible latence et une charge CPU minimale pour une transmission des données à la vitesse du lien.

- **Software Acceleration**

    L'accélération logicielle fonctionne avec <u>Cellular</u>. 
    
    L'accélération logicielle s'appuie sur le CPU général du routeur, associé à des noyaux ou pilotes optimisés (par exemple SWNAT). Elle fonctionne pour l'accès Cellular (4G/5G), généralement dans le principal scénario où l'accélération matérielle n'est pas disponible, tout en offrant une bonne compatibilité et la prise en charge de protocoles complexes. Bien qu'elle soit flexible, elle peut atteindre les limites du CPU sous de fortes charges en bande passante, en particulier lorsque des fonctions avancées comme DPI, QoS ou la redirection de ports sont utilisées.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

