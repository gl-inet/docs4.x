# DPI Engine

**Remarque**: Cette fonction a été introduite dans le firmware v4.9.

Certains modèles, notamment Mango 2 (GL-MG1300), ne prennent pas en charge DPI Engine en raison d’une mémoire insuffisante, même avec le firmware v4.9 ou une version ultérieure. Consultez les [modèles pris en charge](#supported-models) pour plus de détails.

---

Le DPI (Deep Packet Inspection) est une technologie clé de gestion intelligente du réseau. Contrairement aux routeurs traditionnels qui n’identifient que les adresses source et destination, le DPI analyse en profondeur la charge utile des paquets et identifie avec précision les applications et sites web grâce à une bibliothèque de signatures, afin de permettre une classification et un contrôle précis du trafic.

Le DPI Engine de GL.iNet s’exécute localement sur votre routeur afin d’offrir une gestion intelligente du réseau tout en préservant entièrement votre confidentialité. Il fournit un accès complet aux statistiques de trafic, au filtre de contenu et à la QoS pour un contrôle global du trafic.

Intégré à [Netify](https://www.netify.ai/){target="_blank"}, le DPI de GL.iNet s’appuie sur un plug-in embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, il permet une gestion du réseau plus fiable, plus précise et plus efficace.

**Remarque** :

1. Lorsque le routeur est en mode Drop-in Gateway, les fonctionnalités DPI (notamment Statistiques de données, Filtre de contenu et QoS) ainsi que le SQM ne prennent pas effet.

2. Lorsque le DPI est activé, la fonction Network Acceleration sera automatiquement désactivée afin de garantir des performances stables.

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


## Configuration rapide

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **DPI Engine**, puis cliquez sur **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Dans la fenêtre contextuelle, lisez et acceptez les **Terms of Service & Privacy Policy**, puis cliquez sur **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Veuillez patienter pendant que le routeur effectue les opérations système. Il désactivera automatiquement Network Acceleration et activera Data Statistics ainsi que Content Filter.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Une fois l’activation terminée, cliquez sur **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Vous serez redirigé vers le **DPI Engine Version Center**, où vous pourrez consulter la version du programme DPI et la version de la base de données.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Remarque** : cette page affiche uniquement les indicateurs d’état essentiels du système. Le traitement du trafic commencera une fois les fonctionnalités concernées activées.

## Mise à niveau de la base de données

Si une version plus récente de la base de données est disponible, cliquez simplement sur **Upgrade** pour la mettre à jour.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
