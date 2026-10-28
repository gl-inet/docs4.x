# Як отримати доступ до локальної мережі клієнта OpenVPN із боку сервера {#how-to-access-openvpn-client-lan-side-from-server}

У цій інструкції описано, як із боку сервера OpenVPN отримати доступ до локальної підмережі клієнта OpenVPN (наприклад, до NAS, IP-камери тощо).

## Топологія {#topology}

У наведеній нижче схемі GL-AXT1800 працює як сервер OpenVPN, а GL-MT2500 — як підключений до нього клієнт OpenVPN. Із боку сервера можна отримати доступ до пристроїв локальної мережі GL-MT2500 (наприклад, NAS або додаткового маршрутизатора GL-MT3000).

![Топологія мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ovpnlantop.jpg){class="glboxshadow"}

## 1. Додайте правило маршрутизації на сервері {#1-add-route-rule-on-server}

??? "Для прошивки v4.7 і старіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого сервера OpenVPN</u> і перейдіть до **VPN** -> **VPN Dashboard** -> **VPN Server**.

    Натисніть значок маршруту праворуч, щоб відкрити правило маршрутизації.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-1.jpg){class="glboxshadow"}

    У спливному вікні натисніть **Add Route Rule** праворуч і введіть підмережу, до якої потрібен доступ.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-2.png){class="glboxshadow"}

    Наприклад, локальна підмережа клієнта OpenVPN GL-MT2500 — **192.168.48.0/24**, тому **Target Address** — **192.168.48.0/24**.

    **Gateway** — це **Client IP**, яку сервер OpenVPN призначив цьому клієнту OpenVPN. У цьому прикладі встановіть **Gateway** на **10.8.0.1** і натисніть **Apply**.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Примітка: якщо потрібно отримати доступ до локальних підмереж кількох клієнтів OpenVPN, перед налаштуванням правил маршрутизації скористайтеся [цією інструкцією](reserve_fixed_IP_for_ovpn_client.md), щоб зарезервувати **Client IP** для кожного клієнта OpenVPN.

??? "Для прошивки v4.8"

    Увійдіть до вебпанелі адміністрування <u>свого сервера OpenVPN</u> і перейдіть до **VPN** -> **OpenVPN Server**.

    Відкрийте вкладку **Route Rules**, а потім натисніть **Add Route Rule** праворуч.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-1.png){class="glboxshadow"}

    У спливному вікні введіть підмережу, до якої потрібен доступ.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-2.png){class="glboxshadow"}

    Наприклад, локальна підмережа клієнта OpenVPN GL-MT2500 — **192.168.48.0/24**, тому **Target Address** — **192.168.48.0/24**.

    **Gateway** — це **Client IP**, яку сервер OpenVPN призначив цьому клієнту OpenVPN. У цьому прикладі встановіть **Gateway** на **10.8.0.2** і натисніть **Apply**.

    ![Правило маршрутизації сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-ovpn-route-rule-3.jpg){class="glboxshadow"}

    Примітка: якщо потрібно отримати доступ до локальних підмереж кількох клієнтів OpenVPN, перед налаштуванням правил маршрутизації скористайтеся [цією інструкцією](reserve_fixed_IP_for_ovpn_client.md), щоб зарезервувати **Client IP** для кожного клієнта OpenVPN.

## 2. Дозвольте віддалений доступ до локальної мережі клієнта {#2-allow-remote-access-to-client-lan}

??? "Для прошивки v4.7 і старіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта OpenVPN</u> і перейдіть до **VPN** -> **VPN Dashboard** -> **VPN Client**.

    Натисніть значок шестерні, щоб відкрити параметри клієнта.

    ![Параметри клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-client-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Remote Access LAN** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.7-allow-remote-access-lan.jpg){class="glboxshadow"}

??? "Для прошивки v4.8"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта OpenVPN</u> і перейдіть до **VPN** -> **VPN Dashboard**.

    Натисніть значок шестерні у верхньому лівому куті VPN-тунелю, щоб відкрити параметри тунелю.

    ![Параметри клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-client-tunnel-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.8-allow-remote-access-lan.png){class="glboxshadow"}

??? "Для прошивки v4.9 та новіших версій"

    Увійдіть до вебпанелі адміністрування <u>свого клієнта OpenVPN</u> і перейдіть до **VPN** -> **VPN Dashboard**.

    Натисніть значок шестерні у групі тунелів і виберіть **Options**.

    ![Параметри тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-tunnel-options.png){class="glboxshadow"}

    У спливному вікні ввімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

    ![Дозвіл віддаленого доступу до локальної мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/4.9-allow-remote-access-lan.png){class="glboxshadow" width=600}

## 3. Перевірте підключення {#3-test-connection}

Нижче наведено приклад доступу до GL-MT3000 (пристрою в локальній мережі клієнта OpenVPN) з IP-адресою **192.168.48.211**.

На пристрої, підключеному до сервера OpenVPN, виконайте ping до IP-адреси GL-MT3000 **192.168.48.211**. Це IP-адреса, яку клієнт OpenVPN (GL-MT2500) призначив GL-MT3000 у своїй локальній мережі.

Якщо ping успішний, налаштування правильні. Однак доступ до служб на цьому або інших пристроях у підмережі LAN клієнта OpenVPN також залежить від налаштувань міжмережевого екрана й конфігурації служб кожного пристрою.

![Перевірка ping](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_server-access_client_lan_side/ping-test.jpg){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
