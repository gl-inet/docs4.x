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

Vous pouvez y consulter l’état de votre eSIM et gérer vos profils eSIM.

Un seul profil eSIM peut être actif à la fois. Un point vert indique que le profil eSIM sélectionné est actuellement actif.

---

Article associé :

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
