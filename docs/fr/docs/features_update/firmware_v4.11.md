# Firmware v4.11 {#firmware-v411}

Cette version améliore la surveillance de la qualité du réseau et l’évaluation de la sécurité afin de vous aider à identifier les problèmes de connexion et les risques de sécurité potentiels. Elle améliore également DNS, QoS, SQM et les statistiques des données pour une gestion du réseau et un contrôle du trafic plus souples.

Téléchargez le dernier firmware depuis le [centre de téléchargement du firmware](https://dl.gl-inet.com/){target="_blank"}.

## Qualité du réseau {#network-quality}

[Network Quality](../interface_guide/network_quality.md) est une nouvelle fonctionnalité qui surveille votre connexion Internet en temps réel. Elle évalue la réactivité, la latence et les performances DNS, tout en détectant les interruptions de connexion et les pertes de paquets. Elle permet ainsi d'identifier l'instabilité du réseau et les problèmes de connexion que les tests de bande passante seuls ne révèlent pas toujours.

![network quality](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/network_quality.png){class="glboxshadow"}

## Analyse de sécurité {#security-scan}

[Security Scan](../interface_guide/security_scan.md) est une nouvelle fonctionnalité qui évalue les paramètres de sécurité de votre routeur et fournit un score de sécurité, des alertes de risque et des suggestions d'optimisation. Elle vérifie notamment la sécurité Wi-Fi, le ping WAN, l'accès SSH à distance, la redirection de port et la protection du contenu par DPI, afin de vous aider à identifier et à traiter les risques de sécurité potentiels. Une analyse démarre automatiquement lorsque vous ouvrez la page. Vous pouvez également cliquer sur l'icône du score pour réinitialiser et relancer l'analyse.

![security scan](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/security_scan.png){class="glboxshadow"}

## UPnP {#upnp}

[UPnP](../interface_guide/upnp.md) permet aux appareils LAN et aux applications compatibles de demander automatiquement des mappages de ports sans configuration manuelle de redirection de port. Cela simplifie la connexion pour les jeux en ligne, le partage de fichiers entre pairs et l’accès à distance. Sur la page UPnP, vous pouvez consulter les mappages actifs, vérifier la durée de bail restante et supprimer les mappages si nécessaire.

![UPnP](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/upnp.png){class="glboxshadow"}

## DNS {#dns}

Cette version améliore la configuration du [DNS](../interface_guide/dns_v4.11.md) en regroupant WAN DNS, VPN DNS et Manual DNS sur une seule page. Vous pouvez facilement consulter l'état du DNS pour chaque type de connexion, configurer des serveurs DNS personnalisés et choisir si les paramètres DNS manuels s'appliquent aux tunnels VPN ou au routeur lui-même.

![dns](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/dns.png){class="glboxshadow"}

## QoS {#qos}

La [QoS](../interface_guide/qos.md) (qualité de service) propose une option **Run Speedtest** pour la bande passante WAN, qui mesure les débits de téléchargement et d’envoi et remplit automatiquement les champs correspondants. En plus d’Application Priority, cette version ajoute deux stratégies d’ordonnancement : **Device Priority** et **Advanced QoS**.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/qos.png){class="glboxshadow" width=600}

- **Device Priority** : les clients locaux sélectionnés bénéficient d'une priorité réseau plus élevée en cas de congestion du WAN.

- **Application Priority** : définissez des priorités personnalisées pour différentes applications ; le routeur allouera la bande passante en conséquence.

- **Advanced QoS** : créez des règles QoS avancées pour le trafic prioritaire.

## SQM {#sqm}

[SQM](../interface_guide/sqm.md) (Smart Queue Management) propose une option **Run Speedtest** pour la bande passante WAN, qui mesure les débits de téléchargement et d’envoi et remplit automatiquement les champs correspondants. Deux disciplines de file d’attente sont disponibles : **cake** et **fq_codel**.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm.png){class="glboxshadow" width=600}

- **cake** : régulation intelligente et automatique du trafic offrant le meilleur contrôle global de la latence (recommandée).

    Pour cette discipline, la nouvelle option **Cake Autorate** ajuste dynamiquement la bande passante configurée en fonction du RTT des sondes. Elle utilise des pings légers plutôt que des tests de débit actifs et est recommandée pour les connexions WAN dont la bande passante fluctue.

    ![sqm cake autorate](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/sqm_cake_autorate.png){class="glboxshadow" width=600}

- **fq_codel** : mise en file d’attente équitable, simple et efficace, avec une réduction de base de la latence.

## Statistiques des données {#data-statistics}

[Data Statistics](../interface_guide/data_statistics.md) prend désormais en charge le filtrage du trafic par client et propose de nouveaux types de graphiques, notamment des diagrammes en barres et des diagrammes circulaires. Dans App Traffic Statistics, vous pouvez sélectionner un client précis et changer de type de graphique pour analyser plus clairement l'utilisation du trafic.

![data statistics](https://static.gl-inet.com/docs/router/en/4/features_update/4.11/data_statistics.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
