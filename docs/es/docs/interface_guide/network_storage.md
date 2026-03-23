# Almacenamiento en red

## Contenido

- [Introducción](#introducción)
- [Modelos compatibles](#modelos-compatibles)
- [Insertar dispositivo de almacenamiento](#insertar-dispositivo-de-almacenamiento)
- [Configurar Samba](#configurar-samba)
- [Configurar WebDAV](#configurar-webdav)
- [Configurar DLNA](#configurar-dlna)
- [Cliente Samba](#cliente-samba)
- [Cliente WebDAV](#cliente-webdav)

## Introducción

El almacenamiento en red permite compartir archivos de forma inalámbrica entre dispositivos conectando una unidad USB o una tarjeta SD al router. El router convierte el dispositivo de almacenamiento en una unidad de red compartida, accesible para todos los dispositivos conectados por Wi-Fi.

Algunos modelos de GL.iNet tienen ranuras para tarjetas MicroSD (TF), mientras que otros tienen puertos USB y admiten unidades flash USB y discos duros externos portátiles. Puede configurar Samba, WebDAV y DLNA para estos dispositivos de almacenamiento, que admiten formatos comunes como NTFS, FAT32 y EXT4.

!!! note

    1. El consumo de energía de un disco duro USB es bastante alto. Úselo con una fuente de alimentación externa; de lo contrario, puede provocar un mal funcionamiento.

    2. Algunos modelos tienen un puerto USB o una ranura MicroSD, pero disponen de poco espacio de almacenamiento y no admiten almacenamiento en red.

    3. El panel de administración web solo le permite administrar carpetas compartidas. Para administrar archivos en el dispositivo de almacenamiento, utilice la [aplicación móvil](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Modelos compatibles

Normalmente, los modelos con puertos USB o ranuras MicroSD (TF) admiten almacenamiento en red, es decir, uso compartido de archivos.

En los dispositivos con almacenamiento flash de 32 MB o menos, la función Network Storage aún no es compatible.

| Modelo de router                         | Samba | WebDAV | DLNA | Puerto USB | Tarjeta MicroSD |
| :--------------------------------------- | :---: | :----: | :--: | :--------: | :-------------: |
| GL-E5800 (Mudi 7)                        |   √   |   √    |  √   |     √      |        -        |
| GL-MT5000 (Brume 3)                      |   √   |   √    |  √   |     √      |        -        |
| GL-BE3600 (Slate 7)                      |   √   |   √    |  √   |     √      |        -        |
| GL-X2000 (Spitz Plus)                    |   √   |   √    |  √   |     √      |        -        |
| GL-MT6000 (Flint 2)                      |   √   |   √    |  √   |     √      |        -        |
| GL-XE3000 (Puli AX)                      |   √   |   √    |  √   |     √      |        √        |
| GL-X3000 (Spitz AX)                      |   √   |   √    |  √   |     √      |        √        |
| GL-MT3000 (Beryl AX)                     |   √   |   √    |  √   |     √      |        -        |
| GL-MT2500/GL-MT2500A (Brume 2)           |   √   |   √    |  √   |     √      |        -        |
| GL-AXT1800 (Slate AX)                    |   √   |   √    |  √   |     √      |        √        |
| GL-AX1800 (Flint)                        |   √   |   √    |  √   |     √      |        -        |
| GL-A1300 (Slate Plus)                    |   √   |   √    |  √   |     √      |        -        |
| GL-S1300 (Convexa-S)                     |   √   |   √    |  √   |     √      |        -        |
| GL-SFT1200 (Opal)</br>**\*FW 4.7.2**     |   √   |   -    |  -   |     √      |        -        |
| GL-E750V2 (Mudi V2)</br>**\*FW 4.7.2**   |   √   |   -    |  -   |     √      |        √        |
| GL-AR750S-EXT (Slate)</br>**\*FW 4.7.2** |   √   |   -    |  -   |     √      |        √        |

## Insertar dispositivo de almacenamiento

En el caso de una tarjeta TF, primero debe apagar el router, insertar la tarjeta TF y, a continuación, volver a encender el router.

En el caso de una unidad USB, puede conectarla directamente al puerto USB. Si se trata de un disco duro externo portátil y dispone de una fuente de alimentación independiente, conéctelo a esa fuente de alimentación.

Inicie sesión en el panel de administración web del router y vaya a **APPLICATIONS** -> **Network Storage**.

![almacenamiento en red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/network_storage_init.png){class="glboxshadow"}

Conecte el dispositivo de almacenamiento. Cuando se detecte, la página se mostrará como se indica a continuación.

![almacenamiento en red, disco detectado](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/disk_found.png){class="glboxshadow"}

## Configurar Samba {#set-up-samba}

1. Active **Enable Samba** y haga clic en **Apply**.
   - Allow Access Samba from WAN: Habilítelo si desea que los dispositivos de la red ascendente puedan acceder a Samba.

   ![habilitar samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/enable_samba.png){class="glboxshadow"}

2. Haga clic en **Quick Setup Share** para configurar el enlace compartido.

   ![configuración rápida de recurso compartido de samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share.png){class="glboxshadow"}

3. Añada un usuario y haga clic en **Next**. Este paso se omitirá si ya tiene una cuenta.

   ![configuración rápida de recurso compartido de samba, añadir un usuario](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Haga clic en el icono del triángulo para mostrar todas las carpetas. Seleccione una carpeta para compartir o haga clic en el nombre del disco (disk1_part1) si desea compartir todo el disco. Después, haga clic en **Next**.

   ![configuración rápida de recurso compartido de samba, añadir carpeta compartida](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configure la carpeta compartida.

   Por razones de seguridad, no se recomienda habilitar **Anonymous Access**.

   El usuario creado en el paso anterior se añadirá de forma predeterminada a **Read-Only User**. Si desea que este usuario pueda escribir o eliminar archivos, quítelo de **Read-Only User**, añádalo a **Writable User** y haga clic en **Apply**.

   ![configuración rápida de recurso compartido de samba, ajustes de carpeta compartida](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Obtenga el enlace de acceso a la carpeta.

   La página mostrará el enlace para Windows y sistemas tipo Unix. Los sistemas tipo Unix incluyen Android, iOS, macOS, Ubuntu, etc.

   Ahora puede acceder a la carpeta compartida mediante el servicio Samba a través de estos enlaces. Haga clic [aquí](#cliente-samba) para ver los detalles.

   ![configuración rápida de recurso compartido de samba, enlace de acceso a carpeta](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_folder_access_link.png){class="glboxshadow"}

   **Nota:** Si habilita **Allow Access Samba from WAN** y accede a la carpeta compartida desde la red superior, sustituya la IP del router en el enlace de acceso (192.168.8.1 de forma predeterminada) por la IP WAN del router, que se puede encontrar en la página INTERNET del panel de administración web.

---

## Configurar WebDAV {#set-up-webdav}

1. Active **Enable WebDAV** y haga clic en **Apply**.
   - Allow Access WebDAV from WAN: Habilítelo si desea que los dispositivos de la red ascendente puedan acceder a WebDAV.

   - WebDAV Protocol: **HTTP** no está cifrado; úselo bajo su propia responsabilidad. **HTTPS** está cifrado y utiliza un certificado autofirmado.

   - WebDAV Port: No es necesario modificar el número de puerto salvo que haya un conflicto. El rango de puertos recomendado es 1024 - 65535.

   ![habilitar webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/enable_webdav.png){class="glboxshadow"}

2. Haga clic en **Quick Setup Share** para configurar el enlace compartido.

   ![habilitar webdav](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share.png){class="glboxshadow"}

3. Añada un usuario y haga clic en **Next**. Este paso se omitirá si ya tiene una cuenta.

   ![configuración rápida de recurso compartido de webdav, añadir un usuario](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_user.png){class="glboxshadow"}

4. Haga clic en el icono del triángulo para mostrar todas las carpetas. Seleccione una carpeta para compartir o haga clic en el nombre del disco (disk1_part1) para compartir todo el disco. Después, haga clic en **Next**.

   ![configuración rápida de recurso compartido de webdav, añadir carpeta compartida](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_quick_setup_share/samba_quick_setup_share_add_shared_folder.png){class="glboxshadow"}

5. Configure la carpeta compartida.

   Por razones de seguridad, no se recomienda habilitar **Anonymous Access**.

   El usuario creado en el paso anterior se añadirá de forma predeterminada a **Read-Only User**. Si desea que este usuario pueda escribir o eliminar archivos, quítelo de **Read-Only User**, añádalo a **Writable User** y haga clic en **Apply**.

   ![configuración rápida de recurso compartido de webdav, ajustes de carpeta compartida](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_shared_folder_settings.png){class="glboxshadow"}

6. Obtenga el enlace de acceso a la carpeta.

   La página mostrará el enlace para Windows y sistemas tipo Unix. Los sistemas tipo Unix incluyen Android, iOS, macOS, Ubuntu, etc.

   Ahora puede acceder a la carpeta compartida mediante el servicio WebDAV a través de estos enlaces. Haga clic [aquí](#cliente-webdav) para ver los detalles.

   ![configuración rápida de recurso compartido de webdav, enlace de acceso a carpeta](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_quick_setup_share/webdav_quick_setup_share_folder_access_link.png){class="glboxshadow"}

   **Nota:** Si habilitó **Allow Access WebDAV from WAN** y accede a la carpeta compartida desde la red superior, sustituya la IP del router en el enlace de acceso (192.168.8.1 de forma predeterminada) por la IP WAN del router, que se puede encontrar en la página INTERNET del panel de administración web.

---

## Configurar DLNA {#set-up-dlna}

Active **Enable DLNA** y haga clic en **Apply**.

![almacenamiento en red, habilitar dlna](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/enable_dlna.jpg){class="glboxshadow"}

Conecte el televisor inteligente al router y encontrará el servidor DLNA.

---

## Cliente Samba

=== "Windows"

    Aquí se muestra un ejemplo de Windows 11, que también se aplica a Windows 10.

    Abra el Explorador de archivos y haga clic con el botón derecho en **This PC** (en el panel izquierdo). En el menú contextual que aparece, seleccione **Show more options** -> **Add a network location**

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Haga clic en **Choose a custom network location** y después en **Next**.

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Introduzca el enlace de acceso de Samba. Después, haga clic en **Next**.

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Asigne un nombre a esta ubicación. Haga clic en **Next**.

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Haga clic en **Finish**.

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Si necesita nombre de usuario y contraseña, se le pedirá que introduzca las credenciales. Después, haga clic en **OK**.

    ![windows 11 agregar ubicación de red](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Puede acceder a Samba desde Finder.

    Abra Finder y haga clic en Go -> Connect to Server en el menú. Copie y pegue el enlace de acceso de Samba.

    ![almacenamiento en red, finder de macOS conectar al servidor](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Se le pedirá el nombre de usuario y la contraseña; el nombre de usuario es el que configuró en **Shared Folder Settings**.

    Si configuró acceso anónimo, elija **Guest** en la imagen siguiente.

    ![almacenamiento en red, finder de macOS conectar al servidor usuario contraseña](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Haga clic en **Continue** y Samba aparecerá en la barra lateral de Finder.

    ![almacenamiento en red, finder de macOS samba conectado](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Hay muchas aplicaciones de Android compatibles con Samba; aquí se muestra un ejemplo con [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    En la página de inicio, haga clic en **NETWORK**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Haga clic en **New Location**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Haga clic en **SMB**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Introduzca **Host**, **Username** y **Password**. Si se trata de **Anonymous Access**, marque **Anonymous**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    La app [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} de iOS admite Samba, o puede usar otras aplicaciones, por ejemplo [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    La siguiente sección describe cómo conectarse a Samba usando la app **Files** y la app **Documents**, respectivamente.

    - Guía para conectarse al servidor Samba con la app [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}.

        Abra la app **Files**. Viene instalada de forma predeterminada, por lo que debería encontrarla en la pantalla de inicio. Como **Files** ahora es una app extraíble, es posible que tenga que reinstalarla desde la App Store si no aparece.

        ![buscar files en iphone](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width=300"}

        Asegúrese de estar en la pestaña **Browse** en la parte inferior de la pantalla. Toque el icono "…" (tres puntos) de la parte superior derecha para mostrar el menú contextual de la aplicación.

        ![ios files configurar SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width=560"}

        Toque la opción **Connect to Server** cerca de la parte superior del menú. En la pantalla siguiente, introduzca la URL de conexión del servidor. Puede encontrar la URL en el [enlace compartido](#configurar-samba). Toque el botón **Next** en la parte superior derecha para continuar.

        ![ios files configurar SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width=560"}

        La siguiente pantalla le permite introducir las credenciales de autenticación si va a conectarse a un recurso de red protegido. Toque **Registered User** y rellene los campos **Name** y **Password** con su nombre de usuario y contraseña de Samba. Puede tocar "Guest" en su lugar si habilitó **Anonymous Access**.

        ![ios files configurar SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width=560"}

        Pulse el botón **Next** en la parte superior derecha para completar la conexión. El dispositivo iOS debería conectarse correctamente al servidor y mostrar una lista de los recursos compartidos disponibles.

        ![ios files configurar SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width=560"}

        El recurso compartido de Samba aparecerá en la parte inferior del menú, bajo el encabezado **Shared**.

        ![ios files configurar SMB](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width=560"}

    - Guía para conectarse al servidor Samba con la app [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

        Haga clic en el botón con el signo más en la esquina inferior derecha.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Haga clic en **Add Connection**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Haga clic en **Windows SMB**.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** sirve para asignar un nombre a esta conexión. **URL** es el enlace de acceso. **Login** es el nombre de usuario. Si se trata de acceso anónimo, deje **Login** y **Password** vacíos.

        Haga clic en el botón **Done** para completar esta configuración.

        ![documents samba](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## Cliente WebDAV

=== "Windows"

    Hay mucho software compatible con WebDAV, por ejemplo [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"} y [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    Aquí se muestra un ejemplo con RaiDrive.

    Haga clic en **Add**.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    En el área **Storage**, haga clic en **NAS** -> **WebDAV**.

    En el área **Address**, marque o desmarque la casilla situada junto a Address para cambiar entre https y http, e introduzca la dirección.

    En el área **Account**, introduzca el nombre de usuario y la contraseña, o marque **Anonymous**.

    Por último, haga clic en **Connect** y se añadirá una unidad X en el Explorador de archivos.

    ![RaiDrive WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    Hay muchas aplicaciones compatibles con WebDAV, por ejemplo [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} y [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    Aquí se muestra un ejemplo con FE File Explorer.

    Haga clic en el botón Add.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Seleccione **WebDAV**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Introduzca la configuración de conexión. Si se trata de acceso anónimo, deje **User Name** y **Password** vacíos. Después, haga clic en **Save & Connect**.

    ![FE File Explorer WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Puede aparecer una advertencia que diga *The following secure server (null) uses an untrusted certificate. Trust this server?*; esto ocurre porque usa un certificado autofirmado, así que confíe en él.

=== "Android"

    Hay muchas aplicaciones de iOS compatibles con WebDAV; aquí se muestra un ejemplo con [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Nota: Cx File Explorer no admite acceso anónimo.

    En la página de inicio, haga clic en **NETWORK**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Haga clic en **New Location**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Haga clic en **WebDAV**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Introduzca **Host**, **Port**, **Username** y **Password**.

    ![página principal de cx file explorer](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Hay muchas aplicaciones de iOS compatibles con WebDAV; aquí se muestra un ejemplo con [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Haga clic en el botón con el signo más en la esquina inferior derecha.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Haga clic en **Add Connection**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Haga clic en **WebDAV Server**.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** sirve para asignar un nombre a esta conexión. **URL** es el enlace de acceso. **Login** es el nombre de usuario.

    Haga clic en el botón **Done** para completar esta configuración.

    ![documents WebDAV](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Uso de la aplicación móvil

El panel de administración web solo le permite administrar carpetas compartidas. Para administrar archivos en el dispositivo de almacenamiento, utilice la [aplicación móvil](https://www.gl-inet.com/app/#download-app-glinet){target="\_blank"}.

- Cuando accede a la aplicación a través de la **red local**, se muestra el dispositivo de almacenamiento y su capacidad, y se admite acceso de lectura y escritura.

- Cuando accede a la aplicación a través de la **nube**, se muestra el dispositivo de almacenamiento y su capacidad, pero no se admite acceso de lectura y escritura.

---

¿Todavía tiene preguntas? Visite nuestro [Foro de la comunidad](https://forum.gl-inet.com){target="\_blank"} o [contáctenos](https://www.gl-inet.com/contacts/){target="\_blank"}.
