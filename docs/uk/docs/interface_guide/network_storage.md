# Мережеве сховище {#network-storage}

## Вступ {#introduction}

Мережеве сховище дає змогу бездротово обмінюватися файлами між пристроями, підключивши USB-накопичувач або SD-карту до маршрутизатора. Маршрутизатор перетворює накопичувач на спільний мережевий диск, доступний усім пристроям, підключеним через Wi-Fi.

Деякі моделі GL.iNet мають слоти для карт MicroSD(TF), інші — порти USB для флешнакопичувачів і портативних зовнішніх жорстких дисків. Для цих накопичувачів можна налаштувати Samba, WebDAV і DLNA. Підтримуються поширені формати, зокрема NTFS, FAT32 та EXT4.

!!! Note

    1. Жорсткий диск USB споживає багато енергії. Використовуйте зовнішнє джерело живлення, інакше можуть виникати збої.

    2. Деякі моделі мають порт USB або слот MicroSD, але через обмежений обсяг пам’яті не підтримують мережеве сховище.

    3. Вебпанель адміністрування дозволяє керувати лише спільними папками. Для керування файлами на накопичувачі використовуйте [мобільний застосунок](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

## Підтримувані моделі {#supported-models}

Зазвичай моделі з портами USB або слотами MicroSD(TF) підтримують мережеве сховище, тобто спільний доступ до файлів.

Пристрої з обсягом флешпам’яті 32MB або менше поки не підтримують мережеве сховище.

| Модель маршрутизатора | Samba | Webdav | DLNA | Порт USB | Карта MicroSD |
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

## Підключення накопичувача {#connect-storage-device}

Щоб вставити карту TF, спочатку вимкніть маршрутизатор, вставте карту й увімкніть маршрутизатор знову.

USB-накопичувач можна підключити безпосередньо до порту USB. Якщо портативний зовнішній жорсткий диск має окреме джерело живлення, підключіть його.

Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **APPLICATIONS** -> **Network Storage**.

![Мережеве сховище](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/network_storage_init.png){class="glboxshadow"}

Підключіть накопичувач. Коли його буде виявлено, сторінка матиме вигляд, показаний нижче.

![Накопичувач виявлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/disk_found.png){class="glboxshadow"}

## Налаштування Samba {#set-up-samba}

1. Увімкніть **Enable Samba** та натисніть **Apply**.

    ![Увімкнення Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba1.png){class="glboxshadow"}

    * Allow Access Samba from WAN: увімкніть, щоб пристрої мережі вищого рівня могли отримувати доступ до сервісу Samba.

2. Натисніть **Quick Setup Share**, щоб налаштувати посилання для спільного доступу.

    ![Швидке налаштування спільного доступу Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba2.png){class="glboxshadow"}

3. Додайте користувача та натисніть **Next**. Якщо обліковий запис уже є, цей крок буде пропущено.

    ![Додавання користувача Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba3.png){class="glboxshadow"}

4. Натисніть піктограму трикутника, щоб показати всі папки. Виберіть папку для спільного доступу та натисніть **Next**. Щоб надати доступ до всього диска, натисніть його назву, наприклад disk1_part1.

    ![Вибір спільної папки Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba4.png){class="glboxshadow"}

5. Налаштуйте спільну папку.

    Користувача, створеного на попередньому кроці, за замовчуванням буде додано до **Read-Only User**. Щоб дозволити йому записувати або видаляти файли, вилучіть його з Read-Only User, додайте до **Read-Write User** та натисніть **Apply**.

    З міркувань безпеки не рекомендовано вмикати **Anonymous Access**.

    ![Права доступу до спільної папки Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba5.png){class="glboxshadow"}

6. Отримайте посилання для доступу до папки.

    <span id="shared-link"></span>

    На сторінці відобразяться посилання для Windows і Unix-подібних ОС, зокрема Android, iOS, macOS, Ubuntu тощо.

    Відкрийте спільну папку через сервіс Samba за цими посиланнями. Докладні інструкції наведено [тут](#samba-client).

    ![Посилання для доступу до папки Samba](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba6.png){class="glboxshadow"}

    **Примітка:** якщо увімкнено **Allow Access Samba from WAN** і ви відкриваєте спільну папку з мережі вищого рівня, замініть у посиланні IP-адресу маршрутизатора (за замовчуванням 192.168.8.1) на його IP-адресу WAN. Її можна знайти на сторінці INTERNET у вебпанелі адміністрування.

---

## Налаштування WebDAV {#set-up-webdav}

1. Увімкніть **Enable WebDAV** і натисніть **Apply**.

    ![Увімкнення WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav1.png){class="glboxshadow"}

    * Allow Access WebDAV from WAN: увімкніть, щоб пристрої мережі вищого рівня могли отримувати доступ до сервісу WebDAV.

    * WebDAV Protocol: **HTTP** не використовує шифрування; користуйтеся ним на власний ризик. **HTTPS** використовує шифрування та самопідписаний сертифікат.

    * WebDAV Port: змінюйте номер порту лише за наявності конфлікту. Рекомендований діапазон портів — 1024 - 65535.

2. Натисніть **Quick Setup Share**, щоб налаштувати посилання для спільного доступу.

    ![Увімкнення WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav2.png){class="glboxshadow"}

3. Додайте користувача та натисніть **Next**. Якщо обліковий запис уже є, цей крок буде пропущено.

    ![Додавання користувача WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav3.png){class="glboxshadow"}

4. Натисніть піктограму трикутника, щоб показати всі папки. Виберіть папку для спільного доступу та натисніть **Next**. Щоб надати доступ до всього диска, натисніть його назву, наприклад disk1_part1.

    ![Вибір спільної папки WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav4.png){class="glboxshadow"}

5. Налаштуйте спільну папку.

    Користувача, створеного на попередньому кроці, за замовчуванням буде додано до **Read-Only User**. Щоб дозволити йому записувати або видаляти файли, вилучіть його з Read-Only User, додайте до **Read-Write User** та натисніть **Apply**.

    З міркувань безпеки не рекомендовано вмикати **Anonymous Access**.

    ![Права доступу до спільної папки WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav5.png){class="glboxshadow"}

6. Отримайте посилання для доступу до папки.

    На сторінці відобразяться посилання для Windows і Unix-подібних ОС, зокрема Android, iOS, macOS, Ubuntu тощо.

    Відкрийте спільну папку через сервіс WebDAV за цими посиланнями. Докладні інструкції наведено [тут](#webdav-client).

    ![Посилання для доступу до папки WebDAV](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav6.png){class="glboxshadow"}

    **Примітка:** якщо увімкнено **Allow Access WebDAV from WAN** і ви відкриваєте спільну папку з мережі вищого рівня, замініть у посиланні IP-адресу маршрутизатора (за замовчуванням 192.168.8.1) на його IP-адресу WAN. Її можна знайти на сторінці INTERNET у вебпанелі адміністрування.

---

## Налаштування DLNA {#set-up-dlna}

1. Увімкніть **Enable DLNA** і натисніть **Apply**.

    ![Увімкнення DLNA](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna1.png){class="glboxshadow"}

2. За потреби змініть Share Path праворуч.

    ![Шлях спільного ресурсу DLNA](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/dlna2.png){class="glboxshadow"}

3. Підключіть Smart TV до маршрутизатора. Телевізор автоматично знайде сервер DLNA.

---

## Клієнт Samba {#samba-client}

=== "Windows"

    У цьому прикладі використано Windows 11. Інструкція також підходить для Windows 10.

    Відкрийте Провідник і натисніть правою кнопкою миші **This PC** у лівій панелі. У контекстному меню виберіть **Show more options** -> **Add a network location**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location.png){class="glboxshadow"}

    Виберіть **Choose a custom network location** і натисніть **Next**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_2.png){class="glboxshadow"}

    Введіть посилання для доступу до Samba та натисніть **Next**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_3.png){class="glboxshadow"}

    Задайте назву цього розташування й натисніть **Next**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_4.png){class="glboxshadow"}

    Натисніть **Finish**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_5.png){class="glboxshadow"}

    Якщо потрібні ім’я користувача та пароль, система попросить ввести облікові дані. Введіть їх і натисніть **OK**.

    ![Додавання мережевого розташування у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/windows11_add_network_location_6.png){class="glboxshadow"}

