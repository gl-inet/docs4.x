# Comment configurer Urban Shield VPN sur un routeur GL.iNet

[Urban Shield VPN](https://urbanshieldvpn.com/) est un fournisseur VPN dédié à des solutions VPN à la fois hautement sécurisées et performantes pour les utilisateurs du monde entier. Il propose des routeurs VPN GL.iNet préconfigurés ainsi que des formules d'abonnement flexibles, afin d'assurer une navigation sécurisée et privée. Il suffit d'activer Urban Shield VPN sur votre routeur pour bénéficier de l'accès à ses serveurs mondiaux et naviguer ou diffuser du contenu en toute tranquillité.

## Guide de configuration

L'exemple ci-dessous utilise un GL-B3000 pour activer Urban Shield VPN en le configurant comme client WireGuard. 

### 1. Créer un compte Urban Shield VPN

Rendez-vous sur le [site officiel d'Urban Shield VPN](https://urbanshieldvpn.com/){class="_blank"} ou cliquez [ici](https://payment.urbanshieldvpn.com/sign-up) pour créer un compte Urban Shield VPN.

![Urban Shield VPN signup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Mise sous tension et connexion

Allumez votre routeur. Connectez ensuite un appareil au routeur à l'aide d'un câble Ethernet ou via le Wi-Fi.

### 3. Accéder au panneau d'administration web

Suivez les étapes ci-dessous pour accéder au panneau d'administration web. Si vous êtes déjà connecté, passez à la [partie suivante](#4-network-setup).

Ouvrez un navigateur web (Chrome, Edge ou Safari sont recommandés) et accédez à [192.168.8.1](http://192.168.8.1){target="_blank"}. Vous serez dirigé vers la configuration initiale du panneau d'administration web, comme illustré ci-dessous. Définissez votre mot de passe administrateur et cliquez sur **Next** pour continuer.

![set up admin password](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Configurez votre réseau Wi-Fi. La page affiche les informations Wi-Fi d'usine, y compris le nom du Wi-Fi (SSID) et le mot de passe, que vous pouvez modifier ou conserver. Si vous modifiez ces informations, reconnectez votre appareil au Wi-Fi mis à jour.

![set up wifi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Cliquez ensuite sur **Next** pour vous connecter avec votre mot de passe administrateur.

### 4. Configuration du réseau {#4-network-setup}

Un **Network Setup Wizard** est disponible dans l'angle supérieur droit (à partir du firmware v4.7). Suivez cet assistant pour configurer l'accès Internet de votre routeur avant de mettre en place le VPN.

![network setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Activer Urban Shield VPN

Dans le menu de gauche, sélectionnez **VPN** -> **WireGuard Client**. Vous verrez alors une page de connexion intégrée à Urban Shield VPN.

![log in 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Saisissez votre **Email** et votre **Password**, puis cliquez sur **Save And Continue**. Des fichiers de configuration seront générés pour chaque serveur.

![log in 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Sélectionnez le serveur de votre choix, puis cliquez sur **Apply**. 

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Le ou les serveurs disponibles apparaîtront alors dans la liste.

![get server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Cliquez sur l'icône à trois points pour lancer la connexion.

![start server](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Une fois la connexion établie, un point bleu s'affiche pour indiquer que la connexion est réussie.

![server started](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Vous pouvez également vérifier l'état de la connexion dans le VPN Dashboard.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Modifier les informations du compte ou se déconnecter

Cliquez sur l'icône en forme d'engrenage pour modifier les informations du compte ou vous déconnecter.

![edit account or logout 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![edit account or logout 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Renouveler

Si vous cliquez sur **Go Renew**, vous serez redirigé vers le site officiel pour renouveler votre abonnement.

![go renew](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Supprimer 

Vous pouvez supprimer tous les fichiers de configuration en un seul clic, ainsi que la clé privée et la clé publique.

![delete](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
