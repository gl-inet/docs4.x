# Comment accéder aux appareils du LAN du serveur OpenVPN depuis le client via des noms de domaine ?

Ce tutoriel explique comment accéder, depuis un client et à l’aide de noms de domaine, aux appareils du domicile (tels qu’un NAS, une caméra IP, etc.) situés sur le LAN du serveur OpenVPN.

## Topologie

Comme illustré ci-dessous, vous pouvez accéder depuis un PC situé sur le LAN du client à des appareils tels qu’un NAS ou une caméra IP sur le LAN du serveur OpenVPN en utilisant leurs noms de domaine respectifs.

![topology](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Étapes de configuration

### 1. Modifier les hôtes sur le serveur (facultatif)

Cette étape s’applique lorsque votre serveur VPN ne peut pas résoudre correctement les noms de domaine locaux. Ignorez cette étape si vous n’êtes pas sûr.

Connectez-vous au panneau d’administration web de votre routeur serveur VPN, puis accédez à **NETWORK** -> **DNS** -> **Edit Hosts**.

![edit hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Saisissez l’adresse IP et le nom de domaine des appareils du domicile auxquels vous souhaitez accéder, puis cliquez sur **Apply**.

![input ip domain](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Autoriser l’accès à distance au LAN sur le serveur

Dans le panneau d’administration web du serveur, accédez à **VPN** -> **OpenVPN Server**. Cliquez sur **Options** dans l’angle supérieur droit.

![ovpnserver options 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Activez **Allow Remote Access the LAN Subnet**, puis cliquez sur **Apply**.

![ovpnserver allow access lan 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Une fois cette option activée, vous pouvez accéder à distance au routeur et aux appareils du LAN via le VPN.

### 3. Exporter la configuration VPN

Dans le panneau d’administration du serveur, accédez à **VPN** -> **OpenVPN Server** -> onglet **Configuration**, puis cliquez sur **Export Client Configuration** en bas de la page. 

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

Dans la fenêtre contextuelle, cliquez sur **Export**. 

**Remarque** : si l’adresse IP publique de votre serveur est dynamique et change de temps à autre, accédez d’abord à **APPLICATIONS** -> **Dynamic DNS** pour activer **DDNS** avant d’exporter la configuration client.

![export config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Vous obtiendrez ensuite un fichier **.ovpn**, comme illustré ci-dessous.

![downloads](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Si votre routeur serveur exécute le firmware v4.8 ou une version ultérieure, il n’est pas nécessaire de modifier le fichier de configuration ; passez à l’étape suivante.

Si votre routeur serveur exécute le firmware v4.7 ou une version antérieure, ouvrez ce fichier, ajoutez la ligne suivante pour définir le serveur DNS sur l’IP du tunnel de votre serveur OpenVPN, puis enregistrez vos modifications.

`dns server 1 address 10.8.0.1`

![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Astuce : le sous-réseau IPv4 du tunnel du serveur OpenVPN se trouve sous l’onglet **Configuration** de la page OpenVPN Server, comme illustré ci-dessous. Il varie selon la version du firmware. Vérifiez l’IP du tunnel de votre serveur OpenVPN.

![ovpnserver tunnel ip](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Activer le serveur VPN

Sur la page **OpenVPN Server**, cliquez sur le bouton **Start** dans l’angle supérieur droit pour démarrer le serveur.

![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Importer la configuration VPN

Connectez-vous au panneau d’administration web de votre routeur client VPN, accédez à **VPN** -> **OpenVPN Client**, puis cliquez sur **Add Manually**.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Créez un nom pour ce groupe et importez le fichier de configuration.

![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

L’importation a réussi. Cliquez sur **Apply**. 

![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Le fichier de configuration s’affichera ensuite ici.

![applied](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Démarrer la connexion du client VPN

Cliquez sur l’icône à trois points pour lancer la connexion VPN. 

![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Lorsque le point gris devient vert, le client OpenVPN s’est connecté au serveur avec succès.

![ovpnclient connected](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Vous pouvez maintenant accéder, depuis le PC situé sur le LAN du client, à vos appareils du domicile (tels qu’un NAS) sur le LAN du serveur en utilisant leurs noms de domaine.

![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Vous avez encore des questions ? Visitez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
