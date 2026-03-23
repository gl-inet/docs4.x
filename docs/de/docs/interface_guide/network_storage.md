# Network Storage

## Inhalt

- [Einführung](#einführung)
- [Unterstützte Modelle](#unterstützte-modelle)
- [Speichergerät einsetzen](#speichergerät-einsetzen)
- [Samba einrichten](#samba-einrichten)
- [WebDAV einrichten](#webdav-einrichten)
- [DLNA einrichten](#dlna-einrichten)
- [Samba-Client](#samba-client)
- [WebDAV-Client](#webdav-client)

## Einführung

Mit Network Storage können Dateien drahtlos zwischen Geräten freigegeben werden, indem Sie ein USB-Laufwerk oder eine SD-Karte an Ihren Router anschließen. Der Router stellt das Speichergerät als freigegebenes Netzlaufwerk bereit, auf das alle über Wi-Fi verbundenen Geräte zugreifen können.

Einige GL.iNet-Modelle verfügen über einen MicroSD(TF)-Kartenslot, andere über USB-Ports für USB-Sticks und tragbare externe Festplatten. Für diese Speichergeräte können Sie Samba, WebDAV und DLNA konfigurieren. Unterstützt werden gängige Formate wie NTFS, FAT32 und EXT4.

!!! Note 

    1. Der Stromverbrauch einer USB-Festplatte ist relativ hoch. Verwenden Sie sie mit externer Stromversorgung, da es sonst zu Fehlfunktionen kommen kann.

    2. Einige Modelle besitzen zwar einen USB-Port oder einen MicroSD-Slot, verfügen jedoch nur über begrenzten Speicherplatz und unterstützen kein Network Storage.

    3. Im webbasierten Admin Panel können Sie nur freigegebene Ordner verwalten. Um Dateien auf Ihrem Speichergerät zu verwalten, verwenden Sie bitte die [mobile app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Unterstützte Modelle

In der Regel unterstützen Modelle mit USB-Port oder MicroSD(TF)-Slot Network Storage, also die Dateifreigabe.

Bei Geräten mit 32 MB Flash-Speicher oder weniger wird die Network-Storage-Funktion derzeit nicht unterstützt.

| Routermodell                           | Samba | Webdav | DLNA | USB-Port | MicroSD-Karte |
| :------------------------------------- | :---: | :---: | :---: | :------: | :-----------: |
| GL-E5800 (Mudi 7)                      | √     | √     | √     | √        | -             |
| GL-MT5000 (Brume 3)                    | √     | √     | √     | √        | -             |
| GL-BE3600 (Slate 7)                    | √     | √     | √     | √        | -             |
| GL-X2000 (Spitz Plus)                  | √     | √     | √     | √        | -             |
| GL-MT6000 (Flint 2)                    | √     | √     | √     | √        | -             |
| GL-XE3000 (Puli AX)                    | √     | √     | √     | √        | √             |
| GL-X3000 (Spitz AX)                    | √     | √     | √     | √        | √             |
| GL-MT3000 (Beryl AX)                   | √     | √     | √     | √        | -             |
| GL-MT2500/GL-MT2500A (Brume 2)         | √     | √     | √     | √        | -             |
| GL-AXT1800 (Slate AX)                  | √     | √     | √     | √        | √             |
| GL-AX1800 (Flint)                      | √     | √     | √     | √        | -             |
| GL-A1300 (Slate Plus)                  | √     | √     | √     | √        | -             |
| GL-S1300 (Convexa-S)                   | √     | √     | √     | √        | -             |
| GL-SFT1200 (Opal)</br>***FW 4.7.2**    | √     | -     | -     | √        | -             |
| GL-E750V2 (Mudi V2)</br>***FW 4.7.2**  | √     | -     | -     | √        | √             |
| GL-AR750S-EXT (Slate)</br>***FW 4.7.2**| √     | -     | -     | √        | √             |

## Speichergerät einsetzen

Bei einer TF-Karte müssen Sie den Router zunächst ausschalten, die TF-Karte einsetzen und den Router anschließend wieder einschalten.

Ein USB-Laufwerk können Sie direkt an den USB-Port anschließen. Bei einer tragbaren externen Festplatte verbinden Sie diese bitte zusätzlich mit einer separaten Stromversorgung, falls vorhanden.

Melden Sie sich am webbasierten Admin Panel des Routers an und gehen Sie zu **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Schließen Sie das Speichergerät an. Sobald es erkannt wurde, wird die Seite wie unten angezeigt.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Samba einrichten

1. Aktivieren Sie **Enable Samba** und klicken Sie auf **Apply**.

    * **Allow Access Samba from WAN**: Aktivieren Sie diese Option, wenn Geräte im vorgelagerten Netzwerk auf Samba zugreifen sollen.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Klicken Sie auf **Quick Setup Share**, um den Freigabelink einzurichten.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Fügen Sie einen Benutzer hinzu und klicken Sie auf **Next**. Wenn bereits ein Konto vorhanden ist, wird dieser Schritt übersprungen.

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Klicken Sie auf das Dreiecksymbol, um alle Ordner anzuzeigen. Wählen Sie einen Ordner für die Freigabe aus oder klicken Sie auf den Datenträgernamen (`disk1_part1`), wenn Sie den gesamten Datenträger freigeben möchten. Klicken Sie anschließend auf **Next**.

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Richten Sie den freigegebenen Ordner ein.

    Aus Sicherheitsgründen wird nicht empfohlen, **Anonymous Access** zu aktivieren.

    Der im vorherigen Schritt erstellte Benutzer wird standardmäßig zu **Read-Only User** hinzugefügt. Wenn dieser Benutzer Dateien schreiben oder löschen können soll, entfernen Sie ihn aus **Read-Only User** und fügen ihn zu **Writable User** hinzu. Klicken Sie dann auf **Apply**.

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Rufen Sie den Zugriffslink für den Ordner ab.

    Auf der Seite wird der Link für Windows und Unix-ähnliche Betriebssysteme angezeigt. Zu Unix-ähnlichen Systemen zählen unter anderem Android, iOS, macOS und Ubuntu.

    Sie können jetzt über den Samba-Dienst über diese Links auf Ihren freigegebenen Ordner zugreifen. Details finden Sie [hier](#samba-client).

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Hinweis:** Wenn Sie **Allow Access Samba from WAN** aktivieren und aus einem vorgelagerten Netzwerk auf den freigegebenen Ordner zugreifen, ersetzen Sie bitte die Router-IP im Zugriffslink (standardmäßig `192.168.8.1`) durch die WAN-IP Ihres Routers. Diese finden Sie auf der INTERNET-Seite im webbasierten Admin Panel.

---

## WebDAV einrichten

1. Aktivieren Sie **Enable WebDAV** und klicken Sie auf **Apply**.

    * **Allow Access WebDAV from WAN**: Aktivieren Sie diese Option, wenn Geräte im vorgelagerten Netzwerk auf WebDAV zugreifen sollen.

    * **WebDAV Protocol**: **HTTP** ist nicht verschlüsselt; verwenden Sie es auf eigenes Risiko. **HTTPS** ist verschlüsselt und verwendet ein selbstsigniertes Zertifikat.

    * **WebDAV Port**: Die Portnummer muss nur geändert werden, wenn es einen Konflikt gibt. Der empfohlene Portbereich ist 1024 bis 65535.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Klicken Sie auf **Quick Setup Share**, um den Freigabelink einzurichten.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Fügen Sie einen Benutzer hinzu und klicken Sie auf **Next**. Wenn bereits ein Konto vorhanden ist, wird dieser Schritt übersprungen.

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Klicken Sie auf das Dreiecksymbol, um alle Ordner anzuzeigen. Wählen Sie einen Ordner für die Freigabe aus oder klicken Sie auf den Datenträgernamen (`disk1_part1`), um den gesamten Datenträger freizugeben. Klicken Sie anschließend auf **Next**.

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Richten Sie den freigegebenen Ordner ein.

    Aus Sicherheitsgründen wird nicht empfohlen, **Anonymous Access** zu aktivieren.

    Der im vorherigen Schritt erstellte Benutzer wird standardmäßig zu **Read-Only User** hinzugefügt. Wenn dieser Benutzer Dateien schreiben oder löschen können soll, entfernen Sie ihn aus **Read-Only User** und fügen ihn zu **Writable User** hinzu. Klicken Sie dann auf **Apply**.

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Rufen Sie den Zugriffslink für den Ordner ab.

    Auf der Seite wird der Link für Windows und Unix-ähnliche Betriebssysteme angezeigt. Zu Unix-ähnlichen Systemen zählen unter anderem Android, iOS, macOS und Ubuntu.

    Sie können jetzt über den WebDAV-Dienst über diese Links auf Ihren freigegebenen Ordner zugreifen. Details finden Sie [hier](#webdav-client).

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Hinweis:** Wenn Sie **Allow Access WebDAV from WAN** aktivieren und aus einem vorgelagerten Netzwerk auf den freigegebenen Ordner zugreifen, ersetzen Sie bitte die Router-IP im Zugriffslink (standardmäßig `192.168.8.1`) durch die WAN-IP Ihres Routers. Diese finden Sie auf der INTERNET-Seite im webbasierten Admin Panel.

---

## DLNA einrichten

Aktivieren Sie **Enable DLNA** und klicken Sie auf **Apply**.

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Verbinden Sie Ihren Smart-TV mit dem Router; er findet dann den DLNA-Server.

---

## Samba-Client

=== "Windows"

    Hier ist ein Beispiel mit Windows 11; es gilt auch für Windows 10.

    Öffnen Sie den Datei-Explorer und klicken Sie dann mit der rechten Maustaste auf **This PC** (im linken Bereich). Wählen Sie im Kontextmenü **Show more options** -> **Add a network location**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Klicken Sie auf **Choose a custom network location** und dann auf **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Geben Sie den Samba-Zugriffslink ein und klicken Sie dann auf **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Geben Sie diesem Speicherort einen Namen. Klicken Sie auf **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Klicken Sie auf **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Wenn Benutzername und Passwort erforderlich sind, werden Sie zur Eingabe der Zugangsdaten aufgefordert. Klicken Sie dann auf **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Auf Samba können Sie über den Finder zugreifen.

    Öffnen Sie den Finder und klicken Sie im Menü auf Go -> Connect to Server. Kopieren Sie den Samba-Zugriffslink und fügen Sie ihn ein.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Anschließend werden Sie nach Benutzername und Passwort gefragt. Der Benutzername entspricht dem Namen, den Sie bei **Shared Folder Settings** eingerichtet haben.

    Wenn Sie anonymen Zugriff eingerichtet haben, wählen Sie in der folgenden Abbildung bitte **Guest**.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Klicken Sie auf **Continue**. Danach wird Samba in der Seitenleiste des Finders angezeigt.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Es gibt viele Android-Apps mit Samba-Unterstützung. Hier ist ein Beispiel mit [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Tippen Sie auf der Startseite auf **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Tippen Sie auf **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Tippen Sie auf **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Geben Sie **Host**, **Username** und **Password** ein. Bei **Anonymous Access** aktivieren Sie bitte **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    Die iOS-App [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} unterstützt Samba. Alternativ können Sie andere Apps verwenden, z. B. [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Im folgenden Abschnitt wird beschrieben, wie Sie sich jeweils mit der **Files**-App und der **Documents**-App mit Samba verbinden.

    - Anleitung zum Verbinden mit einem Samba-Server über die [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}-App.

        Öffnen Sie die **Files**-App. Sie ist standardmäßig installiert und sollte auf Ihrem Home-Bildschirm zu finden sein. Da **Files** inzwischen entfernt werden kann, müssen Sie die App gegebenenfalls erneut aus dem App Store installieren, wenn sie nicht angezeigt wird.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Stellen Sie sicher, dass Sie sich unten auf der Registerkarte **Browse** befinden. Tippen Sie oben rechts auf das Symbol „…“ (drei Punkte), um das Kontextmenü der App anzuzeigen.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Tippen Sie oben im Menü auf **Connect to Server**. Geben Sie auf dem nächsten Bildschirm die URL für die Serververbindung ein. Sie finden die URL unter [Shared Link](#shared-link). Tippen Sie oben rechts auf **Next**, um fortzufahren.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        Auf dem folgenden Bildschirm können Sie die Zugangsdaten eingeben, wenn Sie sich mit einer geschützten Netzwerkfreigabe verbinden. Tippen Sie auf **Registered User** und füllen Sie **Name** und **Password** mit Ihrem Samba-Benutzernamen und -Passwort aus. Alternativ können Sie auf **Guest** tippen, wenn Sie **Anonymous Access** aktiviert haben.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Tippen Sie oben rechts auf **Next**, um die Verbindung abzuschließen. Ihr iOS-Gerät sollte sich erfolgreich mit dem Server verbinden und eine Liste der verfügbaren Freigaben anzeigen.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        Die Samba-Freigabe wird unten im Menü unter der Überschrift **Shared** aufgeführt.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Anleitung zum Verbinden mit einem Samba-Server über die [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}-App.

        Tippen Sie unten rechts auf die Plus-Schaltfläche.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Tippen Sie auf **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Tippen Sie auf **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** ist der Name dieser Verbindung. **URL** ist der Zugriffslink. **Login** ist der Benutzername. Wenn anonymer Zugriff aktiviert ist, lassen Sie **Login** und **Password** einfach leer.

        Tippen Sie auf **Done**, um die Einrichtung abzuschließen.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV-Client

=== "Windows"

    Es gibt viele Programme mit WebDAV-Unterstützung, zum Beispiel [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"} und [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    Hier ist ein Beispiel mit RaiDrive.

    Klicken Sie auf **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    Klicken Sie im Bereich **Storage** auf **NAS** -> **WebDAV**.

    Aktivieren oder deaktivieren Sie im Bereich **Address** das Kontrollkästchen neben Address, um zwischen HTTPS und HTTP umzuschalten, und geben Sie anschließend die Adresse ein.

    Geben Sie im Bereich **Account** Benutzername und Passwort ein oder aktivieren Sie **Anonymous**.

    Klicken Sie abschließend auf **Connect**. Danach wird im Datei-Explorer ein Laufwerk X hinzugefügt.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    Es gibt viele Apps mit WebDAV-Unterstützung, zum Beispiel [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} und [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Hier ist ein Beispiel mit FE File Explorer.

    Klicken Sie auf die Schaltfläche **Add**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Wählen Sie **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Geben Sie die Verbindungseinstellungen ein. Wenn anonymer Zugriff aktiviert ist, lassen Sie **User Name** und **Password** einfach leer. Klicken Sie dann auf **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Möglicherweise erscheint eine Warnung wie *The following secure server (null) uses an untrusted certificate. Trust this server?*. Das liegt daran, dass ein selbstsigniertes Zertifikat verwendet wird. Bitte vertrauen Sie diesem Zertifikat.

=== "Android"

    Es gibt viele Android-Apps mit WebDAV-Unterstützung. Hier ist ein Beispiel mit [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Hinweis: Cx File Explorer unterstützt keinen anonymen Zugriff.

    Tippen Sie auf der Startseite auf **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Tippen Sie auf **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Tippen Sie auf **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Geben Sie **Host**, **Port**, **Username** und **Password** ein.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Es gibt viele iOS-Apps mit WebDAV-Unterstützung. Hier ist ein Beispiel mit [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Tippen Sie unten rechts auf die Plus-Schaltfläche.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Tippen Sie auf **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Tippen Sie auf **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** ist der Name dieser Verbindung. **URL** ist der Zugriffslink. **Login** ist der Benutzername.

    Tippen Sie auf **Done**, um die Einrichtung abzuschließen.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Mobile App verwenden

Im webbasierten Admin Panel können Sie nur freigegebene Ordner verwalten. Um Dateien auf Ihrem Speichergerät zu verwalten, verwenden Sie bitte die [mobile app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

- Beim Zugriff über das **lokale Netzwerk** werden Ihr Speichergerät und dessen Kapazität angezeigt, und Lese-/Schreibzugriff wird unterstützt.

- Beim Zugriff über die **Cloud** werden Ihr Speichergerät und dessen Kapazität angezeigt, jedoch wird kein Lese-/Schreibzugriff unterstützt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
