# Домашній сервер WireGuard із двома маршрутизаторами GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

У цій статті описано налаштування домашнього маршрутизатора як сервера WireGuard VPN, а дорожнього — як клієнта WireGuard VPN для віддаленого з’єднання. Так можна використовувати домашню IP-адресу на дорожньому маршрутизаторі незалежно від місця перебування.

Перегляньте це відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(У відео налаштування VPN показано на GL-MT5000 (Brume 3) і GL-MT3600BE (Beryl 7).)</small>

У наведених нижче діях використано GL-MT6000 (Flint 2) і GL-MT3000 (Beryl AX):

- Домашній маршрутизатор GL-MT6000 працюватиме як сервер WireGuard VPN. Якщо Wi-Fi не потрібний, можна використати шлюз безпеки GL-MT2500 або інші моделі.

- Дорожній маршрутизатор GL-MT3000 працюватиме як клієнт WireGuard VPN для віддаленого підключення до домашнього сервера VPN.

## Навіщо створювати домашній сервер WireGuard {#why-you-need-to-build-your-own-wireguard-home-server}

1. Використання домашньої IP-адреси для доступу до інтернету, ніби ви перебуваєте вдома.
2. Відсутність щомісячної плати за сторонній VPN-сервіс.
3. Передавання всього інтернет-трафіку до домашньої мережі через шифрований тунель VPN для захисту конфіденційності.
4. Зручний доступ до внутрішніх ресурсів і локального потокового контенту.

## Підготовка {#preparations}

### Перевірка наявності публічної IP-адреси {#check-if-you-have-a-public-ip}

Спочатку переконайтеся, що GL-MT6000 має публічну IP-адресу WAN для доступу з інтернету. Інакше дорожній маршрутизатор не зможе встановити з ним з’єднання VPN під час подорожі.

