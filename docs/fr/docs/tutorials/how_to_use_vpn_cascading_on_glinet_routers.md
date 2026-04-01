# Comment utiliser le VPN Cascading sur les routeurs GL.iNet ?

## Introduction

Le VPN Cascading est parfois appelé « Double VPN » dans certains contextes, mais peut différer légèrement sur les routeurs GL.iNet. Le concept de base est illustré ci-dessous.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (Routeur comme serveur VPN)** : lorsque le routeur agit comme serveur VPN, les clients connectés à ce serveur accèdent à Internet via le réseau FAI du routeur par défaut.

**VPN 2 (Routeur comme client VPN)** : le routeur agit également comme client VPN, se connectant à un service VPN tiers.

**VPN Cascading** : le routeur transmettra le trafic du tunnel VPN 1 vers le tunnel VPN 2, ce qui permettra aux appareils connectés au routeur via VPN 1 d’accéder à Internet via le service VPN tiers (VPN 2) au lieu du réseau FAI du routeur.

## Comment activer le VPN Cascading

### Pour le firmware v4.7 et les versions antérieures

1. Configurez d’abord votre routeur comme serveur VPN. Le protocole WireGuard est recommandé pour une meilleure vitesse. Veuillez consulter [ce lien](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exportez un fichier de configuration depuis votre routeur et chargez-le sur un appareil client, qui se connectera au routeur via VPN.

3. Configurez votre routeur comme client VPN en le connectant à un service VPN tiers. Le protocole WireGuard est recommandé pour une meilleure vitesse. Veuillez consulter [ce lien](../interface_guide/wireguard_client.md){target="_blank"}.

4. Une fois connecté, la page **VPN Dashboard** s’affichera comme ci-dessous, où le routeur est configuré simultanément comme serveur VPN et client VPN.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Dans la section VPN Server de cette même page, cliquez sur **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Activez **VPN Cascading**, puis cliquez sur **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. Le VPN Cascading est activé. Les appareils connectés à votre routeur via VPN accéderont à Internet via le service VPN tiers, au lieu du réseau FAI du routeur.

### Pour le firmware v4.8 et les versions ultérieures

1. Configurez d’abord votre routeur comme serveur VPN. Le protocole WireGuard est recommandé pour une meilleure vitesse. Veuillez consulter [ce lien](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exportez un fichier de configuration depuis votre routeur et chargez-le sur un appareil client, qui se connectera au routeur via VPN.

3. Configurez votre routeur comme client VPN en le connectant à un service VPN tiers. Le protocole WireGuard est recommandé pour une meilleure vitesse. Veuillez consulter [ce lien](../interface_guide/wireguard_client.md){target="_blank"}.

4. Dans le panneau d’administration web, accédez à **VPN Dashboard**. Choisissez les instructions correspondantes ci-dessous selon votre mode VPN.

    ??? "Global Mode"
    
        Si votre mode VPN est Global Mode, dès que le client VPN est activé (comme illustré ci-dessous), le VPN Cascading s’active automatiquement. 
        
        Les appareils connectés à votre routeur via VPN accéderont à Internet via le service VPN tiers, au lieu du réseau FAI du routeur.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"
    
        Si votre mode VPN est Policy Mode, vous devez configurer la règle de tunnel VPN.
        
        Cliquez sur la case grisée à gauche.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Sélectionnez la source du trafic à laquelle appliquer cette règle. Pour activer le VPN Cascading, sélectionnez **All Clients**, ou sélectionnez **Specified Connection Types**, puis **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients** : cela inclut tous les appareils LAN, les appareils provenant de Drop-in Gateway, les appareils du réseau invité et les appareils connectés à votre routeur via VPN. 
        
            Si vous souhaitez que le trafic de tous les appareils utilise la même règle de tunnel, sélectionnez **All Clients**, puis cliquez sur **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types** : cette option vous permet de spécifier les appareils connectés au routeur par une méthode particulière (par ex. des appareils connectés via VPN) afin de leur appliquer cette règle de tunnel. 

            Si vous souhaitez que les clients VPN de votre routeur utilisent une règle différente de celle des autres appareils, sélectionnez **WireGuard/OpenVPN Server**, puis cliquez sur **Apply**.
        
            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}
            
            Voici un exemple de règles de tunnel VPN en Policy Mode.
            
            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. Le VPN Cascading est activé. Les appareils connectés à votre routeur via VPN accéderont à Internet via le service VPN tiers, au lieu du réseau FAI du routeur.

6. **Test de connexion** : sur un ordinateur portable connecté au routeur via VPN, ouvrez un navigateur et rendez-vous sur [What Is My IP](https://whatismyipaddress.com/){target="_blank"} pour vérifier son IP publique. 

    Si le site indique que l’adresse IP de l’ordinateur portable se trouve dans la région du serveur VPN tiers (Buenos Aires dans cet exemple), cela signifie que le VPN Cascading est actif.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
