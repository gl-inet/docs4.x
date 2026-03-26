# Comment utiliser la carte physique eSIM avec les routeurs GL.iNet ?

Ce guide vous explique comment utiliser la carte physique eSIM achetée sur la boutique en ligne GL.iNet avec les routeurs GL.iNet. 

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Fonctionnalités

Les avantages des cartes physiques eSIM sont les suivants :

- Prend en charge les réseaux 4G et 5G pour des connexions fiables et rapides.
- Gérez vos profils eSIM facilement en les ajoutant, en les supprimant ou en les activant.
- Sélectionnez et achetez vos forfaits de données préférés dans la plupart des boutiques eSIM du monde entier, à tout moment.
- Fonctionne avec les profils eSIM de la plupart des boutiques eSIM mondiales.
- Achetez des profils eSIM en ligne sans fournir d'informations personnelles, réduisant ainsi le risque de violation de la vie privée.
- Livré avec un profil de base comprenant 1 Go de données gratuites pour les États-Unis et l'Europe, ainsi que 100 Mo de données mondiales, valables 1 an à compter de la date d'activation.
- Compatible avec certains appareils GL.iNet.

## Modèles pris en charge

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | ※        |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Pour les modèles marqués ※** :

1. Le firmware stable actuel ne prend pas en charge eSIM. Pour utiliser la fonction eSIM, vous devez installer le firmware compatible eSIM. [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"} pour plus d'instructions.
    
2. Si vous utilisez le modèle ※ avec le module EP06-A, eSIM n'est pas pris en charge car le logiciel Qualcomm ne dispose pas du support de commandes AT spécifiques.
    
3. Si vous utilisez le modèle ※ avec le module EP06-E, veuillez consulter ce [lien](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} pour mettre à niveau le firmware du module et installer le firmware compatible eSIM afin d'activer la fonctionnalité eSIM.

**Pour les modèles marqués X** :

1. GL-E750V2 vSIM ne prend pas en charge la fonctionnalité eSIM.

2. GL-E5800 (Mudi 7) est équipé d'une eSIM intégrée. Par conséquent, la carte physique eSIM sera reconnue comme une carte SIM classique sans fonctionnalité eSIM sur Mudi 7.

## Configurer la carte physique eSIM

Si vous utilisez la carte physique eSIM pour la première fois, veuillez regarder cette vidéo de configuration ou suivre les étapes ci-dessous pour la configurer sur votre routeur GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Étape 1 :** Insérez la carte physique eSIM dans votre routeur. Référez-vous aux images ci-dessous pour des instructions détaillées.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Étape 2 :** Ouvrez un navigateur et saisissez « 192.168.8.1 » dans la barre d'adresse pour vous connecter au panneau d'administration GL.iNet.

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Étape 3 :** Connectez votre appareil à Internet. 

Accédez à **INTERNET** et cliquez sur **Connect** (ou **Auto Setup** dans les versions de firmware inférieures) pour vous connecter à Internet via la connexion cellulaire.

*Cette carte physique eSIM est livrée avec un profil de base comprenant 1 Go de données gratuites pour les États-Unis et l'Europe, ainsi que 100 Mo de données mondiales, valables 1 an à compter de la date d'activation. Veuillez noter que ces données sont uniquement destinées à l'achat et au téléchargement de profils eSIM et ne sont pas prévues pour un accès Internet général.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Si la connexion Internet est établie avec succès, l'écran apparaîtra comme suit.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Gérer votre profil eSIM

**Étape 1 :** Assurez-vous que votre appareil GL.iNet dispose du dernier firmware installé.

Veuillez vous assurer que la **Version** est 4.0 ou supérieure et que le numéro **Firmware Type** est 0319 ou supérieur.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Si votre firmware **n'est pas à jour**, vous pouvez le mettre à niveau automatiquement en ligne ou manuellement.

<u>Option 1</u> : Mise à niveau du firmware en ligne

1. Assurez-vous que votre appareil est connecté à Internet. 
    
2. Dans le panneau d'administration web, accédez à **SYSTEM** > **Upgrade** > **Online Upgrade** et cliquez sur le bouton **Install** pour mettre à jour automatiquement vers le dernier firmware.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Option 2</u> : Mise à jour manuelle du firmware

1. Téléchargez le firmware pour le modèle correspondant qui prend en charge la fonctionnalité eSIM depuis [ici](https://dl.gl-inet.com/){target="_blank"}.
    
2. Dans le panneau d'administration web, accédez à **SYSTEM** > **Upgrade** > **Local Upgrade**. Sélectionnez le fichier de firmware ou faites-le glisser dans la zone désignée pour effectuer la mise à niveau vers la dernière version.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Certains modèles, tels que Mudi (GL-E750), Puli (GL-XE300) et Spitz (GL-X750), ne prennent pas en charge eSIM s'ils sont équipés de modules Quectel EP06-A en raison du logiciel Qualcomm qui ne dispose pas du support de commandes AT spécifiques.  
    
    2. S'ils sont équipés de modules EP06-E, veuillez consulter [ce lien](https://forum.gl-inet.com/t/48907){target="_blank"} pour mettre à niveau le module vers le dernier logiciel pour la fonctionnalité eSIM.

**Étape 2 :** Accédez à la gestion eSIM.

Après la mise à jour du firmware, attendez que votre appareil redémarre, puis connectez-vous au panneau d'administration GL.iNet.

Accédez à **APPLICATIONS** > **eSIM Management**. Vous pouvez y consulter l'état actuel de votre eSIM.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Un seul profil eSIM peut être actif à la fois. Un point vert indique que le profil eSIM sélectionné est actuellement actif.

## Guide de gestion eSIM

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. État actuel de l'eSIM :**

Cette section affiche les informations de base de l'eSIM et les détails du profil actuellement actif.

- **EID :** L'identifiant unique mondial de l'eUICC (puce eSIM) utilisé pour l'identification et le contrôle du profil.
- **ICCID :** L'identifiant de carte à circuit intégré du profil eSIM actuellement actif.
- **IMSI :** L'identité internationale d'abonné mobile du profil eSIM actuellement actif.
- **eSIM OS Version :** La version du système d'exploitation de l'eUICC qui définit sa compatibilité et ses capacités.
- **eSIM Storage (remain/total) :** La capacité de stockage disponible et totale sur l'eUICC pour stocker les profils eSIM.
- **eSIM Profile Number :** Le nombre de profils eSIM actuellement stockés sur l'eUICC.

**B. Seed Profile :**

Cette section fournit des détails sur le profil de base. Le profil de base est préchargé avec 1 Go de données gratuites pour les États-Unis et l'Europe, ainsi que 100 Mo de données mondiales, valables 1 an à compter de la date d'activation. Ces données vous permettent de télécharger d'autres profils dans le monde entier. Vous pouvez également surveiller l'utilisation du profil de base, y compris les données restantes, le total de données et la date d'expiration.

**C. Normal Profile :**

Cette section affiche des informations sur les profils normaux. Si vous achetez un profil eSIM dans une boutique en ligne et téléchargez le code QR eSIM à l'aide de la fonction **Add eSIM Profile (QR Code Install)**, le profil apparaîtra ici une fois le téléchargement terminé.

**D. Add eSIM Profile (QR Code Install) :**

Il s'agit de la fonction principale pour télécharger et installer des profils eSIM. Lorsque vous achetez un profil eSIM dans une boutique en ligne, vous recevrez un code QR. Cliquez sur ce bouton pour télécharger le code QR, qui téléchargera et installera ensuite le profil eSIM sur votre routeur.

**E. Export Log for Support :**

Cette section vous permet de consulter tous les journaux liés au fonctionnement de l'eSIM. Si vous rencontrez des problèmes et avez besoin d'une assistance technique, vous pouvez exporter ces journaux et les partager avec notre équipe d'assistance par e-mail à support@gl-inet.com.

**F. Top-up :**

Si vous épuisez les données gratuites et préchargées fournies par GL.iNet, ou si les données ont expiré et que vous souhaitez continuer à utiliser le service, vous pouvez cliquer sur le bouton **Top-up** pour scanner un code QR et acheter des données supplémentaires.

**G. Recommended eSIM Profile Stores :**

GL.iNet recommande deux boutiques eSIM partenaires pour votre commodité : EIOTCLUB et Tuge. Vous pouvez scanner les codes QR ou cliquer sur le lien ([la boutique eSIM EIOTCLUB](https://www.eiotclub.com/pages/esim){target="_blank"} ou [la boutique eSIM Tuge](https://esim_store.gl-inet.com/){target="_blank"}) pour effectuer un achat en fonction de vos besoins. Vous pouvez également choisir d'acheter des forfaits eSIM auprès d'autres fournisseurs tiers de votre choix.

**H. Actions :**

Cette section vous permet de gérer facilement les profils eSIM, y compris leur activation, leur changement ou leur suppression.

## Recharger le profil de base eSIM

Pour la configuration initiale ou l'achat d'un profil eSIM, GL.iNet fournit des données préchargées : 100 Mo pour un usage mondial et 1 Go pour l'Europe et les États-Unis. Ces forfaits sont conçus pour être plus coûteux et sont destinés aux situations où vous devez télécharger un nouveau profil eSIM à votre arrivée dans un lieu sans accès à Internet.

Pour recharger votre profil de base eSIM, il vous suffit de cliquer sur le bouton **Top-up**, de scanner le code QR et de suivre les instructions.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## Acheter et installer un profil eSIM

Après avoir configuré votre routeur, suivez les étapes ci-dessous pour acheter et activer votre profil eSIM.

**Étape 1 :** Achetez un profil eSIM dans les boutiques eSIM.

<u>Option 1</u> : Achetez un profil eSIM dans l'une de nos boutiques recommandées, [la boutique eSIM EIOTCLUB](https://www.eiotclub.com/pages/esim){target="_blank"} ou [la boutique eSIM Tuge](https://esim_store.gl-inet.com){target="_blank"}. Veuillez vous référer à l'image ci-dessous pour les liens directs vers les boutiques.


*Tous les forfaits de profils eSIM achetés dans ces deux boutiques sont entièrement compatibles avec nos routeurs. Si vous avez des questions, veuillez contacter notre équipe d'assistance à support@gl-inet.com.*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Option 2</u> : Consultez [ce lien](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} pour obtenir une liste de boutiques qui ont été testées par GL.iNet. Notez que nous ne pouvons pas garantir que tous les forfaits de ces boutiques seront entièrement compatibles avec les routeurs GL.iNet.

*Étant donné que GL.iNet n'a pas de partenariat avec ces boutiques, nous ne sommes pas en mesure d'aider pour le support après-vente ou les remboursements liés à ces forfaits.*

<u>Option 3</u> : Achetez un profil eSIM auprès d'autres fournisseurs tiers de votre choix.

**Étape 2** : Installez votre profil eSIM

Après avoir acheté le profil eSIM, vous recevrez un code QR. Enregistrez ce code QR sur votre ordinateur. Ensuite, cliquez sur le bouton **Add eSIM Profile (QR Code Install)** pour télécharger et installer votre profil eSIM acheté.

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Remarque :** Comme indiqué par la flèche verte dans l'image ci-dessus, un code QR correctement formaté affichera un code d'activation commençant par **LPA:**.

*Cependant, certains codes QR non standard peuvent ne produire qu'un code d'activation brut sans le préfixe LPA.
Si cela se produit, veuillez ajouter manuellement « LPA: » au début du code avant de cliquer sur le bouton **Download & Install**.*

**Étape 3 :** Activez votre nouveau profil

Après avoir téléchargé avec succès le code QR, vous verrez votre nouveau profil eSIM répertorié sous **Normal Profile**. Cliquez sur **Enable** pour activer votre nouveau profil eSIM. 

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Étape 4 :** Appliquez votre nouveau profil eSIM et connectez-vous à Internet

Après avoir activé votre profil eSIM, accédez à **INTERNET** et cliquez sur **Connect** pour appliquer votre profil eSIM et vous connecter à Internet.

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*Remarque : Certains profils eSIM peuvent nécessiter des paramètres supplémentaires, tels que APN, PIN ou TTL. Si nécessaire, cliquez sur **Manual Setup** ou **SIM Card Settings** pour configurer ces paramètres. Dans certains cas, vous devrez peut-être redémarrer l'appareil pour établir une connexion Internet.*

Une fois le profil eSIM configuré avec succès, l'écran apparaîtra comme suit :

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Étape 5 :** Changez ou supprimez facilement les profils eSIM

Vous pouvez facilement basculer entre les profils eSIM en cliquant sur **Enable** à côté du profil que vous souhaitez activer. Pour supprimer un profil eSIM, cliquez simplement sur **Delete**.

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
