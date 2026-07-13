# Impossible de se connecter à un serveur WireGuard obfusqué

L'obfuscation VPN est une technique qui fait ressembler le trafic VPN à du trafic Internet ordinaire. Certains routeurs GL.iNet prennent actuellement en charge le protocole AmneziaWG, ce qui permet de configurer un serveur WireGuard avec obfuscation du trafic activée.

Si vous ne parvenez pas à établir une connexion avec un serveur WireGuard obfusqué, suivez les étapes de dépannage ci-dessous.

1. **Assurez-vous que la configuration WireGuard importée sur chaque client est dédiée.**

    Chaque client nécessite un fichier de configuration peer exclusif. Utiliser la même configuration sur plusieurs clients entraînera des échecs de connexion.

    Si nécessaire, allez dans **VPN** -> **WireGuard Server** -> **Profiles** pour afficher vos profils exportés.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Assurez-vous que les paramètres d’obfuscation peuvent être vérifiés par le client.**

    Le protocole AmneziaWG est rétrocompatible. Si votre serveur WireGuard ne prend en charge qu’AmneziaWG v1.0, le fichier de configuration passera tout de même la vérification lorsqu’il est importé dans un client prenant en charge v2.0.
        
    Toutefois, si votre fichier de configuration inclut des paramètres d’obfuscation AmneziaWG v2.0, assurez-vous que votre client WireGuard prend en charge AmneziaWG v2.0. Sinon, la vérification des paramètres peut échouer.

    !!! tip "Comment identifier la version d’AmneziaWG ?"

        **V1.0** : pas de paramètres S3-S4 ; H1-H4 sont des entiers fixes uniques.
        
        **V2.0** : il s’agit de la version V2.0 si l’une des conditions ci-dessous est remplie :
        
        - Inclut des paramètres S3-S4
        - H1-H4 sont définis comme des plages numériques
        - Inclut des paramètres I1-I5 personnalisés.
        
        > Remarque : I1-I5 ne sont pas générés automatiquement. Les utilisateurs peuvent les ajouter manuellement comme lignes supplémentaires dans le fichier de configuration afin que le trafic AmneziaWG ressemble à d’autres protocoles courants, tels que QUIC ou WebRTC.

    Si votre client WireGuard est un routeur GL.iNet, vérifiez sa version d’AmneziaWG avec les deux méthodes suivantes.

    ??? note "Vérifier depuis le Router Web Admin Panel"

        1. Connectez-vous au Web Admin Panel du routeur.

        2. Allez dans **VPN** -> **WireGuard Server** -> **Configuration** et vérifiez les paramètres d'obfuscation. Si la configuration contient **S3-S4** et **H1-H4** sous forme de plages variables, au lieu de valeurs fixes, votre routeur exécute AmneziaWG 2.0, comme ci-dessous.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            Sinon, il utilise AmneziaWG 1.0, comme ci-dessous.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Vérifier avec une commande SSH"

        1. Connectez-vous au routeur via SSH.

        2. Exécutez `opkg list|grep awg` et vérifiez le suffixe du paquet **kmod-amneziawg** dans la sortie. S'il est marqué **2.0**, le routeur prend en charge AmneziaWG 2.0, comme ci-dessous.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            Sinon, il exécute AmneziaWG 1.0, comme ci-dessous.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Ajustez les paramètres d'obfuscation.**

    Si vous avez configuré manuellement des [paramètres d'obfuscation](amneziawg_obfuscation.md#parameter-overview), tels que Jc, Jmin ou Jmax, sur votre serveur WireGuard, des valeurs incorrectes peuvent entraîner des échecs de handshake.

    Essayez de modifier ces paramètres d'obfuscation, puis reconnectez-vous afin d'exclure un problème d'incompatibilité de paramètres. Vous pouvez aussi restaurer les paramètres d'obfuscation par défaut pour tester.

4. **Testez la connexion avec l'application officielle AmneziaWG.**

    Effectuez un test comparatif : installez l'application officielle AmneziaWG, importez le fichier de configuration original exporté par le serveur dans l'application, puis essayez de vous connecter.

    - Si la connexion réussit dans l'application officielle, le fichier de configuration est valide. Le problème vient peut-être de votre appareil client initial. Vérifiez sa connectivité réseau ou contactez le support pour obtenir de l'aide.

    - Si la connexion échoue toujours, le problème provient de la configuration du serveur du routeur. Vérifiez les paramètres du serveur et les paramètres d'obfuscation.

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
