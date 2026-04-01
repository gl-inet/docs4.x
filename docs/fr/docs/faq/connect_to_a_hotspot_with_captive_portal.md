# Connecter un routeur GL.iNet à des points d'accès publics avec un portail captif

## Qu'est-ce qu'un portail captif ?

Un portail captif est une page web sur laquelle les points d'accès publics demandent aux utilisateurs d'afficher la page et d'interagir avec elle avant d'autoriser l'accès à Internet.

## Pourquoi utiliser un routeur avec des points d'accès publics ?

* Le Wi-Fi public n'est pas sûr

    Il est difficile de surestimer les risques du Wi-Fi public. En connectant votre routeur GL.iNet à un Wi-Fi public, vous pouvez vous connecter directement à votre compte VPN via le panneau d'administration du routeur. Le routeur chiffrera automatiquement tous les appareils connectés au réseau local, ce qui vous évite de configurer un VPN sur chaque appareil.

* Utiliser le routeur comme répéteur pour connecter plusieurs appareils

    En outre, certains réseaux Wi-Fi publics (par exemple le Wi-Fi d'hôtel) limitent l'accès à un certain nombre d'appareils, par exemple deux. Lors d'un voyage en groupe, cela n'est pas pratique. Vous pouvez à la place connecter un routeur de voyage au Wi-Fi de l'hôtel et l'utiliser comme répéteur pour diffuser un signal Wi-Fi vers tous vos appareils, notamment ordinateurs portables, smartphones, tablettes, etc. Le Wi-Fi de l'hôtel ne verra que le routeur de voyage comme un seul appareil, alors que vous pourrez connecter autant d'appareils que vous le souhaitez au Wi-Fi gratuit.

## Comment connecter un routeur à des points d'accès publics avec portail captif ?

Regardez cette vidéo ou suivez les étapes ci-dessous.

<iframe width="560" height="315" src="https://www.youtube.com/embed/CM4_soLf9fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. Connectez un smartphone ou un ordinateur au routeur.

    Mettez le routeur sous tension. Sur votre smartphone ou votre ordinateur, recherchez le SSID du routeur puis saisissez le mot de passe Wi-Fi. Le SSID et le mot de passe par défaut sont imprimés sous le routeur.

2. Connectez-vous au panneau d'administration web du routeur.

    Sur votre smartphone ou votre ordinateur, ouvrez un navigateur web et saisissez l'adresse IP du routeur (adresse IP par défaut : `192.168.8.1`) dans la barre d'adresse. Vous pourrez alors accéder au panneau d'administration web du routeur.
    
    S'il s'agit de votre première connexion, sélectionnez une langue et créez un mot de passe de connexion pour le panneau d'administration web du routeur.

3. Connectez votre routeur au point d'accès public. Veuillez consulter le tutoriel [Repeater](../interface_guide/internet_repeater.md/).

## Dépannage

Si vous n'arrivez pas à ouvrir le portail captif, il est possible que votre routeur ne puisse pas accéder à Internet. Essayez les méthodes de dépannage suivantes.

### Méthode 1 : activer le mode de connexion pour hotspots publics et le camouflage

**Remarque** : ces deux fonctionnalités sont disponibles uniquement à partir du firmware v4.6.

Lorsque vous connectez le routeur à un point d'accès public, l'activation des fonctions suivantes sur la page **Join Network** peut améliorer le taux de réussite de la connexion.

![hotspot login mode & camouflage](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/hotspot_login_mode_camouflage.png){class="glboxshadow"}

- Auto-Enable Login Mode for Public Hotspots

    Si cette option est activée, le routeur entrera automatiquement en Login Mode for Public Hotspots lorsqu'il sera connecté avec succès à un hotspot, mais pas encore à Internet. Dans ce mode, certains services seront suspendus et le mode DNS passera à automatique, ce qui peut exposer votre activité réseau au fournisseur du hotspot (par exemple un hôtel ou un centre commercial).

- Enable Camouflage

    Si cette option est activée, le routeur se fera passer pour l'appareil client que vous utilisez pour accéder au panneau d'administration en imitant l'adresse MAC de cet appareil.

---

### Méthode 2 : modifier les paramètres du routeur

1. Connectez-vous au panneau d'administration web, puis accédez à **NETWORK -> DNS**. Assurez-vous que **DNS Rebinding Attack Protection** est désactivé et que **Mode** est réglé sur **Automatic**.

    ![dns rebinding attack protection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/dns_rebinding_attack_protection.png){class="glboxshadow" width="600"}

2. Dans le panneau d'administration web, accédez à **VPN -> VPN Dashboard**. Assurez-vous que toutes les connexions VPN sont désactivées.

    **Pour le firmware v4.7 et antérieur**, la page s'affiche comme ci-dessous.
    
    ![vpn client disabled v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_client_is_disable.png){class="glboxshadow" width="600"}
    
    **Pour le firmware v4.8 et versions ultérieures**, la page s'affiche comme ci-dessous.

    ![vpn client disabled v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/vpn_disabled_4.8.png){class="glboxshadow" width="600"}

3. Dans le panneau d'administration web, accédez à **APPLICATIONS -> AdGuard Home**. Assurez-vous qu'AdGuard Home est désactivé.

    ![adguard home is stopped](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/adguardhome_init.png){class="glboxshadow"}

4. Ouvrez un navigateur web, saisissez de nouveau l'adresse du portail captif ou actualisez sa page. Attendez une minute et vérifiez si vous êtes automatiquement redirigé vers la page d'authentification du portail captif.

    Si vous utilisez un smartphone et que votre navigateur web ne redirige pas vers le portail captif, désactivez puis réactivez le Wi-Fi du smartphone, puis reconnectez-vous au Wi-Fi du routeur. Le portail captif devrait s'afficher directement après la saisie du mot de passe Wi-Fi.

    ![connected](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/connected.png){class="glboxshadow"}

---

### Méthode 3 : clonage d'adresse MAC

Certains hôtels limitent le nombre d'appareils que chaque client peut connecter au Wi-Fi de l'hôtel en identifiant leurs adresses MAC, et enregistrent l'adresse MAC du premier appareil connecté. Dans ce cas, vous pouvez cloner vers le routeur l'adresse MAC utilisée par votre téléphone pour se connecter au Wi-Fi de l'hôtel, afin que le routeur utilise cette adresse MAC pour accéder au Wi-Fi de l'hôtel.

1. Connectez votre téléphone au Wi-Fi de l'hôtel. Relevez l'adresse MAC que votre téléphone utilise pour se connecter au Wi-Fi de l'hôtel.

    Voici un exemple sur iPhone (iOS 16.1.2) : allez dans Settings -> Wi-Fi -> sélectionnez le Wi-Fi de l'hôtel et vous verrez l'adresse Wi-Fi. Notez cette adresse.

    ![iphone wifi private address](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/iphone_wifi_private_address.png){class="glboxshadow" width="350"}

    Sur certains anciens modèles, l'adresse MAC peut ne pas être disponible dans les paramètres Wi-Fi. Dans ce cas, l'appareil peut utiliser sa véritable adresse MAC pour se connecter au Wi-Fi public. Vous pouvez alors la trouver dans Settings > About (ou "About Phone") sur votre téléphone.

2. Connectez votre téléphone ou votre ordinateur au routeur. Connectez-vous au panneau d'administration web du routeur, puis clonez cette adresse MAC ou saisissez-la manuellement.

    **Pour le firmware v4.5 et antérieur**, sélectionnez **NETWORK** dans la barre latérale gauche -> **MAC Address**.

    Sélectionnez **Manual Mode**, saisissez l'adresse MAC obtenue à l'étape 1, puis cliquez sur **Apply**.

    ![MAC manual](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/mac_address_manual.png){class="glboxshadow"}

    **Pour le firmware v4.6 et versions ultérieures**, sélectionnez **INTERNET** dans la barre latérale gauche -> section **Repeater**, puis cliquez sur **Modify**.

    ![repeater modify](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_modify.png){class="glboxshadow gl-90-desktop"}

    Dans la fenêtre contextuelle, réglez **MAC Mode** sur **Clone**, saisissez manuellement l'adresse MAC, puis cliquez sur **Apply**.

    ![repeater clone mac](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_a_hotspot_with_captive_portal/repeater_clone_mac.png){class="glboxshadow gl-90-desktop"}

3. Il peut être nécessaire de redémarrer le routeur pour que la modification prenne effet.

---

### Méthode 4 : demander de l'aide au personnel de l'hôtel

Certains hôtels appliquent des politiques de vérification très strictes à leur réseau. Si aucune des méthodes ci-dessus ne fonctionne, essayez de demander au personnel de l'hôtel d'ajouter directement l'adresse MAC de votre routeur (utilisez l'adresse MAC d'usine par défaut, et non une adresse aléatoire) à la liste blanche du réseau de l'hôtel.

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.

