# Як із клієнта отримати доступ до пристроїв LAN сервера WireGuard за доменними іменами? {#how-to-access-wireguard-server-lan-devices-from-the-client-via-domain-names}

У цьому посібнику описано доступ із клієнта до домашніх пристроїв у LAN сервера WireGuard, наприклад NAS або IP-камери, за доменними іменами.

## Топологія {#topology}

Як показано нижче, з комп’ютера в LAN клієнта можна отримати доступ до NAS та IP-камери в LAN сервера WireGuard за їхніми доменними іменами.

![Топологія доступу до LAN сервера за доменними іменами](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Кроки налаштування {#setup-steps}

### 1. Редагування правил хостів на сервері (необов’язково) {#1-edit-hosts-on-server-optional}

Цей крок потрібен, якщо сервер VPN не може правильно обробляти локальні доменні імена. Якщо ви не впевнені, пропустіть його.

Увійдіть у вебпанель адміністрування маршрутизатора сервера VPN та перейдіть до **NETWORK** -> **DNS** -> **Edit Hosts**.

![Редагування правил хостів на сервері](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Уведіть IP-адресу та доменне ім’я домашніх пристроїв, до яких потрібен доступ, і натисніть **Apply**.

![Уведення IP-адрес і доменних імен](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Дозвіл віддаленого доступу до LAN на сервері {#2-allow-remote-access-lan-on-server}

??? "Для маршрутизатора сервера з прошивкою v4.8"

    У вебпанелі адміністрування сервера перейдіть до **VPN** -> **WireGuard Server**. Натисніть **Options** угорі праворуч.

    ![Параметри сервера у прошивці 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.8.png){class="glboxshadow gl-90-desktop"}

    Увімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

    ![Дозвіл доступу до LAN у прошивці 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.8.png){class="glboxshadow"}

    **Коли ввімкнено, до цього маршрутизатора та пристроїв LAN можна отримати віддалений доступ через VPN.**

??? "Для маршрутизатора сервера з прошивкою v4.7 та ранішими версіями"

    У вебпанелі адміністрування сервера перейдіть до **VPN** -> **VPN Dashboard** -> розділу **VPN Server**. Натисніть значок шестірні праворуч від сервера WireGuard.

    ![Параметри сервера у прошивці 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server_options_4.7.png){class="glboxshadow gl-90-desktop"}

    Увімкніть **Remote Access LAN** і натисніть **Apply**.

    ![Дозвіл доступу до LAN у прошивці 4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/server-allow-access-lan-4.7.png){class="glboxshadow"}

    **Коли ввімкнено, до цього маршрутизатора та пристроїв LAN можна отримати віддалений доступ через VPN.**

### 3. Експорт конфігурації VPN {#3-export-vpn-configuration}

У панелі адміністрування сервера відкрийте **VPN** -> **WireGuard Server** -> вкладку **Profiles** і натисніть **Add**, щоб експортувати профіль конфігурації.

![Експорт конфігурації VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/export_config.png){class="glboxshadow"}

Ви отримаєте файл **.conf**, як показано нижче.

![Завантаження файла .conf](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/downloads.png){class="glboxshadow"}

Відкрийте файл. Переконайтеся, що поле DNS указує на IP-адресу тунелю сервера, яка відображається на вкладці **Configuration** сторінки WireGuard Server. Також видаліть "64.6.64.6" із поля DNS, якщо ця адреса є, щоб уникнути збою DNS-пошуку.

![Поле DNS у конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/dns_field.png){class="glboxshadow"}

![IP-адреса тунелю WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_tunnel_ip.png){class="glboxshadow"}

**Примітка**: IP-адреса тунелю сервера WireGuard залежить від версії прошивки. Перевірте адресу тунелю свого сервера.

### 4. Увімкнення сервера VPN {#4-enable-vpn-server}

На сторінці **WireGuard Server** натисніть кнопку **Start** угорі праворуч, щоб запустити сервер.

![Запуск сервера VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_server.png){class="glboxshadow"}

### 5. Завантаження конфігурації VPN {#5-upload-vpn-configuration}

Увійдіть у вебпанель адміністрування маршрутизатора клієнта VPN, перейдіть до **VPN** -> **WireGuard Client** і натисніть **Add Manually**.

![Ручне додавання конфігурації клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually.png){class="glboxshadow"}

Задайте назву групи та завантажте файл конфігурації.

![Ручне додавання конфігурації клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_manually-2.png){class="glboxshadow"}

Після успішного завантаження натисніть **Apply**.

![Застосування конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_apply.png){class="glboxshadow"}

Файл конфігурації з’явиться у списку.

![Конфігурація у списку](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wgclient_add_applied.png){class="glboxshadow"}

### 6. Установлення з’єднання клієнта VPN {#6-start-vpn-client-connection}

Натисніть значок із трьома крапками, щоб установити з’єднання VPN.

![Установлення з’єднання клієнта VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/start_client.png){class="glboxshadow"}

Коли сіра крапка стане зеленою, клієнт WireGuard успішно підключився до сервера.

![Клієнт WireGuard підключений](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/wg_client_connected.png){class="glboxshadow"}

Тепер з комп’ютера в LAN клієнта можна отримати доступ до домашніх пристроїв, наприклад NAS, у LAN сервера за доменними іменами.

![Перевірка доступу до NAS командою ping](https://static.gl-inet.com/docs/router/en/4/tutorials/access_server_lan_via_domain_names/ping_nas.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
