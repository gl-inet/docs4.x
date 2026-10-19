# Як налаштувати клієнт OpenVPN на маршрутизаторах GL.iNet? {#how-to-set-up-openvpn-client-on-glinet-routers}

У цьому посібнику описано налаштування клієнта OpenVPN на маршрутизаторах GL.iNet.

Перегляньте відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Перед початком переконайтеся, що маєте активну підписку провайдера VPN, який підтримує налаштування OpenVPN вручну. Перелік провайдерів OpenVPN, сумісних із GL.iNet, наведено [тут](https://www.gl-inet.com/solutions/vpn/){target="_blank"}.

Нижче наведено налаштування клієнта OpenVPN через вебпанель адміністрування маршрутизатора.

## 1. Увійдіть у маршрутизатор {#1-log-in-to-your-router}

Відкрийте вебпанель адміністрування маршрутизатора у веббраузері (IP-адреса за замовчуванням: 192.168.8.1). Увійдіть за допомогою пароля адміністратора.

![Вхід у маршрутизатор](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/router-login.jpeg){class="glboxshadow"}

## 2. Налаштуйте клієнт VPN {#2-set-up-vpn-client}

Скористайтеся розділом для вашого провайдера VPN.

??? "NordVPN"

    1. У вебпанелі адміністрування маршрутизатора перейдіть до **VPN** > **OpenVPN Client**.

    2. Натисніть **NordVPN**.

        ![Вибір NordVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-nordvpn.png){class="glboxshadow"}

    3. Уведіть облікові дані служби та натисніть **Save and Continue**.

        Примітка: Це НЕ електронна пошта та пароль для входу в обліковий запис. Потрібні облікові дані служби з вебсайту NordVPN -> Nord Dashboard.

        ![Збереження облікових даних служби](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-save-and-continue.png){class="glboxshadow"}

    4. У вікні виберіть місця розташування VPN, до яких потрібно підключатися, і натисніть **Apply**.

        ![Застосування конфігурації VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/nordvpn-servers-click-apply.png){class="glboxshadow"}

    5. Виберіть сервер VPN, натисніть значок із трьома крапками та **Start**.

        ![Запуск клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-start.png){class="glboxshadow"}

??? "Інші провайдери VPN (наприклад, Surfshark)"

    1. У вебпанелі адміністрування маршрутизатора перейдіть до **VPN** > **OpenVPN Client**.

    2. Натисніть **Add Manually**.

        ![Ручне додавання провайдера VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-add-manually.png){class="glboxshadow"}

    3. Задайте назву, наприклад назву провайдера VPN, і натисніть значок позначки.

        ![Підтвердження назви групи](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/click-check-icon.png){class="glboxshadow"}

    4. Переконайтеся, що завантажили файл конфігурації від провайдера VPN та облікові дані служби, якщо вони потрібні.
    5. Завантажте отриманий файл конфігурації.

        За потреби введіть облікові дані служби та натисніть **Apply**.

        ![Застосування конфігурації VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-click-apply.png){class="glboxshadow"}

    6. Біля адреси сервера VPN натисніть значок із трьома крапками та **Start**.

        ![Запуск клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_openvpn_client/openvpn-manual-click-start.png){class="glboxshadow"}

## 3. Перевірте з’єднання VPN {#3-verify-vpn-connection}

Відкрийте веббраузер і перевірте свою IP-адресу та місце розташування. Якщо вони відповідають IP-адресі й розташуванню сервера VPN, а не вашого інтернет-провайдера, з’єднання VPN успішне.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
