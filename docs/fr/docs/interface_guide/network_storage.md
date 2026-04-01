# Stockage réseau

## Sommaire

- [Introduction](#introduction)
- [Modèles pris en charge](#supported-models)
- [Insérer un périphérique de stockage](#insert-storage-device)
- [Configurer Samba](#set-up-samba)
- [Configurer WebDAV](#set-up-webdav)
- [Configurer DLNA](#set-up-dlna)
- [Client Samba](#samba-client)
- [Client WebDAV](#webdav-client)

## Introduction {#introduction}

Le stockage réseau permet de partager des fichiers sans fil entre plusieurs appareils en connectant un lecteur USB ou une carte SD à votre routeur. Le routeur transforme le périphérique de stockage en lecteur réseau partagé, accessible à tous les appareils connectés au Wi-Fi.

Certains modèles GL.iNet disposent d'un emplacement pour carte MicroSD(TF), tandis que d'autres possèdent des ports USB compatibles avec les clés USB et les disques durs externes portables. Vous pouvez configurer Samba, WebDAV et DLNA pour ces périphériques de stockage, qui prennent en charge des formats courants tels que NTFS, FAT32 et EXT4.

!!! Note 

    1. La consommation électrique d'un disque dur USB est assez élevée. Utilisez une alimentation externe, sinon cela peut provoquer un dysfonctionnement.

    2. Certains modèles disposent d'un port USB ou d'un emplacement MicroSD, mais leur espace de stockage est limité et ils ne prennent pas en charge le stockage réseau.

    3. Le panneau d'administration web permet uniquement de gérer les dossiers partagés. Pour gérer les fichiers sur votre périphérique de stockage, veuillez utiliser l'[application mobile](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Modèles pris en charge {#supported-models}

En général, les modèles équipés de ports USB ou d'emplacements MicroSD(TF) prennent en charge le stockage réseau (c.-à-d. le partage de fichiers). 

Pour les appareils dotés d'une mémoire flash de 32MB ou moins, la fonction Network Storage n'est pas encore prise en charge.

| Modèle de routeur                       | Samba | WebDAV | DLNA | Port USB | Carte MicroSD |
| :------------------------------------- | :---: | :----: | :--: | :------: | :-----------: |
| GL-E5800 (Mudi 7)                      | √     | √      | √    | √        | -             |
| GL-MT5000 (Brume 3)                    | √     | √      | √    | √        | -             |
| GL-BE3600 (Slate 7)                    | √     | √      | √    | √        | -             |
| GL-X2000 (Spitz Plus)                  | √     | √      | √    | √        | -             |
| GL-MT6000 (Flint 2)                    | √     | √      | √    | √        | -             |
| GL-XE3000 (Puli AX)                    | √     | √      | √    | √        | √             |
| GL-X3000 (Spitz AX)                    | √     | √      | √    | √        | √             |
| GL-MT3000 (Beryl AX)                   | √     | √      | √    | √        | -             |
| GL-MT2500/GL-MT2500A (Brume 2)         | √     | √      | √    | √        | -             |
| GL-AXT1800 (Slate AX)                  | √     | √      | √    | √        | √             |
| GL-AX1800 (Flint)                      | √     | √      | √    | √        | -             |
| GL-A1300 (Slate Plus)                  | √     | √      | √    | √        | -             |
| GL-S1300 (Convexa-S)                   | √     | √      | √    | √        | -             |
| GL-SFT1200 (Opal)</br>***FW 4.7.2**    | √     | -      | -    | √        | -             |
| GL-E750V2 (Mudi V2)</br>***FW 4.7.2**  | √     | -      | -    | √        | √             |
| GL-AR750S-EXT (Slate)</br>***FW 4.7.2**| √     | -      | -    | √        | √             |

## Insérer un périphérique de stockage {#insert-storage-device}

Pour une carte TF, vous devez d'abord éteindre le routeur, insérer la carte TF, puis rallumer le routeur.

Pour un lecteur USB, vous pouvez le brancher directement sur le port USB. Pour un disque dur externe portable, si vous disposez d'une alimentation séparée, veuillez l'y connecter.

Connectez-vous au panneau d'administration web du routeur et allez dans **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Connectez le périphérique de stockage. Lorsqu'il est détecté, la page s'affiche comme ci-dessous.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Configurer Samba {#set-up-samba}

1. Activez **Enable Samba**, puis cliquez sur **Apply**.

    * Allow Access Samba from WAN: Activez cette option si vous souhaitez que les appareils du réseau amont puissent accéder à Samba.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Cliquez sur **Quick Setup Share** pour définir le lien de partage.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Ajoutez un utilisateur, puis cliquez sur **Next**. Cette étape sera ignorée si vous avez déjà un compte. 

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Cliquez sur l'icône en forme de triangle pour afficher tous les dossiers. Sélectionnez un dossier à partager, ou cliquez sur le nom du disque (disk1_part1) si vous souhaitez partager l'ensemble du disque. Cliquez ensuite sur **Next**.

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configurez le dossier partagé.

    Pour des raisons de sécurité, il n'est pas recommandé d'activer **Anonymous Access**.

    L'utilisateur créé à l'étape précédente sera ajouté à **Read-Only User** par défaut. Si vous souhaitez que cet utilisateur puisse écrire ou supprimer des fichiers, retirez-le de **Read-Only User**, ajoutez-le à **Writable User**, puis cliquez sur **Apply**.

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Récupérez le lien d'accès au dossier. 

    La page affichera le lien pour Windows et pour les systèmes de type Unix. Les systèmes de type Unix incluent Android, iOS, macOS, Ubuntu, etc. 
    
    Vous pouvez désormais accéder à votre dossier partagé via le service Samba à l'aide de ces liens. Cliquez [ici](#samba-client) pour plus de détails.

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Remarque :** Si vous activez **Allow Access Samba from WAN** et accédez au dossier partagé depuis le réseau amont, remplacez l'adresse IP du routeur (192.168.8.1 par défaut) dans le lien d'accès par l'adresse IP WAN de votre routeur, que vous pouvez trouver sur la page INTERNET du panneau d'administration web.

---

## Configurer WebDAV {#set-up-webdav}

1. Activez **Enable WebDAV**, puis cliquez sur **Apply**.

    * Allow Access WebDAV from WAN: Activez cette option si vous souhaitez que les appareils du réseau amont puissent accéder à WebDAV.

    * WebDAV Protocol: **HTTP** n'est pas chiffré ; utilisez-le à vos risques. **HTTPS** est chiffré et utilise un certificat auto-signé.

    * WebDAV Port: Il n'est pas nécessaire de modifier le numéro de port, sauf en cas de conflit. La plage de ports recommandée est 1024 - 65535.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Cliquez sur **Quick Setup Share** pour définir le lien de partage.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Ajoutez un utilisateur, puis cliquez sur **Next**. Cette étape sera ignorée si vous avez déjà un compte.

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Cliquez sur l'icône en forme de triangle pour afficher tous les dossiers. Sélectionnez un dossier à partager, ou cliquez sur le nom du disque (disk1_part1) pour partager l'ensemble du disque. Cliquez ensuite sur **Next**.

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configurez le dossier partagé.

    Pour des raisons de sécurité, il n'est pas recommandé d'activer **Anonymous Access**.

    L'utilisateur créé à l'étape précédente sera ajouté à **Read-Only User** par défaut. Si vous souhaitez que cet utilisateur puisse écrire ou supprimer des fichiers, retirez-le de **Read-Only User**, ajoutez-le à **Writable User**, puis cliquez sur **Apply**.

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Récupérez le lien d'accès au dossier. 

    La page affichera le lien pour Windows et pour les systèmes de type Unix. Les systèmes de type Unix incluent Android, iOS, macOS, Ubuntu, etc. 
    
    Vous pouvez désormais accéder à votre dossier partagé via le service WebDAV à l'aide de ces liens. Cliquez [ici](#webdav-client) pour plus de détails.

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Remarque :** Si vous activez **Allow Access WebDAV from WAN** et accédez au dossier partagé depuis le réseau amont, remplacez l'adresse IP du routeur (192.168.8.1 par défaut) dans le lien d'accès par l'adresse IP WAN de votre routeur, que vous pouvez trouver sur la page INTERNET du panneau d'administration web.

---

## Configurer DLNA {#set-up-dlna}

Activez **Enable DLNA**, puis cliquez sur **Apply**.

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Connectez votre téléviseur intelligent au routeur, et il détectera le serveur DLNA.

---

## Client Samba {#samba-client}

=== "Windows"

    Voici un exemple sous Windows 11, également valable pour Windows 10.

    Ouvrez l'Explorateur de fichiers, puis faites un clic droit sur **This PC** (dans le volet de gauche). Dans le menu contextuel qui s'affiche, sélectionnez **Show more options** -> **Add a network location**

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Cliquez sur **Choose a custom network location**, puis sur **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Saisissez le lien d'accès Samba, puis cliquez sur **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Donnez un nom à cet emplacement. Cliquez sur **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Cliquez sur **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Si un nom d'utilisateur et un mot de passe sont requis, une fenêtre vous invitera à saisir les identifiants. Cliquez ensuite sur **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Vous pouvez accéder à Samba via le Finder.

    Ouvrez le Finder, puis cliquez sur Go -> Connect to Server dans le menu. Copiez-collez le lien d'accès Samba.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Le système vous demandera le nom d'utilisateur et le mot de passe ; le nom d'utilisateur correspond à celui défini dans **Shared Folder Settings**.
    
    Si vous avez configuré l'accès anonyme, choisissez **Guest** dans l'image ci-dessous.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Cliquez sur **Continue** ; Samba s'affichera dans la barre latérale du Finder.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    De nombreuses applications Android prennent en charge Samba. Voici un exemple avec [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Sur la page d'accueil, cliquez sur **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Cliquez sur **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Cliquez sur **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Saisissez **Host**, **Username** et **Password**. Si **Anonymous Access** est activé, cochez **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    L'application [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} sur iOS prend en charge Samba ; vous pouvez aussi utiliser d'autres applications, par exemple [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    La section suivante explique comment se connecter à Samba avec l'application **Files** puis avec l'application **Documents**.

    - Guide pour se connecter à un serveur Samba avec l'application [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}.

        Ouvrez l'application **Files**. Elle est installée par défaut, vous devriez donc la trouver sur votre écran d'accueil. Comme **Files** est désormais une application amovible, vous devrez peut-être la réinstaller depuis l'App Store si elle n'apparaît pas.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Assurez-vous d'être dans l'onglet **Browse** en bas de l'écran. Touchez l'icône « … » (trois points) en haut à droite pour afficher le menu contextuel de l'application.
        
        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Touchez l'option **Connect to Server** en haut du menu. Sur l'écran suivant, saisissez l'URL de connexion de votre serveur. Vous trouverez cette URL dans le [lien partagé](#shared-link). Touchez le bouton **Next** en haut à droite pour continuer.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        L'écran suivant vous permet de saisir les identifiants d'authentification si vous vous connectez à un partage réseau protégé. Touchez **Registered User** et renseignez les champs **Name** et **Password** avec votre nom d'utilisateur et votre mot de passe Samba. Vous pouvez aussi toucher « Guest » si vous avez activé **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Appuyez sur le bouton **Next** en haut à droite pour terminer la connexion. Votre appareil iOS devrait se connecter correctement au serveur et afficher la liste des partages disponibles.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        Le partage Samba sera affiché en bas du menu, sous l'intitulé **Shared**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Guide pour se connecter à un serveur Samba avec l'application [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

        Cliquez sur le bouton plus en bas à droite.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Cliquez sur **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Cliquez sur **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** correspond au nom de cette connexion. **URL** est le lien d'accès. **Login** est le nom d'utilisateur. S'il s'agit d'un accès anonyme, laissez simplement **Login** et **Password** vides.

        Cliquez sur le bouton **Done** pour terminer cette configuration.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## Client WebDAV {#webdav-client}

=== "Windows"

    De nombreux logiciels prennent en charge WebDAV, par exemple [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.
    
    Voici un exemple avec RaiDrive.

    Cliquez sur **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    Dans la zone **Storage**, cliquez sur **NAS** -> **WebDAV**.

    Dans la zone **Address**, cochez ou décochez la case située à côté de Address pour basculer entre https et http, puis saisissez l'adresse.

    Dans la zone **Account**, saisissez le nom d'utilisateur et le mot de passe, ou cochez **Anonymous**.

    Enfin, cliquez sur **Connect** ; un lecteur X sera ajouté dans l'Explorateur de fichiers.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    De nombreuses applications prennent en charge WebDAV, par exemple [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Voici un exemple avec FE File Explorer.

    Cliquez sur le bouton Add.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Sélectionnez **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Saisissez les paramètres de connexion. S'il s'agit d'un accès anonyme, laissez simplement **User Name** et **Password** vides. Cliquez ensuite sur **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Il se peut qu'un avertissement s'affiche, indiquant *The following secure server (null) uses an untrusted certificate. Trust this server?* ; cela est dû à l'utilisation d'un certificat auto-signé, veuillez donc l'accepter.

=== "Android"

    De nombreuses applications Android prennent en charge WebDAV. Voici un exemple avec [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Remarque : Cx File Explorer ne prend pas en charge l'accès anonyme.

    Sur la page d'accueil, cliquez sur **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Cliquez sur **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Cliquez sur **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Saisissez **Host**, **Port**, **Username** et **Password**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    De nombreuses applications iOS prennent en charge WebDAV. Voici un exemple avec [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Cliquez sur le bouton plus en bas à droite.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Cliquez sur **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Cliquez sur **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** correspond au nom de cette connexion. **URL** est le lien d'accès. **Login** est le nom d'utilisateur.

    Cliquez sur le bouton **Done** pour terminer cette configuration.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Utiliser l'application mobile

Le panneau d'administration web permet uniquement de gérer les dossiers partagés. Pour gérer les fichiers sur votre périphérique de stockage, veuillez utiliser l'[application mobile](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

- Lorsque vous accédez à l'application via le **réseau local**, elle affiche votre périphérique de stockage et sa capacité, et prend en charge la lecture/écriture.

- Lorsque vous accédez à l'application via le **cloud**, elle affiche votre périphérique de stockage et sa capacité, mais ne prend pas en charge la lecture/écriture.

---

Vous avez encore des questions ? Consultez notre [forum communautaire](https://forum.gl-inet.com){target="_blank"} ou [contactez-nous](https://www.gl-inet.com/contacts/){target="_blank"}.
