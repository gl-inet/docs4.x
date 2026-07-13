# Port Ethernet

**Note**: Cette page est disponible sous le nom **Port Management** depuis le firmware v4.7 et a été renommée **Ethernet Port** dans le firmware v4.8.3.

---

Dans le panneau d'administration web, accédez à **NETWORK** -> **Port Management** ou **Ethernet Port**.

Cette page vous permet de gérer le rôle des ports Ethernet (WAN/LAN) et d'afficher les détails des ports, comme l'adresse MAC et la vitesse négociée.

## WAN

Cette section affiche le rôle du port (WAN ou LAN), l'adresse MAC et la vitesse négociée. 

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

- **WAN/LAN** : mode de fonctionnement actuel du port WAN physique. Vous pouvez le définir en LAN si nécessaire.

- **MAC Mode** : utilise **Factory Mode** par défaut. Vous pouvez le basculer vers **Clone Mode** ou **Random Mode**.

- **Mac Address** : adresse MAC de l'interface WAN.

- **Negotiated Network Port Rate** : vitesse négociée du port réseau de l'interface WAN ; elle n'est affichée que lorsqu'une liaison valide est détectée.

## LAN

Cette section affiche la vitesse négociée du port LAN. Elle n'est affichée que lorsqu'une liaison valide est détectée.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Certains modèles permettent de basculer LAN 1 vers un port WAN pour les scénarios WAN Ethernet double. Cliquez sur [Dual-Ethernet WAN](#dual-ethernet-wan) pour plus de détails.

## Dual-Ethernet WAN

La fonctionnalité Dual-Ethernet WAN permet de transformer un port Ethernet LAN par défaut en port WAN secondaire pour un accès Internet Ethernet double. Elle offre une connectivité de secours fiable et prend en charge l'agrégation de bande passante lorsque celle-ci est compatible, pour les charges de travail gourmandes en bande passante. Elle permet également de se connecter simultanément à deux réseaux indépendants, par exemple un réseau professionnel et un réseau personnel, ce qui améliore la flexibilité sans matériel supplémentaire.

??? "Modèles pris en charge"
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Note**: Le GL-E5800 (Mudi 7) dispose d'un port Ethernet (LAN par défaut, commutable en WAN) et d'un **port USB-C compatible OTG**. Pour ajouter un second port Ethernet à Dual-Ethernet WAN, connectez au port USB-C un adaptateur USB-C vers Ethernet vendu séparément.

??? "Modèles non pris en charge"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Suivez les étapes ci-dessous pour basculer un port LAN vers un port WAN.

1. Sur la page **Port Management** ou **Ethernet Port**, cliquez sur l'onglet **LAN**, basculez le rôle du port sur WAN, puis cliquez sur **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. Dans la fenêtre contextuelle, cliquez sur **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. Le port sélectionné fonctionne désormais comme un port WAN. Vous pouvez ensuite configurer Multi-WAN [ici](multi-wan.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
