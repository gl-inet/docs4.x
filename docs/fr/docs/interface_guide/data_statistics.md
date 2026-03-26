# Statistiques de données

Data Statistics propose un tableau de bord intelligent de visualisation du trafic qui classe et représente l’utilisation du réseau par application, afin de vous aider à surveiller le trafic en temps réel et l’historique pour une meilleure visibilité et un meilleur contrôle du réseau.

**Note**:

1. Cette fonctionnalité n’est actuellement disponible que sur le **GL-MT5000 (Brume 3)**.

2. Cette fonctionnalité ne peut pas fonctionner avec Network Acceleration. Son activation désactivera automatiquement Network Acceleration afin de garantir un fonctionnement correct.

---

## Configuration rapide

Sur le côté gauche du panneau d’administration web, allez à **FLOW CONTROL** > **Data Statistics**.

Activez le commutateur en haut à droite pour afficher **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data-statistics.png){class="glboxshadow"}

- **Top 10 Apps by Bandwidth Usage** : cette section présente un graphique de tendance basé sur le temps (par exemple sur la journée écoulée) pour montrer la consommation de bande passante des 10 applications principales pendant la période sélectionnée.

    Basculez la chronologie entre Past Hour, Past Day et Past Week si nécessaire.

- **App Traffic Statistics** : cette section affiche des métriques détaillées de trafic pour chaque application, y compris les données Download, Upload et Total Bandwidth.

    Recherchez des applications spécifiques dans la barre de recherche si nécessaire.

## Règles de stockage des données

1. Les statistiques de trafic sont enregistrées en RAM toutes les 15 secondes et écrites dans la mémoire flash toutes les 1 heure. Les écritures fréquentes en flash sont évitées afin de préserver sa durée de vie.

2. Un redémarrage logiciel n’entraîne pas de perte de données. Le système écrit d’abord les données de la RAM vers la mémoire flash avant de redémarrer.

3. Un redémarrage forcé (débrancher puis rebrancher l’alimentation) ou une mise à niveau du firmware (en conservant les paramètres) peut entraîner une perte de données allant jusqu’à la dernière heure.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
