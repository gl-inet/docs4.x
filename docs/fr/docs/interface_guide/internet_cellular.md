# Se connecter à Internet via le réseau cellulaire

**Remarque** : ce guide est basé sur le firmware v4.8. Pour les versions antérieures, veuillez consulter [ce guide](internet_cellular_v4.7.md).

---

La plupart des routeurs GL.iNet prennent en charge la connectivité cellulaire. Ce guide couvre trois types de modèles :

1. **Modèles 4G Single-SIM intégrés**

    Certains modèles intègrent un module 4G avec un seul emplacement pour carte SIM, comme le GL-E750 (Mudi). Veuillez consulter [Configuration des modèles Single-SIM](#setup-for-single-sim-models).

2. **Modèles 5G Dual-SIM intégrés**

    Certains modèles intègrent un module 5G avec deux emplacements pour carte SIM, comme le GL-X3000 (Spitz AX). Les paramètres cellulaires dans le panneau d'administration web peuvent différer légèrement. Veuillez consulter [Configuration des modèles Dual-SIM](#setup-for-dual-sim-models).

3. **Modèles compatibles avec un modem USB**

    Certains modèles n'ont pas d'emplacement pour carte SIM intégré, mais disposent d'un port USB et prennent en charge la connectivité cellulaire via un modem USB, comme le GL-MT3000 (Beryl AX). Veuillez consulter [Configuration d'un modem USB](#setup-for-usb-modem).

**Remarque :** certaines cartes SIM doivent être activées avant leur première utilisation. Pour garantir la compatibilité, activez la carte SIM dans un smartphone avant de l'insérer dans le routeur.

## Configuration des modèles Single-SIM {#setup-for-single-sim-models}

Les étapes suivantes s'appliquent aux modèles dotés d'un modem cellulaire intégré et d'un seul emplacement pour carte SIM.

Nous prenons ici le **GL-E750 (Mudi)** comme exemple. 

Nous vous recommandons d'éteindre d'abord le routeur, d'insérer une carte SIM préactivée dans l'emplacement, puis de le rallumer. Si vous insérez la carte SIM après le démarrage du routeur, le panneau d'administration web peut ne pas se mettre à jour automatiquement. Dans ce cas, actualisez la page ou redémarrez le routeur.

### Configuration automatique

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** -> **Cellular**.

1. Lorsqu'aucune carte SIM n'est insérée, la page affiche le message « Your SIM card has not been detected ».

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Insérez une carte SIM. L'appareil commencera à se connecter comme indiqué ci-dessous.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    S'il ne se connecte pas automatiquement, cliquez sur le bouton **Connect** s'il est disponible.

    Si la carte SIM n'est pas détectée, essayez de redémarrer le routeur pour voir si elle peut être détectée.
    
3. Une fois le réseau cellulaire connecté, la page affiche les détails du réseau avec un point vert, indiquant que la connexion a réussi.
    
    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Si la configuration automatique échoue, essayez la [configuration manuelle](#manual-setup-single-sim).

### Configuration manuelle {#manual-setup-single-sim}

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**, puis cliquez sur **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Vous pouvez afficher ou modifier les paramètres cellulaires de la carte SIM actuelle. 

**Remarque** : certaines cartes SIM peuvent nécessiter un APN spécifique. Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. Configurez l'APN correct sur votre routeur si nécessaire. 

L'application des modifications déclenchera une reconnexion.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN** : l'APN (Access Point Name) est un paramètre de passerelle requis pour une connexion au réseau cellulaire. Il permet au routeur de se connecter à Internet via votre opérateur mobile. Vous pouvez utiliser l'APN par défaut ou définir un APN personnalisé fourni par votre opérateur.

- **Protocol** : protocole de communication cellulaire (par exemple 3G, QMI ou QCM). Il est généralement détecté automatiquement et vous pouvez le modifier pour l'adapter à votre modem et aux exigences de votre opérateur.

- **Port** : port série utilisé pour communiquer avec le modem cellulaire. Il est généralement détecté automatiquement et ne nécessite pas d'ajustement manuel.

- **TTL** : TTL (Time To Live) définit la durée maximale pendant laquelle les paquets peuvent survivre dans le réseau. Par défaut, le routeur décrémente de 1 le TTL des paquets entrants provenant des appareils clients avant de les transférer. Si vous devez le forcer, vous pouvez définir ici une valeur fixe. Le paramètre TTL n'est valable que pour IPv4.

- **HL** : en IPv6, HL (Hop Limit) limite le nombre de sauts de transmission des paquets de données sur le réseau et correspond au TTL en IPv4.

- **MTU** : la valeur MTU par défaut est de 1500 octets.

- **Authentication** : choisissez la méthode d'authentification requise par votre opérateur (par exemple NONE, PAP, CHAP). Elle est généralement définie sur NONE si aucun identifiant n'est nécessaire.

- **Band Masking** : vous pouvez activer le masquage de bandes si vous souhaitez que le routeur bloque certaines bandes ou n'utilise que certaines bandes cellulaires. Cliquez [ici](#band-masking) pour plus de détails.

## Configuration des modèles Dual-SIM {#setup-for-dual-sim-models}

Les étapes suivantes s'appliquent aux modèles dotés d'un modem cellulaire intégré prenant en charge deux cartes SIM. Les pages peuvent différer légèrement de celles des modèles Single-SIM.

Nous prenons ici le **GL-X3000 (Spitz AX)** comme exemple. Il prend en charge le mode Dual SIM, Single Standby, ce qui signifie qu'il peut contenir deux cartes SIM pour l'accès cellulaire, mais qu'une seule carte SIM peut être active à la fois. Vous pouvez basculer manuellement entre les deux cartes SIM.

Nous vous recommandons d'éteindre d'abord le routeur, d'insérer vos cartes SIM préactivées dans les emplacements, puis de le rallumer. Si vous insérez la carte SIM après le démarrage du routeur, le panneau d'administration web peut ne pas se mettre à jour automatiquement. Dans ce cas, actualisez la page ou redémarrez le routeur.

### Configuration automatique

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** -> **Cellular**.

1. Lorsqu'aucune carte SIM n'est insérée, la page affiche le message « Your SIM card has not been detected ». 

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Lorsqu'une carte SIM est insérée, la page s'affiche comme ci-dessous. Cliquez sur **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Si la carte SIM n'est pas détectée, essayez de redémarrer le routeur pour voir si elle peut être détectée.

3. Une fois le réseau cellulaire connecté, la page affiche les détails du réseau avec un point vert, indiquant que la connexion a réussi.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Cliquez sur **View More Information** pour afficher davantage d'informations cellulaires, notamment les détails du modem, de la carte SIM, de l'accès à Internet et du signal cellulaire.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Si la configuration automatique échoue, essayez la [configuration manuelle](#manual-setup-dual-sim).

### Configuration manuelle {#manual-setup-dual-sim}

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**, puis cliquez sur **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Vous pouvez afficher ou modifier les paramètres cellulaires de la carte SIM actuelle. 

**Remarque** : certaines cartes SIM peuvent nécessiter un APN spécifique. Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. Configurez l'APN correct sur votre routeur si nécessaire. 

L'application des modifications déclenchera une reconnexion.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN** : l'APN (Access Point Name) est un paramètre de passerelle requis pour une connexion au réseau cellulaire. Il permet au routeur de se connecter à Internet via votre opérateur mobile. Vous pouvez utiliser l'APN par défaut ou définir un APN personnalisé fourni par votre opérateur.

- **Protocol** : protocole de communication cellulaire détecté automatiquement (par exemple QMI ou QCM) selon votre modem et votre opérateur.

- **Port** : port série détecté automatiquement pour la communication avec le modem cellulaire. 

- **TTL** : TTL (Time To Live) définit la durée maximale pendant laquelle les paquets peuvent survivre dans le réseau. Par défaut, le routeur décrémente de 1 le TTL des paquets entrants provenant des appareils clients avant de les transférer. Si vous devez le forcer, vous pouvez définir ici une valeur fixe. Le paramètre TTL n'est valable que pour IPv4.

- **HL** : en IPv6, HL (Hop Limit) limite le nombre de sauts de transmission des paquets de données sur le réseau et correspond au TTL en IPv4.

- **MTU** : la valeur MTU par défaut est de 1500 octets.

- **Authentication** : choisissez la méthode d'authentification requise par votre opérateur (par exemple NONE, PAP, CHAP). Elle est généralement définie sur NONE si aucun identifiant n'est nécessaire.

- **Band Masking** : vous pouvez activer le masquage de bandes si vous souhaitez que le routeur bloque certaines bandes ou n'utilise que certaines bandes cellulaires. Cliquez [ici](#band-masking) pour plus de détails.

### Paramètres des emplacements de carte SIM

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**, puis cliquez sur **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

La page affiche le bouton d'auto-basculement, la carte SIM active, l'ICCID et l'opérateur réseau.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Si deux cartes SIM sont insérées, vous pouvez activer **Auto Switch**.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch** : active le basculement automatique entre SIM 1 et SIM 2. La méthode de détection du réseau pour **SIM Auto Switch** est la même que celle configurée sur la page Multi-WAN.

- **Preferred SIM Card Slot** : définissez l'emplacement de carte SIM préféré sur SIM 1 ou SIM 2.

- **Failover Interval** : les valeurs disponibles vont de 5 minutes à 24 heures.

    Si la connexion Internet n'est toujours pas disponible après un basculement, l'appareil revient sur l'emplacement SIM préféré et attend cet intervalle avant de réessayer le basculement.

    Cette option s'applique lorsque ni la carte SIM préférée ni la carte SIM de secours n'ont de signal. L'appareil basculera entre les cartes SIM jusqu'à ce que l'une d'elles obtienne un signal valide.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled** 
    
    Lorsque cette option est activée, l'appareil vérifie chaque jour l'emplacement SIM préféré à l'heure configurée et tente d'y revenir si la carte SIM préférée retrouve un accès à Internet.
    
    Cela évite que la carte SIM de secours ne consomme un volume de données excessif. Si la carte SIM préférée n'a toujours pas de signal, l'appareil continuera d'utiliser la carte SIM de secours.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Remarque** : la fonction **Auto Switch** ne bascule pas immédiatement vers une autre carte SIM. D'une part, l'appareil a besoin de temps pour confirmer que la carte SIM actuelle ne peut pas accéder à Internet. D'autre part, l'autre carte SIM n'est pas en veille et nécessite un certain temps pour s'activer.

## Configuration d'un modem USB {#setup-for-usb-modem}

Les étapes suivantes s'appliquent aux modèles sans emplacement pour carte SIM intégré, mais disposant d'un port USB pour connecter un modem USB externe.

Nous prenons ici le **GL-MT3000 (Beryl AX)** avec un modem USB externe **SIMPoYo uFi** comme exemple.

Nous vous recommandons d'éteindre d'abord le routeur, d'insérer une carte SIM préactivée dans le modem USB, de brancher le modem sur le port USB du routeur, puis de rallumer le routeur. Si vous branchez le modem USB après le démarrage du routeur, le panneau d'administration web peut ne pas se mettre à jour automatiquement. Dans ce cas, actualisez la page ou redémarrez le routeur.

### Configuration rapide

1. Éteignez d'abord le routeur. Insérez une carte SIM dans le modem USB, branchez le modem sur le port USB du routeur, puis rallumez le routeur.

2. Connectez-vous au panneau d'administration web du routeur, accédez à **INTERNET** -> **Tethering**, puis cliquez sur **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Si vous devez définir des paramètres avancés (par exemple TTL, HL et MTU), cliquez sur **Advanced** pour les personnaliser, puis cliquez sur **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    La connexion démarre.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Une fois connecté, la page affiche les détails du réseau avec un point vert, indiquant que la connexion a réussi.
    
    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Remarque :** après la configuration initiale, si vous redémarrez le routeur avec le modem USB branché, ou si vous rebranchez le modem, celui-ci sera reconnu automatiquement et la connexion réseau sera établie sans avoir à cliquer de nouveau sur le bouton de connexion.

### Modems compatibles

Voici la liste des modems pris en charge que nous avons déjà testés. 

**SIMPoYo uFi** est une clé USB plug & play compacte avec hotspot Wi‑Fi intégrée, conçue pour offrir une connectivité rapide et fiable partout. Elle fonctionne de manière transparente avec la plupart des routeurs GL.iNet, ainsi qu'avec les ordinateurs portables, batteries externes, ports USB de voiture et autres sources d'alimentation USB. Elle comprend 10 Go de données gratuites pendant 30 jours, valables au Royaume-Uni et dans 34 pays européens.

| Modèle                                 | Cellulaire | Testé | Testé par       | Commentaires* |
| -------------------------------------- | ---------- | ----- | --------------- | ------------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)                        | 5G    | Oui    | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/)               | 4G    | Oui    | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | Oui    | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | Oui    | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | Oui    | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | Oui    | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | Oui    | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | Oui    | akw2312         |           |
| Quectel RM520N-GL                      | 5G       | Oui    | akw2312         |           |
| Quectel UC20-E                         | 3G       | Oui    | GL.iNet         |           |
| ZTE ME909s-821                         | 4G       | Oui    | GL.iNet         |           |
| Huawei E1550                           | 3G       | Oui    | GL.iNet         |           |
| Huawei E3276                           | 4G       | Oui    | GL.iNet         |           |
| Huawei E3372                           | 4G       | Oui    | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G       | Oui    | anonymous       | Host-less |
| TP-Link MA260                          | 3G       | Oui    | GL.iNet         |           |
| ZTE M823                               | 4G       | Oui    | Arnas Risqianto |           |
| ZTE MF190                              | 3G       | Oui    | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G       | Oui    | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G       | Oui    | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G       | Oui    | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G       | Oui    | anonymous       | Host-less |

- **QMI** : ce modem prend en charge le mode QMI. Veuillez sélectionner QMI comme protocole de communication cellulaire, ainsi que **/dev/cdc-wdm0** comme port série dans les paramètres de la carte SIM.

- **Host-less** : ce modem prend en charge le mode Tethering. Veuillez gérer la connexion via l'interface Tethering du routeur plutôt que via l'interface Cellular.

## Statistiques de trafic

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**, puis cliquez sur **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Vous accéderez à la page Traffic Statistics. Elle affiche la consommation de données de la ou des cartes SIM et propose des paramètres de limite de données.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Si **Data Used** dépasse **Data Cap Amount**, modifiez manuellement **Data Cap Amount** ou **Data Used**. Sinon, le réseau peut être déconnecté, ou la carte SIM peut basculer automatiquement (**Auto Switch** pour les modèles Dual-SIM).

- **Modifier Data Used**

    Cliquez sur **Modify** à droite de **SIM 1/2 Data Used**. 

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Vous pouvez ensuite modifier ou réinitialiser la quantité de données utilisée. 

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Définir une limite de données SIM**

    Si vous souhaitez définir une limite de données SIM, activez d'abord **Save data when power off**. Cela signifie que les données peuvent être conservées même après l'extinction de l'appareil.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Activez ensuite les **SIM 1 or SIM 2 Limit Settings**.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Pour les modèles Dual-SIM, nous recommandons d'activer également **SIM Card Slot Auto Switch**. Si **SIM 1 Data Cap Amount** est défini et que **SIM Card Slot Auto Switch** est activé, la carte SIM 1 basculera automatiquement vers la carte SIM 2 lorsque sa consommation dépassera **Data Cap Amount**, et la carte SIM 1 sera désactivée.

## Historique du signal

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**, puis cliquez sur **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Vous pouvez y vérifier la qualité de votre connexion cellulaire. Si le signal est faible, essayez de changer d'antenne relais pour obtenir un meilleur signal.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Consultez l'historique de la puissance du signal en sélectionnant différentes périodes dans le coin supérieur droit.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Masquage de bandes {#band-masking}

Le masquage de bandes vous permet de bloquer certaines bandes ou d'utiliser uniquement des bandes cellulaires préférées afin d'améliorer un signal cellulaire faible.

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular** -> **SIM Card Settings**, puis activez **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Sélectionnez le **Masking Mode** (Block ou Open), puis choisissez les bandes LTE, les bandes 5G NSA et les bandes 5G SA.

## SMS

Veuillez consulter le [tutoriel SMS](sms.md).

## SMS Forwarding

Veuillez consulter le [tutoriel SMS Forwarding](../tutorials/sms_forwarding.md).

## Verrouillage d'antenne relais

!!! note "Modèles pris en charge"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Le GL-X2000 (Spitz Plus) prend en charge cette fonctionnalité à partir du firmware v4.7.

Si vous souhaitez obtenir un signal de meilleure qualité et garantir une connexion cellulaire stable, vous pouvez essayer de verrouiller une antenne relais.

**Remarque :** l'antenne relais verrouillée doit correspondre aux bandes de fréquences prises en charge par votre opérateur et votre appareil ; sinon, la connexion peut échouer.

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**. Cliquez sur l'icône à trois points en haut à droite, puis sélectionnez **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Cliquez sur **Scan** pour lancer l'analyse des antennes relais cellulaires disponibles. Cela prendra quelques minutes. N'actualisez pas la page pendant l'analyse. 

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

Les antennes relais disponibles s'afficheront.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Cliquez sur une antenne relais pour afficher les détails et la verrouiller.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Remarque** : 

1. Il se peut que l'appareil ne puisse pas analyser toutes les antennes relais lorsque l'interface Cellular est activée.

2. Si l'antenne relais verrouillée ne correspond pas aux paramètres de masquage de bandes ou d'APN définis dans vos paramètres cellulaires, le routeur ne pourra pas se connecter au réseau cellulaire.

3. Après avoir verrouillé une antenne relais, si vous déplacez le routeur vers un autre emplacement, il tentera toujours de se reconnecter à l'antenne relais verrouillée après redémarrage. Cela peut empêcher le routeur de se connecter automatiquement au réseau cellulaire dans le nouvel emplacement. Dans ce cas, vous devrez soit déverrouiller l'antenne relais actuelle, soit la verrouiller manuellement sur une nouvelle antenne relais.

## Verrouillage d'opérateur

Cette fonctionnalité est disponible uniquement sur GL-X3000, GL-XE3000 et GL-X2000 (firmware v4.8 ou version ultérieure).

En verrouillant un opérateur mobile spécifique, le routeur n'utilisera que le réseau de cet opérateur, ce qui garantit une connexion stable et évite les frais d'itinérance involontaires — en particulier dans les zones frontalières où l'appareil pourrait sinon se connecter à des réseaux étrangers.

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**. Cliquez sur l'icône à trois points en haut à droite, puis sélectionnez **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Trois modes de verrouillage sont disponibles : 

- **Auto** : se connecter automatiquement à un réseau d'opérateur disponible.
- **Manual** : verrouiller manuellement un opérateur spécifique.
- **Manual-Auto** : basculer automatiquement vers un réseau d'opérateur disponible si le verrouillage manuel échoue.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Commandes AT du modem

Les commandes AT du modem sont des instructions standard utilisées pour communiquer avec le modem cellulaire. Cette fonctionnalité vous permet d'envoyer des commandes et de vérifier l'état du modem.

Dans le panneau d'administration web du routeur, accédez à **INTERNET** -> **Cellular**. Cliquez sur l'icône à trois points en haut à droite, puis sélectionnez **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Vous accéderez à la page AT Command.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Lorsque Shortcut est défini sur **Manual command**, vous pouvez saisir la commande souhaitée dans le champ AT Command.

Vous pouvez également cliquer sur la liste déroulante Shortcut pour sélectionner l'une des **preset commands**.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Les commandes prédéfinies suivantes sont disponibles :

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

À titre d'exemple, le raccourci « Request IMEI » est sélectionné ici. Cliquez sur « Send » et vous obtiendrez le résultat comme indiqué ci-dessous.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

Dans le coin inférieur droit, vous pouvez cliquer sur **Export Debug Info** pour télécharger un fichier .json.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Dépannage

Si vous ne parvenez pas à établir une connexion cellulaire, cliquez sur le message d'erreur ci-dessous pour consulter les solutions correspondantes.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Voici quelques suggestions de dépannage.
    
    1. Actualisez la page et attendez quelques minutes pour vérifier si la carte SIM peut être détectée.
    
    2. Assurez-vous que la carte SIM est correctement installée. Alignez l'encoche de la carte SIM avec le repère correspondant sur le logement afin de confirmer l'orientation d'insertion correcte.
    
    3. Éteignez le routeur, retirez puis réinsérez la carte SIM, puis rallumez le routeur.
    
    4. Essayez une autre carte SIM si possible.

    Si le problème persiste, téléchargez les journaux et envoyez-les à [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Ce problème comporte deux types de messages d'erreur :

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed
    
        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Voici quelques suggestions de dépannage.

    1. Actualisez la page et attendez quelques minutes pour vérifier si l'erreur disparaît.
    
    2. Cliquez sur **Disconnect**/**Abort**, puis sur **Connect** pour réessayer la connexion.
    
    3. Redémarrez le routeur.
    
    4. Vérifiez l'état de la carte SIM et assurez-vous qu'elle est activée. Testez la carte SIM en l'insérant dans un smartphone pour confirmer qu'elle peut accéder normalement à Internet avec un forfait de données mobiles actif, ou contactez votre opérateur réseau pour vérification.
    
    5. Certains opérateurs peuvent exiger un protocole 3G pour la connexion réseau. Accédez à **SIM Card Settings** -> **Protocol**, sélectionnez **3G**, puis cliquez sur **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        L'appareil se reconnectera automatiquement. Attendez quelques minutes pour vérifier si la connexion aboutit.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Si la connexion réussit, la page s'affichera comme ci-dessous.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}
    
    6. Certaines cartes SIM peuvent avoir des restrictions d'utilisation spécifiques (par exemple, exiger un APN particulier). Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. 
    
        Si nécessaire, accédez à **SIM Card Settings** -> **APN**, configurez l'APN correct sur le routeur, puis cliquez sur **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}
    
    7. Cliquez sur **View More Information** pour vérifier la puissance du signal cellulaire. Si le signal est faible, assurez-vous que l'antenne est correctement installée. Déplacez le routeur vers un emplacement dégagé et sans obstacle afin d'améliorer la réception du signal.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}
    
    8. Vérifiez si **Band Masking** ou **Lock Tower** est activé. Si c'est le cas, désactivez la fonctionnalité et réessayez de vous connecter.

    Si le problème persiste, téléchargez les journaux et envoyez-les à [support@gl-inet.com](mailto:support@gl-inet.com).

## Certification IoT {#iot-certification}

### Certification AT&T

Cliquez sur le lien [att device certification](https://iotdevices.att.com/certified-devices.aspx#), puis saisissez le nom de l'appareil pour le trouver. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Certification T-Mobile

Cliquez sur le lien [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification), choisissez 5G dans **Filter**, puis recherchez votre appareil. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Articles connexes

- [Page Internet](internet.md)
- [Comment définir la priorité de chaque méthode d'accès à Internet ?](multi-wan.md)
- [Comment définir l'équilibrage de charge lorsque plusieurs méthodes d'accès à Internet sont utilisées en même temps ?](multi-wan.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
