# Comment se connecter à NordVPN avec une IP dédiée sur les routeurs GL.iNet ?

Cet article présente les étapes pour configurer une connexion NordVPN avec une IP dédiée sur les routeurs GL.iNet.

Nous utilisons le GL-AXT1800 comme exemple.

1. Connectez-vous à votre Nord Account et vérifiez les détails de l'IP dédiée. Comme indiqué ci-dessous, l'IP attribuée est **193.32.211.142** et le serveur est **United Kingdom #1625**.

    ![nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Accédez à [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/) et recherchez le fichier de configuration pour **United Kingdom #1625**. Téléchargez le fichier de configuration UDP ou TCP.

    ![download nordvpn dedicated ip info](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Revenez sur la page de votre Nord Account, allez dans **Manual Setup** et cliquez sur **Set up NordVPN Manually** pour obtenir vos identifiants de service.

    ![nordvpn manual setup](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![nordvpn manual setup service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Connectez-vous au panneau d'administration web de votre routeur, puis allez dans **VPN** > **OpenVPN Client**. Créez un nouveau groupe pour téléverser le fichier de configuration téléchargé à l'étape 2. Saisissez ensuite les identifiants de service obtenus à l'étape 3.

    ![set up nordvpn on glinet router](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    1 fichier de configuration valide a été détecté. Veuillez saisir votre nom d'utilisateur et votre mot de passe. Si ces configurations utilisent des mots de passe différents, vous devrez saisir le mot de passe correspondant pour chaque fichier de configuration.

5. Cliquez sur l'icône à trois points à droite pour vous connecter. Vous pouvez également aller dans **VPN Dashboard**, sélectionner le fichier de configuration et cliquer sur **Apply** pour établir la connexion.

6. Une fois connecté, vérifiez votre IP publique [ici](https://whatismyipaddress.com/) et confirmez qu'elle correspond à votre IP dédiée fournie par NordVPN.

    ![check ip after connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
