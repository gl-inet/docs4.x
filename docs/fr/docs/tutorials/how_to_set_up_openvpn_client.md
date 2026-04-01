# Comment configurer un client OpenVPN sur les routeurs GL.iNet

Ce tutoriel vous montrera comment configurer un client OpenVPN sur les routeurs GL.iNet.

Regardez cette vidéo ou consultez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Avant de commencer, assurez-vous d'avoir un abonnement actif auprès d'un fournisseur de services VPN qui prend en charge la configuration manuelle OpenVPN. Cliquez [ici](https://www.gl-inet.com/solutions/vpn/){target="_blank"} pour vérifier les fournisseurs OpenVPN compatibles avec GL.iNet.

Voici les étapes pour configurer un client OpenVPN via le panneau d'administration web du routeur.

## 1. Connectez-vous à votre routeur

Ouvrez un navigateur web et accédez au panneau d'administration web du routeur (IP par défaut : 192.168.8.1). Connectez-vous avec votre mot de passe administrateur.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Configurez le client VPN

Consultez la section correspondant au fournisseur de services VPN que vous utilisez.

??? "NordVPN"

    1. Dans le panneau d'administration web du routeur, allez dans **VPN** > **OpenVPN Client**.

    2. Cliquez sur **NordVPN**.

        ![nordvpn](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Entrez vos identifiants de service, puis cliquez sur **Save and Continue**. 

        Note : Il ne s'agit PAS de l'e-mail/mot de passe du compte de connexion, mais des identifiants de service obtenus depuis le site web NordVPN -> Nord Dashboard.

        ![save and continue](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. Dans l'invite, sélectionnez les emplacements VPN auxquels vous souhaitez vous connecter, puis cliquez sur **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Sélectionnez le serveur VPN auquel vous souhaitez vous connecter, cliquez sur l'icône à trois points et sur **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Autres fournisseurs de services VPN (par exemple, Surfshark)"

    1. Dans le panneau d'administration web du routeur, allez dans **VPN** > **OpenVPN Client**.

    2. Cliquez sur **Add Manually**. 

        ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Définissez un nom. Vous pouvez entrer le nom de votre fournisseur de services VPN, puis cliquez sur l'icône de validation. 

        ![click-check-icon](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Assurez-vous d'avoir téléchargé le fichier de configuration fourni par votre fournisseur de services VPN, ainsi que les identifiants de service si nécessaire.  
    5. Téléchargez le fichier de configuration que vous avez téléchargé. 
    
        Entrez les identifiants de service si requis, puis cliquez sur **Apply**. 

        ![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. À côté de l'adresse du serveur VPN, cliquez sur l'icône à trois points et sur **Start**. 

        ![start](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Vérifiez la connexion VPN

Ouvrez un navigateur web et recherchez votre adresse IP et votre localisation. Si elles correspondent à l'IP du serveur VPN (au lieu de l'IP de votre fournisseur d'accès Internet) et à sa localisation, la connexion VPN est réussie.

---

Vous avez encore des questions ? Visitez notre [Community Forum](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

