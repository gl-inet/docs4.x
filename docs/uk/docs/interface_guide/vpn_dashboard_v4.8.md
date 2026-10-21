# Панель керування VPN (прошивка v4.8) {#vpn-dashboard-firmware-v48}

Ця сторінка описує прошивку v4.8.x. Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.8" markdown="1">

- [Прошивка v4.7 та раніші версії](vpn_dashboard_v4.7.md)
- [Прошивка v4.9 та новіші версії](vpn_dashboard.md)

</div>

У меню ліворуч у вебпанелі адміністрування перейдіть до **VPN** -> **VPN Dashboard**.

Панель керування VPN відображає відомості про з’єднання VPN: правила тунелів, адресу сервера, статистику трафіку, віртуальну IP-адресу клієнта та журнал з’єднання. Також тут можна налаштувати додаткові параметри, зокрема аварійне блокування VPN (Kill Switch), маскарадинг IP і MTU.

Для роботи з кількома тунелями можна активувати кілька з’єднань VPN.

## Майстер налаштування {#setup-wizard}

Натисніть значок книги вгорі ліворуч і дотримуйтеся інструкцій VPN Setup Wizard, щоб швидко налаштувати VPN.

![Відкриття майстра налаштування VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![Майстер налаштування інтегрованих служб VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Примітка**: VPN Setup Wizard призначений лише для інтегрованих служб VPN: AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA і Surfshark. Для інших служб пропустіть майстер і відкрийте [OpenVPN Client](openvpn_client.md){target="_blank"} або [WireGuard Client](wireguard_client.md){target="_blank"}, щоб налаштувати VPN вручну.

Нижче наведено приклад для **Hide.me**. Увійдіть за допомогою облікових даних Hide.me.

![Вхід у Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Виберіть сервер VPN і натисніть **Apply**. Цей тунель VPN підключатиметься до вибраного сервера, а ваша публічна IP-адреса виглядатиме так, наче походить із місця його розташування.

![Вибір сервера VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

З’єднання встановиться автоматично. Після успішного підключення перейдіть до VPN Dashboard: ви побачите ввімкнений тунель VPN.

![Установлене з’єднання VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Відображаються поточний протокол VPN (наприклад, WireGuard), файл конфігурації, адреса сервера, порт прослуховування сервера, статистика трафіку та віртуальна IP-адреса клієнта. Журнал з’єднання можна переглянути внизу праворуч.

Усі підключені клієнти отримуватимуть доступ до інтернету через цей тунель VPN.

Щоб налаштувати політику VPN, дивіться [Режим політик](#policy-mode).

## Режим VPN {#vpn-mode}

На сторінці VPN Dashboard натисніть кнопку вгорі праворуч, щоб змінити режим VPN.

![Вибір режиму VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Доступні два режими: **Global Mode** і **Policy Mode**.

![Вибір режиму VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Глобальний режим {#global-mode}

У цьому режимі весь трафік спрямовується через тунель VPN. Можна активувати лише один екземпляр клієнта VPN.

Цей режим підходить, коли весь клієнтський трафік потрібно спрямувати через один сервер VPN, наприклад для єдиного захисту мережі або доступу до вмісту певного регіону.

У цьому прикладі маршрутизатор підключається до сервера в Австралії за протоколом WireGuard. Увесь трафік підключених клієнтів проходитиме через цей тунель VPN.

![З’єднання VPN у глобальному режимі](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

#### Параметри тунелю {#tunnel-options}

Для тунелю VPN можна налаштувати додаткові параметри, зокрема Kill Switch, маскарадинг IP і MTU.

Натисніть значок шестірні у верхньому правому куті.

![Параметри тунелю глобального режиму](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options1.png){class="glboxshadow"}

![Параметри тунелю глобального режиму](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode_options2.png){class="glboxshadow"}

- **Kill Switch**: Якщо ввімкнено, увесь трафік, спрямований через цей тунель VPN, автоматично блокується в разі збою з’єднання VPN. Якщо вимкнено, трафік повертається до локального WAN і отримує доступ до інтернету без тунелю VPN.

- **Services from GL.iNet Use VPN**: Якщо ввімкнено, служби GoodCloud, DDNS і rtty передають пакети через тунелі VPN. За замовчуванням цей параметр вимкнено, оскільки для належної роботи цих служб зазвичай потрібна справжня IP-адреса пристрою.

- **Allow Remote Access the LAN Subnet**: Якщо ввімкнено, дозволено віддалений доступ через VPN до цього маршрутизатора та його пристроїв LAN. Сервер VPN має оголошувати маршрут до підмережі LAN цього маршрутизатора.

- **IP Masquerading**: Якщо ввімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

    Як показано нижче, якщо маскарадинг IP увімкнено і ноутбук (192.168.10.200) у дорожній мережі LAN надсилає трафік через тунель на домашній NAS (192.168.8.100), дорожній маршрутизатор замінює IP-адресу джерела `192.168.10.200` на адресу тунелю клієнта VPN `10.1.0.2`. Тому сторона сервера бачить, що трафік надходить від клієнта, а не з локальної мережі LAN клієнта.

    ![Маскарадинг IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Скорочення від Maximum Transmission Unit (максимальний розмір пакета для передавання). Задане для тунелю значення MTU перевизначає значення у файлі конфігурації.

### Режим політик {#policy-mode}

У цьому режимі маршрутизатор може підключатися до кількох серверів VPN. Для різних клієнтів або призначень трафіку можна налаштувати власні правила маршрутизації.

Цей режим підходить для гнучкого керування трафіком, наприклад для спрямування різного трафіку до різних призначень через кілька серверів VPN.

Змініть VPN Mode на Policy Mode і натисніть **Apply**.

![Перемикання в режим політик](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Після перемикання, якщо VPN не ввімкнено, сторінка матиме такий вигляд. Вона містить три розділи: Primary Tunnel, Add Tunnel і All Other Traffic.

![Режим політик без увімкненого VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Натисніть відповідний розділ, щоб дізнатися більше.

- [Основний тунель](#primary-tunnel)
- [Додавання тунелю](#add-tunnel)
- [Увесь інший трафік](#all-other-traffic)

#### Основний тунель {#primary-tunnel}

Основний тунель — <u>попередньо налаштований</u> тунель у режимі політик. Він має найвищий пріоритет. Якщо тунелів кілька, можна змінити [пріоритет тунелів](#tunnel-priority).

Налаштуйте правило цього тунелю за трьома параметрами:

1. **From**: Джерело трафіку, тобто трафік, який має проходити через цей тунель.

    Натисніть сіре поле, щоб вибрати джерело трафіку.

    ![Вибір джерела трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![Вибір джерела трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}

    - **All Clients**: Якщо вибрано, трафік усіх пристроїв відповідає цьому правилу.

        ![Правило для всіх клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: Якщо вибрано, цьому правилу відповідає трафік визначених типів підключення (наприклад, підмережі LAN, Drop-in Gateway або Guest Network).

        ![Вибір типів підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Якщо на маршрутизаторі ввімкнено сервер OpenVPN або WireGuard, у Specified Connection Types з’являться додаткові варіанти. Це корисно для [каскадування VPN](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![Вибір типів підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: Якщо вибрано, трафік визначених пристроїв, які ідентифікуються за MAC-адресами, відповідає цьому правилу.

        ![Вибір визначених пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: Якщо вибрано, трафік визначених пристроїв, які ідентифікуються за MAC-адресами, **НЕ** відповідає цьому правилу.

        ![Виключення визначених пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: Призначення трафіку.

    Натисніть сіре поле, щоб вибрати призначення трафіку.

    ![Вибір призначення трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}

    ![Вибір призначення трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: Якщо вибрано, правило маршрутизації застосовується до трафіку до всіх призначень.

        ![Правило для всіх призначень](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Якщо вибрано, трафік за цим правилом спрямовується до визначених доменів або IP-адрес. Уведіть їх вручну.

        Якщо вказати <u>основний домен</u>, правило охоплюватиме всі його піддомени. Наприклад, щоб указати `archive.ubuntu.com`, `security.ubuntu.com` і `old-releases.ubuntu.com` для тунелю, достатньо основного домену `ubuntu.com`.

        ![Ручне введення визначених доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Або змініть **Input Mode** із Manual на Subscription URL і введіть URL-посилання.

        ![Підписка на список визначених доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Якщо вказати основний домен, правило охоплюватиме всі його піддомени.

            - Якщо вибрати Subscribe URL, доменні імена або IP-адреси за цим URL оновлюватимуться автоматично щодня.

            - Переконайтеся, що введено правильний URL. Перевірка URL визначатиме дійсність доменного імені або IP-адреси. [Докладніше](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: Якщо вибрано, трафік до визначених доменів або IP-адрес **НЕ** спрямовується за цим правилом. Уведіть їх вручну.

        Якщо вказати <u>основний домен</u>, правило охоплюватиме всі його піддомени. Наприклад, щоб указати `archive.ubuntu.com`, `security.ubuntu.com` і `old-releases.ubuntu.com` для тунелю, достатньо основного домену `ubuntu.com`.

        ![Ручне введення виключених доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Або змініть **Input Mode** із Manual на Subscription URL і введіть URL-посилання.

        ![Підписка на список виключених доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note

            - Якщо вказати основний домен, правило охоплюватиме всі його піддомени.

            - Якщо вибрати Subscribe URL, доменні імена або IP-адреси за цим URL оновлюватимуться автоматично щодня.

            - Переконайтеся, що введено правильний URL. Перевірка URL визначатиме дійсність доменного імені або IP-адреси. [Докладніше](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: Метод маршрутизації трафіку, тобто чи використовувати VPN.

    Натисніть сіре поле, щоб вибрати метод маршрутизації.

    ![Вибір методу маршрутизації](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![Вибір методу маршрутизації](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: Якщо вибрано, трафік за цим правилом спрямовується до вибраних призначень через VPN.

        Спочатку налаштуйте маршрутизатор як клієнт VPN. Скористайтеся [VPN Setup Wizard](#setup-wizard), щоб швидко завершити налаштування, або відкрийте OpenVPN Client / WireGuard Client у меню ліворуч для налаштування вручну.

        Після налаштування маршрутизатора як клієнта VPN виберіть файл конфігурації VPN для цього тунелю та натисніть **Apply**.

        ![Маршрутизація через VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: Якщо вибрано, трафік за цим правилом спрямовується до вибраних призначень через локальний WAN замість VPN.

        ![Маршрутизація через локальний WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Після вибору джерела, призначення та методу маршрутизації налаштування правила основного тунелю завершено.

У цьому прикладі правило Primary Tunnel таке: усі клієнти використовують VPN для доступу до визначених доменів. Їхній трафік проходить через сервер в Австралії та цей тунель до вибраних інтернет-доменів.

![Установлене з’єднання в режимі політик](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Примітка**: З міркувань безпеки перед увімкненням тунелів перевірте інші налаштування в розділах [Увесь інший трафік](#all-other-traffic) і [Параметри тунелю](#tunnel-options_1).

#### Додавання тунелю {#add-tunnel}

Щоб створити додаткові тунелі для кількох екземплярів VPN, натисніть **Add Tunnel** під Primary Tunnel і налаштуйте власні правила.

![Додавання тунелю](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Задайте назву тунелю.

![Назва нового тунелю](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

На сторінці VPN Dashboard з’явиться ще один тунель.

![Два налаштовані тунелі](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

За потреби додайте інші тунелі. Можна створити до 5 тунелів, зокрема попередньо налаштований основний тунель.

Налаштуйте правила тунелю, задавши джерело, призначення та метод маршрутизації трафіку. Дивіться [Основний тунель](#primary-tunnel).

**Примітка**: З міркувань безпеки перед увімкненням тунелів перевірте інші налаштування в розділах [Увесь інший трафік](#all-other-traffic) і [Параметри тунелю](#tunnel-options_1).

#### Увесь інший трафік {#all-other-traffic}

У режимі політик унизу сторінки VPN Dashboard відображається <u>попередньо ввімкнений</u> тунель.

![Тунель для всього іншого трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Цей тунель визначає, чи може трафік, який не відповідає жодній із наведених вище груп тунелів VPN, отримувати доступ до інтернету. Він увімкнений за замовчуванням, щоб забезпечувати звичайний доступ до інтернету для трафіку поза VPN.

- Коли ввімкнено, трафік, який не відповідає правилам, і далі має доступ до інтернету.

    ![Увесь інший трафік дозволено](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Коли вимкнено, доступ до інтернету дозволено лише трафіку через VPN. Увесь трафік поза VPN і трафік після аварійного перемикання зі з’єднань VPN блокується. Цей параметр не перевизначає окремий Kill Switch кожного тунелю VPN.

    ![Увесь інший трафік заблоковано](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Пріоритет тунелів {#tunnel-priority}

За замовчуванням попередньо налаштований Primary Tunnel має найвищий пріоритет. Далі йдуть інші тунелі, додані вручну, якщо вони є, а останнім — All Other Traffic, щоб забезпечувати з’єднання локальної мережі через локальний WAN.

Щоб змінити пріоритет тунелів, натисніть **Modify Priority** у верхній інформаційній панелі або **позначку пріоритету** вгорі ліворуч будь-якого тунелю (наприклад, Priority 1/Priority 2).

![Зміна пріоритету тунелів](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Натисніть і утримуйте значок із трьома лініями праворуч, щоб змінити порядок тунелів, а потім натисніть **Apply**.

![Зміна пріоритету тунелів](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Коли ввімкнено кілька тунелів, маршрутизатор спрямовує трафік у такому порядку**:

1. Спочатку перевіряється відповідність трафіку правилу тунелю з найвищим пріоритетом. Якщо трафік відповідає правилу, він проходить через цей тунель. Інакше перевіряється наступний тунель за пріоритетом і так далі, доки трафік не відповідатиме тунелю "All Other Traffic".

2. Якщо тунель VPN несподівано відключається, система визначає, чи перемикати трафік на наступний тунель за пріоритетом, залежно від того, чи ввімкнено **Kill Switch** цього тунелю.

    - Якщо Kill Switch увімкнено, трафік блокується та не перемикається на наступний тунель за пріоритетом.
    - Якщо Kill Switch вимкнено, трафік перемикається на наступний тунель за пріоритетом, де перевіряється його відповідність правилам цього тунелю.

3. Тунель **All Other Traffic** увімкнено за замовчуванням, щоб трафік, який не відповідає тунелям VPN, і далі мав доступ до інтернету.

    - Якщо ввімкнено, трафік, який не відповідає правилам, або трафік після аварійного перемикання спрямовується через локальний WAN.
    - Якщо вимкнено, він посилює аварійне блокування VPN (Kill Switch) і блокує звичайний доступ до інтернету, щоб запобігти витоку IP-адреси.

#### Параметри тунелю {#tunnel-options_1}

Для кожного тунелю VPN можна налаштувати додаткові параметри, зокрема Kill Switch, маскарадинг IP та MTU.

Натисніть значок шестірні біля назви тунелю та виберіть **Options**.

![Параметри тунелю в режимі політик](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![Параметри тунелю в режимі політик](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: Якщо ввімкнено, увесь трафік, спрямований через цей тунель VPN, автоматично блокується в разі збою з’єднання VPN. Якщо вимкнено, трафік перемикається на наступний тунель за пріоритетом або локальний WAN.

- **Services from GL.iNet Use VPN**: Якщо ввімкнено, служби GoodCloud, DDNS і rtty передають пакети через тунелі VPN. За замовчуванням цей параметр вимкнено, оскільки для належної роботи цих служб зазвичай потрібна справжня IP-адреса пристрою.

- **Allow Remote Access the LAN Subnet**: Якщо ввімкнено, дозволено віддалений доступ через VPN до цього маршрутизатора та його пристроїв LAN. Сервер VPN має оголошувати маршрут до підмережі LAN цього маршрутизатора.

- **IP Masquerading**: Якщо ввімкнено, IP-адреси джерела трафіку клієнтів LAN замінюються IP-адресою тунелю VPN маршрутизатора. Вимикайте цей параметр лише для з’єднань між мережами (site-to-site), коли віддалений вузол знає ваші підмережі LAN.

    Як показано нижче, якщо маскарадинг IP увімкнено і ноутбук (192.168.10.200) у дорожній мережі LAN надсилає трафік через тунель на домашній NAS (192.168.8.100), дорожній маршрутизатор замінює IP-адресу джерела `192.168.10.200` на адресу тунелю клієнта VPN `10.1.0.2`. Тому сторона сервера бачить, що трафік надходить від клієнта, а не з локальної мережі LAN клієнта.

    ![Маскарадинг IP](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Скорочення від Maximum Transmission Unit (максимальний розмір пакета для передавання). Задане для тунелю значення MTU перевизначає значення у файлі конфігурації.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
