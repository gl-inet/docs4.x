# Comment configurer et utiliser Spitz AX (GL-X3000) dans votre véhicule de loisirs

Ce guide vous montre comment configurer et utiliser Spitz AX dans votre véhicule de loisirs. Avant de commencer, vous aurez peut-être besoin de préparer les équipements et services supplémentaires suivants : 

- Carte(s) SIM ou câble USB (pour le partage de connexion), selon la méthode de connexion Internet que vous utilisez. Si vous utilisez une ou plusieurs cartes SIM, demandez l’APN à votre opérateur. 
- Une antenne de toit si vous souhaitez une meilleure couverture. 
- [Un abonnement Starlink](https://www.starlink.com/roam), si vous vous rendez dans des zones sans couverture cellulaire. 

---

## 1. Installez votre Spitz AX et les autres équipements

Avant de prendre la route, configurez votre Spitz AX en suivant ces étapes.

### Étape 1 : Choisir l’emplacement de votre Spitz AX 

Il est recommandé de choisir un emplacement central et dégagé afin d’obtenir une couverture maximale. Assurez-vous que l’emplacement se trouve à moins d’un mètre de la source d’alimentation, ce qui correspond à la longueur du câble de l’adaptateur secteur. 

![location](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-power-source.jpg){class="glboxshadow"}

Vous pouvez placer votre Spitz AX sur une surface plane ou le fixer au mur. Si vous choisissez de le fixer au mur, suivez l’étape suivante. 

### (Facultatif) Étape 2 : Installer votre Spitz AX au mur 

Il existe deux façons d’installer votre Spitz AX au mur :
- Utiliser le patin adhésif fourni
- Utiliser les supports muraux

Les supports muraux sont fournis dans l’emballage. Pour fixer votre Spitz AX au mur, suivez les étapes ci-dessous :

1. Fixez le support au mur à l’aide de vis.
2. Enclenchez votre Spitz AX sur le support. 

![wall mount](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-screws.jpg){class="glboxshadow"}

### (Facultatif) Étape 3 : Installer l’antenne de toit du véhicule de loisirs

![roof](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-roof-antenna.jpg){class="glboxshadow"}

Pour obtenir un meilleur signal, utilisez une antenne de toit avec votre Spitz AX. Nous vous recommandons d’utiliser [l’antenne multibande LTMG942 de MobileMark](https://www.mobilemark.com/product/ltmg942-4xlte-2xwifi-gnss/), qui offre un signal réseau optimal. Si vous souhaitez utiliser des antennes de toit d’autres marques, assurez-vous qu’elles répondent aux exigences suivantes : 

- 4 antennes cellulaires, plage de fréquences de réception 600M~6GHz.
- 2 antennes Wi-Fi, plage de fréquences de réception : 2.4G~2.5GHz, 5.15~5.84GHz

![antennas](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-six-antennas.jpg){class="glboxshadow"}

**Note:** Vous pouvez utiliser une antenne 7-en-1 (qui comprend une antenne GPS), mais vous n’aurez besoin de connecter que les six antennes sur votre Spitz AX. L’interface DIV/GNSS du Spitz AX prend en charge les signaux GPS, car l’antenne cellulaire (plage de réception de 600M~6GHz) couvre la fréquence du GPS. Spitz AX permet de consulter votre position GPS via la ligne de commande, mais ne prend actuellement pas en charge l’affichage de votre position sur la carte.

Pour éviter l’atténuation du signal, le câble radiofréquence reliant l’antenne de toit à votre Spitz AX ne doit pas dépasser 5 mètres. (Par exemple, lorsque le câble radiofréquence de MobileMark mesure 5 mètres de long, la réception du signal à 3000MHz est réduite de 3dB, soit la moitié de la puissance. Plus la fréquence du signal est élevée, plus l’atténuation est importante.)

[Découvrez comment remplacer les antennes sur Spitz AX.](https://docs.gl-inet.com/router/en/4/tutorials/how_to_change_x3000_and_xe3000_antennas/) 

---

## 2. Configurer Internet pour votre Spitz AX 

Pour vous assurer d’avoir un accès à Internet pendant votre trajet, configurez Internet à l’aide de cartes SIM. 

Spitz AX intègre un module 5GNR et prend en charge deux cartes SIM. Les différents opérateurs mobiles proposent des forfaits cellulaires différents pour les cartes SIM et utilisent des APN différents. Vous devrez saisir l’APN dans les paramètres, alors vérifiez auprès de votre opérateur quelle valeur APN utiliser. 

Pour configurer vos cartes SIM, suivez ces étapes : 

1. Insérez votre ou vos cartes SIM. 
![insert sim](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/x3000-with-sim-card.jpg){class="glboxshadow"}
2. Branchez l’adaptateur secteur et allumez le routeur. 

Pour saisir votre APN, suivez ces étapes : 

1. Saisissez `192.168.8.1` dans un navigateur web et connectez-vous. 
2. Le nom de votre opérateur devrait s’afficher dans le coin supérieur gauche. Cliquez sur **Manual Setup**.
3. À côté de **APN**, saisissez l’APN. 
4. Cliquez sur **Apply**. 

Si vous utilisez deux cartes SIM, notez qu’une seule carte SIM fonctionne à la fois. Vous pouvez sélectionner manuellement la carte SIM à utiliser à chaque fois. Vous pouvez également activer la [fonction Auto Switch](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#setup-for-dual-sim-models). Si le routeur détecte que l’une des cartes SIM ne peut pas accéder correctement à Internet, il basculera automatiquement vers l’autre carte SIM. La commutation prend environ 1 minute. 

---

## 3. Utiliser Spitz AX dans différents scénarios

### Sur la route

![on the road](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_rv-antennas.png){class="glboxshadow"}

Lorsque vous roulez, vous devriez pouvoir vous connecter à Internet via la ou les cartes SIM que vous avez configurées à l’étape précédente.

### Au camping

![campground](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_repeater.png){class="glboxshadow"}

Si vous faites une halte dans un camping pendant votre voyage, vous pouvez utiliser le réseau Wi-Fi public fourni sur place afin d’économiser vos données cellulaires. [Découvrez comment vous connecter à un réseau Wi-Fi existant.](https://docs.gl-inet.com/router/en/4/interface_guide/internet_repeater/) 

Après vous être connecté une première fois au réseau Wi-Fi, Spitz AX peut mémoriser le nom du réseau et le mot de passe. Il se reconnectera automatiquement au réseau la prochaine fois que vous serez à proximité.

### Dans les zones sans couverture cellulaire

![cellular](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_and_use_in_recreational_vehicle/rv-connectivity_scene_starlink.png){class="glboxshadow"}

Si vous vous rendez dans une zone sans couverture cellulaire (par exemple une zone désertique peu peuplée), utilisez Starlink, un service Internet par satellite. Ainsi, dans les zones bénéficiant d’une bonne couverture cellulaire, utilisez le signal 5G reçu par le Spitz AX et, dans les zones sans couverture cellulaire, utilisez Starlink.

Lorsque vous installez l’antenne Starlink, assurez-vous qu’elle n’est pas obstruée. Les obstacles des deux côtés de la route (par exemple les arbres) affecteront la réception, essayez donc de vous garer à l’écart de tout obstacle. 

---

## 4. Définir les priorités de basculement 
Spitz AX prend en charge le multi-WAN (basculement et équilibrage de charge). Vous pouvez définir des priorités de basculement pour différents réseaux selon votre scénario. 

| Scénario| Priorité |
| --------| ------- |
| Au camping (connecté à son réseau Wi-Fi via le mode répéteur)    | <p>Attribuez une priorité plus élevée au répéteur qu’au réseau cellulaire.</p> <p>Dès que vous quittez le camping, votre routeur basculera automatiquement vers le réseau cellulaire.</p>|
| Starlink (Ethernet) + réseau cellulaire | Attribuez une priorité plus élevée au réseau cellulaire qu’à Ethernet. <p>Dans les zones avec couverture cellulaire, votre routeur utilisera votre réseau cellulaire.</p> <p>Lorsque vous arrivez dans des zones sans couverture cellulaire, votre routeur basculera automatiquement vers Starlink via Ethernet.</p>|

Pour configurer le basculement, consultez la section [Failover](https://docs.gl-inet.com/router/en/4/interface_guide/multi-wan/).

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
