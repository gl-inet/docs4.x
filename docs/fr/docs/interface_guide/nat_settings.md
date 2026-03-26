# NAT Settings

Cette fonctionnalité est disponible depuis la v4.5.16.

Dans la partie gauche du panneau d'administration Web, allez dans **NETWORK** -> **NAT Settings**.

Cette page vous permet d'activer **Full Cone NAT** pour améliorer la stabilité des connexions pair à pair pour des applications comme les jeux ou le streaming, ainsi que **SIP ALG** pour corriger les problèmes de compatibilité avec les services téléphoniques basés sur la VoIP/SIP.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

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
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Note** : GL-SFT1200 (Opal) et GL-E750/E750V2 (Mudi) prennent en charge cette fonctionnalité avec le firmware v4.7 et les versions ultérieures.

??? "Modèles non pris en charge"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT

Full Cone NAT agit comme un « raccourci direct » pour les appareils tels que les consoles de jeu ou les téléphones lorsqu'ils se connectent à d'autres appareils en ligne (par exemple dans des jeux multijoueurs ou lors d'appels vidéo). 

En permettant aux appareils externes d'atteindre directement les appareils locaux via le routeur — au lieu de les masquer derrière plusieurs couches — il améliore la stabilité des connexions pair à pair (P2P), réduit la latence et résout les échecs de connexion dans les applications P2P. 

**Note** : l'activation de cette fonctionnalité peut réduire le niveau de sécurité par rapport à d'autres types de NAT, car elle expose les ports des appareils au réseau public.

## SIP ALG

SIP ALG (Application Layer Gateway) joue le rôle de « traducteur » du routeur pour les services de communication basés sur la VoIP/SIP, comme les téléphones de bureau professionnels ou les appels passés via des applications. 

Conçu pour résoudre les difficultés de traversée du NAT, il ajuste les données d'appel afin d'assurer une transmission fluide à travers plusieurs couches NAT — situation courante dans les réseaux comportant plusieurs routeurs (par exemple un routeur principal et un routeur GL.iNet) — ce qui limite les conflits et évite les interruptions d'appel. 

**Note** : un SIP ALG incompatible ou mal implémenté peut dégrader la qualité des appels et provoquer des problèmes tels qu'un son à sens unique, une sonnerie qui ne répond pas, des appels interrompus ou des appels redirigés directement vers la messagerie vocale.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
