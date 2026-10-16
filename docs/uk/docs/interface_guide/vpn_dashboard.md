# Панель VPN {#vpn-dashboard}

Вміст цієї сторінки ґрунтується на прошивці v4.9.x та новіших версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.9 та новіші версії" markdown="1">

- [Прошивка v4.7 і попередні версії](vpn_dashboard_v4.7.md)
- [Прошивка v4.8](vpn_dashboard_v4.8.md)

</div>

---

У лівому меню вебпанелі адміністрування відкрийте **VPN** -> **VPN Dashboard**.

На VPN Dashboard відображаються відомості про з’єднання VPN: правила маршрутизації, підключений сервер, статистика трафіку, віртуальна IP-адреса клієнта та журнал з’єднання. Також можна налаштувати додаткові параметри, зокрема аварійне блокування VPN (Kill Switch), маскарадинг IP та MTU.

Порівняно з прошивкою v4.8, у v4.9 до VPN Dashboard додано такі поліпшення:

1. **Можна вибрати кілька профілів у групі тунелів і задати їхній пріоритет**. Тунель намагатиметься підключитися за допомогою кожного профілю в порядку пріоритету, доки з’єднання не буде встановлено.

2. **Кожна група тунелів працює незалежно, без аварійного перемикання між групами**. Якщо жоден профіль одного тунелю не зможе підключитися, система визначатиме, чи переходити на локальний WAN, відповідно до стану Kill Switch тунелю та налаштувань тунелю All Other Traffic.

## Завантаження профілю VPN {#upload-vpn-profile}

Якщо під час першого відкриття сторінки ще не створено жодного тунелю, вона має такий вигляд. Натисніть **Add VPN Tunnel**, щоб почати налаштування.

