# Comment se connecter à Surfshark avec une IP dédiée sur les routeurs GL.iNet ?

Cet article présente les étapes pour configurer une connexion Surfshark avec une IP dédiée sur les routeurs GL.iNet.

Nous utilisons le GL-AXT1800 comme exemple.

1. Connectez-vous à votre compte Surfshark, puis sélectionnez **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){class="glboxshadow"}

2. Dans la section Dedicated IP, cliquez sur **Settings**.

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){class="glboxshadow"}

3. Sélectionnez un protocole (WireGuard ou OpenVPN) et téléchargez les fichiers de configuration pour une connexion manuelle.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){class="glboxshadow"}
    
    Pour la configuration WireGuard, la page de téléchargement affiche le Server IP et la Server Public Key, comme illustré ci-dessous.
    
    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){class="glboxshadow"}

    Pour la configuration OpenVPN, la page de téléchargement affiche le Server IP ainsi que les identifiants (Username & Password), comme illustré ci-dessous. Copiez les identifiants pour les utiliser plus tard.
    
    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){class="glboxshadow"}

4. Consultez les liens ci-dessous pour téléverser les fichiers de configuration sur votre routeur GL.iNet. Saisissez les identifiants si nécessaire.

    - [Téléverser une configuration WireGuard](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Téléverser une configuration OpenVPN](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