Для перевірки відкрийте браузер і перейдіть на [what is my ip](https://whatismyipaddress.com/){target="_blank"}.

![Перевірка публічної IP-адреси](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/whatismyip.jpg){class="glboxshadow"}

Відобразиться публічна IP-адреса. Якщо вона збігається з WAN IP, яку провайдер призначив GL-MT6000, маршрутизатор має публічну IP-адресу.

Якщо публічної IP-адреси немає, скористайтеся одним із таких способів.

1. Якщо у вас є головний маршрутизатор, увійдіть у нього та перевірте, чи отримує він публічну IP-адресу від провайдера.
2. Запитайте публічну IP-адресу у провайдера. Це може потребувати додаткової оплати.
3. Якщо попередні способи не допомагають, наприклад мережа перебуває за CGNAT, спробуйте наше рішення SD-WAN [AstroWarp](../interface_guide/astrowarp.md){target="_blank"}.

### Перевірка потреби в перенаправленні портів {#check-if-port-forwarding-is-required}

??? "GL.iNet як головний маршрутизатор"

    Якщо маршрутизатор GL.iNet підключено безпосередньо до модема провайдера кабелем Ethernet, він є головним маршрутизатором.

    **Як перевірити, чи GL.iNet підключено безпосередньо до модема провайдера?**

    Виконайте такі дії:

    1. Увійдіть у вебпанель адміністрування GL.iNet.

    2. Виберіть INTERNET у лівому меню та перевірте топологію й відомості про з’єднання:

        За прямого підключення через Ethernet відображається розділ «Ethernet» із Protocol, IP address, Gateway та іншими відомостями.

        У прикладі нижче позначена IP Address — WAN IP, яку провайдер призначив цьому маршрутизатору GL-iNet.

        ![Домашнє підключення mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

        Ця WAN IP публічна. Отже, маршрутизатор GL.iNet працює як головний, має публічну IP-адресу та **не потребує перенаправлення портів**.

        Налаштуйте цей маршрутизатор GL.iNet як сервер WireGuard, а дорожній — як клієнт WireGuard, який підключатиметься до сервера. Між ними буде створено тунель VPN.

        ![Топологія WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet як додатковий маршрутизатор"

    Налаштуйте **Port Forwarding** на головному маршрутизаторі для GL.iNet, якщо останній перебуває за NAT.

    Топологія

    ![WireGuard із додатковим маршрутизатором](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywgtp.jpg){class="glboxshadow"}

    У цьому прикладі головний домашній маршрутизатор — TP-Link.

    Підключіться до Wi-Fi або LAN домашнього маршрутизатора та увійдіть у його вебпанель адміністрування. Перевірте WAN IP, отриману від провайдера. На зображенні нижче публічна IP-адреса — **42.200.00.00**.

    ![WAN IP головного маршрутизатора TP-Link](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_home.png){class="glboxshadow"}

    **Перед перенаправленням портів рекомендовано зарезервувати IP-адресу маршрутизатора GL.iNet на головному маршрутизаторі, щоб адреса залишалася постійною.** Інакше після перезавантаження головного маршрутизатора або GL.iNet може бути призначено іншу адресу, і правило перенаправлення перестане працювати.

    Потім налаштуйте перенаправлення портів на головному маршрутизаторі для GL.iNet.

    1. Відкрийте «Advanced», натисніть «virtual Server», а потім «Add».

    2. Internal IP (Device IP): IP-адреса, призначена маршрутизатору GL.iNet. Знайдіть її у списку клієнтів TP-Link.

    3. External/Internal port: в обох полях введіть «51820».

    4. Protocol: виберіть All, UDP або TCP/UDP.

    ![Перенаправлення портів на TP-Link](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/tp_port1.jpg){class="glboxshadow"}

    **Інші приклади [перенаправлення портів](how_to_set_up_port_forwarding.md)**

## Налаштування сервера WireGuard {#set-up-wireguard-server}

### Увімкнення DDNS — за потреби {#enable-ddns-optional}

Увімкніть DDNS, якщо у вас динамічна публічна IP-адреса замість статичної.

Увійдіть у вебпанель адміністрування GL-MT6000 та відкрийте **APPLICATIONS** -> **Dynamic DNS**. Увімкніть **Enable DDNS**.

Прийміть **Terms of Service & Privacy Policy** та натисніть **Apply**.

![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/enable_ddns.jpg){class="glboxshadow"}

Відкрийте **WireGuard Server** -> вкладку Configuration, перевірте, що Listen Port — 51820, і натисніть **Apply**.

![Налаштування сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgserver-apply.png){class="glboxshadow"}

### Створення конфігурації {#generate-configuration}

На цій сторінці відкрийте вкладку **Profiles** біля Configuration і натисніть **Add** (позначка 1 на зображенні).

Конфігурацію клієнта буде створено автоматично. Натисніть **піктограму пересилання** (позначка 2).

У спливному вікні за потреби увімкніть DDNS Domain (позначка 3). Це потрібно лише для динамічної публічної IP-адреси.

![Створення профілю WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgconfiggen.jpg){class="glboxshadow"}

Відскануйте QR-код [мобільним застосунком WireGuard](https://www.wireguard.com/install/), щоб перевірити сервер. Докладніше див. [цей розділ](../interface_guide/wireguard_server.md#check-if-wireguard-server-is-working-properly).

Також можна експортувати текстову конфігурацію для підключення клієнта VPN.

Відкрийте вкладку **Configuration File**, щоб перейти від QR-коду до текстового формату.

Скопіюйте текст для клієнта або натисніть Download і збережіть файл для подальшого використання.

![Експорт конфігурації WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/configload.jpg){class="glboxshadow"}

## Налаштування клієнта WireGuard {#set-up-wireguard-client}

### Зміна IP-адреси LAN {#change-the-lan-ip}

У цьому прикладі GL-MT6000 і GL-MT3000 мають однакову IP-адресу LAN за замовчуванням — **192.168.8.1**. Щоб уникнути конфлікту, змініть адресу одного з маршрутизаторів.

Нижче описано зміну LAN IP на GL-MT3000, який працює як клієнт WireGuard.

Увійдіть у вебпанель адміністрування GL-MT3000 та відкрийте **NETWORK** у лівому меню -> **LAN**, щоб змінити IP-адресу LAN. Наприклад, замініть стандартну 192.168.8.1 на `192.168.10.1`.

![Зміна IP-адреси LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

Докладні відомості про інтерфейс LAN наведено [тут](../interface_guide/lan.md).

### Додавання конфігурації {#add-the-configuration}

У вебпанелі адміністрування GL-MT3000 відкрийте **VPN** -> **WireGuard Client** і натисніть **Add Manually**.

![Додавання клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-1.png){class="glboxshadow"}

Створіть групу ліворуч і задайте назву. Виберіть файл конфігурації для завантаження або перетягніть його в область завантаження праворуч.

![Група профілів WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-2.png){class="glboxshadow"}

Після перевірки файлу натисніть **Apply**.

![Завантаження конфігурації WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-3.png){class="glboxshadow"}

Також можна натиснути **Manually Add Configuration**, вставити текст конфігурації та натиснути **Apply**.

![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-4.png){class="glboxshadow"}

![Текст конфігурації WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-5.jpg){class="glboxshadow"}

Після успішного завантаження файл з’явиться на сторінці WireGuard Client.

![Завантажений профіль WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/addwgclient-6.png){class="glboxshadow"}

### Встановлення з’єднання {#start-the-connection}

Натисніть піктограму з трьома крапками, а потім **Start**.

![Запуск клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientstart.png){class="glboxshadow"}

Зачекайте кілька хвилин. Після успішного підключення з’явиться зелена крапка.

![З’єднання WireGuard встановлено](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclient_connected.png){class="glboxshadow"}

Відкрийте **VPN Dashboard**. Відобразиться підключення клієнта до сервера з домашньою публічною IP-адресою. Вигляд сторінки може відрізнятися залежно від прошивки.

![Стан клієнта VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgclientup.jpg){class="glboxshadow"}

Поверніться у вебпанель адміністрування GL-MT6000 (сервера WireGuard) та відкрийте **VPN** -> **WireGuard Server**. У прошивці v.4.7 і попередніх версіях відкрийте **VPN** -> **VPN Dashboard**. Відобразиться стан з’єднання, який підтверджує підключення клієнта.

![Стан сервера VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.8.png){class="glboxshadow"}
<small>(Сторінка WireGuard Server у FW v4.8)</small>

![Стан сервера VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wgservercon-4.7.jpg){class="glboxshadow"}
<small>(VPN Dashboard у FW v4.7 і попередніх версіях)</small>

## Підготовка до віддаленого усунення проблем VPN {#prep-for-remote-vpn-fixes-ahead}

Перед подорожжю прив’яжіть обидва маршрутизатори до облікового запису GoodCloud. Це дасть змогу віддалено усувати проблеми, якщо з’єднання VPN не працюватиме через конфігурацію або інші мережеві проблеми. Віддалений доступ працює лише тоді, коли маршрутизатори залишаються ввімкненими й підключеними до інтернету.

---

Пов’язані статті

- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
