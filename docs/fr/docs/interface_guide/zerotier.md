# ZeroTier

ZeroTier est un réseau privé virtuel (VPN) logiciel qui permet des communications sécurisées et chiffrées entre des appareils via Internet. Il crée un réseau privé virtuel qui permet aux appareils de communiquer comme s’ils se trouvaient sur le même réseau local, quelle que soit leur localisation physique ou la topologie du réseau. ZeroTier est conçu pour être simple à configurer et à utiliser, et propose des fonctionnalités telles que le chiffrement de bout en bout, la segmentation du réseau et le pontage réseau.

La fonctionnalité ZeroTier sur les routeurs GL.iNet, disponible depuis le firmware v4.2, permet au routeur de rejoindre un réseau virtuel ZeroTier. Une fois connecté, vous pouvez accéder au routeur à distance, y compris à ses ressources WAN et LAN.

**Note** :

1. Il n’est pas recommandé d’utiliser ZeroTier simultanément avec l’une des fonctionnalités ou l’un des services suivants, car cela peut provoquer des conflits de routage : OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale, AstroWarp.

2. Cette fonctionnalité est actuellement en version bêta et peut comporter certains bugs.

3. Certains modèles, bien qu'ils exécutent le firmware v4.2 ou une version ultérieure, ne prennent pas en charge ZeroTier en raison d'une mémoire insuffisante.

## Modèles pris en charge

??? "Modèles pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Modèles non pris en charge"
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Configurer un réseau ZeroTier

Deux versions de ZeroTier Central sont disponibles : New Central et Legacy Central.

- **New Central** : une version plus récente de ZeroTier Central, avec une meilleure ergonomie et de nouvelles fonctionnalités. Elle est recommandée pour les nouveaux utilisateurs afin de bénéficier de la meilleure expérience et des outils les plus récents.

- **Legacy Central** : pour les comptes créés avant novembre 2025. Legacy Central continue de prendre en charge les utilisateurs existants pour la gestion de leurs réseaux.

Les deux versions peuvent être utilisées en parallèle, mais il n’existe actuellement aucune voie de migration directe.

Veuillez sélectionner la version appropriée pour continuer.

### New Central

L’exemple suivant utilise le GL-MT3600BE.

