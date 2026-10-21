# Як налаштувати сервер OpenVPN на маршрутизаторах GL.iNet? {#how-to-set-up-openvpn-server-on-glinet-routers}

У цьому посібнику описано налаштування сервера OpenVPN на маршрутизаторі GL.iNet. Сервер VPN дає змогу встановлювати захищене з’єднання з домашньою або офісною мережею віддалено. На маршрутизаторі GL.iNet сервер OpenVPN можна налаштувати за кілька хвилин.

!!! note "Перед початком перевірте такі вимоги"

    **Публічна IP-адреса**

    Для налаштування сервера OpenVPN потрібна публічна IP-адреса. Перевірте її наявність за [цією інструкцією](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    **Перенаправлення портів**

    Якщо GL.iNet підключено за основним маршрутизатором, [налаштуйте перенаправлення портів на основному маршрутизаторі](how_to_set_up_port_forwarding.md).

## 1. Увійдіть у маршрутизатор {#1-log-in-to-your-router}

Відкрийте вебпанель адміністрування маршрутизатора у веббраузері (IP-адреса за замовчуванням: 192.168.8.1). Увійдіть за допомогою пароля адміністратора.

![Вхід у маршрутизатор](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Увімкніть Dynamic DNS (необов’язково) {#2-enable-dynamic-dns-optional}

Для налаштування сервера OpenVPN зазвичай потрібна **статична публічна IP-адреса**, яка забезпечує постійну адресу для доступу інших пристроїв до сервера VPN.

Якщо замість статичної публічної IP-адреси у вас динамічна, може знадобитися **Dynamic DNS (DDNS)** на маршрутизаторі GL.iNet. Це дає змогу зберігати доступ до сервера OpenVPN навіть після зміни публічної IP-адреси.

Щоб увімкнути Dynamic DNS, виконайте такі дії.

1. У вебпанелі адміністрування маршрутизатора перейдіть до **APPLICATIONS** > **Dynamic DNS**.
![Відкриття Dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Увімкніть **Enable DDNS**, прочитайте й прийміть **Terms of Service & Privacy Policy** та натисніть **Apply**.
![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Завантажте файл конфігурації {#3-download-configuration-file}

1. У вебпанелі адміністрування маршрутизатора перейдіть до **VPN** > **OpenVPN Server**.
2. Натисніть **Generate Configuration**.
3. Залиште налаштування за замовчуванням і натисніть **Export Client Configuration**.
![Експорт конфігурації клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. У спливному вікні ввімкніть **Use DDNS Domain**, якщо Dynamic DNS було налаштовано раніше.
5. Натисніть **Download** і збережіть файл.
6. Угорі сторінки **OpenVPN Server** натисніть **Start**.
![Запуск сервера OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Необов’язково) Для доступу до локальної мережі сервера VPN увімкніть такі параметри"

    Для прошивки v4.7 та раніших версій:

    1. У меню ліворуч виберіть **VPN** > **VPN Dashboard**.
    2. Натисніть значок Options.
    3. Увімкніть **Remote Access LAN**.
    4. Натисніть **Apply**.

        ![Дозвіл віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Для прошивки v4.8 та новіших версій:

    1. У меню ліворуч виберіть **VPN** > **OpenVPN Server**.
    2. Натисніть **Options** угорі праворуч.
    3. Увімкніть **Allow Remote Access the LAN Subnet**.
    4. Натисніть **Apply**.

        ![Дозвіл віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Підключіться до сервера OpenVPN {#4-connect-to-openvpn-server}

Для підключення до сервера OpenVPN потрібен клієнт OpenVPN. Налаштуйте його одним із наведених способів.

??? "Спосіб 1: сторонній застосунок OpenVPN (якщо немає додаткового маршрутизатора з підтримкою клієнта OpenVPN)"

    У прикладі використовується OpenVPN Connect — офіційний застосунок OpenVPN Inc.

    1. На іншому пристрої підключіться до іншої мережі Wi-Fi або до стільникової мережі, якщо це мобільний пристрій.
    2. Передайте отриманий файл конфігурації на пристрій, наприклад електронною поштою, і завантажте його на цей пристрій.
    3. Завантажте OpenVPN Connect для операційної системи пристрою:
        * [Windows](https://openvpn.net/client/)
        * [Mac](https://openvpn.net/client/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/client/)
    4. У застосунку прочитайте умови та виберіть **Agree**.
    5. Виберіть **Upload File**.
    ![Імпорт файла в OpenVPN Connect](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Виберіть **Browse** і отриманий файл конфігурації.
    7. Виберіть **OK**.
        ![Підтвердження імпорту конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Виберіть **Connect** > **OK** > **Allow**.

    Угорі профілю VPN з’явиться "Connected".
    ![Стан успішного підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Спосіб 2: маршрутизатор із підтримкою клієнта OpenVPN"

    Можна використовувати будь-який маршрутизатор із підтримкою ручного налаштування клієнта OpenVPN. У цьому прикладі використовується маршрутизатор GL.iNet для подорожей [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/).

    1. На іншому пристрої підключіться до іншої мережі Wi-Fi або до стільникової мережі, якщо це мобільний пристрій.
    2. Уведіть адресу панелі адміністрування маршрутизатора у веббраузері, наприклад 192.168.8.1.
    3. Уведіть пароль і натисніть **Login**.
    4. У меню ліворуч виберіть **VPN** > **OpenVPN Client**.
    ![Відкриття клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Натисніть **Add Manually**.
    ![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Уведіть назву в поле та натисніть значок позначки.
    7. Завантажте отриманий файл конфігурації.
    ![Вибір файла конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Натисніть **Apply**.
    9. Натисніть значок із трьома крапками та **Start**.
    10. Підключіть пристрій до маршрутизатора з клієнтом OpenVPN.

## 5. Перевірте з’єднання VPN {#5-verify-vpn-connection}

Відкрийте веббраузер і перевірте свою IP-адресу та місце розташування. Якщо вони відповідають IP-адресі й розташуванню сервера VPN, а не вашого інтернет-провайдера, з’єднання VPN успішне.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
