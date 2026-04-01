# Guide de dépannage du réseau cellulaire

Si vous ne parvenez pas à établir une connexion cellulaire, veuillez vérifier les points suivants.

??? "Vérifier le matériel de l'appareil"

    **1.1** Utilisez un adaptateur secteur standard pour votre appareil. Les adaptateurs secteur non standard peuvent entraîner une alimentation insuffisante.
    
    **1.2** Assurez-vous que **Modem name**, **IMEI** et **SIM ICCID** s'affichent dans le panneau d'administration Web.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}
    
    Pour le firmware version 4.8 et ultérieure, cliquez sur **View More Information** pour trouver le SIM ICCID.

    Si vous ne les trouvez pas, redémarrez votre routeur. Si le nom du modem et l'IMEI ne sont toujours pas reconnus, veuillez nous contacter à [support@gl-inet.com](mailto:support@gl-inet.com).
    
    **1.3** Cliquez sur **View More** pour vérifier **Cells Info** et confirmer que le signal est stable. Si le signal est très faible, assurez-vous que les antennes sont correctement installées, ou déplacez le routeur vers une zone où le signal est bon, puis réessayez.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** Cliquez sur **View More** pour vérifier si la bande de fréquences prise en charge par votre appareil est compatible avec votre région.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Vérifier les paramètres logiciels"

    **2.1** Connectez-vous au panneau d'administration Web et assurez-vous que le programme de connexion cellulaire a bien démarré. Vous pouvez également cliquer sur **Abort**, puis sur **Connect**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** Certains opérateurs mobiles peuvent exiger le **protocole 3G** pour établir la connexion. Passez au protocole 3G et réessayez.

    Pour le firmware version 4.7 et antérieure, allez dans **Manual Setup** -> **Protocol**, sélectionnez **3G**, puis cliquez sur **Apply**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    Pour le firmware version 4.8 et ultérieure, allez dans **SIM Card Settings** -> **Protocol**, sélectionnez **3G**, puis cliquez sur **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    L'appareil se reconnectera automatiquement. Attendez quelques minutes pour vérifier si la connexion a réussi.

    **2.3** Certaines cartes SIM exigent un APN spécifique. Si votre carte SIM ne parvient pas à s'enregistrer, contactez votre opérateur pour vérifier s'il existe des restrictions. Configurez l'APN correct sur votre routeur si nécessaire, puis cliquez sur **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** Activez **Band Maksing** et réessayez. Pour le firmware version 4.7 et antérieure, reportez-vous à [ce lien](../interface_guide/internet_cellular_v4.7.md/#band-masking). Pour le firmware version 4.8 et ultérieure, reportez-vous à [ce lien](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Verrouillez ou déverrouillez une antenne relais et réessayez. Cette fonctionnalité est disponible uniquement sur les GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) et GL-X2000 (Spitz Plus). Cliquez [ici](../interface_guide/internet_cellular.md/#lock-tower) pour plus d'instructions.
    
    Le verrouillage sur une antenne relais spécifique permet au routeur d'accéder à une ressource réseau de haute qualité et de maintenir une connectivité cellulaire stable.
    
    Cependant, une fois qu'une antenne relais est verrouillée, le routeur continuera d'essayer de s'y reconnecter après un redémarrage, même s'il est déplacé vers un nouvel emplacement. Cela peut empêcher le routeur de se connecter automatiquement au réseau cellulaire. Dans ce cas, vous pouvez soit déverrouiller l'antenne relais actuelle via le panneau d'administration Web du routeur, soit la verrouiller manuellement sur une nouvelle antenne relais.

    **Remarque :** L'antenne relais verrouillée doit correspondre aux bandes de fréquences prises en charge par votre opérateur et votre appareil ; sinon, la connexion peut échouer.

??? "Vérifier la compatibilité de la carte SIM"
    
    **3.1** Confirmez le type de carte SIM. Les routeurs cellulaires GL.iNet sont certifiés comme appareils IoT. En théorie, l'appareil ne prend en charge que les cartes SIM de type IoT. Si vous n'êtes pas sûr du type de carte SIM, veuillez contacter votre opérateur.
    
    Les types de carte SIM courants comprennent : data-only, data-only + voice, IoT et hotspot. Nous recommandons d'utiliser des cartes SIM IoT ou hotspot. Le fonctionnement des cartes SIM data-only ou data-only + voice n'est pas garanti.
    
    **3.2** Certaines cartes SIM doivent d'abord être activées. Assurez-vous que la carte SIM peut accéder à Internet lorsqu'elle est insérée dans un téléphone, puis placez-la dans le routeur.
    
    **3.3** Certaines cartes SIM personnalisées ne peuvent être utilisées que sur des téléphones mobiles ou des appareils spécifiques. Veuillez vérifier si la carte SIM est verrouillée sur un appareil particulier.
    
    **3.4** Dans certains États ou certaines villes des États-Unis (par exemple, AT&T à Seattle), il peut être nécessaire d'enregistrer l'IMEI de l'appareil auprès de votre opérateur. Si vous n'êtes pas sûr de cet enregistrement, veuillez contacter votre opérateur.
    
    **3.5** Si le panneau d'administration Web affiche "SIM card not registered", essayez d'abord les étapes ci-dessus.

    Nous vous recommandons d'éteindre le routeur, d'insérer la carte SIM, puis de redémarrer le routeur. Certains modèles ne prennent pas en charge le hot swap et peuvent ne pas détecter la carte SIM si elle est insérée alors que l'appareil est sous tension.

    Assurez-vous que toutes les antennes sont correctement installées, puis testez à nouveau en extérieur dans une zone où le signal cellulaire est fort. Un signal faible peut empêcher la carte SIM de s'enregistrer sur le réseau.

    Si le problème persiste, la carte SIM peut être incompatible avec le routeur. Contactez votre opérateur réseau pour obtenir une assistance complémentaire.

    Si votre opérateur confirme que le problème n'est pas lié à la carte SIM, veuillez contacter notre équipe d'assistance à [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Si la carte SIM peut s'enregistrer et obtenir une adresse IP mais ne peut pas accéder à Internet (l'envoi fonctionne mais pas le téléchargement), elle est très probablement restreinte par votre opérateur réseau. Contactez votre opérateur pour lever cette restriction, ou définissez le TTL sur 65 et testez à nouveau comme indiqué ci-dessous.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    Lorsque vous contactez votre opérateur réseau, veuillez fournir le nom du modem de l'appareil, l'IMEI, le SIM ICCID et le modèle du routeur.
    
Si aucune des solutions ci-dessus ne résout le problème, veuillez contacter notre équipe d'assistance à [support@gl-inet.com](mailto:support@gl-inet.com).
