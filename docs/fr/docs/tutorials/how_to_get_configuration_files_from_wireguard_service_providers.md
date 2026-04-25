# Comment obtenir des fichiers de configuration auprès des fournisseurs de services WireGuard

??? "AzireVPN"
    ### AzireVPN

    [Site officiel](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Accédez au [site officiel d'AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} et connectez-vous, puis ouvrez le [générateur de configuration WireGuard](https://www.azirevpn.com/cfg/wireguard){target="_blank"}

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. Dans l'option IP, veuillez sélectionner **IPv4**. Cliquez ensuite sur **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-azirevpn) pour continuer.

    4. Vous pouvez également utiliser [l'application mobile](../faq/mobile_app.md) pour configurer AzireVPN.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Site officiel](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN offre un moyen simple d'utiliser son service WireGuard sur un routeur GL.iNet.

    1. Connectez-vous au routeur en [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Copiez l'URL d'installation ci-dessous, collez-la dans le terminal, puis appuyez sur Entrée. (Un clic droit avec la souris la collera.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. L'installation démarre ensuite et demande le nom d'utilisateur et le mot de passe. Lorsque vous saisissez ou collez le mot de passe, aucun changement n'est visible dans le terminal ; appuyez simplement sur Entrée après la saisie.

    4. Une fois l'opération terminée, allez dans le panneau d'administration web et vous verrez qu'un groupe hide.me VPN a été créé avec des fichiers de configuration déjà présents. Il vous suffit ensuite de vous connecter comme avec n'importe quel autre fichier de configuration.

    **Remarque :** La clé du fichier de configuration Hide.me VPN est régénérée avant chaque connexion et devient invalide après la déconnexion. Copier ce fichier de configuration vers d'autres appareils ne permettra donc pas de se connecter avec succès.

    [Lien de référence](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Site officiel](https://mullvad.net/){target="_blank"}

    1. Accédez au [site officiel de Mullvad](https://mullvad.net/){target="_blank"} et connectez-vous, puis ouvrez le [générateur de fichiers de configuration WireGuard](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}

    2. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md/#set-up-mullvad) pour continuer.

    3. Vous pouvez également utiliser [l'application mobile](../faq/mobile_app.md) pour configurer Mullvad.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Site officiel](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Il n'est pas possible de télécharger les configurations WireGuard depuis son site web ; veuillez utiliser [l'application mobile](../faq/mobile_app.md) pour configurer PIA VPN.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Site officiel](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Si vous utilisez [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, connectez-vous puis accédez à [cette page](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, cliquez sur **Router**, puis sélectionnez **WireGuard**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. Dans la fenêtre suivante, sélectionnez **I don't have a key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Sélectionnez **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Une fois la clé générée, sélectionnez **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Enfin, choisissez l'emplacement que vous souhaitez configurer, puis cliquez sur le bouton **download** à côté de cet emplacement. Vous pourrez alors télécharger les fichiers de configuration.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-surfshark) pour continuer.

    [Lien de référence](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Site officiel](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Si vous utilisez [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, connectez-vous sur son site web, ouvrez le [Client Area](https://airvpn.org/client/){target="_blank"}, puis cliquez sur [Config Generator](https://airvpn.org/generator/){target="_blank"}

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Sur la page Config Generator, sélectionnez WireGuard dans la section des protocoles.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Sélectionnez un serveur, faites ensuite défiler jusqu'en bas, puis cliquez sur le bouton **Generate**. Le fichier de configuration sera téléchargé.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "Astrill"
    ### Astrill

    [Site officiel](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Si vous utilisez [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, veuillez vous connecter puis accéder à [cette page](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"} pour générer des configurations WireGuard.

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "IVPN"
    ### IVPN

    [Site officiel](https://www.ivpn.net/){target="_blank"}

    Si vous utilisez [IVPN](https://www.ivpn.net/){target="_blank"}, vous devez générer la configuration WireGuard manuellement. Suivez le guide correspondant à votre système d'exploitation.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "NVPN"
    ### NVPN

    [Site officiel](https://www.nvpn.net/){target="_blank"}

    Suivez le guide disponible [ici](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"} pour créer la configuration.

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "OVPN"
    ### OVPN

    [Site officiel](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Connectez-vous à [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"}, puis recherchez le menu ci-dessous pour obtenir les fichiers de configuration WireGuard.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Cliquez sur **Generate WireGuard keys**, choisissez le serveur souhaité, puis téléchargez la configuration.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Ouvrez la configuration avec un éditeur de texte, puis copiez le contenu.

        La configuration peut contenir des éléments IPv6. Comme les routeurs GL.iNet ne prennent pas suffisamment bien en charge IPv6, veuillez supprimer le contenu IPv6. Un exemple est présenté ci-dessous ; le contenu surligné correspond au contenu IPv6.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

    5. Vous pouvez également utiliser [l'application mobile](../faq/mobile_app.md) pour configurer OVPN.

??? "PrivateVPN"
    ### PrivateVPN

    [Site officiel](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Connectez-vous, puis accédez au [panneau de contrôle](https://privatevpn.com/control-panel){target="_blank"}

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Sélectionnez un serveur

        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Cliquez sur **GENERATE CONFIG**, puis copiez la configuration.

        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Site officiel](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Accédez au site web de PrivadoVPN, puis connectez-vous.

    Dans le tableau de bord, recherchez la section Manual Configuration, cliquez sur WireGuard. Sélectionnez le serveur auquel vous souhaitez vous connecter, puis cliquez sur Download Configration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "Proton VPN"
    ### Proton VPN

    [Site officiel](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Si vous utilisez [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, veuillez suivre le guide disponible [ici](https://protonvpn.com/support/wireguard-configurations/){target="_blank"} pour générer le fichier de configuration WireGuard.

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "PureVPN"
    ### PureVPN

    [Site officiel](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Veuillez consulter [ce guide](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} ou suivre les étapes ci-dessous pour obtenir manuellement le fichier de configuration PureVPN.

    1. Connectez-vous à la [PureVPN Member Area](https://my.puremember.com/){target="_blank"} avec votre compte. Après la connexion, cliquez sur **Manual Configuration** dans le menu de gauche.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Sélectionnez la ville cible, puis cliquez sur **Download** à droite.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. Dans la fenêtre pop-up, sélectionnez **WireGuard** comme protocole.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Sélectionnez **Linux** comme type d'appareil, puis cliquez sur **Generate Configuration**. Le fichier de configuration sera téléchargé sur votre appareil local.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour terminer la configuration.

    [Lien de référence](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Site officiel](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Connectez-vous à [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff), trouvez la section permettant d'obtenir votre configuration VPN, puis suivez les étapes pour l'obtenir.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Téléchargez la configuration VPN.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "StarVPN"
    ### StarVPN

    [Site officiel](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Créer un compte StarVPN**

        Rendez-vous dans les options de [tarifs](https://www.starvpn.com/#pricing){target="_blank"} et choisissez une offre VPN adaptée à vos besoins. Vous pouvez vous inscrire au moment du paiement ou directement [ici](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Télécharger la configuration WireGuard**

        Connectez-vous au [tableau de bord](https://www.starvpn.com/dashboard){target="_blank"} de l’espace membre StarVPN. Cliquez sur **Wireguard Config** pour télécharger le fichier de configuration. Chaque emplacement contient un fichier de configuration WireGuard unique.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Conseil** : si vous souhaitez utiliser les techniques d’obfuscation AmneziaWG, cliquez sur **AmneziaWG Config** pour télécharger le fichier de configuration. Chaque emplacement contient un fichier de configuration AmneziaWG unique.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Modifier le fichier de configuration (facultatif)**

        La configuration peut contenir une adresse IPv6. Pour éviter les problèmes de compatibilité et de connectivité, ouvrez le fichier `.conf` et supprimez l’adresse IPv6, comme indiqué ci-dessous.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour téléverser le fichier de configuration sur votre routeur GL.iNet.

    Références :

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Site officiel](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Si vous utilisez [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, connectez-vous sur [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}

    2. Sélectionnez un emplacement dans la liste déroulante, cliquez sur **GENERATE**, puis ouvrez le fichier texte téléchargé.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

    4. Vous pouvez également utiliser [l'application mobile](../faq/mobile_app.md) pour configurer StrongVPN.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Site officiel](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Accédez à [https://trust.zone/setup](https://trust.zone/setup) et connectez-vous.

    2. Faites défiler jusqu'à la section WireGuard, choisissez le port souhaité, puis téléchargez soit la configuration d'un serveur spécifique, soit un fichier zip contenant toutes les configurations.

    3. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "VPN.AC"
    ### VPN.AC

    [Site officiel](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Si vous utilisez [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, vous devez vous connecter au panneau de contrôle et trouver WireGuard Manager dans le menu "Services".

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Créez ensuite la configuration et téléchargez-la.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Site officiel](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Si vous utilisez [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, connectez-vous à votre [User Office](https://my.keepsolid.com/){target="_blank"} > sélectionnez l'application VPN Unlimited® > cliquez sur **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Appuyez sur le champ sous **Device** et cliquez sur **Manually create a new device…** > définissez un nom personnalisé, par exemple WireGuard > choisissez l'emplacement approprié du **Server** > sélectionnez le protocole **WireGuard**® dans la liste déroulante > cliquez sur **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}

    3. Les paramètres de configuration apparaîtront ensuite ci-dessous au format texte.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        Assemblez la configuration comme ci-dessous.

        <p>
        [Interface]</br>
        PrivateKey = <i>collez la PrivateKey depuis votre User Office</i></br>
        ListenPort = <i>collez les informations ListenPort</i></br>
        Address = <i>collez les informations Address</i></br>
        DNS = <i>collez les détails DNS depuis votre User Office</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>collez la PublicKey depuis votre User Office</i></br>
        PresharedKey = <i>collez les informations PresharedKey</i></br>
        AllowedIPs = <i>collez les informations AllowedIPs</i></br>
        Endpoint = <i>collez les informations Endpoint</i></br>
        </p>

    4. Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

    [Lien de référence 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Lien de référence 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Site officiel](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Connectez-vous à votre compte membre Windscribe [ici](https://windscribe.com/login?auth_required){target="_blank"}, puis ouvrez le [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Sélectionnez l'emplacement du serveur et le port que vous souhaitez utiliser, puis cliquez sur **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Suivez [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

??? "12VPX"
    ### 12VPX

    [Site officiel](https://12vpx.com/?aff=1174){target="_blank"}

    Si vous utilisez [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, connectez-vous puis accédez à [cette page](https://12vpx.com/setup/wireguard){target="_blank"} ; vous y verrez les configurations de tous les serveurs.

    Suivez ensuite [ce guide](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers) pour continuer.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
