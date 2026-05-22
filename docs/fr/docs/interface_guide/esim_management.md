# Gestion de l'eSIM

Dans le panneau d'administration web, allez dans **APPLICATIONS** -> **eSIM Management**.

Cette page permet de vérifier l'état de la carte physique eSIM et de gérer les profils eSIM. Elle se compose de deux parties : **État actuel de l'eSIM** et **Liste des profils eSIM**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Modèles pris en charge

| Router Model          | Support |
| :-------------------- | :-----: |
| GL-X2000 (Spitz Plus) |    √    |
| GL-X3000 (Spitz AX)   |    √    |
| GL-XE3000 (Puli AX)   |    √    |
| GL-E750V2 (Mudi V2)   |    √    |
| GL-E750 (Mudi)        |    √    |
| GL-XE300 (Puli)       |    ※    |
| GL-X750 (Spitz)       |    ※    |
| GL-X300B (Collie)     |    ※    |
| GL-E750V2 vSIM        |    X    |
| GL-E5800 (Mudi 7)     |    X    |

**Pour les modèles marqués ※** :

1. Le firmware stable actuel ne prend pas en charge l'eSIM. Pour utiliser cette fonction, vous devez installer un firmware compatible eSIM. [Contactez-nous](https://www.gl-inet.com/contacts/){target="\_blank"} pour plus d'instructions.

2. Pour les modèles marqués ※ équipés d'un module EP06-A, l'eSIM n'est pas prise en charge, car le logiciel Qualcomm ne prend pas en charge les commandes AT nécessaires.

3. Pour le GL-E750 (Mudi) et les modèles marqués ※ équipés d'un module EP06-E, consultez ce [lien](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="\_blank"} pour d'abord mettre à niveau le firmware du module, puis installer le firmware compatible eSIM afin d'activer la fonction eSIM.

**Pour les modèles marqués X** :

1. Le GL-E750V2 vSIM ne prend pas en charge la fonctionnalité eSIM.

2. Le GL-E5800 (Mudi 7) intègre déjà une eSIM. Par conséquent, la carte physique eSIM sera reconnue comme une carte SIM classique, sans fonctionnalité eSIM, sur le Mudi 7.

## État actuel de l'eSIM

Cette section affiche les informations de base et les détails du profil eSIM actuellement actif.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Identifiant unique mondial de l'eUICC (puce eSIM), utilisé pour l'identification et la gestion des profils.
- **ICCID:** Identifiant de circuit intégré de la carte du profil eSIM actuellement actif.
- **IMSI:** Identité internationale d'abonné mobile du profil eSIM actuellement actif.
- **eSIM OS Version:** Version du système d'exploitation de l'eUICC, qui définit sa compatibilité et les fonctions prises en charge.
- **eSIM Storage (remain/total):** Capacité disponible et capacité totale de l'eUICC pour stocker les profils eSIM.
- **eSIM Profile Number:** Nombre de profils eSIM actuellement stockés sur l'eUICC. Notez que les profils eSIM proposés par différents opérateurs n'ont pas tous la même taille ; le nombre de profils pouvant être stockés sur l'eUICC peut donc varier.

## Liste des profils eSIM

Cette section affiche les informations relatives au Seed Profile et aux profils normaux.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile** : le Seed Profile est préchargé avec 1 Go de données gratuites pour les États-Unis et l'Europe, ainsi que 100 Mo de données globales, valables pendant 1 an à compter de la date d'activation. Ces données vous permettent de télécharger d'autres profils n'importe où dans le monde. Vous pouvez également suivre l'utilisation du Seed Profile, y compris les données restantes, le volume total et la date d'expiration.

- **Normal Profile** : si vous achetez un profil eSIM et le téléchargez via un QR code ou un code d'activation, il s'affichera ici.

### Recharger le Seed Profile

GL.iNet fournit un Seed Profile préchargé avec 100 Mo de données globales et 1 Go de données valables en Europe et aux États-Unis pour la configuration initiale et l'activation des profils eSIM. Cette offre est conçue pour télécharger de nouveaux profils eSIM lorsque vous arrivez à destination sans accès à Internet.

Si vous avez déjà utilisé les données gratuites préchargées, ou si elles ont expiré et que vous souhaitez continuer à utiliser le service, vous pouvez recharger votre Seed Profile.

