# Як вручну налаштувати статичну IP-адресу на клієнтських пристроях? {#how-to-manually-configure-static-ip-on-the-client-devices}

=== "Windows 11"

    У Windows 11 можна налаштувати статичну IP-адресу для бездротових і дротових адаптерів.

    **Налаштування статичної IP-адреси адаптера Wi-Fi**

    1. На комп’ютері з Windows 11 відкрийте **Settings** -> **Network & internet** -> **Wi-Fi** та виберіть поточне з’єднання Wi-Fi.

    2. Знайдіть **IP assignment** і натисніть кнопку **Edit**.

        ![Редагування IP-адреси у Windows 11](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Windows_11_edit_IP_address.png){class="glboxshadow"}

    3. У спливному вікні виберіть **Manual** і ввімкніть **IPv4**.

        ![Ручне налаштування IP](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Виконайте наведені нижче кроки, щоб змінити налаштування IP.

        ![Налаштування статичної IP-адреси](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: установіть статичну IP-адресу, наприклад `10.1.4.119`.

        - Subnet mask: укажіть маску підмережі, наприклад `255.255.255.0`.

        - Gateway: введіть адресу шлюзу, зазвичай це IP-адреса LAN маршрутизатора в тій самій підмережі. Наприклад, якщо ваша IP-адреса — `10.1.4.119`, адреса шлюзу зазвичай — `10.1.4.1`.

        - Preferred DNS: укажіть основну адресу DNS (обов’язково). Можна використати публічний DNS-сервер, наприклад DNS-сервер Google `8.8.8.8`.

        - Alternate DNS: укажіть альтернативну адресу DNS (необов’язково).

        - DNS over HTTPS: виберіть "Off". Доступні три варіанти:

            - Off: увесь DNS-трафік передається без шифрування.

            - On (automatic template): увесь DNS-трафік передається із шифруванням.

            - On (manual template): дає змогу вказати конкретний шаблон. Це потрібно лише тоді, коли служба DNS не працює автоматично або має шаблон, який працює належним чином.

        - Вимкніть перемикач "Fallback to plaintext", якщо вмикаєте DNS over HTTPS.

            **Порада**: якщо ввімкнути цю функцію, система шифруватиме DNS-трафік, але дозволятиме надсилати запити без шифрування.

    5. Натисніть **Save**, щоб застосувати налаштування.

        Після виконання цих кроків статичну конфігурацію мережі буде застосовано на комп’ютері. Щоб перевірити нові налаштування, відкрийте браузер і завантажте вебсайт.

    ---

    **Налаштування статичної IP-адреси адаптера Ethernet**
    {#set-static-ip-address-on-ethernet-adapter}

    1. На комп’ютері з Windows 11 відкрийте **Settings** -> **Network & internet** -> **Ethernet**.

    2. Знайдіть **IP assignment** і натисніть кнопку **Edit**.

        ![Редагування параметрів TCP/IP для Ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Edit_TCP_IP_Ethernet_settings.png){class="glboxshadow"}

    3. У спливному вікні виберіть **Manual** і ввімкніть **IPv4**.

        ![Ручне налаштування IP](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/manual.jpg){class="glboxshadow"}

    4. Виконайте наведені нижче кроки, щоб змінити налаштування IP.

        ![Налаштування статичної IP-адреси](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Settings_app_set_static_IP_address.png){class="glboxshadow"}

        - IP address: установіть статичну IP-адресу, наприклад `10.1.4.119`.

        - Subnet mask: укажіть маску підмережі, наприклад `255.255.255.0`.

        - Gateway: введіть адресу шлюзу, зазвичай це IP-адреса LAN маршрутизатора в тій самій підмережі. Наприклад, якщо ваша IP-адреса — `10.1.4.119`, адреса шлюзу зазвичай — `10.1.4.1`.

        - Preferred DNS: укажіть основну адресу DNS (обов’язково). Можна використати публічний DNS-сервер, наприклад DNS-сервер Google `8.8.8.8`.

        - Alternate DNS: укажіть альтернативну адресу DNS (необов’язково).

        - DNS over HTTPS: виберіть "Off". Доступні три варіанти:

            - Off: увесь DNS-трафік передається без шифрування.

            - On (automatic template): увесь DNS-трафік передається із шифруванням.

            - On (manual template): дає змогу вказати конкретний шаблон. Це потрібно лише тоді, коли служба DNS не працює автоматично або має шаблон, який працює належним чином.

        - Вимкніть перемикач "Fallback to plaintext", якщо вмикаєте DNS over HTTPS.

            **Порада**: якщо ввімкнути цю функцію, система шифруватиме DNS-трафік, але дозволятиме надсилати запити без шифрування.

    5. Натисніть **Save**, щоб застосувати налаштування.

        Після виконання цих кроків статичну конфігурацію мережі буде застосовано на комп’ютері. Щоб перевірити нові налаштування, відкрийте браузер і завантажте вебсайт.

=== "macOS"

    Ось як налаштувати статичну IP-адресу в macOS.

    У меню Apple виберіть **System Preferences**.

    Виберіть **Network**, щоб відкрити наведену нижче сторінку. На бічній панелі виберіть активний мережевий інтерфейс, наприклад **Wi-Fi**.

    ![Мережеві налаштування Mac](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_network_settings.png){class="glboxshadow"}

    Запишіть поточну IP-адресу свого Mac. Потрібно буде вибрати нову IP-адресу з наведеного діапазону приватних IP-адрес.

    Натисніть **Advanced** у нижньому правому куті.

    Потім виберіть **TCP/IP**, щоб відкрити наведену нижче сторінку.

    ![Налаштування Wi-Fi на Mac](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/Mac_Wi-Fi_settings.png){class="glboxshadow"}

    - Configure IPv4: виберіть "Manually".

    - IPv4 Address: введіть статичну IP-адресу. Залиште перші три октети поточної IP-адреси та змініть останній октет на невикористане значення. Наприклад, у мережі `192.168.7.0/24` виберіть вільну адресу від `192.168.7.2` до `192.168.7.254` (уникайте `.1`, це адреса маршрутизатора). Не використовуйте `192.168.7.0` або `192.168.7.255`.

    - Subnet Mask: введіть `255.255.255.0` (або маску підмережі, надану адміністратором мережі).

    - Router: введіть IP-адресу LAN маршрутизатора, наприклад `192.168.7.1`.

    Натисніть **OK**, а потім **Apply**.

=== "iOS"

    Кроки можуть відрізнятися залежно від версії iOS. Наведені нижче кроки стосуються iOS 26.2.2.

    1. Відкрийте **Settings** -> **WLAN**. Натисніть синій значок інформації (i) поруч із поточною підключеною мережею Wi-Fi.

        ![Статична IP-адреса в iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios1.png){class="glboxshadow" width="360"}

    2. Прокрутіть униз до **IPv4 Address** і встановіть **Manual** для **Configure IP**.

        ![Статична IP-адреса в iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios2.png){class="glboxshadow" width="360"}

    3. Укажіть значення **IP Address**, **Subnet Mask** і **Router IP**, які хочете використовувати на iPhone/iPad, а потім натисніть **Save** у верхньому правому куті.

        ![Статична IP-адреса в iOS](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/ios3.png){class="glboxshadow" width="360"}

=== "Android"

    Кроки можуть відрізнятися залежно від версії Android. Наведені нижче кроки стосуються Android 11.

    1. Відкрийте **Settings** -> **Network & Internet** -> **Wi-Fi**. Натисніть поточну підключену мережу, щоб відкрити меню налаштувань.

        ![Список доступних мереж](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/list_available_networks.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    2. Натисніть значок олівця у верхньому правому куті, щоб відкрити налаштування мережі.

        ![Значок олівця](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/pencil_icon.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    3. Натисніть **Advanced options**.

        ![Додаткові параметри](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/advanced_options.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    4. Натисніть **IP Settings** і виберіть **Static**.

        ![Зміна DHCP на Static](https://static.gl-inet.com/docs/router/en/4/tutorials/manually_configure_static_ip/DHCP_to_Static.png){class="gl-50-desktop"}
        {class="glboxshadow"}

    5. Введіть **IP address**. Поле **Gateway** має заповнитися автоматично на основі IP-адреси. Якщо цього не сталося, введіть шлюз вашої мережі. Зазвичай це IP-адреса LAN маршрутизатора в тій самій підмережі.

        **Порада**: для домашніх та інших приватних мереж виберіть вільну адресу вузла у своїй поточній підмережі. Стандартні діапазони приватних IP-адрес:

        ```
        10.0.0.0 ~ 10.255.255.255
        172.16.0.0 ~ 172.31.255.255
        192.168.0.0 ~ 192.168.255.255
        ```

    6. Натисніть **Save** і дочекайтеся повторного підключення до мережі.

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.