![Додавання тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Відкриється сторінка **VPN Client Profile**. Виберіть VPN-провайдера та увійдіть.

![Вибір VPN-провайдера](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. VPN-провайдери, показані на зображенні вище, інтегровані у вебпанель адміністрування маршрутизатора GL.iNet. За наявності активної підписки введіть облікові дані, щоб увійти та отримати файли конфігурації VPN.

    2. Якщо у вас підписка на іншого провайдера або потрібно використати власні конфігурації VPN, натисніть **Add Manually** і завантажте їх.

У цьому прикладі використано [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Натисніть PureVPN та увійдіть із дійсними обліковими даними.

![Вхід до PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![Облікові дані PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Відобразиться список профілів VPN. Деякі VPN-провайдери спочатку пропонують вибрати протокол VPN або потрібні сервери чи міста.

![Профілі PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Натисніть **Go to Dashboard** унизу. Відкриється VPN Dashboard для додавання тунелю та налаштування політик VPN.

<span id="set-up-vpn-policy"></span>

## Додавання тунелю VPN {#add-vpn-tunnel}

### Загальна послідовність дій {#general-steps}

Виконайте наведені нижче дії, щоб додати тунель VPN і налаштувати політики VPN. За потреби див. [приклади налаштування](#case-reference).

1. На VPN Dashboard натисніть **Add VPN Tunnel**. Праворуч відкриється майстер налаштування VPN.

    ![Додавання тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Виберіть профіль VPN.

    Виберіть один або кілька профілів, за потреби змініть їхній пріоритет праворуч і натисніть **Next**.

    ![Вибір профілю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Примітка**: якщо вибрано кілька профілів, тунель намагатиметься підключитися за допомогою кожного з них у порядку пріоритету, доки з’єднання не буде встановлено. Якщо жоден профіль у межах одного тунелю не зможе підключитися, система визначатиме, чи переходити на локальну мережу маршрутизатора (WAN), відповідно до стану Kill Switch у [параметрах тунелю](#tunnel-options) і налаштувань [All Other Traffic](#all-other-traffic).

3. Виберіть джерело клієнтського трафіку та натисніть **Next**.

    Доступні чотири варіанти:

    - **All Clients**: трафік усіх пристроїв відповідатиме цьому правилу.
    ![Усі клієнти](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: трафік із зазначених типів підключення (наприклад, підмережі LAN, Drop-in Gateway, Guest Network) відповідатиме цьому правилу.
    ![Зазначені типи підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: трафік зазначених пристроїв, визначених за MAC-адресами, відповідатиме цьому правилу.
    ![Зазначені пристрої](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: трафік зазначених пристроїв, визначених за MAC-адресами, не відповідатиме цьому правилу.
    ![Виключення зазначених пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Виберіть призначення трафіку та натисніть **Apply**.

    Доступні три варіанти:

    - **All Targets**: трафік, що відповідає цьому правилу, маршрутизуватиметься до всіх адрес призначення.
    ![Усі адреси призначення](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: трафік, що відповідає цьому правилу, маршрутизуватиметься до зазначених доменів або IP-адрес. Їх потрібно ввести вручну.
    ![Зазначені домени та IP-адреси](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: трафік, що відповідає цьому правилу, не маршрутизуватиметься до зазначених доменів або IP-адрес. Їх потрібно ввести вручну.
    ![Виключення зазначених доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Тунель VPN успішно додано. Відкриється **VPN Dashboard**. За потреби додайте інші тунелі VPN.

    З міркувань безпеки перед увімкненням тунелю VPN перевірте стан **Kill Switch** у розділах [увесь інший трафік](#all-other-traffic) і [параметри тунелю](#tunnel-options).

### Приклади налаштування {#case-reference}

Нижче наведено два типові приклади політик VPN із покроковими інструкціями.

??? note "Приклад 1: лише зазначені пристрої використовують VPN."

    **Вимоги:**

    1. Лише певні пристрої, підключені до цього маршрутизатора, отримують доступ до інтернету через VPN. Усі інші пристрої використовують локальний WAN.

    2. Вибрані пристрої повинні використовувати лише з’єднання VPN. Якщо VPN несподівано відключиться, доступ цих пристроїв до інтернету має блокуватися для запобігання витокам DNS і відстеженню за IP-адресою.

    **Налаштування:**

    1. Виберіть профіль VPN.

        Якщо ви вже увійшли до інтегрованого VPN-сервісу зі службовими обліковими даними або завантажили конфігурацію, доступні профілі будуть наведені тут. Інакше відкрийте **VPN Client Profile**, щоб увійти або вручну завантажити файл конфігурації.

        У цьому прикладі використано [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Виберіть один або кілька профілів і за потреби змініть їхній пріоритет праворуч.

        ![Приклад 1: вибір профілів VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Виберіть джерело клієнтського трафіку.

        Натисніть вкладку **Specified Devices**, виберіть пристрої, які використовуватимуть VPN, і натисніть **Next**.

        ![Приклад 1: вибір джерела трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Виберіть призначення трафіку.

        Натисніть вкладку **All Targets**, задайте її як призначення трафіку та натисніть **Apply**.

        ![Приклад 1: вибір призначення трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Відкриється VPN Dashboard. Тунель VPN успішно додано, як показано нижче.

        ![Приклад 1: тунель додано](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Переконайтеся, що **Kill Switch** для цього тунелю увімкнено. Якщо VPN несподівано відключиться, доступ до інтернету для трафіку, що відповідає цьому тунелю, буде заблоковано для запобігання витокам DNS і відстеженню за IP-адресою.

        ![Приклад 1: параметри тунелю](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![Приклад 1: увімкнення Kill Switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

    6. Переконайтеся, що **Allow Non-VPN Traffic** увімкнено. Цей параметр увімкнено за замовчуванням, щоб трафік, який не відповідає тунелю VPN, міг отримувати доступ до інтернету через локальний WAN.

        ![Приклад 1: дозвіл трафіку поза VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Натисніть кнопку посередині, щоб активувати цей тунель.

        ![Приклад 1: запуск тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Після підключення на сторінці відобразяться відомості про з’єднання VPN: політика VPN, статистика трафіку, адреса сервера, порт прослуховування та віртуальна IP-адреса.

        ![Приклад 1: з’єднання VPN встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Тепер лише два зазначені пристрої отримують доступ до інтернету через VPN. Якщо VPN несподівано відключиться, доступ цих пристроїв до інтернету буде заблоковано для запобігання витокам DNS і відстеженню за IP-адресою. Усі інші пристрої використовуватимуть локальний WAN.

??? note "Приклад 2: усі пристрої використовують VPN 1 для певних сайтів, а весь інший трафік проходить через VPN 2."

    **Вимоги:**

    1. Усі пристрої використовують **VPN Tunnel 1** для доступу до доменів зазначених соціальних мереж і потокових сервісів, а **VPN Tunnel 2** — для всього іншого доступу до інтернету.

    2. Якщо тунелі VPN несподівано відключаться, доступ усіх пристроїв до інтернету має блокуватися для запобігання витокам DNS і відстеженню за IP-адресою.

    **Налаштування:**

    1. Виберіть профіль VPN для тунелю 1.

        Якщо ви вже увійшли до інтегрованого VPN-сервісу зі службовими обліковими даними або завантажили конфігурацію, доступні профілі будуть наведені тут. Інакше відкрийте **VPN Client Profile**, щоб увійти або вручну завантажити файл конфігурації.

        У цьому прикладі використано [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Виберіть один або кілька профілів, за потреби змініть їхній пріоритет праворуч і натисніть **Next**.

        ![Приклад 2: профілі тунелю 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Виберіть джерело клієнтського трафіку.

        Натисніть вкладку **All Clients**, задайте її як джерело клієнтського трафіку для тунелю 1 і натисніть **Next**.

        ![Приклад 2: джерело трафіку тунелю 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Виберіть призначення трафіку.

        Натисніть вкладку **Specified Domain / IP List**, введіть домени поширених соціальних мереж і потокових сервісів, як показано нижче, та натисніть **Apply**.

        ![Приклад 2: призначення трафіку тунелю 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Відкриється VPN Dashboard. Тунель VPN 1 успішно додано.

        ![Приклад 2: тунель 1 додано](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Переконайтеся, що **Kill Switch** для тунелю 1 увімкнено. Якщо VPN несподівано відключиться, доступ до інтернету для трафіку, що відповідає цьому тунелю, буде заблоковано для запобігання витокам DNS і відстеженню за IP-адресою.

        ![Аварійне блокування тунелю 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![Аварійне блокування тунелю 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

    6. Натисніть **Add New Tunnel**, щоб додати тунель 2.

        ![Приклад 2: додавання тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Виберіть профіль VPN для тунелю 2.

        У цьому прикладі використано [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}. Виберіть один або кілька профілів і за потреби змініть їхній пріоритет праворуч.

        ![Приклад 2: профілі тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Виберіть джерело клієнтського трафіку.

        Натисніть вкладку **All Clients**, задайте її як джерело клієнтського трафіку для тунелю 2 і натисніть **Next**.

        ![Приклад 2: джерело трафіку тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Виберіть призначення трафіку.

        Натисніть вкладку **All Targets**, задайте її як призначення трафіку для тунелю 2 і натисніть **Apply**.

        ![Приклад 2: призначення трафіку тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Відкриється VPN Dashboard. Тунель VPN 2 успішно додано.

        ![Приклад 2: тунель 2 додано](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Переконайтеся, що **Kill Switch** для тунелю 2 увімкнено. Якщо VPN несподівано відключиться, доступ до інтернету для трафіку, що відповідає цьому тунелю, буде заблоковано для запобігання витокам DNS і відстеженню за IP-адресою.

        ![Аварійне блокування тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![Аварійне блокування тунелю 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Натисніть піктограму шестерні у верхньому правому куті та увімкніть **Enhanced Kill Switch**. Це забезпечить доступ до інтернету для всього трафіку лише через VPN.

        ![Налаштування загальної політики трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![Увімкнення Enhanced Kill Switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Натисніть кнопку посередині, щоб активувати тунелі 1 і 2.

        ![Приклад 2: запуск тунелів VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Після підключення на сторінці відобразяться відомості про з’єднання VPN: політика VPN, статистика трафіку, адреса сервера, порт прослуховування та віртуальна IP-адреса.

        ![Приклад 2: з’єднання VPN встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Тепер усі пристрої використовуватимуть **VPN Tunnel 1** для доступу до зазначених доменів, а **VPN Tunnel 2** — для всього іншого доступу до інтернету. Якщо тунелі VPN несподівано відключаться, доступ усіх пристроїв до інтернету буде заблоковано для запобігання витокам DNS і відстеженню за IP-адресою.

## Аварійне блокування VPN (Kill Switch) {#kill-switch}

!!! Tip "Що таке Kill Switch?"

    Аварійне блокування VPN (Kill Switch) — це функція безпеки з’єднань VPN. Вона автоматично блокує доступ до інтернету для трафіку, охопленого відповідними налаштуваннями Kill Switch, якщо з’єднання VPN несподівано розривається, щоб запобігти розкриттю справжньої IP-адреси й даних та забезпечити безперервний захист конфіденційності. Ця функція особливо корисна для захищеного анонімного доступу до інтернету, наприклад у публічних мережах, під час обробки конфіденційних даних або приховування справжньої IP-адреси.

    Після увімкнення вона блокує клієнтський трафік, який намагається обійти тунель VPN, запобігаючи витокам через проблеми конфігурації DNS, несподівані розриви з’єднання, прямі запити за IP-адресою та подібні ситуації.

Починаючи з прошивки v4.8, маршрутизатори GL.iNet підтримують налаштування Kill Switch як для VPN загалом, так і для кожного окремого тунелю VPN.

- Налаштування Kill Switch для VPN загалом (Enhanced Kill Switch) описано в розділі [увесь інший трафік](#all-other-traffic).

- Налаштування Kill Switch для окремого тунелю VPN описано в розділі [параметри тунелю](#tunnel-options).

## Увесь інший трафік {#all-other-traffic}

Натисніть піктограму шестерні у верхньому правому куті, щоб налаштувати політику для трафіку, який не відповідає тунелям VPN.

![Увесь інший трафік](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Ця політика визначає, чи може трафік, який не відповідає жодній групі тунелів VPN, отримувати доступ до інтернету. Доступні два варіанти: **Allow Non-VPN Traffic** і **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: увімкнено за замовчуванням для забезпечення звичайного доступу до інтернету для трафіку поза VPN.

    ![Дозвіл трафіку поза VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: змушує всі пристрої використовувати VPN для доступу до інтернету. Трафік, який не відповідає тунелю VPN, блокується. Цей глобальний параметр не перевизначає Kill Switch, налаштований для окремих тунелів VPN.

    ![Розширене аварійне блокування VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Параметри тунелю {#tunnel-options}

Для кожного тунелю VPN можна налаштувати додаткові параметри, зокрема Kill Switch, маскарадинг IP та MTU.

Натисніть піктограму шестерні у групі тунелів і виберіть **Options**.

![Відкриття параметрів тунелю](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![Параметри тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: якщо увімкнено, трафік, що відповідає цьому тунелю VPN, блокується за несподіваного розриву з’єднання VPN. Якщо вимкнено, такий трафік перемикається на тунель **All Other Traffic**.

- **Services from GL.iNet Use VPN**: якщо увімкнено, сервіси GoodCloud, DDNS і rtty передають пакети через тунелі VPN. За замовчуванням цей параметр вимкнено, оскільки для належної роботи цих сервісів зазвичай потрібна справжня IP-адреса пристрою.

- **Allow Remote Access to the LAN Subnet**: якщо увімкнено, дозволяється віддалений доступ через VPN до цього маршрутизатора та його пристроїв LAN. Сервер VPN повинен оголошувати зворотний маршрут до його підмережі LAN.

- **IP Masquerading**: якщо увімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

- **MTU**: задане для тунелю значення MTU перевизначає налаштування MTU у файлі конфігурації.

## Пріоритет тунелів {#tunnel-priority}

Щоб змінити пріоритет тунелів, натисніть піктограму шестерні у групі тунелів і виберіть **Priority**.

![Відкриття налаштувань пріоритету](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Натисніть і утримуйте піктограму з трьома лініями праворуч, змініть порядок тунелів перетягуванням і натисніть **Apply**.

![Порядок пріоритету тунелів](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Коли увімкнено кілька тунелів, маршрутизатор обробляє трафік за такими правилами**:

1. Спочатку перевіряється, чи відповідає трафік правилу тунелю з найвищим пріоритетом. Якщо так, він проходить через цей тунель. Якщо ні, перевіряється наступний тунель у порядку пріоритету, і так далі.

2. Кожна група тунелів працює незалежно. Щойно трафік відповідає правилу тунелю, він проходить через цей тунель і не перемикається між групами тунелів у разі збою.

3. У кожній групі тунелів можна вибрати кілька профілів для аварійного перемикання в межах тунелю. Якщо профіль із найвищим пріоритетом у групі перестає працювати, тунель автоматично підключається за допомогою наступного профілю за пріоритетом, і так далі.

4. Якщо тунель VPN несподівано відключиться, система визначатиме, чи перемикати трафік на тунель All Other Traffic, відповідно до стану **Kill Switch** цього тунелю.

    - Якщо Kill Switch увімкнено, трафік блокується і не перемикається на тунель All Other Traffic.
    - Якщо Kill Switch вимкнено, трафік перемикається на тунель All Other Traffic.

5. У тунелі **All Other Traffic** вибраний режим визначає, чи може трафік, який не відповідає тунелю VPN, отримувати доступ до інтернету.

    - **Allow Non-VPN Traffic**: увімкнено за замовчуванням, щоб трафік, який не відповідає тунелям VPN, міг отримувати доступ до інтернету через локальний WAN.

    - **Enhanced Kill Switch**: змушує всі пристрої використовувати VPN для доступу до інтернету. Трафік, який не відповідає тунелю VPN, блокується. Цей глобальний параметр не перевизначає Kill Switch, налаштований для окремих тунелів VPN. Він посилює аварійне блокування VPN і блокує звичайний доступ до інтернету для запобігання витокам IP-адреси.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
