# ZeroTier {#zerotier}

ZeroTier — програмна віртуальна приватна мережа (VPN), яка забезпечує захищений і зашифрований обмін даними між пристроями через інтернет. Вона створює приватну віртуальну мережу, де пристрої можуть взаємодіяти так, наче перебувають в одній локальній мережі, незалежно від фізичного розташування та топології. ZeroTier проста в налаштуванні й використанні та підтримує наскрізне шифрування, сегментацію мережі й мережеві мости.

Функція ZeroTier на маршрутизаторах GL.iNet, доступна починаючи з прошивки v4.2, дає маршрутизатору змогу приєднатися до віртуальної мережі ZeroTier. Після підключення можна отримувати віддалений доступ до маршрутизатора, зокрема до ресурсів його WAN і LAN.

**Примітка**:

1. Не рекомендовано використовувати ZeroTier одночасно з такими функціями або службами: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, Tailscale, AstroWarp. Це може спричинити конфлікти маршрутизації.

2. Ця функція наразі перебуває в бета-тестуванні та може містити помилки.

3. Деякі моделі не підтримують ZeroTier через недостатній обсяг пам’яті, навіть із прошивкою v4.2 або новішою.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Моделі без підтримки"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Налаштування мережі ZeroTier {#set-up-zerotier-network}

Доступні дві версії ZeroTier Central: New Central і Legacy Central.

- **New Central**: Новіша версія ZeroTier Central зі зручнішим інтерфейсом і новими функціями. Рекомендована новим користувачам для найкращого досвіду роботи та доступу до найновіших інструментів.

- **Legacy Central**: Для облікових записів, створених до листопада 2025 року. Legacy Central і надалі підтримує наявних користувачів у керуванні їхніми мережами.

Обидві версії можна використовувати паралельно, проте прямого способу перенесення між ними наразі немає.

Виберіть відповідну версію, щоб продовжити.

### New Central {#new-central}

Нижче наведено приклад для GL-MT3600BE.

