# Contrôle parental

Le contrôle parental permet d'aider les enfants à naviguer en ligne en toute sécurité en bloquant les sites inappropriés et en limitant la durée d'utilisation des appareils. Il permet d'empêcher l'accès aux contenus nuisibles, de gérer le temps d'écran et de favoriser une utilisation responsable d'Internet.

Cette fonctionnalité est disponible depuis le firmware v4.2. **Remarque** : certains modèles, bien qu'ils exécutent le firmware v4.2 ou une version ultérieure, ne prennent pas en charge le contrôle parental en raison d'une mémoire insuffisante.

Regardez cette vidéo ou suivez les étapes ci-dessous pour configurer le contrôle parental sur les routeurs GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Version locale

La version locale est fournie par GL.iNet. Elle est actuellement en bêta et n'entraîne aucun coût supplémentaire. Dans cette version, si vous devez filtrer les requêtes par application, vous devez saisir le domaine manuellement.

### Modèles pris en charge

??? "Modèles pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Modèles non pris en charge"
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

### Étapes de configuration

Connectez-vous au panneau d'administration web du routeur, puis accédez à **APPLICATIONS** -> **Parental Control**. 

Pour le firmware ver.4.8.4 et les versions ultérieures, accédez à **FLOW CONTROL** -> **Parental Control**.

Assurez-vous que l'heure du routeur est correcte. Si ce n'est pas le cas, allez dans **SYSTEM** -> **Time Zone** pour la synchroniser d'abord.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Activez Parental Control puis cliquez sur **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices** : bloque l’accès à Internet pour tous les appareils qui ne figurent pas dans la liste de Parental Control.

Suivez ensuite l'assistant de configuration pour configurer le contrôle parental.

---

Voici un cas d'usage à titre de référence. Vous pouvez adapter les paramètres selon vos besoins.

**Scénario** : les appareils du profil peuvent accéder à Internet uniquement pour étudier de 8 h à 11 h les jours de semaine, et pour jouer de 18 h à 20 h le week-end. À tous les autres moments, l'accès à Internet est bloqué par défaut.

Suivez les étapes ci-dessous pour configurer Parental Control.

1. Créez un profil et personnalisez son nom.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Sélectionnez les appareils que vous souhaitez gérer. Vous devez d'abord les connecter au routeur. S'ils ne se sont pas encore connectés au routeur, ajoutez-les manuellement en saisissant leurs adresses MAC.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Définissez les limites d'accès.

    Deux ensembles de règles sont fournis par défaut : **Block Internet Access** et **No Limit**.

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Cliquez sur **Add a New Ruleset** pour créer ensuite deux ensembles de règles supplémentaires pour une utilisation ultérieure : **Learning** et **Play**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Spécifiez le nom de l'ensemble de règles (par exemple, Learning), sa couleur, puis saisissez les sites que vous souhaitez bloquer avant de cliquer sur **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Note** : les noms de domaine saisis dans la liste de blocage doivent inclure leurs sous-domaines. Par exemple, si vous saisissez "example.com", cela inclut également tous les sous-domaines, tels que "subdomain.example.com".

    Créez de la même manière un autre ensemble de règles. Spécifiez le nom de l'ensemble de règles (par exemple, Play), sa couleur, puis saisissez les sites que vous souhaitez bloquer avant de cliquer sur **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    Une fois l'opération appliquée, vous disposerez de quatre ensembles de règles au total. Veillez à sélectionner **Block Internet Access** comme **Default Ruleset**, puis cliquez sur **Finish**.

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Définissez ensuite l'horaire de votre profil. Cliquez sur **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    Ajoutez l'ensemble de règles **Learning** à l'horaire. Réglez **Execution Time** de 8 h à 11 h en semaine, puis cliquez sur **Apply**.

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. Vous serez ensuite redirigé vers la page de modification du profil nouvellement créé.

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Descendez en bas de la page ; vous verrez qu'un horaire a été créé. Cliquez sur l'icône d'engrenage en haut à droite, puis sélectionnez **Add Schedule**.

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Ajoutez un autre ensemble de règles, **Play**, à l'horaire. Réglez **Execution Time** de 18 h à 20 h le week-end, puis cliquez sur **Apply**.

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    L'ensemble de règles **Play** sera alors ajouté à l'horaire.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Note** : la ligne rouge en pointillés indique l'heure actuelle.

    Vous pouvez également modifier la période d'exécution en cliquant sur un ensemble de règles dans l'horaire.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Cliquez sur **Parental Control** en haut pour revenir à la page Parental Control.

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    Vous verrez la configuration finale. Le contrôle parental est désormais appliqué selon l'horaire défini. Vous pouvez modifier les profils et ensembles de règles existants, ou en ajouter de nouveaux si nécessaire.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Dépannage