Dans la section **Seed Profile**, cliquez sur le bouton **Top-up** à droite.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, scannez le QR code et suivez les instructions pour finaliser la recharge.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Acheter un profil eSIM

Vous pouvez acheter des profils eSIM dans nos boutiques recommandées, dans des boutiques testées, ou auprès d'autres fournisseurs eSIM tiers.

??? note "Option 1: Acheter dans nos boutiques recommandées"

    Il y a deux boutiques recommandées : [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} et [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Dans la section **Normal Profile**, cliquez sur **eSIM Profile Recommended Store** à droite.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Scannez le QR code ou cliquez sur les liens pour acheter des profils eSIM.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Note** : Tous les forfaits eSIM achetés dans ces deux boutiques sont entièrement compatibles avec les routeurs GL.iNet. Si vous avez des questions, contactez notre équipe d'assistance à [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Option 2: Acheter dans des boutiques testées"

    Consultez [ce lien](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} pour voir la liste des boutiques testées par GL.iNet.

    **Note** : Nous ne pouvons pas garantir une compatibilité totale avec les routeurs GL.iNet pour tous les profils ou forfaits provenant de ces boutiques. Comme GL.iNet n'a pas de partenariat avec elles, nous ne pouvons ni fournir de support après-vente ni aider pour les remboursements.

??? note "Option 3: Acheter auprès d'autres fournisseurs eSIM tiers"

    Vous pouvez aussi choisir d'acheter des profils eSIM auprès d'autres fournisseurs tiers.

    Cependant, nous ne pouvons pas garantir une compatibilité totale avec les routeurs GL.iNet pour les profils eSIM achetés auprès d'autres fournisseurs tiers. Effectuez votre achat à votre propre discrétion. GL.iNet n'est pas responsable des problèmes d'incompatibilité.

    Pour le support après-vente ou les remboursements, contactez le fournisseur eSIM concerné.

### Téléverser un profil eSIM

Après avoir acheté un profil eSIM, vous recevrez en général un QR code ou un code d'activation. Enregistrez ce QR code en local, puis suivez les étapes ci-dessous pour téléverser votre profil eSIM.

1. Dans la section **Normal Profile**, cliquez sur **Add eSIM Profile** en bas.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Téléversez votre QR code eSIM ou saisissez le code d'activation, puis cliquez sur **Install**. Le profil eSIM sera alors téléchargé et installé sur votre routeur.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Note :**

    1. La plupart des profils eSIM ne peuvent être téléchargés et installés qu'une seule fois.

    2. Un QR code correctement formaté affichera un code d'activation commençant par **LPA:**. Cependant, certains QR codes non standard peuvent ne fournir qu'un code brut sans le préfixe LPA. Dans ce cas, ajoutez manuellement `LPA:` au début du code avant de cliquer sur **Install**.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Si vous n'avez encore acheté aucun profil eSIM, vous pouvez en acheter un depuis **eSIM Profile Recommended Store**. Cliquez [ici](#acheter-un-profil-esim) pour les détails.

3. Activez votre profil eSIM.

    Une fois le téléversement terminé avec succès, votre nouveau profil eSIM apparaîtra dans la liste **Normal Profile**. Cliquez sur **Enable** pour l'activer.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Connectez-vous à Internet.

    Après avoir activé votre profil eSIM, allez dans **INTERNET** -> **Cellular**. Cliquez sur **Connect** pour établir une connexion Internet via votre profil eSIM.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Note** : Certains profils eSIM peuvent nécessiter des paramètres supplémentaires, comme l'APN, le PIN ou le TTL. Si nécessaire, cliquez sur **Manual Setup** ou **SIM Card Settings** pour ajuster ces paramètres. Dans certains cas, un redémarrage de l'appareil peut être nécessaire pour établir la connexion Internet.\*

5. Une fois que le routeur se connecte avec succès via le profil eSIM, la page s'affiche comme suit :

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Exporter les journaux pour le support

Cliquez sur **Export Log for Support** pour afficher tous les journaux liés à l'eSIM. Si vous rencontrez des problèmes et avez besoin d'une assistance technique, exportez les journaux eSIM et envoyez-les à notre équipe d'assistance par e-mail à [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Articles associés :

- [Comment utiliser la carte physique eSIM avec les routeurs GL.iNet ?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Comment utiliser la carte physique eSIM avec les appareils Android ?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Vous avez encore des questions ? Visitez notre [Community Forum](https://forum.gl-inet.com){target="\_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="\_blank"}.
