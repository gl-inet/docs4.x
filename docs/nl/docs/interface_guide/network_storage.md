# Network Storage {#network-storage}

## Inleiding {#introduction}

Met netwerkopslag kun je bestanden draadloos tussen apparaten delen door een USB-station of SD-kaart op de router aan te sluiten. De router maakt er een gedeeld netwerkstation van voor alle apparaten op Wi-Fi.

Sommige GL.iNet-modellen hebben een MicroSD(TF)-sleuf en andere USB-poorten voor flashstations en draagbare externe schijven. Je kunt Samba, WebDAV en DLNA configureren. Gangbare indelingen zoals NTFS, FAT32 en EXT4 worden ondersteund.

!!! Note

    1. Een USB-schijf verbruikt veel stroom. Gebruik een externe voeding om storingen te voorkomen.

    2. Sommige modellen hebben een USB-poort of MicroSD-sleuf, maar onvoldoende opslagruimte en ondersteunen geen netwerkopslag.

    3. Via het webbeheerpaneel kun je alleen gedeelde mappen beheren. Gebruik de [mobiele app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} om bestanden te beheren.

## Ondersteunde modellen {#supported-models}

Modellen met USB-poorten of MicroSD(TF)-sleuven ondersteunen gewoonlijk netwerkopslag.

Apparaten met maximaal 32MB flashopslag ondersteunen Network Storage nog niet.

| Routermodel                           | Samba | WebDAV | DLNA | USB-poort | MicroSD-kaart |
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

## Opslagapparaat aansluiten {#connect-storage-device}

Schakel voor een TF-kaart de router uit, plaats de kaart en schakel de router in.

Sluit een USB-station rechtstreeks aan. Verbind een draagbare externe schijf zo mogelijk met een afzonderlijke voeding.

Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/network_storage_init.png){class="glboxshadow"}

Sluit het opslagapparaat aan. Na detectie ziet de pagina er als volgt uit.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/disk_found.png){class="glboxshadow"}

## Samba instellen {#set-up-samba}

1. Schakel **Enable Samba** in en klik op **Apply**.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba1.png){class="glboxshadow"}

    * Allow Access Samba from WAN: schakel dit in als upstream apparaten toegang tot Samba moeten hebben.

2. Klik op **Quick Setup Share** om de gedeelde link in te stellen.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba2.png){class="glboxshadow"}

3. Voeg een gebruiker toe en klik op **Next**. Deze stap wordt overgeslagen als je al een account hebt.

    ![samba add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba3.png){class="glboxshadow"}

4. Klik op het driehoekpictogram voor alle mappen. Selecteer een map en klik op **Next**. Klik op de schijfnaam, bijvoorbeeld disk1_part1, om de hele schijf te delen.

    ![samba add shared folder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba4.png){class="glboxshadow"}

5. Stel de gedeelde map in.

    De gebruiker wordt standaard aan **Read-Only User** toegevoegd. Verplaats deze naar **Read-Write User** om schrijven of verwijderen toe te staan en klik op **Apply**.

    Om veiligheidsredenen raden we **Anonymous Access** af.

    ![samba shared folder settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba5.png){class="glboxshadow"}

6. Verkrijg de toegangslink voor de map.

    De pagina toont links voor Windows en Unix-achtige systemen, waaronder Android, iOS, macOS en Ubuntu.

    Je kunt de gedeelde map nu via Samba openen. Klik [hier](#samba-client) voor meer informatie.

    ![samba folder access link](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba6.png){class="glboxshadow"}

    **Opmerking:** als **Allow Access Samba from WAN** is ingeschakeld, vervang je voor toegang vanaf het upstream netwerk het standaardrouter-IP 192.168.8.1 in de link door het WAN-IP op de pagina INTERNET.

---

## WebDAV instellen {#set-up-webdav}

1. Schakel **Enable WebDAV** in en klik op **Apply**.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav1.png){class="glboxshadow"}

    * Allow Access WebDAV from WAN: schakel dit in als upstream apparaten toegang tot WebDAV moeten hebben.

    * WebDAV Protocol: **HTTP** is niet versleuteld; gebruik op eigen risico. **HTTPS** is versleuteld en gebruikt een zelfondertekend certificaat.

    * WebDAV Port: wijzig de poort alleen bij een conflict. Het aanbevolen bereik is 1024-65535.

2. Klik op **Quick Setup Share** om de gedeelde link in te stellen.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav2.png){class="glboxshadow"}

3. Voeg een gebruiker toe en klik op **Next**. Deze stap wordt overgeslagen als je al een account hebt.

    ![webdav add a user](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav3.png){class="glboxshadow"}

4. Klik op het driehoekpictogram voor alle mappen. Selecteer een map en klik op **Next**. Klik op de schijfnaam, bijvoorbeeld disk1_part1, om de hele schijf te delen.

    ![webdav add shared folder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav4.png){class="glboxshadow"}

5. Stel de gedeelde map in.

    De gebruiker wordt standaard aan **Read-Only User** toegevoegd. Verplaats deze naar **Read-Write User** om schrijven of verwijderen toe te staan en klik op **Apply**.

    Om veiligheidsredenen raden we **Anonymous Access** af.

    ![webdav shared folder settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav5.png){class="glboxshadow"}