1. Відвідайте [офіційний вебсайт ZeroTier](https://www.zerotier.com/){target="_blank"} і ввійдіть в обліковий запис.

    ![Вхід у ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Створіть організацію.

    ![Створення організації ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Виберіть план. У цьому прикладі використовується Personal: 10 пристроїв, 1 адміністратор мережі та 1 мережа. Якщо потрібно створити більше мереж, додати більше пристроїв або власні маршрути та DNS, виберіть Essential або Scale.

    ![Вибір плану ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Мережу ZeroTier створено. Запишіть **Network ID** у верхньому правому куті — комбінацію з 16 літер і цифр. Він знадобиться для підключення інших пристроїв.

    ![Ідентифікатор мережі ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Увімкніть ZeroTier на маршрутизаторі GL.iNet.

    Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **ZeroTier**.

    Увімкніть ZeroTier, введіть Network ID на цій самій сторінці та натисніть **Apply**.

    ![Увімкнення ZeroTier на маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    За деякий час з’явиться повідомлення про потребу в авторизації. Натисніть посилання **ZeroTier Central**, щоб відкрити ZeroTier Central.

    ![Запит на авторизацію пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Авторизуйте пристрій у ZeroTier Central.

    У ZeroTier Central знайдіть пристрій зі станом Pending і авторизуйте його.

    ![Авторизація пристрою в ZeroTier Central](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Після авторизації сторінка матиме такий вигляд:

    ![Авторизований маршрутизатор](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Додайте інший пристрій (наприклад, комп’ютер або смартфон) до тієї самої мережі ZeroTier за [цією інструкцією](https://docs.zerotier.com/platforms/){target="_blank"}.

    Нижче наведено приклад для ноутбука з Windows 10 Pro.

    1. Установіть ZeroTier на ноутбук, завантаживши його [тут](https://www.zerotier.com/download/){target="_blank"}.

    2. Запустіть ZeroTier. Значок ZeroTier з’явиться в системному треї в нижньому правому куті робочого стола.

    3. Натисніть значок правою кнопкою миші, виберіть **Join New Network** і введіть **Network ID** із кроку 4 у спливному вікні.

        ![Підключення ноутбука до мережі ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Відкрийте ZeroTier Central, знайдіть пристрій зі станом Pending і авторизуйте його.

        ![Авторизація ноутбука](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Після авторизації сторінка матиме такий вигляд. Відображатимуться відомості про пристрої-учасники: **Device ID**, **Name**, **Status**, **Managed IP** і **Public IP**.

        ![Відомості про авторизовані пристрої](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Поради**: Натисніть значок із трьома крапками праворуч, щоб змінити налаштування пристрою-учасника, зокрема назву, Managed IP(s) і додаткові параметри.

8. Натисніть **Managed IP** маршрутизатора, щоб скопіювати її. Використовуйте цю Managed IP для доступу до маршрутизатора з ноутбука в тій самій мережі ZeroTier.

    ![Віртуальна IP-адреса ZeroTier маршрутизатора](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Перевірте з’єднання.

    На ноутбуці, підключеному до тієї самої мережі ZeroTier, відкрийте веббраузер і введіть Managed IP маршрутизатора з попереднього кроку.

    Якщо вебпанель адміністрування маршрутизатора доступна, з’єднання ZeroTier успішне.

    ![Вебпанель адміністрування через ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Також виконайте `ping` адреси Managed IP маршрутизатора з ноутбука для перевірки з’єднання. Успішна відповідь означає, що з’єднання ZeroTier встановлено.

    ![Перевірка з’єднання командою ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central {#legacy-central}

Нижче наведено приклад для GL-MT2500.

1. Створіть свою першу мережу ZeroTier.

    Скористайтеся офіційним [посібником із початку роботи ZeroTier](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"}, щоб створити обліковий запис і мережу ZeroTier. Запишіть Network ID — комбінацію з 16 літер і цифр, яка знадобиться для підключення інших пристроїв.

    ![Ідентифікатор мережі Legacy Central](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Увімкніть ZeroTier на маршрутизаторі GL.iNet.

    Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **ZeroTier**.

    Увімкніть ZeroTier, введіть Network ID на цій самій сторінці та натисніть **Apply**.

    ![Увімкнення ZeroTier на маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_enable.png){class="glboxshadow"}

    За деякий час з’явиться повідомлення про потребу в авторизації.

    Натисніть посилання **ZeroTier Central**, щоб відкрити ZeroTier Central.

    ![Консоль ZeroTier Central](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_central.png){class="glboxshadow"}

3. Авторизуйте пристрій у ZeroTier Central.

    У ZeroTier Central перейдіть до розділу **Members**. Знайдіть новий пристрій і позначте **Auth**, щоб авторизувати його. За потреби задайте власну назву пристрою.

    ![Авторизація учасника ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    За деякий час ZeroTier призначить пристрою **Managed IP**. Запишіть цю IP-адресу: вона знадобиться для перевірки.

    ![Призначена адреса Managed IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/managed_ip.png){class="glboxshadow"}

4. Додайте інший пристрій (наприклад, комп’ютер або смартфон) до тієї самої мережі ZeroTier за [цією інструкцією](https://docs.zerotier.com/platforms/){target="_blank"}.

5. Перевірте з’єднання.

    На іншому пристрої в тій самій мережі ZeroTier відкрийте веббраузер і введіть ZeroTier Managed IP маршрутизатора з попереднього кроку.

    Відкриється вебпанель адміністрування маршрутизатора.

    ![Вебпанель адміністрування через ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/web_admin_panel.png)

    Також можна перевірити з’єднання командою `ping`. Дивіться [короткий посібник ZeroTier](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"}.

## Віддалений доступ до WAN {#allow-remote-access-wan}

Якщо цей параметр увімкнено, ресурси з боку WAN пристрою доступні через віртуальну мережу ZeroTier.

Наприклад, у наведеній нижче топології після ввімкнення функції можна відкрити `GL-AXT1800` за його IP-адресою (`192.168.29.1`) з `leo-phone`. GL-AXT1800 — пристрій вищого рівня для `GL-MT2500`, а GL-MT2500 підключено до тієї самої мережі ZeroTier, що й leo-phone.

![Топологія віддаленого доступу до WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Примітка**: Для роботи цієї функції потрібно додати правила маршрутизації до мережі ZeroTier. У Legacy Central можна безкоштовно додати один власний маршрут. У New Central власні маршрути доступні лише з планом Essential або вищим. Докладніше дивіться [тут](https://www.zerotier.com/pricing/).

Наведені нижче дії показано на прикладі Legacy Central.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **ZeroTier**.

    Увімкніть **Allow Remote Access WAN** і натисніть **Apply**.

    ![Налаштування віддаленого доступу до WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    З’явиться запит на налаштування правил маршрутизації. Залиште цю сторінку відкритою або запишіть параметри маршруту (Destination і Via): вони знадобляться в наступному кроці.

    ![Налаштування віддаленого доступу до WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Відкрийте **ZeroTier Central** і знайдіть розділ **Advanced**.

    Уведіть параметри маршруту (Destination і Via) з попереднього кроку та натисніть **Submit**.

    ![Додавання маршруту ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_1.png){class="glboxshadow"}

    Після додавання маршруту розділ **Managed Routes** матиме такий вигляд:

    ![Додавання маршруту ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_2.png){class="glboxshadow"}

3. Тепер з інших пристроїв можна отримати доступ до `GL-AXT1800` за IP-адресою (`192.168.29.1`). Також доступні всі пристрої в підмережі `192.168.29.0/24`.

    ![Віддалений доступ до GL-AXT1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Віддалений доступ до LAN {#allow-remote-access-lan}

Якщо цей параметр увімкнено, ресурси з боку LAN пристрою доступні через віртуальну мережу ZeroTier.

Наприклад, у наведеній нижче топології після ввімкнення функції можна ввійти через SSH на `Ubuntu` за IP-адресою (`192.168.8.110`) з `leo-phone`. `Ubuntu` — пристрій нижчого рівня, підключений до `GL-MT2500`, а GL-MT2500 підключено до тієї самої мережі ZeroTier, що й leo-phone.

![Топологія віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Примітка**: Для роботи цієї функції потрібно додати правила маршрутизації до мережі ZeroTier. У Legacy Central можна безкоштовно додати один власний маршрут. У New Central власні маршрути доступні лише з планом Essential або вищим. Докладніше дивіться [тут](https://www.zerotier.com/pricing/).

Наведені нижче дії показано на прикладі Legacy Central.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **ZeroTier**.

    Увімкніть **Allow Remote Access LAN** і натисніть **Apply**.

    ![Налаштування віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    З’явиться запит на налаштування правил маршрутизації. Залиште цю сторінку відкритою або запишіть параметри маршруту (Destination і Via): вони знадобляться в наступному кроці.

    ![Налаштування віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Відкрийте **ZeroTier Central** і знайдіть розділ **Advanced**.

    Уведіть параметри маршруту (Destination і Via) з попереднього кроку та натисніть **Submit**.

    ![Додавання маршруту ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_3.png){class="glboxshadow"}

    Після додавання маршруту розділ **Managed Routes** матиме такий вигляд:

    ![Додавання маршруту ZeroTier](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/add_routes_4.png){class="glboxshadow"}

3. Тепер з інших пристроїв можна виконати ping або ввійти через SSH на `Ubuntu` за IP-адресою (`192.168.8.110`). Також доступні всі пристрої в підмережі `192.168.8.0/24`.

    ![Віддалений доступ до Ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
