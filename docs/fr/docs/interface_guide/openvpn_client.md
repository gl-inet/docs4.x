# Configurer le client OpenVPN sur les routeurs GL.iNet {#setup-openvpn-client}

OpenVPN est un protocole VPN open source qui utilise des techniques de réseau privé virtuel pour établir des connexions sécurisées site à site ou point à point.

Pour configurer le client OpenVPN sur un routeur GL.iNet, regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Avant de commencer, assurez-vous de disposer d'un abonnement actif auprès d'un fournisseur de services VPN prenant en charge la configuration manuelle OpenVPN. Cliquez [ici](https://www.gl-inet.com/solutions/vpn/){target="_blank"} pour consulter les fournisseurs OpenVPN compatibles avec GL.iNet.

En général, vous devez d'abord visiter le site officiel du fournisseur de services VPN auquel vous êtes abonné, obtenir le fichier de configuration, puis l'importer dans le routeur afin de le configurer comme client OpenVPN. Si vous ne savez pas comment obtenir le fichier de configuration, consultez [ce lien](#get-configuration-files-from-openvpn-service-providers) ou contactez leur assistance.

Vous pouvez configurer un client OpenVPN via le panneau d'administration web ou l'[application mobile](../faq/mobile_app.md). Les étapes ci-dessous décrivent la configuration via le panneau d'administration web.

---

Dans le panneau d'administration web, accédez à **VPN** -> **OpenVPN Client**. 

Si vous avez un abonnement NordVPN, cliquez sur **NordVPN** pour vous connecter ; sinon, cliquez sur **Add Manually** pour importer les fichiers de configuration OpenVPN.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Configurer NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} est un service VPN en ligne populaire pour sa rapidité et sa sécurité.

La configuration rapide de NordVPN est intégrée au panneau d'administration des routeurs GL.iNet. Vous pouvez récupérer en ligne les fichiers de configuration de tous les serveurs NordVPN en saisissant les identifiants de votre compte (obtenus depuis le NordVPN Dashboard) dans le panneau d'administration web ou l'application mobile du routeur, sans avoir à importer les fichiers manuellement.

1. Connectez-vous à votre compte web NordVPN [ici](https://my.nordaccount.com/){target="_blank"}.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    Après la connexion, dans le Nord Dashboard, cliquez sur **NordVPN**, puis sur **Set up NordVPN manually**.

    ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Vous y trouverez les **service credentials**. Copiez-les pour les utiliser plus tard.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Connectez-vous au panneau d'administration web de votre routeur, accédez à VPN -> OpenVPN Client -> NordVPN. Saisissez les **service credentials** obtenus à l'étape 1 (remarque : ce ne sont **PAS** l'adresse e-mail et le mot de passe du compte de connexion), puis cliquez sur **Save and Continue**.
   
    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Sélectionnez le protocole, le nombre maximal de serveurs pour chaque emplacement ainsi que les emplacements, puis cliquez sur **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    Les fichiers de configuration seront téléchargés.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Démarrez une connexion.

    Sélectionnez le serveur souhaité, puis cliquez sur l'icône à trois points à droite pour lancer la connexion.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Une fois connecté, un point vert apparaît à côté du fichier de configuration.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Les détails de la connexion VPN s'affichent également dans **VPN Dashboard**.

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Mettre à jour les serveurs.

    Vous pouvez cliquer sur **Update Servers** pour récupérer la liste la plus récente des serveurs disponibles et éviter les échecs de connexion dus à la maintenance ou à l'arrêt de certains serveurs.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Modifier les identifiants.

    Cliquez sur l'icône d'engrenage pour modifier vos identifiants de connexion.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Supprimer tous les fichiers.

    Vous pouvez cliquer sur **Delete All** pour supprimer tous les fichiers de configuration en un seul clic.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Configurer manuellement le client OpenVPN (pour les autres fournisseurs) {#set-up-openvpn-client-manually-for-other-providers}

Si votre fournisseur de services OpenVPN n'est pas intégré à notre panneau d'administration, visitez d'abord le site officiel du fournisseur auquel vous êtes abonné afin d'obtenir le fichier de configuration. Importez-le ensuite dans le routeur pour configurer un client OpenVPN.

Dans les étapes suivantes, nous utiliserons [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} comme exemple.

1. Téléchargez un fichier de configuration depuis le site officiel de Private Internet Access.

2. Connectez-vous au panneau d'administration web de votre routeur, accédez à VPN -> OpenVPN Client, puis cliquez sur **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. Cela créera un groupe dans la barre latérale gauche.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Définissez un nom descriptif pour le groupe (par exemple, private internet access).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Importez votre fichier de configuration OpenVPN. Saisissez les identifiants si nécessaire, puis cliquez sur **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - Il existe 4 types d'identifiants pour l'authentification :

        1. Aucune authentification.
        
        2. Nom d'utilisateur et mot de passe uniquement. 
        
        3. Phrase secrète uniquement.

        4. Nom d'utilisateur, mot de passe et phrase secrète.

    Le fichier de configuration importé s'affichera ensuite.
     
    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Cliquez sur l'icône à trois points à droite pour démarrer une connexion.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Une fois connecté, un point vert apparaît à côté du fichier de configuration.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    Les détails de la connexion VPN s'affichent également dans **VPN Dashboard**.

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## Configurer le serveur OpenVPN sur un routeur GL.iNet

Si vous possédez deux routeurs GL.iNet, vous pouvez envisager d'en configurer un comme serveur OpenVPN (une adresse IP publique est requise) et l'autre comme client OpenVPN. Vous pouvez ainsi établir votre propre connexion VPN sans vous abonner à des services VPN tiers.

Pour configurer un serveur OpenVPN, consultez [ici](openvpn_server.md).

## Obtenir les fichiers de configuration auprès de fournisseurs de services OpenVPN {#get-configuration-files-from-openvpn-service-providers}

Nous avons testé plus de 30 fournisseurs de services OpenVPN et documenté les étapes nécessaires pour obtenir leurs fichiers de configuration. Si vous ne savez pas comment récupérer le fichier de configuration, reportez-vous aux étapes ci-dessous.

Si le fournisseur auquel vous êtes abonné n'est pas listé ci-dessous, veuillez contacter son assistance pour obtenir de l'aide.

??? "NordVPN"
    ### NordVPN

    [Site officiel](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Connectez-vous à votre compte NordVPN**

        Connectez-vous au [site officiel](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}, puis accédez au Nord Account Dashboard, où vous trouverez les service credentials.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Après vous être connecté au Nord Dashboard, cliquez sur NordVPN à gauche, puis sur **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Recherchez les **Service credentials**. Copiez-les si vous devez les utiliser pour importer la configuration.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Choisissez un serveur NordVPN et téléchargez le fichier de configuration**

        Accédez à l'onglet **Server recommendation**. Il recommandera un serveur en fonction de votre réseau et proposera les protocoles disponibles au téléchargement. Cliquez sur **Get setup configuration** pour continuer.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        Dans la fenêtre contextuelle, sélectionnez le protocole **OpenVPN** et téléchargez la configuration UDP ou TCP. 

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Vous pouvez télécharger les configurations de tous les serveurs [ici](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

    [Lien de référence](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Vous pouvez également utiliser l'[application mobile](../faq/mobile_app.md) pour configurer NordVPN.

??? "AirVPN"
    ### AirVPN

    [Site officiel](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Connectez-vous à votre compte AirVPN

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Choisissez Config Generator dans la colonne de gauche, puis sélectionnez Linux comme système d'exploitation. Ensuite, choisissez le serveur de votre choix.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Vous accéderez à la page de téléchargement du fichier de configuration.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Site officiel](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Informations extraites des [instructions officielles d'Astrill](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Générez et téléchargez le fichier ZIP de configuration OpenVPN d'Astrill

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Saisissez une description, par exemple OPENVPN_GUI.

    3. Cliquez sur le bouton ADD to my certificates.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Une fois le certificat OpenVPN ajouté, cliquez sur le bouton Download.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Site officiel](https://www.bolehvpn.net/){target="_blank"}

    Connectez-vous au [Dashboard](https://users.bolehvpn.net/){target="_blank"}, téléchargez vos fichiers de configuration et sélectionnez le format [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Extrayez les fichiers zip une fois le téléchargement terminé.

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

    [Lien de référence](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Site officiel](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Téléchargement direct](https://www.cactusvpn.com/downloads/).

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Site officiel](https://cryptostorm.is/){target="_blank"}

    [Téléchargement direct](https://cryptostorm.is/configs/ecc/).

??? "CyberGhost"
    ### CyberGhost

    [Site officiel](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Informations extraites des [instructions officielles de CyberGhost](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Connectez-vous à votre compte CyberGhost VPN en ligne.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Sélectionnez "**VPN**" dans le menu de gauche, puis cliquez sur "**Configure Device**" et créez votre configuration de serveur comme indiqué ci-dessous :

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Créez ensuite votre configuration de serveur comme indiqué ci-dessous :

        * **Protocol** : **OpenVPN**
        * **Country** : comme les connexions via les protocoles natifs ne peuvent être utilisées qu'avec un seul serveur précis, vous devez choisir le pays depuis lequel vous souhaitez naviguer ; le serveur à utiliser dans ce pays sera choisi automatiquement par CyberGhost.
        * **Server group** : choisissez le groupe de serveurs et le protocole OpenVPN (UDP ou TCP) à utiliser

        **OpenVPN UDP** offre une vitesse plus élevée que la version TCP, mais peut entraîner des téléchargements corrompus dans certains cas. C'est le réglage par défaut.
        
        **OpenVPN TCP** offre des connexions plus stables que la version UDP, mais il est un peu plus lent. Choisissez cette version si vous rencontrez des problèmes de connexion récurrents, comme des déconnexions soudaines.

        Une fois les paramètres souhaités choisis, enregistrez-les avec **Save Configuration**.

    4. Pour afficher les identifiants **OpenVPN** générés pour vous sur le tableau de bord de configuration, cliquez sur **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Après avoir défini vos préférences de connexion, veuillez prendre note des points suivants :

        * **Server Group** : il s'agit de l'adresse du pays (serveur) auquel vous souhaitez vous connecter, par exemple '12345-1-ca.cg-dialup.net'. Cette adresse change à chaque fois que vous choisissez un autre pays à l'étape précédente. Le serveur réel utilisé sera sélectionné automatiquement par CyberGhost.
        * **Username** : nom d'utilisateur généré spécifiquement pour ce protocole. Ce n'est **PAS** votre nom d'utilisateur habituel du compte CyberGhost ; il sert uniquement à l'authentification auprès des serveurs CyberGhost via les configurations manuelles. Vous en aurez besoin pour configurer OpenVPN sur les routeurs GL.iNet.
        * **Password** : mot de passe généré spécifiquement pour l'utilisation de ce protocole. Ce n'est **PAS** votre mot de passe habituel du compte CyberGhost ; il sert uniquement à l'authentification auprès des serveurs CyberGhost via les configurations manuelles. Vous en aurez besoin pour configurer OpenVPN sur les routeurs GL.iNet.

        Une fois cela fait, téléchargez le fichier de configuration. Pour cela, cliquez sur *Download Configuration* afin de télécharger le fichier de configuration sur votre ordinateur.

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Site officiel](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Informations extraites des [instructions officielles d'Expressvpn](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Accédez au site [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} et connectez-vous avec vos identifiants ExpressVPN.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Saisissez le code de vérification** envoyé à votre adresse e-mail.

    2. Dans la section "Set up your devices", cliquez sur **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Cliquez sur **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Vous verrez votre **username**, votre **password** et une liste de **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Cliquez sur l'emplacement ou les emplacements souhaités afin de télécharger le ou les fichiers .ovpn.

        **Gardez cette fenêtre du navigateur ouverte**. Vous aurez besoin de ces informations plus tard lors de la configuration.

    [Lien de référence](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Site officiel](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Téléchargez le dossier zip des fichiers de configuration FastestVPN pour OpenVPN TCP et UDP [ici](https://support.fastestvpn.com/download/fastestvpn_ovpn/).

    Conseil : si le fichier zip est trop volumineux à importer, supprimez certains fichiers .ovpn du dossier .zip ou importez un seul fichier .ovpn.

    [Lien de référence](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Site officiel](https://www.finchvpn.com/){target="_blank"}

    1. Connectez-vous à votre compte FinchVPN.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Accédez à la page Download, puis cliquez sur Download sous FinchVPN OpenVPN Config.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Choisissez Linux.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Choisissez le protocole selon vos préférences. En général, vous pouvez choisir la première option : **Port 8484 over UDP**

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. N'oubliez pas de cocher la case permettant d'inclure votre nom d'utilisateur et votre mot de passe avant de télécharger le fichier.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Site officiel](https://www.hideipvpn.com/){target="_blank"}

    1. Connectez-vous à votre compte HideIPVPN.

    2. Accédez à Package dans la colonne de gauche, cliquez sur votre forfait et assurez-vous qu'il est actif.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Dans l'onglet VPN, vous trouverez les VPN Login Details, c'est-à-dire le nom d'utilisateur et le mot de passe utilisés lors de la connexion OpenVPN

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Faites défiler la page vers le bas pour télécharger les fichiers de configuration OpenVPN.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Site officiel](https://hide.me/?friend=glinet){target="_blank"}

    1. Connectez-vous à votre compte Hide.me et trouvez Server Locations dans la colonne de gauche.

    2. Téléchargez la configuration OpenVPN pour Windows.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Site officiel](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Remarque : les fichiers de configuration Hotspot Shield Router ne sont plus disponibles ni pris en charge. Les étapes suivantes sont conservées uniquement à des fins historiques pour les utilisateurs qui pourraient encore avoir ces fichiers installés.**

    1. Accédez à [https://www.hotspotshield.com/](https://www.hotspotshield.com/) et cliquez sur Account. Connectez-vous si cela vous est demandé.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Accédez à [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)

        Ouvrez la liste déroulante Select location et choisissez l'emplacement virtuel que le routeur utilisera. Cliquez ensuite sur "Download file". Le fichier de configuration (config.ovpn) sera téléchargé sur votre ordinateur. Le nom d'utilisateur et le mot de passe devront être saisis lorsque vous configurerez le client OpenVPN sur le routeur.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Lien de référence](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Site officiel](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Vous pouvez télécharger tous les fichiers de configuration de tous les serveurs [ici](https://configs.ipvanish.com/configs/configs.zip), il contient tous les fichiers de configuration serveur (.ovpn) ainsi qu'un fichier certificat (.crt). Le fichier .zip peut être un peu volumineux pour certains modèles ; veuillez supprimer les configurations (.ovpn) des serveurs que vous n'utiliserez pas.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Vous pouvez également télécharger des fichiers de configuration serveur individuels [ici](https://www.ipvanish.com/software/configs/), mais vous devrez aussi télécharger **ca.ipvanish.com.crt**. Avant de les importer dans le routeur, vous devez compresser **ca.ipvanish.com.crt** et les fichiers de configuration .ovpn dans une archive .zip.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Lien de référence](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Site officiel](https://billing.ivacy.com/page/22852){target="_blank"}

    Pour configurer un client OpenVPN avec Ivacy, vous aurez besoin des éléments suivants : 

    - Votre nom d'utilisateur pour la configuration manuelle OpenVPN, affiché dans l'invite "Download Configuration"
     ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Votre mot de passe (identique à celui utilisé pour vous connecter à votre compte Ivacy)
    - Un fichier de configuration OpenVPN

    [Lien de référence](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Site officiel](https://www.ivpn.net/){target="_blank"}

    1. Téléchargez les [fichiers de configuration OpenVPN](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Recherchez l'Account ID dans l'[espace client IVPN](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Lorsque vous faites glisser le fichier de configuration dans Add a New OpenVPN Configuration, il vous sera demandé de saisir un User Name et un Password. Le User Name correspond à votre Account ID qui commence par les lettres **ivpn**. Le mot de passe peut être n'importe quoi, par exemple **ivpn**

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Lien de référence](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Site officiel](https://mullvad.net/en){target="_blank"}

    1. Accédez au site [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"} et connectez-vous avec vos identifiants Mullvad.

    2. Choisissez OpenVPN Configuration

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Choisissez **Linux** et sélectionnez l'emplacement de votre serveur

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Site officiel](https://www.ovpn.com/en?ref=glinet){target="_blank"}
    
    Connectez-vous simplement, puis vous pourrez facilement obtenir le fichier de configuration OpenVPN en cliquant sur le menu ci-dessous.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Choisissez ensuite le serveur et téléchargez-le.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Le nom d'utilisateur et le mot de passe sont les mêmes que ceux utilisés pour vous connecter à OVPN.

??? "OysterVPN"
    ### OysterVPN

    [Site officiel](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Accédez à [la page de liste des serveurs OysterVPN](https://support.oystervpn.com/server-list/){target="_blank"}, cliquez sur **Download .ovpn file** pour télécharger le fichier de configuration.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Le nom d'utilisateur et le mot de passe utilisés pour la connexion OpenVPN sont les mêmes que ceux de votre connexion OysterVPN.

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

??? "PIA (Private Internet Access)"
    ### PIA

    [Site officiel](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Téléchargement direct](https://www.privateinternetaccess.com/openvpn/openvpn.zip).

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Site officiel](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Connectez-vous simplement, puis vous trouverez facilement l'option **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

??? "PrivateVPN"
    ### PrivateVPN

    [Site officiel](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Téléchargement](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank} direct.

    [Ici](https://privatevpn.com/client/PrivateVPN-TUN.zip) se trouve le lien de téléchargement officiel. En raison d'un bug rencontré lors de l'importation sur le routeur, le nom de fichier interne contient des caractères spéciaux comme 'Bogotá'. Nous l'avons renommé et fourni le lien de téléchargement ci-dessus. Nous corrigerons ce bug dans les versions futures.

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

??? "Proton VPN"
    ### Proton VPN

    [Site officiel](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN propose aussi le service WireGuard ; nous vous recommandons d'utiliser WireGuard. Consultez [ici](wireguard_client.md#wireguard-providers)**.

    1. Connectez-vous à votre compte [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}.

    2. Cliquez sur **Download** dans la barre latérale gauche.

    3. Choisissez la plateforme Router, le protocole, etc., puis trouvez le pays cible pour télécharger le fichier de configuration.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. Les identifiants utilisés pour la connexion OpenVPN ne sont pas ceux du tableau de bord du site Proton. Vous trouverez ces identifiants dans **Account -> OpenVPN/IKEv2 username**

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Site officiel](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Pour configurer un client OpenVPN avec PureVPN, vous aurez besoin de votre nom d'utilisateur et de votre mot de passe OpenVPN ainsi que d'un fichier de configuration, que vous trouverez dans votre compte PureVPN. 
   
    1. [Connectez-vous à votre compte PureVPN.](https://my.purevpn.com/)
    2. Dans la barre latérale gauche, cliquez sur **Subscriptions**.
    3. Faites défiler la page vers le bas pour trouver votre nom d'utilisateur et votre mot de passe OpenVPN.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Dans la barre latérale gauche, cliquez sur **Manual Configuration**. 
    5. Sélectionnez un emplacement VPN, puis cliquez sur **Download** pour télécharger le fichier de configuration. 

    [Lien de référence](https://support.purevpn.com/openvpn-files)

    Les routeurs GL.iNet ne prennent pas en charge la fonctionnalité [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"} de PureVPN, car elle nécessite PPTP.

??? "SaferVPN"
    ### SaferVPN

    [Site officiel](https://safervpn.com/?a_aid=563){target="_blank"}

    [Téléchargement direct](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup).

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Site officiel](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN propose également le service WireGuard ; nous vous recommandons d'utiliser WireGuard. Consultez [ici](wireguard_client.md#starvpn).

    1. **Créer un compte StarVPN**

        Rendez-vous sur leurs options de [tarification](https://www.starvpn.com/#pricing){target="_blank"} et choisissez une offre VPN adaptée à vos besoins. Vous pouvez vous inscrire lors du paiement ou directement [ici](https://www.starvpn.com/dashboard/register.php){target="_blank"}

    2. Informations de connexion VPN

        Connectez-vous à l'espace membre StarVPN [dashboard](https://www.starvpn.com/dashboard){target="_blank"}. Vous pouvez trouver votre nom d'utilisateur et votre mot de passe VPN pour chaque slot dans la section Manage Slots ou dans la zone dashboard.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        Pour plusieurs slots, les paramètres de configuration VPN et les identifiants se trouvent dans la section “Manage Slots”.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. Télécharger le fichier de configuration OpenVPN

        À cette étape, vous devez télécharger les fichiers de configuration du serveur VPN nécessaires pour que le logiciel OpenVPN sache à quel serveur se connecter. Téléchargez le fichier de configuration depuis le dashboard de l'espace membre.

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        Certains routeurs GL.iNet ne prennent pas en charge IPv6 ni DNS Leak Protection ; vous pouvez donc rencontrer une erreur d'adresse IP ou de connexion. Modifiez le fichier de configuration ovpn et désactivez IPv6 en suivant ces étapes simples.

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}
        
??? "StreamVPN"
    ### StreamVPN

    [Site officiel](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Connectez-vous à votre compte [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"} puis vous pourrez voir les informations liées à votre abonnement. Cliquez sur **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Cliquez sur **VPN Router** ; une archive .zip nommée `StreamVPN.zip` sera téléchargée.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Remarque :** seules les configurations dont le nom de fichier contient "Primary" fonctionnent.

??? "StrongVPN"
    ### StrongVPN

    [Site officiel](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Connectez-vous à votre compte [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} puis vous verrez le récapitulatif des comptes VPN. Cliquez sur **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Recherchez la section de configuration manuelle et suivez les étapes pour obtenir la configuration.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Site officiel](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Trouvez vos informations de connexion**

        Les service credentials de Surfshark sont différents des identifiants de votre compte Surfshark, à savoir votre adresse e-mail et votre mot de passe. Vous aurez besoin des service credentials Surfshark pour vous connecter au VPN en utilisant la méthode de configuration manuelle OpenVPN sur le routeur.

        Connectez-vous au [site officiel](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, puis accédez à [cette page](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, où vous trouverez toutes les informations nécessaires pour une connexion manuelle.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Choisissez un serveur Surfshark**

        Sélectionnez l'onglet **Locations**, où vous verrez tous les serveurs Surfshark.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Il vous sera demandé de choisir TCP ou UDP. Cliquez [ici](../faq/openvpn_tcp_udp.md) pour voir la différence.

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Vous pouvez télécharger toutes les configurations [ici](https://api.surfshark.com/v1/server/configurations) directement.

    Conseil : si le fichier zip est trop volumineux à importer, vous pouvez supprimer certains fichiers .ovpn du fichier .zip ou importer un seul fichier .ovpn.

    [Lien de référence](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Site officiel](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Téléchargement](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Site officiel](https://www.vpngate.net/en/){target="_blank"}

    Les fichiers de configuration OpenVPN sont répertoriés sur le [site web VPN Gate](https://www.vpngate.net/en/) en fonction de l'emplacement du serveur.

    1. Cliquez sur OpenVPN Config file dans la colonne **OpenVPN**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Vous verrez alors la page de téléchargement.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Site officiel](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Informations extraites des [instructions officielles de VPN unlimited](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Commencez par vous connecter à votre espace utilisateur, cliquez sur Manage pour le service VPN Unlimited, puis suivez quelques étapes simples :

    1. Sélectionner un appareil

        Choisissez un appareil dans la liste ou créez-en un nouveau. Si vous n'avez plus de slots disponibles, supprimez un ancien appareil ou achetez des slots supplémentaires.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Choisir l'emplacement du serveur souhaité
    
        VPN Unlimited propose un grand nombre de serveurs : plus de 400 dans plus de 70 emplacements. Dans cet exemple, ce sera l'Allemagne.

    3. Sélectionner le protocole VPN

        Sélectionnez le protocole OpenVPN.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Créer une configuration

        Cliquez sur Generate et vous obtiendrez toutes les données nécessaires pour configurer une connexion VPN.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN propose les fichiers OpenVPN ici : [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Le fichier zip fourni contient deux dossiers avec les fichiers .ovpn : l'un nommé OpenVPN160 et l'autre OpenVPN256. Supprimez simplement le dossier OpenVPN160 du fichier zip, puis importez-le sur le routeur GL.iNet comme d'habitude.

??? "Windscribe"
    ### Windscribe

    [Site officiel](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Connectez-vous à votre compte membre Windscribe [ici](https://windscribe.com/login?auth_required){target="_blank"}, puis accédez à [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}. 
    
    2. Sélectionnez l'emplacement du serveur, le protocole (UDP/TCP), le port (par exemple 1194) que vous souhaitez utiliser, ainsi que la version OpenVPN (de préférence la plus récente), puis cliquez sur **Download Config**. Un fichier avec le suffixe ".ovpn" sera alors téléchargé sur votre appareil local.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Cliquez sur le bouton **Get Credentials** sur la même page. Vous recevrez alors les identifiants correspondants, qui seront ensuite utilisés dans le panneau d'administration web du routeur lors de l'importation du fichier de configuration dans le routeur pour l'authentification. Copiez les identifiants ou laissez cette page web ouverte.

    4. Suivez ensuite [ce guide](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers) pour continuer.

??? "ZoogVPN"
    ### ZoogVPN

    [Site officiel](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Connectez-vous à son [site officiel](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}, puis accédez à la [page des fichiers de configuration OpenVPN](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}. Vous y trouverez tous les serveurs. Téléchargez le fichier de configuration dans la colonne TCP ou UDP.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Suivez ensuite le [guide de configuration du client OpenVPN sur le routeur GL.iNet](#setup-openvpn-client) ; le nom d'utilisateur et le mot de passe sont les mêmes que ceux utilisés pour vous connecter au site web ZoogVPN.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
