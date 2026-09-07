# GoodPAS

**Remarque** : cette fonctionnalité a été introduite dans le firmware v4.10, version dans laquelle AstroWarp a été renommé GoodPAS. Si votre appareil utilise une version antérieure du firmware, consultez [AstroWarp](./astrowarp.md).

---

Dans la partie gauche du panneau d’administration web, accédez à **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS est une solution avancée d’accès à distance intégrée au SDK des routeurs GL.iNet. Elle utilise le protocole AmneziaWG avec obfuscation intégrée du trafic afin d’offrir des connexions stables et sécurisées pour un accès à distance fiable, à tout moment et où que vous soyez.

Cette fonctionnalité permet d’accéder facilement à votre réseau domestique à distance. Vous pouvez configurer et appairer directement les appareils au moyen d’un code d’accès dynamique dans le panneau d’administration web. Une connexion sécurisée entre votre routeur de voyage et votre réseau domestique est ainsi établie en quelques secondes, sans inscription ni connexion à un compte.

**Remarque** :

1. Il est déconseillé d’utiliser GoodPAS en même temps que l’une des fonctionnalités suivantes, car cela peut provoquer des conflits de routage : GoodCloud Site to Site, ZeroTier, Tailscale et Tor.

2. Lorsque GoodPAS est activé, Network Mode ne peut pas être utilisé.

## Configuration rapide

Dans l’exemple suivant, nous utiliserons **Flint 3 (GL-BE9300)** et **Mango 2 (GL-MG1300)** pour configurer un réseau GoodPAS.

Flint 3 servira de routeur domestique, tandis que Mango 2 fera office de routeur de voyage et acheminera le trafic réseau vers Flint 3 pour l’accès à Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Configurez Flint 3 pour l’accès à Internet.

    Connectez-vous au panneau d’administration web de Flint 3, puis ouvrez la page INTERNET. Connectez-le à Internet à l’aide de l’une des méthodes prises en charge : Ethernet, Repeater, Tethering ou Cellular.

    Comme illustré ci-dessous, le routeur domestique Flint 3 est connecté par câble Ethernet au modem du FAI (Hong Kong Broadband Network Ltd).

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Générez un code d’accès.

    Dans le panneau d’administration web de Flint 3, accédez à **CLOUD SERVICES** -> **GoodPAS**. Cliquez sur **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Un Access Code est généré. Copiez-le pour l’utiliser ultérieurement.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Configurez Mango 2 pour l’accès à Internet.

    Connectez-vous au panneau d’administration web de Mango 2, puis ouvrez la page INTERNET. Connectez-le à Internet à l’aide de l’une des méthodes prises en charge : Ethernet, Repeater, Tethering ou Cellular.

    Comme illustré ci-dessous, le routeur de voyage Mango 2 est connecté au point d’accès personnel d’un iPhone 17 (situé à Shenzhen et utilisant le réseau China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Saisissez le code d’accès.

    Dans le panneau d’administration web de Mango 2, accédez à **CLOUD SERVICES** -> **GoodPAS**. Cliquez sur **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Saisissez le code d’accès obtenu à l’étape 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Attendez la fin de la vérification.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    La connexion au routeur domestique Flint 3 est alors établie. Vous pouvez désormais naviguer sur Internet en toute sécurité via votre réseau domestique.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Le panneau d’administration web de Flint 3 affiche également l’état de la connexion, comme illustré ci-dessous.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Tester la connectivité

1. Connectez un ordinateur portable ou un smartphone au Wi-Fi du routeur de voyage Mango 2.

2. Ouvrez un navigateur et consultez [ipcheck.ing](https://ipcheck.ing/){target="_blank"} ou tout autre site de vérification d’adresse IP.

    L’adresse IP publique de Mango 2 s’affiche, ce qui indique que Mango 2 accède à Internet via votre routeur domestique Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Déconnectez GoodPAS sur Mango 2, puis actualisez la page web pour relancer la requête d’adresse IP.

    L’adresse IP publique de Mango 2 s’affiche, ce qui indique que Mango 2 accède à Internet via son réseau local.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **Q : Quel est le format du code d’accès dynamique et combien de temps reste-t-il valide ?**

    R : Il s’agit d’un code de 8 caractères composé de chiffres et de lettres majuscules, valable pendant 10 minutes.

2. **Q : Que se passe-t-il pour le routeur de voyage si je mets fin à la connexion sur le routeur domestique ?**

    R : Le routeur de voyage est déconnecté et reste en attente, sans accès au réseau. Lorsque le routeur domestique rétablit la connexion, le routeur de voyage peut se reconnecter automatiquement sans qu’il soit nécessaire de saisir à nouveau le code d’accès.

3. **Q : Dans quels cas le routeur de voyage passe-t-il en attente ?**

    R : Le routeur de voyage passe en attente lorsque le routeur domestique remplit l’une des conditions suivantes :

    - Il met fin à la connexion GoodPAS.
    - Il perd l’accès à Internet.

4. **Q : À quoi sert le bouton Reset en haut à droite ?**

    R : Il efface tous les appareils autorisés et revient à la page de sélection du rôle du routeur afin de pouvoir choisir à nouveau ce rôle.

5. **Q : Que se passe-t-il pour le routeur de voyage si je réinitialise GoodPAS sur le routeur domestique ?**

    R : Une fois le routeur domestique réinitialisé, les appareils connectés à distance sont déconnectés du réseau GoodPAS et utilisent à nouveau leur réseau local pour accéder à Internet.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