Si les paramètres que vous avez configurés ne prennent pas effet, vérifiez les causes possibles suivantes.

1. Problème de cache DNS.
  
    Les navigateurs et les systèmes d'exploitation conservent des caches DNS ; les modifications de configuration peuvent donc mettre un certain temps à prendre effet. Videz le cache DNS pour appliquer les changements immédiatement.
  
      * [Vider le cache DNS dans Chrome sur ordinateur](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Vider le cache DNS dans Edge sur ordinateur](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. L'horaire du profil n'a pas encore démarré.

3. Le nom de domaine saisi est peut-être incorrect.

    Le domaine public d'un site web est facile à trouver, mais les domaines d'API utilisés par les applications ne sont souvent pas publics. Pour identifier le bon domaine, utilisez un outil de capture de paquets comme Wireshark ou recherchez les informations de domaine concernées.

    Par exemple, pour bloquer `www.google.com`, il est plus efficace d'utiliser `google.com` que `www.google.com`.

4. L'appareil cible utilise une adresse MAC aléatoire pour chaque connexion réseau, ce qui empêche l'application des règles d'accès. Désactivez l'adresse MAC aléatoire sur l'appareil cible, puis ajoutez-le de nouveau à votre profil.

## Version Bark

La version [Bark](https://www.bark.us/){target="_blank"}, qui est fournie et gérée par Bark sur sa propre plateforme, permet de filtrer les applications et les sites web en un clic et de surveiller l'historique des requêtes. 

Elle offre une fonction de surveillance pour plus de 24 applications populaires et plateformes de réseaux sociaux, qui figurent dans la liste prédéfinie de notre fonctionnalité locale de contrôle parental.

Grâce à sa fonction de journalisation, elle enregistre quel client a accédé à quel site web et à quel moment. Cela permet aux parents de consulter facilement les journaux, d'identifier les sites web qui ne figurent pas sur la liste noire et de les ajouter rapidement au périmètre de gestion.

La fonction Bark Parental Control est disponible depuis le firmware v4.5 et n'est prise en charge que sur certains routeurs GL.iNet.

**Note** : 

1. Le service Bark est disponible **uniquement aux États-Unis, en Australie et en Afrique du Sud**. Cliquez [ici](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} pour plus de détails.

2. Le service Bark nécessite généralement un abonnement payant. Toutefois, dans le cadre de notre partenariat avec Bark, GL.iNet propose gratuitement le forfait Bark Home sur certains modèles de routeur, avec surveillance avancée et alertes sans frais supplémentaires.

3. Les deux versions de Parental Control ne peuvent pas être activées en même temps. Le passage de l'une à l'autre désactive automatiquement l'autre version.

### Modèles pris en charge

??? "Modèles pris en charge"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)

??? "Modèles non pris en charge"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
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

### Étapes de configuration

Connectez-vous au panneau d'administration web du routeur, puis accédez à **APPLICATIONS** -> **Parental Control**. 

Sélectionnez la version Bark, activez l'interrupteur, puis cliquez sur **Apply**. 

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Note:** le service Bark peut ne pas être disponible dans certains pays. Comme GL.iNet n'est pas le fournisseur de ce service, si vous rencontrez un problème lors de l'utilisation de Bark, veuillez contacter directement le [support technique de Bark ](https://www.bark.us/contact-us/?ref=glinet&home=glinet) pour obtenir de l'aide.

Le service Bark est activé, mais cet appareil n'est pas encore associé à un compte. Veuillez utiliser le [Device Pairing Link](https://www.bark.us/app/signup/?ref=glinet&home=glinet) pour associer cet appareil à votre compte Bark.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Une fois l'association effectuée, la page s'affiche comme suit.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Votre appareil est désormais connecté à Bark Cloud Services et associé à votre compte. Veuillez [aller sur Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) et vous connecter à votre compte pour créer un profil de contrôle du réseau.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
