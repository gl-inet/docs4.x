# Comment mettre à niveau vers le firmware 4.x ?

**Ce document est obsolète et n'est plus maintenu. Cliquez [ici](../interface_guide/upgrade.md) pour consulter le guide de mise à niveau le plus récent.**

---

Suivez les étapes ci-dessous pour mettre à niveau votre routeur du firmware 3.x vers le firmware 4.x.

Remarque : ne conservez pas les paramètres lors de la mise à niveau de la version 3.x vers la version 4.x, car cela peut entraîner une instabilité. Sauvegardez tous les paramètres importants avant la mise à niveau.

Les GL-B1300 et GL-S1300 ne prennent pas en charge la fonction mesh avec le firmware v4.x.

---

## Méthode 1. Mise à niveau locale

Vous pouvez mettre à niveau le firmware via le panneau d'administration web.

1. Mettez à niveau le firmware vers la dernière version stable 3.x.

2. Téléchargez le firmware 4.x [ici](https://dl.gl-inet.com){target="_blank"}. Assurez-vous de **télécharger celui destiné à une mise à niveau standard**.

3. Connectez-vous au panneau d'administration web, puis allez dans **Upgrade** -> **Local Upgrade**. Importez le fichier du firmware que vous venez de télécharger.

    **Remarque :** le firmware 4.x n'est pas compatible avec le firmware 3.x. Lors d'une mise à niveau depuis le firmware 3.x, ne conservez **PAS** les paramètres.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/gl-ax1800_upgrade_to_4/ax1800_upgrade_4.png){class="glboxshadow gl-90-desktop"}

## Méthode 2. Mise à niveau via U-Boot

1. Téléchargez le firmware 4.x [ici](https://dl.gl-inet.com){target="_blank"}. Assurez-vous de **télécharger celui destiné à U-Boot**.

2. Reportez-vous à ce guide [U-Boot](debrick.md) pour flasher le firmware.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
