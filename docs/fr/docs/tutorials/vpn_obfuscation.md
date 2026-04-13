# Comment configurer l’obfuscation VPN sur les routeurs GL.iNet

## Qu’est-ce que l’obfuscation VPN

L’obfuscation VPN est une technique qui déguise le trafic VPN pour le faire ressembler à du trafic Internet ordinaire. Cela aide les utilisateurs à contourner les restrictions réseau et la censure, en particulier dans les régions soumises à des politiques Internet strictes.

- Elle masque les caractéristiques du VPN afin d’empêcher sa détection par les FAI, les pare-feu ou l’inspection approfondie des paquets (DPI).

- Elle fait apparaître votre connexion VPN comme du trafic web standard, améliorant ainsi la stabilité et le taux de réussite de la connexion sur les réseaux restreints.

## Qu’est-ce qu’AmneziaWG

AmneziaWG est un protocole VPN basé sur WireGuard, avec une obfuscation du trafic intégrée. Il conserve les principaux avantages de WireGuard, tels que la vitesse élevée, la légèreté et la faible latence, tout en ajoutant un module d’obfuscation dédié. Ce module masque efficacement les modèles de trafic VPN, ce qui permet aux particuliers comme aux entreprises de protéger leur vie privée en ligne, de contourner les restrictions régionales et d’éviter les interruptions de connexion causées par des contrôles réseau stricts.

AmneziaWG est compatible avec un large éventail d’appareils, notamment Windows, macOS, iOS, Android, Linux et les routeurs, offrant des connexions VPN obfusquées fiables dans tous les scénarios.

Actuellement, plusieurs routeurs GL.iNet (par ex. **Brume 3**, **Flint 3**, **Flint 2** et **Beryl AX**) prennent en charge le protocole AmneziaWG dans certaines versions de firmware. La prise en charge officielle complète sera disponible avec le firmware ver.4.9 et sera progressivement déployée sur davantage de modèles.

## Configuration rapide

Vous trouverez ci-dessous deux scénarios courants pour configurer l’obfuscation VPN AmneziaWG sur les routeurs GL.iNet.

### Scénario 1. Utilisation de deux routeurs GL.iNet

Ce scénario utilise deux routeurs GL.iNet pour établir une connexion VPN obfusquée via le protocole AmneziaWG.

- **Brume 3 (GL-MT5000)** : utilisé comme serveur VPN domestique.
- **Beryl AX (GL-MT3000)** : utilisé comme client VPN portable pour les déplacements.

#### Configurer le serveur VPN

1. Connectez-vous au panneau d’administration web du Brume 3.

    Connectez un appareil (par ex. votre ordinateur portable ou PC) au port LAN du Brume 3 à l’aide d’un câble Ethernet. Ouvrez un navigateur et saisissez l’adresse d’administration par défaut (généralement `192.168.8.1`), puis connectez-vous avec votre mot de passe administrateur.

2. Terminez la configuration initiale du Brume 3 pour l’accès à Internet.

    Si le Brume 3 est utilisé comme routeur principal, connectez son port WAN au réseau amont, par exemple à un modem de FAI.

    S’il n’est pas le routeur principal (c’est-à-dire si un autre appareil en amont, comme un routeur de FAI, joue ce rôle), une configuration de redirection de port est requise sur votre routeur principal. Veuillez consulter [ce lien](how_to_set_up_port_forwarding.md).

3. Activez le DDNS (facultatif).

    Activez la fonction DDNS si votre IP publique est dynamique et non statique.

    Dans la barre latérale gauche, accédez à **APPLICATIONS** -> **Dynamic DNS**. Activez **Enable DDNS**, acceptez les **Terms of Service & Privacy Policy**, puis cliquez sur **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

4. Activez l’obfuscation VPN.

    Dans la barre latérale gauche, accédez à **VPN** > **WireGuard Server** -> onglet **Configurations**, activez **Enable Obfuscation**, puis cliquez sur **Apply**.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    Vous pouvez personnaliser les paramètres d’obfuscation selon vos besoins. Nous vous recommandons de conserver les réglages par défaut.

    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Exportez le fichier de configuration.

    Sur la page **WireGuard Server**, passez à l’onglet **Profiles**, puis cliquez sur le bouton **Add** pour créer un fichier de configuration permettant au Beryl AX de se connecter.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Définissez un nom explicite (par ex. Travel Router), puis cliquez sur **Apply**.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    Dans la fenêtre contextuelle, cliquez sur **Export** pour télécharger la configuration sur votre appareil local, afin de l’utiliser plus tard.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Démarrez le serveur VPN.

    En haut de la page **WireGuard Server**, cliquez sur le bouton **Start** pour lancer le serveur.

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    Votre serveur VPN avec obfuscation AmneziaWG est maintenant activé. Vous pouvez à présent vous connecter à ce serveur VPN Brume 3 via l’application AmneziaWG ou un routeur GL.iNet exécutant un firmware prenant en charge l’obfuscation AmneziaWG.

    **Remarque : les clients qui ne prennent pas en charge l’obfuscation AmneziaWG ne pourront pas se connecter.**

    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

#### Configurer le client VPN

1. Connectez-vous au panneau d’administration web du Beryl AX.

    Connectez un appareil (par ex. votre ordinateur portable ou PC) au Wi-Fi ou au port LAN du Beryl AX à l’aide d’un câble Ethernet. Ouvrez un navigateur et saisissez l’adresse d’administration par défaut (généralement `192.168.8.1`), puis connectez-vous avec votre mot de passe administrateur.

