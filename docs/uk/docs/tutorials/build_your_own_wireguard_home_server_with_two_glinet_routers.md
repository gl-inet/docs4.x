# Домашній сервер WireGuard із двома маршрутизаторами GL.iNet {#build-your-own-wireguard-home-server-with-two-glinet-routers}

У цій статті описано налаштування домашнього маршрутизатора як сервера WireGuard VPN, а дорожнього — як клієнта WireGuard VPN для віддаленого з’єднання. Так можна використовувати домашню IP-адресу на дорожньому маршрутизаторі незалежно від місця перебування.

Перегляньте це відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mJXA5MfMb8" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(У відео налаштування VPN показано на GL-MT5000 (Brume 3) і GL-MT3600BE (Beryl 7).)</small>

У наведених нижче діях використано GL-MT6000 (Flint 2) і GL-MT3000 (Beryl AX):

- Домашній маршрутизатор GL-MT6000 працюватиме як сервер WireGuard VPN. Якщо Wi-Fi не потрібний, можна використати шлюз безпеки GL-MT2500 або інші моделі.

- Дорожній маршрутизатор GL-MT3000 працюватиме як клієнт WireGuard VPN для віддаленого підключення до домашнього сервера VPN.

## Навіщо створювати власний домашній сервер WireGuard {#why-build-your-own-wireguard-home-server}

1. Використовуйте домашню IP-адресу як публічну, щоб ваш трафік виглядав так, ніби він надходить з дому.
2. Уникайте щомісячної плати за сторонні послуги VPN.
3. Шифруйте весь інтернет-трафік у тунелі до домашньої мережі, щоб захистити конфіденційність.
4. Отримуйте доступ до домашніх пристроїв і місцевих стримінгових сервісів звідусіль.

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

    Увійдіть у вебпанель адміністрування GL.iNet. У лівому меню виберіть **INTERNET** і перевірте топологію та відомості про з’єднання.

    За прямого підключення через Ethernet відображається розділ «Ethernet» із Protocol, IP address, Gateway та іншими відомостями.

    У прикладі нижче позначена IP Address — WAN IP, яку провайдер призначив цьому маршрутизатору GL.iNet.

    ![Домашнє підключення mt6000-home](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/mt6000_home.png){class="glboxshadow"}

    Ця WAN IP публічна. Отже, маршрутизатор GL.iNet працює як головний, має публічну IP-адресу та **не потребує перенаправлення портів**.

    Налаштуйте цей маршрутизатор GL.iNet як сервер WireGuard, а дорожній — як клієнт WireGuard, який підключатиметься до сервера. Між ними буде створено тунель VPN.

    ![Топологія WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/topologywg.jpg){class="glboxshadow"}

??? "GL.iNet як додатковий маршрутизатор"

    Налаштуйте **Port Forwarding** на головному маршрутизаторі для GL.iNet, якщо останній перебуває за NAT.

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

