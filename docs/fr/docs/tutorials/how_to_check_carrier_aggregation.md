# Comment vérifier l'état de l'agrégation de porteuses sur votre routeur cellulaire

L'agrégation de porteuses combine plusieurs bandes réseau pour offrir une bande passante plus élevée et des vitesses plus rapides à votre connexion cellulaire.

Cette fonctionnalité ne peut pas être activée dans le panneau d'administration Web du routeur, car elle dépend de la prise en charge de votre opérateur mobile.

Cependant, vous pouvez vérifier l'état de l'agrégation de porteuses à l'aide des commandes AT dans le panneau d'administration Web du routeur.

!!! note "Supported Models"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Suivez les étapes ci-dessous pour vérifier l'état de l'agrégation de porteuses.

1. Insérez une carte SIM dans le routeur. 
2. Ouvrez un navigateur Web, saisissez `192.168.8.1` dans la barre d'adresse, puis connectez-vous. 
3. Accédez à la section **INTERNET** -> **Cellular**, cliquez sur l'icône à trois points en haut à droite, puis cliquez sur **Modem AT Command**. 
    
    ![Modem AT Command](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. Dans la fenêtre contextuelle, saisissez **AT+QCAINFO**, puis cliquez sur **Send**.

    Si l'agrégation de porteuses est active, plusieurs bandes réseau apparaîtront dans la liste. 
    
    ![atcainfo](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