1. Rendez-vous sur le [site officiel de ZeroTier](https://www.zerotier.com/){target="_blank"} et connectez-vous à votre compte.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Créez une organisation.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Sélectionnez un plan. Ici, nous choisissons le plan Personal comme exemple ; il comprend 10 appareils, 1 administrateur réseau et 1 réseau. Si vous devez créer davantage de réseaux, ajouter davantage d’appareils ou ajouter des routes personnalisées et du DNS, choisissez le plan Essential ou Scale.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Votre réseau ZeroTier est maintenant créé. Notez le **Network ID**, qui est une combinaison alphanumérique de 16 caractères située dans l’angle supérieur droit, car il sera nécessaire plus tard lors de la connexion d’autres appareils.

    ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Activez ZeroTier sur le routeur GL.iNet.

    Connectez-vous au panneau d’administration web de votre routeur, puis accédez à **APPLICATIONS** -> **ZeroTier**.

    Activez ZeroTier, saisissez le Network ID sur la même page, puis cliquez sur **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Après un court instant, l’interface indiquera qu’une autorisation est requise. Cliquez sur le lien **ZeroTier Central** pour être redirigé vers ZeroTier Central.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autorisez votre appareil dans ZeroTier Central.

    Dans ZeroTier Central, repérez l’appareil en attente et autorisez-le.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Une fois autorisé, la page s’affiche comme suit.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Ajoutez un autre appareil (comme un ordinateur ou un smartphone) au même réseau ZeroTier en suivant [ce guide](https://docs.zerotier.com/platforms/){target="_blank"}.

    Voici un exemple avec un ordinateur portable Windows 10 Pro.
    
    1. Installez ZeroTier sur l’ordinateur portable à partir d’[ici](https://www.zerotier.com/download/){target="_blank"}.

    2. Lancez ZeroTier. L’icône ZeroTier apparaîtra dans la zone de notification, en bas à droite du bureau.
        
    3. Cliquez avec le bouton droit sur l’icône, sélectionnez **Join New Network**, puis saisissez le **Network ID** obtenu à l’étape 4 dans la fenêtre contextuelle.
        
        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Ensuite, accédez à ZeroTier Central, repérez l’appareil en attente et autorisez-le.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Une fois l’appareil autorisé, la page s’affiche comme suit. Vous verrez les détails des appareils membres, tels que **Device ID**, **Name**, **Status**, **Managed IP** et **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Astuce** : vous pouvez cliquer sur l’icône à trois points à droite pour modifier les paramètres de l’appareil membre, notamment le nom de l’appareil, le ou les Managed IP et les paramètres avancés.

8. Cliquez sur le **Managed IP** du routeur pour le copier. Vous pouvez ensuite utiliser ce Managed IP pour accéder au routeur depuis votre ordinateur portable connecté au même réseau ZeroTier.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Testez la connectivité.

    Sur l’ordinateur portable connecté au même réseau ZeroTier, ouvrez un navigateur web et saisissez le Managed IP du routeur obtenu à l’étape précédente.

    Si vous pouvez accéder au panneau d’administration web du routeur, la connexion ZeroTier est réussie.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Vous pouvez également utiliser `ping` vers le Managed IP du routeur depuis votre ordinateur portable pour tester la connectivité. Si vous recevez une réponse positive, la connexion ZeroTier est correctement établie.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

L’exemple suivant utilise le GL-MT2500.

1. Créez votre premier réseau ZeroTier.

    Reportez-vous au [guide de démarrage](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"} officiel de ZeroTier pour créer un compte et un réseau ZeroTier. N’oubliez pas de noter le Network ID, qui est une combinaison alphanumérique de 16 caractères, car il sera nécessaire plus tard lors de la connexion d’autres appareils.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Activez ZeroTier sur le routeur GL.iNet.

    Connectez-vous au panneau d’administration web de votre routeur, puis accédez à **APPLICATIONS** -> **ZeroTier**.

    Activez ZeroTier, saisissez le Network ID sur la même page, puis cliquez sur **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    Après un court instant, l’interface indiquera qu’une autorisation est requise.
    
    Cliquez sur le lien **ZeroTier Central** pour être redirigé vers ZeroTier Central.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autorisez votre appareil dans ZeroTier Central.

    Dans ZeroTier Central, accédez à la section **Members**. Repérez le nouvel appareil et cochez la case **Auth** pour l’autoriser. Vous pouvez personnaliser le nom de l’appareil si vous le souhaitez.
    
    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Après un court instant, ZeroTier attribuera un **Managed IP** à l’appareil. Notez cette adresse IP, car elle sera utilisée à l’étape de test.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. Ajoutez un autre appareil (comme un ordinateur ou un smartphone) au même réseau ZeroTier en suivant [ce guide](https://docs.zerotier.com/platforms/){target="_blank"}.

5. Testez la connectivité.

    Sur un autre appareil connecté au même réseau ZeroTier, ouvrez un navigateur web et saisissez le ZeroTier Managed IP du routeur obtenu à l’étape précédente.

    Vous pourrez accéder au panneau d’administration web du routeur.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

    Vous pouvez également utiliser la commande `ping` pour tester la connectivité. Veuillez consulter le [guide de démarrage rapide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"} de ZeroTier.

## Allow Remote Access WAN

Si cette option est activée, les ressources situées du côté WAN de l’appareil peuvent être accessibles via le réseau virtuel ZeroTier.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez accéder au `GL-AXT1800` via son adresse IP (`192.168.29.1`) depuis `leo-phone`. Cela est possible car le GL-AXT1800 est l’appareil de niveau supérieur du `GL-MT2500`, et ce dernier est connecté au même réseau ZeroTier que leo-phone.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Note** : Cette fonctionnalité nécessite l’ajout de règles de routage dans le réseau ZeroTier pour prendre effet. Une route personnalisée peut être ajoutée gratuitement dans Legacy Central, tandis que dans New Central, vous ne pouvez configurer des routes personnalisées qu’avec un plan Essential ou supérieur. Cliquez [ici](https://www.zerotier.com/pricing/) pour plus de détails.

Les étapes suivantes utilisent Legacy Central comme exemple.

1. Connectez-vous au panneau d’administration web de votre routeur, puis accédez à **APPLICATIONS** -> **ZeroTier**.

    Activez **Allow Remote Access WAN**, puis cliquez sur **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Le système vous invitera à configurer des règles de routage. Laissez cette page web ouverte ou notez les détails de la route (Destination et Via), car ils seront nécessaires à l’étape suivante.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Accédez à **ZeroTier Central** et repérez la section **Advanced**.

    Saisissez les détails de la route (Destination et Via) obtenus à l’étape précédente, puis cliquez sur **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    Une fois la route ajoutée, la section **Managed Routes** s’affichera comme indiqué ci-dessous.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Vous pouvez maintenant accéder au `GL-AXT1800` via son adresse IP (`192.168.29.1`) depuis d’autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.29.0/24`.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Allow Remote Access LAN

Si cette option est activée, les ressources situées du côté LAN de l’appareil peuvent être accessibles via le réseau virtuel ZeroTier.

Par exemple, comme indiqué dans la topologie ci-dessous, si cette fonction est activée, vous pouvez vous connecter en SSH à `Ubuntu` via son adresse IP (`192.168.8.110`) depuis `leo-phone`. Cela est possible car `Ubuntu` est l’appareil de niveau inférieur du `GL-MT2500`, et ce dernier est connecté au même réseau ZeroTier que leo-phone.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Note** : Cette fonctionnalité nécessite l’ajout de règles de routage dans le réseau ZeroTier pour prendre effet. Une route personnalisée peut être ajoutée gratuitement dans Legacy Central, tandis que dans New Central, vous ne pouvez configurer des routes personnalisées qu’avec un plan Essential ou supérieur. Cliquez [ici](https://www.zerotier.com/pricing/) pour plus de détails.

Les étapes suivantes utilisent Legacy Central comme exemple.

1. Connectez-vous au panneau d’administration web de votre routeur, puis accédez à **APPLICATIONS** -> **ZeroTier**.

    Activez **Allow Remote Access LAN**, puis cliquez sur **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Le système vous invitera à configurer des règles de routage. Laissez cette page web ouverte ou notez les détails de la route (Destination et Via), car ils seront nécessaires à l’étape suivante.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Accédez à **ZeroTier Central** et repérez la section **Advanced**.

    Saisissez les détails de la route (Destination et Via) obtenus à l’étape précédente, puis cliquez sur **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    Une fois la route ajoutée, la section **Managed Routes** s’affichera comme indiqué ci-dessous.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Vous pouvez maintenant envoyer un ping à `Ubuntu` ou vous y connecter en SSH via son adresse IP (`192.168.8.110`) depuis d’autres appareils. En réalité, vous pouvez accéder à tous les appareils du sous-réseau `192.168.8.0/24`.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
