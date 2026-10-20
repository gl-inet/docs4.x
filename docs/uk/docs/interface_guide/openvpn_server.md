# Налаштування сервера OpenVPN на маршрутизаторах GL.iNet {#set-up-openvpn-server-on-glinet-routers}

OpenVPN — протокол VPN із відкритим вихідним кодом, який використовує технології віртуальних приватних мереж для встановлення захищених з’єднань між мережами (site-to-site) або між двома вузлами (point-to-point).

Щоб налаштувати сервер OpenVPN на маршрутизаторі GL.iNet, перегляньте це відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/GSbytyaqOY0" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Перевірка наявності публічної IP-адреси {#make-sure-you-have-a-public-ip-address}

За [цією інструкцією](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) перевірте, чи ваш інтернет-провайдер надає публічну IP-адресу.

**Якщо ні, маршрутизатор не можна налаштувати як сервер OpenVPN.**

Альтернативні способи:

1. Якщо у вас є головний маршрутизатор, увійдіть у нього та перевірте, чи отримує він публічну IP-адресу від провайдера.
2. Запитайте публічну IP-адресу у провайдера. Це може потребувати додаткової оплати.
3. Якщо попередні способи не допомагають, наприклад мережа перебуває за CGNAT, спробуйте наше рішення SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

## Перевірка потреби в перенаправленні портів {#confirm-if-port-forwarding-is-required}

**Топологія мережі**

