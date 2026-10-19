# Як зарезервувати фіксовану IP-адресу клієнта OpenVPN у власному з’єднанні OpenVPN? {#how-to-reserve-a-fixed-ip-for-openvpn-client-in-a-self-built-openvpn-connection}

У цій інструкції описано, як зарезервувати фіксовану IP-адресу для клієнта OpenVPN, підключеного до вашого сервера. Перед виконанням наведених нижче кроків налаштуйте маршрутизатор GL.iNet як сервер OpenVPN.

1. Увійдіть до вебпанелі адміністрування сервера OpenVPN і на бічній панелі ліворуч перейдіть до **VPN** -> **OpenVPN Server**.

    На вкладці **Configuration** запишіть **IPv4 subnet** (наприклад, 10.8.0.0/24 на зображенні нижче) і змініть **Authentication Mode** на **Username and Password Only**.

    ![Конфігурація сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_config.png){class="glboxshadow"}

2. Перейдіть на вкладку **Users** і створіть ім’я користувача та пароль, як показано нижче.

    ![Користувачі OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_server_users.png){class="glboxshadow"}

3. Увійдіть до маршрутизатора через SSH і виконайте наведену нижче команду, щоб відкрити файл скрипту конфігурації сервера OpenVPN:

    `vi /lib/netifd/proto/openserver.sh`

    У відкритому файлі перевірте, чи є у скрипті рядок «*client-config-dir /etc/openvpn/ccd*».

    ![Перевірка рядка конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/check_config_line.png){class="glboxshadow"}

    Якщо його немає, додайте його вручну, збережіть файл і закрийте його.

4. Перейдіть до `/etc/openvpn/` і створіть каталог ccd командою `mkdir ccd`.

    ![Створення каталогу ccd](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/add_ccd_folder.png){class="glboxshadow"}

5. Перейдіть до `/etc/openvpn/ccd` і створіть файл «GLsupport», введіть `ifconfig-push 10.8.0.10 255.255.255.0`, збережіть файл і закрийте його.

    Перевірте вміст командою `cat GLsupport`.

    ![Команда ifconfig-push](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ifconfig-push.png){class="glboxshadow"}

    - Під час підключення до сервера OpenVPN з ім’ям GLsupport цьому користувачу GLsupport буде призначено фіксовану IP-адресу 10.8.0.10.

    - «255.255.255.0» — це маска підмережі. Її можна замінити маскою підмережі вашого сервера OpenVPN.

    **Примітка:** Щоб закріпити IP-адреси за кількома клієнтами OpenVPN, на кроці 2 створіть кілька імен користувачів і паролів. Потім повторіть крок 5: додайте до каталогу CCD файли для відповідних користувачів, наприклад user_1, user_2, user_3, із командою «ifconfig-push», відповідною фіксованою IP-адресою та маскою підмережі.

    Наприклад: `ifconfig-push 10.8.0.20 255.255.255.0`, `ifconfig-push 10.8.0.30 255.255.255.0`, `ifconfig-push 10.8.0.40 255.255.255.0`.

6. Перевірте підключення клієнта OVPN і переконайтеся, що **Client Virtual IP (IPv4)** відповідає зарезервованій адресі.

    Наприклад, якщо клієнт OpenVPN — це маршрутизатор GL.iNet, увійдіть до його вебпанелі адміністрування та перейдіть до **VPN Dashboard**, щоб перевірити **Client Virtual IP (IPv4)**.

    ![Перевірка клієнта OpenVPN у v4.7](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.7.png){class="glboxshadow"}
    <small>(VPN Dashboard у прошивці v4.7 і старіших версіях)</small>

    ![Перевірка клієнта OpenVPN у v4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/reserve_fixed_ip_for_ovpn_client/ovpn_client_test_4.8.png){class="glboxshadow"}
    <small>(VPN Dashboard у прошивці v4.8)</small>

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
