# Як налаштувати Drop-in Gateway на маршрутизаторі GL.iNet? {#how-to-set-up-drop-in-gateway-on-a-glinet-router}

Функція Drop-in Gateway від GL.iNet розширює можливості основного маршрутизатора, додаючи функції, яких він може не мати, зокрема AdGuard Home, зашифрований DNS і VPN. Основний маршрутизатор можна й надалі використовувати звичним способом, отримуючи додаткові можливості.

Увімкніть Drop-in Gateway для [всіх пристроїв](#enable-drop-in-gateway-for-all-devices) або [лише певних пристроїв](#enable-drop-in-gateway-for-specific-devices), підключених до основного маршрутизатора. Скористайтеся відповідним розділом.

**Примітка**: На моделях із прошивкою нижче v4.5.0 Drop-in Gateway можна ввімкнути лише для всіх пристроїв. Коли його ввімкнено, усі клієнтські пристрої підключаються через Drop-in Gateway: увесь їхній трафік спочатку обробляє цей маршрутизатор.

---

## Увімкнення Drop-in Gateway для всіх пристроїв {#enable-drop-in-gateway-for-all-devices}

### 1. Підключіть маршрутизатор GL.iNet до основного {#1-connect-glinet-router-to-the-main-router}

З’єднайте порт WAN маршрутизатора GL.iNet з портом LAN основного маршрутизатора кабелем Ethernet.

### 2. Увімкніть Drop-in Gateway {#2-enable-drop-in-gateway}

Є два способи ввімкнення Drop-in Gateway: через панель адміністрування маршрутизатора або мобільний застосунок GL.iNet.

??? "Через вебпанель адміністрування"

    1. У веббраузері відкрийте `192.168.8.1`.

    2. Уведіть пароль і натисніть **Login**.

    3. У меню ліворуч виберіть **Network** > **Drop-in Gateway**.

        ![Відкриття Drop-in Gateway у вебпанелі](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Увімкніть перемикач **Enable Drop-in Gateway Mode**.

    5. Виберіть **All devices are networked through drop-in gateway**.

        ![Увімкнення для всіх пристроїв](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Натисніть **Apply**.

??? "Через мобільний застосунок GL.iNet"

    **Примітка:** Перед початком установіть мобільний застосунок GL.iNet на пристрої.

    1. На головному екрані застосунку відкрийте вкладку **System** > **Drop-in Gateway**.

        ![Drop-in Gateway у мобільному застосунку](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Натисніть **Enable**.

    3. Для **Devices are networked via drop-in gateway** виберіть **All**.

        ![Вибір All у застосунку](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Натисніть **Done**.

### 3. Вимкніть DHCP-сервер основного маршрутизатора {#3-disable-dhcp-server-on-the-main-router}

Увійдіть в основний маршрутизатор і вимкніть DHCP-сервер. Скористайтеся інструкціями його виробника або зверніться до його служби підтримки.

### 4. Налаштуйте AdGuard, DNS, VPN та інші функції {#4-set-up-adguard-dns-vpn-and-other-features}

Скористайтеся цими посібниками, щоб увімкнути потрібні функції на маршрутизаторі GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Зашифрований DNS](../interface_guide/dns.md){target="_blank"}
* [Батьківський контроль](../interface_guide/parental_control.md){target="_blank"}
* [Клієнт WireGuard](../interface_guide/wireguard_client.md){target="_blank"}
* [Клієнт OpenVPN](../interface_guide/openvpn_client.md){target="_blank"}

---

## Увімкнення Drop-in Gateway для певних пристроїв {#enable-drop-in-gateway-for-specific-devices}

### 1. Підключіть маршрутизатор GL.iNet до основного {#1-connect-glinet-router-to-the-main-router_1}

З’єднайте порт WAN маршрутизатора GL.iNet з портом LAN основного маршрутизатора кабелем Ethernet.

### 2. Увімкніть Drop-in Gateway {#2-enable-drop-in-gateway_1}

Є два способи ввімкнення Drop-in Gateway: через [панель адміністрування маршрутизатора](#using-web-admin-panel) або [мобільний застосунок GL.iNet](#using-glinet-mobile-app).

??? "Через вебпанель адміністрування"

    <span id="using-web-admin-panel"></span>

    1. У веббраузері відкрийте `192.168.8.1`.

    2. Уведіть пароль і натисніть **Login**.

    3. У меню ліворуч виберіть **Network** > **Drop-in Gateway**.

        ![Відкриття Drop-in Gateway у вебпанелі](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Увімкніть перемикач **Enable Drop-in Gateway Mode**.

    5. Виберіть **Some devices select their own networking gateway**.

        ![Увімкнення для певних пристроїв](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Натисніть **Apply**.

    **Примітка:** НЕ закривайте цю вкладку. У наступному кроці знадобиться IP-адреса, показана на екрані.

??? "Через мобільний застосунок GL.iNet"

    <span id="using-glinet-mobile-app"></span>

    **Примітка:** Перед початком установіть мобільний застосунок GL.iNet на пристрої.

    1. На головному екрані застосунку відкрийте вкладку **System** > **Drop-in Gateway**.

        ![Drop-in Gateway у мобільному застосунку](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Натисніть **Enable**.

    3. Для **Devices are networked via drop-in gateway** виберіть **part**.

        ![Вибір part у застосунку](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Натисніть **Done**.

    **Примітка:** НЕ закривайте цю вкладку. У наступному кроці знадобиться IP-адреса, показана на екрані.

### 3. Налаштуйте шлюз і DNS на потрібному пристрої {#3-set-gateway-and-dns-on-specific-device}

??? "Windows"

    1. Підключіть пристрій до основного маршрутизатора.
    2. У Windows відкрийте **Settings** > **Network & Internet**.
    3. Виконайте дії відповідно до способу підключення:
        * Ethernet: Натисніть **Ethernet**.
        * Wi-Fi: Натисніть **Wi-Fi**, а потім назву мережі Wi-Fi.
    4. Скопіюйте IPv4-адресу. Біля **IP assignment** натисніть **Edit**.
    5. Натисніть **Manual**.
    6. Увімкніть **IPv4**.
    7. Уведіть такі відомості:
        * **IP address:** Вставте IP-адресу, скопійовану в кроці 4.
        * **Subnet mask:** Уведіть **255.255.255.0**.
        * **Gateway:** Уведіть IP-адресу зі сторінки **Drop-in Gateway**.
        * **Preferred DNS:** Уведіть IP-адресу зі сторінки **Drop-in Gateway**.
    8. Натисніть **Save**.

??? "Android"
    1. Підключіть пристрій до основного маршрутизатора.
    2. На Android відкрийте **Settings**.
    3. Натисніть **Connections** > **Wi-Fi**.
    4. Натисніть значок **Settings** біля поточної мережі.
    5. Натисніть **View more**.
    6. Натисніть **IP settings** > **Static**.
    7. Для **Gateway** і **DNS 1** введіть IP-адресу з екрана **Drop-in Gateway**.
    8. Натисніть **Save**.

??? "iOS"
    1. Підключіть пристрій до основного маршрутизатора.
    2. В iOS відкрийте **Settings**.
    3. Натисніть **Wi-Fi**.
    4. Натисніть поточну мережу Wi-Fi.
    5. У розділі **IPv4 Address** запишіть **IP Address** і **Subnet Mask**.
    6. Натисніть **Configure IP** > **Manual**.
    7. Уведіть такі відомості:
        * **IP Address:** Уведіть IP-адресу з кроку 5.
        * **Subnet Mask:** Уведіть маску підмережі з кроку 5.
        * **Router:** Уведіть IP-адресу з екрана **Drop-in Gateway**.
    8. Натисніть **Save**.
    9. Натисніть **Configure DNS**, а потім **Manual**.
    10. Натисніть **Add Server** і введіть IP-адресу з екрана **Drop-in Gateway**.
    11. Натисніть **Save**.

??? "Mac"
    1. Підключіть пристрій до основного маршрутизатора.
    2. На Mac натисніть значок Apple > **System Settings**.
    3. У меню ліворуч натисніть **Network**.
    4. Біля поточної мережі натисніть **Details**.
    5. Натисніть **TCP/IP**.
    6. Запишіть **IP Address** і **Subnet Mask**.
    7. Для **Configure IPv4** виберіть **Manually**.
    8. Уведіть такі відомості:
        * **IP address:** Уведіть IP-адресу з кроку 6.
        * **Subnet mask:** Уведіть маску підмережі з кроку 6.
        * **Router:** Уведіть IP-адресу зі сторінки **Drop-in Gateway**.
    9. Натисніть **OK** > **OK**.

### 4. Налаштуйте AdGuard, DNS, VPN та інші функції {#4-set-up-adguard-dns-vpn-and-other-features_1}

Скористайтеся цими посібниками, щоб увімкнути потрібні функції на маршрутизаторі GL.iNet.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Зашифрований DNS](../interface_guide/dns.md){target="_blank"}
* [Батьківський контроль](../interface_guide/parental_control.md){target="_blank"}
* [Клієнт WireGuard](../interface_guide/wireguard_client.md){target="_blank"}
* [Клієнт OpenVPN](../interface_guide/openvpn_client.md){target="_blank"}

---

Пов’язана стаття:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
