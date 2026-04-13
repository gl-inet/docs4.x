# Statistiques de données

Data Statistics fournit un tableau de bord de trafic intuitif qui identifie l’utilisation du réseau par application et par protocole. Il prend en charge l’affichage des tendances historiques sur 1 heure, 1 jour et 7 jours, présente les classements d’utilisation, surveille le trafic par appareil et permet de bloquer en un clic les applications indésirables.

**Remarque** : cette fonctionnalité ne peut pas fonctionner avec Network Acceleration. Son activation désactivera automatiquement Network Acceleration afin de garantir un fonctionnement correct.

## Modèles pris en charge

!!! note "Modèles pris en charge"
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)

## Configuration rapide

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **Data Statistics**.

Activez l’interrupteur dans l’angle supérieur droit pour afficher **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Cette page se compose de deux parties :

- **Top 10 Apps by Bandwidth Usage** : cette section présente un graphique d’évolution dans le temps (par ex. sur la dernière journée) afin de montrer la consommation de bande passante des 10 principales applications sur la période sélectionnée.

    Survolez le graphique avec la souris pour voir l’utilisation de données des 10 applications consommant le plus de bande passante à un moment précis.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics** : cette section affiche des métriques détaillées pour chaque application, notamment **Download**, **Upload** et **Total Bandwidth**. Recherchez des applications spécifiques dans la barre de recherche si nécessaire.

    Cliquez sur la flèche de tri à côté de l’en-tête de colonne pour classer la liste par ordre croissant ou décroissant.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

## Règles de stockage des données

1. Les statistiques de trafic sont enregistrées en RAM toutes les 15 secondes et écrites dans la mémoire flash toutes les 1 heure. Les écritures fréquentes en mémoire flash sont évitées afin d’en préserver la durée de vie.

2. Un redémarrage logiciel n’entraîne pas de perte de données. Le système écrit d’abord les données de la RAM vers la mémoire flash avant de redémarrer.

3. Un redémarrage forcé (débrancher puis rebrancher l’alimentation) ou une mise à niveau du firmware (en conservant les paramètres) peut entraîner une perte de données allant jusqu’à la dernière heure.

## Changer la plage horaire

Vous pouvez changer la plage horaire entre **Past hour**, **Past day** et **Past week** selon vos besoins.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

La plage horaire choisie détermine la manière dont les données sont affichées :

- **Pour une vue détaillée (par ex. Past Hour)** : le graphique montre des variations fines et en temps réel. Les pics sont plus élevés et les baisses plus marquées, ce qui permet de repérer facilement les augmentations soudaines de bande passante.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Pour une vue d’ensemble (par ex. Past Day ou Past Week)** : le graphique condense les données sur une période plus longue. Les courbes deviennent plus lisses et montrent la tendance générale du trafic plutôt que chaque petite variation.

    ![past day](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_day.png){class="glboxshadow"}

## Effacer les statistiques

Cliquez sur l’icône en forme de balai dans l’angle supérieur gauche pour effacer les statistiques si nécessaire.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Après l’effacement, la page sera mise à jour comme ci-dessous. Vous devrez peut-être attendre un moment avant que de nouvelles statistiques commencent à se charger.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
