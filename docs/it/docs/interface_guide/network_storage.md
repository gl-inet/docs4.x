# Network Storage

## Indice

- [Introduzione](#introduction)
- [Modelli supportati](#supported-models)
- [Inserire il dispositivo di archiviazione](#insert-storage-device)
- [Configurare Samba](#set-up-samba)
- [Configurare WebDAV](#set-up-webdav)
- [Configurare DLNA](#set-up-dlna)
- [Client Samba](#samba-client)
- [Client WebDAV](#webdav-client)

## Introduction

Network storage consente la condivisione wireless dei file tra dispositivi collegando un'unita' USB o una scheda SD al router. Il router converte il dispositivo di archiviazione in un'unita' di rete condivisa, accessibile a tutti i dispositivi connessi al Wi-Fi.

Alcuni modelli GL.iNet dispongono di slot per schede MicroSD(TF), mentre altri dispongono di porte USB e supportano chiavette USB e hard disk esterni portatili. Puoi configurare Samba, WebDAV e DLNA per questi dispositivi di archiviazione, che supportano formati comuni come NTFS, FAT32 ed EXT4.

!!! Note

    1. Il consumo energetico di un hard disk USB e' piuttosto elevato. Usalo con un'alimentazione esterna, altrimenti potrebbe causare malfunzionamenti.

    2. Alcuni modelli hanno una porta USB o uno slot MicroSD ma dispongono di uno spazio di archiviazione limitato e non supportano Network Storage.

    3. Il pannello di amministrazione web consente solo di gestire le cartelle condivise. Per gestire i file sul dispositivo di archiviazione, usa la [mobile app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Supported Models

Di solito, i modelli con porte USB o slot MicroSD(TF) supportano Network Storage, cioe' la condivisione dei file.

Per i dispositivi con memoria flash di 32 MB o inferiore, la funzione Network Storage non e' ancora supportata.

| Router Model                           | Samba | Webdav | DLNA | USB Port | MicroSD Card |
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

## Insert Storage Device

Per una scheda TF, devi prima spegnere il router, inserire la scheda TF e poi riaccendere il router.

Per un'unita' USB, puoi inserirla direttamente nella porta USB. Per un hard disk esterno portatile, se disponi di un'alimentazione separata, collegalo all'alimentazione.

Accedi al pannello di amministrazione web del router e vai su **APPLICATIONS** -> **Network Storage**.

![network storage](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Collega il dispositivo di archiviazione. Quando viene rilevato, la pagina verra' visualizzata come mostrato di seguito.

![network storage, disk found](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Set Up Samba {#set-up-samba}

1. Attiva **Enable Samba** e fai clic su **Apply**.

    * Allow Access Samba from WAN: abilitalo se vuoi che i dispositivi a monte possano accedere a Samba.

    ![enable samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Fai clic su **Quick Setup Share** per impostare il link di condivisione.

    ![samba quick setup share](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Aggiungi un utente e fai clic su **Next**. Questo passaggio verra' saltato se hai gia' un account.

    ![samba quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Fai clic sull'icona a triangolo per mostrare tutte le cartelle. Seleziona una cartella da condividere oppure fai clic sul nome del disco (`disk1_part1`) se vuoi condividere l'intero disco. Poi fai clic su **Next**.

    ![samba quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configura la cartella condivisa.

    Per motivi di sicurezza, non e' consigliato abilitare **Anonymous Access**.

    L'utente creato nel passaggio precedente verra' aggiunto per impostazione predefinita a **Read-Only User**. Se vuoi che questo utente possa scrivere o eliminare file, rimuovilo da Read-Only User e aggiungilo a **Writable User**, quindi fai clic su **Apply**.

    ![samba quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Ottieni il link di accesso alla cartella.

    La pagina mostrera' il link per Windows e per sistemi operativi di tipo Unix. I sistemi di tipo Unix includono Android, iOS, macOS, Ubuntu, ecc.

    Ora puoi accedere alla cartella condivisa tramite il servizio Samba usando questi link. Fai clic [qui](#samba-client) per i dettagli.

    ![samba quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Nota:** se abiliti **Allow Access Samba from WAN** e accedi alla cartella condivisa dalla rete superiore, sostituisci l'IP del router (predefinito 192.168.8.1) nel link di accesso con l'IP WAN del router, che puoi trovare nella pagina INTERNET del pannello di amministrazione web.

---

## Set Up WebDAV {#set-up-webdav}

1. Attiva **Enable WebDAV** e fai clic su **Apply**.

    * Allow Access WebDAV from WAN: abilitalo se vuoi che i dispositivi a monte possano accedere a WebDAV.

    * WebDAV Protocol: **HTTP** non e' crittografato; usalo a tuo rischio. **HTTPS** e' crittografato e usa un certificato autofirmato.

    * WebDAV Port: non e' necessario modificare il numero di porta a meno che non ci sia un conflitto. L'intervallo di porte consigliato e' 1024 - 65535.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Fai clic su **Quick Setup Share** per impostare il link di condivisione.

    ![enable webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Aggiungi un utente e fai clic su **Next**. Questo passaggio verra' saltato se hai gia' un account.

    ![webdav quick setup share, add a user](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Fai clic sull'icona a triangolo per mostrare tutte le cartelle. Seleziona una cartella da condividere oppure fai clic sul nome del disco (`disk1_part1`) per condividere l'intero disco. Poi fai clic su **Next**.

    ![webdav quick setup share, add shared folder](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configura la cartella condivisa.

    Per motivi di sicurezza, non e' consigliato abilitare **Anonymous Access**.

    L'utente creato nel passaggio precedente verra' aggiunto per impostazione predefinita a **Read-Only User**. Se vuoi che questo utente possa scrivere o eliminare file, rimuovilo da Read-Only User e aggiungilo a **Writable User**, quindi fai clic su **Apply**.

    ![webdav quick setup share, shared folder settings](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Ottieni il link di accesso alla cartella.

    La pagina mostrera' il link per Windows e per sistemi operativi di tipo Unix. I sistemi di tipo Unix includono Android, iOS, macOS, Ubuntu, ecc.

    Ora puoi accedere alla cartella condivisa tramite il servizio WebDAV usando questi link. Fai clic [qui](#webdav-client) per i dettagli.

    ![webdav quick setup share, folder access link](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

    **Nota:** se hai abilitato **Allow Access WebDAV from WAN** e accedi alla cartella condivisa dalla rete superiore, sostituisci l'IP del router (predefinito 192.168.8.1) nel link di accesso con l'IP WAN del router, che puoi trovare nella pagina INTERNET del pannello di amministrazione web.

---

## Set Up DLNA {#set-up-dlna}

Attiva **Enable DLNA** e fai clic su **Apply**.

![network storage, enable dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Collega la tua smart TV al router e trovera' il server DLNA.

---

## Samba Client

=== "Windows"

    Ecco un esempio con Windows 11, valido anche per Windows 10.

    Apri Esplora file, quindi fai clic con il pulsante destro su **This PC** (nel pannello sinistro). Dal menu contestuale risultante, seleziona **Show more options** -> **Add a network location**

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Fai clic su **Choose a custom network location** e poi su **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Inserisci il link di accesso Samba. Poi fai clic su **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Assegna un nome a questa posizione. Fai clic su **Next**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Fai clic su **Finish**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Se sono necessari nome utente e password, ti verra' chiesto di inserire le credenziali. Poi fai clic su **OK**.

    ![windows 11 add network location](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Puoi accedere a Samba tramite Finder.

    Apri Finder e fai clic su Go -> Connect to Server nel menu. Copia e incolla il link di accesso Samba.

    ![network storage, mac os finder connect to server](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Ti verra' chiesto il nome utente e la password; il nome utente e' quello impostato quando hai configurato **Shared Folder Settings**.

    Se hai configurato l'accesso anonimo, scegli **Guest** nell'immagine qui sotto.

    ![network storage, mac os finder connect to server username password](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Fai clic su **Continue** e Samba verra' mostrato nella barra laterale del Finder.

    ![network storage, mac os finder samba connected](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Esistono molte app Android che supportano Samba; ecco un esempio con [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Nella home page, fai clic su **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Fai clic su **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Fai clic su **SMB**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Inserisci **Host**, **Username** e **Password**. Se si tratta di **Anonymous Access**, seleziona **Anonymous**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    L'app iOS [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} supporta Samba, oppure puoi usare altre app, ad esempio [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    La sezione seguente descrive come collegarsi a Samba usando rispettivamente l'app **Files** e l'app **Documents**.

    - Guida alla connessione a un server Samba tramite l'app [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}.

        Apri l'app **Files**. E' installata per impostazione predefinita, quindi dovresti trovarla nella schermata Home. Poiche' **Files** ora e' un'app rimovibile, potresti doverla reinstallare dall'App Store se non compare.

        ![search files on iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Assicurati di essere nella scheda **Browse** nella parte inferiore dello schermo. Tocca l'icona "..." (tre puntini) in alto a destra per mostrare il menu contestuale dell'app.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Tocca l'opzione **Connect to Server** nella parte superiore del menu. Nella schermata successiva, inserisci l'URL di connessione del server. Puoi trovare l'URL in [Shared Link](#shared-link). Tocca il pulsante **Next** in alto a destra per continuare.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        La schermata successiva consente di inserire le credenziali di autenticazione se ti collegherai a una condivisione di rete protetta. Tocca **Registered User** e compila i campi **Name** e **Password** con il nome utente e la password Samba. Puoi anche toccare "Guest" se abiliti **Anonymous Access**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Premi il pulsante **Next** in alto a destra per completare la connessione. Il tuo dispositivo iOS dovrebbe collegarsi correttamente al server e mostrare un elenco delle condivisioni disponibili.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        La condivisione Samba verra' elencata nella parte inferiore del menu, sotto l'intestazione **Shared**.

        ![ios files set up SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Guida alla connessione a un server Samba tramite l'app [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

        Fai clic sul pulsante piu' nell'angolo inferiore destro.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Fai clic su **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Fai clic su **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** e' il nome di questa connessione. **URL** e' il link di accesso. **Login** e' il nome utente. Se si tratta di accesso anonimo, lascia semplicemente vuoti **Login** e **Password**.

        Fai clic sul pulsante **Done** per completare la configurazione.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## WebDAV Client

=== "Windows"

    Esistono molti software che supportano WebDAV, ad esempio [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}, [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    Ecco un esempio con RaiDrive.

    Fai clic su **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    Nell'area **Storage**, fai clic su **NAS** -> **WebDAV**.

    Nell'area **Address**, seleziona o deseleziona la casella vicino ad Address per passare tra https/http, quindi inserisci l'indirizzo.

    Nell'area **Account**, inserisci nome utente e password oppure seleziona **Anonymous**.

    Infine, fai clic su **Connect**: verra' aggiunta un'unita' X in Esplora file.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    Esistono molte app che supportano WebDAV, ad esempio [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Ecco un esempio con FE File Explorer.

    Fai clic sul pulsante Add.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Seleziona **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Inserisci le impostazioni di connessione. Se si tratta di accesso anonimo, lascia semplicemente vuoti **User Name** e **Password**. Poi fai clic su **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Potrebbe comparire un avviso come *The following secure server (null) uses an untrusted certificate. Trust this server?*, perche' viene usato un certificato autofirmato; in questo caso, consideralo attendibile.

=== "Android"

    Esistono molte app iOS che supportano WebDAV; ecco un esempio con [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Nota: Cx File Explorer non supporta l'accesso anonimo.

    Nella home page, fai clic su **NETWORK**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Fai clic su **New Location**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Fai clic su **WebDAV**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Inserisci **Host**, **Port**, **Username** e **Password**.

    ![cx file explorer home page](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Esistono molte app iOS che supportano WebDAV; ecco un esempio con [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Fai clic sul pulsante piu' nell'angolo inferiore destro.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Fai clic su **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Fai clic su **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** e' il nome di questa connessione. **URL** e' il link di accesso. **Login** e' il nome utente.

    Fai clic sul pulsante **Done** per completare la configurazione.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Using Mobile App

Il pannello di amministrazione web consente solo di gestire le cartelle condivise. Per gestire i file sul dispositivo di archiviazione, usa la [mobile app](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

- Quando accedi all'app tramite la **rete locale**, vengono mostrati il dispositivo di archiviazione e la sua capacita', ed e' supportato l'accesso in lettura/scrittura.

- Quando accedi all'app tramite il **cloud**, vengono mostrati il dispositivo di archiviazione e la sua capacita', ma l'accesso in lettura/scrittura non e' supportato.

---

Hai ancora domande? Visita il nostro [Community Forum](https://forum.gl-inet.com){target="_blank"} o [contattaci](https://www.gl-inet.com/contacts/){target="_blank"}.
