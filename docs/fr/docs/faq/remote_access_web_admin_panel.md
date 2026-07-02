# Comment accéder à distance au panneau d'administration web d'un routeur GL.iNet ?

La méthode suivante nécessite une préconfiguration lorsque vous êtes encore physiquement à proximité du routeur.

## Méthode 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} est une plateforme conçue pour simplifier le déploiement et la gestion à distance des appareils connectés. Elle fournit un moyen simple d'accéder aux routeurs GL.iNet et de les gérer à distance. Il vous suffit de lier votre routeur GL.iNet à GoodCloud ; vous pourrez ensuite accéder à distance au panneau d'administration web du routeur à tout moment, où que vous soyez.

Veuillez consulter [ce guide](../interface_guide/cloud.md){target="_blank"} pour plus de détails.

## Méthode 2. VPN

Si votre routeur dispose d'une **IP publique**, vous pouvez accéder à distance à son panneau d'administration web via un tunnel VPN. Notez que cette méthode implique des configurations avancées et nécessite davantage de temps de mise en place.

1. Assurez-vous que votre routeur dispose d'une IP publique. [Comment vérifier si je dispose d'une adresse IP publique ?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Configurez votre routeur en tant que WireGuard Server. Consultez les détails [ici](../interface_guide/wireguard_server.md){target="_blank"}.

3. Exportez un fichier de configuration depuis votre WireGuard Server pour une utilisation ultérieure.

4. Dans le panneau d'administration web du routeur, accédez à **VPN** -> **WireGuard Server** et cliquez sur **Options** dans l'angle supérieur droit. Activez **Allow Remote Access to the LAN Subnet**, puis cliquez sur **Apply**.

5. Configurez l'appareil depuis lequel vous souhaitez accéder à distance à votre routeur comme WireGuard Client en important manuellement le fichier de configuration.

    - Si votre WireGuard Client est un terminal, par exemple un smartphone ou un ordinateur portable, [installez l'application WireGuard](https://www.wireguard.com/install){target="_blank"}, puis importez le fichier pour démarrer une connexion.

    - Si votre WireGuard Client est un autre routeur GL.iNet, par exemple un routeur de voyage GL.iNet, consultez [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"} pour y importer le fichier de configuration et démarrer une connexion.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
