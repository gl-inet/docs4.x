# Tor

Tor (abréviation de **The Onion Router**) est un logiciel libre et open source permettant les communications anonymes. Il aide les utilisateurs à naviguer sur Internet en préservant leur confidentialité. [En savoir plus sur Tor](https://www.torproject.org/){target="_blank"}.

**Remarque** : cette fonctionnalité est actuellement en version bêta et peut poser problème dans certains pays. Lorsque Tor est activé, les fonctions suivantes ne fonctionneront pas correctement :

  - VPN
  - DNS
  - IPv6
  - AdGuard Home.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Remarque** : les modèles marqués d'un * ne prennent pas en charge Tor nativement, mais les utilisateurs peuvent l'installer manuellement via un plug-in. Cliquez [ici](#installation-manuelle) pour plus de détails.

??? "Modèles non pris en charge"
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Configuration rapide

Dans la partie gauche du panneau d'administration web, accédez à **VPN** -> **Tor**.

Pour le firmware v4.8.4 et les versions ultérieures, accédez à **APPLICATIONS** -> **Tor**.

Activez l'interrupteur, activez **Custom Exit Nodes** si nécessaire, puis cliquez sur **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/enable_tor.png){class="glboxshadow"}

La connexion commencera. Si votre réseau remplit les conditions requises, l'état connecté s'affichera.

![tor connected](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/connected.png){class="glboxshadow" width="672"}

## Installation manuelle {#installation-manuelle}

**Remarque** : certains modèles permettent une installation manuelle de Tor via un plug-in, mais cela peut augmenter la charge du CPU et ralentir la réactivité du système.

Dans la partie gauche du panneau d'administration web, accédez à **APPLICATIONS** -> **Plug-ins**.

Recherchez **gl-sdk4-ui-torview** puis installez-le.

![torview](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/tutorials/tor/torpage.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
