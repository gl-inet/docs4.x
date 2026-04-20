# Mettre à niveau la version d'U-Boot

## Avertissement

**La mise à niveau d'U-Boot est très dangereuse et n'est généralement pas recommandée. En cas d'échec, votre appareil sera briqué et il n'y aura aucun moyen de le restaurer. Ne procédez ainsi que lorsque c'est nécessaire ou sur instruction du support GL.iNet.**

**NE coupez PAS l'alimentation pendant le processus de mise à niveau, sinon la mise à niveau peut échouer et l'appareil peut être briqué.**

## Préparation

- Un ordinateur avec un port Ethernet. Si ce n'est pas le cas, préparez un adaptateur USB vers Ethernet.
- Un câble Ethernet.
- Téléchargez le fichier U-Boot conformément aux instructions du support GL.iNet. Assurez-vous d'utiliser le bon fichier U-Boot. Si vous ne savez pas comment télécharger le fichier U-Boot, contactez-nous par e-mail à support@gl-inet.com.

## Étapes de mise à niveau

Veuillez suivre la procédure ci-dessous pour accéder à la page de mise à niveau d'U-Boot.

1. Coupez l'alimentation du routeur. Connectez votre ordinateur au **port Ethernet LAN** du routeur. Vous **DEVEZ** laisser **tous les autres ports déconnectés**.

    !!! note

        Sur certains modèles, certains ports LAN individuels et le port WAN sont interchangeables. Veuillez ne pas utiliser ce port LAN. Par exemple, sur le GL-MT6000 (Flint 2), n'utilisez pas LAN 1. Utilisez plutôt LAN 2, LAN 3 ou LAN 4.

2. Maintenez fermement le bouton Reset enfoncé et, en même temps, mettez le routeur sous tension. Si votre routeur n'a pas de bouton d'alimentation, le fait de brancher l'alimentation l'allumera automatiquement.

    Vous verrez alors la LED clignoter plusieurs fois selon une séquence régulière ; relâchez le bouton lorsque la séquence change.

3. Définissez manuellement l'adresse IP de votre ordinateur sur **192.168.1.2**. Consultez le guide pas à pas correspondant à votre système d'exploitation ci-dessous :

    ??? "Windows 7 / Windows 10"

        1. Allez dans **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Cliquez avec le bouton droit sur **Local Area Connection** -> **Properties**.

        3. Cliquez sur **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Définissez manuellement l'**IP address** sur `192.168.1.2`.

        5. Définissez le **Subnet mask** sur `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Cliquez sur le bouton **OK**.

    ??? "Windows 11"

        7. Ouvrez **Settings**.

        8. Cliquez sur **Network & Internet**.

        9. Cliquez sur l'onglet **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Dans la section "IP assignment", cliquez sur le bouton **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Sélectionnez l'option **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Activez le commutateur **IPv4**.

        13. Définissez l'**IP address** statique sur **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Renseignez le **Subnet mask** comme **255.255.255.0**.

        15. Cliquez sur le bouton **Save**.

    ??? "macOS"

        16. Cliquez sur l'icône **Apple** en haut à gauche de l'écran, puis sélectionnez **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Cliquez sur **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Cliquez sur **Ethernet** à gauche, puis sur la liste déroulante à côté de **Configure IPv4** et sélectionnez **Manually**. Si vous utilisez un adaptateur USB vers Ethernet, **Ethernet** peut ne pas apparaître et être remplacé par le nom de l'adaptateur.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Saisissez **IPv4 Address** : `192.168.1.2`, **Subnet Mask** : `255.255.255.0`, **Router** : `192.168.1.1`, puis cliquez sur le bouton Apply en bas à droite.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Utilisez Google Chrome/Microsoft Edge pour ouvrir `http://192.168.1.1/uboot.html`**

    **N'utilisez PAS Mozilla/Firefox, car cela peut briquer votre routeur.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. Cliquez sur le bouton **Choose file**, puis sélectionnez le fichier U-Boot que vous avez téléchargé.

6. Cliquez sur le bouton **Update U-Boot**. NE coupez PAS l'alimentation pendant le processus de mise à niveau. La mise à jour prendra plusieurs minutes.

7. Une fois la mise à jour réussie, le routeur redémarrera. Vous pourrez alors rétablir les paramètres IP modifiés à l'étape 3 et essayer d'accéder au panneau d'administration Web via **192.168.8.1**. Si vous pouvez accéder normalement au panneau d'administration Web, cela signifie que le routeur a redémarré.

    **Remarque :** il peut être nécessaire d'utiliser le mode navigation privée ou de supprimer le cache et les cookies du navigateur pour accéder au routeur.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
