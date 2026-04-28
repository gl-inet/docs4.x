# Gestion eSIM

Dans le panneau d'administration web, allez dans **APPLICATIONS** -> **eSIM Management**.

Cette page permet de verifier l'etat de la eSIM Physical Card et de gerer les profils eSIM. Elle se compose de deux parties : **Current eSIM Status** et **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Modeles pris en charge

| Router Model                   | Support   |
| :----------------------------- | :-------: |
| GL-X2000 (Spitz Plus)          | √         |
| GL-X3000 (Spitz AX)            | √         |
| GL-XE3000 (Puli AX)            | √         |
| GL-E750V2 (Mudi V2)            | √         |
| GL-E750 (Mudi)                 | √         |
| GL-XE300 (Puli)                | ※        |
| GL-X750 (Spitz)                | ※        |
| GL-X300B (Collie)              | ※        |
| GL-E750V2 vSIM                 | X         |
| GL-E5800 (Mudi 7)              | X         |

**Pour les modeles marques ※** :

1. Le firmware stable actuel ne prend pas en charge eSIM. Pour utiliser cette fonction, vous devez installer un firmware compatible eSIM. [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"} pour plus d'instructions.

2. Pour les modeles marques ※ avec un module EP06-A, eSIM n'est pas prise en charge, car le logiciel Qualcomm ne prend pas en charge les commandes AT necessaires.

3. Pour le GL-E750 (Mudi) et les modeles marques ※ avec un module EP06-E, consultez ce [lien](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} pour mettre d'abord a niveau le firmware du module, puis installez le firmware compatible eSIM afin d'activer la fonction eSIM.

**Pour les modeles marques X** :

1. GL-E750V2 vSIM ne prend pas en charge la fonctionnalite eSIM.

2. GL-E5800 (Mudi 7) integre deja une eSIM. La eSIM Physical Card sera donc reconnue comme une carte SIM classique sans fonctionnalite eSIM sur le Mudi 7.

## Current eSIM Status

Cette section affiche les informations de base et les details du profil eSIM actuellement actif.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Identifiant unique mondial de l'eUICC (puce eSIM), utilise pour l'identification et la gestion des profils.
- **ICCID:** Integrated Circuit Card Identifier du profil eSIM actuellement actif.
- **IMSI:** International Mobile Subscriber Identity du profil eSIM actuellement actif.
- **eSIM OS Version:** Version du systeme d'exploitation de l'eUICC, qui definit sa compatibilite et les fonctions prises en charge.
- **eSIM Storage (remain/total):** Capacite disponible et capacite totale de l'eUICC pour stocker les profils eSIM.
- **eSIM Profile Number:** Nombre de profils eSIM actuellement stockes sur l'eUICC. Notez que les profils eSIM proposes par differents operateurs n'ont pas tous la meme taille, donc le nombre de profils pouvant etre stockes sur l'eUICC peut varier.

## eSIM Profile List

Cette section affiche les informations du Seed Profile et des profils normaux.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile** : Le Seed Profile est precharge avec 1 Go de donnees gratuites pour les Etats-Unis et l'Europe, ainsi que 100 Mo de donnees globales, valables pendant 1 an a compter de la date d'activation. Ces donnees vous permettent de telecharger d'autres profils n'importe ou dans le monde. Vous pouvez egalement suivre l'utilisation du Seed Profile, y compris les donnees restantes, le volume total et la date d'expiration.

- **Normal Profile** : Si vous achetez un profil eSIM et le telechargez via un QR code ou un code d'activation, il s'affichera ici.

### Recharger le Seed Profile

GL.iNet fournit un Seed Profile precharge avec 100 Mo de donnees globales et 1 Go de donnees valables en Europe et aux Etats-Unis pour la configuration initiale et l'activation des profils eSIM. Cette offre est concue pour telecharger de nouveaux profils eSIM lorsque vous arrivez a destination sans acces a Internet.

Si vous avez deja utilise les donnees gratuites prechargees, ou si elles ont expire et que vous souhaitez continuer a utiliser le service, vous pouvez recharger votre Seed Profile.

Dans la section **Seed Profile**, cliquez sur le bouton **Top-up** a droite.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Dans la fenetre contextuelle, scannez le QR code et suivez les instructions pour finaliser la recharge.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Acheter un profil eSIM

Vous pouvez acheter des profils eSIM dans nos boutiques recommandees, dans des boutiques testees, ou aupres d'autres fournisseurs eSIM tiers.

??? note "Option 1: Acheter dans nos boutiques recommandees"

    Il y a deux boutiques recommandees : [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} et [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Dans la section **Normal Profile**, cliquez sur **eSIM Profile Recommended Store** a droite.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Scannez le QR code ou cliquez sur les liens pour acheter des profils eSIM.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Note** : Tous les forfaits eSIM achetes dans ces deux boutiques sont entierement compatibles avec les routeurs GL.iNet. Si vous avez des questions, contactez notre equipe support a [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Option 2: Acheter dans des boutiques testees"

    Consultez [ce lien](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} pour voir la liste des boutiques testees par GL.iNet.

    **Note** : Nous ne pouvons pas garantir une compatibilite totale avec les routeurs GL.iNet pour tous les profils ou forfaits provenant de ces boutiques. Comme GL.iNet n'a pas de partenariat avec elles, nous ne pouvons ni fournir de support apres-vente ni aider pour les remboursements.

??? note "Option 3: Acheter aupres d'autres fournisseurs eSIM tiers"

    Vous pouvez aussi choisir d'acheter des profils eSIM aupres d'autres fournisseurs tiers.

    Cependant, nous ne pouvons pas garantir une compatibilite totale avec les routeurs GL.iNet pour les profils eSIM achetes aupres d'autres fournisseurs tiers. Effectuez votre achat a votre propre discretion. GL.iNet n'est pas responsable des problemes d'incompatibilite.

    Pour le support apres-vente ou les remboursements, contactez le fournisseur eSIM concerne.

### Televerser un profil eSIM

Apres avoir achete un profil eSIM, vous recevrez en general un QR code ou un code d'activation. Enregistrez ce QR code en local, puis suivez les etapes ci-dessous pour televerser votre profil eSIM.

1. Dans la section **Normal Profile**, cliquez sur **Add eSIM Profile** en bas.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Televersez votre QR code eSIM ou saisissez le code d'activation, puis cliquez sur **Install**. Le profil eSIM sera alors telecharge et installe sur votre routeur.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Note :**

    1. La plupart des profils eSIM ne peuvent etre telecharges et installes qu'une seule fois.

    2. Un QR code correctement formate affichera un code d'activation commencant par **LPA:**. Cependant, certains QR codes non standard peuvent ne fournir qu'un code brut sans le prefixe LPA. Dans ce cas, ajoutez manuellement `LPA:` au debut du code avant de cliquer sur **Install**.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Si vous n'avez encore achete aucun profil eSIM, vous pouvez en acheter un depuis **eSIM Profile Recommended Store**. Cliquez [ici](#acheter-un-profil-esim) pour les details.

3. Activez votre profil eSIM.

    Une fois le televersement termine avec succes, votre nouveau profil eSIM apparaitra dans la liste **Normal Profile**. Cliquez sur **Enable** pour l'activer.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Connectez-vous a Internet.

    Apres avoir active votre profil eSIM, allez dans **INTERNET** -> **Cellular**. Cliquez sur **Connect** pour etablir une connexion Internet via votre profil eSIM.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Note** : Certains profils eSIM peuvent necessiter des parametres supplementaires, comme l'APN, le PIN ou le TTL. Si necessaire, cliquez sur **Manual Setup** ou **SIM Card Settings** pour ajuster ces parametres. Dans certains cas, un redemarrage de l'appareil peut etre necessaire pour etablir la connexion Internet.*

5. Une fois que le routeur se connecte avec succes via le profil eSIM, la page s'affiche comme suit :

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Exporter les journaux pour le support

Cliquez sur **Export Log for Support** pour afficher tous les journaux lies a l'eSIM. Si vous rencontrez des problemes et avez besoin d'une assistance technique, exportez les journaux eSIM et envoyez-les a notre equipe support par e-mail a [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Articles associes :

- [Comment utiliser la carte physique eSIM avec les routeurs GL.iNet ?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Comment utiliser la carte physique eSIM avec les appareils Android ?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Vous avez encore des questions ? Visitez notre [Community Forum](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
