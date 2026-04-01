# Dual-Ethernet WAN

La fonctionnalité Dual-Ethernet WAN permet de basculer le port LAN1 par défaut en second port WAN afin d'obtenir un accès Ethernet double. Elle offre une connectivité de secours fiable et prend en charge l'agrégation de bande passante lorsque celle-ci est compatible, pour les usages exigeants. Elle permet également de se connecter simultanément à deux réseaux distincts (par exemple un réseau professionnel et un réseau personnel), ce qui améliore la flexibilité sans matériel supplémentaire.

## Modèles pris en charge

??? "Modèles pris en charge"
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Note**: Le GL-E5800 (Mudi 7) dispose d'un port Ethernet (LAN par défaut, commutable en WAN) et d'un **port USB-C compatible OTG**. Pour ajouter un second port Ethernet à Dual-Ethernet WAN, connectez un adaptateur USB‑C vers Ethernet vendu séparément au port USB-C.

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

## Configuration

1. Connectez-vous au panneau d'administration web du routeur.

2. Accédez à **NETWORK** -> **Port Management** -> onglet **LAN**, changez la propriété du port en WAN, puis cliquez sur **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_1.png){class="glboxshadow"}

3. Dans la fenêtre contextuelle, cliquez sur **Apply**.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/tutorials/dual-ethernet_wan/dual_ethernet_2.png){class="glboxshadow"}

4. Une fois Dual-Ethernet WAN activé, vous pouvez configurer les fonctions multi-WAN [ici](../interface_guide/multi-wan.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
