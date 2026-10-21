# Налаштування сервера WireGuard на маршрутизаторах GL.iNet {#set-up-wireguard-server-on-glinet-routers}

WireGuard® — простий, швидкий і сучасний VPN, який використовує передову криптографію. Його розроблено, щоб бути швидшим, простішим, легшим і кориснішим за IPSec без зайвих складнощів та значно перевершувати OpenVPN за продуктивністю.

Щоб налаштувати сервер WireGuard на маршрутизаторі GL.iNet, перегляньте відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Перевірка наявності публічної IP-адреси {#make-sure-you-have-a-public-ip-address}

За [цією інструкцією](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md) перевірте, чи ваш інтернет-провайдер надає публічну IP-адресу.

**Якщо ні, маршрутизатор не можна налаштувати як сервер WireGuard.**

Альтернативні способи:

1. Якщо у вас є основний маршрутизатор, увійдіть у нього та перевірте, чи отримує він публічну IP-адресу від провайдера.
2. Попросіть провайдера надати публічну IP-адресу. За це може стягуватися додаткова плата.
3. Якщо ці два способи не працюють (наприклад, мережа перебуває за CGNAT), можна спробувати наше рішення SD-WAN [AstroWarp](https://www.astrowarp.net/){target="_blank"}.

## Перевірка потреби в перенаправленні портів {#confirm-if-port-forwarding-is-required}

**Топологія мережі**

??? "GL.iNet — основний маршрутизатор"

    * Якщо GL.iNet — основний маршрутизатор мережі, перенаправлення портів не потрібне. Перейдіть до [наступного кроку](#set-up-wireguard-server).

??? "GL.iNet — додатковий маршрутизатор"

    * Якщо в мережі вже є основний маршрутизатор, а GL.iNet налаштовано як додатковий, налаштуйте [перенаправлення портів](../tutorials/how_to_set_up_port_forwarding.md) на основному маршрутизаторі.

    * Якщо в мережі вже є основний маршрутизатор, а GL.iNet розташований на кілька рівнів нижче нього, налаштуйте [перенаправлення портів](../tutorials/how_to_set_up_port_forwarding.md) на кожному проміжному рівні.

## Налаштування сервера WireGuard {#set-up-wireguard-server}

Увійдіть у вебпанель адміністрування та перейдіть до **VPN** -> **WireGuard Server**.

1. Натисніть **Generate Configuration** (лише під час початкового налаштування сервера VPN).

    ![Створення конфігурації сервера](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Перевірте конфігурацію.

    Конфігурація за замовчуванням підходить для більшості випадків, як показано нижче. Якщо IPv4-адреса не конфліктує зі шлюзом маршрутизатора вищого рівня, змінювати її не потрібно.

    ![Перевірка конфігурації сервера](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/check_configuration.png){class="glboxshadow"}

    (На GL.iNet IPv6 вимкнено за замовчуванням. Щоб використовувати IPv6-адресу, увімкніть IPv6 на маршрутизаторі.)

    IPv4-адреса — це IP-адреса тунелю сервера WireGuard. Якщо вона конфліктує зі шлюзом маршрутизатора вищого рівня, змініть її, наприклад на **10.1.0.1/24**, і натисніть **Apply**. Обов’язково вкажіть суфікс CIDR "/24", щоб уникнути проблем зі з’єднанням.

    ![Зміна IP-адреси тунелю](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Наприклад, якщо вище маршрутизатора GL.iNet розташований маршрутизатор Xfinity, його IP-адреса може бути 10.0.0.1. Вона може конфліктувати з IP-адресою тунелю сервера WireGuard на GL.iNet, тому можуть знадобитися зазначені зміни. Якщо конфлікту немає, пропустіть цей крок.

    ![Адреса шлюзу Xfinity](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Додайте профіль.

    Відкрийте вкладку **Profiles** і натисніть **Add**, щоб створити профіль для пристрою.

    ![Додавання профілю клієнта](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles.png){class="glboxshadow"}

    Задайте зрозумілу назву та натисніть **Apply**, щоб продовжити.

    ![Назва профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_name.png){class="glboxshadow"}

    Якщо потрібні додаткові налаштування, натисніть **Set More**. Потім натисніть **Apply**, щоб продовжити.

    ![Додаткові налаштування профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Додавання правил маршрутизації за потреби"

        У більшості випадків додавати правила маршрутизації не потрібно.

        Щоб отримувати із сервера доступ до пристроїв LAN клієнта WireGuard, відкрийте вкладку **Route Rules** на сторінці **WireGuard Server** і налаштуйте правила маршрутизації. Додаткові інструкції наведено [тут](../tutorials/wireguard_server_access_to_client_lan_side.md).

        ![Правила маршрутизації до LAN клієнта](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/route_rules.png){class="glboxshadow"}

        Інакше перейдіть до кроку 4, щоб завантажити конфігурацію клієнта.

4. Завантажте конфігурацію.

    Після додавання профілю та застосування налаштувань буде створено конфігурацію в трьох форматах: QR-код, звичайний текст і файл .conf. Виберіть зручний спосіб отримання конфігурації.

    - **QR code**: Підходить для кінцевих пристроїв (наприклад, смартфона, планшета або ноутбука), на яких установлено застосунок WireGuard. Щоб налаштувати пристрій як клієнт WireGuard, відкрийте застосунок WireGuard і відскануйте QR-код. Конфігурацію буде імпортовано автоматично.

        ![Конфігурація клієнта у форматі QR-коду](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: У текстовому форматі можна переглянути конфігурацію та скопіювати її для налаштування вручну, наприклад у застосунку WireGuard або на маршрутизаторі GL.iNet.

        ![Конфігурація клієнта у текстовому форматі](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **Файл .conf**: Натисніть **Download**, щоб зберегти файл .conf на своєму пристрої. Його можна безпосередньо завантажити в застосунок WireGuard або на маршрутизатор GL.iNet.

        ![Файл конфігурації клієнта .conf](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/download_config_file.png){class="glboxshadow"}

    За потреби виберіть адресу сервера: публічну IP-адресу, домен DDNS або поточну IP-адресу WAN. Ця функція доступна починаючи з прошивки v4.8. Після зміни адреса сервера у файлі конфігурації оновиться одночасно.

    Наприклад, якщо публічна IP-адреса мережі часто змінюється, рекомендовано ввімкнути [DDNS](ddns.md) і використовувати домен DDNS як адресу сервера.

    ![Вибір адреси сервера](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Запустіть сервер WireGuard.

    Натисніть кнопку **Start** угорі праворуч, щоб запустити сервер WireGuard.

    ![Запуск сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/start_wgserver.png){class="glboxshadow"}

    Стан з’єднання відображатиметься на цій самій сторінці.

    ![Стан сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Перевірка роботи сервера WireGuard {#check-if-wireguard-server-is-working-properly}

### Перевірка стану сервера {#verify-server-status}

Починаючи з прошивки v4.8, стан з’єднання сервера можна перевірити на сторінці **WireGuard Server**.

Якщо відображаються статистика передавання та завантаження трафіку й підключені пристрої, сервер WireGuard працює та має підключених клієнтів WireGuard.

![Підключені клієнти сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status.png){class="glboxshadow"}

Якщо відображається 0 трафіку та 0 клієнтів, жоден клієнт WireGuard не підключений.

![Сервер WireGuard без підключених клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

Для прошивки v4.7 та раніших версій перевіряйте стан з’єднання сервера на сторінці **VPN Dashboard**.

### Перевірка IP-адреси клієнта {#verify-clients-ip}

Щоб перевірити успішне підключення до сервера, імпортуйте експортовану конфігурацію WireGuard на пристрій в іншій мережі, поза локальною мережею сервера. Відкрийте веббраузер і перевірте свою IP-адресу та місце розташування. Якщо вони відповідають IP-адресі та місцю розташування сервера VPN, а не вашого інтернет-провайдера, з’єднання VPN успішне.

Найпростіше скористатися смартфоном з офіційним [застосунком WireGuard](https://www.wireguard.com/install){target="_blank"}. Спочатку вимкніть Wi-Fi на смартфоні та підключіться до інтернету лише через стільникові дані (4G/5G). Відкрийте застосунок WireGuard, імпортуйте файл конфігурації та встановіть з’єднання. Перевірте, чи має смартфон доступ до інтернету та чи відповідає його IP-адреса IP-адресі сервера WireGuard.

Якщо підключення не вдається, можливі такі поширені причини:

* Інтернет-провайдер не надає публічну IP-адресу. Перевірте це [тут](#make-sure-you-have-a-public-ip-address).
* Може бути потрібне перенаправлення портів. Перевірте це [тут](#confirm-if-port-forwarding-is-required).
* Інтернет-провайдер блокує порт сервера WireGuard. Виберіть інший порт або зверніться до провайдера по допомогу.
* У деяких країнах або регіонах з’єднання VPN можуть блокуватися.

## Параметри сервера {#server-options}

Параметри сервера містять додаткові налаштування, зокрема віддалений доступ до LAN сервера та маскарадинг IP. Налаштуйте їх відповідно до потреб.

Для прошивки v4.8 та новіших версій відкрийте **WireGuard Server** і натисніть **Options** угорі праворуч.

![Параметри сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options1.png){class="glboxshadow"}

Для прошивки v4.7 та раніших версій відкрийте **VPN Dashboard** -> **VPN Server** і натисніть значок шестірні, щоб відкрити параметри WireGuard.

![Параметри сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options2.png){class="glboxshadow"}

У спливному вікні відобразяться такі функції.

![Параметри сервера WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/wgserver_options3.png){class="glboxshadow"}

- **Allow Remote Access to the LAN Subnet**: Якщо ввімкнено, ресурси підмережі LAN сервера доступні через тунель VPN.

- **IP Masquerading**: Якщо ввімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

    Як показано нижче, якщо маскарадинг IP увімкнено і NAS (192.168.8.100) у домашній мережі LAN надсилає трафік через тунель на ноутбук (192.168.10.200) у дорожній мережі, домашній маршрутизатор замінює IP-адресу джерела `192.168.8.100` на адресу тунелю сервера VPN `10.1.0.1`. Тому віддалена сторона бачить, що трафік надходить від сервера, а не з локальної мережі LAN сервера.

    ![Маскарадинг IP на сервері WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_server/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Maximum Transmission Unit — максимальний розмір одиниці передавання. Задане для тунелю значення MTU перевизначає налаштування MTU у файлі конфігурації.

- **Client to Client**: Якщо ввімкнено, клієнти VPN цього сервера можуть отримувати доступ один до одного за своїми IP-адресами тунелів VPN.

    Client‑to‑Client оголошує лише IP-адресу тунелю кожного клієнта. Локальні підмережі LAN за клієнтами VPN не стають доступними автоматично. Щоб дозволити клієнтам доступ до LAN один одного, додайте правила маршрутизації на сервері VPN для оголошення цих віддалених підмереж LAN.

## Установлення застосунку WireGuard {#wireguard-app-install}

Завантажте застосунок WireGuard з [офіційного вебсайту WireGuard](https://www.wireguard.com/install){target="_blank"}.

---

WireGuard® — зареєстрована торговельна марка Jason A.Donenfeld.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
