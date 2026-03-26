# AstroWarp

**Note** : Ce guide présente la nouvelle version d’AstroWarp, actuellement disponible sur **Flint 3 (GL-BE9300)** et **Slate 7 (GL-BE3600)** avec les firmwares v4.8.4 et v4.8.3 respectivement.

Pour les autres modèles, veuillez consulter [ce lien](https://docs.astrowarp.net/){target="_blank"} pour plus d’informations.

---

AstroWarp est une fonctionnalité réseau avancée intégrée aux routeurs GL.iNet. Elle permet un accès à distance fluide à votre réseau domestique sans inscription ni connexion. En utilisant le protocole AmneziaWG avec obfuscation de trafic intégrée, elle maintient une connexion stable et sécurisée, ce qui en fait une solution idéale pour un accès à distance fiable, où que vous soyez.

Les utilisateurs peuvent configurer un réseau AstroWarp directement depuis le panneau d’administration du routeur GL.iNet. Il suffit d’appairer vos routeurs à l’aide d’un code d’accès pour connecter en toute sécurité votre routeur de voyage à votre réseau domestique en quelques secondes.

**Note:** 

1. Il n’est pas recommandé d’utiliser AstroWarp en même temps que l’une des fonctionnalités suivantes, car cela peut provoquer des conflits de routage : GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Lorsque AstroWarp est activé, la fonction **Network Mode** ne peut pas être utilisée.

## Configuration rapide

Dans l’exemple suivant, nous utiliserons **Flint 3 (GL-BE9300)** et **Slate 7 (GL-BE3600)** pour configurer un réseau AstroWarp.

Flint 3 jouera le rôle de routeur domestique, tandis que Slate 7 fera office de routeur de voyage qui renvoie le trafic réseau vers Flint 3 pour l’accès à Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Note** : Chaque routeur GL.iNet inclut **10 GB de données gratuites par mois** pour le réseau AstroWarp. Les appareils d’un réseau AstroWarp utilisent les données du routeur domestique pour accéder à Internet. Vous pouvez passer au forfait AstroWarp+ pour obtenir des données illimitées si nécessaire.
 
1. Configurez Flint 3 pour l’accès à Internet.

    Connectez-vous au panneau d’administration web de Flint 3 et ouvrez la page **INTERNET**. Connectez-le à Internet à l’aide de l’une des méthodes de connexion prises en charge : Ethernet, Repeater, Tethering et Cellular.

    Comme indiqué ci-dessous, le routeur domestique Flint 3 est connecté au modem du FAI (Hong Kong Broadband Network Ltd) via un câble Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Générez un code d’accès.

    Dans le panneau d’administration web de Flint 3, allez à **CLOUD SERVICES** -> **AstroWarp**. Cliquez sur **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Un **Access Code** sera généré. Copiez ce code pour l’utiliser plus tard.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Configurez Slate 7 pour l’accès à Internet.

    Connectez-vous au panneau d’administration web de Slate 7, puis ouvrez la page **INTERNET**. Connectez-le à Internet à l’aide de l’une des méthodes de connexion prises en charge : Ethernet, Repeater, Tethering et Cellular.

    Comme indiqué ci-dessous, le routeur de voyage Slate 7 est connecté au point d’accès personnel d’un iPhone 15 Pro (situé à Shenzhen, utilisant le réseau China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Saisissez le code d’accès.

    Dans le panneau d’administration web de Slate 7, allez à **CLOUD SERVICES** -> **AstroWarp**. Cliquez sur **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Saisissez l’Access Code obtenu à l’étape 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Attendez que la vérification soit terminée.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    La connexion au routeur domestique Flint 3 sera alors établie avec succès. Vous pourrez désormais naviguer sur Internet de manière sécurisée via votre réseau domestique.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    Dans le panneau d’administration web de Flint 3, l’état de la connexion s’affiche également, comme indiqué ci-dessous.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Tester la connectivité

1. Connectez un ordinateur portable ou un smartphone au Wi-Fi du routeur de voyage Slate 7.

2. Ouvrez un navigateur et consultez [ipcheck.ing](https://ipcheck.ing/){target="_blank"} ou tout autre site de vérification d’adresse IP.

    Le site affichera l’adresse IP publique de Flint 3, ce qui indique que Slate 7 accède à Internet via votre routeur domestique Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Déconnectez la connexion AstroWarp sur Slate 7, puis actualisez la page web pour relancer la requête d’adresse IP.

    Le site affichera l’adresse IP publique de Slate 7, ce qui indique que Slate 7 accède à Internet via son réseau local.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Mettre à niveau le forfait

Chaque routeur GL.iNet inclut **10 GB de données gratuites par mois** pour le réseau AstroWarp. Les appareils d’un réseau AstroWarp utilisent les données du routeur domestique pour accéder à Internet.

Vous pouvez passer au forfait **AstroWarp+** pour obtenir des données illimitées si nécessaire.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
