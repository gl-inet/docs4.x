# Tailscale {#tailscale}

Tailscale — служба VPN, яка забезпечує безпечний і простий доступ до ваших пристроїв та застосунків із будь-якої точки світу. Докладніше дивіться на [офіційному вебсайті Tailscale](https://tailscale.com/){target="_blank"}.

Функція Tailscale на маршрутизаторах GL.iNet, доступна починаючи з прошивки v4.2, дає маршрутизатору змогу приєднатися до віртуальної мережі Tailscale. Після підключення можна отримувати віддалений доступ до маршрутизатора, зокрема до ресурсів його WAN і LAN.

**Примітка**:

1. Оскільки Tailscale працює на основі WireGuard, не рекомендовано використовувати її одночасно з такими функціями або службами: OpenVPN Client, WireGuard Client, GoodCloud Site to Site, ZeroTier, AstroWarp. Це може спричинити конфлікти маршрутизації.

2. Ця функція наразі перебуває в бета-тестуванні та може містити помилки.

3. Деякі моделі не підтримують Tailscale через недостатній обсяг пам’яті, навіть із прошивкою v4.2 або новішою.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Моделі без підтримки"
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

## Налаштування мережі Tailscale {#set-up-tailscale-network}

Нижче наведено приклад для GL-MT2500.

1. Прив’яжіть пристрої.

    Спочатку створіть обліковий запис Tailscale, а потім прив’яжіть до нього один або два пристрої (наприклад, смартфон чи ноутбук) для перевірки.

    Після прив’язування пристрої та їхній стан відображатимуться в консолі адміністрування Tailscale.

    ![Консоль адміністрування Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Увімкніть Tailscale на маршрутизаторі GL.iNet.

    Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **Tailscale**.

    ![Tailscale вимкнено на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Увімкніть Tailscale за допомогою перемикача та натисніть **Apply**.

    ![Увімкнення Tailscale на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. За деякий час з’явиться **Device Bind Link**. Натисніть Device Bind Link.

    ![Посилання прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    У спливному вікні з’явиться посилання Tailscale. Натисніть його, щоб перейти на вебсайт Tailscale, і ввійдіть в обліковий запис.

    ![Посилання прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Після входу підтвердьте пристрій, який потрібно підключити. Натисніть **Connect**.

    ![Підтвердження підключення пристрою Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Після успішного підключення відкриється консоль адміністрування Tailscale. У цьому прикладі IP-адреса GL-MT2500 — `100.88.54.21`. Тепер за цією адресою можна відкрити маршрутизатор.

    ![Консоль адміністрування Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Перевірте з’єднання.

    На пристроях, підключених до тієї самої мережі Tailscale, перевірте з’єднання одним із трьох способів.

    * Скористайтеся командою ping

        ![Перевірка з’єднання командою ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * Увійдіть на маршрутизатор через SSH

        ![Доступ до маршрутизатора через SSH](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Відкрийте вебпанель адміністрування

        ![Вебпанель адміністрування через Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Віддалений доступ до WAN {#allow-remote-access-wan}

**Примітка**: У прошивці v4.9 та новіших версіях цю функцію перейменовано на **Advertise WAN Subnets**.

Якщо цей параметр увімкнено, ресурси з боку WAN пристрою доступні через віртуальну мережу Tailscale. Маршрути набувають чинності лише після схвалення в консолі адміністрування Tailscale.

Наприклад, у наведеній нижче топології після ввімкнення параметра можна відкрити `GL-AXT1800` за його IP-адресою (`192.168.29.1`) з `leo-phone`. GL-AXT1800 — пристрій вищого рівня для `GL-MT2500`, а GL-MT2500 підключено до тієї самої мережі Tailscale, що й leo-phone.

![Топологія віддаленого доступу до WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Виконайте такі дії, щоб налаштувати цю функцію.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **Tailscale**.

    Увімкніть **Allow Remote Access WAN** і натисніть **Apply**.

    ![Увімкнення віддаленого доступу до WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Відкрийте консоль адміністрування Tailscale. З’явиться сповіщення, що GL-MT2500 має підмережі.

    Натисніть значок із трьома крапками праворуч від GL-MT2500 і виберіть **Edit route settings**.

    ![Сповіщення про підмережі Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Увімкніть маршрути підмереж.

    ![Увімкнення маршрутів підмереж Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Тепер з інших пристроїв можна отримати доступ до GL-AXT1800 за IP-адресою (`192.168.29.1`). Також доступні всі пристрої в підмережі `192.168.29.0/24`.

    ![Віддалений доступ до GL-AXT1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Віддалений доступ до LAN {#allow-remote-access-lan}

**Примітка**: У прошивці v4.9 та новіших версіях цю функцію перейменовано на **Advertise LAN Subnets**.

Якщо цей параметр увімкнено, ресурси з боку LAN пристрою доступні через віртуальну мережу Tailscale. Маршрути набувають чинності лише після схвалення в консолі адміністрування Tailscale.

Наприклад, у наведеній нижче топології після ввімкнення параметра можна ввійти через SSH на `Ubuntu` за його IP-адресою (`192.168.8.110`) з `leo-phone`. `Ubuntu` — пристрій нижчого рівня, підключений до `GL-MT2500`, а GL-MT2500 підключено до тієї самої мережі Tailscale, що й leo-phone.

![Топологія віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Виконайте такі дії, щоб налаштувати цю функцію.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **Tailscale**.

    Увімкніть **Allow Remote Access LAN** і натисніть **Apply**.

    ![Увімкнення віддаленого доступу до LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Відкрийте консоль адміністрування Tailscale. З’явиться сповіщення, що GL-MT2500 має підмережі.

    Натисніть значок із трьома крапками праворуч від GL-MT2500 і виберіть **Edit route settings**.

    ![Сповіщення про підмережі Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Увімкніть маршрути підмереж.

    ![Увімкнення маршрутів підмереж LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Тепер з інших пристроїв можна виконати ping або ввійти через SSH на Ubuntu за IP-адресою (`192.168.8.110`). Також доступні всі пристрої в підмережі `192.168.8.0/24`.

    ![Віддалений доступ до Ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Власні вихідні вузли {#custom-exit-nodes}

За замовчуванням Tailscale працює як накладена мережа: вона маршрутизує лише трафік між пристроями, на яких працює Tailscale, і не обробляє трафік публічного інтернету, наприклад під час перегляду вебсайтів на кшталт Google.

Однак іноді потрібно спрямувати трафік публічного інтернету через Tailscale. Наприклад, якщо ви перебуваєте поза домом або подорожуєте за кордоном і потребуєте доступу до онлайн-служб (зокрема банківських), доступних лише у вашій країні, налаштуйте домашній комп’ютер із публічною IP-адресою як вихідний вузол. На інших пристроях тієї самої мережі Tailnet, наприклад GL-AXT1800 і GL-MT3000 на зображенні нижче, налаштуйте передавання трафіку через нього. Тоді весь трафік публічного інтернету пересилатиметься через вихідний вузол.

![Топологія власного вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Коли весь трафік спрямовується через вихідний вузол, використовуються маршрути за замовчуванням (0.0.0.0/0, ::/0), аналогічно звичайному з’єднанню VPN.

Вихідний вузол спрямовує вихідний інтернет-трафік пристроїв мережі Tailnet, фактично діючи як сервер VPN. Коли пристрій підключено до вихідного вузла, весь його інтернет-трафік поза Tailscale виглядає так, наче походить із місця розташування цього вузла. Це допомагає отримати доступ до вмісту з географічними обмеженнями та підвищити конфіденційність в інтернеті. Пристрій, який пересилає такий трафік, називається вихідним вузлом (exit node).

**Примітка**: Якщо DNS-сервер маршрутизатора має приватну IP-адресу, доступну лише в локальній мережі, під час використання вихідного вузла можна втратити доступ до інтернету. Щоб усунути проблему, увійдіть у маршрутизатор, перейдіть до **NETWORK** -> **DNS** і вручну задайте публічний DNS-сервер, наприклад 8.8.8.8.

---

У цьому прикладі маршрутизатор GL.iNet **GL-MT2500** і **Leo-Desktop** перебувають в одній мережі Tailnet.

Виконайте наведені нижче дії, щоб налаштувати Leo-Desktop як вихідний вузол. Інший спосіб налаштування власного вихідного вузла описано в розділі [Маскарадинг IP](#ip-masquerading).

1. Увімкніть маршрути підмереж GL-MT2500 у консолі адміністрування Tailscale.

    Відкрийте консоль адміністрування Tailscale, натисніть значок із трьома крапками праворуч від GL-MT2500 і виберіть **Edit route settings**.

    ![Редагування маршрутів Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    У спливному вікні ввімкніть маршрути підмереж.

    ![Увімкнення маршрутів підмереж Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. На пристрої, який використовуватиметься як вихідний вузол (у цьому прикладі Leo-Desktop), виберіть **Run exit node**. Нижче наведено приклад для Windows.

    ![Запуск вихідного вузла у Windows](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Потім натисніть **Yes**.

    ![Підтвердження запуску вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. У консолі адміністрування Tailscale налаштуйте Leo-Desktop як вихідний вузол.

    ![Редагування маршрутів Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![Дозвіл використання вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Увійдіть у вебпанель адміністрування GL-MT2500, перейдіть до **APPLICATIONS** -> **Tailscale** та ввімкніть **Custom Exit Nodes**. Натисніть кнопку оновлення, виберіть IP-адресу Leo-Desktop із розкривного списку та натисніть **Apply**.

    ![Вибір власного вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Підключені до маршрутизатора пристрої спрямовуватимуть свій трафік через вихідний вузол для доступу до інтернету. Весь інтернет-трафік виглядатиме так, наче походить із місця розташування вихідного вузла.

5. **Усунення несправностей**: Якщо після ввімкнення Custom Exit Node підключені до маршрутизатора GL.iNet пристрої не мають доступу до інтернету, перевірте, чи ввімкнено маршрути підмереж маршрутизатора в консолі адміністрування Tailscale.

    У вебпанелі адміністрування маршрутизатора може з’явитися відповідне повідомлення, як показано нижче.

    ![Повідомлення про налаштування маршрутів підмереж](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Щоб усунути проблему, увімкніть маршрути підмереж маршрутизатора в консолі адміністрування Tailscale, як описано в **кроці 1** вище.

## Запуск вихідного вузла {#run-exit-node}

**Примітка**: Ця функція з’явилася у прошивці v4.9.

Запуск вихідного вузла на маршрутизаторі дає іншим пристроям мережі Tailnet змогу спрямовувати весь вихідний інтернет-трафік через публічну IP-адресу цього маршрутизатора.

У наведеній нижче топології ноутбук розташований у Бостоні, а маршрутизатор GL-BE9300 — у Гонконгу. Обидва пристрої додано до однієї мережі Tailscale Tailnet. Якщо налаштувати GL-BE9300 як вихідний вузол, увесь вихідний трафік ноутбука проходитиме через цей маршрутизатор у Гонконгу для доступу до інтернету. Зовнішня публічна IP-адреса ноутбука буде гонконзькою замість бостонської.

![Топологія вихідного вузла в Гонконгу](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Порада**: Рекомендуємо скасувати обмеження терміну дії ключа вихідного вузла, щоб уникнути переривання з’єднання після завершення терміну дії ключа автентифікації вузла.*

Виконайте наведені нижче дії, щоб налаштувати GL-BE9300 як вихідний вузол.

1. Додайте GL-BE9300 і ноутбук для подорожей до однієї мережі Tailscale Tailnet.

    ![Пристрої однієї мережі Tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. У вебпанелі адміністрування GL-BE9300 увімкніть **Run Exit Node** і натисніть **Apply**.

    ![Увімкнення вихідного вузла на маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. Відкрийте консоль адміністрування Tailscale. Під GL-BE9300 з’явиться позначка "Exit Node".

    ![Позначка вихідного вузла в Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Натисніть значок із трьома крапками праворуч від GL-BE9300 і виберіть **Edit route settings**.

    ![Редагування маршрутів вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. У спливному вікні позначте **Use as exit node** і натисніть **Save**.

    ![Дозвіл використання як вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Скасуйте обмеження терміну дії ключа.

    З міркувань безпеки користувачі мають періодично повторно проходити автентифікацію на кожному пристрої. Щоб уникнути переривання з’єднання після завершення терміну дії ключа автентифікації вихідного вузла, рекомендуємо скасувати обмеження терміну дії ключа для цього вузла. Докладніше про термін дії ключів дивіться [тут](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"}.

    Натисніть значок із трьома крапками праворуч від GL-BE9300 і виберіть **Disable key expiry**.

    ![Скасування обмеження терміну дії ключа](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    Після застосування під GL-BE9300 з’явиться позначка "Expiry disabled".

    ![Позначка скасованого обмеження терміну дії ключа](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Виберіть GL-BE9300 як вихідний вузол для ноутбука, яким користуєтеся в подорожі.

    Запустіть Tailscale на ноутбуці. Значок Tailscale з’явиться в системному треї в нижньому правому куті.

    Натисніть значок правою кнопкою миші, виберіть **Exit nodes**, а потім **gl-be9300**.

    ![Вибір вихідного вузла на ноутбуці](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    Тепер увесь вихідний трафік цього ноутбука проходитиме через GL-BE9300 для доступу до інтернету.

8. Перевірте з’єднання.

    1. На ноутбуці відкрийте веббраузер і перейдіть на [ipcheck.ing](https://ipcheck.ing/){target="_blank"} або інший вебсайт перевірки IP-адреси. На сторінці відобразиться публічна IP-адреса вихідного вузла Tailscale. Це підтверджує, що ноутбук отримує доступ до інтернету через вихідний вузол (у цьому прикладі GL-BE9300 у Гонконгу).

        ![Публічна IP-адреса вихідного вузла в Гонконгу](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Натисніть `Win+R`, уведіть `cmd`, щоб відкрити командний рядок, і виконайте `tracert google.com` для відстеження маршруту вихідного трафіку. Результат команди містить усі переходи маршруту інтернет-трафіку. За правильного налаштування перший зовнішній перехід проходитиме через вихідний вузол, як показано нижче, підтверджуючи, що весь вихідний інтернет-трафік проходить через цей маршрутизатор.

        ![Відстеження маршруту командою tracert через вихідний вузол](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Відключіть вихідний вузол для порівняння.

        Натисніть значок Tailscale в системному треї в нижньому правому куті правою кнопкою миші, виберіть **Exit nodes**, а потім **None**, щоб припинити використання вихідного вузла.

        ![Відключення вихідного вузла для порівняння](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Відкрийте нову вкладку браузера та перейдіть на [ipcheck.ing](https://ipcheck.ing/){target="_blank"} або інший сервіс перевірки IP-адреси. Тепер відображатиметься власна публічна IP-адреса ноутбука. Це підтверджує використання локального з’єднання з інтернетом (у цьому прикладі — у Бостоні).

        ![Локальна публічна IP-адреса в Бостоні](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}


Докладніше дивіться [Вихідні вузли (маршрутизація всього трафіку)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}.

## Маскарадинг IP {#ip-masquerading}

**Примітка**: Ця функція з’явилася у прошивці v4.9.

Маскарадинг IP — механізм підміни мережевих адрес. Якщо ввімкнути цей параметр на маршрутизаторі, IP-адреси джерела пакетів від клієнтів LAN автоматично замінюються IP-адресою інтерфейсу Tailscale маршрутизатора. Тому інші вузли мережі Tailscale сприйматимуть увесь трафік, пересланий маршрутизатором підмережі, як трафік самого маршрутизатора, а не початкового клієнта LAN.

Маскарадинг IP рекомендовано використовувати в таких сценаріях:

- Під час налаштування власного вихідного вузла, якщо ви не хочете налаштовувати маршрути підмереж у консолі адміністрування Tailscale та прагнете простішого пересилання всього клієнтського трафіку через маршрутизатор.

- Якщо на пристроях LAN неможливо встановити Tailscale, але їм потрібен доступ до мереж Tailscale через маршрутизатор.

У наведеному нижче прикладі маршрутизатори GL.iNet GL‑BE9300 і GL-MG1300 перебувають в одній мережі Tailnet.

![Пристрої однієї мережі Tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailnet.png){class="glboxshadow"}

Виконайте наведені нижче дії, щоб налаштувати **власний вихідний вузол** на GL‑BE9300.

1. Увійдіть у вебпанель адміністрування GL-BE9300, перейдіть до **APPLICATIONS** -> **Tailscale**, увімкніть **IP Masquerading** і натисніть **Apply**.

    ![Увімкнення маскарадингу IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ip_masquerading.png){class="glboxshadow"}

    Коли IP Masquerading увімкнено, маршрути підмереж не потрібно налаштовувати в консолі адміністрування Tailscale. Клієнти LAN, підключені до маршрутизатора, можуть отримувати доступ до мережі Tailscale безпосередньо через віртуальну IP-адресу Tailscale маршрутизатора.

    У цьому прикладі GL-BE9300 (100.115.61.35) і GL-MG1300 (100.113.50.89) мають віртуальні IP-адреси Tailscale. Якщо комп’ютер підключено до GL‑BE9300, він може безпосередньо відкрити вебпанель адміністрування GL‑MG1300 через IP-адресу інтерфейсу Tailscale маршрутизатора GL‑BE9300.

    ![Перевірка доступу з маскарадингом IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/test_ip_masquerading.png){class="glboxshadow"}

2. Виберіть пристрій, який використовуватиметься як вихідний вузол (у цьому прикладі GL-MG1300), та ввімкніть **Run exit node**.

    ![Запуск GL-MG1300 як вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_1.png){class="glboxshadow" width=600}

    Потім натисніть **Apply**.

    ![Застосування налаштувань вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node_2.png){class="glboxshadow"}

3. У консолі адміністрування Tailscale налаштуйте GL-MG1300 як вихідний вузол.

    ![Налаштування вихідного вузла в Tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_1.png){class="glboxshadow"}

    ![Дозвіл використання GL-MG1300 як вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_exit_node_2.png){class="glboxshadow" width=500}

    Щоб уникнути переривання з’єднання після завершення терміну дії ключа автентифікації вихідного вузла, увімкніть **Disable Key Expiry**.

    ![Скасування обмеження терміну дії ключа GL-MG1300](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_1.png){class="glboxshadow"}

    ![Позначка скасованого обмеження терміну дії ключа GL-MG1300](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/disable_key_expiry_2.png){class="glboxshadow"}

4. Поверніться до вебпанелі адміністрування GL-BE9300, перейдіть до **APPLICATIONS** -> **Tailscale** та ввімкніть **Custom Exit Nodes**. Натисніть кнопку оновлення, виберіть IP-адресу GL-MG1300 із розкривного списку та натисніть **Apply**.

    ![Вибір GL-MG1300 як власного вихідного вузла](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes_1.png){class="glboxshadow"}

Після налаштування пристрої, підключені до маршрутизатора GL-BE9300, спрямовуватимуть свій трафік через вихідний вузол GL-MG1300 для доступу до інтернету. Весь інтернет-трафік виглядатиме так, наче походить із місця розташування вихідного вузла.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
