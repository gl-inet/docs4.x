# DNS dynamique

Le service Dynamic Domain Name Service (Dynamic DNS ou DDNS) permet d’associer un nom de domaine à l’adresse IP dynamique d’un appareil réseau. Avec Dynamic DNS, vous pouvez accéder à votre routeur à distance. Une adresse IP publique Internet est requise pour cette fonctionnalité.

## Activer DDNS

Sur le côté gauche du panneau d’administration web, allez à **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Activez **Enable DDNS**, acceptez les **Terms of Services & Privacy Policy**, puis cliquez sur **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Cliquez sur **Security Settings** en bas à droite.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, vérifiez si le protocole d’accès à distance que vous souhaitez utiliser est activé. Sinon, allez à **SYSTEM** -> **Security** -> **Remote Access Control** pour l’activer.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Activez le protocole d’accès à distance souhaité, puis cliquez sur **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

La synchronisation des enregistrements entre les serveurs DNS peut prendre jusqu’à 10 minutes. Cela peut vous empêcher d’accéder immédiatement au nom de domaine DDNS juste après son activation ou après un changement de votre adresse IP publique.

**Note** : Si vous activez DDNS et le client VPN en même temps, assurez-vous que **Services From GL.iNet Use VPN** est désactivé. Cette option se trouve dans les [VPN Client Options](vpn_dashboard.md#tunnel-options) du VPN Dashboard.

## Vérifier si DDNS fonctionne

Vous pouvez vérifier si DDNS fonctionne à l’aide de l’outil de test DDNS ou manuellement à l’aide de commandes.

=== "Utiliser l’outil DDNS Test"

    Dans la page Dynamic DNS, cliquez sur **DDNS Test**.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Assurez-vous que l’adresse IP issue de la résolution du domaine DDNS correspond à l’adresse IP WAN du routeur.
    
    Si ce n’est pas le cas, un avertissement jaune s’affiche en haut, indiquant que le routeur est peut-être derrière un NAT et que vous devez configurer une redirection de port sur le routeur en amont.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Vérification manuelle"

    1. Utilisez la commande `nslookup` pour obtenir l’association entre le nom de domaine et l’adresse IP, comme illustré ci-dessous.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Remplacez "xxxxxxx.glddns.com" dans l’image ci-dessus par votre nom d’hôte.
        
        Le "8.8.8.8" dans l’image ci-dessus correspond au DNS de Google. Vous pouvez l’utiliser ou le remplacer par un autre DNS, puis appuyer sur Entrée.

    2. Si la commande renvoie une adresse IP publique, telle que "103.81.180.10" dans l’image ci-dessous, cela indique que votre domaine DDNS a bien été associé à une adresse IP publique.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        Sur un appareil connecté au routeur, recherchez "what is my ip address" dans un navigateur ou consultez un site comme [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. Vous obtiendrez votre adresse IP publique. Comparez les deux adresses IP obtenues aux étapes 1 et 2. Si elles sont identiques, le DDNS fonctionne ; sinon, ce n’est pas le cas.

    3. Si vous obtenez le message `** server can't find xxxxxxx.glddns.com: NXDOMAIN`, comme ci-dessous, cela indique que la résolution du domaine a échoué et que votre domaine DDNS n’a pas été correctement associé à une adresse IP publique.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## Accès à distance HTTPS

!!! Note

    1. Une adresse **IP publique** est requise pour l’accès à distance HTTPS.
    
        Cliquez [ici](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) pour vérifier si votre fournisseur d’accès à Internet (ISP) vous attribue une adresse IP publique.
    
    2. Si votre routeur est derrière un NAT, configurez une redirection de port (port **443**) sur le routeur en amont pour l’accès HTTPS.

Suivez les étapes ci-dessous pour activer l’accès à distance HTTPS pour votre routeur.

1. Dans la page Dynamic DNS, activez **Enable DDNS**, acceptez les **Terms of Services & Privacy Policy**, puis cliquez sur **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Dans le panneau d’administration web, allez à **SYSTEM** -> **Security** -> **Remote Access Control**.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Activez **HTTPS Remote Access**, puis cliquez sur **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Une fois activé, vous pouvez accéder au panneau d’administration du routeur depuis n’importe où en utilisant le nom d’hôte DDNS via **HTTPS** (par exemple `https://xxxxxxx.glddns.com`).

Si une redirection de port est configurée, accédez-y via `https://xxxxxxx.glddns.com:external_port` (remplacez external_port par votre numéro de port réel).

**Note** : Cette fonction utilise des certificats auto-signés. Les navigateurs afficheront donc **Your connection is not private** lorsque vous accédez au panneau d’administration du routeur via le nom d’hôte DDNS en **HTTPS**, comme illustré ci-dessous (le port 8001 est utilisé ci-dessous comme exemple).

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Pour continuer l’accès à distance HTTPS, cliquez sur **Advanced** en bas de la page.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Cliquez ensuite sur **Proceed to xxxxxxx.glddns.com** pour continuer.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Vous pourrez alors accéder au panneau d’administration web via le nom d’hôte DDNS en HTTPS.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Accès à distance SSH

!!! Note

    1. Une adresse **IP publique** est requise pour l’accès à distance SSH.
    
        Cliquez [ici](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) pour vérifier si votre fournisseur d’accès à Internet (ISP) vous attribue une adresse IP publique.
    
    2. Si votre routeur est derrière un NAT, configurez une redirection de port (port **22**) sur le routeur en amont pour l’accès SSH.

Suivez les étapes ci-dessous pour activer l’accès à distance SSH pour votre routeur.

1. Dans la page Dynamic DNS, activez **Enable DDNS**, acceptez les **Terms of Services & Privacy Policy**, puis cliquez sur **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Dans le panneau d’administration web, allez à **SYSTEM** -> **Security** -> **Remote Access Control**.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Activez **SSH Remote Access**, puis cliquez sur **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Une fois activé, vous pouvez accéder au terminal du routeur depuis n’importe où en utilisant le nom d’hôte DDNS via **SSH** (par exemple `ssh root@xxxxxxx.glddns.com`).

Si une redirection de port est configurée, accédez-y via `ssh root@xxxxxxx.glddns.com:external_port` (remplacez external_port par votre numéro de port réel).

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
