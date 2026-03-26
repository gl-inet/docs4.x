# Le serveur WireGuard sur mon routeur GL.iNet ne fonctionne pas correctement

Il existe plusieurs raisons pour lesquelles le serveur WireGuard que vous avez configuré sur votre routeur GL.iNet peut ne pas fonctionner correctement.

Si vous rencontrez des problèmes, suivez ces étapes de dépannage en fonction de votre situation.

#### Situation 1 : le serveur WireGuard démarre, mais la connexion n'aboutit pas

??? "Suivez ces étapes"

    ![client](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/client.jpg){class="glboxshadow"}

    La redirection de port configurée sur votre routeur principal, auquel votre routeur secondaire (GL.iNet) est connecté, peut ne pas fonctionner correctement.
    Pour vérifier si la redirection de port fonctionne correctement, essayez de rediriger le port HTTPS du routeur principal vers votre serveur WireGuard. Suivez ces étapes :

    1. Redirigez le port HTTPS de votre routeur principal vers votre serveur WireGuard

        1. Connectez-vous au panneau d'administration de votre routeur principal.
        2. Accédez à l'écran de redirection de port.
        3. Créez un nouveau port et nommez-le **HTTPS**.
        4. Saisissez les informations suivantes :
            * **External port/Internal port:** saisissez **443**.
            * **Protocol:** choisissez **All** ou **UDP/TCP**.
            * **Internal IP** (ou **Host IP**) : saisissez l'adresse IP WAN de votre routeur secondaire ou sélectionnez votre routeur secondaire dans la liste déroulante si cette option est disponible.
            ![DDNS1](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns1.jpg){class="glboxshadow"}

    2. Activez le DDNS et l'accès à distance HTTPS (sur le routeur GL.iNet)

        1. Dans un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur GL.iNet (par exemple, 192.168.8.1), puis connectez-vous.
        2. Dans la barre latérale gauche, cliquez sur **Applications** > **Dynamic DNS**.
        3. Activez **Enable DDNS** et cochez la case **I have read and agree to the Terms of Service & Privacy Policy**.
            ![DDNS2](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns2.jpg){class="glboxshadow"}
        4. Enregistrez le nom d'hôte quelque part, car vous en aurez besoin plus tard, puis cliquez sur **Apply**.
        5. Dans la barre latérale gauche, cliquez sur **System** > **Security**.
        6. Sous **Remote Access Control**, activez **HTTPS Remote Access**.
            ![DDNS3](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns3.jpg){class="glboxshadow"}
        7. Cliquez sur **Apply**.

    3. Vérifiez si vous pouvez accéder au panneau d'administration du routeur GL.iNet

        1. Sur un autre appareil (par exemple, un ordinateur portable ou un appareil mobile), connectez-vous à un autre réseau Wi-Fi ou au réseau cellulaire.
        2. Dans la barre d'adresse d'un navigateur Web, saisissez le nom d'hôte que vous avez enregistré précédemment (abcd123.glddns.com).
        3. Cliquez sur **Advanced**.
            ![DDNS4](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns4.jpg){class="glboxshadow"}
        4. Cliquez sur **Proceed to abcd123.glddns.com(unsafe)**.
            ![DDNS5](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns5.jpg){class="glboxshadow"}

    Si vous voyez l'écran de connexion de votre routeur GL.iNet (routeur secondaire), la redirection de port que vous avez configurée sur votre routeur principal fonctionne correctement.

    ![DDNS6](https://static.gl-inet.com/docs/router/en/4/faq/troubleshooting/my_wireguard_server_is_not_working/ddns6.jpg){class="glboxshadow"}

    Si vous ne voyez pas l'écran de connexion de votre routeur GL.iNet (routeur secondaire), la redirection de port ne fonctionne pas correctement. Configurez à nouveau la redirection de port ou assurez-vous d'utiliser comme routeur principal un routeur dont la fonction de redirection de port fonctionne correctement.

#### Situation 2 : le serveur WireGuard indique que mon client VPN est connecté, mais le client VPN ne peut pas accéder à Internet

??? "Suivez ces étapes"

    Suivez les étapes indiquées pour chaque cause possible ci-dessous et vérifiez si le problème est résolu. Si c'est le cas, vous pouvez ignorer le reste de cette section.

    **Cause possible 1 : votre fournisseur d'accès à Internet peut ne pas être en mesure de résoudre les serveurs DNS de GL.iNet**

    Essayez de configurer manuellement les adresses des serveurs DNS en suivant ces étapes :

    1. Dans un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur GL.iNet (par exemple, 192.168.8.1), puis connectez-vous.
    2. Dans la barre latérale gauche, cliquez sur **Network** > **DNS**.
    3. Pour **Mode**, sélectionnez **Manual DNS**.
    4. Pour **DNS Server 1**, sélectionnez **Google Public DNS**.
    5. Cliquez sur **Apply**.

    **Cause possible 2 : l'adresse IP de passerelle de votre routeur principal est en conflit avec l'adresse IP du serveur WireGuard**

    Essayez de modifier l'adresse IPv4 en suivant ces étapes :

    1. Dans un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur GL.iNet (par exemple, 192.168.8.1), puis connectez-vous.
    2. Dans la barre latérale gauche, cliquez sur **VPN** > **WireGuard Server**.
    3. Dans l'onglet **Configuration**, pour le champ **IPv4 Address**, saisissez une nouvelle adresse IP (par exemple, 10.1.0.1/24).
    4. Cliquez sur **Apply**.

    **Cause possible 3 : si votre serveur WireGuard et votre client WireGuard sont tous deux configurés sur des routeurs GL.iNet, leurs adresses IP LAN sont en conflit**

    Essayez de modifier l'adresse IP LAN de l'un des routeurs en suivant ces étapes :

    1. Dans un navigateur Web, connectez-vous au panneau d'administration de l'un des routeurs GL.iNet (par exemple, 192.168.8.1).
    2. Dans la barre latérale gauche, cliquez sur **Network** > **LAN**.
    3. Dans le champ **Router IP address**, saisissez une nouvelle adresse IP LAN (par exemple, 192.168.10.1).
    4. Cliquez sur **Apply**.

    **Cause possible 4 : l'adresse IP du serveur WireGuard a été mise à jour, mais le sous-réseau est manquant**

    Ajoutez un sous-réseau à l'adresse IP de votre serveur WireGuard en suivant ces étapes :

    1. Dans un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur GL.iNet (par exemple, 192.168.8.1), puis connectez-vous.
    2. Dans la barre latérale gauche, cliquez sur **VPN** > **WireGuard Server**.
    3. Dans l'onglet **Configuration**, pour le champ **IPv4 Address**, ajoutez **/24** après **10.0.0.1**.
    4. Cliquez sur **Apply**.

#### Situation 3 : le serveur WireGuard fonctionne, mais je ne parviens pas à y connecter mon client VPN

??? "Suivez ces étapes"

    Suivez les étapes indiquées pour chaque cause possible ci-dessous et vérifiez si le problème est résolu. Si c'est le cas, vous pouvez ignorer le reste de cette section.

    **Cause possible 1 : la redirection de port configurée sur votre routeur principal peut ne pas fonctionner correctement**

    Pour vérifier si la redirection de port fonctionne correctement, essayez de rediriger le port HTTPS vers votre serveur WireGuard en suivant les étapes de résolution indiquées dans la Situation 1.

    **Cause possible 2 : vous n'avez peut-être pas d'adresse IP publique**

    Pour le vérifier, consultez [cette page](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/).

    **Cause possible 3 : si votre serveur WireGuard et votre client WireGuard sont tous deux configurés sur des routeurs GL.iNet, leurs adresses IP LAN sont en conflit**

    Modifiez l'adresse IP LAN de l'un des routeurs en suivant ces étapes :

    1. Dans un navigateur Web, connectez-vous au panneau d'administration de l'un des routeurs GL.iNet (par exemple, 192.168.8.1).
    2. Dans la barre latérale gauche, cliquez sur **Network** > **LAN**.
    3. Dans le champ **Router IP address**, saisissez une nouvelle adresse IP LAN (par exemple, 192.168.10.1).
    4. Cliquez sur **Apply**.

    **Cause possible 4 : l'appareil que vous utilisez pour vous connecter au serveur WireGuard est connecté à son réseau Wi-Fi ou à son port LAN**

    Connectez votre appareil à un autre réseau Wi-Fi ou à son réseau cellulaire.

    **Cause possible 5 : certaines lignes peuvent manquer dans le fichier de configuration que vous avez téléversé sur votre appareil client**

    Téléversez de nouveau vos informations de configuration.

#### Situation 4 : le serveur WireGuard est connecté, mais la connexion n'est pas stable

??? "Suivez ces étapes"

    Suivez les étapes ci-dessous pour résoudre le problème. Après chaque étape, vérifiez si le problème est résolu. Si c'est le cas, vous pouvez ignorer le reste des étapes.

    1. Sur votre appareil client VPN, remplacez le MTU de **1420** par une valeur plus petite (par exemple, **1380**).
    2. Sur votre routeur principal, activez la fonction VPN passthrough si elle est disponible.
    3. Essayez de configurer manuellement les serveurs DNS sur votre routeur GL.iNet en suivant ces étapes :
        1. Dans un navigateur Web, saisissez l'URL du panneau d'administration de votre routeur GL.iNet (par exemple, 192.168.8.1), puis connectez-vous.
        2. Dans la barre latérale gauche, cliquez sur **Network** > **DNS**.
        3. Pour **Mode**, sélectionnez **Manual DNS**.
        4. Pour **DNS Server 1**, sélectionnez **Google Public DNS**.
        5. Cliquez sur **Apply**.

#### Situation 5 : le serveur WireGuard a soudainement cessé de fonctionner

??? "Suivez ces étapes"

    Suivez les étapes indiquées pour chaque cause possible ci-dessous et vérifiez si le problème est résolu. Si c'est le cas, vous pouvez ignorer le reste de cette section.

    **Cause possible 1 : il peut y avoir une panne de courant à l'endroit où vous avez installé votre serveur WireGuard**

    Vérifiez si votre serveur WireGuard est toujours en ligne en suivant les étapes de résolution de la Situation 1 ou via [GoodCloud](https://docs.gl-inet.com/router/en/4/interface_guide/cloud/) (si vous y avez déjà connecté votre routeur).

    **Cause possible 2 : vous n'avez pas activé le DNS dynamique (DDNS)**

    Si vous avez une adresse IP dynamique (ce qui est très probablement le cas), vous devrez activer le DDNS. [Activez le DDNS](https://www.youtube.com/watch?v=qLEj9zoiYRs&t=26s) et suivez le reste des étapes pour configurer à nouveau le serveur WireGuard.

    **Cause possible 3 : la redirection de port a cessé de fonctionner pour une raison inconnue**

    [Configurez à nouveau la redirection de port](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/) avec un autre port.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
