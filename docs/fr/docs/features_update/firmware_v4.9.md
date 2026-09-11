# Firmware v4.9

Cette version met l’accent sur un contrôle réseau plus précis, une meilleure gestion du trafic, une sécurité réseau renforcée et une interface utilisateur remaniée, afin d’améliorer l’expérience globale.

Téléchargez le dernier firmware depuis le [Centre de téléchargement du firmware](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control est un module central de gestion réseau qui permet d’identifier, de surveiller, de réguler et de filtrer précisément le trafic réseau. Il optimise l’allocation des ressources réseau, réduit la congestion de la bande passante et normalise les comportements d’accès au réseau pour offrir une expérience plus fluide, plus sûre et mieux contrôlable. Dans le firmware v4.9, ce module s’intègre à plusieurs fonctions pratiques pour une gestion complète du trafic.

Le module Flow Control comprend DPI Engine, Data Statistics, Content Filter, QoS, SQM et Parental Control.

### DPI Engine

Contrairement aux routeurs traditionnels, qui identifient uniquement les adresses source et de destination, DPI (Deep Packet Inspection) analyse en profondeur le contenu des paquets et identifie précisément les applications et les sites web à l’aide d’une bibliothèque de correspondance de caractéristiques. Il permet ainsi une classification et un contrôle détaillés du trafic.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics fournit un tableau de bord intuitif qui identifie l’utilisation du réseau par application et par protocole. Cette fonction permet de consulter les tendances sur 1 heure, 1 jour et 7 jours, affiche le classement des utilisations, surveille le trafic de chaque appareil et permet de bloquer en un clic les applications indésirables.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter est une fonction de sécurité en ligne intelligente fondée sur la classification DPI. Elle bloque automatiquement les sites web nuisibles et malveillants afin de préserver la sécurité du réseau. Elle prend également en charge des règles personnalisées pour bloquer des applications, des domaines ou des adresses IP spécifiques.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS (Quality of Service) optimise l’allocation de la bande passante en donnant la priorité aux activités essentielles, telles que les appels vidéo et les jeux, lorsque le réseau est encombré. Cela réduit la latence et améliore les performances globales du réseau.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) gère intelligemment le trafic réseau du routeur afin de réduire au minimum la latence et le « bufferbloat », pour des jeux et des appels vocaux plus fluides.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

Auparavant classée dans le menu **Applications**, cette fonction est déplacée vers le menu **Flow Control** dans le firmware v4.9. Elle exploite le DPI Engine amélioré pour identifier et bloquer avec précision les applications et contenus réseau inappropriés, offrant ainsi des restrictions d’accès basées sur le trafic plus professionnelles et plus précises.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

Le firmware v4.9 améliore de manière complète la logique de routage sous-jacente et l’interface interactive du module VPN. Il corrige les conflits de routage potentiels, simplifie la logique de configuration et rend l’utilisation plus intuitive.

Les ajustements détaillés sont les suivants.

### Tunnel VPN isolé

Chaque tunnel VPN fonctionne comme un groupe indépendant, sans basculement entre groupes. Dès que le trafic réseau correspond à un groupe VPN donné, il ne bascule pas automatiquement vers d’autres groupes VPN, même si le tunnel actuel échoue. Le routage du trafic reste ainsi stable et prévisible.

**Remarque** : la stratégie traditionnelle « Not Use VPN » est supprimée dans le firmware v4.9, ce qui élimine les configurations redondantes et évite les conflits de routage provoqués par des règles de tunnel multiples et complexes.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Basculement des profils VPN

Un même groupe de tunnels VPN peut contenir plusieurs profils de configuration. Les utilisateurs peuvent personnaliser la priorité de chaque profil au sein du même groupe, ce qui permet un basculement interne automatique afin de maintenir la connectivité VPN lorsqu’un profil échoue.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Tableau de bord repensé

Le VPN Dashboard a été entièrement repensé avec une mise en page plus intuitive. L’état des tunnels, les détails de connexion et les entrées de configuration sont présentés plus clairement, ce qui améliore considérablement l’exploitation et la gestion au quotidien. En outre, dans la nouvelle architecture, le Kill Switch est activé par défaut pour tous les tunnels VPN afin de protéger le trafic en permanence.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

Le firmware v4.9 introduit officiellement le protocole AmneziaWG 2.0, doté de plusieurs nouveaux paramètres d’obfuscation du trafic. Le protocole amélioré permet d’éviter efficacement la détection par DPI et par d’autres systèmes d’identification du trafic, ce qui renforce nettement la discrétion de la connexion et la résistance aux interférences. Il permet ainsi d’établir des connexions VPN stables et fiables dans les régions soumises à des restrictions réseau et dans les environnements réseau complexes.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## Réseau IoT

Dans le firmware v4.9, vous pouvez créer un réseau Wi-Fi dédié et indépendant pour les appareils IoT intelligents. Isolé physiquement et logiquement du réseau principal, il évite l’occupation des ressources réseau et les risques de sécurité liés à l’accès des appareils IoT au réseau principal. Cette optimisation offre une compatibilité plus large avec divers clients IoT intelligents et renforce globalement la sécurité du réseau domestique.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL, abréviation de Access Control List, est une fonction centrale de gestion de la sécurité réseau qui permet de créer des règles d’accès personnalisées pour gérer le trafic interne et externe selon les protocoles de connexion, les adresses IP des appareils et les ports. Elle prend en charge un contrôle précis des autorisations afin d’autoriser ou de bloquer certains comportements d’accès au réseau. Lorsque plusieurs règles ACL entrent en conflit, le système applique automatiquement la règle de priorité la plus élevée afin de garantir l’exécution correcte de la stratégie.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL se distingue de Port Forwarding par son rôle principal : ACL se concentre sur la gestion de la sécurité réseau en contrôlant les autorisations d’accès des appareils et du trafic, tandis que Port Forwarding sert à rediriger les ressources réseau en transférant le trafic externe vers des terminaux locaux spécifiques pour permettre l’accès à distance aux services du réseau local.

## Interface Wireless

L’interface Wireless a été entièrement repensée avec une mise en page simplifiée et un style visuel unifié. Cela réduit la complexité d’utilisation et améliore nettement la simplicité et la convivialité de l’interface.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## DNS chiffré

Le DNS chiffré prend désormais en charge davantage de protocoles de chiffrement, notamment DoH, DoT et DoQ. D’autres fournisseurs DNS officiels sont également intégrés, et la configuration manuelle de serveurs DNS chiffrés personnalisés est ajoutée pour répondre à différents besoins de résolution sécurisée des noms de domaine.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

Les routeurs GL.iNet peuvent désormais fonctionner comme Tailscale Exit Node. Tout le trafic Internet sortant des appareils du Tailnet peut être routé via l’adresse IP publique du routeur, ce qui permet une gestion de sortie réseau unifiée et sécurisée pour l’ensemble du réseau Tailscale. Consultez [cette page](../interface_guide/tailscale.md#run-exit-node) pour plus de détails.

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