=== "macOS"

    Доступ до Samba можна отримати через Finder.

    Відкрийте Finder і виберіть у меню Go -> Connect to Server. Скопіюйте та вставте посилання для доступу до Samba.

    ![Підключення до сервера у Finder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_connect_to_server.png){class="glboxshadow"}

    Система попросить ввести ім’я користувача та пароль. Використовуйте ім’я користувача, задане під час налаштування **Shared Folder Settings**.

    Якщо налаштовано анонімний доступ, виберіть **Guest**, як показано нижче.

    ![Облікові дані Samba у Finder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_username_password.png){class="glboxshadow"}

    Натисніть **Continue**. Спільний ресурс Samba з’явиться на бічній панелі Finder.

    ![Підключений ресурс Samba у Finder](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/finder_samba_connected.png){class="glboxshadow"}

=== "Android"

    Багато застосунків Android підтримують Samba. У цьому прикладі використано [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    На головній сторінці натисніть **NETWORK**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Натисніть **New Location**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Натисніть **SMB**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Введіть **Host**, **Username** і **Password**. Якщо увімкнено **Anonymous Access**, установіть прапорець **Anonymous**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_smb.png){class="glboxshadow" width="350"}

=== "iOS"

    Застосунок [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"} для iOS підтримує Samba. Також можна використовувати інші застосунки, наприклад [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Нижче описано підключення до Samba за допомогою застосунків **Files** і **Documents**.

    - Підключення до сервера Samba за допомогою застосунку [Files](https://apps.apple.com/us/app/files/id1232058109){target="_blank"}.

        Відкрийте застосунок **Files**. Він встановлений за замовчуванням і зазвичай доступний на головному екрані. Якщо його немає, можливо, його видалено; тоді встановіть його повторно з App Store.

        ![Пошук застосунку Files на iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios15-iphone-12-pro-home-screen-search-files.jpg){class="glboxshadow" width="300"}

        Відкрийте вкладку **Browse** внизу екрана. Натисніть піктограму «…» (три крапки) у верхньому правому куті, щоб відкрити контекстне меню застосунку.

        ![Налаштування SMB у застосунку Files для iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_1.png){class="glboxshadow" width="560"}

        Виберіть **Connect to Server** у верхній частині меню. На наступному екрані введіть URL для підключення до сервера. Його наведено в розділі [посилання для спільного доступу](#shared-link). Натисніть **Next** у верхньому правому куті, щоб продовжити.

        ![Налаштування SMB у застосунку Files для iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_2.png){class="glboxshadow" width="560"}

        На наступному екрані введіть облікові дані, якщо підключаєтеся до захищеного спільного ресурсу. Натисніть **Registered User** і заповніть поля **Name** та **Password** своїм ім’ям користувача й паролем Samba. Якщо увімкнено **Anonymous Access**, натомість виберіть «Guest».

        ![Налаштування SMB у застосунку Files для iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_3.png){class="glboxshadow" width="560"}

        Натисніть **Next** у верхньому правому куті, щоб завершити підключення. Пристрій iOS має підключитися до сервера та показати список доступних спільних ресурсів.

        ![Налаштування SMB у застосунку Files для iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_4.png){class="glboxshadow" width="560"}

        Спільний ресурс Samba з’явиться внизу меню під заголовком **Shared**.

        ![Налаштування SMB у застосунку Files для iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/ios_files_smb_5.png){class="glboxshadow" width="560"}

    - Підключення до сервера Samba за допомогою застосунку [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

        Натисніть кнопку з плюсом у нижньому правому куті.

        ![Налаштування Samba у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

        Натисніть **Add Connection**.

        ![Налаштування Samba у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

        Натисніть **Windows SMB**.

        ![Налаштування Samba у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

        **Title** — назва з’єднання, **URL** — посилання для доступу, **Login** — ім’я користувача. Для анонімного доступу залиште **Login** і **Password** порожніми.

        Натисніть **Done**, щоб завершити налаштування.

        ![Налаштування Samba у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/documents_4_samba.png){class="glboxshadow" width="560"}

## Клієнт WebDAV {#webdav-client}

=== "Windows"

    WebDAV підтримують різні програми, наприклад [RaiDrive](https://www.raidrive.com/){target="_blank"}, [Cyberduck](https://cyberduck.io/download/){target="_blank"} і [WinSCP](https://winscp.net/eng/index.php){target="_blank"}.

    У цьому прикладі використано RaiDrive.

    Натисніть **Add**.

    ![Налаштування WebDAV у RaiDrive](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_add.png){class="glboxshadow"}

    У розділі **Storage** виберіть **NAS** -> **WebDAV**.

    У розділі **Address** установіть або зніміть прапорець біля Address, щоб перемикатися між https/http, та введіть адресу.

    У розділі **Account** введіть ім’я користувача та пароль або встановіть прапорець **Anonymous**.

    Натисніть **Connect**. У Провіднику з’явиться диск X.

    ![Налаштування WebDAV у RaiDrive](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/raidrive_new_drive_webdav.png){class="glboxshadow"}

=== "macOS"

    WebDAV підтримують різні застосунки, наприклад [FE File Explorer](https://apps.apple.com/hk/app/fe-file-explorer/id1444382558?l=en&mt=12){target="_blank"} і [Cyberduck](https://cyberduck.io/download/){target="_blank"}.

    У цьому прикладі використано FE File Explorer.

    Натисніть кнопку Add.

    ![Налаштування WebDAV у FE File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_add.png){class="glboxshadow"}

    Виберіть **WebDAV**.

    ![Налаштування WebDAV у FE File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav.png){class="glboxshadow"}

    Введіть параметри з’єднання. Для анонімного доступу залиште **User Name** і **Password** порожніми. Потім натисніть **Save & Connect**.

    ![Налаштування WebDAV у FE File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/fe_file_explorer_webdav_connection_setting.png){class="glboxshadow"}

    Може з’явитися попередження *The following secure server (null) uses an untrusted certificate. Trust this server?*. Воно пов’язане з використанням самопідписаного сертифіката. Підтвердьте довіру до сервера.

=== "Android"

    Багато застосунків Android підтримують WebDAV. У цьому прикладі використано [Cx File Explorer](https://play.google.com/store/apps/details?id=com.cxinventor.file.explorer&hl=en&gl=US){target="_blank"}.

    Примітка: Cx File Explorer не підтримує анонімний доступ.

    На головній сторінці натисніть **NETWORK**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_home.png){class="glboxshadow" width="400"}

    Натисніть **New Location**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_new_location.png){class="glboxshadow" width="400"}

    Натисніть **WebDAV**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/samba_client/cx_file_explorer_remote.png){class="glboxshadow" width="350"}

    Введіть **Host**, **Port**, **Username** і **Password**.

    ![Налаштування підключення у Cx File Explorer](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/cx_file_explorer_webdav.png){class="glboxshadow" width="350"}

=== "iOS"

    Багато застосунків iOS підтримують WebDAV. У цьому прикладі використано [Documents](https://apps.apple.com/us/app/documents-file-reader-browser/id364901807){target="_blank"}.

    Натисніть кнопку з плюсом у нижньому правому куті.

    ![Налаштування WebDAV у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_1.png){class="glboxshadow" width="560"}

    Натисніть **Add Connection**.

    ![Налаштування WebDAV у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_2.png){class="glboxshadow" width="560"}

    Натисніть **WebDAV Server**.

    ![Налаштування WebDAV у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_3.png){class="glboxshadow" width="560"}

    **Title** — назва з’єднання, **URL** — посилання для доступу, **Login** — ім’я користувача.

    Натисніть **Done**, щоб завершити налаштування.

    ![Налаштування WebDAV у Documents](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_storage/webdav_client/documents_4_webdav.png){class="glboxshadow" width="560"}

## Використання мобільного застосунку {#using-mobile-app}

Вебпанель адміністрування дозволяє керувати лише спільними папками. Для керування файлами на накопичувачі використовуйте [мобільний застосунок](https://www.gl-inet.com/app/#download-app-glinet){target="_blank"}.

- Під час доступу до застосунку через **локальну мережу** відображаються накопичувач і його місткість. Доступне читання та запис файлів.

- Під час доступу до застосунку через **хмару** відображаються накопичувач і його місткість, але читання та запис файлів не підтримуються.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
