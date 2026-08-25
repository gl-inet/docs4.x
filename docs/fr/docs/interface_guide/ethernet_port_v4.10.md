# Port Ethernet (micrologiciel v4.10)

**Remarque** : le contenu de cette page est actuellement disponible sur Flint 4 (GL-BE14000) et sera déployé sur d’autres modèles avec le micrologiciel v4.10.

Si votre appareil utilise une autre version du micrologiciel, utilisez le sélecteur ci-dessous pour afficher le guide correspondant.

<div class="gl-link-select" data-label="Version du micrologiciel" data-placeholder="Micrologiciel v4.10" markdown="1">

- [Micrologiciel v4.9 et versions antérieures](ethernet_port.md)

</div>

---

Dans la partie gauche du panneau d’administration Web, accédez à **NETWORK** -> **Ethernet Port**.

Cette page affiche toutes les interfaces du routeur. Vous pouvez consulter l’état de connexion de chaque interface, gérer le rôle des ports Ethernet (WAN ou LAN) et afficher des informations telles que l’adresse MAC, le débit négocié et l’état actuel de la liaison. Vous pouvez également attribuer des interfaces physiques aux sous-réseaux que vous avez créés.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up** : lorsque l’icône du port est surlignée en bleu, la liaison physique est active.

- **Link Down** : lorsque l’icône du port est grise, la liaison physique est inactive.

- **Speed** : débit de transmission négocié du port Ethernet.

- **MAC** : adresse MAC du port.

- **VLAN Mode** : le mode de fonctionnement des ports LAN peut être défini sur Standard ou Multiple VLANs.

- **Native Network** : sous-réseau non balisé par défaut attribué au port LAN.

- **Allowed VLANs** : VLAN balisés autorisés à transiter par ce port en mode Multiple VLANs.

- **Settings** : cliquez pour accéder à la page de configuration de chaque port.

## WAN

Cette section affiche le mode du port (WAN ou LAN), l’adresse MAC et le débit négocié.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode** : mode de fonctionnement actuel du port WAN physique. Vous pouvez le définir sur LAN si nécessaire.

- **MAC Mode** : défini par défaut sur Factory Mode. Vous pouvez sélectionner Clone Mode ou Random Mode.

- **MAC Address** : adresse MAC de l’interface WAN.

- **Negotiated Network Port Rate** : débit de liaison négocié de l’interface WAN, affiché uniquement lorsqu’une liaison valide est détectée.

## LAN

Cette section affiche la configuration du port LAN. Vous pouvez définir Ethernet Mode sur **Standard** ou **Multiple VLANs** selon vos besoins.

### Mode Standard

Le mode Standard n’autorise qu’un seul VLAN (non balisé) et sert à connecter des appareils terminaux.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate** : débit de liaison négocié de l’interface LAN, affiché uniquement lorsqu’une liaison valide est détectée.

- **Ethernet Mode** : défini par défaut sur Standard Mode.

- **Access Network** : Access Network permet d’isoler les réseaux en attribuant les ports LAN à différents sous-réseaux.

Une fois la configuration terminée, vous pouvez revenir à la page Ethernet Port pour vérifier les paramètres.

### Mode Multiple VLANs

Le mode Multiple VLANs autorise plusieurs VLAN (balisés) sur un même port, généralement pour connecter des points d’accès ou d’autres commutateurs.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate** : débit de liaison négocié de l’interface LAN, affiché uniquement lorsqu’une liaison valide est détectée.

- **VLAN Mode** : pour passer en mode Multiple VLANs, cliquez sur l’onglet Multiple VLANs.

- **Untagged Traffic Handling** : configurez le traitement des paquets non balisés pour le port. Vous pouvez choisir de les supprimer directement ou de les transférer vers un autre sous-réseau en tant que réseau PVID natif.

- **Allowed Tagged Networks** : indique les VLAN autorisés à transiter par ce port en mode balisé. Vous pouvez sélectionner des réseaux VLAN dans la liste ; seul le trafic correspondant sera transféré.

Une fois la configuration terminée, vous pouvez revenir à la page Ethernet Port pour vérifier les paramètres.

Certains modèles permettent de convertir le port LAN 1 en port WAN pour utiliser deux connexions WAN Ethernet. Pour plus de détails, cliquez sur [Double WAN Ethernet](#dual-ethernet-wan).

## Dual-Ethernet WAN

La fonction Double WAN Ethernet permet de convertir un port Ethernet LAN par défaut en port WAN secondaire afin d’utiliser deux accès Internet Ethernet. Elle fournit une connexion de secours fiable et prend en charge l’agrégation de bande passante, lorsqu’elle est compatible, pour les usages exigeants. Elle permet également de se connecter simultanément à deux réseaux indépendants (par exemple professionnel et personnel), pour plus de flexibilité sans matériel supplémentaire.

??? "Modèles pris en charge"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
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

    **Remarque** : GL-E5800 (Mudi 7) possède un port Ethernet (LAN par défaut, convertible en WAN) et un **port USB-C compatible OTG**. Pour ajouter un deuxième port Ethernet pour la fonction Double WAN Ethernet, connectez au port USB-C un adaptateur USB-C vers Ethernet vendu séparément.

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

Pour convertir un port LAN en port WAN, procédez comme suit. Flint 3 (GL-BE9300) est utilisé dans cet exemple.

1. Sur la page **Ethernet Port**, cliquez sur les paramètres de **LAN1** pour accéder à la page Configuration. Définissez ensuite le rôle du port sur WAN, puis cliquez sur **Apply**.

    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Vous pouvez revenir à la page Ethernet Port pour vérifier que le rôle du port est désormais WAN.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. Le port sélectionné fonctionne désormais comme port WAN. Vous pouvez poursuivre la configuration de Multi-WAN [ici](multi-wan.md).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
