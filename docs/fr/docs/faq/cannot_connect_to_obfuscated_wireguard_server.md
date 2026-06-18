# Impossible de se connecter à un serveur WireGuard obfusqué

L'obfuscation VPN est une technique qui fait ressembler le trafic VPN à du trafic Internet ordinaire. Certains routeurs GL.iNet prennent actuellement en charge le protocole AmneziaWG, ce qui permet de configurer un serveur WireGuard avec obfuscation du trafic activée.

Si vous ne parvenez pas à établir une connexion avec un serveur WireGuard obfusqué, suivez les étapes de dépannage ci-dessous.

1. **Assurez-vous que le fichier de configuration WireGuard importé sur votre client est exactement celui exporté depuis votre serveur WireGuard GL.iNet.**

    Chaque client nécessite un fichier de configuration peer exclusif. Utiliser la même configuration sur plusieurs clients entraînera des échecs de connexion.

    Si nécessaire, allez dans **VPN** -> **WireGuard Server** -> **Profiles** pour afficher vos profils exportés.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Faites correspondre les versions du protocole AmneziaWG sur le serveur et le client.**

    AmneziaWG 1.0 et 2.0 sont mutuellement incompatibles. Le serveur et le client doivent utiliser la même version du protocole AmneziaWG pour établir une connexion valide.

    Si votre appareil client est un routeur GL.iNet, vous pouvez vérifier la version du protocole avec les deux méthodes suivantes.

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
