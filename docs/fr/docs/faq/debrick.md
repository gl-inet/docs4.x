# Utiliser U-Boot pour débricker votre routeur

Si votre routeur est devenu inutilisable à cause de certains projets DIY ou du flash d'un mauvais firmware, vous risquez de ne plus pouvoir y accéder. Dans ce cas, vous pouvez réinstaller le firmware en utilisant le mode failsafe U-Boot.

**Remarque :** L'opération U-Boot supprimera les paramètres de votre routeur ainsi que les plug-ins installés.

---

## Préparation

Préparez un ordinateur avec un port Ethernet. Si votre ordinateur ne dispose pas d'un port Ethernet, prévoyez un adaptateur USB Ethernet supplémentaire.

## Étapes pour débricker

Reportez-vous à ce tutoriel vidéo ou suivez les procédures ci-dessous pour accéder à l'interface Web U-Boot et réinstaller le firmware.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Les étapes de réinstallation du firmware avec U-Boot sont globalement les mêmes, et cette vidéo prend Mudi/Mudi V2 comme exemple. Pour les autres modèles, vous pouvez suivre les procédures ci-dessous.</small>

1. Téléchargez le firmware [ici](https://dl.gl-inet.com/){target="_blank"} sur votre ordinateur.

    Certains modèles, comme le GL-AR750S-EXT, sont disponibles en deux formats de firmware. Veuillez utiliser le firmware pour U-Boot, dont l'extension du nom de fichier est **.img**.

2. Coupez l'alimentation du routeur. Connectez votre ordinateur au **port Ethernet LAN** du routeur. Vous **DEVEZ** laisser tous les autres ports **déconnectés**.

    !!! note

        Pour certains modèles, certains ports LAN individuels et le port WAN sont interchangeables. Veuillez ne pas utiliser ce port LAN. Par exemple, sur le GL-MT6000 (Flint 2), n'utilisez pas LAN 1. Utilisez plutôt LAN 2, LAN 3 ou LAN 4.

3. Maintenez fermement le bouton Reset enfoncé et, **en même temps, mettez le routeur sous tension**. Si votre routeur n'a pas de bouton d'alimentation, le fait de brancher l'alimentation l'allumera automatiquement.

    Vous verrez alors la LED clignoter plusieurs fois selon une séquence régulière ; relâchez votre doigt **après** le changement de séquence.

    Voici la description de la séquence de clignotement des LED pour chaque modèle.

    **Remarque :** Un même modèle de routeur peut avoir des couleurs de LED ou des séquences de clignotement différentes selon sa date de fabrication ; cela n'affectera pas le processus U-Boot. Faites surtout attention au changement dans la séquence de clignotement.

    - Pour le **GL-BE9300(Flint 3)**, la LED bleue clignote 6 fois, puis devient blanche fixe.
    
    - Pour le **GL-BE3600(Slate 7)**, après avoir maintenu le bouton Reset enfoncé pendant environ 5 secondes, un compte à rebours de 5 secondes apparaît sur l'écran LED. Continuez à appuyer sur le bouton Reset jusqu'à ce que l'étape suivante s'affiche à l'écran :

        1. Manually set the IP address of your computer to 192.168.1.2
        2. Use browser to visit  http://192.168.1.1

        Passez à l'étape 4 pour la suite des instructions.

    - Pour le **GL-B3000(Marble)**, la LED bleue clignote 7 fois, puis devient blanche fixe.

    - Pour le **GL-MT6000(Flint 2)**, la LED bleue clignote 6 fois, puis devient blanche fixe.

    - Pour le **GL-MT3000(Beryl AX)**, la LED bleue clignote 6 fois, puis devient blanche fixe.

    - Pour le **GL-MT2500/GL-MT2500A(Brume 2)**, la LED bleue clignote 5 fois, puis devient blanche fixe.

    - Pour le **GL-S200**, la LED cyan clignote 5 fois, devient brièvement violette, puis reste cyan fixe.

    - Pour le **GL-A1300(Slate Plus)**, la LED clignote lentement 5 fois, reste allumée un court instant, puis clignote rapidement en continu.

    - Pour les **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)** et **microuter-N300**, la LED clignote 5 fois.

    - Pour le **GL-E750(Mudi)**, son écran affiche d'abord "Booting", puis "Reset Counting 1 to 4", puis enfin "Please Open Web 192.168.1.1".

    - Pour les **GL-S1300(Convexa-S)** et **GL-B1300(Convexa-B)**, la LED clignote 4 fois.
        
        La LED Power la plus à gauche peut rester allumée tout le temps tandis que la LED Wi-Fi la plus à droite clignote 4 fois, puis la LED Mesh du milieu reste allumée en continu.
        
        (Pour certains anciens GL-B1300, la LED Power la plus à gauche reste allumée en permanence, et la LED du milieu ainsi que celle de droite clignotent 5 fois simultanément, puis restent allumées.)

    - Pour le **GL-SF1200**, la LED 5G clignote 5 fois, puis reste allumée en continu.

    - Pour le **GL-AX1800(Flint)**, la LED bleue clignote 5 fois, puis devient blanche fixe.

    - Pour le **GL-AXT1800(Slate AX)**, la LED bleue clignote 5 fois, puis reste allumée en continu.

    - Pour le **GL-XE300(Puli)**, la LED LAN clignote 5 fois, puis la LED Wi-Fi reste allumée.

    - Pour le **GL-X300B(Collie)**, la LED WAN clignote 5 fois, puis la LED Wi-Fi reste allumée.

    - Pour le **GL-X3000(Spitz AX)**, la LED WAN clignote 5 fois, puis la LED Wi-Fi reste allumée.

    - Pour le **GL-XE3000(Puli AX)**, la LED WAN clignote 5 fois, puis la LED Wi-Fi reste allumée.

    - Pour le **GL-SFT1200(Opal)**, la LED bleue clignote 5 fois, puis devient blanche fixe.

    - Pour le **GL-AP1300(Cirrus)**, la LED d'alimentation clignote lentement 5 fois, reste allumée un court instant, puis clignote rapidement en continu.

    - Pour le **GL-MT1300(Beryl)**, la LED est d'abord bleue, clignote deux fois lentement, puis clignote 5 fois plus rapidement et devient blanche fixe.

    - Pour le **GL-B2200(Velica)**, les deux LED sont d'abord bleues, puis deviennent blanches et clignotent 5 fois, avant de devenir bleues fixes.

    - Pour les **GL-MV1000/GL-MV1000W(Brume)**, il n'y a pas de séquence répétée de clignotement des LED. (Les LED Power et WAN restent allumées en permanence.)

    - Pour le **GL-MiFi**, la LED clignote 6 fois.

    - Pour les **GL-MT300N**, **GL-MT300A**, la LED clignote 3 fois.

