# Statistiques de données

**Remarque** : cette fonction a été introduite dans le firmware v4.9. Certains modèles, tels que Mango 2 (GL-MG1300), ne prennent pas en charge Data Statistics en raison d’une mémoire insuffisante, même lorsqu’ils exécutent le firmware v4.9 ou une version ultérieure.

---

Dans la partie gauche du panneau d’administration web, accédez à **FLOW CONTROL** -> **Data Statistics**.

Data Statistics fournit un tableau de bord de trafic intuitif qui identifie l’utilisation du réseau par application et par protocole. Il prend en charge l’affichage des tendances historiques sur 1 heure, 1 jour et 7 jours, présente les classements d’utilisation, surveille le trafic par appareil et permet de bloquer en un clic les applications indésirables.

**Remarque** :

1. La fonctionnalité Statistiques de données ne prend pas effet lorsque le routeur est en mode Drop-in Gateway.
2. La fonctionnalité Statistiques de données ne peut pas fonctionner avec Network Acceleration. Son activation désactivera automatiquement Network Acceleration afin de garantir des performances stables.
3. Data Statistics suit uniquement l’utilisation du trafic des appareils répertoriés sur la page **Clients**. Si un appareil se connecte au routeur via une interface de tunnel (par exemple, VPN Client, Tailscale ou AstroWarp), le trafic provenant de cet appareil et transféré par le routeur est exclu de ces statistiques.

## Pour le firmware v4.11 et les versions ultérieures

Activez l’interrupteur dans l’angle supérieur droit pour afficher **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Cette page se compose de deux parties :

- **Top 10 Apps by Bandwidth Usage** : cette section présente un graphique d’évolution dans le temps (par exemple sur la dernière journée) afin d’indiquer la consommation de bande passante des 10 principales applications sur la période sélectionnée.

    Survolez le graphique avec la souris pour afficher l’utilisation des données des 10 applications qui consomment le plus de bande passante à un moment précis.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics** : cette section affiche des mesures détaillées pour chaque application, notamment Download, Upload et Total Bandwidth. Recherchez une application dans la barre de recherche si nécessaire.

    Cliquez sur la flèche de tri à côté de l’en-tête de colonne pour classer la liste par ordre croissant ou décroissant.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Règles de stockage des données

1. Les statistiques de trafic sont enregistrées en RAM toutes les 15 secondes et dans la mémoire flash toutes les heures. Les écritures fréquentes dans la mémoire flash sont évitées afin d’en préserver la durée de vie.

2. Un redémarrage logiciel n’entraîne aucune perte de données. Le système écrit d’abord les données de la RAM dans la mémoire flash avant de redémarrer.

3. Un redémarrage forcé (débrancher puis rebrancher l’alimentation) ou une mise à niveau du firmware qui conserve les paramètres peut entraîner la perte des données de la dernière heure au maximum.

### Sélecteur de clients

Le sélecteur de clients permet de choisir un client précis ou de conserver l’option par défaut **All clients**. Le graphique et le tableau de statistiques s’actualisent automatiquement pour afficher uniquement les données de trafic de l’appareil sélectionné.

**Remarque** : cette fonction a été introduite dans le firmware v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Changer le type de graphique

Vous pouvez changer le type de graphique selon vos besoins lorsque vous consultez **App Traffic Statistics**.

**Remarque** : cette fonction a été introduite dans le firmware v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart** : ce graphique suit l’utilisation de la bande passante sur la période sélectionnée. Les courbes continues montrent l’évolution du trafic et facilitent l’identification des tendances à la hausse ou à la baisse.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart** : ce graphique compare côte à côte l’utilisation de la bande passante par application. Les barres permettent de voir rapidement quelles applications consomment le plus de bande passante.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart** : ce graphique répartit l’utilisation totale de la bande passante en pourcentages. Chaque secteur représente la part relative du trafic utilisée par une application.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Changer la plage horaire

Vous pouvez choisir **Past hour**, **Past day** ou **Past week** selon vos besoins.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

La plage choisie détermine la manière dont les données sont affichées :

- **Pour une vue détaillée (par exemple Past Hour)** : le graphique affiche des variations fines en temps réel. Les pics sont plus élevés et les baisses plus marquées, ce qui facilite la détection des augmentations soudaines de l’utilisation de la bande passante.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **Pour une vue d’ensemble (par exemple Past Day ou Past Week)** : le graphique condense les données sur une chronologie plus longue. Les courbes sont plus lisses et montrent la tendance générale du trafic plutôt que chaque petite variation.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Effacer les statistiques

Cliquez sur l’icône en forme de balai dans l’angle supérieur gauche pour effacer les statistiques si nécessaire.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Après l’effacement, la page s’actualise comme ci-dessous. Vous devrez peut-être attendre un instant avant le chargement de nouvelles statistiques.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Pour les firmwares v4.9 à v4.10

Activez l’interrupteur dans l’angle supérieur droit pour afficher **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Cette page se compose de deux parties :

- **Top 10 Apps by Bandwidth Usage** : cette section présente un graphique d’évolution dans le temps (par ex. sur la dernière journée) afin de montrer la consommation de bande passante des 10 principales applications sur la période sélectionnée.

    Survolez le graphique avec la souris pour voir l’utilisation de données des 10 applications consommant le plus de bande passante à un moment précis.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics** : cette section affiche des métriques détaillées pour chaque application, notamment **Download**, **Upload** et **Total Bandwidth**. Recherchez des applications spécifiques dans la barre de recherche si nécessaire.

    Cliquez sur la flèche de tri à côté de l’en-tête de colonne pour classer la liste par ordre croissant ou décroissant.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Règles de stockage des données

1. Les statistiques de trafic sont enregistrées en RAM toutes les 15 secondes et écrites dans la mémoire flash toutes les 1 heure. Les écritures fréquentes en mémoire flash sont évitées afin d’en préserver la durée de vie.

2. Un redémarrage logiciel n’entraîne pas de perte de données. Le système écrit d’abord les données de la RAM vers la mémoire flash avant de redémarrer.

3. Un redémarrage forcé (débrancher puis rebrancher l’alimentation) ou une mise à niveau du firmware (en conservant les paramètres) peut entraîner une perte de données allant jusqu’à la dernière heure.

### Changer la plage horaire

Vous pouvez changer la plage horaire entre **Past hour**, **Past day** et **Past week** selon vos besoins.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

La plage horaire choisie détermine la manière dont les données sont affichées :

- **Pour une vue détaillée (par ex. Past Hour)** : le graphique montre des variations fines et en temps réel. Les pics sont plus élevés et les baisses plus marquées, ce qui permet de repérer facilement les augmentations soudaines de bande passante.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Pour une vue d’ensemble (par ex. Past Day ou Past Week)** : le graphique condense les données sur une période plus longue. Les courbes deviennent plus lisses et montrent la tendance générale du trafic plutôt que chaque petite variation.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Effacer les statistiques

Cliquez sur l’icône en forme de balai dans l’angle supérieur gauche pour effacer les statistiques si nécessaire.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Après l’effacement, la page sera mise à jour comme ci-dessous. Vous devrez peut-être attendre un moment avant que de nouvelles statistiques commencent à se charger.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
