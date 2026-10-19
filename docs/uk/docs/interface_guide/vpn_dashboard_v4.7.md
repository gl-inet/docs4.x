# Панель VPN (прошивка v4.7 і попередні версії) {#vpn-dashboard-firmware-v47-and-earlier}

Вміст цієї сторінки ґрунтується на прошивці v4.7.x і попередніх версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.7 і попередні версії" markdown="1">

- [Прошивка v4.8](vpn_dashboard_v4.8.md)
- [Прошивка v4.9 та новіші версії](vpn_dashboard.md)

</div>

Увійдіть у вебпанель адміністрування та відкрийте **VPN** -> **VPN Dashboard**.

На VPN Dashboard відображаються відомості про з’єднання VPN: адреса сервера, статистика трафіку, віртуальна IP-адреса клієнта та журнал з’єднання. Також можна налаштувати додаткові параметри: аварійне блокування VPN (Kill Switch), політики VPN, маскарадинг IP, MTU та каскадне з’єднання VPN.

Сторінка містить два розділи: [клієнт VPN](#vpn-client) і [сервер VPN](#vpn-server).

![Панель VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpn_dashboard_initial.png){class="glboxshadow"}

## Клієнт VPN {#vpn-client}

Якщо під час першого відкриття сторінки ще немає файлів конфігурації для OpenVPN і WireGuard, сторінка має такий вигляд. Натисніть **Set Up Now**, щоб відкрити [OpenVPN Client](openvpn_client.md) або [WireGuard Client](wireguard_client.md) і завантажити файл конфігурації VPN.

![Налаштування клієнта VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_setup.png){class="glboxshadow"}

Завантажена конфігурація з’явиться у стовпці **Configuration File**. Якщо файлів кілька, виберіть потрібний у цьому полі.

![Вибір файлу конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_config.png){class="glboxshadow"}

<span id="vpn-client-options"></span>
<span id="vpn-clinet-options"></span>

### Параметри клієнта {#client-options}

Натисніть піктограму шестерні праворуч, щоб відкрити параметри клієнта OpenVPN або WireGuard.

![Параметри клієнта VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options.png){class="glboxshadow"}

Параметри клієнта OpenVPN мають такий вигляд.

![Параметри клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_ovpn.png){class="glboxshadow"}

Параметри клієнта WireGuard мають такий вигляд.

![Параметри клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_options_wg.png){class="glboxshadow"}

- **Remote Access LAN**: якщо увімкнено, дозволяється віддалений доступ через VPN до цього маршрутизатора та його пристроїв LAN. Сервер VPN повинен оголошувати маршрут до підмережі LAN цього маршрутизатора.

    У прикладі нижче маршрутизатор GL.iNet працює як клієнт VPN і підключається до сервера VPN через тунель. Якщо цей параметр увімкнено, пристрої на боці сервера VPN, наприклад NAS, можуть отримувати доступ до маршрутизатора GL.iNet та його пристроїв LAN. Для цього додайте на сервері VPN правило маршрутизації до підмережі LAN маршрутизатора GL.iNet.

    ![Віддалений доступ до LAN через VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **IP Masquerading**: якщо увімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

- **MTU**: Maximum Transmission Unit — максимальний розмір одиниці передавання. За потреби задайте власний MTU тунелю VPN; він перевизначає значення у файлі конфігурації.

### Режим проксі {#proxy-mode}

За замовчуванням для VPN використовується **Global Proxy**. Виберіть поле у верхньому правому куті, щоб змінити режим проксі.

![Режим проксі VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_proxy.png){class="glboxshadow"}

Доступні три режими проксі: **Global Proxy**, **Policy Mode** і **Route Mode**.

1. Global Proxy

    У цьому режимі весь трафік проходить через VPN. Можна активувати лише один екземпляр клієнта VPN.

2. Policy Mode

    Цей режим містить три політики.

    - На основі домену або IP-адреси призначення (Based on the Target Domain or IP).

        У цьому режимі лише трафік певних сайтів, визначених за IP-адресою або доменним ім’ям, проходить через VPN. Можна активувати лише один екземпляр клієнта VPN.

    - На основі клієнтського пристрою (Based on the Client Device).

        У цьому режимі лише трафік певних пристроїв LAN, визначених за MAC-адресами, проходить через VPN. Можна активувати лише один екземпляр клієнта VPN.

    - На основі VLAN (Based on the VLAN).

        У цьому режимі лише трафік певної VLAN проходить через VPN. Можна активувати лише один екземпляр клієнта VPN.

3. Route Mode

    - Auto Detect

        Використовуються правила маршрутизації, задані у файлі конфігурації кожного клієнта VPN або надані сервером VPN.

    - Customize Routing Rules

        Правила маршрутизації для кожного екземпляра клієнта VPN можна налаштувати вручну.

### Глобальні параметри {#global-options}

Натисніть **Global Options** у верхньому правому куті, щоб налаштувати додаткові параметри клієнта VPN.

![Глобальні параметри клієнта VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_1.png){class="glboxshadow"}

![Глобальні параметри VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: якщо увімкнено, весь інтернет-трафік проходить виключно через тунель VPN і не може використовувати інші інтерфейси, зокрема локальний WAN провайдера. Якщо VPN несподівано відключиться, весь інтернет-трафік повністю блокується для запобігання переходу на звичайний WAN. Це захищає від витоків через збої VPN, неправильні налаштування DNS клієнтів та подібні проблеми.

    Цю функцію також називають [аварійним блокуванням VPN (Kill Switch)](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Вона запобігає розкриттю даних користувача в інтернеті. Звичайний Kill Switch автоматично припиняє доступ до інтернету, якщо VPN перестає працювати. Block Non-VPN Traffic на маршрутизаторах GL.iNet забезпечує ширший захист від витоків у таких ситуаціях:

    1. Витоки DNS

    2. Витоки IPv6

    3. Витоки WebRTC

    4. Розрив з’єднання VPN

    5. Запуск застосунків до встановлення з’єднання VPN

    6. Витоки трафіку окремих застосунків

- **Allow Access WAN**: якщо увімкнено, локальні клієнтські пристрої можуть отримувати доступ до сервісів на боці WAN, наприклад принтерів, NAS та інших пристроїв підмережі вищого рівня, поки VPN активний.

    ![Доступ до підмережі вищого рівня під час роботи VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Як показано вище, цей параметр дозволяє локальним пристроям отримувати доступ до вузлів підмережі вищого рівня, наприклад принтерів і NAS.

    Цей параметр насамперед призначений для доступу клієнтів до пристроїв підмережі вищого рівня. Однак маршрутизатор не може відрізнити трафік цієї підмережі від звичайного інтернет-трафіку. Якщо клієнти відкривають ресурси безпосередньо за публічними IP-адресами, існує ризик витоку трафіку. Тому **Allow Access WAN** і **Block Non-VPN Traffic** взаємовиключні та не можуть бути увімкнені одночасно.

- **Services From GL.iNet Use VPN**: якщо увімкнено, сервіси GoodCloud, DDNS і rtty передають пакети через тунелі VPN. За замовчуванням цей параметр вимкнено, оскільки для належної роботи цих сервісів зазвичай потрібна справжня IP-адреса пристрою.

## Сервер VPN {#vpn-server}

Якщо маршрутизатор ще не налаштовано як сервер OpenVPN або WireGuard, сторінка має такий вигляд. Натисніть **Set Up Now**, щоб відкрити **OpenVPN Server** або **WireGuard Server** і виконати початкове налаштування сервера VPN.

![Налаштування сервера VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_setup.png){class="glboxshadow"}

Після увімкнення сервера OpenVPN або WireGuard на сторінці відобразиться його стан.

![Сервер VPN увімкнено](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_connected.png){class="glboxshadow"}

### Параметри сервера {#server-options}

Натисніть піктограму шестерні праворуч, щоб відкрити параметри сервера OpenVPN або WireGuard.

![Параметри сервера VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options.png){class="glboxshadow"}

Параметри сервера OpenVPN мають такий вигляд.

![Параметри сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_ovpn.png){class="glboxshadow"}

<span id="wireguard-server-options"></span>

Параметри сервера WireGuard мають такий вигляд.

![Параметри сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_options_wg.png){class="glboxshadow"}

* **Remote Access LAN**: якщо увімкнено, ресурси підмережі LAN сервера доступні через тунель VPN.

* **IP Masquerading**: якщо увімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

* **MTU**: Maximum Transmission Unit — максимальний розмір одиниці передавання. Задане для тунелю значення MTU перевизначає налаштування MTU у файлі конфігурації.

* **Client to Client**: якщо увімкнено, клієнти VPN, підключені до цього сервера, можуть отримувати доступ один до одного за своїми IP-адресами тунелю VPN. Щоб надати доступ і до їхніх підмереж LAN, додайте на сервері VPN правила маршрутизації, які оголошують ці віддалені підмережі.

### Правила маршрутизації сервера {#server-route-rule}

Натисніть піктограму маршрутизації праворуч, щоб за потреби налаштувати власні правила OpenVPN або WireGuard.

![Правила маршрутизації сервера](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule.png){class="glboxshadow"}

Правила маршрутизації сервера OpenVPN мають такий вигляд. Натисніть **Add Route Rule**, введіть **Target Address** і **Gateway**, а потім натисніть зелену піктограму підтвердження для застосування.

![Правила маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

Правила маршрутизації сервера WireGuard мають такий вигляд. Натисніть **Add Route Rule**, введіть **Target Address** і **Gateway**, а потім натисніть зелену піктограму підтвердження для застосування.

![Правила маршрутизації сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Примітка**: у режимі власних правил маршрутизації клієнт VPN ігноруватиме файл конфігурації та налаштування маршрутизації, надані сервером. Використання шифрованого тунелю VPN для доступу до будь-якого сегмента мережі визначатиметься правилами, які ви задали вручну.

### Глобальні параметри {#global-options_1}

Натисніть **Global Options** у верхньому правому куті, щоб налаштувати додаткові параметри сервера VPN.

![Глобальні параметри сервера VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_1.png){class="glboxshadow"}

![Глобальні параметри сервера VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.7/vpnserver_global_options_2.png){class="glboxshadow"}

- **VPN Cascading**: якщо увімкнено, коли маршрутизатор одночасно працює як сервер і клієнт VPN, трафік віддалених клієнтів, підключених до його сервера VPN, проходитиме через тунель VPN вищого рівня, який цей маршрутизатор використовує як клієнт VPN. [Докладніше про каскадне з’єднання VPN](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
