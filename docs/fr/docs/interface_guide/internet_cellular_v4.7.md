# Se connecter à Internet via le réseau cellulaire (firmware v4.7 et versions antérieures)

**Remarque** : ce guide est basé sur le firmware v4.7 et les versions antérieures. Pour les versions plus récentes, veuillez consulter [ce guide](internet_cellular.md).

---

La plupart des routeurs GL.iNet prennent en charge la connectivité cellulaire. Ce guide couvre trois types de modèles :

1. **Modèles 4G Single-SIM intégrés**

    Certains modèles intègrent un module 4G avec un seul emplacement pour carte SIM, comme le GL-XE300 (Puli). Veuillez consulter [Configuration des modèles Single-SIM](#setup-for-single-sim-models).

2. **Modèles compatibles avec un modem USB**

    Certains modèles disposent d'un port USB et prennent en charge la connectivité cellulaire via un modem USB, comme le GL-AXT1800 (Slate AX). Les étapes de configuration sont similaires à celles des modèles 4G Single-SIM intégrés. Veuillez consulter [Configuration des modèles Single-SIM](#setup-for-single-sim-models).

3. **Modèles 5G Dual-SIM intégrés**

    Certains modèles intègrent un module 5G avec deux emplacements pour carte SIM, comme le GL-X3000 (Spitz AX). Les paramètres cellulaires dans le panneau d'administration web peuvent différer légèrement. Veuillez consulter [Configuration des modèles Dual-SIM](#setup-for-dual-sim-models).

**Remarque :** certaines cartes SIM doivent être activées avant leur première utilisation. Pour garantir la compatibilité, activez la carte SIM dans un smartphone avant de l'insérer dans le routeur.

## Configuration des modèles Single-SIM {#setup-for-single-sim-models}

Les étapes suivantes s'appliquent aux modèles dotés d'un modem cellulaire intégré et d'un seul emplacement pour carte SIM (par exemple GL-XE300 Puli), ou d'un port USB pour connecter un modem USB externe (par exemple GL-AXT1800 Slate AX).

Nous prenons ici le **GL-AXT1800 (Slate AX)** avec un modem USB externe comme exemple.

Nous vous recommandons d'éteindre d'abord le routeur. Insérez une carte SIM préactivée dans le modem USB, puis branchez le modem sur le port USB du routeur. Ensuite, rallumez le routeur.

Si vous branchez le modem USB après le démarrage du routeur, le panneau d'administration web peut ne pas se mettre à jour automatiquement. Dans ce cas, actualisez la page ou redémarrez le routeur.

### Configuration automatique

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** -> **Cellular**.

1. Lorsque vous accédez à la page pour la première fois, il se peut qu'elle ne se connecte pas automatiquement, mais elle devrait afficher le nom de votre opérateur dans le coin supérieur gauche, ainsi que l'IMEI. Cliquez sur **Auto Setup**.

    Ignorez l'avertissement *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. La connexion démarre.

    **Remarque :** certaines cartes SIM peuvent avoir des restrictions d'utilisation particulières, par exemple exiger un APN spécifique. Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions particulières.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Une fois connecté, la page affichera les détails du réseau avec un point vert, indiquant que la connexion a réussi.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Remarque :** après la configuration initiale, si vous redémarrez le routeur avec le modem USB branché, ou si vous rebranchez le modem, le modem USB sera reconnu automatiquement et la connexion réseau sera établie sans devoir cliquer de nouveau sur le bouton Auto Setup.

Si la configuration automatique échoue, essayez la [configuration manuelle](#manual-setup).

### Configuration manuelle {#manual-setup}

Dans la section Cellular, cliquez sur **Manual Setup** pour afficher ou modifier les paramètres cellulaires de la carte SIM actuelle. 

**Remarque** : certaines cartes SIM peuvent nécessiter un APN spécifique. Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. Configurez l'APN correct sur votre routeur si nécessaire. 

L'application des modifications déclenchera une reconnexion.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol** : protocole de communication cellulaire (par exemple 3G, QMI ou QCM). Il est généralement détecté automatiquement et vous pouvez le modifier pour l'adapter à votre modem et aux exigences de votre opérateur.

- **Port** : port série utilisé pour communiquer avec le modem cellulaire. Il est généralement détecté automatiquement et ne nécessite pas d'ajustement manuel.

- **APN** : l'APN (Access Point Name) est un paramètre de passerelle requis pour une connexion au réseau cellulaire. Il permet au routeur de se connecter à Internet via votre opérateur mobile. Vous pouvez utiliser l'APN par défaut ou définir un APN personnalisé fourni par votre opérateur.

- **PIN** : si votre carte SIM est protégée par un code PIN, saisissez-le ici. Ce champ est facultatif si aucun code PIN n'est défini.

- **TTL** : TTL (Time To Live) définit la durée maximale pendant laquelle les paquets peuvent survivre dans le réseau. Par défaut, le routeur décrémente de 1 le TTL des paquets entrants provenant des appareils clients avant de les transférer. Si vous devez le forcer, vous pouvez définir ici une valeur fixe. Le paramètre TTL n'est valable que pour IPv4.

- **Service** : sélectionnez le type de service cellulaire afin de définir les technologies réseau que le modem utilisera.

- **Dial Number** : saisissez le numéro d'appel fourni par votre opérateur. Il est souvent préconfiguré et peut être laissé vide sur la plupart des réseaux modernes.

- **Authentication** : choisissez la méthode d'authentification requise par votre opérateur (par exemple NONE, PAP, CHAP). Elle est généralement définie sur NONE si aucun identifiant n'est nécessaire.

### Modems compatibles

Voici la liste des modems pris en charge que nous avons déjà testés.

| Modèle                                 | 3G/4G | Testé | Testé par       | Commentaires* |
| -------------------------------------- | ----- | ----- | --------------- | ------------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Oui   | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Oui   | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Oui   | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Oui   | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Oui   | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Oui   | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Oui   | akw2312         |           |
| Quectel UC20-E                         | 3G    | Oui   | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Oui   | GL.iNet         |           |
| Huawei E1550                           | 3G    | Oui   | GL.iNet         |           |
| Huawei E3276                           | 4G    | Oui   | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Oui   | GL.iNet         |           |
| ZTE M823                               | 4G    | Oui   | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Oui   | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Oui   | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Oui   | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Oui   | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Oui   | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Oui   | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Oui   | anonymous       | Host-less |

- **QMI** : ce modem prend en charge le mode QMI. Veuillez sélectionner QMI comme protocole et **/dev/cdc-wdm0** comme port série sur votre routeur cellulaire.

- **Host-less** : ce modem prend en charge le mode Tethering. Veuillez gérer la connexion via l'interface Tethering du routeur plutôt que via l'interface Cellular.

## Configuration des modèles Dual-SIM {#setup-for-dual-sim-models}

Les étapes suivantes s'appliquent aux modèles dotés d'un modem cellulaire intégré prenant en charge deux cartes SIM. Le panneau d'administration web peut différer légèrement de celui des modèles Single-SIM.

Nous prenons ici le **GL-X3000 (Spitz AX)** comme exemple. Il prend en charge le mode Dual SIM, Single Standby, ce qui signifie qu'il peut contenir deux cartes SIM pour l'accès cellulaire, mais qu'une seule carte SIM peut être active à la fois. Vous pouvez basculer manuellement entre les deux cartes SIM.

Nous vous recommandons d'éteindre d'abord le routeur, d'insérer vos cartes SIM préactivées dans les emplacements, puis de le rallumer. Si vous insérez la carte SIM après le démarrage du routeur, le panneau d'administration web peut ne pas se mettre à jour automatiquement. Dans ce cas, actualisez la page ou redémarrez le routeur.

### Configuration automatique

Connectez-vous au panneau d'administration web du routeur, puis accédez à **INTERNET** -> **Cellular**.

1. Lorsqu'aucune carte SIM n'est insérée, la page s'affiche comme suit.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Lorsqu'une carte SIM est insérée, le routeur commence automatiquement à se connecter.

    Si la connexion réussit, la page s'affiche comme suit.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

S'il ne se connecte pas automatiquement, cliquez sur **Auto Setup** et attendez que le routeur se connecte, ou essayez **Manual Setup**.

### Configuration manuelle

Dans la section Cellular, cliquez sur **Manual Setup** pour accéder à Cellular Settings.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Vous pouvez afficher ou modifier les paramètres cellulaires de la carte SIM actuelle. La page stocke également certains profils préconfigurés et vous permet d'ajouter manuellement des configurations dans **Saved Settings**.

### Paramètres des emplacements de carte SIM

Dans la section Cellular, cliquez sur **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Vous accéderez à **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Si deux cartes SIM sont insérées, vous pouvez activer **Auto Switch**.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

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

## Statistiques de trafic

Dans la section Cellular, cliquez sur **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Vous accéderez à la page Traffic Statistics. 

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Veuillez consulter le [tutoriel SMS](sms.md).

## SMS Forwarding

Veuillez consulter le [tutoriel SMS Forwarding](../tutorials/sms_forwarding.md).

## Modem Management

Dans la section Cellular, cliquez sur le bouton **Tool** en haut à droite pour accéder à la page Modem Management.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Elle comprend deux sections : **Modem Info** et **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

Les commandes AT sont des instructions standard utilisées pour communiquer avec le modem cellulaire.

Lorsque Shortcut est défini sur **Manual command**, saisissez la commande souhaitée dans le champ AT Command pour vérifier l'état du modem.

Vous pouvez également cliquer sur la liste déroulante Shortcut pour sélectionner l'une des **preset commands**.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Les commandes prédéfinies suivantes sont disponibles :

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

À titre d'exemple, le raccourci « Request IMEI » est sélectionné ici. Cliquez sur « Send » et vous obtiendrez le résultat comme indiqué ci-dessous.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Profil d'opérateur

Vous pouvez enregistrer différents profils pour un même opérateur ou pour des opérateurs différents.

Dans la section Cellular, cliquez sur le bouton **Profile** en haut à droite pour gérer les profils.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Ajoutez un nouveau profil ou enregistrez le profil actuel.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Créez votre propre profil selon les exigences de votre opérateur.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Vous pourrez sélectionner un profil enregistré ultérieurement.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Choisissez les profils dont vous avez besoin.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Verrouillage d'antenne relais

Cette fonctionnalité est disponible uniquement sur GL-X3000, GL-XE3000 et GL-X2000 (firmware v4.7 ou version ultérieure).

Si vous souhaitez obtenir un signal de meilleure qualité et garantir une connexion cellulaire stable, vous pouvez essayer de verrouiller une antenne relais.

**Remarque :** l'antenne relais verrouillée doit correspondre aux bandes de fréquences prises en charge par votre opérateur et votre appareil ; sinon, la connexion peut échouer.

Dans la section Cellular, cliquez sur l'icône **Tower** en haut à droite.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Les antennes relais disponibles s'afficheront.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Cliquez sur une antenne relais pour afficher les détails et la verrouiller.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

L'état de l'antenne relais (par exemple Locked/Unlocked) s'affichera en haut.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Remarque** : 

1. Il se peut que l'appareil ne puisse pas analyser toutes les antennes relais lorsque l'interface Cellular est activée.

2. Si l'antenne relais verrouillée ne correspond pas aux paramètres de masquage de bandes ou d'APN définis dans vos paramètres cellulaires, le routeur ne pourra pas se connecter au réseau cellulaire.

3. Après avoir verrouillé une antenne relais, si vous déplacez le routeur vers un autre emplacement, il tentera toujours de se reconnecter à l'antenne relais verrouillée après redémarrage. Cela peut empêcher le routeur de se connecter automatiquement au réseau cellulaire dans le nouvel emplacement. Dans ce cas, vous devrez soit déverrouiller l'antenne relais actuelle, soit la verrouiller manuellement sur une nouvelle antenne relais.

## Historique du signal

Dans la section Cellular, cliquez sur l'icône **Signal** en haut à droite pour consulter l'historique de la puissance du signal.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Cela vous aide à évaluer la qualité de votre connexion cellulaire. Si le signal est faible, essayez de changer d'antenne relais pour obtenir un meilleur signal.

Vous pouvez afficher l'historique de la puissance du signal cellulaire en sélectionnant différentes plages de temps.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Masquage de bandes

Dans la section Cellular, cliquez sur **View More** et sélectionnez **Cells Info** pour vérifier les détails des cellules.

Vous verrez les bandes actuellement utilisées ainsi que l'état de leur signal.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Si le signal est faible, vous pouvez activer le masquage de bandes pour bloquer certaines bandes. À l'inverse, si le signal est bon, vous pouvez autoriser le routeur à utiliser uniquement certaines bandes cellulaires.

Cliquez sur **Manual Setup** pour accéder à la page Cellular Settings, puis activez **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Sélectionnez le **Masking Mode** (Block ou Open), puis choisissez les bandes LTE, les bandes 5G NSA et les bandes 5G SA.

## Dépannage

Si vous ne parvenez pas à établir une connexion cellulaire, cliquez sur le message d'erreur ci-dessous pour consulter les solutions correspondantes.

??? note "No SIM / Your SIM card has not been detected"
    
    1. Actualisez la page et attendez quelques minutes pour vérifier si la carte SIM peut être détectée.
    
    2. Assurez-vous que la carte SIM est correctement installée. Alignez l'encoche de la carte SIM avec le repère correspondant sur le logement afin de confirmer l'orientation d'insertion correcte.
    
    3. Éteignez le routeur, retirez puis réinsérez la carte SIM, puis rallumez le routeur.
    
    4. Essayez une autre carte SIM si possible.

    Si le problème persiste, téléchargez les journaux et envoyez-les à [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Actualisez la page et attendez quelques minutes pour vérifier si l'erreur disparaît.
    
    2. Cliquez sur **Disconnect**/**Abort**, puis sur **Connect** pour réessayer la connexion.
    
    3. Redémarrez le routeur.
    
    4. Vérifiez l'état de la carte SIM et assurez-vous qu'elle est activée. Testez la carte SIM en l'insérant dans un smartphone pour confirmer qu'elle peut accéder normalement à Internet avec un forfait de données mobiles actif, ou contactez votre opérateur réseau pour vérification.
    
    5. Certains opérateurs peuvent exiger un protocole 3G pour la connexion réseau. Accédez à **Manual Setup** -> **Cellular Settings** -> **Protocol**, sélectionnez **3G**, puis cliquez sur **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        L'appareil se reconnectera automatiquement. Attendez quelques minutes pour vérifier si la connexion aboutit.

    6. Certaines cartes SIM peuvent avoir des restrictions d'utilisation spécifiques (par exemple, exiger un APN particulier). Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. 
    
        Si nécessaire, accédez à **Manual Setup** -> **Cellular Settings** -> **APN**, configurez l'APN correct sur le routeur, puis cliquez sur **Apply**.

    7. Cliquez sur **View More** et sélectionnez **Cells Info** pour vérifier la puissance du signal cellulaire. Si le signal est faible, assurez-vous que l'antenne est correctement installée. Déplacez le routeur vers un emplacement dégagé et sans obstacle afin d'améliorer la réception du signal.
    
    8. Vérifiez si **Band Masking** ou **Lock Tower** est activé. Si c'est le cas, désactivez la fonctionnalité et réessayez de vous connecter.

    Si le problème persiste, téléchargez les journaux et envoyez-les à [support@gl-inet.com](mailto:support@gl-inet.com).

## Certification IoT

### Certification AT&T

Cliquez sur le lien [att device certification](https://iotdevices.att.com/certified-devices.aspx#) et saisissez le nom de l'appareil pour le trouver. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Certification T-Mobile

Cliquez sur le lien [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) et choisissez 5G dans **Filter** pour le trouver. 

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Articles connexes

- [Page Internet](internet.md)
- [Comment définir la priorité de chaque méthode d'accès à Internet ?](multi-wan.md)
- [Comment définir l'équilibrage de charge lorsque plusieurs méthodes d'accès à Internet sont utilisées en même temps ?](multi-wan.md)

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
