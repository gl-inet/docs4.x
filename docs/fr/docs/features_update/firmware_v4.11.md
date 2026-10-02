# Firmware v4.11

Cette version améliore la surveillance de la qualité du réseau et l'évaluation de la sécurité afin de vous aider à identifier les problèmes de connexion et les risques de sécurité potentiels. Elle introduit également de nouvelles fonctionnalités Mesh, GL.iNet Account et VLAN, ainsi que des améliorations importantes du DNS, de SQM, de QoS et des statistiques de trafic.

Téléchargez le dernier firmware depuis le [centre de téléchargement du firmware](https://dl.gl-inet.com/){target="_blank"}.

## Qualité du réseau

[Network Quality](../interface_guide/network_quality.md) est une nouvelle fonctionnalité qui surveille votre connexion Internet en temps réel. Elle évalue la réactivité, la latence et les performances DNS, tout en détectant les interruptions de connexion et les pertes de paquets. Elle permet ainsi d'identifier l'instabilité du réseau et les problèmes de connexion que les tests de bande passante seuls ne révèlent pas toujours.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Analyse de sécurité

[Security Scan](../interface_guide/security_scan.md) est une nouvelle fonctionnalité qui évalue les paramètres de sécurité de votre routeur et fournit un score de sécurité, des alertes de risque et des suggestions d'optimisation. Elle vérifie notamment la sécurité Wi-Fi, le ping WAN, l'accès SSH à distance, la redirection de port et la protection du contenu par DPI, afin de vous aider à identifier et à traiter les risques de sécurité potentiels. Une analyse démarre automatiquement lorsque vous ouvrez la page. Vous pouvez également cliquer sur l'icône du score pour réinitialiser et relancer l'analyse.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## Mesh

[Mesh](../interface_guide/mesh.md) est une fonctionnalité basée sur la norme Wi-Fi EasyMesh™ qui étend la couverture Wi-Fi à l'ensemble du domicile et permet une itinérance fluide. Si vous disposez de plusieurs routeurs GL.iNet, configurez-en un comme routeur principal et les autres comme nœuds mesh pour bénéficier d'une itinérance Wi-Fi fluide dans votre domicile.

**Remarque** : cette fonctionnalité a d'abord été proposée sur certains modèles, puis étendue à davantage de modèles dans la version 4.11 du firmware.

![mesh](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/mesh.png){class="glboxshadow"}

## Compte GL.iNet

Un [compte GL.iNet](../interface_guide/glinet_account.md) fournit un accès unifié à vos appareils et aux services cloud. Avec un seul compte GL.iNet, vous pouvez accéder à GoodCloud et à l'application GL.iNet pour gérer plus facilement votre réseau et vos appareils. Vous pouvez également utiliser GoodPAS pour établir rapidement une connexion sécurisée entre votre routeur de voyage et votre réseau domestique, afin d'y accéder à distance lorsque vous êtes absent.

**Remarque** : cette fonctionnalité a d'abord été proposée sur certains modèles, puis étendue à davantage de modèles dans la version 4.11 du firmware.

![gli.net account](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/glinet_account.png){class="glboxshadow"}

## GoodPAS

[GoodPAS](../interface_guide/goodpas.md) est une solution d'accès à distance basée sur le protocole AmneziaWG avec obfuscation intégrée du trafic. Elle permet de connecter en toute sécurité votre routeur de voyage à votre réseau domestique à l'aide d'un code d'accès dynamique, sans inscription ni connexion à un compte.

**Remarque** : cette fonctionnalité a d'abord été proposée sur certains modèles, puis étendue à davantage de modèles dans la version 4.11 du firmware.

![goodpas](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodpas.png){class="glboxshadow"}

## GoodCloud

[GoodCloud](../interface_guide/cloud.md) permet l'accès à distance et la gestion centralisée des routeurs GL.iNet. Vous pouvez gérer les appareils par lot, déployer des configurations réseau, effectuer des mises à niveau du firmware et accéder à distance au panneau d'administration web ou au terminal SSH du routeur.

**Remarque** : cette fonctionnalité a d'abord été proposée sur certains modèles, puis étendue à davantage de modèles dans la version 4.11 du firmware.

![goodcloud](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/goodcloud.png){class="glboxshadow"}

## Port Ethernet

La page [Ethernet Port](../interface_guide/ethernet_port_v4.10.md) affiche toutes les interfaces du routeur. Vous pouvez consulter l'état de connexion de chaque interface, gérer le rôle des ports Ethernet (WAN ou LAN) et afficher les détails des ports, comme l'adresse MAC, la vitesse négociée et l'état actuel de la liaison. Vous pouvez également affecter des interfaces physiques à n'importe lequel des sous-réseaux que vous avez créés.

**Remarque** : cette fonctionnalité a d'abord été proposée sur certains modèles, puis étendue à davantage de modèles dans la version 4.11 du firmware.

La figure suivante présente la page Ethernet Port du Flint 3 (GL-BE9300).

![ethernet port](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/ethernet_port.png){class="glboxshadow"}

## DNS

Cette version améliore la configuration du [DNS](../interface_guide/dns_v4.11.md) en regroupant WAN DNS, VPN DNS et Manual DNS sur une seule page. Vous pouvez facilement consulter l'état du DNS pour chaque type de connexion, configurer des serveurs DNS personnalisés et choisir si les paramètres DNS manuels s'appliquent aux tunnels VPN ou au routeur lui-même.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns_v4.11.png){class="glboxshadow"}

## QoS

La [QoS](../interface_guide/qos.md) (qualité de service) a été améliorée dans ce firmware. L'option **Run Speedtest** a été ajoutée pour la bande passante WAN : elle mesure les débits de téléchargement et d'envoi de la connexion WAN et remplit automatiquement les champs correspondants. Trois stratégies d'ordonnancement sont disponibles, dont les nouvelles options **Device Priority** et **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority** : les clients locaux sélectionnés bénéficient d'une priorité réseau plus élevée en cas de congestion du WAN.

- **Application Priority** : définissez des priorités personnalisées pour différentes applications ; le routeur allouera la bande passante en conséquence.

- **Advanced QoS** : créez des règles QoS avancées pour le trafic prioritaire.

## SQM

[SQM](../interface_guide/sqm.md) (Smart Queue Management) propose une option **Run Speedtest** pour la bande passante WAN, qui mesure les débits de téléchargement et d'envoi et remplit automatiquement les champs correspondants. Pour la discipline de file d'attente **cake**, la nouvelle option **Cake Autorate** ajuste dynamiquement la bande passante configurée en fonction du RTT des sondes. Elle utilise des pings légers plutôt que des tests de débit actifs et est recommandée pour les connexions WAN dont la bande passante fluctue.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_v4.11.png){class="glboxshadow" width=600}

![cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/cake_autorate.png){class="glboxshadow" width=600}

## Statistiques des données

[Data Statistics](../interface_guide/data_statistics.md) prend désormais en charge le filtrage du trafic par client et propose de nouveaux types de graphiques, notamment des diagrammes en barres et des diagrammes circulaires. Dans App Traffic Statistics, vous pouvez sélectionner un client précis et changer de type de graphique pour analyser plus clairement l'utilisation du trafic.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
