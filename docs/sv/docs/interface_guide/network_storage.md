# Network Storage {#network-storage}

## Introduction {#introduction}

Nätverkslagring delar filer trådlöst genom att ansluta en USB-enhet eller ett SD-kort till routern. Lagringen blir en delad nätverksenhet för Wi-Fi-anslutna enheter.

Vissa GL.iNet-modeller har MicroSD(TF)-kortplats och andra USB-port för flashenheter och externa hårddiskar. Samba, WebDAV och DLNA stöder format som NTFS, FAT32 och EXT4.

!!! Note

    1. USB-hårddiskar förbrukar mycket ström. Använd extern strömförsörjning för att undvika fel.

    2. Vissa modeller har USB- eller MicroSD-port men stöder inte nätverkslagring på grund av begränsat utrymme.

    3. Webbadministrationspanelen hanterar endast delade mappar. Använd [mobilappen](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} för filer.

## Supported Models {#supported-models}

Usually, models with USB ports or MicroSD(TF) slots support network storage (i.e. file sharing).

Network Storage stöds inte på enheter med högst 32MB flashlagring.

| Router Model                           | Samba | Webdav | DLNA | USB Port | MicroSD Card |
| :------------------------------------- | :---: | :---: | :---: | :------: | :----------: |
| GL-MT6000 (Fortify)                    | √     | √     | √     | √        | -            |
| GL-MG1300 (Mango 2)                    | √     | -     | -     | √        | -            |
| GL-BE14000 (Flint 4)                   | √     | √     | √     | √        | -            |
| GL-BE10000 (Slate 7 Pro)               | √     | √     | √     | √        | -            |
| GL-E5800 (Mudi 7)                      | √     | √     | √     | √        | -            |
| GL-MT3600BE (Beryl 7)                  | √     | √     | √     | √        | -            |
| GL-MT5000 (Brume 3)                    | √     | √     | √     | √        | -            |
| GL-BE9300 (Flint 3)                    | √     | √     | √     | √        | -            |
| GL-BE6500 (Flint 3e)                   | √     | √     | √     | √        | -            |
| GL-BE3600 (Slate 7)                    | √     | √     | √     | √        | -            |
| GL-X2000 (Spitz Plus)                  | √     | √     | √     | √        | -            |
| GL-MT6000 (Flint 2)                    | √     | √     | √     | √        | -            |
| GL-XE3000 (Puli AX)                    | √     | √     | √     | √        | √            |
| GL-X3000 (Spitz AX)                    | √     | √     | √     | √        | √            |
| GL-MT3000 (Beryl AX)                   | √     | √     | √     | √        | -            |
| GL-MT2500/GL-MT2500A (Brume 2)         | √     | √     | √     | √        | -            |
| GL-AXT1800 (Slate AX)                  | √     | √     | √     | √        | √            |
| GL-AX1800 (Flint)                      | √     | √     | √     | √        | -            |
| GL-A1300 (Slate Plus)                  | √     | √     | √     | √        | -            |
| GL-S1300 (Convexa-S)                   | √     | √     | √     | √        | -            |
| GL-SFT1200 (Opal)<br>**FW 4.8+**     | √     | -     | -     | √        | -            |
| GL-E750V2 (Mudi V2)<br>**FW 4.8+**   | √     | -     | -     | √        | √            |
| GL-AR750S-EXT (Slate)<br>**FW 4.7+** | √     | -     | -     | √        | √            |

## Connect Storage Device {#connect-storage-device}

Stäng av routern, sätt in TF-kortet och slå på routern.

Anslut en USB-enhet direkt. Anslut en extern hårddisk till separat strömförsörjning om sådan finns.

Logga in och öppna **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/network_storage_init.png){class="glboxshadow"}

Anslut lagringsenheten. När den identifieras visas sidan nedan.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/disk_found.png){class="glboxshadow"}

## Set Up Samba {#set-up-samba}

1. Aktivera **Enable Samba** och klicka på **Apply**.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba1.png){class="glboxshadow"}

    * Allow Access Samba from WAN: Aktivera om uppströms enheter ska nå Samba.

2. Klicka på **Quick Setup Share** för delningslänken.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba2.png){class="glboxshadow"}

3. Lägg till en användare och klicka på **Next**. Steget hoppas över om ett konto redan finns.

    ![samba add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba3.png){class="glboxshadow"}

4. Klicka på triangeln, välj en mapp och klicka på **Next**. Klicka på disknamnet, till exempel disk1_part1, för hela disken.

    ![samba add shared folder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba4.png){class="glboxshadow"}

5. Set up the shared folder.

    Användaren läggs som standard till i **Read-Only User**. Flytta den till **Read-Write User** för skrivning och radering och klicka på **Apply**.

    For security reasons, it is not recommended to enable **Anonymous Access**.

    ![samba shared folder settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba5.png){class="glboxshadow"}

6. Obtain the folder access link.

    Sidan visar länkar för Windows och Unix-liknande system som Android, iOS, macOS och Ubuntu.

    Öppna den delade mappen via Samba med länkarna. Klicka [här](#samba-client) för mer information.

    ![samba folder access link](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba6.png){class="glboxshadow"}

    **Obs!** Med **Allow Access Samba from WAN** ersätter du routerns IP (standard 192.168.8.1) i länken med WAN-IP från sidan INTERNET.

---

## Set Up WebDAV {#set-up-webdav}

1. Aktivera **Enable WebDAV** och klicka på **Apply**.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav1.png){class="glboxshadow"}

    * Allow Access WebDAV from WAN: Aktivera om uppströms enheter ska nå WebDAV.

    * WebDAV Protocol: **HTTP** är okrypterat och används på egen risk. **HTTPS** är krypterat och använder självsignerat certifikat.

    * WebDAV Port: No need to modify the port number unless there's a conflict. The recommended port number range is 1024 - 65535.

