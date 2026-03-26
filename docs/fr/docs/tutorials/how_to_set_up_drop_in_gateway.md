# Comment configurer Drop-in Gateway sur un routeur GL.iNet

GL.iNet propose la fonctionnalité Drop-in Gateway, qui améliore les capacités de votre routeur principal avec des fonctions qu’il ne possède peut-être pas, notamment AdGuard Home, un DNS chiffré et le VPN. En utilisant cette fonctionnalité, vous pouvez continuer à utiliser votre routeur principal comme d’habitude tout en profitant de fonctions supplémentaires. 

Vous pouvez activer Drop-in Gateway pour [tous vos appareils](#enable-drop-in-gateway-for-all-devices) ou pour des [appareils spécifiques](#enable-drop-in-gateway-for-specific-devices) connectés à votre routeur principal. Suivez la section appropriée selon votre configuration.

**Note**: Les modèles avec une version de firmware inférieure à v4.5.0 ne prennent en charge l’activation de Drop-in Gateway que pour tous les appareils. Lorsque Drop-in Gateway est activé, tous les appareils clients sont mis en réseau via Drop-in Gateway, ce qui signifie que tout le trafic des clients connectés est d’abord traité par ce routeur.

---

## Activer Drop-in Gateway pour tous les appareils {#enable-drop-in-gateway-for-all-devices}

### 1. Connecter le routeur GL.iNet au routeur principal

Connectez le port WAN du routeur GL.iNet au port LAN du routeur principal à l’aide d’un câble Ethernet.

### 2. Activer Drop-in Gateway 

Il existe deux méthodes pour activer Drop-in Gateway : via le panneau d’administration du routeur ou via l’application mobile GL.iNet. 

<a id="using-web-admin-panel"></a>
??? "Utiliser le panneau d’administration web"

    1. Dans un navigateur web, saisissez `192.168.8.1`.  

    2. Saisissez votre mot de passe, puis cliquez sur **Login**. 

    3. Dans la barre latérale gauche, cliquez sur **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. À côté de **Enable Drop-in Gateway Mode**, activez l’interrupteur. 

    5. Sélectionnez **All devices are networked through drop-in gateway**. 

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Cliquez sur **Apply**. 

<a id="using-glinet-mobile-app"></a>
??? "Utiliser l’application mobile GL.iNet"

    **Note:** Avant de commencer, installez l’application mobile GL.iNet sur votre appareil. 

    1. Sur l’écran principal de l’application, appuyez sur l’onglet **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Appuyez sur **Enable**. 

    3. Pour **Devices are networked via drop-in gateway**, appuyez sur **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Appuyez sur **Done**. 

### 3. Désactiver le serveur DHCP sur le routeur principal

Veuillez vous connecter à votre routeur principal pour désactiver le serveur DHCP. Vous pouvez vous référer aux instructions fournies par le fabricant de votre routeur ou contacter son assistance. 

### 4. Configurer AdGuard, le DNS, le VPN et les autres fonctionnalités

Suivez ces guides pour activer les fonctionnalités souhaitées sur votre routeur GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

## Activer Drop-in Gateway pour des appareils spécifiques {#enable-drop-in-gateway-for-specific-devices}

### 1. Connecter le routeur GL.iNet au routeur principal

Connectez le port WAN du routeur GL.iNet au port LAN du routeur principal à l’aide d’un câble Ethernet.

### 2. Activer Drop-in Gateway

Il existe deux méthodes pour activer Drop-in Gateway : via le [panneau d’administration du routeur](#using-web-admin-panel-specific) ou via l’[application mobile GL.iNet](#using-glinet-mobile-app-specific). 

<a id="using-web-admin-panel-specific"></a>
??? "Utiliser le panneau d’administration web"

    1. Dans un navigateur web, saisissez `192.168.8.1`. 

    2. Saisissez votre mot de passe, puis cliquez sur **Login**. 

    3. Dans la barre latérale gauche, cliquez sur **Network** > **Drop-in Gateway**. 

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. À côté de **Enable Drop-in Gateway Mode**, activez l’interrupteur. 
    
    5. Sélectionnez **Some devices select their own networking gateway**. 

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Cliquez sur **Apply**. 

    **Note:** Veuillez **NE PAS** fermer cet onglet. Vous devrez saisir l’adresse IP (affichée à l’écran) à l’étape suivante.

<a id="using-glinet-mobile-app-specific"></a>
??? "Utiliser l’application mobile GL.iNet"

    **Note:** Avant de commencer, installez l’application mobile GL.iNet sur votre appareil. 

    1. Sur l’écran principal de l’application, appuyez sur l’onglet **System** > **Drop-in Gateway**.
    
        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
    
    2. Appuyez sur **Enable**. 
    
    3. Pour **Devices are networked via drop-in gateway**, appuyez sur **part**.
    
        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Appuyez sur **Done**. 

    **Note:** Veuillez **NE PAS** fermer cet onglet. Vous devrez saisir l’adresse IP (affichée à l’écran) à l’étape suivante. 

### 3. Définir la passerelle et le DNS sur l’appareil spécifique

??? "Windows"
    
    1. Connectez votre appareil au routeur principal. 
    2. Sous Windows, ouvrez **Settings** > **Network & Internet**.
    3. Selon votre méthode de connexion, suivez ces étapes : 
        * Ethernet : cliquez sur **Ethernet**. 
        * Wi-Fi : cliquez sur **Wi-Fi**, puis sur le nom du réseau Wi-Fi. 
    4. Copiez l’adresse IPv4. À côté de **IP assignment**, cliquez sur **Edit**. 
    5. Cliquez sur **Manual**. 
    6. Activez **IPv4**.
    7. Saisissez les informations suivantes : 
        * **IP address:** Collez l’adresse IP copiée à l’étape 4. 
        * **Subnet mask:** Saisissez **255.255.255.0**. 
        * **Gateway:** Saisissez l’adresse IP affichée sur la page **Drop-in Gateway**. 
        * **Preferred DNS:**  Saisissez l’adresse IP affichée sur la page **Drop-in Gateway**. 
    8. Cliquez sur **Save**. 

??? "Android"
    1. Connectez votre appareil au routeur principal. 
    2. Sur votre appareil Android, ouvrez **Settings**. 
    3. Appuyez sur **Connections** > **Wi-Fi**.
    4. Appuyez sur l’icône **Settings** à côté du réseau auquel vous êtes connecté. 
    5. Appuyez sur **View more**. 
    6. Appuyez sur **IP settings** > **Static**. 
    7. Pour **Gateway** et **DNS 1**, saisissez l’adresse IP affichée sur l’écran **Drop-in Gateway**. 
    8. Appuyez sur **Save**. 

??? "iOS"
    1. Connectez votre appareil au routeur principal. 
    2. Sur votre appareil iOS, ouvrez **Settings**.
    3. Appuyez sur **Wi-Fi**.
    4. Appuyez sur le réseau Wi-Fi auquel vous êtes connecté. 
    5. Sous **IPv4 Address**, notez **IP Address** et **Subnet Mask**.
    6. Appuyez sur **Configure IP** > **Manual**. 
    7. Saisissez les informations suivantes : 
        * **IP Address:** Saisissez l’adresse IP obtenue à l’étape 5. 
        * **Subnet Mask:** Saisissez le masque de sous-réseau obtenu à l’étape 5. 
        * **Router:** Saisissez l’adresse IP affichée sur l’écran **Drop-in Gateway**. 
    8. Appuyez sur **Save**.
    9. Appuyez sur **Configure DNS**, puis sur **Manual**. 
    10. Appuyez sur **Add Server**, puis saisissez l’adresse IP affichée sur l’écran **Drop-in Gateway**.
    11. Appuyez sur **Save**.

??? "Mac"
    1. Connectez votre appareil au routeur principal.
    2. Sur votre Mac, cliquez sur l’icône Apple > **System Settings**. 
    3. Dans la barre latérale gauche, cliquez sur **Network**.
    4. À côté du réseau auquel vous êtes connecté, cliquez sur **Details**.
    5. Cliquez sur **TCP/IP**.
    6. Notez **IP Address** et **Subnet Mask**.
    7. À côté de **Configure IPv4**, cliquez sur **Manually**.
    8. Saisissez les informations suivantes : 
        * **IP address:** Saisissez l’IP Address obtenue à l’étape 6. 
        * **Subnet mask:** Saisissez le Subnet Mask obtenu à l’étape 6. 
        * **Router:** Saisissez l’adresse IP affichée sur la page **Drop-in Gateway**. 
    9. Cliquez sur **OK** > **OK**. 

### 4. Configurer AdGuard, le DNS, le VPN et les autres fonctionnalités

Suivez ces guides pour activer les fonctionnalités souhaitées sur votre routeur GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGaurd Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

Article connexe :

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Vous avez encore des questions ? Consultez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
