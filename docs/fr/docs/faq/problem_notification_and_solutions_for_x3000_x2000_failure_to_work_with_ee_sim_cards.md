# Notification de problème et solutions pour les GL-X3000/GL-XE3000/GL-X2000 qui ne fonctionnent pas avec les cartes SIM EE

Chers clients GL.iNet,

Nous avons récemment constaté que certains clients rencontraient des échecs de connectivité sur les GL-X3000/GL-XE3000/GL-X2000 lors de l'utilisation de cartes SIM EE. Après des investigations supplémentaires, nous avons découvert que certaines cartes SIM EE ne prennent en charge que le protocole IPv4. Or, les paramètres par défaut des routeurs cellulaires GL.iNet activent simultanément IPv4 et IPv6, ce qui provoque ce problème.

## Solutions et contournements

1. **Mise à jour du firmware**

    Nous avons publié de nouvelles mises à jour du firmware qui remplacent le protocole par défaut par IPv4 afin de résoudre ce problème. Les clients qui ont besoin d'IPv6 peuvent toujours modifier le réglage dans le panneau d'administration pour utiliser IPv4 et IPv6.

    | Modèle de routeur             |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Téléchargement du firmware](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Téléchargement du firmware](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Téléchargement du firmware](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Contournement pour les autres modèles**

    Si vous utilisez d'autres modèles, ou si vous préférez ne pas utiliser le firmware ci-dessus, veuillez exécuter les commandes AT l'une après l'autre après avoir démarré la connexion cellulaire.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Remarque** : pour les cartes SIM EE, "User_APN" est généralement "everywhere". Répétez cette opération après chaque redémarrage du routeur.

    ??? note "Comment exécuter une commande AT ?"

        1. Dans le panneau d'administration web, accédez à la section **INTERNET -> Cellular**, cliquez sur l'icône à trois points en haut à droite, puis sélectionnez **Modem AT Command**.
        
            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}
        
            Pour les anciens firmwares, cliquez sur le bouton d'outil en haut à droite pour accéder à la page de gestion du modem.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}
        
        2. Repérez la zone de commande AT, comme illustré ci-dessous.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Si vous rencontrez d'autres problèmes, veuillez contacter notre équipe d'assistance à [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Cordialement,

Support technique GL.iNet

17 juin 2025

