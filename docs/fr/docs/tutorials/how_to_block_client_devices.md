# Comment bloquer des appareils clients spécifiques sur un routeur GL.iNet

Ce tutoriel vous montre comment bloquer des appareils clients spécifiques sur un routeur GL.iNet. En bloquant des appareils clients, vous empêchez les accès non autorisés à votre réseau. Cela permet de renforcer la sécurité de votre réseau ou de contrôler l'accès de votre famille à Internet.

Les routeurs GL.iNet bloquent les appareils clients en fonction de leur adresse MAC (un identifiant unique de 12 caractères attribué à chaque appareil sur un réseau). Cette méthode est également appelée filtrage d'adresses MAC. 

Il existe deux méthodes pour bloquer des appareils clients sur votre routeur GL.iNet : via le [panneau d'administration du routeur](#block-client-devices-via-the-admin-panel) ou via l'[application mobile GL.iNet](#block-client-devices-via-the-glinet-mobile-app). 

## Bloquer des appareils clients via le panneau d'administration {#block-client-devices-via-the-admin-panel}

### 1. Connectez-vous au panneau d'administration

Dans un navigateur Web, saisissez `192.168.8.1`. Entrez votre mot de passe, puis cliquez sur **Login**. 

### 2. Bloquer des appareils clients

Il existe deux façons de bloquer des appareils clients, selon que vous disposez ou non de leurs adresses MAC :

* Si vous n'avez pas leurs adresses MAC : utilisez la [première méthode](#method-1-block-devices-without-their-mac-addresses), qui vous permet de bloquer les appareils affichés dans les listes.
* Si vous avez leurs adresses MAC : utilisez la [deuxième méthode](#method-2-block-devices-with-their-mac-addresses). 

#### Méthode 1 : bloquer des appareils sans leurs adresses MAC {#method-1-block-devices-without-their-mac-addresses}

1. Dans la barre latérale gauche, cliquez sur **Clients**.
![click clients](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. À côté de l'appareil, activez l'interrupteur. 
![toggle switch](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Si vous ne voyez pas les appareils que vous souhaitez bloquer dans les listes, vous devrez les bloquer en [ajoutant leurs adresses MAC à la liste de blocage](#method-2-block-devices-with-their-mac-addresses). 

#### Méthode 2 : bloquer des appareils avec leurs adresses MAC {#method-2-block-devices-with-their-mac-addresses}

Pour utiliser cette méthode, vous devez obtenir l'adresse MAC de l'appareil. Reportez-vous aux instructions fournies par le fabricant de l'appareil. 
Une fois que vous avez l'adresse MAC de l'appareil, suivez les étapes suivantes : 

1. Dans la barre latérale gauche, cliquez sur **Clients**.
2. En haut, cliquez sur **Blocklist**. 
![click blocklist](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Suivez l'une des méthodes suivantes pour bloquer des appareils : 
    - Pour saisir les adresses MAC individuellement : saisissez-les dans le champ vide.
    - Pour importer une liste d'adresses MAC : cliquez sur **Import Clients**. Importez un fichier, puis cliquez sur **Import**. 
4. Cliquez sur **Apply**. 
![click apply](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Bloquer des appareils clients via l'application mobile GL.iNet {#block-client-devices-via-the-glinet-mobile-app}

**Remarque :** avant de commencer, installez et configurez l'application mobile GL.iNet sur votre appareil. 

Il existe deux façons de bloquer des appareils clients, selon que vous disposez ou non de leurs adresses MAC :

* Si vous n'avez pas leurs adresses MAC : utilisez la [première méthode](#mobile-1), qui vous permet de bloquer les appareils affichés dans la liste. 
* Si vous avez leurs adresses MAC : utilisez la [deuxième méthode](#mobile-2). 

### Méthode 1 : bloquer des appareils sans leurs adresses MAC {#mobile-1}

1. Sur l'écran principal de l'application, appuyez sur l'appareil que vous souhaitez bloquer sous **Connected Clients** et **Office Clients**. 
![tap a device](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. Dans **Settings**, activez l'interrupteur **Block**. 
![toggle block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Si vous ne voyez pas les appareils que vous souhaitez bloquer dans les listes, vous devrez les bloquer en [ajoutant leurs adresses MAC à la liste de blocage](#mobile-2)

### Méthode 2 : bloquer des appareils avec leurs adresses MAC {#mobile-2}

Pour utiliser cette méthode, vous devez obtenir l'adresse MAC de l'appareil que vous souhaitez bloquer. Reportez-vous aux instructions fournies par le fabricant. 
Une fois que vous avez l'adresse MAC de l'appareil, suivez les étapes suivantes : 

1. Sur l'écran principal de l'application, appuyez sur l'icône des paramètres > **Access Control**. 
![tap access control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Appuyez sur **Block**.
![tap block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Suivez l'une des méthodes suivantes pour bloquer des appareils : 
    - Pour saisir les adresses MAC individuellement : appuyez sur **Add MAC address**. Saisissez l'adresse MAC, puis appuyez sur **Done**. 
    - Pour importer une liste d'adresses MAC, appuyez sur **Import Clients** > **Import Clients**, puis appuyez sur le fichier à importer.

---

Vous avez encore des questions ? Visitez notre [Forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [Contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
