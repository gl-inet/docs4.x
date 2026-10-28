# Sécuriser RDP depuis un réseau externe avec WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Vous pouvez avoir besoin d’accéder à distance à votre PC depuis un réseau externe, ou inversement. Une méthode sécurisée consiste à utiliser votre propre tunnel WireGuard. Cela offre davantage de sécurité que la redirection de ports et l’accès direct au PC via votre adresse IP publique. Une fois le tunnel configuré, vous pouvez utiliser **Windows Remote Desktop** pour accéder à votre PC depuis n’importe où.

Ce tutoriel utilise deux routeurs GL.iNet pour montrer comment sécuriser Windows RDP sur un réseau WireGuard.

## Topologie {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Étapes de configuration {#setup-steps}

1. Configurez votre réseau WireGuard.

    Commencez par configurer votre propre serveur WireGuard et votre client WireGuard avec deux routeurs GL.iNet. Consultez [Créer votre propre serveur WireGuard avec deux routeurs GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Autorisez votre serveur WireGuard à accéder au LAN du client.

    Pour permettre un accès bidirectionnel entre le serveur et le client, autorisez d’abord le serveur à accéder au LAN du client. Consultez [Accéder au LAN du client WireGuard depuis le serveur](wireguard_server_access_to_client_lan_side.md).

    Les étapes peuvent varier selon la version du firmware.

3. Autorisez votre client WireGuard à accéder au LAN du serveur.

    Cette étape peut varier selon la version du firmware. Sélectionnez ci-dessous la version du firmware du routeur configuré comme client WireGuard.

    ??? note "Pour le firmware v4.7 et les versions antérieures"

        Connectez-vous à votre client WireGuard et accédez à **VPN** -> **VPN Dashboard**. Repérez **VPN Server** et cliquez sur l’icône d’engrenage à droite.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        Dans la fenêtre contextuelle, activez **Remote Access LAN** et cliquez sur **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Pour le firmware v4.8 et les versions ultérieures"

        Connectez-vous à votre client WireGuard et accédez à **VPN** -> **WireGuard Server**. Cliquez sur **Options** en haut à droite.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        Dans la fenêtre contextuelle, activez **Allow Remote Access to the LAN Subnet** et cliquez sur **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Connectez l’ordinateur auquel vous souhaitez accéder au serveur VPN et relevez son adresse IP LAN.

    Dans l’exemple suivant, l’adresse IP du PC côté serveur est **192.168.29.123**.

5. Configurez le PC côté serveur pour le rendre accessible.

    Sur le PC côté serveur, accédez à **System Settings** et cliquez sur **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Activez **Remote Desktop** et cliquez sur **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Accédez à distance depuis l’ordinateur portable côté client.

    Recherchez **Remote Desktop Connection** dans la barre de recherche.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Lancez l’application et saisissez l’adresse IP du PC côté serveur, par exemple **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Saisissez les identifiants du PC côté serveur pour vous connecter.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Vous pouvez alors contrôler à distance le PC côté serveur.

    Pour effectuer l’opération inverse, inversez simplement les étapes entre le PC serveur et l’ordinateur portable client.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
