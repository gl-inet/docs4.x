# Додатковий шлюз Drop-in Gateway {#drop-in-gateway}

У меню ліворуч у вебпанелі адміністрування перейдіть до **NETWORK** -> **Drop-in Gateway**.

Drop-in Gateway — функція, яка розширює можливості наявного основного маршрутизатора без його заміни або переналаштування. Підключивши маршрутизатор GL.iNet до основного маршрутизатора кабелем Ethernet, можна додати до наявної мережі розширені функції, наприклад:

- Фільтрацію реклами через AdGuard Home
- Клієнт VPN
- Зашифрований DNS

Рекомендовано використовувати продуктивніший маршрутизатор або шлюз безпеки з достатнім обсягом пам’яті (наприклад, GL-MT2500, GL-MT5000) та за потреби встановити додаткові засоби перенаправлення й контролю трафіку.

## Топологія мережі {#network-topology}

Drop-in Gateway працює як проміжна мережева система: спрямовує трафік клієнтських пристроїв через маршрутизатор GL.iNet для оброблення перед передаванням через основний маршрутизатор. При цьому зберігаються наявні налаштування мережі (наприклад, SSID і пароль), що забезпечує безперервне з’єднання всіх підключених пристроїв. Водночас можна керувати мережевим трафіком усіх або окремих клієнтських пристроїв.

![Топологія мережі з Drop-in Gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_mode_topology.svg){class="glboxshadow gl-60-desktop"}

На схемі вище показано два типи ліній: сірі лінії та зелені лінії з трьома стрілками, кожна з яких позначена відповідним номером.

1. **Сірі лінії** показують топологію фізичних з’єднань: клієнтські пристрої (наприклад, комп’ютер або ноутбук) підключені до основного маршрутизатора, а його порт LAN з’єднаний кабелем Ethernet із портом WAN маршрутизатора GL.iNet, на якому ввімкнено Drop-in Gateway.

2. **Зелені лінії** показують послідовність передавання даних, коли Drop-in Gateway активний. Нумеровані стрілки вказують порядок руху трафіку:

    1. Трафік клієнтських пристроїв спочатку спрямовується на основний маршрутизатор;

    2. Основний маршрутизатор пересилає трафік на маршрутизатор GL.iNet для оброблення (наприклад, фільтрації реклами або шифрування VPN);

    3. Після оброблення трафік повертається на основний маршрутизатор, який передає кінцеві дані початковим клієнтським пристроям або спрямовує їх в інтернет.

## Налаштування {#setup}

Для різних сценаріїв доступні два режими розгортання: усі клієнтські пристрої підключаються до мережі через Drop-in Gateway або лише певні клієнтські пристрої використовують Drop-in Gateway.

У наведеному нижче прикладі адреса шлюзу основного маршрутизатора — `192.168.1.1`.

### Усі пристрої використовують Drop-in Gateway {#all-devices-managed-by-the-drop-in-gateway}

1. З’єднайте порт LAN основного маршрутизатора з портом WAN маршрутизатора GL.iNet кабелем Ethernet.

2. Увійдіть у вебпанель адміністрування маршрутизатора GL.iNet та ввімкніть Drop-in Gateway. Система автоматично згенерує відповідні параметри налаштування.

    ![Автоматично згенеровані параметри Drop-in Gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_all_device_enabled.png){class="glboxshadow"}

    - **IP Address** — WAN IP-адреса маршрутизатора GL.iNet, яку динамічно призначає основний маршрутизатор. Її можна переглянути в розділі Ethernet на сторінці [INTERNET](internet_ethernet.md).

    - За замовчуванням поля **Gateway** і **DNS Server 1** автоматично заповнюються IP-адресою основного маршрутизатора. Якщо ці параметри налаштовано неправильно, змініть їх вручну за потреби.

    Запишіть цю IP-адресу: вона знадобиться в наступних кроках.

    Виберіть перший спосіб налаштування та натисніть **Apply**.