4. Définissez manuellement l'adresse IP de votre ordinateur sur **192.168.1.2**. Veuillez consulter le guide pas à pas pour les différents systèmes d'exploitation ci-dessous :

    ??? "Windows 7 / Windows 10"

        1. Accédez à **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Faites un clic droit sur **Local Area Connection** -> **Properties**.

        3. Cliquez sur **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Définissez manuellement l'**IP adress** sur `192.168.1.2`.

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

        14. Indiquez le **Subnet mask** comme **255.255.255.0**.

        15. Cliquez sur le bouton **Save**.

    ??? "macOS"
    
        16. Cliquez sur l'icône **Apple** en haut à gauche de l'écran, puis sélectionnez **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Cliquez sur **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Cliquez sur **Ethernet** à gauche, puis cliquez sur la liste déroulante à côté de **Configure IPv4** et sélectionnez **Manually**. Si vous utilisez un adaptateur USB Ethernet, **Ethernet** peut ne pas apparaître et le nom de l'adaptateur USB Ethernet peut s'afficher à la place.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Saisissez **IPv4 Address** = `192.168.1.2`, **Subnet Mask** = `255.255.255.0`, **Router** = `192.168.1.1`, puis cliquez sur le bouton Apply en bas à droite.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Utilisez un navigateur pour accéder à **http://192.168.1.1**. Il s'agit de l'interface Web U-Boot.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note 
    
        - Si vous ne parvenez pas à accéder à l'interface Web U-Boot, vérifiez si un logiciel VPN ou proxy est en cours d'exécution. Désactivez tout logiciel VPN ou proxy, y compris Tailscale et ZeroTier.
    
        - L'interface Web U-Boot ci-dessus peut ne pas être exactement identique à ce que vous voyez, car la version d'U-Boot diffère selon les dates de production. Dans certains cas extrêmes, nous recommandons de mettre à niveau la version d'U-Boot. Veuillez consulter le tutoriel [ici](upgrade_uboot_version.md).

6. Cliquez sur le bouton **Choose file** pour trouver le fichier du firmware. Cliquez ensuite sur le bouton **Update firmware**.

7. Attendez environ 3 minutes. N'éteignez pas votre appareil pendant la mise à jour. Le routeur est prêt lorsque les LED d'alimentation et Wi-Fi sont allumées, ou lorsque vous pouvez trouver son SSID sur votre appareil.

8. Rétablissez le paramétrage IP modifié à l'étape 4 et connectez votre appareil au LAN ou au Wi-Fi du routeur. Vous pourrez de nouveau accéder au routeur via **192.168.8.1**.

    **Remarque :** Il peut être nécessaire d'utiliser le mode navigation privée ou de supprimer le cache et les cookies du navigateur pour accéder au routeur.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
