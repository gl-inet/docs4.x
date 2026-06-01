# AstroWarp

**Remarque** : ce guide couvre la nouvelle version d’AstroWarp.

La nouvelle version d’AstroWarp est intégrée au SDK des routeurs GL.iNet. Elle adopte le protocole AmneziaWG avec obfuscation de trafic intégrée, offrant des connexions stables et sécurisées pour un accès à distance fiable à tout moment, où que vous soyez.

Cette fonctionnalité permet un accès à distance fluide à votre réseau domestique. Vous pouvez configurer et appairer directement les appareils via un code d’accès dynamique dans le panneau d’administration web, afin d’établir rapidement une connexion sécurisée entre votre routeur de voyage et votre réseau domestique en quelques secondes, sans inscription ni connexion.

L’ancienne version d’AstroWarp, bien que visible dans le panneau d’administration web, reposait sur une plateforme AstroWarp autonome pour établir des connexions réseau à distance. Cliquez [ici](https://docs.astrowarp.net/){target="_blank"} pour consulter la documentation de l’ancienne version d’AstroWarp.

**Remarque** :

1. Il n’est pas recommandé d’utiliser AstroWarp en même temps que les fonctionnalités suivantes, car cela peut provoquer des conflits de routage : GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Lorsque AstroWarp est activé, la fonction **Network Mode** ne peut pas être utilisée.


## Modèles pris en charge

??? "Modèles pris en charge"

    Ces modèles sont compatibles avec la nouvelle version d’AstroWarp. Pour consulter la liste des modèles pris en charge par l’ancienne version d’AstroWarp, cliquez [ici](https://docs.astrowarp.net/en/quick_start/){target="_blank"}.

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Remarque** : les modèles marqués d’un ※ prennent en charge l’intégration d’AstroWarp dans un firmware bêta.

??? "Modèles non pris en charge"
    Ces appareils sont incompatibles avec la nouvelle version d’AstroWarp, tandis que certains modèles fonctionnent encore avec l’ancienne version. Consultez [ce lien](https://docs.astrowarp.net/en/quick_start/){target="_blank"} pour plus de détails.

    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
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
    - GL-X300B (Collie)

## Configuration rapide

Dans l’exemple suivant, nous utiliserons **Flint 3 (GL-BE9300)** et **Slate 7 (GL-BE3600)** pour configurer un réseau AstroWarp.

Flint 3 jouera le rôle de routeur domestique, tandis que Slate 7 fera office de routeur de voyage qui renvoie le trafic réseau vers Flint 3 pour l’accès à Internet.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Remarque** : chaque routeur GL.iNet inclut **10 GB de données gratuites par mois** pour le réseau AstroWarp. Les appareils d’un réseau AstroWarp utilisent les données du routeur domestique pour accéder à Internet. Vous pouvez passer au forfait AstroWarp+ pour obtenir des données illimitées si nécessaire.

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

    Comme indiqué ci-dessous, le routeur de voyage Slate 7 est connecté au point d’accès personnel d’un iPhone 15 Pro (situé à Shenzhen et utilisant le réseau China Unicom Guangdong Province).

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

## FAQ

1. **Q : Quel est le format du code d’accès dynamique et combien de temps reste-t-il valide ?**

    R : Il s’agit d’un code de 8 caractères composé de chiffres et de lettres majuscules, valable 10 minutes.

2. **Q : Que se passe-t-il pour le routeur de voyage si je mets fin à la connexion depuis le routeur domestique ?**

    R : Le routeur de voyage sera déconnecté et restera en attente sans accès réseau. Une fois la connexion rétablie sur le routeur domestique, le routeur de voyage pourra se reconnecter automatiquement sans devoir ressaisir le code d’accès.

3. **Q : Que se passe-t-il si les données gratuites sont épuisées ou si le forfait AstroWarp+ expire sur le routeur domestique ?**

    R : Le routeur de voyage passe en attente, sans accès réseau, et ne bascule pas automatiquement vers le réseau local.

4. **Q : Dans quels cas le routeur de voyage passe-t-il en attente ?**

    R : Le routeur de voyage passe en attente lorsque le routeur domestique remplit l’une des conditions suivantes :

    - Il met fin à la connexion AstroWarp.
    - Il a épuisé le quota de données gratuites.
    - La date d’expiration du forfait AstroWarp+ est atteinte (le cas échéant).
    - Il perd l’accès à Internet.

5. **Q : À quoi sert le bouton Reset en haut à droite ?**

    R : Il efface tous les appareils autorisés et ramène la page à la sélection du rôle du routeur afin de pouvoir le choisir à nouveau.

6. **Q : Que se passe-t-il pour le routeur de voyage si je réinitialise AstroWarp sur le routeur domestique ?**

    R : Une fois AstroWarp réinitialisé sur le routeur domestique, les appareils connectés à distance sont déconnectés du réseau AstroWarp et reviennent sur leur réseau local pour accéder à Internet.

7. **Q : Si je mets à niveau le routeur domestique vers le forfait AstroWarp+ et que je change son rôle en routeur de voyage pendant que le forfait est encore valide, la durée restante est-elle conservée ?**

    R : La durée restante ne peut pas être conservée et expirera à la date prévue. Pour éviter toute perte inutile, changez le rôle de l’appareil après l’expiration de votre forfait actuel.

8. **Q : Si j’ai activé la nouvelle version d’AstroWarp dans le panneau d’administration web du routeur, comment la désactiver et revenir à l’ancienne version ?**

    R : Dans le panneau d’administration web du routeur, accédez à **CLOUD SERVICES** -> **AstroWarp**, puis cliquez sur **Reset** en haut à droite.

    ![reset](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/reset.png){class="glboxshadow"}

    Connectez-vous ensuite à [astrowarp.net](https://my.astrowarp.net/#/login){target="_blank"} avec votre compte cloud. Après connexion, cliquez sur le bouton **"+"** pour ajouter le routeur à votre réseau AstroWarp.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/add_device.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