1. Увійдіть до вебпанелі адміністрування та перейдіть до **VPN** -> **WireGuard Server**. Натисніть **Generate Configuration** лише під час початкового налаштування сервера VPN.

    ![Створення конфігурації сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Перевірте конфігурацію.

    Показана нижче конфігурація за замовчуванням підходить для більшості випадків.

    ![Перевірка конфігурації сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/wg_configuration.png){class="glboxshadow"}

    - **IPv4 Address**: Це IP-адреса тунелю сервера WireGuard. Змінюйте її, лише якщо вона конфліктує з адресою шлюзу маршрутизатора вище за потоком.

        Якщо вона конфліктує зі шлюзом маршрутизатора вищого рівня, змініть її, наприклад на **10.1.0.1/24**, і натисніть **Apply**. Обов’язково вкажіть суфікс CIDR "/24", щоб уникнути проблем зі з’єднанням.

        ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/modify_ipv4.png){class="glboxshadow"}

        Наприклад, якщо вище маршрутизатора GL.iNet розташований маршрутизатор Xfinity, його IP-адреса може бути 10.0.0.1. Вона може конфліктувати з IP-адресою тунелю сервера WireGuard на GL.iNet, тому можуть знадобитися зазначені зміни. Якщо конфлікту немає, пропустіть цей крок.

        ![Адреса шлюзу Xfinity](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

    - **IPv6 Address**: На маршрутизаторах GL.iNet протокол IPv6 за замовчуванням вимкнено. Щоб використовувати IPv6-адресу, увімкніть [IPv6](../interface_guide/ipv6.md) на маршрутизаторі.

    - **Listen Port**: За замовчуванням сервер WireGuard прослуховує порт UDP `51820`. Якщо ви зміните порт і використовуєте перенаправлення портів, оновіть правило на пристрої вище за потоком, щоб перенаправляти трафік на новий порт прослуховування сервера. У параметрі `Endpoint` кожного профілю клієнта вкажіть зовнішній порт із правила перенаправлення. Якщо сервер доступний безпосередньо, використовуйте його порт прослуховування.

    - **Enable Obfuscation**: Якщо цей параметр увімкнено, сервер VPN використовує протокол AmneziaWG для маскування трафіку VPN. Радимо зберегти налаштування маскування за замовчуванням і змінювати їх, лише якщо ви добре знаєте ці параметри. Див. наведені нижче посібники.

        - [Маскування трафіку AmneziaWG на маршрутизаторах GL.iNet](../faq/amneziawg_obfuscation.md)
        - [Налаштування маскування VPN на маршрутизаторах GL.iNet](../tutorials/how_to_set_up_vpn_obfuscation_on_glinet_routers.md)

3. Додайте профіль.

    Відкрийте вкладку **Profiles** і натисніть **Add**, щоб створити профіль для пристрою.

    ![Додавання профілю клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles.png){class="glboxshadow"}

    Задайте зрозумілу назву та натисніть **Apply**, щоб продовжити.

    ![Назва профілю](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Якщо потрібні додаткові налаштування, натисніть **Set More**. Потім натисніть **Apply**, щоб продовжити.

    ![Додаткові налаштування профілю](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Додавання правил маршрутизації за потреби"

        У більшості випадків додавати правила маршрутизації не потрібно.

        Щоб отримувати із сервера доступ до пристроїв LAN клієнта WireGuard, відкрийте вкладку **Route Rules** на сторінці **WireGuard Server** і налаштуйте правила маршрутизації. Додаткові інструкції наведено [тут](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![Правила маршрутизації до LAN клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/route_rules.png){class="glboxshadow"}

        Інакше перейдіть до кроку 4, щоб завантажити конфігурацію клієнта.

4. Завантажте конфігурацію.

    Після додавання профілю та натискання **Apply** маршрутизатор надає конфігурацію як QR-код, звичайний текст або файл `.conf` для завантаження.

    - **QR-код:** Відскануйте код у застосунку WireGuard, щоб імпортувати стандартний профіль WireGuard. Якщо ви ввімкнули маскування, скористайтеся застосунком AmneziaWG або іншим клієнтом із підтримкою маскування AmneziaWG.

        ![Конфігурація клієнта у форматі QR-коду](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: У текстовому форматі можна переглянути конфігурацію та скопіювати її для налаштування вручну, наприклад у застосунку WireGuard або на маршрутизаторі GL.iNet.

        ![Конфігурація клієнта у текстовому форматі](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_text.png){class="glboxshadow"}

    - **Файл .conf**: Натисніть **Download**, щоб зберегти файл .conf на своєму пристрої. Його можна безпосередньо завантажити в застосунок WireGuard або на маршрутизатор GL.iNet.

        ![Файл конфігурації клієнта .conf](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/download_config_file.png){class="glboxshadow"}

    За потреби виберіть адресу сервера: публічну IP-адресу, домен DDNS або поточну IP-адресу WAN. Ця функція доступна починаючи з прошивки v4.8. Після зміни адреса сервера у файлі конфігурації оновиться одночасно.

    Наприклад, якщо публічна IP-адреса мережі часто змінюється, рекомендовано ввімкнути [DDNS](../interface_guide/ddns.md) і використовувати домен DDNS як адресу сервера.

    ![Вибір адреси сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_server_address.png){class="glboxshadow"}

5. Натисніть **Start** угорі праворуч, щоб запустити сервер WireGuard. Стан з’єднання відображатиметься на цій самій сторінці.

    ![Запуск сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/start_wgserver.png){class="glboxshadow"}

## Налаштування клієнта WireGuard {#set-up-wireguard-client}

### Зміна IP-адреси LAN {#change-the-lan-ip}

У цьому прикладі GL-MT6000 і GL-MT3000 мають однакову IP-адресу LAN за замовчуванням — **192.168.8.1**. Щоб уникнути конфлікту, змініть адресу одного з маршрутизаторів.

Нижче описано зміну LAN IP на GL-MT3000, який працює як клієнт WireGuard.

Увійдіть у вебпанель адміністрування GL-MT3000 та відкрийте **NETWORK** у лівому меню -> **LAN**, щоб змінити IP-адресу LAN. Наприклад, замініть стандартну 192.168.8.1 на `192.168.20.1`.

![Зміна IP-адреси LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_wireguard_server/change_lan_ip.png){class="glboxshadow"}

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

- [Налаштування сервера WireGuard на маршрутизаторах GL.iNet](../interface_guide/wireguard_server.md)
- [GL.iNet GoodCloud](../interface_guide/cloud.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
