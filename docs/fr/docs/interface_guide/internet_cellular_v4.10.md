# Se connecter à Internet via le réseau cellulaire (v4.10)

Le contenu de cette page est basé sur les versions de firmware v4.10 et ultérieures. Si votre appareil utilise une autre version du firmware, utilisez le sélecteur ci-dessous pour passer au guide correspondant.

<div class="gl-link-select" data-label="Version du firmware" data-placeholder="Firmware v4.10 et versions ultérieures" markdown="1">

- [Firmware v4.8 - v4.9](internet_cellular.md)
- [Firmware v4.7 et versions antérieures](internet_cellular_v4.7.md)

</div>

---

La plupart des routeurs GL.iNet prennent en charge la connectivité cellulaire. Ce guide présente les connexions cellulaires pour deux types de routeurs :

1. **Routeurs cellulaires**

    Les routeurs cellulaires GL.iNet sont équipés d’un module 4G/5G intégré et d’un ou de deux emplacements pour carte SIM, comme Spitz AX (GL-X3000) et Mudi 7 (GL-E5800). Les paramètres cellulaires du panneau d’administration web peuvent varier légèrement selon le modèle et la version du firmware. Pour configurer la connexion cellulaire de ces modèles, consultez [Routeurs cellulaires](#routeurs-cellulaires).

2. **Routeurs non cellulaires**

    Il s’agit d’autres types de routeurs, notamment les routeurs domestiques, de voyage et mini, ainsi que les passerelles de sécurité. Ils disposent généralement d’un port USB permettant de connecter un dongle USB (non fourni) pour obtenir une connectivité cellulaire. Pour configurer la connexion cellulaire de ces modèles, consultez [Routeurs non cellulaires](#routeurs-non-cellulaires).

**Remarque :** certaines cartes SIM doivent être activées avant leur première utilisation. Pour assurer la compatibilité, activez la carte SIM dans un smartphone avant de l’insérer dans le routeur.

## Routeurs cellulaires

Cette section utilise **Mudi 7 (GL-E5800)** comme exemple pour présenter les étapes de configuration cellulaire et les fonctionnalités associées.

Mudi 7 dispose d’une eSIM intégrée et de deux emplacements Nano-SIM, et prend en charge Dual SIM Dual Standby. Son panneau d’administration web peut donc différer légèrement de celui des autres routeurs cellulaires, en particulier des modèles dotés d’un seul emplacement SIM.

### Configuration du réseau

Connectez-vous au panneau d’administration web du routeur, puis accédez à **INTERNET** -> **Cellular**.

1. Lorsqu’aucune carte SIM n’est insérée, la page affiche « Your SIM card has not been detected ».

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Insérez une carte SIM. Le routeur commence automatiquement à se connecter. Une fois la connexion établie, la page affiche l’opérateur de la carte SIM, la puissance du signal, la bande, la consommation de données et d’autres options.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Si la carte SIM n’est pas détectée, réinsérez-la dans le routeur ou redémarrez le routeur et réessayez.

3. Pour afficher les détails du réseau, cliquez sur **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Dans **Network Information**, vous pouvez consulter SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address et IPv4 DNS Server.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Qu’est-ce que Max Bit Rate (AMBR) ?"

        AMBR signifie Aggregate Maximum Bit Rate. Ce paramètre définit le débit binaire maximal agrégé de tous les supports non-GBR de votre opérateur. Il est fourni par l’opérateur de réseau mobile.

4. Pour configurer manuellement le réseau, cliquez sur **Details & Configuration**.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Dans **Network Settings**, vous pouvez configurer des paramètres réseau tels que l’APN.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN** : les paramètres APN sont généralement récupérés automatiquement depuis la carte SIM. Certaines cartes SIM nécessitent un APN particulier. Si vous ne connaissez pas l’APN correct, contactez votre opérateur réseau.

    - **IP Type** : le type d’IP est détecté automatiquement. Vous pouvez sélectionner IPv4, IPv6 ou les deux. Vérifiez que l’option sélectionnée correspond au type d’IP pris en charge par votre carte SIM. Si la carte SIM ne prend pas en charge le type d’IP actuel, ou si IPv6 est sélectionné ici alors qu’il est désactivé sur le routeur, des problèmes de connexion peuvent survenir.

    - **International Data Roaming** : cette fonction est activée par défaut afin de faciliter l’utilisation des données lors de voyages à l’étranger. Vous pouvez la désactiver si elle n’est pas nécessaire ou pour éviter des frais d’itinérance élevés de la part de votre opérateur.

    - **TTL** : certains opérateurs déterminent si la carte SIM est utilisée dans un routeur en lisant la valeur TTL. Si la carte SIM ne fonctionne pas dans le routeur, essayez de définir une valeur TTL autre que 64 ou 128, par exemple 65.

    - **HL** : dans IPv6, le champ HL (Hop Limit) limite le nombre de sauts de transmission des paquets de données sur le réseau. Il correspond au TTL dans IPv4.

    - **MTU** : définissez la valeur MTU en fonction de votre scénario d’utilisation. Un réglage incorrect peut interrompre la connexion Internet. Si vous modifiez la MTU, redémarrez l’appareil pour appliquer le changement.

    - **Authentication** : cette option est généralement définie sur NONE si aucun identifiant n’est requis. Vous pouvez sélectionner PAP, CHAP ou PAP/CHAP.

### Statistiques de trafic

Pour afficher les statistiques de trafic, cliquez sur **Data Usage**.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Pour définir une limite de données pour votre carte SIM ou programmer la réinitialisation périodique de la consommation, activez **SIM Limit Settings**.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Définissez Data Cap Amount, Data Reset Period, Start Day et Start Hour, puis cliquez sur **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Remarque** :

1. Si Data Used dépasse Data Cap Amount, modifiez Data Cap Amount ou Data Used. Sinon, le réseau peut être déconnecté ou le routeur peut basculer vers une autre carte SIM, à condition que [SIM Failover](#sim-failover) soit activé.

2. Si Data Cap Amount est défini pour SIM 1 et que SIM Auto Switch est activé, SIM 1 bascule automatiquement vers SIM 2 lorsque sa consommation dépasse la limite, puis SIM 1 est désactivée.

3. Start Day : le nombre maximal de jours correspond au nombre réel de jours du mois en cours.

### Détails de la connexion cellulaire

Pour afficher les détails de la connexion cellulaire, cliquez sur **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Dans **Cellular Information**, vous pouvez consulter Network Type, TAC, Cell ID, Band et Signal History.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type** : le type de réseau est détecté automatiquement. Pour le définir, ouvrez l’onglet **Cellular Settings** et sélectionnez-le dans la liste déroulante.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Sélectionnez 5G pour obtenir un débit supérieur (un signal 5G est requis) ou 4G pour privilégier la stabilité.

    Si vous verrouillez une antenne relais, le type de réseau est fixé et ne peut plus être modifié.

- **TAC** : abréviation de Tracking Area Code. Cet identifiant attribué par le réseau représente une zone de suivi utilisée pour la gestion de la mobilité dans le réseau cellulaire. Il est détecté automatiquement à partir de la station de base cellulaire.

- **Cell ID** : identifiant unique permettant de distinguer une cellule particulière d’une station de base cellulaire. Il est également détecté automatiquement à partir de la station de base.

- **Band Information** : cliquez sur cette option pour afficher d’autres paramètres associés à la bande cellulaire.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History** : cliquez sur cette option pour afficher l’historique de la puissance du signal. Vous pouvez l’utiliser pour surveiller la qualité de la connexion cellulaire.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Masquage de bandes

Band Masking permet d’utiliser des bandes cellulaires précises afin d’améliorer le signal cellulaire.

Pour activer Band Masking, cliquez sur **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Dans **Cellular Settings**, activez **Band Masking**, sélectionnez les bandes souhaitées, puis cliquez sur **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Verrouillage de l’opérateur

!!! note "Modèles pris en charge"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Le GL-X2000 (Spitz Plus) prend en charge cette fonctionnalité à partir du firmware v4.8.

Le verrouillage sur un opérateur mobile précis oblige le routeur à utiliser uniquement son réseau. Cela assure une connexion stable et évite les frais d’itinérance involontaires, notamment dans les zones frontalières où l’appareil pourrait se connecter à des réseaux étrangers.

Pour verrouiller un opérateur, cliquez sur **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Dans **Cellular Settings**, cliquez sur **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Avant de rechercher les réseaux, vous pouvez sélectionner le **Lock Mode**.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual** : verrouille manuellement un opérateur précis.

- **Manual-Auto** : bascule automatiquement vers un réseau d’opérateur disponible si le verrouillage manuel échoue.

Cliquez ensuite sur **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Patientez environ une minute. Les opérateurs disponibles s’affichent. Sélectionnez-en un, puis cliquez sur **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Le signal cellulaire est alors verrouillé sur l’opérateur sélectionné.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Verrouillage d’une antenne relais

!!! note "Modèles pris en charge"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Le GL-X2000 (Spitz Plus) prend en charge cette fonctionnalité à partir du firmware v4.7.

Pour obtenir un signal de qualité et assurer une connexion cellulaire stable, vous pouvez essayer de verrouiller une antenne relais. Celle-ci doit toutefois correspondre aux bandes de fréquences prises en charge par votre opérateur et votre appareil, faute de quoi la connexion peut échouer.

Pour verrouiller une antenne relais, cliquez sur **Details & Configuration**.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Dans **Cellular Settings**, cliquez sur **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, cliquez sur **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Patientez environ une minute. Les antennes relais disponibles s’affichent.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Sélectionnez-en une pour afficher ses détails, puis cliquez sur **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Le signal cellulaire est alors verrouillé sur l’antenne relais sélectionnée.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Remarque** :

1. Il se peut que l’appareil ne puisse pas rechercher toutes les antennes relais lorsque l’interface Cellular est activée.

2. Si l’antenne relais verrouillée ne correspond pas au paramètre Band Masking (s’il est activé) ou aux paramètres APN de la configuration cellulaire, le routeur ne pourra pas se connecter au réseau cellulaire.

3. Si vous déplacez le routeur après avoir verrouillé une antenne relais, il tentera toujours de s’y reconnecter après un redémarrage. Cela peut l’empêcher de se connecter automatiquement au réseau cellulaire dans le nouvel emplacement. Dans ce cas, déverrouillez l’antenne relais actuelle ou verrouillez manuellement une nouvelle antenne.

### SMS

Consultez [SMS](../tutorials/sms.md).

### Transfert des SMS

Consultez [SMS Forwarding](../tutorials/sms_forwarding.md).

### Mode avion

Pour activer Airplane Mode, cliquez sur l’icône d’engrenage en haut à droite, puis activez **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Informations sur le modem

Pour afficher les détails du modem, cliquez sur l’icône d’engrenage en haut à droite, puis sélectionnez **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Basculement des cartes SIM

Cette fonctionnalité est disponible uniquement sur les routeurs cellulaires prenant en charge Dual-SIM.

SIM Failover permet au routeur de basculer automatiquement entre SIM 1 et SIM 2. Lorsque la consommation de données de la carte SIM prioritaire dépasse Data Cap Amount ou qu’elle ne parvient pas à se connecter à Internet, le routeur utilise la carte SIM de secours afin de maintenir la connexion réseau.

Pour activer SIM Failover, cliquez sur l’icône d’engrenage en haut à droite, puis sélectionnez **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

Dans la fenêtre contextuelle, activez **Auto Switch**. Vous pouvez faire glisser le bouton à droite afin de régler la priorité des cartes SIM.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Pour que le routeur revienne à la carte SIM préférée à une heure définie, activez **Scheduled Switch to Preferred SIM**, définissez **Daily Execution Time**, puis cliquez sur **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### Commande AT

Les commandes AT sont des instructions standard utilisées pour communiquer avec le modem cellulaire. Cette fonctionnalité permet d’envoyer des commandes et de vérifier l’état du modem.

Cliquez sur l’icône d’engrenage en haut à droite, puis sélectionnez **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut** : lorsque Shortcut est défini sur **Manual command**, saisissez la commande souhaitée dans le champ **AT Command**, puis cliquez sur **Send** en bas de la page. Le système affiche le résultat dans la zone de sortie située en dessous.

    Vous pouvez également cliquer sur le champ et sélectionner une **preset command** dans la liste déroulante.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Par exemple, si vous sélectionnez le raccourci « Request SIM card status » et l’emplacement SIM1, cliquez sur « Send » pour obtenir le résultat illustré ci-dessous.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot** : choisissez si la commande s’applique à SIM1 ou SIM2.

- **AT Command** : saisissez la commande souhaitée dans ce champ lorsque Shortcut est défini sur « Manual command ».

## Routeurs non cellulaires

Cette section utilise **Flint 3 (GL-BE9300)** et le dongle USB externe [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} comme exemple pour présenter la configuration cellulaire.

**Remarque** :

1. Certains dongles cellulaires USB, notamment SIMPoYo uFi, fonctionnent en **mode host-less**. Dans ce mode, le dongle établit lui-même la connexion cellulaire et expose une interface Ethernet USB virtuelle au routeur. Le routeur le traite comme une connexion WAN par partage de connexion plutôt que comme un modem cellulaire contrôlable. La connexion est donc établie via l’interface Tethering et non l’interface Cellular.

2. En mode de partage de connexion host-less, le routeur ne peut pas accéder aux mesures cellulaires de bas niveau, telles que la puissance du signal, Cell ID et TAC, ni contrôler l’APN ou les paramètres associés à la carte SIM. Configurez ces paramètres dans l’interface web intégrée du dongle.

---

Suivez les étapes ci-dessous pour configurer la connexion cellulaire.

1. Branchez le dongle USB sur le port USB du routeur.

2. Connectez-vous au panneau d’administration web du routeur, accédez à **INTERNET** -> **Tethering**, puis cliquez sur **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Pour définir des paramètres avancés tels que TTL, HL et MTU, cliquez sur **Advanced** et personnalisez-les avant de cliquer sur **Connect**.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Une fois la connexion établie, la page affiche les détails du réseau et un point vert, ce qui indique que la connexion a réussi.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

Après la configuration initiale, si vous redémarrez le routeur avec le modem USB branché ou si vous rebranchez le modem, celui-ci est reconnu automatiquement et la connexion réseau est établie sans avoir à cliquer de nouveau sur **Connect**.
