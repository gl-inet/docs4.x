# Firmware v4.9

Cette version met l’accent sur un contrôle réseau plus précis, une meilleure gestion du trafic, une sécurité réseau renforcée et une interface utilisateur remaniée, afin d’améliorer l’expérience globale. [Centre de téléchargement du firmware](https://dl.gl-inet.com/){target="_blank"}

## Flow Control

Flow Control est un module central de gestion réseau qui permet d’identifier, de surveiller, de réguler et de filtrer précisément le trafic réseau. Il optimise l’allocation des ressources réseau, réduit la congestion de la bande passante et normalise les comportements d’accès au réseau pour offrir une expérience plus fluide, plus sûre et mieux contrôlable. Dans le firmware v4.9, ce module s’intègre à plusieurs fonctions pratiques pour une gestion complète du trafic.

Le module Flow Control comprend les fonctions suivantes :

!!! note "DPI Engine"
    
    Technologie Deep Packet Inspection permettant d’identifier avec précision les protocoles applicatifs, les types de trafic et les comportements réseau.

!!! note "Statistiques de données"
    
    Collecte, analyse et visualisation en temps réel et historique des données de trafic réseau pour une surveillance intuitive de l’état du réseau.

!!! note "Filtrage de contenu"
    
    Interception et filtrage intelligents des contenus réseau inappropriés afin de normaliser l’accès au réseau.

!!! note "QoS (Quality of Service)"
    
    Allocation de bande passante et planification des priorités de trafic pour garantir la qualité du réseau aux applications clés.

!!! note "SQM (Smart Queue Management)"
    
    Optimise la planification des files d’attente réseau afin de réduire la latence et la perte de paquets, pour une transmission réseau plus fluide.

!!! note "Contrôle parental"
    
    Auparavant classée dans le menu **Applications**, cette fonction est déplacée vers le menu **Flow Control** dans la version v4.9. Elle exploite le DPI Engine amélioré pour identifier et bloquer avec précision les applications et contenus réseau inappropriés, offrant ainsi des restrictions d’accès basées sur le trafic plus professionnelles et plus précises.

## VPN

Le firmware v4.9 améliore de manière complète la logique de routage sous-jacente et l’interface interactive du module VPN. Il corrige les conflits de routage potentiels, simplifie la logique de configuration et rend l’utilisation plus intuitive.
    
Les ajustements détaillés sont les suivants :

!!! note "Regroupement VPN indépendant"

    Chaque tunnel VPN fonctionne comme un groupe indépendant, sans basculement entre groupes. Lorsque le trafic réseau correspond à un groupe VPN donné, il ne bascule pas automatiquement vers d’autres groupes VPN, même si le tunnel actuel échoue. Le routage du trafic reste ainsi stable et prévisible.

!!! note "Basculement des profils au sein du groupe"
    
    Un même groupe de tunnels VPN peut contenir plusieurs profils de configuration. Les utilisateurs peuvent personnaliser la priorité de chaque profil au sein du même groupe, ce qui permet un basculement interne automatique afin de maintenir la connectivité VPN lorsqu’un profil échoue.
    
!!! note "Suppression de la stratégie \"Not Use VPN\""
    
    L’option traditionnelle "Not Use VPN" pour la configuration des stratégies VPN est supprimée dans la version v4.9. Cela élimine les entrées de configuration redondantes et évite efficacement les conflits complexes de logique de routage causés par plusieurs paramètres de stratégie.
    
!!! note "VPN Dashboard repensé"
        
    Le VPN Dashboard a été entièrement repensé avec une mise en page plus intuitive. Il affiche plus clairement l’état des tunnels, les informations de connexion et les entrées de configuration, ce qui améliore considérablement l’exploitation et la gestion au quotidien.

## Protocole AmneziaWG 2.0

Le firmware v4.9 introduit officiellement le protocole AmneziaWG 2.0, doté de plusieurs nouveaux paramètres d’obfuscation du trafic. Le protocole amélioré permet d’éviter efficacement la détection par DPI et par d’autres systèmes d’identification du trafic, ce qui renforce nettement la discrétion de la connexion et la résistance aux interférences. Il permet ainsi d’établir des connexions VPN stables et fiables dans les régions soumises à des restrictions réseau et dans les environnements réseau complexes.

## Réseau IoT

La nouvelle fonction de réseau IoT permet de créer un réseau Wi-Fi dédié et indépendant pour les appareils IoT intelligents. Isolé physiquement et logiquement du réseau principal, il évite l’occupation des ressources réseau et les risques de sécurité liés à l’accès des appareils IoT au réseau principal. Cette optimisation offre une compatibilité plus large avec divers clients IoT intelligents et renforce globalement la sécurité du réseau domestique.

## ACL (Access Control List)

ACL, abréviation de Access Control List, est une fonction centrale de gestion de la sécurité réseau qui permet de créer des règles d’accès personnalisées pour gérer le trafic interne et externe selon les protocoles de connexion, les adresses IP des appareils et les ports. Elle prend en charge un contrôle précis des autorisations afin d’autoriser ou de bloquer certains comportements d’accès au réseau. Lorsque plusieurs règles ACL entrent en conflit, le système applique automatiquement la règle de priorité la plus élevée afin de garantir l’exécution correcte de la stratégie.

ACL se distingue de Port Forwarding par son rôle principal : ACL se concentre sur la gestion de la sécurité réseau en contrôlant les autorisations d’accès des appareils et du trafic, tandis que Port Forwarding sert à rediriger les ressources réseau en transférant le trafic externe vers des terminaux locaux spécifiques pour permettre l’accès à distance aux services du réseau local.

## Autres améliorations

!!! note "Refonte de l’interface Wireless"
    
    L’interface des paramètres Wireless a été entièrement repensée avec une mise en page simplifiée et un style visuel unifié. Cela réduit la complexité d’utilisation et améliore nettement la simplicité et la convivialité de l’interface.

!!! note "DNS chiffré amélioré"
    
    Le DNS chiffré prend désormais en charge davantage de protocoles de chiffrement, notamment DoH, DoT et DoQ. D’autres fournisseurs DNS officiels sont également intégrés, et la configuration manuelle de serveurs DNS chiffrés personnalisés est ajoutée pour répondre à différents besoins de résolution sécurisée des noms de domaine.
    
!!! note "Prise en charge de Tailscale Exit Node"
    
    Les routeurs GL.iNet peuvent désormais fonctionner comme Tailscale Exit Node. Tout le trafic Internet sortant des appareils du Tailnet peut être routé via l’adresse IP publique du routeur, ce qui permet une gestion de sortie réseau unifiée et sécurisée pour l’ensemble du réseau Tailscale.
    
!!! note "Intégration d’AstroWarp"
    
    AstroWarp est officiellement intégré au GL.iNet Router SDK dans la version v4.9. Basé sur le protocole AmneziaWG avec capacité native d’obfuscation du trafic, il fournit un accès à distance stable, chiffré et sécurisé. Les utilisateurs peuvent terminer rapidement l’appairage de l’appareil et la configuration de la connexion à l’aide d’un code d’accès dynamique dans le panneau d’administration web. Il prend en charge une connexion sécurisée en un clic entre les routeurs de voyage et les réseaux domestiques en quelques secondes, sans création de compte ni connexion.
