# Comment configurer un serveur OpenVPN sur les routeurs GL.iNet

Ce tutoriel explique comment configurer un serveur OpenVPN sur les routeurs GL.iNet. Un serveur VPN vous permet d'établir à distance une connexion sécurisée à votre réseau domestique ou professionnel. Avec un routeur GL.iNet, vous pouvez configurer un serveur OpenVPN en quelques minutes.

!!! note "Avant de commencer, assurez-vous de remplir les conditions suivantes"
    
    **Adresse IP publique**

    La configuration d'un serveur OpenVPN nécessite une adresse IP publique. Pour vérifier si vous en avez une, consultez [ce lien](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Redirection de port**

    Si votre routeur GL.iNet est connecté derrière un routeur principal, [configurez la redirection de port sur le routeur principal](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Connectez-vous à votre routeur

Ouvrez un navigateur Web et accédez au panneau d'administration Web du routeur (IP par défaut : 192.168.8.1). Connectez-vous avec votre mot de passe administrateur.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Activer le DNS dynamique (facultatif)

La configuration d'un serveur OpenVPN nécessite généralement une **adresse IP publique statique**, qui fournit un point de terminaison fixe permettant aux autres appareils d'accéder à votre serveur VPN.

Toutefois, si vous ne disposez pas d'une adresse IP publique statique, par exemple si vous avez à la place une adresse IP dynamique, vous devrez peut-être activer le **DNS dynamique (DDNS)** sur votre routeur GL.iNet. Cela permet de maintenir la connectivité au serveur OpenVPN même lorsque votre adresse IP publique change de manière dynamique.

Suivez les étapes ci-dessous pour activer le DNS dynamique :

1. Dans le panneau d'administration Web du routeur, accédez à **APPLICATIONS** > **Dynamic DNS**.
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Activez **Enable DDNS**, lisez et acceptez les **Terms of Service & Privacy Policy**, puis cliquez sur **Apply**.
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Télécharger le fichier de configuration

1. Dans le panneau d'administration Web du routeur, accédez à **VPN** > **OpenVPN Server**.
2. Cliquez sur **Generate Configuration**.
3. Conservez les paramètres par défaut tels quels, puis cliquez sur **Export Client Configuration**.
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. Dans la fenêtre contextuelle, activez **Use DDNS Domain** si vous avez configuré **Dynamic DNS** auparavant.
5. Cliquez sur **Download**, puis enregistrez le fichier.
6. En haut de la page **OpenVPN Server**, cliquez sur **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Facultatif) Pour accéder au réseau local du serveur VPN, activez ces paramètres :"
    
    Pour le firmware v4.7 et versions antérieures :

    1. Dans la barre latérale gauche, cliquez sur **VPN** > **VPN Dashboard**.
    2. Cliquez sur l'icône Options.
    3. Activez **Remote Access LAN**.
    4. Cliquez sur **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Pour le firmware v4.8 et versions ultérieures :

    1. Dans la barre latérale gauche, cliquez sur **VPN** > **OpenVPN Server**.
    2. Cliquez sur **Options** en haut à droite.
    3. Activez **Allow Remote Access the LAN Subnet**.
    4. Cliquez sur **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Se connecter au serveur OpenVPN

Pour vous connecter au serveur OpenVPN, vous aurez besoin d'un client OpenVPN. Vous pouvez le configurer en utilisant l'une des méthodes ci-dessous :

??? "Méthode 1 : une application cliente OpenVPN tierce (utilisez cette méthode si vous ne disposez pas d'un routeur supplémentaire prenant en charge la configuration d'un client OpenVPN)"

    Dans ce tutoriel, nous utiliserons comme exemple l'application OpenVPN Connect, l'application officielle développée par OpenVPN Inc.

    1. Sur un autre appareil, connectez-vous à un réseau Wi-Fi différent (ou à un réseau cellulaire si vous utilisez un appareil mobile).
    2. Envoyez le fichier de configuration téléchargé précédemment vers l'appareil (par exemple par e-mail), puis téléchargez-le sur cet appareil.
    3. Téléchargez OpenVPN Connect pour le système d'exploitation de votre appareil :
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. Dans l'application, lisez les termes et conditions, puis sélectionnez **Agree**.
    5. Sélectionnez **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Sélectionnez **Browse**, puis choisissez le fichier de configuration téléchargé précédemment.
    7. Sélectionnez **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Sélectionnez **Connect** > **OK** > **Allow**.

    Vous verrez le mot "Connected" en haut du profil VPN.
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Méthode 2 : un routeur prenant en charge la configuration d'un client OpenVPN"

    Vous pouvez utiliser n'importe quel routeur qui prend en charge la configuration manuelle d'un client OpenVPN. Dans ce tutoriel, nous prendrons comme exemple le routeur de voyage GL.iNet [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/).

    1. Sur un autre appareil, connectez-vous à un réseau Wi-Fi différent (ou à un réseau cellulaire si vous utilisez un appareil mobile).
    2. Dans la barre d'adresse d'un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur (par exemple 192.168.8.1).
    3. Saisissez votre mot de passe, puis cliquez sur **Login**.
    4. Dans la barre latérale gauche, cliquez sur **VPN** > **OpenVPN Client**.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Cliquez sur **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Saisissez un nom dans le champ, puis cliquez sur l'icône de validation.
    7. Téléversez le fichier de configuration téléchargé précédemment.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Cliquez sur **Apply**.
    9. Cliquez sur l'icône à trois points, puis sur **Start**.
    10. Connectez un appareil au routeur qui exécute le client OpenVPN.

## 5. Vérifier la connexion VPN

Ouvrez un navigateur Web et recherchez votre adresse IP ainsi que votre emplacement. S'ils correspondent à l'adresse IP du serveur VPN (et non à celle de votre fournisseur d'accès à Internet) et à son emplacement, la connexion VPN est établie avec succès.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

