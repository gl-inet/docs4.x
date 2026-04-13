# DPI Engine

Le DPI (Deep Packet Inspection) est une technologie clé de gestion intelligente du réseau. Contrairement aux routeurs traditionnels qui n’identifient que les adresses source et destination, le DPI analyse en profondeur la charge utile des paquets et identifie avec précision les applications et sites web grâce à une bibliothèque de signatures, afin de permettre une classification et un contrôle précis du trafic.

Le DPI Engine de GL.iNet s’exécute localement sur votre routeur afin d’offrir une gestion intelligente du réseau tout en préservant entièrement votre confidentialité. Il fournit un accès complet aux statistiques de trafic, au filtre de contenu et à la QoS pour un contrôle global du trafic.

Intégré à [Netify](https://www.netify.ai/){target="_blank"}, le DPI de GL.iNet s’appuie sur un plug-in embarqué léger pour un déploiement efficace. Grâce à la base de signatures Netify mise à jour en ligne, il permet une gestion du réseau plus fiable, plus précise et plus efficace.

**Remarque** :

1. Les fonctionnalités DPI ne prennent pas effet lorsque le routeur est en mode Drop-in Gateway.

2. Lorsque le DPI est activé, la fonction Network Acceleration sera automatiquement désactivée afin de garantir un fonctionnement stable.

## Modèles pris en charge

!!! note "Modèles pris en charge"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

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