??? "GL.iNet — головний маршрутизатор"

    * Якщо маршрутизатор GL.iNet є головним у вашій мережі, перенаправлення портів не потрібне. Перейдіть до [наступного кроку](#set-up-openvpn-server).

??? "GL.iNet — додатковий маршрутизатор"

    * Якщо в мережі вже є головний маршрутизатор, а GL.iNet працює як додатковий, налаштуйте [перенаправлення портів](../tutorials/how_to_set_up_port_forwarding.md) на головному маршрутизаторі.

    * Якщо маршрутизатор GL.iNet розташований на кілька рівнів нижче головного, налаштуйте [перенаправлення портів](../tutorials/how_to_set_up_port_forwarding.md) на кожному проміжному рівні.

## Налаштування сервера OpenVPN {#set-up-openvpn-server}

Увійдіть у вебпанель адміністрування та відкрийте **VPN** -> **OpenVPN Server**.

1. Натисніть **Generate Configuration** (лише під час початкового налаштування сервера VPN).

    ![Створення конфігурації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_generate.png){class="glboxshadow"}

2. Застосуйте конфігурацію.

    Конфігурація за замовчуванням підходить для більшості випадків.

    Якщо змінювати конфігурацію не потрібно, натисніть **Export Client Configuration** унизу та перейдіть до кроку 3.

    Якщо конфігурацію змінено, натисніть **Apply** перед її експортом для клієнта.

    ![Конфігурація сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_configuration.png){class="glboxshadow"}

    * **Device Mode:** TAP-S2S або Tun. Відмінності описано [тут](../tutorials/how_to_enable_openvpn_tap_s2s_mode_on_glinet_routers.md#tap-s2s-vs-tun-mode).

    * **Protocol:** UDP або TCP. Відмінності описано [тут](../faq/openvpn_tcp_udp.md).

    * **Authentication Mode:** спосіб автентифікації під час підключення клієнта до сервера. Доступні три варіанти.

        - **Certificate Only**: маршрутизатор автоматично створює сертифікати сервера та клієнта й вбудовує сертифікат і ключ клієнта у файл конфігурації клієнта. Під час завантаження цієї конфігурації на клієнт додаткові облікові дані не потрібні.

        - **Username/Password Only**: маршрутизатор створює конфігурацію клієнта без ключів сертифікатів. Перед експортом спочатку додайте ім’я користувача та пароль на вкладці Users. Під час завантаження конфігурації на клієнт потрібно ввести ці дані для автентифікації.

        - **Username/Password and Certificate**: перед експортом конфігурації клієнта спочатку додайте ім’я користувача та пароль на вкладці Users. Маршрутизатор автоматично створює сертифікати сервера та клієнта й вбудовує сертифікат і ключ клієнта у файл конфігурації. Під час завантаження на клієнт спочатку перевіряється ключ сертифіката, а потім ім’я користувача та пароль для двофакторного захисту.

        Нижче наведено приклад створення користувача.

        ![Додавання користувача сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_add_a_user.png){class="glboxshadow"}

    * **Advanced Configuration**: за потреби змініть додаткові параметри сервера.

        ![Додаткові налаштування сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_advanced_config.png){class="glboxshadow"}

3. Експортуйте конфігурацію клієнта.

    Натисніть **Export Client Configuration** унизу вкладки Configuration або застосуйте змінену конфігурацію. З’явиться вікно, показане нижче.

    ![Експорт конфігурації OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_export_config.png){class="glboxshadow"}

    - Якщо публічна IP-адреса мережі часто змінюється, увімкніть [DDNS](ddns.md), щоб використовувати домен DDNS як адресу сервера.

    - Починаючи з прошивки v4.8, для адреси сервера можна вибрати публічну IP-адресу, домен DDNS або поточну IP-адресу WAN. Після зміни адреса сервера у файлі конфігурації оновлюється одночасно.

    Потім натисніть **Download**, щоб експортувати конфігурацію.

4. Запустіть сервер OpenVPN.

    На сторінці OpenVPN Server натисніть **Start** у верхньому правому куті для запуску сервера. Відкрийте VPN Dashboard, щоб перевірити стан і додаткові налаштування.

    ![Запуск сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/start_ovpnserver.png){class="glboxshadow"}

## Перевірка роботи сервера OpenVPN {#check-if-openvpn-server-is-working-properly}

### Перевірка стану сервера {#verify-server-status}

Починаючи з прошивки v4.8, стан з’єднання сервера можна перевірити на сторінці **OpenVPN Server**.

Якщо відображається статистика завантаження та передавання трафіку, сервер OpenVPN працює.

![Стан сервера OpenVPN у v4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_status.jpg){class="glboxshadow"}

У прошивці v4.7 і попередніх версіях перевіряйте стан з’єднання сервера на **VPN Dashboard**.

![Стан сервера OpenVPN у v4.7](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/openserverup.jpg){class="glboxshadow"}

### Перевірка IP-адреси клієнта {#verify-clients-ip}

Щоб перевірити з’єднання із сервером, імпортуйте експортовану конфігурацію OpenVPN на пристрій в іншій мережі, за межами локальної мережі сервера. Відкрийте браузер і перевірте свою IP-адресу та розташування. Якщо вони відповідають IP-адресі та розташуванню сервера VPN, а не вашого інтернет-провайдера, з’єднання VPN встановлено успішно.

Найпростіше використати смартфон з офіційним [застосунком OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}. Вимкніть Wi-Fi та підключіться до інтернету лише через стільникові дані (4G/5G). Відкрийте OpenVPN, імпортуйте файл конфігурації та встановіть з’єднання. Перевірте доступ до інтернету й відповідність IP-адреси смартфона IP-адресі сервера OpenVPN.

Під час імпорту конфігурації в OpenVPN може з’явитися повідомлення, показане нижче. Натисніть **CONTINUE**, оскільки сертифікат уже вбудовано у файл конфігурації.

![Повідомлення про сертифікат у застосунку OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/select_certificate.png){class="glboxshadow" width="360"}

Якщо підключення не вдається, можливі такі поширені причини:

* Провайдер не надає публічну IP-адресу. Див. [цей розділ](#make-sure-you-have-a-public-ip-address).
* Потрібно налаштувати перенаправлення портів. Див. [цей розділ](#confirm-if-port-forwarding-is-required).
* Провайдер блокує порт сервера OpenVPN. Змініть порт або зверніться до провайдера по допомогу.
* У деяких країнах або регіонах з’єднання VPN можуть блокуватися.

## Параметри сервера {#server-options}

Параметри сервера містять додаткові налаштування, зокрема віддалений доступ до LAN сервера та маскарадинг IP. Налаштуйте їх відповідно до потреб.

У прошивці v4.8 і новіших версіях відкрийте **OpenVPN Server** і натисніть **Options** у верхньому правому куті.

![Параметри сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options1.png){class="glboxshadow"}

У прошивці v4.7 і попередніх версіях відкрийте **VPN Dashboard** -> **VPN Server** і натисніть піктограму шестерні, щоб відкрити OpenVPN Options.

![Параметри сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options2.jpg){class="glboxshadow"}

У спливному вікні відобразяться такі функції.

![Параметри сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: якщо увімкнено, ресурси підмережі LAN сервера доступні через тунель VPN.

- **IP Masquerading**: якщо увімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

- **MTU**: Maximum Transmission Unit — максимальний розмір одиниці передавання. Задане для тунелю значення MTU перевизначає налаштування MTU у файлі конфігурації.

## Зв’язок між клієнтами {#client-to-client}

Client-to-Client — функція сервера VPN. Після увімкнення підключені клієнти VPN можуть обмінюватися даними за своїми IP-адресами тунелю VPN.

Топологія мережі має такий вигляд.

![Схема зв’язку між клієнтами VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ptptopology.jpg){class="glboxshadow"}

За потреби виконайте наведені нижче дії, щоб увімкнути Client to Client на сервері OpenVPN.

1. На сторінці **OpenVPN Server** натисніть **Advanced Configuration** у нижньому правому куті.

    ![Додаткові налаштування сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/ovpnserver_config_advanced.png){class="glboxshadow"}

2. Увімкніть **Client to Client** і натисніть **Apply**. Потім експортуйте нову конфігурацію та завантажте її на клієнти OpenVPN.

    ![Увімкнення зв’язку між клієнтами](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_server/client-to-client.png){class="glboxshadow"}

**Порада**: Client-to-Client оголошує лише IP-адресу тунелю кожного клієнта. Функція не надає автоматично доступ до локальних підмереж LAN за клієнтами VPN. Щоб клієнти могли отримувати доступ до підмереж LAN один одного, додайте на сервері VPN правила маршрутизації, які оголошують ці віддалені підмережі.

## Встановлення застосунку OpenVPN {#openvpn-app-install}

Завантажте застосунок OpenVPN з [офіційного сайту OpenVPN](https://openvpn.net/vpn-client/){target="_blank"}.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
