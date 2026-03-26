# Comment accéder aux appareils du LAN du serveur WireGuard depuis le client via des noms de domaine ?

Ce tutoriel explique comment accéder, depuis un client et à l’aide de noms de domaine, aux appareils du domicile (tels qu’un NAS, une caméra IP, etc.) situés sur le LAN du serveur WireGuard.

## Topologie

Comme illustré ci-dessous, vous pouvez accéder depuis un PC situé sur le LAN du client à des appareils tels qu’un NAS ou une caméra IP sur le LAN du serveur WireGuard en utilisant leurs noms de domaine respectifs.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Étapes de configuration

### 1. Modifier les hôtes sur le serveur (facultatif)

Cette étape s’applique lorsque votre serveur VPN ne peut pas résoudre correctement les noms de domaine locaux. Ignorez cette étape si vous n’êtes pas sûr.

Connectez-vous au panneau d’administration web de votre routeur serveur VPN, puis accédez à **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Saisissez l’adresse IP et le nom de domaine des appareils du domicile auxquels vous souhaitez accéder, puis cliquez sur **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Autoriser l’accès à distance au LAN sur le serveur

??? "Pour un routeur serveur exécutant le firmware v4.8"

    Dans le panneau d’administration web du serveur, accédez à **VPN** -> **WireGuard Server**. Cliquez sur **Options** dans l’angle supérieur droit.

    ![server options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Activez **Allow Remote Access the LAN Subnet**, puis cliquez sur **Apply**.

    ![server allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Une fois cette option activée, ce routeur et les appareils du LAN sont accessibles à distance via le VPN.**

??? "Pour un routeur serveur exécutant le firmware v4.7 ou une version antérieure"

    Dans le panneau d’administration web du serveur, accédez à **VPN** -> **VPN Dashboard** -> section **VPN Server**. Cliquez sur l’icône d’engrenage à droite du serveur WireGuard.

    ![server options 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Activez **Remote Access LAN**, puis cliquez sur **Apply**.

    ![server allow access lan 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Une fois cette option activée, ce routeur et les appareils du LAN sont accessibles à distance via le VPN.**

### 3. Exporter la configuration VPN

Dans le panneau d’administration du serveur, accédez à **VPN** -> **WireGuard Server** -> onglet **Profiles**, puis cliquez sur **Add** pour exporter un profil de configuration. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Vous obtiendrez ensuite un fichier **.conf**, comme illustré ci-dessous.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Ouvrez ce fichier. Assurez-vous que le champ DNS du fichier pointe vers l’IP du tunnel du serveur, affichée sous l’onglet **Configuration** de la page WireGuard Server, comme illustré ci-dessous. Supprimez également `64.6.64.6` du champ DNS s’il est présent afin d’éviter un échec de résolution DNS.

![dns field](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![wg tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Remarque** : l’IP du tunnel du serveur WireGuard varie selon la version du firmware. Vérifiez l’IP du tunnel de votre serveur.

### 4. Activer le serveur VPN

Sur la page **WireGuard Server**, cliquez sur le bouton **Start** dans l’angle supérieur droit pour démarrer le serveur.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Importer la configuration VPN

Connectez-vous au panneau d’administration web de votre routeur client VPN, accédez à **VPN** -> **WireGuard Client**, puis cliquez sur **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Créez un nom pour ce groupe et importez le fichier de configuration.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

L’importation a réussi. Cliquez sur **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Le fichier de configuration s’affichera ensuite ici.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Démarrer la connexion du client VPN

Cliquez sur l’icône à trois points pour lancer la connexion VPN. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Lorsque le point gris devient vert, le client WireGuard s’est connecté au serveur avec succès.

![wgclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Vous pouvez maintenant accéder, depuis le PC situé sur le LAN du client, à vos appareils du domicile (tels qu’un NAS) sur le LAN du serveur en utilisant leurs noms de domaine.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
