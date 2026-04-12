# Magazyn sieciowy

## Spis treści

- [Wprowadzenie](#introduction)
- [Obsługiwane modele](#supported-models)
- [Podłączanie urządzenia pamięci masowej](#insert-storage-device)
- [Konfiguracja Samba](#set-up-samba)
- [Konfiguracja WebDAV](#set-up-webdav)
- [Konfiguracja DLNA](#set-up-dlna)
- [Klient Samba](#samba-client)
- [Klient WebDAV](#webdav-client)

## Wprowadzenie

Magazyn sieciowy umożliwia bezprzewodowe udostępnianie plików między urządzeniami poprzez podłączenie dysku USB lub karty SD do routera. Router przekształca urządzenie pamięci masowej w udostępniony dysk sieciowy, dostępny dla wszystkich urządzeń połączonych przez Wi-Fi.

Niektóre modele GL.iNet mają gniazda kart MicroSD(TF), inne zaś porty USB obsługujące pamięci USB i przenośne dyski zewnętrzne. Możesz skonfigurować Samba, WebDAV i DLNA dla tych urządzeń pamięci masowej, które obsługują popularne formaty, takie jak NTFS, FAT32 i EXT4.

!!! Note 

    1. Pobór energii przez dysk twardy USB jest dość duży. Używaj go z zewnętrznym zasilaczem, w przeciwnym razie może to spowodować nieprawidłowe działanie.

    2. Niektóre modele mają port USB lub gniazdo MicroSD, ale ograniczoną przestrzeń pamięci masowej i nie obsługują magazynu sieciowego.

    3. Panel administratora umożliwia tylko zarządzanie folderami udostępnionymi. Do zarządzania plikami na urządzeniu pamięci masowej użyj [aplikacji mobilnej](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Obsługiwane modele

Zazwyczaj modele z portami USB lub gniazdami MicroSD(TF) obsługują magazyn sieciowy (tj. udostępnianie plików).

W przypadku urządzeń z pamięcią flash o pojemności 32 MB lub mniejszej funkcja magazynu sieciowego nie jest jeszcze obsługiwana.

| Model routera                          | Samba | Webdav | DLNA | Port USB | Karta MicroSD |
| :------------------------------------- | :---: | :---: | :---: | :------: | :----------: |
| GL-E5800 (Mudi 7)                      | √     | √     | √     | √        | -            |
| GL-MT5000 (Brume 3)                    | √     | √     | √     | √        | -            |
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
| GL-SFT1200 (Opal)</br>***FW 4.7.2**    | √     | -     | -     | √        | -            |
| GL-E750V2 (Mudi V2)</br>***FW 4.7.2**  | √     | -     | -     | √        | √            |
| GL-AR750S-EXT (Slate)</br>***FW 4.7.2**| √     | -     | -     | √        | √            |

## Podłączanie urządzenia pamięci masowej {#insert-storage-device}

W przypadku karty TF najpierw wyłącz router, włóż kartę TF, a następnie uruchom router ponownie.

W przypadku pamięci USB możesz ją bezpośrednio podłączyć do portu USB. W przypadku przenośnego dysku zewnętrznego, jeśli masz oddzielny zasilacz, podłącz go do zasilacza.

Zaloguj się do panelu administratora routera i przejdź do **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Podłącz urządzenie pamięci masowej. Po jego wykryciu strona wyświetli się jak poniżej.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Konfiguracja Samba {#set-up-samba}

1. Włącz przełącznik **Enable Samba** i kliknij **Apply**.

    * Allow Access Samba from WAN: Włącz, jeśli chcesz, aby urządzenia nadrzędne miały dostęp do Samba.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Kliknij **Quick Setup Share**, aby ustawić łącze udostępniania.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Dodaj użytkownika i kliknij **Next**. Ten krok zostanie pominięty, jeśli masz już konto.

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Kliknij ikonę trójkąta, aby wyświetlić wszystkie foldery. Wybierz folder do udostępnienia lub kliknij nazwę dysku (disk1_part1), jeśli chcesz udostępnić cały dysk. Następnie kliknij **Next**.

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Skonfiguruj folder udostępniony.

    Ze względów bezpieczeństwa nie zaleca się włączania opcji **Anonymous Access**.

    Użytkownik utworzony w poprzednim kroku zostanie domyślnie dodany do grupy **Read-Only User**. Jeśli chcesz, aby ten użytkownik mógł zapisywać lub usuwać pliki, usuń go z grupy Read-Only User i dodaj do grupy **Writable User**, a następnie kliknij **Apply**.

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Uzyskaj łącze dostępu do folderu.

    Na stronie zostanie wyświetlone łącze dla systemów Windows i Unix-like. Systemy Unix-like obejmują Android, iOS, macOS, Ubuntu itp.
    
    Teraz możesz uzyskać dostęp do udostępnionego folderu za pośrednictwem usługi Samba za pomocą tych łączy. Kliknij [tutaj](#samba-client), aby uzyskać szczegóły.

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Uwaga:** Jeśli włączysz opcję **Allow Access Samba from WAN** i uzyskasz dostęp do folderu udostępnionego z sieci nadrzędnej, zastąp adres IP routera (domyślnie 192.168.8.1) w łączu dostępu adresem IP WAN routera, który znajdziesz na stronie INTERNET w panelu administratora.

---

## Konfiguracja WebDAV {#set-up-webdav}

1. Włącz przełącznik **Enable WebDAV** i kliknij **Apply**.

    * Allow Access WebDAV from WAN: Włącz, jeśli chcesz, aby urządzenia nadrzędne miały dostęp do WebDAV.

    * WebDAV Protocol: **HTTP** jest nieszyfrowany; używaj go na własne ryzyko. **HTTPS** jest szyfrowany i używa certyfikatu z podpisem własnym.

    * WebDAV Port: Nie ma potrzeby modyfikowania numeru portu, chyba że wystąpi konflikt. Zalecany zakres numerów portów to 1024–65535.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Kliknij **Quick Setup Share**, aby ustawić łącze udostępniania.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Dodaj użytkownika i kliknij **Next**. Ten krok zostanie pominięty, jeśli masz już konto.

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Kliknij ikonę trójkąta, aby wyświetlić wszystkie foldery. Wybierz folder do udostępnienia lub kliknij nazwę dysku (disk1_part1), aby udostępnić cały dysk. Następnie kliknij **Next**.

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Skonfiguruj folder udostępniony.

    Ze względów bezpieczeństwa nie zaleca się włączania opcji **Anonymous Access**.

    Użytkownik utworzony w poprzednim kroku zostanie domyślnie dodany do grupy **Read-Only User**. Jeśli chcesz, aby ten użytkownik mógł zapisywać lub usuwać pliki, usuń go z grupy Read-Only User i dodaj do grupy **Writable User**, a następnie kliknij **Apply**.

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Uzyskaj łącze dostępu do folderu.

    Na stronie zostanie wyświetlone łącze dla systemów Windows i Unix-like. Systemy Unix-like obejmują Android, iOS, macOS, Ubuntu itp.
    
    Teraz możesz uzyskać dostęp do udostępnionego folderu za pośrednictwem usługi WebDAV za pomocą tych łączy. Kliknij [tutaj](#webdav-client), aby uzyskać szczegóły.

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Uwaga:** Jeśli włączysz opcję **Allow Access WebDAV from WAN** i uzyskasz dostęp do folderu udostępnionego z sieci nadrzędnej, zastąp adres IP routera (domyślnie 192.168.8.1) w łączu dostępu adresem IP WAN routera, który znajdziesz na stronie INTERNET w panelu administratora.

---

## Konfiguracja DLNA {#set-up-dlna}

Włącz przełącznik **Enable DLNA** i kliknij **Apply**.

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Podłącz telewizor Smart TV do routera – wykryje on serwer DLNA.

---

## Klient Samba

=== "Windows"

    Poniżej przedstawiono przykład dla systemu Windows 11, który ma również zastosowanie do systemu Windows 10.

    Otwórz Eksplorator plików i kliknij prawym przyciskiem myszy **Ten komputer** (w lewym panelu). Z wyświetlonego menu kontekstowego wybierz **Pokaż więcej opcji** -> **Dodaj lokalizację sieciową**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Kliknij **Wybierz niestandardową lokalizację sieciową**, a następnie kliknij **Dalej**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Wprowadź łącze dostępu do Samba. Następnie kliknij **Dalej**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Nadaj nazwę tej lokalizacji. Kliknij **Dalej**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Kliknij **Zakończ**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Jeśli wymagana jest nazwa użytkownika i hasło, zostaniesz poproszony o ich podanie. Następnie kliknij **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Dostęp do Samba możliwy jest przez Findera.

    Otwórz Findera i kliknij Idź -> Połącz z serwerem w menu. Skopiuj i wklej łącze dostępu do Samba.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    System poprosi o podanie nazwy użytkownika i hasła; nazwa użytkownika pochodzi z ustawień **Shared Folder Settings**.
    
    Jeśli skonfigurowałeś dostęp anonimowy, wybierz opcję **Guest** na poniższym zrzucie ekranu.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Kliknij **Continue** – Samba pojawi się na pasku bocznym Findera.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Istnieje wiele aplikacji Android obsługujących Samba; poniżej przedstawiono przykład z użyciem [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Na stronie głównej kliknij **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Kliknij **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Kliknij **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Wprowadź **Host**, **Username**, **Password**. W przypadku **Anonymous Access** zaznacz opcję **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    Aplikacja iOS [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} obsługuje Samba; możesz też użyć innych aplikacji, np. [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    W następnej sekcji opisano, jak połączyć się z Samba za pomocą aplikacji **Files** i **Documents**.

    - Przewodnik połączenia z serwerem Samba za pomocą aplikacji [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}.

        Otwórz aplikację **Files**. Jest ona zainstalowana domyślnie, więc powinna być widoczna na ekranie głównym. Ponieważ Files jest teraz aplikacją usuwalną, może być konieczne jej ponowne zainstalowanie z App Store, jeśli nie jest widoczna.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Upewnij się, że jesteś na karcie **Browse** na dole ekranu. Stuknij ikonę „…" (trzy kropki) w prawym górnym rogu, aby wyświetlić menu kontekstowe aplikacji.
        
        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Stuknij opcję **Connect to Server** przy górze menu. Na następnym ekranie wprowadź adres URL połączenia z serwerem. Adres URL znajdziesz w sekcji [Shared Link](#shared-link). Stuknij przycisk **Next** w prawym górnym rogu, aby kontynuować.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        Na następnym ekranie możesz wprowadzić dane uwierzytelniające, jeśli łączysz się z chronionym udziałem sieciowym. Stuknij **Registered User** i wypełnij pola **Name** i **Password** nazwą użytkownika i hasłem Samba. Możesz stuknąć „Guest", jeśli włączyłeś opcję **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Naciśnij przycisk **Next** w prawym górnym rogu, aby zakończyć połączenie. Urządzenie iOS powinno pomyślnie połączyć się z serwerem i wyświetlić listę dostępnych udziałów.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        Udział Samba zostanie wyświetlony na dole menu, pod nagłówkiem **Shared**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Przewodnik połączenia z serwerem Samba za pomocą aplikacji [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

        Kliknij przycisk plus w prawym dolnym rogu.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Kliknij **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Kliknij **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        Pole **Title** służy jako nazwa tego połączenia. **URL** to łącze dostępu. **Login** to nazwa użytkownika. W przypadku dostępu anonimowego pozostaw pola **Login** i **Password** puste.

        Kliknij **Done**, aby zakończyć konfigurację.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## Klient WebDAV

=== "Windows"

    Istnieje wiele programów obsługujących WebDAV, np. [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.
    
    Poniżej przedstawiono przykład z użyciem RaiDrive.

    Kliknij **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    W obszarze **Storage** kliknij **NAS** -> **WebDAV**.

    W obszarze **Address** zaznacz lub odznacz pole wyboru przy Address, aby przełączyć się między https/http, i wprowadź adres.

    W obszarze **Account** wprowadź nazwę użytkownika i hasło lub zaznacz opcję **Anonymous**.

    Na koniec kliknij **Connect** – w Eksploratorze plików pojawi się dysk X.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    Istnieje wiele aplikacji obsługujących WebDAV, np. [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Poniżej przedstawiono przykład z użyciem FE File Explorer.

    Kliknij przycisk Add.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Wybierz **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Wprowadź ustawienia połączenia. W przypadku dostępu anonimowego pozostaw pola **User Name** i **Password** puste. Następnie kliknij **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Może pojawić się ostrzeżenie: *The following secure server (null) uses an untrusted certificate. Trust this server?* – wynika to z używania certyfikatu z podpisem własnym; zaakceptuj go.

=== "Android"

    Istnieje wiele aplikacji Android obsługujących WebDAV; poniżej przedstawiono przykład z użyciem [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Uwaga: Cx File Explorer nie obsługuje dostępu anonimowego.

    Na stronie głównej kliknij **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Kliknij **New Location**.
    
    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Kliknij **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Wprowadź **Host**, **Port**, **Username**, **Password**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Istnieje wiele aplikacji iOS obsługujących WebDAV; poniżej przedstawiono przykład z użyciem [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Kliknij przycisk plus w prawym dolnym rogu.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Kliknij **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Kliknij **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    Pole **Title** służy jako nazwa tego połączenia. **URL** to łącze dostępu. **Login** to nazwa użytkownika.

    Kliknij **Done**, aby zakończyć konfigurację.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Korzystanie z aplikacji mobilnej

Panel administratora umożliwia tylko zarządzanie folderami udostępnionymi. Do zarządzania plikami na urządzeniu pamięci masowej użyj [aplikacji mobilnej](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

- Podczas dostępu za pośrednictwem **sieci lokalnej** aplikacja wyświetla urządzenie pamięci masowej wraz z jego pojemnością i obsługuje odczyt/zapis.

- Podczas dostępu za pośrednictwem **chmury** aplikacja wyświetla urządzenie pamięci masowej wraz z jego pojemnością, ale nie obsługuje odczytu/zapisu.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.