2. Klicka på **Quick Setup Share** för delningslänken.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav2.png){class="glboxshadow"}

3. Lägg till en användare och klicka på **Next**. Steget hoppas över om ett konto redan finns.

    ![webdav add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav3.png){class="glboxshadow"}

4. Klicka på triangeln, välj en mapp och klicka på **Next**. Klicka på disknamnet, till exempel disk1_part1, för hela disken.

    ![webdav add shared folder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav4.png){class="glboxshadow"}

5. Set up the shared folder.

    Användaren läggs som standard till i **Read-Only User**. Flytta den till **Read-Write User** för skrivning och radering och klicka på **Apply**.

    For security reasons, it is not recommended to enable **Anonymous Access**.

    ![webdav shared folder settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav5.png){class="glboxshadow"}

6. Obtain folder access link.

    Sidan visar länkar för Windows och Unix-liknande system som Android, iOS, macOS och Ubuntu.

    Öppna den delade mappen via WebDAV med länkarna. Klicka [här](#webdav-client) för mer information.

    ![webdav folder access link](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav6.png){class="glboxshadow"}

    **Obs!** Med **Allow Access WebDAV from WAN** ersätter du routerns IP (standard 192.168.8.1) i länken med WAN-IP från sidan INTERNET.

---

## Set Up DLNA {#set-up-dlna}

1. Aktivera **Enable DLNA** och klicka på **Apply**.

    ![enable dlna](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna1.png){class="glboxshadow"}

2. Ändra Share Path till höger vid behov.

    ![dlna share path](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna2.png){class="glboxshadow"}

3. Anslut smart-TV:n till routern. DLNA-servern hittas automatiskt.

---

## Samba Client {#samba-client}

=== "Windows"

    Windows 11 används som exempel och gäller även Windows 10.

    Öppna Utforskaren, högerklicka på **This PC** och välj **Show more options** -> **Add a network location**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Klicka på **Choose a custom network location** och **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Ange Samba-länken och klicka på **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Namnge platsen och klicka på **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Click **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Ange användarnamn och lösenord om det efterfrågas och klicka på **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Samba kan öppnas via Finder.

    Öppna Finder och välj Go -> Connect to Server. Klistra in Samba-länken.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Ange användarnamnet och lösenordet från **Shared Folder Settings**.

    Välj **Guest** för anonym åtkomst.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Klicka på **Continue**. Samba visas i Finders sidofält.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Flera Android-appar stöder Samba, till exempel [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Klicka på **NETWORK** på startsidan.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Ange **Host**, **Username** och **Password**. Markera **Anonymous** för anonym åtkomst.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    iOS-appen [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} och exempelvis [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} stöder Samba.

    Följande avsnitt beskriver anslutning med **Files** respektive **Documents**.

    - Guide of connect to Samba server by [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} app.

        Öppna **Files**. Den är normalt installerad men kan behöva installeras om från App Store.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width="300"}

        Öppna fliken **Browse** och tryck på ikonen "…" uppe till höger.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width="560"}

        Tryck på **Connect to Server**, ange serverns URL från [Shared Link](#set-up-samba) och tryck på **Next**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width="560"}

        För en skyddad resurs väljer du **Registered User** och anger **Name** och **Password**. Välj Guest för **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width="560"}

        Tryck på **Next** för att ansluta och visa tillgängliga resurser.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width="560"}

        Samba-resursen visas längst ned under **Shared**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width="560"}

    - Guide of connect to Samba server by [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} app.

        Klicka på plusknappen nere till höger.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Click **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Click **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** är anslutningsnamn, **URL** åtkomstlänk och **Login** användarnamn. Lämna Login och Password tomma för anonym åtkomst.

        Klicka på **Done**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV Client {#webdav-client}

=== "Windows"

    WebDAV stöds av bland annat [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"} och [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    Here is an example of RaiDrive.

    Click **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    Klicka på **NAS** -> **WebDAV** under **Storage**.

    In the **Address** area, check/uncheck the checkbox near Address to switch https/http, enter the address.

    Ange användarnamn och lösenord under **Account** eller markera **Anonymous**.

    Klicka på **Connect** för att lägga till en X-enhet i Utforskaren.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    WebDAV stöds av appar som [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} och [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Here is an example of FE File Explorer.

    Click Add button.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Select **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Ange anslutningsinställningar. Lämna **User Name** och **Password** tomma för anonym åtkomst. Klicka på **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Varningen *The following secure server (null) uses an untrusted certificate. Trust this server?* kan visas på grund av det självsignerade certifikatet. Godkänn servern.

=== "Android"

    Flera Android-appar stöder WebDAV, till exempel [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Note: Cx File Explorer doesn't support anonymous access.

    Klicka på **NETWORK** på startsidan.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Click **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Click **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Input the **Host**, **Port**, **Username**, **Password**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Flera iOS-appar stöder WebDAV, till exempel [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Klicka på plusknappen nere till höger.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Click **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Click **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** är anslutningsnamn, **URL** åtkomstlänk och **Login** användarnamn.

    Klicka på **Done**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Using Mobile App {#using-mobile-app}

Webbadministrationspanelen hanterar endast delade mappar. Använd [mobilappen](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} för filer.

- Via **lokalt nätverk** visar appen lagringsenheten och kapaciteten och stöder läsning/skrivning.

- Via **molnet** visas lagringsenheten och kapaciteten utan läs-/skrivåtkomst.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
