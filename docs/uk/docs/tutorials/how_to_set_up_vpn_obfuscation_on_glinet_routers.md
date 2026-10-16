# Як налаштувати обфускацію VPN на маршрутизаторах GL.iNet? {#how-to-set-up-vpn-obfuscation-on-glinet-routers}

**Примітка**: Маршрутизатори GL.iNet підтримують AmneziaWG у прошивці v4.9 та новіших версіях. Спочатку оновіть маршрутизатор до підтримуваної версії.

У цьому посібнику описано два сценарії налаштування обфускації AmneziaWG на маршрутизаторах GL.iNet.

## Сценарій 1. Два маршрутизатори GL.iNet {#scenario-1-using-two-glinet-routers}

У цьому сценарії два маршрутизатори GL.iNet встановлюють з’єднання VPN з обфускацією за протоколом AmneziaWG.

- Brume 3 (GL-MT5000): сервер VPN для дому.
- Beryl AX (GL-MT3000): портативний клієнт VPN для подорожей.

### Налаштування сервера VPN {#set-up-vpn-server}

1. Увійдіть у вебпанель адміністрування Brume 3.

    Підключіть пристрій, наприклад ноутбук або комп’ютер, до порту LAN Brume 3 кабелем Ethernet. Відкрийте браузер, уведіть адресу адміністрування за замовчуванням, зазвичай `192.168.8.1`, і ввійдіть за допомогою пароля адміністратора.

2. Завершіть початкове налаштування Brume 3 для доступу до інтернету.

    Якщо Brume 3 — основний маршрутизатор, підключіть його порт WAN до мережі вищого рівня, наприклад модема провайдера.

    Якщо він не основний, тобто вище є інший основний пристрій, наприклад маршрутизатор провайдера, налаштуйте **перенаправлення портів** на основному маршрутизаторі. Дивіться [цю інструкцію](how_to_set_up_port_forwarding.md).

3. Увімкніть DDNS (необов’язково).

    Увімкніть DDNS, якщо публічна IP-адреса динамічна, а не статична.

    У меню ліворуч перейдіть до **APPLICATIONS** -> **Dynamic DNS**. Увімкніть **Enable DDNS**, прийміть **Terms of Service & Privacy Policy** і натисніть **Apply**.

    ![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/enable_ddns.png){class="glboxshadow"}