3. Увійдіть у вебпанель адміністрування основного маршрутизатора.

    ??? "GL.iNet"

        Якщо основний маршрутизатор — GL.iNet із прошивкою v4.2 або новішою, виконайте наведені нижче дії.

        Увійдіть у вебпанель адміністрування -> NETWORK -> LAN -> DHCP Server -> Advanced

        ![Додаткові налаштування LAN маршрутизатора GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_advanced.png){class="glboxshadow"}

        У поле DHCP Gateway введіть IP-адресу з кроку 2, наприклад `192.168.1.23`, і натисніть **Apply**.

        ![Шлюз DHCP у налаштуваннях LAN GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/tips_dhcp_gateway.png){class="glboxshadow"}

        ![Шлюз DHCP у налаштуваннях LAN GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/glinet/lan_dhcp_gateway.png){class="glboxshadow"}

    ??? "TP-Link"

        Якщо основний маршрутизатор — TP-Link, виконайте наведені нижче дії (на прикладі TP-LINK Archer C3150).

        Увійдіть на сторінку адміністрування TP-Link, перейдіть до **Advanced** -> **Network** -> **DHCP Server** і вимкніть **DHCP**.

        ![Вимкнення DHCP у панелі TP-Link](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_1.png){class="glboxshadow"}

        Потім натисніть **Save**.

        ![Вимкнення DHCP у панелі TP-Link](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/tplink/tplink_disable_dhcp_2.png){class="glboxshadow"}

    ??? "Linksys"

        Якщо основний маршрутизатор — Linksys, виконайте наведені нижче дії (на прикладі Linksys WHW01).

        Увійдіть на сторінку адміністрування Linksys і перейдіть до **Router Settings** -> **Connectivity**.

        ![Налаштування з’єднання Linksys](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_connectivity.png){class="glboxshadow"}

        Відкрийте вкладку **Local Network**, вимкніть **DHCP Server** і натисніть **OK**.

        ![Вимкнення DHCP-сервера в локальній мережі Linksys](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_disable_dhcp.png){class="glboxshadow"}

        З’явиться попередження. Натисніть **OK**.

        ![Застосування змін у Linksys](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/linksys/linksys_apply_changes.png){class="glboxshadow"}

    ??? "Інші виробники"

        Увійдіть у панель адміністрування основного маршрутизатора та вимкніть його DHCP-сервер. Скористайтеся посібником користувача відповідного виробника або зверніться до його служби підтримки.

4. Поверніться до маршрутизатора GL.iNet і налаштуйте потрібні функції, наприклад [AdGuard Home](adguardhome.md), [зашифрований DNS](dns.md), [клієнт WireGuard](wireguard_client.md) та [клієнт OpenVPN](openvpn_client.md).

### Лише певні пристрої використовують Drop-in Gateway {#some-devices-managed-by-the-drop-in-gateway}

1. З’єднайте порт LAN основного маршрутизатора з портом WAN маршрутизатора GL.iNet кабелем Ethernet.

2. Увійдіть у вебпанель адміністрування маршрутизатора GL.iNet та ввімкніть Drop-in Gateway. Система автоматично згенерує відповідні параметри налаштування.

    ![Автоматично згенеровані параметри Drop-in Gateway](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/drop-in_gateway_some_device_enabled.png){class="glboxshadow"}

    - **IP Address** — WAN IP-адреса маршрутизатора GL.iNet, яку динамічно призначає основний маршрутизатор. Її можна переглянути в розділі Ethernet на сторінці [INTERNET](internet_ethernet.md).

    - За замовчуванням поля **Gateway** і **DNS Server 1** автоматично заповнюються IP-адресою основного маршрутизатора. Якщо ці параметри налаштовано неправильно, змініть їх вручну за потреби.

    Запишіть цю IP-адресу: вона знадобиться в наступних кроках.

    Виберіть другий спосіб налаштування та натисніть **Apply**.