6. Verkrijg de toegangslink voor de map.

    De pagina toont links voor Windows en Unix-achtige systemen, waaronder Android, iOS, macOS en Ubuntu.

    Je kunt de gedeelde map nu via WebDAV openen. Klik [hier](#webdav-client) voor meer informatie.

    ![webdav folder access link](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav6.png){class="glboxshadow"}

    **Opmerking:** als **Allow Access WebDAV from WAN** is ingeschakeld, vervang je voor toegang vanaf het upstream netwerk het standaardrouter-IP 192.168.8.1 in de link door het WAN-IP op de pagina INTERNET.

---

## DLNA instellen {#set-up-dlna}

1. Schakel **Enable DLNA** in en klik op **Apply**.

    ![enable dlna](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna1.png){class="glboxshadow"}

2. Wijzig zo nodig rechts Share Path.

    ![dlna share path](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna2.png){class="glboxshadow"}

3. Verbind je smart-tv met de router. De DLNA-server wordt automatisch gevonden.

---

## Samba-client {#samba-client}

=== "Windows"

    Windows 11 wordt als voorbeeld gebruikt; dit geldt ook voor Windows 10.

    Open File Explorer, klik links met de rechtermuisknop op **This PC** en kies **Show more options** -> **Add a network location**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Klik op **Choose a custom network location** en vervolgens op **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Voer de Samba-toegangslink in en klik op **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Geef de locatie een naam en klik op **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Klik op **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Voer zo nodig de gebruikersnaam en het wachtwoord in en klik op **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Je kunt Samba via Finder openen.

    Open Finder en klik op Go -> Connect to Server. Plak de Samba-toegangslink.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Voer de gebruikersnaam en het wachtwoord uit **Shared Folder Settings** in.

    Kies **Guest** als Anonymous Access is ingesteld.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Klik op **Continue**. Samba verschijnt in de zijbalk van Finder.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Veel Android-apps ondersteunen Samba. [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} wordt als voorbeeld gebruikt.

    Klik op de startpagina op **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Klik op **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Klik op **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Voer **Host**, **Username** en **Password** in. Selecteer bij **Anonymous Access** **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    De iOS-app [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} ondersteunt Samba. Je kunt ook [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} gebruiken.

    Hieronder staat hoe je via **Files** en **Documents** verbinding maakt.

    - Via de app [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} met Samba verbinden.

        Open **Files**. De app is standaard geïnstalleerd maar kan worden verwijderd; installeer deze zo nodig opnieuw via de App Store.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width="300"}

        Open onderaan **Browse** en tik rechtsboven op "…" voor het contextmenu.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width="560"}

        Tik op **Connect to Server**, voer de URL uit [Shared Link](#set-up-samba) in en tik rechtsboven op **Next**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width="560"}

        Voer voor een beveiligde share de gegevens in. Tik op **Registered User** en vul **Name** en **Password** in. Kies "Guest" bij **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width="560"}

        Tik rechtsboven op **Next** om verbinding te maken. Het iOS-apparaat toont de beschikbare shares.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width="560"}

        De Samba-share staat onderaan onder **Shared**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width="560"}

    - Via de app [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} met Samba verbinden.

        Klik rechtsonder op de plusknop.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Klik op **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Klik op **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** is de verbindingsnaam, **URL** de toegangslink en **Login** de gebruikersnaam. Laat bij anonieme toegang **Login** en **Password** leeg.

        Klik op **Done** om de installatie te voltooien.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV-client {#webdav-client}

=== "Windows"

    Veel software ondersteunt WebDAV, zoals [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"} en [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    RaiDrive wordt als voorbeeld gebruikt.

    Klik op **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    Klik onder **Storage** op **NAS** -> **WebDAV**.

    Schakel onder **Address** het selectievakje in of uit voor HTTPS/HTTP en voer het adres in.

    Voer onder **Account** de gebruikersnaam en het wachtwoord in of selecteer **Anonymous**.

    Klik op **Connect**. Er wordt een X-station aan File Explorer toegevoegd.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    Veel apps ondersteunen WebDAV, zoals [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} en [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    FE File Explorer wordt als voorbeeld gebruikt.

    Klik op Add.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Selecteer **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Voer de verbindingsinstellingen in. Laat bij anonieme toegang **User Name** en **Password** leeg. Klik op **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Er kan een waarschuwing verschijnen over een niet-vertrouwd certificaat. Dit komt door het zelfondertekende certificaat; vertrouw het om door te gaan.

=== "Android"

Veel Android-apps ondersteunen WebDAV. [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"} wordt als voorbeeld gebruikt.

    Opmerking: Cx File Explorer ondersteunt geen anonieme toegang.

    Klik op de startpagina op **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Klik op **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Klik op **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Voer **Host**, **Port**, **Username** en **Password** in.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Veel iOS-apps ondersteunen WebDAV. [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"} wordt als voorbeeld gebruikt.

    Klik rechtsonder op de plusknop.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Klik op **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Klik op **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** is de verbindingsnaam, **URL** de toegangslink en **Login** de gebruikersnaam.

    Klik op **Done** om de installatie te voltooien.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Mobiele app gebruiken {#using-mobile-app}

Via het webbeheerpaneel kun je alleen gedeelde mappen beheren. Gebruik de [mobiele app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"} om bestanden te beheren.

- Via het **lokale netwerk** toont de app het opslagapparaat en de capaciteit en ondersteunt lezen en schrijven.

- Via de **cloud** toont de app het opslagapparaat en de capaciteit, maar ondersteunt geen lezen of schrijven.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
