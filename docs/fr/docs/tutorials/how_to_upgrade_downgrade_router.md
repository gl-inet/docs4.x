# Comment mettre à niveau ou rétrograder manuellement le firmware de votre routeur (de v4.x à v4.x) ?

Ce tutoriel vous montre **comment mettre à niveau ou rétrograder manuellement le firmware de votre routeur (de v4.x à v4.x)**. Les étapes pour mettre à niveau et rétrograder manuellement le firmware de votre routeur sont identiques.

!!! Note "À propos de la mise à niveau et de la rétrogradation du firmware de votre routeur"

    **Mise à niveau :** Les routeurs GL.iNet exécutant la version de firmware 4.x n'offrent pas la fonctionnalité de mise à jour automatique. 
    
    Lorsqu'une nouvelle version de firmware est disponible, vous verrez l'invite « Upgrade Reminder » après vous être connecté au panneau d'administration du routeur. Vous pouvez cliquer sur le bouton **Upgrade** pour installer la dernière version de firmware répertoriée. Si vous avez une version de firmware spécifique vers laquelle vous souhaitez mettre à niveau, suivez les étapes ci-dessous pour mettre à niveau votre routeur manuellement. 

    **Rétrogradation :** Vous pouvez rétrograder le firmware de votre routeur pour résoudre certains problèmes.

## 1. Vérifier si votre routeur exécute la dernière version du firmware (uniquement pour la mise à niveau)

1. Dans un navigateur web, entrez l'URL du panneau d'administration de votre routeur (par exemple, 192.168.8.1) et connectez-vous.
2. Dans la barre latérale gauche, sélectionnez **SYSTEM** > **Upgrade**.  

## 2. Télécharger le fichier de firmware

1. Dans la barre de recherche du [centre de téléchargement de firmware](https://dl.gl-inet.com/), recherchez et sélectionnez le modèle de votre routeur.
2. Dans l'onglet **Stable** ou d'autres onglets, sélectionnez **Download for common upgrade and uboot** à côté de la version de firmware que vous souhaitez télécharger. 

## 3. Téléverser le firmware

Les instructions suivantes ont été rédigées pour téléverser votre firmware via le panneau d'administration du routeur. (Pour téléverser votre firmware via l'application mobile GL.iNet, [téléchargez l'application](https://www.gl-inet.com/app/) et configurez-la.)

1. Dans un navigateur web, entrez l'URL du panneau d'administration de votre routeur (par exemple, 192.168.8.1) et connectez-vous. 
2. (Facultatif) Si vous souhaitez sauvegarder vos paramètres actuels, suivez les étapes ci-dessous.

    ??? "Sauvegarder vos paramètres actuels"

        a. Dans la barre latérale gauche, cliquez sur **SYSTEM** > **Advanced Settings**. 

        b. Cliquez sur le lien ou le bouton **Go To LuCI** pour accéder à la page de connexion LuCI. 

        c. Entrez le mot de passe administrateur, puis cliquez sur **Log in**. 

        d. Cliquez sur **System** > **Backup / Flash Firmware**. 

        e. Sous **Backup**, cliquez sur **Generate archive**. Un fichier contenant vos paramètres actuels sera téléchargé sur votre appareil. 
        
        **Veuillez noter que ce fichier est uniquement applicable à la version du firmware au moment de la sauvegarde et non à d'autres versions de firmware.**

3. Dans la barre latérale gauche, cliquez sur **SYSTEM** > **Upgrade**. 
4. Cliquez sur **Local Upgrade** et sélectionnez le fichier que vous avez téléchargé précédemment. 
5. Pour conserver vos paramètres actuels (par exemple, votre mot de passe administrateur du routeur), basculez **Keep Settings** sur activé. 
6. Cliquez sur **Install**.

**Note :** Pendant le processus de mise à niveau, n'éteignez pas le routeur. Une fois la mise à niveau terminée, vous verrez l'écran de connexion du routeur. 

Si vous avez perdu les paramètres du routeur pendant le processus de mise à jour du firmware, restaurez les paramètres de votre routeur. 

Si la méthode ci-dessus ne fonctionne pas, essayez de mettre à niveau le firmware via [U-boot](../faq/debrick.md).

---

Vous avez encore des questions ? Visitez notre [Forum Communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
