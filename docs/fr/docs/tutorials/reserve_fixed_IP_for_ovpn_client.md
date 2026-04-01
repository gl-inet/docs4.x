# Comment réserver une IP fixe pour un client OpenVPN dans une connexion OpenVPN auto-hébergée ?

Ce tutoriel vous montrera comment réserver une IP fixe pour votre client OpenVPN se connectant à votre serveur. Configurez d'abord un routeur GL.iNet comme serveur OpenVPN avant de suivre les étapes ci-dessous.

1. Connectez-vous au panneau d'administration web de votre serveur OpenVPN, puis dans la barre latérale gauche, accédez à **VPN** -> **OpenVPN Server**.

    Dans l'onglet **Configuration**, notez le sous-réseau IPv4 (**IPv4 subnet**) (tel que 10.8.0.0/24 dans l'image suivante), puis basculez le mode d'authentification (**Authentication Mode**) sur **Username and Password Only**.

    ![ovpn configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Ouvrez l'onglet **Users**, puis créez un nom d'utilisateur et un mot de passe, comme illustré ci-dessous.

    ![ovpn users](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Connectez-vous au routeur en SSH, puis exécutez la commande suivante pour ouvrir le fichier de script de configuration du serveur OpenVPN :

    `vi /lib/netifd/proto/openserver.sh`

    Dans le fichier ouvert, vérifiez si la ligne "*client-config-dir /etc/openvpn/ccd*" existe dans le script. 

    ![check config line](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Si ce n'est pas le cas, ajoutez-la manuellement, puis enregistrez le fichier et quittez-le.

4. Accédez à `/etc/openvpn/`, puis ajoutez un dossier ccd avec `mkdir ccd`.

    ![add ccd folder](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Ajoutez un fichier "GLsupport", saisissez `ifconfig-push 10.8.0.10 255.255.255.0`, puis enregistrez et quittez le fichier.

    Vérifiez le contenu avec `cat GLsupport`

    ![ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Lorsque vous utilisez GLsupport pour vous connecter à votre serveur OpenVPN, celui-ci attribue l'IP fixe 10.8.0.10 à cet utilisateur GLsupport. 
    
    - "255.255.255.0" est le masque de sous-réseau, que vous pouvez remplacer par le masque de sous-réseau de votre serveur OpenVPN.

    **Remarque** : si vous souhaitez fixer des adresses IP pour plusieurs clients OpenVPN, veuillez créer plusieurs noms d'utilisateur et mots de passe à l'étape 2, puis répéter l'étape 5, ajouter des fichiers dans le dossier CCD dans l'ordre des utilisateurs, comme user_1, user_2, user_3, suivis de la commande "ifconfig push" et de leurs IP fixes et masques de sous-réseau correspondants. 
    
    Par exemple, `ifconfig-push 10.8.0.20 225.225.225.0`, `ifconfig-push 10.8.0.30 225.225.225.0`, `ifconfig-push 10.8.0.40 225.225.225.0`

6. Enfin, testez avec votre client OVPN et vérifiez que l'IP virtuelle du client (**Client Virtual IP (IPv4)**) correspond bien à l'adresse réservée. 

    Par exemple, si votre client OpenVPN est un routeur GL.iNet, vous pouvez vous connecter au panneau d'administration web du routeur client OpenVPN, accéder au tableau de bord VPN (**VPN Dashboard**) et vérifier l'IP virtuelle du client (**Client Virtual IP (IPv4)**).

    ![ovpn client test v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(Tableau de bord VPN dans le firmware v4.7 et les versions antérieures)</small>

    ![ovpn client test v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(Tableau de bord VPN dans le firmware v4.8)</small>

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
