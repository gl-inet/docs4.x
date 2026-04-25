# Que faire si l'installation du profil eSIM echoue ?

Si vous essayez d'ajouter un profil eSIM sur votre routeur GL.iNet mais que l'installation echoue, veuillez suivre les etapes suivantes pour effectuer le depannage :

1. Assurez-vous que le routeur est connecte a Internet.

    Assurez-vous que votre routeur est bien connecte a Internet. Un reseau instable peut perturber le televersement du profil eSIM et empecher le routeur de l'obtenir et de l'installer.

    Si possible, essayez de connecter le routeur a une autre source reseau, comme le hotspot de votre smartphone ou un reseau Wi-Fi public, puis televersez de nouveau votre profil eSIM pour tester.

2. Modifiez les parametres DNS.

    Si Internet fonctionne correctement, connectez-vous au panneau d'administration web du routeur et allez dans **NETWORK** -> **DNS**.

    Basculez le mode DNS sur **Manual DNS** et configurez d'autres serveurs DNS publics pour le test, par exemple Google DNS (`8.8.8.8`, `8.8.4.4`) ou Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Cliquez sur **Apply** pour enregistrer les modifications, puis essayez de televerser de nouveau votre profil eSIM.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Desactivez AdGuard Home.

    Si AdGuard Home est disponible et active sur votre routeur, desactivez-le puis essayez d'installer de nouveau votre profil eSIM.

4. Verifiez la disponibilite du profil eSIM.

    Verifiez si ce profil eSIM ou ce QR code a deja ete active ou installe sur un autre appareil.

    La plupart des profils eSIM ne peuvent etre installes qu'une seule fois et ne peuvent pas etre actives sur plusieurs appareils. Si possible, contactez votre fournisseur eSIM pour confirmer si le profil eSIM actuel est toujours disponible. Si le QR code ou le code d'activation a expire, demandez-en un nouveau puis reessayez.

5. Verifiez le code d'activation.

    Un QR code correctement formate affichera un code d'activation commencant par **LPA:**. Cependant, certains QR codes non standard peuvent ne fournir qu'un code brut sans le prefixe LPA. Dans ce cas, ajoutez manuellement `LPA:` au debut du code avant de cliquer sur **Install**.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Verifiez si un code de confirmation est requis.

    Certains profils eSIM exigent la saisie d'un code de confirmation pendant l'installation, comme Smarty eSIM. Verifiez votre forfait eSIM ou le guide d'installation pour savoir si un code de confirmation est necessaire. Si oui, saisissez le bon code.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Si les etapes ci-dessus ne resolvent pas le probleme, exportez le journal eSIM depuis la page **eSIM Management**.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Envoyez ensuite ce journal, avec les informations importantes ci-dessous, a [support@gl-inet.com](mailto:support@gl-inet.com) pour obtenir une assistance supplementaire.

    - Le probleme rencontre
    - Les methodes de depannage deja essayees
    - Votre fournisseur eSIM

---