2. Terminez la configuration initiale du Beryl AX pour l’accès à Internet.

    **Conseil** : connectez le Beryl AX à un réseau différent de celui du Brume 3. Par exemple, vous pouvez activer un point d’accès mobile auquel le Beryl AX se connectera.

3. Téléversez le fichier de configuration.

    Dans la barre latérale gauche, accédez à **VPN** > **WireGuard Client**. Ajoutez un nouveau groupe et définissez un nom explicite (par ex. Home Router).

    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Téléversez le fichier de configuration précédemment exporté dans la partie droite.

    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Après avoir téléversé le fichier de configuration et validé la vérification, cliquez sur **Apply**.

    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    La page s’actualisera et un fichier de configuration apparaîtra dans la liste.

4. Démarrez la connexion VPN.

    Cliquez sur l’icône à trois points, puis sélectionnez **Start**.

    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Attendez environ 1 minute. Si l’indicateur d’état devient vert, cela signifie que la connexion VPN a réussi.

    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Accédez au **VPN Dashboard** ; vous verrez que le Beryl AX est connecté au routeur domestique Brume 3.

    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Double vérification (facultatif).

    Connectez-vous au panneau d’administration web du Brume 3, puis accédez à **VPN** -> **WireGuard Server**. Vous verrez également un client en ligne, à savoir le Beryl AX, actuellement connecté à ce serveur VPN Brume 3.

    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    La connexion VPN est terminée. Tous les appareils connectés au Beryl AX accèdent maintenant à Internet via la passerelle du Brume 3, ce qui permet une connexion VPN obfusquée.

### Scénario 2. Utilisation d’un seul routeur GL.iNet

Ce scénario utilise un seul routeur GL.iNet **Brume 3 (GL-MT5000)** comme client VPN pour se connecter à un serveur AmneziaVPN.

Dans ce cas, vous n’avez pas besoin de déployer votre propre serveur. Téléchargez simplement un fichier de configuration AmneziaWG depuis le [site officiel d’Amnezia](https://amnezia.org/){target="_blank"} ou depuis n’importe quel fournisseur de services VPN intégrant AmneziaWG, puis téléversez ce fichier sur votre routeur GL.iNet. Vous pourrez alors établir une connexion VPN avec obfuscation activée.

#### Télécharger la configuration

<u>Option 1</u> : télécharger une configuration depuis Amnezia Official (abonnement Premium requis).

1. Connectez-vous au [tableau de bord Amnezia Premium](https://cp.amnezia.org/en/login){target="_blank"} avec votre Subscription Key.

    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. Dans le tableau de bord Amnezia, accédez à **Connection Assets** -> **Configuration Files**, sélectionnez un pays et téléchargez un fichier de configuration sur votre appareil local pour l’utiliser plus tard.

    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Option 2</u> : télécharger une configuration depuis un autre fournisseur VPN qui intègre AmneziaWG.

Prenons StarVPN comme exemple.

1. Rendez-vous sur les [offres tarifaires](https://www.starvpn.com/#pricing){target="_blank"} de StarVPN et choisissez une offre VPN adaptée à vos besoins. Vous pouvez créer un compte StarVPN au moment du paiement ou directement [ici](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

2. Connectez-vous au [tableau de bord StarVPN](https://www.starvpn.com/dashboard){target="_blank"}, repérez la section **VPN Configuration** et cliquez sur **AmneziaWG Config** pour télécharger le fichier de configuration.

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. La configuration peut contenir une adresse IPv6. Pour éviter les problèmes de compatibilité et de connectivité, ouvrez le fichier `.conf` et supprimez l’adresse IPv6, comme indiqué ci-dessous.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Suivez ensuite les étapes ci-dessous pour configurer le client VPN.

#### Configurer le client VPN

1. Connectez-vous au panneau d’administration web du Brume 3.

    Connectez un appareil (par ex. votre ordinateur portable ou PC) au port LAN du Brume 3 à l’aide d’un câble Ethernet. Ouvrez un navigateur et saisissez l’adresse d’administration par défaut (généralement `192.168.8.1`), puis connectez-vous avec votre mot de passe administrateur.

2. Terminez la configuration initiale du Brume 3 pour l’accès à Internet.

3. Téléversez le fichier de configuration.

    Dans la barre latérale gauche, accédez à **VPN** > **WireGuard Client**. Ajoutez un nouveau groupe et définissez un nom explicite (par ex. AmneziaVPN).

    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Téléversez le fichier de configuration AmneziaVPN précédemment exporté dans la partie droite.

    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Après avoir téléversé le fichier de configuration et validé la vérification, cliquez sur **Apply**.

    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    La page s’actualisera et un fichier de configuration apparaîtra dans la liste.

4. Démarrez la connexion VPN.

    Cliquez sur l’icône à trois points, puis sélectionnez **Start**.

    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Attendez environ 1 minute. Si l’indicateur d’état devient vert, cela signifie que la connexion VPN a réussi.

    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Accédez au **VPN Dashboard** ; vous verrez que le Brume 3 est connecté à un serveur AmneziaVPN.

    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    La connexion VPN est terminée. Tous les appareils connectés au Brume 3 accèdent maintenant à Internet via le serveur AmneziaVPN, ce qui permet une connexion VPN obfusquée.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