3. На пристрої, який має використовувати Drop-in Gateway, установіть для шлюзу та DNS IP-адресу, показану на сторінці Drop-in Gateway.

    ??? "Windows"

        Нижче наведено приклад для Windows 11; у Windows 10 налаштування подібні. Переконайтеся, що комп’ютер підключено до основного маршрутизатора. У цьому прикладі він підключений мережевим кабелем; для підключення через Wi-Fi налаштування подібні.

        1. Відкрийте Settings.

        2. Натисніть **Network & Internet**.

        3. Відкрийте вкладку **Ethernet**.

            ![Налаштування Ethernet у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet.png){class="glboxshadow"}

        4. Знайдіть IP-адресу цього комп’ютера. У розділі "IP assignment" натисніть кнопку **Edit**.

            ![Зміна параметрів IP у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Виберіть **Manual**. Увімкніть перемикач **IPv4 toggle**.

        6. У поле **IP address** введіть IP-адресу з кроку 4, у поле **Subnet mask** — `255.255.255.0`, а в поля **Gateway** і **Preferred DNS** — IP-адресу зі сторінки Drop-in Gateway.

            ![Зміна параметрів IP у Windows 11](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/windows/windwos11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        7. Натисніть кнопку **Save**.

    ??? "Android"

        Нижче наведено приклад для Samsung S21. Переконайтеся, що смартфон підключено до основного маршрутизатора.

        1. Відкрийте Settings і натисніть Connections.

            ![Розділ з’єднань у налаштуваннях Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/settings_connections.jpg){class="glboxshadow"}

        2. Натисніть Wi-Fi.

            ![Розділ Wi-Fi в Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/connections_wifi.jpg){class="glboxshadow"}

        3. Натисніть значок шестірні біля поточного SSID.

            ![Налаштування поточної мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_cog.jpg){class="glboxshadow"}

        4. Натисніть **View more**.

            ![Додаткові налаштування Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_view_more.jpg){class="glboxshadow"}

        5. Натисніть **IP settings** і виберіть **Static**.

            ![Налаштування IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/wifi_ip_settings.jpg){class="glboxshadow"}

            ![Статичні налаштування IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/ip_settings_static.jpg){class="glboxshadow"}

        6. У поля **Gateway** і **DNS 1** введіть IP-адресу зі сторінки Drop-in Gateway та натисніть **Save**.

            ![Задання адрес шлюзу та DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/android/set_gateway.jpg){class="glboxshadow"}

    ??? "iOS"

        Нижче наведено приклад для iOS 16.3 на iPhone 8. Переконайтеся, що смартфон підключено до основного маршрутизатора.

        1. Відкрийте Settings і натисніть Wi-Fi.

            ![Налаштування Wi-Fi в iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/setting_wifi.jpg){class="glboxshadow gl-60-desktop"}

        2. Натисніть SSID.

            ![Налаштування Wi-Fi в iOS](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/wifi_list.jpg){class="glboxshadow gl-60-desktop"}

        3. Прокрутіть униз: параметр **Configure IP** має значення **Automatic**. Запишіть **IP Address** і **Subnet Mask** для наступного кроку.

            ![Параметри IPv4 мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/ipv4.jpg){class="glboxshadow gl-60-desktop"}

        4. Змініть **Configure IP** на **Manual**, уведіть у поля **IP Address** і **Subnet Mask** значення з попереднього кроку, а в поле **Router** — IP-адресу зі сторінки Drop-in Gateway. Потім натисніть **Save**.

            ![Ручне налаштування IPv4 мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_ipv4.jpg){class="glboxshadow gl-60-desktop"}

        5. Натисніть **Configure DNS** і змініть значення на **Manual**. Натисніть **Add Server**, уведіть IP-адресу DNS-сервера зі сторінки Drop-in Gateway та натисніть **Save**.

            ![Параметри DNS мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/dns.jpg){class="glboxshadow gl-60-desktop"}

            ![Задання DNS для мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/drop-in_gateway/iphone/set_dns.jpg){class="glboxshadow gl-60-desktop"}

4. Поверніться до вебпанелі адміністрування маршрутизатора GL.iNet і налаштуйте потрібні функції, наприклад [AdGuard Home](adguardhome.md), [зашифрований DNS](dns.md), [клієнт WireGuard](wireguard_client.md) та [клієнт OpenVPN](openvpn_client.md).

## Застереження {#cautions}

1. Увімкнення Drop-in Gateway збільшує затримку мережі.

2. Коли Drop-in Gateway ввімкнено, обмін даними між вибраними пристроями LAN також проходить через додатковий шлюз. Тому пропускна здатність між основним маршрутизатором і додатковим шлюзом впливає на загальну пропускну здатність LAN.

---

Пов’язана стаття:

- [Як налаштувати Drop-in Gateway на маршрутизаторі GL.iNet](../tutorials/how_to_set_up_drop_in_gateway.md)

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