4. Увімкніть обфускацію VPN.

    У меню ліворуч відкрийте **VPN** > **WireGuard Server** -> вкладку **Configurations**, увімкніть **Enable Obfuscation** і натисніть **Apply**.

    ![Увімкнення обфускації VPN на сервері](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}

    За потреби змініть параметри обфускації. Докладніше дивіться [тут](../faq/amneziawg_obfuscation.md#parameter-overview).

    Рекомендуємо залишити налаштування за замовчуванням.

    ![Увімкнення обфускації VPN на сервері](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}

5. Експортуйте файл конфігурації.

    На сторінці **WireGuard Server** відкрийте вкладку **Profiles** і натисніть **Add**, щоб створити файл конфігурації для підключення Beryl AX.

    ![Створення та експорт профілю клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}

    Задайте зрозумілу назву, наприклад Travel Router, і натисніть **Apply**.

    ![Створення та експорт профілю клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}

    У спливному вікні натисніть **Export**, щоб завантажити файл конфігурації на пристрій для подальшого використання.

    ![Створення та експорт профілю клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}

6. Запустіть сервер VPN.

    Угорі сторінки **WireGuard Server** натисніть кнопку **Start**, щоб запустити сервер.

    ![Запуск сервера з обфускацією](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}

    Сервер VPN з обфускацією AmneziaWG увімкнено. До Brume 3 можна підключатися через застосунок AmneziaWG або маршрутизатор GL.iNet із прошивкою, яка підтримує обфускацію AmneziaWG.

    **Примітка: Клієнти без підтримки обфускації AmneziaWG не зможуть підключитися.**

    ![Запуск сервера з обфускацією](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}

### Налаштування клієнта VPN {#set-up-vpn-client}

1. Увійдіть у вебпанель адміністрування Beryl AX.

    Підключіть пристрій, наприклад ноутбук або комп’ютер, до Wi-Fi Beryl AX або до його порту LAN кабелем Ethernet. Відкрийте браузер, уведіть адресу адміністрування за замовчуванням, зазвичай `192.168.8.1`, і ввійдіть за допомогою пароля адміністратора.

2. Завершіть початкове налаштування Beryl AX для доступу до інтернету.

    **Порада**: Підключіть Beryl AX до іншої мережі, ніж Brume 3. Наприклад, увімкніть мобільну точку доступу для підключення Beryl AX.

3. Завантажте файл конфігурації.

    У меню ліворуч перейдіть до **VPN** > **WireGuard Client**. Додайте групу та задайте зрозумілу назву, наприклад Home Router.

    ![Додавання групи клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}

    Праворуч завантажте раніше експортований файл конфігурації.

    ![Завантаження файла конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}

    Після завантаження файла та успішної перевірки натисніть **Apply**.

    ![Перевірена конфігурація клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}

    Сторінка оновиться, а у списку відображатиметься один файл конфігурації.

4. Установіть з’єднання VPN.

    Натисніть значок із трьома крапками та виберіть **Start**.

    ![Запуск з’єднання клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}

    Зачекайте приблизно 1 хвилину. Якщо індикатор стану стане зеленим, з’єднання VPN успішне.

    ![Клієнт успішно підключений](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}

    Відкрийте **VPN Dashboard**. Ви побачите, що Beryl AX підключено до домашнього маршрутизатора Brume 3.

    ![Стан з’єднання з домашнім сервером](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}

5. Виконайте додаткову перевірку (необов’язково).

    Увійдіть у вебпанель адміністрування Brume 3 та перейдіть до **VPN** -> **WireGuard Server**. Там відображатиметься клієнт Beryl AX, підключений до сервера VPN Brume 3.

    ![Підключений клієнт на сервері](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}

    З’єднання VPN налаштовано. Усі пристрої на Beryl AX тепер отримують доступ до інтернету через шлюз Brume 3 із використанням обфускації VPN.

## Сценарій 2. Один маршрутизатор GL.iNet {#scenario-2-using-a-single-glinet-router}

У цьому сценарії один маршрутизатор GL.iNet **Brume 3 (GL-MT5000)** працює як клієнт VPN для підключення до сервера AmneziaVPN.

Власний сервер розгортати не потрібно. Завантажте файл конфігурації AmneziaWG з [офіційного вебсайту Amnezia](https://amnezia.org/){target="_blank"} або від провайдера VPN, який підтримує AmneziaWG, і завантажте файл на маршрутизатор GL.iNet. Після цього можна встановити з’єднання VPN з обфускацією.

### Завантаження конфігурації {#download-configuration}

<u>Варіант 1</u>: Завантажте конфігурацію з офіційного сайту Amnezia (потрібна підписка Premium).

1. Увійдіть у [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} за допомогою Subscription Key.

    ![Вхід у Amnezia Premium](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}

2. У панелі Amnezia відкрийте **Connection Assets** -> **Configuration Files**, виберіть країну та завантажте файл конфігурації на свій пристрій.

    ![Завантаження конфігурації Amnezia](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Варіант 2</u>: Завантажте конфігурацію від іншого провайдера VPN із підтримкою AmneziaWG.

Нижче наведено приклад для StarVPN.

1. Відкрийте [плани StarVPN](https://www.starvpn.com/#pricing){target="_blank"} і виберіть план VPN відповідно до потреб. Створіть обліковий запис StarVPN під час оформлення замовлення або [за цим посиланням](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

2. Увійдіть у [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"}, знайдіть **VPN Configuration** і натисніть **AmneziaWG Config**, щоб завантажити файл конфігурації.

    ![Завантаження AmneziaWG Config у StarVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. Конфігурація може містити IPv6-адресу. Щоб уникнути проблем сумісності та з’єднання, відкрийте файл .conf і видаліть IPv6-адресу, як показано нижче.

    ![Видалення IPv6-адреси з конфігурації StarVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Потім налаштуйте клієнт VPN за такими кроками.

### Налаштування клієнта VPN {#set-up-vpn-client_1}

1. Увійдіть у вебпанель адміністрування Brume 3.

    Підключіть пристрій, наприклад ноутбук або комп’ютер, до порту LAN Brume 3 кабелем Ethernet. Відкрийте браузер, уведіть адресу адміністрування за замовчуванням, зазвичай `192.168.8.1`, і ввійдіть за допомогою пароля адміністратора.

2. Завершіть початкове налаштування Brume 3 для доступу до інтернету.

3. Завантажте файл конфігурації.

    У меню ліворуч перейдіть до **VPN** > **WireGuard Client**. Додайте групу та задайте зрозумілу назву, наприклад AmneziaVPN.

    ![Створення групи AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}

    Праворуч завантажте отриманий файл конфігурації AmneziaVPN.

    ![Завантаження конфігурації AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}

    Після завантаження файла та успішної перевірки натисніть **Apply**.

    ![Перевірена конфігурація AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}

    Сторінка оновиться, а у списку відображатиметься один файл конфігурації.

4. Установіть з’єднання VPN.

    Натисніть значок із трьома крапками та виберіть **Start**.

    ![Запуск з’єднання AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}

    Зачекайте приблизно 1 хвилину. Якщо індикатор стану стане зеленим, з’єднання VPN успішне.

    ![Успішне з’єднання AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}

    Відкрийте **VPN Dashboard**. Ви побачите, що Brume 3 підключено до сервера AmneziaVPN.

    ![Стан підключення до AmneziaVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}

    З’єднання VPN налаштовано. Усі пристрої на Brume 3 тепер отримують доступ до інтернету через сервер AmneziaVPN із використанням обфускації VPN.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
