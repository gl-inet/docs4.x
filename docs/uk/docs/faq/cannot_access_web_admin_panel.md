# Не вдається відкрити вебпанель адміністрування {#cannot-access-web-admin-panel}

Іноді адреса [http://192.168.8.1](http://192.168.8.1) може бути недоступна, через що не вдається увійти у вебпанель адміністрування. Можливі кілька причин.

![Вебпанель адміністрування недоступна](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/cantaccessadmin.jpg){class="glboxshadow"}

## Можливі причини {#the-possible-causes}

* Комп’ютер або телефон не підключено до маршрутизатора.
* `192.168.8.1` — IP-адреса маршрутизатора за замовчуванням. Можливо, ви її змінили.
* Кеш або розширення браузера перешкоджають доступу до панелі.
* Програма VPN або проксі обробляє ваш трафік і може перешкоджати доступу до панелі.
* Маршрутизатор став непрацездатним (bricked).

## Перевірка основних дій для доступу до вебпанелі {#check-the-general-steps-to-access-web-admin-panel}

1. Увімкніть маршрутизатор, не підключаючи його до інших пристроїв.
2. Підключіть телефон або ноутбук до Wi-Fi маршрутизатора. Введіть ключ Wi-Fi, зазначений на його етикетці.
3. Якщо крок 2 не допоміг, вимкніть Wi-Fi на комп’ютері або ноутбуці й підключіть його кабелем Ethernet до порту LAN маршрутизатора.
4. Відкрийте браузер, введіть `192.168.8.1` у рядку адреси та натисніть Enter. Має відкритися вебпанель адміністрування GL.iNet.

Також можна отримати доступ до маршрутизатора через [застосунок](mobile_app.md).

## Інші дії для усунення проблеми {#other-steps-to-fix-this-issue}

1. [Перевірте підключення](#check-the-connection)
2. [Перевірте IP-адресу маршрутизатора](#check-routers-ip-address)
3. [Відкрийте IP-адресу маршрутизатора](#access-the-routers-ip-address)

---

### Перевірка підключення {#check-the-connection}

Якщо ви використовуєте кабель Ethernet, перевірте правильність підключення портів WAN/LAN:

- Порт WAN підключено до джерела інтернету, наприклад модема або головного маршрутизатора.
- Порт LAN підключено до кінцевого пристрою, наприклад ноутбука.

Якщо ви використовуєте Wi-Fi, переконайтеся, що вибрано правильний SSID і введено правильний пароль.

### Перевірка IP-адреси маршрутизатора {#check-routers-ip-address}

Виконайте наведені нижче дії, щоб перевірити IP-адресу маршрутизатора.

=== "Windows 10 / Windows 11"

    Відкрийте Control Panel. У верхньому правому куті виберіть для View by значення Large icons або Small icons.

    ![Панель керування Windows](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/control_panel_view_by.png){class="glboxshadow"}

    Відкрийте Control Panel -> Network and Sharing Center і натисніть з’єднання. Якщо з’єднань кілька, виберіть те, яке відповідає потрібному маршрутизатору.

    ![Мережеві з’єднання в центрі мереж](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections.png){class="glboxshadow"}

    З’явиться вікно стану з’єднання. Натисніть кнопку докладних відомостей.

    ![Стан мережевого з’єднання](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status.png){class="glboxshadow"}

    У вікні докладних відомостей про мережеве з’єднання IP-адреса маршрутизатора вказана в **IPv4 Default Gateway**.

    ![Докладні відомості про мережеве з’єднання](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/network_and_sharing_center_connections_status_detail.png){class="glboxshadow"}

=== "Windows 7"

    Відкрийте Control Panel -> Network and Internet -> Network and Sharing Center -> Change adapter settings.

    Натисніть мережеве з’єднання правою кнопкою миші та виберіть Status -> Details.

    IP-адреса маршрутизатора вказана в **IPv4 Default Gateway**.

    ![Властивості мережі у Windows 7](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/property_of_network_win7.jpg){class="glboxshadow"}

=== "macOS"

    1. Відкрийте System Preferences -> Network.

    2. У лівому стовпці виберіть мережеве з’єднання. Для Ethernet відобразиться IP-адреса маршрутизатора.

    ![IP-адреса маршрутизатора для Ethernet у macOS](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_ethernet_on_mac_os.jpg){class="glboxshadow"}

    Для Wi-Fi натисніть «Advanced...», а потім вкладку «TCP/IP» угорі вікна. Відобразиться IP-адреса маршрутизатора.

    ![IP-адреса маршрутизатора для Wi-Fi у macOS](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_of_wifi_on_mac_os.jpg){class="glboxshadow"}

=== "iOS"

    1. Відкрийте Settings -> Wi-Fi.
    2. Натисніть піктограму інформації (синя літера i у колі) біля поточної мережі Wi-Fi. Відобразиться IP-адреса маршрутизатора.

    ![IP-адреса маршрутизатора на iPhone](https://static.gl-inet.com/docs/router/en/4/faq/cannot_access_web_admin_panel/router_ip_address_on_iphone.jpg){class="glboxshadow"}

=== "Android"

    Дії можуть відрізнятися залежно від пристрою Android.

    1. Відкрийте Settings -> Network & internet.
    2. Відкрийте Wi-Fi, знайдіть підключену мережу та натисніть піктограму налаштувань.
    3. Розгорніть Advanced. Якщо доступні варіанти Static або Dynamic IP, виберіть Static.
    4. IP-адреса маршрутизатора має відображатися в Gateway.

### Доступ за IP-адресою маршрутизатора {#access-the-routers-ip-address}

1. Для кращої сумісності використовуйте Chrome/Edge/Safari, щоб відкрити панель адміністрування.

2. Щоб уникнути проблем із кешем і розширеннями браузера, відкрийте вікно інкогніто та спробуйте знову відкрити IP-адресу маршрутизатора.

3. Вимкніть усі програми VPN або проксі, зокрема Tailscale і ZeroTier.

4. На телефоні вимкніть мобільні дані.

    Деякі смартфони відключаються від Wi-Fi маршрутизатора та переходять на мобільні дані, якщо виявляють, що маршрутизатор не має доступу до інтернету. Однак без підключення до маршрутизатора вебпанель адміністрування недоступна.

5. Якщо попередні дії не допомогли, спробуйте [скинути маршрутизатор до заводських налаштувань](repair_network_or_reset_firmware.md#reset-to-factory).

6. Якщо скидання не допомогло, спробуйте [відновлення через U-Boot](debrick.md).

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
