# QoS (Quality of Service)

**Remarque** : cette fonction a été introduite dans le firmware v4.9.

Certains modèles, notamment Mango 2 (GL-MG1300), ne prennent pas en charge die QoS en raison d’une mémoire insuffisante, même avec le firmware v4.9 ou une version ultérieure. Consultez les [modèles pris en charge](#supported-models) pour plus de détails.

---

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **QoS**.

La QoS (Quality of Service) optimise l’allocation de la bande passante en donnant la priorité aux activités critiques (par ex. appels vidéo, jeux en ligne) lors de la congestion du réseau, ce qui réduit la latence et améliore les performances globales du réseau.

**Remarque** :

1. Cette fonctionnalité affecte uniquement le trafic qui traverse le routeur lorsqu’il fonctionne comme passerelle, y compris le trafic des clients locaux et le trafic du client VPN. Elle ne s’applique pas au trafic entrant lorsque le routeur agit comme serveur VPN.
2. La QoS ne prend pas effet lorsque le routeur est en mode Drop-in Gateway.
3. La QoS et le SQM ne peuvent pas être activés simultanément.
4. La QoS ne peut pas fonctionner avec Network Acceleration. L’activation de la QoS désactivera automatiquement Network Acceleration afin de garantir des performances stables.

## Modèles pris en charge {#supported-models}

??? "Modèles pris en charge"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Modèles non pris en charge"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)


## Pour le firmware v4.11 et les versions ultérieures

Activez l’interrupteur pour activer la QoS, puis effectuez la configuration en suivant les étapes ci-dessous.

![qos v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Saisissez manuellement les débits montant et descendant du WAN (plage de saisie : 1 - 10000), ou cliquez sur **Run Speedtest** pour les mesurer et remplir automatiquement les champs. Une connexion Internet active est nécessaire pour exécuter le test de débit.

    ![wan bandwidth](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Remarque** : les valeurs saisies sont exprimées en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) est affiché à titre indicatif.

2. **Scheduling Policy**

    Vous pouvez sélectionner un mode de stratégie. Les règles avancées remplacent la stratégie de base pour le trafic correspondant.

    - **Device Priority**

        Dans ce mode, les clients locaux sélectionnés bénéficient d’une priorité réseau plus élevée lorsque la connexion WAN est encombrée. Cliquez sur **Add Device** et sélectionnez les appareils auxquels accorder la priorité de bande passante lorsque le WAN est fortement sollicité.

        ![device priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Vous pouvez rechercher des appareils par nom de client, adresse MAC ou adresse IP. Sélectionnez les appareils, puis cliquez sur **Apply**.

        ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        Dans ce mode, vous pouvez définir la priorité des différentes applications. Le routeur attribue la bande passante en conséquence.

        ![application priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Pour personnaliser la priorité des applications, sélectionnez **Customize**, puis cliquez sur **Pre-Set up**.

        ![customize priority 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        Dans la fenêtre contextuelle, toutes les catégories ont par défaut une priorité moyenne.

        ![customize priority 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Faites glisser les catégories pour régler leur priorité, puis cliquez sur **Confirm**.

        ![customize priority 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        Dans ce mode, vous pouvez créer des règles QoS avancées pour le trafic prioritaire. Cliquez sur **Add Rule** pour définir des règles selon le protocole, le port et l’adresse IP source.

        ![advanced qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Indiquez Name, Protocol, Source Address et Destination Port, puis cliquez sur **Apply**.

        ![advanced qos rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Pour les firmwares v4.9 à v4.10

Activez l’interrupteur pour activer la QoS ; la page s’affichera comme ci-dessous.

![qos](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Définissez ensuite vos vitesses maximales d’envoi et de téléchargement (plage de saisie : 1 - 10000) pour l’ordonnancement du trafic. Faites-les correspondre à votre bande passante Internet réelle pour obtenir les meilleurs résultats.

![qos speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Remarque** : les valeurs saisies dans le champ sont en **Mbps** (mégabits par seconde). L’équivalent en **MB/s** (mégaoctets par seconde) s’affiche à titre indicatif.

Définissez ensuite les priorités pour les différentes applications. Le routeur allouera la bande passante en conséquence.

![app priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Pour personnaliser la priorité des applications, sélectionnez **Customize** puis cliquez sur **Pre-Set up**.

![customize priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

Dans la fenêtre contextuelle, toutes les catégories sont définies par défaut sur **Medium Priority**.

![customize priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Faites glisser les catégories pour ajuster leur priorité selon vos besoins, puis cliquez sur **Confirm**.

![customize priority3](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
