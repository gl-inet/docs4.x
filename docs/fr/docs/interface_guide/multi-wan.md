# Multi-WAN

<iframe width="560" height="315" src="https://www.youtube.com/embed/D1s1WScLP4s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Dans la partie gauche du panneau d'administration Web, allez dans **NETWORK** -> **Multi-WAN**.

Vous pouvez configurer le routeur avec plusieurs méthodes d'accès à Internet afin que, lorsqu'un type d'accès n'est pas disponible, il bascule automatiquement vers un autre en peu de temps. Vous pouvez aussi utiliser plusieurs méthodes d'accès à Internet en même temps et répartir les connexions réseau entre elles selon un certain ratio.

Les routeurs GL.iNet peuvent se connecter à Internet de plusieurs façons, par exemple via [Ethernet](internet_ethernet.md), [Repeater](internet_repeater.md), [Tethering](internet_tethering.md) ou [Cellular](internet_cellular.md). 

!!! Note

    1. Les modèles sans fonctionnalité Wi-Fi (par exemple GL-MT2500/GL-MT2500A) prennent uniquement en charge l'accès réseau par Ethernet, Tethering et Cellular.

    2. Les modèles sans port USB (par exemple GL-B3000) prennent uniquement en charge l'accès réseau par Ethernet et Repeater.

    3. Certains modèles prennent en charge [Dual-Ethernet WAN](dual-ethernet_wan.md), ce qui ajoute une interface Ethernet supplémentaire dans l'interface utilisateur.

## Suivi de l'état des interfaces

Les routeurs GL.iNet prennent en charge jusqu'à 5 interfaces réseau virtuelles, bien que le nombre exact varie selon le modèle. Par exemple, le GL-MT6000 dispose de **Ethernet 1**, **Ethernet 2**, **Repeater**, **Tethering** et **Cellular**, chacune assurant une fonction réseau distincte dans une configuration définie par logiciel.

Les routeurs utilisent la commande **ping** ou **httping** (uniquement pour la v4.3 et les versions antérieures) pour suivre l'état de la connexion vers l'IP de destination et déterminer si l'interface est disponible. 

Si l'interface est disponible, un point vert s'affiche à gauche ; sinon, il est gris.

![interface status track 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_1.jpg){class="glboxshadow"}

### Paramètres du suivi d'état

Cliquez sur l'icône en forme d'engrenage pour accéder aux paramètres de suivi d'état de chaque interface réseau. 

Par exemple, il s'agit du paramétrage du suivi d'état pour l'interface Ethernet, et le même principe s'applique aux autres interfaces.

![interface status track 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/interface_status_track_2.png){class="glboxshadow"}

- **Enable Interface Status Track** : cette option est activée par défaut. Vous pouvez désactiver le suivi d'état de l'interface ; dans ce cas, le routeur déterminera l'état de l'interface à partir de son état physique (par exemple, selon que le câble réseau est branché ou non).

- **Detection Mode** : cette fonction a été introduite sous le nom Low Data Mode en v4.5, puis renommée Detection Mode en v4.7. Trois modes sont disponibles : Normal Mode, Low Data Mode et Strict Mode.  

    Le mode normal est utilisé par défaut, le mode faible consommation de données n'effectue un suivi que lorsqu'une erreur réseau survient sur une interface, et le mode strict détermine l'état de l'interface uniquement à partir du résultat d'une commande de détection vers une IP publique.
    
    Vous pouvez utiliser Low Data Mode si vous disposez d'un forfait de données limité. En revanche, la reconnexion après une coupure réseau peut être légèrement plus lente qu'en mode normal, et seule l'interface Cellular sera activée par défaut.

- **Track Command** : la commande ping est utilisée pour suivre l'état de la connexion vers l'IP de destination afin de déterminer si l'interface est disponible. Pour le firmware v4.3 et les versions antérieures, la commande httping est également disponible.

- **IPv4 Track IP** : vous pouvez personnaliser ici l'IPv4 Track IP.

!!! Note

    Certains anciens firmwares, comme la v4.3, proposent des paramètres tels que **Track Interval**, **Change to Failure Condition** et **Change to Available Condition**. Ces paramètres ont été supprimés à partir de la v4.5 et remplacés par Detection Mode et Sensitivity Options.

### Options de sensibilité

Cette fonction est disponible depuis la v4.5.

