# Contrôle parental (firmware v4.9)

> Ce guide s'applique au firmware v4.9 et aux versions ultérieures. Pour les versions antérieures, veuillez cliquer [ici](parental_control.md).

Dans le panneau d'administration web, accédez à **FLOW CONTROL** -> **Parental Control**.

Le contrôle parental protège les enfants en ligne en bloquant les sites inappropriés et en limitant le temps d'écran. Il filtre les contenus nuisibles et favorise une utilisation responsable d'Internet.

GL.iNet Parental Control propose une planification flexible pour restreindre l'accès à Internet sur les appareils que vos enfants utilisent le plus souvent. Vous pouvez bloquer des applications et des sites web inappropriés en un clic. En outre, vous pouvez saisir manuellement des domaines si nécessaire afin d'obtenir une protection en ligne complète.

La mise en page et le flux de travail de Parental Control ont été améliorés dans le firmware v4.9, ce qui simplifie la configuration et offre une vue plus intuitive des règles.

---

Suivez les étapes ci-dessous pour configurer le contrôle parental.

1. Connectez-vous au panneau d'administration web du routeur et accédez à **FLOW CONTROL** -> **Parental Control**. Vérifiez que l'heure du routeur est correcte.

    ![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/router_time.png){class="glboxshadow"}

    Sinon, allez d'abord dans **SYSTEM** -> **Time Zone** pour la synchroniser.

2. Activez Parental Control puis cliquez sur **Apply**.

    ![enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/enable.png){class="glboxshadow"}

3. Une liste de règles s'affiche alors comme ci-dessous. Cliquez sur **Add a New Rule**.

    ![add a new rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/add_rules.png){class="glboxshadow"}

4. Dans la fenêtre pop-up, créez une règle, définissez un nom personnalisé, puis cliquez sur **Next**.

    ![create a rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. Sélectionnez l'appareil de votre enfant, puis cliquez sur **Next**.

    Un appareil n'apparaît sur cette page que s'il est connecté au routeur via le Wi-Fi ou Ethernet. Le cyan indique un appareil en ligne, tandis que le gris indique qu'il est hors ligne.

    ![select device](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **Conseil** : si vous souhaitez mieux distinguer les appareils connectés, rendez-vous sur la page **CLIENTS** et personnalisez les noms des appareils.

6. Définissez l'heure du coucher pour l'appareil de votre enfant, puis cliquez sur **Next**.

    Pendant cette période, Internet ne sera pas disponible sur les appareils sélectionnés. Par défaut, la même heure du coucher s'applique à tous les jours.

    ![bedtime1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    Si vous souhaitez définir des heures du coucher différentes pour chaque jour de la semaine, sélectionnez **Customize Days**, ajustez les horaires, puis cliquez sur **Next**.

    ![bedtime2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. Sélectionnez le filtre de contenu.

    Trois catégories sont sélectionnées par défaut : **Gambling**, **Malicious Content** et **Sexual Content**.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Vous pouvez sélectionner d'autres catégories si nécessaire, comme **Games**, **Shopping**, **Social Media**, **Entertainment**, etc.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Si une application que vous souhaitez bloquer est difficile à trouver, utilisez la recherche en haut pour la localiser rapidement.

    ![search app](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. Si vous devez bloquer certains domaines, cliquez sur **Advanced Settings** en bas à droite.

    ![block domain1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    Saisissez les domaines manuellement, puis cliquez sur **Finish**.

    ![block domain2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. La règle est maintenant ajoutée. La liste affiche le nom de la règle, le nombre d'appareils connectés, le planning de coucher, les contenus filtrés et l'état de la règle (activée/désactivée).

    ![rules added](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/rules_added.png){class="glboxshadow"}

    Vous pouvez effectuer des opérations de base sur les règles existantes : Modify, Copy et Delete.

    ![action](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action.png){class="glboxshadow"}

    - **Modify** : modifie les appareils sélectionnés, les heures du coucher et les règles du filtre de contenu.

        ![action modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_modify.png){class="glboxshadow"}

    - **Copy** : crée une copie d'une règle existante pour éviter de tout reconfigurer manuellement.

        ![action copy](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/4.9/action_copy.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [Community Forum](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.