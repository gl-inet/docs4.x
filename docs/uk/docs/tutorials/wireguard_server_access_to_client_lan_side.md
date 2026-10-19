# Як отримати доступ до локальної мережі клієнта WireGuard із боку сервера {#how-to-access-wireguard-client-lan-side-from-server}

У цій інструкції описано, як із боку сервера WireGuard отримати доступ до локальної підмережі клієнта WireGuard (наприклад, до IP-камери, NAS тощо).

## Топологія {#topology}

У наведеній нижче схемі GL-MT2500 працює як сервер WireGuard, а GL-AXT1800 — як підключений до нього клієнт WireGuard. Із боку сервера можна отримати доступ до пристроїв локальної мережі GL-AXT1800, зокрема IP-камери або NAS.

![Топологія мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/Topology.jpg){class="glboxshadow"}

## 1. Додайте правило маршрутизації на сервері {#1-add-route-rule-on-server}

??? "Для прошивки v4.7 і старіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого сервера WireGuard</u> і перейдіть до **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Натисніть значок маршруту праворуч, щоб відкрити правило маршрутизації.

    ![Додавання правила маршрутизації](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-1.jpg){class="glboxshadow"}

    Натисніть **Add Route Rule** у верхньому правому куті та введіть підмережу, до якої потрібен доступ.

    ![Введення цільової підмережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-2.png){class="glboxshadow"}

    Наприклад, локальна підмережа клієнта WireGuard GL-AXT1800 — **192.168.8.0/24**, тому **Target Address** — **192.168.8.0/24**.

    **Gateway** — це IP-адреса клієнта, яку сервер WireGuard призначив цьому клієнту WireGuard. Її можна знайти на вкладці **Profiles** сторінки **WireGuard Server**. У наведеному нижче прикладі IP-адреса клієнта WireGuard GL-AXT1800 — **10.0.0.4**.

    ![IP-адреса клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-client-ip.png){class="glboxshadow"}

    Установіть **Gateway** на **10.0.0.4**, а **Scope** — на **global**, і натисніть **Apply**.

    ![Налаштування шлюзу маршруту](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-route-rule-3.jpg){class="glboxshadow"}

??? "Для прошивки v4.8"

    Увійдіть до вебпанелі адміністрування <u>свого сервера WireGuard</u> і перейдіть до **VPN** -> **WireGuard Server**.

    Відкрийте вкладку **Route Rules** і натисніть **Add Route Rule** праворуч.

    ![Додавання правила маршрутизації](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-1.png){class="glboxshadow"}

    У спливному вікні введіть підмережу, до якої потрібен доступ.

    ![Введення цільової підмережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-2.png){class="glboxshadow"}

    Наприклад, локальна підмережа клієнта WireGuard GL-AXT1800 — **192.168.8.0/24**, тому **Target Address** — **192.168.8.0/24**.

    **Gateway** — це IP-адреса клієнта, яку сервер WireGuard призначив цьому клієнту WireGuard. Її можна знайти на вкладці **Profiles** цієї сторінки. У наведеному нижче прикладі IP-адреса клієнта WireGuard GL-AXT1800 — **10.1.0.2**.

    ![IP-адреса клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-client-ip.png){class="glboxshadow"}

    Установіть **Gateway** на **10.1.0.2** і натисніть **Apply**.

    ![Налаштування шлюзу маршруту](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-route-rule-3.png){class="glboxshadow"}

## 2. Дозвольте віддалений доступ до локальної мережі клієнта {#2-allow-remote-access-to-client-lan}

??? "Для прошивки v4.7 і старіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта WireGuard</u> і перейдіть до **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Натисніть значок шестерні праворуч від WireGuard.

    ![Параметри клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-wgclient-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Remote Access LAN** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.7-allow-remote-access-lan.png){class="glboxshadow"}

??? "Для прошивки v4.8"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта WireGuard</u> і перейдіть до **VPN** -> **VPN Dashboard**.

    Натисніть значок шестерні у верхньому лівому куті VPN-тунелю, щоб відкрити параметри тунелю.

    ![Параметри VPN-тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-tunnel-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "Для прошивки v4.9 та новіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта WireGuard</u> і перейдіть до **VPN** -> **VPN Dashboard**.

    Натисніть значок шестерні у групі тунелів і виберіть **Options**.

    ![Параметри тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}

## 3. Перевірте підключення {#3-test-connection}

Перевірте, чи можете ви отримати доступ до пристроїв локальної мережі клієнта WireGuard із боку сервера.

З’єднання можна перевірити за допомогою ping. Наприклад, на пристрої, підключеному до сервера WireGuard (GL-MT2500), виконайте ping до IP-адреси пристрою в локальній мережі клієнта WireGuard (GL-AXT1800) і перевірте результат.

![Перевірка ping](https://static.gl-inet.com/docs/router/en/4/tutorials/wiregaurd_server_access_client_lan_side/ping.jpg){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