![Sensitivity Options](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/sensitivity_options.jpg){class="glboxshadow"}

Ce niveau de sensibilité détermine l'intervalle de temps de détection de l'état de la connexion Internet. 

- Si le réseau est stable, par exemple pour regarder des vidéos ou des diffusions en direct, ou pour jouer, il est recommandé d'utiliser une sensibilité élevée afin d'obtenir un basculement rapide en cas de coupure réseau. 
- Si le réseau est instable et que vous téléchargez des fichiers en cache, il est recommandé d'utiliser une sensibilité faible afin d'éviter des basculements réseau constants et la détection répétée de connexions infructueuses.

**Conseil** : passer à une sensibilité élevée peut entraîner une déconnexion réseau ; ajustez ce paramètre avec prudence.

## Méthodes Multi-WAN

Il existe deux méthodes : **Failover** et **Load Balance**. **Failover** est activé par défaut lorsqu'il existe plusieurs connexions Multi-WAN.

**Failover** et **Load Balance** sont mutuellement exclusifs ; vous ne pouvez en utiliser qu'un seul.

### Failover

![multi-wan failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/failover.png){class="glboxshadow"}

Vous pouvez définir la priorité de chaque interface. Si l'interface en cours d'utilisation tombe en panne, le routeur basculera automatiquement vers l'autre interface disponible ayant la priorité la plus élevée.

Par exemple, si le routeur est configuré avec deux types d'accès à Internet, **Ethernet** et **Repeater**, et que la priorité d'Ethernet est 1 tandis que celle de Repeater est 2, l'interface Ethernet a la priorité la plus élevée ; le routeur utilisera donc Ethernet pour accéder à Internet. Si vous débranchez le câble Ethernet, l'interface Ethernet devient indisponible et le routeur bascule automatiquement vers l'interface Repeater pour l'accès à Internet.

Une fois la connexion Ethernet rétablie, le routeur rebascule automatiquement vers Ethernet pour l'accès à Internet, car cette interface a une priorité plus élevée.

### Load Balance

Utilisez plusieurs interfaces réseau en même temps pour augmenter la bande passante totale du routeur.

Le ratio de charge correspond à la proportion attribuée à chaque interface réseau, et le système affectera les nouvelles connexions aux interfaces en fonction du ratio configuré.

Par exemple, si le routeur est connecté en même temps à quatre réseaux (Ethernet, Repeater, Tethering et Cellular), et que les quatre interfaces réseau sont disponibles pour accéder à Internet, alors l'activation de Load Balance avec un ratio de 1:1:1:1 signifie que la charge de la bande passante sera répartie de manière équilibrée entre les quatre interfaces, car le système affectera les nouvelles connexions selon ce ratio 1:1:1:1.

Vous pouvez également personnaliser le ratio de charge. Si la bande passante Ethernet est de 200 Mbps, celle du Wi-Fi Repeater est de 100 Mbps et qu'aucune connexion Tethering ou Cellular n'est active, vous pouvez définir le ratio à 2 pour Ethernet, 1 pour Repeater et 0 pour Tethering/Cellular. Le système répartira alors les nouvelles connexions entre ces interfaces selon le ratio configuré de 2:1, ce qui signifie que l'interface Ethernet prendra en charge environ deux fois plus de connexions que l'interface Repeater. Par rapport au mode Failover, cela optimise l'efficacité globale du débit en équilibrant la charge sur les interfaces disponibles.

**Remarque :** il n'est pas garanti que les connexions actives ou le trafic correspondent exactement au ratio de charge. L'utilisation s'en rapproche davantage sur une durée plus longue.

![multi-wan load balance](https://static.gl-inet.com/docs/router/en/4/interface_guide/multi-wan/load_balance.png){class="glboxshadow"}

## Scénarios d'utilisation

* Le système de caisse d'un magasin utilise une connexion Internet filaire, tandis que Repeater vers le Wi-Fi des magasins voisins (ou l'insertion d'une carte SIM pour activer le réseau mobile) sert de méthode d'accès à Internet de secours afin d'éviter toute interruption des paiements mobiles lorsque le câble réseau n'est pas disponible.

* Si le routeur se connecte en Repeater à un Wi-Fi public, mais que la vitesse du réseau n'est pas suffisante, vous pouvez utiliser Mobile Tethering en même temps pour effectuer une répartition de charge et améliorer la bande passante globale.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

