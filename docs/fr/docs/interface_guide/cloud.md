# GL.iNet GoodCloud

## Sommaire

- [Présentation](#introduction)
- [Lier des appareils à GoodCloud](#bind-devices-to-goodcloud)
    - [Pour le firmware v4.6 ou antérieur](#for-firmware-v46-or-earlier)
        - [Activer GoodCloud](#enable-goodcloud)
        - [Créer un compte](#sign-up-an-account)
        - [Ajouter des appareils](#add-devices)
        - [Détails de l’association](#binding-details)
        - [Dissocier un appareil](#unbind-device)
    - [Pour le firmware v4.7 ou ultérieur](#for-firmware-v47-or-later)
        - [Activer Cloud Service](#enable-cloud-service)
        - [Détails de l’association](#binding-details_1)
        - [Dissocier un appareil](#unbind-device_1)
- [Gérer les appareils](#manage-devices)
    - [Informations système et actions](#system-info-and-actions)
    - [Détails de l’appareil](#device-details)
        - [Informations de base](#basic-info)
        - [Statistiques](#statistics)
        - [Paramètres réseau](#network-settings)
        - [Liste des clients](#clients-list)
- [Accès à distance](#remote-access)
    - [GUI à distance](#remote-gui)
    - [SSH à distance](#remote-ssh)
- [Modifier les paramètres](#modify-settings)
- [Alertes par e-mail](#email-alarm)
- [Site à site](#site-to-site)
- [GoodCloud et VPN](#goodcloud-and-vpn)
- [Afficher les journaux](#view-logs)
- [Désactiver le cloud](#disable-cloud)
- [Supprimer le compte](#delete-account)

## Présentation {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} est une plateforme conçue pour simplifier le déploiement et la gestion à distance des appareils connectés. Elle offre un moyen simple d’accéder à distance aux routeurs GL.iNet et de les administrer. En centralisant les équipements réseau dans le cloud, les utilisateurs peuvent effectuer efficacement des tâches de gestion par lot, telles que le déploiement de configurations réseau et les mises à niveau logicielles. Ils peuvent également accéder à distance au panneau d’administration web du routeur ou se connecter au terminal du routeur via SSH, pour une gestion des équipements réseau de bout en bout et entre différentes régions.

Avec GoodCloud, vous pouvez :

1. Vérifier l’état du routeur en temps réel
    - Surveiller l’état en ligne/hors ligne
    - Consulter l’utilisation de la RAM et la charge moyenne en temps réel
    - Recevoir des alertes par e-mail lors des changements d’état en ligne/hors ligne

2. Configurer des routeurs à distance
    - configurer les paramètres du routeur (par exemple le SSID et le mot de passe)
    - Accès SSH à distance
    - Accès à distance au WebUI
    - Partager l’accès au routeur avec d’autres personnes

3. Surveiller les clients connectés à distance
    - Voir les appareils connectés à votre réseau
    - Surveiller le trafic en temps réel et bloquer des clients
    - Recevoir des alertes par e-mail pour les nouvelles connexions et les événements de blocage

4. Effectuer des opérations par lot
    - Redémarrage par lot
    - Mise à niveau du firmware par lot

5. Établir une connectivité site à site
    - Bureau virtuel : étendre votre réseau de bureau à d’autres agences
    - Déplacements professionnels : accéder à distance aux systèmes du bureau (par ex. OA, CRM, MySQL)
    - Maison connectée : accéder à distance aux appareils de la maison (par ex. caméras IP, NAS)

Si vous devez gérer plusieurs appareils et débloquer des fonctionnalités avancées comme les opérations groupées, la gestion multi-comptes et des solutions personnalisées, choisissez nos forfaits à valeur ajoutée. Cliquez [ici](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} pour plus de détails, et n’hésitez pas à contacter [support@glinet.biz](mailto:support@glinet.biz).

## Lier des appareils à GoodCloud {#bind-devices-to-goodcloud}

Pour connecter correctement des appareils à la plateforme cloud, veuillez suivre la procédure d’association correspondant à votre version du firmware.

### Pour le firmware v4.6 ou antérieur {#for-firmware-v46-or-earlier}

#### Activer GoodCloud {#enable-goodcloud}

Connectez-vous au panneau d’administration web de votre routeur, puis allez à **APPLICATIONS** -> **GoodCloud**. Activez le commutateur pour activer GoodCloud.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

Activez **Remote SSH** et **Remote Web Access** selon vos besoins, sélectionnez le serveur le plus proche, lisez et acceptez les **Terms of Service & Privacy Policy**, puis cliquez sur **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH** : permet d’accéder à distance au terminal du routeur via GoodCloud.

- **Remote Web Access** : permet d’accéder à distance au panneau d’administration web du routeur via GoodCloud.

- **Data Server** : choisissez le serveur le plus proche de l’emplacement de votre appareil. Trois options sont disponibles : Asia Pacific (Japan), America (Oregon) et Europe (Ireland).

#### Créer un compte {#sign-up-an-account}

Rendez-vous sur le [site GoodCloud](https://www.goodcloud.xyz){target="_blank"} pour créer un compte, puis connectez-vous.

Si vous ne recevez pas l’e-mail de vérification, consultez votre dossier spam ou attendez quelques minutes avant de réessayer. Pour toute difficulté lors de l’inscription, envoyez un e-mail à [support@glinet.biz](mailto:support@glinet.biz).

#### Ajouter des appareils {#add-devices}

Sur la plateforme cloud, allez à **Devices** -> **Bound Devices** -> **Add Devices**.

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

Il existe trois méthodes pour lier un appareil à votre compte GoodCloud : Auto Discover, Manually Add et Bulk Import.

??? "Auto Discover"

    Vous pouvez essayer **Auto discover** si votre routeur et l’appareil utilisé pour accéder au site GoodCloud se trouvent sur le même réseau.
    
    Sélectionnez votre appareil dans la liste déroulante, puis saisissez le **DDNS / Device ID**, que vous trouverez au bas de votre routeur ou sur la page GoodCloud du panneau d’administration web.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Veuillez consulter [ce lien](../faq/where_to_find_the_device_id_mac_sn.md) pour savoir où trouver le Device ID.

??? "Manually Add"

    Si votre appareil n’apparaît pas dans la liste, cliquez sur **Manually add** et saisissez les informations de votre routeur. Toutes les informations demandées se trouvent au bas du routeur ou sur la page GoodCloud du panneau d’administration web.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** est conçu pour les utilisateurs qui gèrent un grand nombre d’appareils. Vous pouvez importer plusieurs appareils via un fichier Microsoft Excel.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Détails de l’association {#binding-details}

Après une association réussie, reconnectez-vous au panneau d’administration web du routeur, puis allez à **APPLICATIONS** -> **GoodCloud**. Actualisez cette page : elle affichera alors le nom d’utilisateur GoodCloud associé ainsi que la date d’association.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Dissocier un appareil {#unbind-device}

Si vous souhaitez dissocier votre routeur, connectez-vous au panneau d’administration web du routeur, allez à **APPLICATIONS** -> **GoodCloud** et cliquez sur **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Vous pouvez également supprimer l’appareil correspondant de la Bound Devices List sur la plateforme GoodCloud. Le panneau d’administration web du routeur se synchronisera ensuite pour refléter l’état d’association le plus récent.

Pour toute difficulté, envoyez un e-mail à [support@glinet.biz](mailto:support@glinet.biz).

### Pour le firmware v4.7 ou ultérieur {#for-firmware-v47-or-later}

#### Activer Cloud Service {#enable-cloud-service}

Connectez-vous au panneau d’administration web de votre routeur, puis allez à **CLOUD SERVICE** -> **GoodCloud**.

Cliquez sur le bouton **Get Started** ; une fenêtre contextuelle Cloud Service apparaîtra dans le coin supérieur droit. Cliquez sur **Enable** pour utiliser Cloud Service.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Connectez-vous à votre compte GoodCloud.

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

Si vous n’avez pas encore de compte, créez-en un puis connectez-vous. Une fois l’inscription terminée, le routeur sera automatiquement associé à ce compte.

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

Si vous ne recevez pas l’e-mail de vérification, consultez votre dossier spam ou attendez quelques minutes avant de réessayer. Pour toute difficulté lors de l’inscription, envoyez un e-mail à [support@glinet.biz](mailto:support@glinet.biz).

#### Détails de l’association {#binding-details_1}

Après une association réussie, reconnectez-vous au panneau d’administration web du routeur, cliquez sur l’icône cloud en haut à droite, et vous verrez les détails de l’association, notamment le nom d’utilisateur GoodCloud associé et la date, le Device ID, le Device MAC et le Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

Dans le panneau d’administration web, allez à **CLOUD SERVICES** -> **GoodCloud** ; vous pourrez y activer ou désactiver l’accès à distance pour votre routeur.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH** : permet d’accéder à distance au terminal du routeur via GoodCloud.

- **Remote Web Access** : permet d’accéder à distance au panneau d’administration web du routeur via GoodCloud.

- **View Logs** : affiche les journaux d’appels API effectués par GoodCloud.

#### Dissocier un appareil {#unbind-device_1}

Si vous souhaitez dissocier votre routeur, connectez-vous au panneau d’administration web du routeur. Cliquez sur l’icône cloud en haut à droite, puis sur **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Vous pouvez également supprimer l’appareil correspondant de la Bound Devices List sur la plateforme GoodCloud. Le panneau d’administration web du routeur se synchronisera ensuite pour refléter l’état d’association le plus récent.

Pour toute difficulté, envoyez un e-mail à [support@glinet.biz](mailto:support@glinet.biz).

## Gérer les appareils {#manage-devices}

### Informations système et actions {#system-info-and-actions}

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, vous pouvez consulter les informations système (par ex. modèle, version, adresse MAC, adresse IP) et l’état (par ex. en ligne, hors ligne) de tous les appareils associés à votre compte.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Sélectionnez un appareil, puis utilisez les actions disponibles dans le coin supérieur droit, comme modifier les paramètres, mettre à jour le firmware, accéder à distance à l’appareil, redémarrer ou réinitialiser.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Cliquez sur l’icône d’engrenage à l’extrémité droite de l’en-tête de la liste pour personnaliser l’affichage des colonnes ainsi que leur ordre, afin de mettre en avant les informations les plus importantes pour vous.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Détails de l’appareil {#device-details}

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, cliquez sur le nom d’un appareil pour être redirigé vers la page de détails, qui affiche notamment les informations de base du routeur, les données statistiques, les paramètres réseau et la liste des clients.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Informations de base {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistiques {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Paramètres réseau {#network-settings}

Cette page affiche la configuration réseau de votre routeur ainsi que ses paramètres Wi-Fi.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Liste des clients {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Accès à distance {#remote-access}

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, cliquez sur le nom de l’appareil auquel vous souhaitez accéder pour ouvrir la page de détails ; vous verrez ensuite les actions à distance dans le coin supérieur droit.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### GUI à distance {#remote-gui}

Cliquez sur **Remote GUI** pour accéder à distance au panneau d’administration web de votre routeur.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Si cette option est grisée ou indisponible, il est probable que cette fonctionnalité soit désactivée. Activez-la d’abord dans le panneau d’administration web du routeur avant d’y accéder via GoodCloud.

Si cette option est cliquable mais ne répond pas, essayez le mode navigation privée/incognito de votre navigateur.

### SSH à distance {#remote-ssh}

Cliquez sur **Remote SSH** pour accéder à distance au terminal de votre routeur via SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Si cette option est grisée ou indisponible, il est probable que cette fonctionnalité soit désactivée. Activez-la d’abord dans le panneau d’administration web du routeur avant d’y accéder via GoodCloud.

Si cette option est cliquable mais ne répond pas, essayez le mode navigation privée/incognito de votre navigateur.

## Modifier les paramètres {#modify-settings}

Vous pouvez configurer plusieurs paramètres pour un seul appareil ou pour plusieurs appareils.

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, sélectionnez l’appareil que vous souhaitez configurer puis, dans le coin supérieur droit, cliquez sur **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Vous pouvez y consulter et modifier les paramètres réseau du routeur, notamment les réglages sans fil, Ethernet, de sécurité, de redirection de port, du LAN et du système.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Alertes par e-mail {#email-alarm}

Vous pouvez configurer une alerte par e-mail lorsque l’état de l’appareil change (en ligne/hors ligne) ou lorsqu’un nouveau client se connecte.

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications**, cliquez sur le bouton **Add Rule** dans le coin supérieur droit.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Sélectionnez l’appareil à surveiller, puis cliquez sur **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Sélectionnez l’événement déclencheur, comme l’état en ligne/hors ligne de l’appareil, puis cliquez sur **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Vérifiez les paramètres de la règle, puis cliquez sur **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Dans la liste Notifications, vous pouvez consulter les règles d’alerte que vous avez créées. Chaque utilisateur ne peut créer qu’une seule règle d’alerte. Si vous avez besoin d’une gestion groupée des appareils, n’hésitez pas à nous contacter pour faire évoluer votre forfait.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site à site {#site-to-site}

Veuillez consulter [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud et VPN {#goodcloud-and-vpn}

Si vous activez **GoodCloud** et le **client VPN** en même temps sur votre routeur, la connexion entre le routeur et le serveur GoodCloud ne passera pas par le VPN par défaut. Cela garantit une connexion plus stable aux services GoodCloud.

Cependant, si vous souhaitez que la connexion GoodCloud passe par le VPN, vous pouvez modifier ce paramètre dans le panneau d’administration web du routeur. Allez à **VPN** -> **VPN Dashboard** -> **VPN Client** -> **Options**, puis activez l’option **Services from GL.iNet Use VPN**.

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Notez que faire passer GoodCloud par le VPN peut affecter la stabilité de la connexion cloud, en particulier si :

* la connexion VPN est instable
* le fournisseur VPN filtre ou bloque le trafic GoodCloud
* le VPN ajoute une latence importante à la connexion

Il est généralement recommandé de conserver les paramètres par défaut, dans lesquels GoodCloud contourne le VPN, afin d’obtenir les meilleures performances et la meilleure fiabilité.

## Afficher les journaux {#view-logs}

Vous pouvez consulter les journaux GoodCloud selon vos besoins, notamment Activity Logs, Device Logs, Upgrade Logs, Alert Logs et Device Settings Logs.

Sur [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs**, sélectionnez les journaux que vous souhaitez afficher dans la liste déroulante.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Désactiver le cloud {#disable-cloud}

Si vous ne souhaitez plus que votre appareil soit connecté à la plateforme cloud, vous pouvez désactiver le service cloud dans le panneau d’administration web du routeur.

??? "Pour le firmware v4.6 ou antérieur"

    Connectez-vous au panneau d’administration web de votre routeur, allez à **APPLICATIONS** -> **GoodCloud**, désactivez le commutateur GoodCloud, puis cliquez sur **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Une fois désactivé, l’interface s’affichera comme suit.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Pour le firmware v4.7 ou ultérieur"

    Connectez-vous au panneau d’administration web de votre routeur, puis cliquez sur l’icône cloud en haut à droite.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Une fois désactivé, l’interface s’affichera comme suit.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Supprimer le compte {#delete-account}

Pour des raisons de sécurité, vous pouvez supprimer votre compte s’il n’est plus utilisé.

Sur la plateforme [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, cliquez sur le nom d’utilisateur en haut à droite puis sélectionnez **Personal Center**. Faites défiler jusqu’en bas de la page et cliquez sur **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    La suppression effacera définitivement tous les services, données et informations personnelles associés, sans possibilité de récupération.
    
    Si votre compte appartient à une organisation, veuillez d’abord quitter toutes les organisations avant de supprimer votre compte.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
