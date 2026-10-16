# Налаштування клієнта WireGuard на маршрутизаторах GL.iNet {#set-up-wireguard-client-on-glinet-routers}

Вміст цієї сторінки ґрунтується на прошивці v4.6 і попередніх версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.6 і попередні версії" markdown="1">

- [Прошивка v4.7 і новіші версії](wireguard_client.md)

</div>

---

WireGuard® — простий, швидкий і сучасний VPN, який використовує сучасні криптографічні технології. Його мета — працювати швидше, простіше й ефективніше за IPsec, бути кориснішим і не створювати зайвих складнощів. Він також має на меті забезпечити значно вищу продуктивність, ніж OpenVPN.

Якщо у вас уже є підписка на WireGuard, але ви не знаєте, як отримати файли конфігурації, див. [отримання файлів конфігурації від провайдерів WireGuard](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) або зверніться до служби підтримки провайдера.

Клієнт WireGuard можна налаштувати через вебпанель адміністрування або [мобільний застосунок](../faq/mobile_app.md).

- У мобільний застосунок інтегровано кількох провайдерів WireGuard, зокрема AzireVPN, Mullvad, OVPN, StrongVPN і PIA VPN.

- Вебпанель адміністрування підтримує менше провайдерів WireGuard, наприклад AzireVPN і Mullvad, але надає наочніші й докладніші сторінки налаштування.

Нижче описано налаштування через вебпанель адміністрування.

---

Увійдіть у вебпанель адміністрування та відкрийте **VPN** -> **WireGuard Client**.

Якщо у вас є підписка **AzireVPN** або **Mullvad**, увійдіть безпосередньо зі своїми обліковими даними. Інакше натисніть **Add Manually**, щоб завантажити профілі WireGuard вручну.

![Початкове налаштування клієнта WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Налаштування AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} — VPN-сервіс, орієнтований на конфіденційність, який надає захищені, сучасні й надійні тунелі, зокрема WireGuard.

![Налаштування AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Введіть **Username** і **Password** та натисніть **Save Credentials & Get Servers**. Буде створено файли конфігурації для кожного сервера.

    ![Профілі AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Відкрийте VPN Dashboard, щоб увімкнути з’єднання.

    ![AzireVPN на панелі VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Після підключення відобразяться ваша IP-адреса та кількість надісланих і отриманих байтів.

    ![З’єднання AzireVPN на панелі VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Оновіть список серверів.

    Деякі сервери AzireVPN можуть бути вимкнені або перебувати на технічному обслуговуванні, що спричиняє збої підключення. Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів.

    ![Оновлення серверів AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Змініть облікові дані.

    Натисніть піктограму шестерні, щоб змінити облікові дані.

    ![Зміна облікових даних AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

5. Видалення

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням.

    ![Видалення всіх конфігурацій AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_delete_all_configuration_file.png){class="glboxshadow"}

## Налаштування Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} — VPN-сервіс, який допомагає зберігати конфіденційність вашої активності в інтернеті, особи та розташування.

У прошивку 4.x інтегровано сервіс Mullvad WireGuard.

![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Введіть **Account** і натисніть **Save Credentials & Get Servers**.

    Номер облікового запису Mullvad — 16-значне десяткове число в діапазоні від «1000 0000 0000 0000» до «9999 9999 9999 9999».

    З’явиться вікно вибору розташування.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Буде створено файли конфігурації сервера вибраного розташування.

    **Public Key** — публічний ключ WireGuard, який передається серверу Mullvad. Одночасно можна мати до п’яти ключів. Керуйте ключами WireGuard на [сторінці Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Відкрийте VPN Dashboard, щоб увімкнути з’єднання.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Після підключення відобразяться ваша IP-адреса та кількість надісланих і отриманих байтів.

    ![З’єднання Mullvad на панелі VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Оновіть список серверів.

    Деякі сервери Mullvad можуть бути вимкнені або перебувати на технічному обслуговуванні, що спричиняє збої підключення. Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Змініть облікові дані.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Видаліть дані облікового запису.

    Натисніть **Delete**, щоб видалити облікові дані, приватний і публічний ключі та файли конфігурації **на маршрутизаторі**.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Видаліть конфігурації.

    Можна видалити всі файли конфігурації одним натисканням. Також з’явиться запит на видалення приватного й публічного ключів.

    ![Налаштування Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Налаштування клієнта WireGuard {#set-up-wireguard-client}

Починаючи з прошивки 4.0, профілі WireGuard можна об’єднувати в групи для керування.

1. Натисніть **Add Manually**.

    ![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Буде створено групу.

    ![Додавання групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Задайте зрозумілу назву групи, наприклад azirevpn. Потім виберіть завантаження файлів конфігурації або ручне додавання конфігурації.

    ![Назва нової групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Завантажте файли конфігурації**.

        Завантажте файл конфігурації WireGuard і натисніть **Apply**.

        ![Завантаження профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![Завантажений профіль](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration** дозволяє вставити конфігурацію WireGuard або заповнити кожен параметр окремо.

        ![Текстова конфігурація WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Задайте зрозумілу назву та вставте конфігурацію. Натисніть **Apply**, щоб продовжити.

        ![Текстова конфігурація WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Щоб додати конфігурацію, заповнюючи окремі параметри, натисніть **Item Mode**.

        ![Конфігурація WireGuard за окремими параметрами](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![Конфігурація WireGuard за окремими параметрами](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Натисніть піктограму з трьома крапками, щоб запустити, змінити або видалити профіль.

    ![Дії з профілем](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Перевірте стан з’єднання на [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![Панель VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® — зареєстрована торговельна марка Jason A.Donenfeld.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
