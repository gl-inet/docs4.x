# GL.iNet GoodCloud {#glinet-goodcloud}

## Вступ {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} — це платформа для спрощення віддаленого розгортання підключених пристроїв і керування ними. Вона дає змогу легко отримувати віддалений доступ до маршрутизаторів GL.iNet та керувати ними. Завдяки централізованому керуванню мережевими пристроями у хмарі користувачі можуть ефективно виконувати групові операції, зокрема розгортати мережеві конфігурації та оновлювати програмне забезпечення. Також можна віддалено відкривати вебпанель адміністрування маршрутизатора або підключатися до його термінала через SSH, керуючи мережевими пристроями в різних регіонах від одного кінця з’єднання до іншого.

GoodCloud дає змогу:

1. Перевіряти стан маршрутизатора в реальному часі
    - Відстежувати, чи пристрій у мережі
    - Переглядати використання оперативної пам’яті та середнє навантаження в реальному часі
    - Отримувати сповіщення електронною поштою, коли пристрій підключається до мережі або відключається від неї

2. Налаштовувати маршрутизатори віддалено
    - Налаштовувати параметри маршрутизатора (наприклад, SSID і пароль)
    - Отримувати віддалений доступ через SSH
    - Отримувати віддалений доступ до вебінтерфейсу
    - Надавати іншим користувачам доступ до маршрутизатора

3. Віддалено відстежувати підключених клієнтів
    - Переглядати пристрої, підключені до вашої мережі
    - Відстежувати трафік у реальному часі та блокувати клієнтів
    - Отримувати сповіщення електронною поштою про нові підключення та блокування

4. Виконувати групові операції
    - Перезавантажувати пристрої групою
    - Оновлювати прошивку на кількох пристроях одночасно

5. Встановлювати з’єднання між мережами (site-to-site)
    - Віртуальний офіс: розширювати офісну мережу на інші філії
    - Відрядження: отримувати віддалений доступ до офісних систем (наприклад, OA, CRM, MySQL)
    - Розумний дім: отримувати віддалений доступ до домашніх пристроїв (наприклад, IP-камер, NAS)

Якщо потрібно керувати кількома пристроями та використовувати розширені можливості, як-от групові операції, керування кількома обліковими записами та індивідуальні рішення, виберіть один із наших розширених тарифних планів. Докладні відомості наведено [тут](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}. Також можна звернутися за адресою [support@gl-inet.com](mailto:support@gl-inet.com).

<span id="setup-your-goodcloud-account"></span>
<span id="add-device-in-your-account"></span>

## Прив’язування пристроїв до хмари {#bind-devices-to-cloud}

Виберіть розділ з інструкціями з прив’язування пристрою відповідно до версії його прошивки.

### Для прошивки v4.10 і новіших версій {#for-firmware-v410-and-above}

1. Увімкніть GoodCloud.

    Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте **CLOUD SERVICE** -> **GoodCloud** і натисніть **Get Started**.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Відкриється сторінка **GL.iNet Account**. Натисніть **Bind GL.iNet Account via URL**.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    У спливному вікні натисніть **Continue**. Вас буде перенаправлено на сайт GoodCloud для завершення прив’язування.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Увійдіть, щоб прив’язати пристрій.

    Увійдіть у свій обліковий запис GL.iNet. Якщо у вас немає облікового запису, зареєструйте його та увійдіть.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Після входу перевірте відомості про обліковий запис і пристрій, зокрема Device ID, модель та MAC-адресу. Задайте назву пристрою та натисніть **Bind**. Маршрутизатор буде прив’язано до вашого облікового запису.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Якщо лист із підтвердженням не надійшов, перевірте папку зі спамом або зачекайте кілька хвилин і повторіть спробу. Щоб отримати додаткову допомогу, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com).

3. Перегляньте відомості про прив’язування.

    Після успішного прив’язування поверніться до вебпанелі адміністрування маршрутизатора та відкрийте **CLOUD SERVICES** -> **GoodCloud**. На цій сторінці відображаються посилання для переходу на платформу GoodCloud, ідентифікаційні дані пристрою та останні журнали хмарного сервісу.

    ![Прив’язування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Віддалений доступ.

    У прошивці v4.10 віддалений доступ до вебпанелі адміністрування та термінала маршрутизатора вмикається за замовчуванням після прив’язування маршрутизатора до GoodCloud.

5. Скасуйте прив’язування пристрою.

    Щоб скасувати прив’язування маршрутизатора, увійдіть у його вебпанель адміністрування та відкрийте **CLOUD SERVICES** -> **GL.iNet Account**. Натисніть **Unbind**.

    ![Скасування прив’язування](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    Також можна видалити пристрій зі списку Bound Devices на платформі GoodCloud. Вебпанель адміністрування маршрутизатора синхронізується та відобразить актуальний стан прив’язування.

    Якщо виникли труднощі, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com), щоб отримати допомогу.

### Для прошивки v4.7–v4.9 {#for-firmware-v47-to-v49}

1. Увімкніть GoodCloud.

    Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **CLOUD SERVICE** -> **GoodCloud**.

    Натисніть кнопку **Get Started**. У верхньому правому куті з’явиться спливне вікно Cloud Service. Натисніть **Enable**.

    ![Увімкнення хмарного сервісу](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. Увійдіть, щоб прив’язати пристрій.

    ![Вхід у GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Якщо у вас немає облікового запису, зареєструйте його та увійдіть. Після завершення реєстрації маршрутизатор буде автоматично прив’язано до вашого облікового запису.

    ![Реєстрація в GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Якщо лист із підтвердженням не надійшов, перевірте папку зі спамом або зачекайте кілька хвилин і повторіть спробу. Щоб отримати додаткову допомогу, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com).

3. Перегляньте відомості про прив’язування.

    Після успішного прив’язування поверніться до вебпанелі адміністрування маршрутизатора та натисніть піктограму хмари у верхньому правому куті. Відобразяться відомості про прив’язування, зокрема ім’я користувача, час прив’язування, Device ID, Device MAC і Device S/N.

    ![Відомості про прив’язування](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. Увімкніть віддалений доступ.

    У вебпанелі адміністрування відкрийте **CLOUD SERVICES** -> **GoodCloud**, щоб увімкнути віддалений доступ до маршрутизатора.

    ![Увімкнення віддаленого доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: віддалений доступ до термінала маршрутизатора через SSH із платформи GoodCloud.

    - **Remote Web Access**: віддалений доступ до вебпанелі адміністрування маршрутизатора через HTTP/HTTPS із платформи GoodCloud.

    - **View Logs**: перегляд журналів викликів API, виконаних GoodCloud.

5. Скасуйте прив’язування пристрою.

    Щоб скасувати прив’язування маршрутизатора, увійдіть у його вебпанель адміністрування. Натисніть піктограму хмари у верхньому правому куті та виберіть **Unbind**.

    ![Скасування прив’язування до GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    Також можна видалити пристрій зі списку Bound Devices на платформі GoodCloud. Вебпанель адміністрування маршрутизатора синхронізується та відобразить актуальний стан прив’язування.

    Якщо виникли труднощі, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com), щоб отримати допомогу.

### Для прошивки v4.6 і попередніх версій {#for-firmware-v46-or-earlier}

1. Увімкніть GoodCloud.

    Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **APPLICATIONS** -> **GoodCloud**. Увімкніть GoodCloud за допомогою перемикача.

    ![Увімкнення GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    За потреби увімкніть **Remote SSH** і **Remote Web Access**, виберіть найближчий сервер, прочитайте й прийміть **Terms of Service & Privacy Policy**, а потім натисніть **Apply**.

    ![Увімкнення GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: віддалений доступ до термінала маршрутизатора через SSH із платформи GoodCloud.

    - **Remote Web Access**: віддалений доступ до вебпанелі адміністрування маршрутизатора через HTTP/HTTPS із платформи GoodCloud.

    - **Data Server**: виберіть сервер, найближчий до розташування пристрою. Доступні три варіанти: Asia Pacific (Japan), America (Oregon) та Europe (Ireland).

2. Зареєструйте обліковий запис.

    Відкрийте [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, зареєструйтеся та увійдіть.

    Якщо лист із підтвердженням не надійшов, перевірте папку зі спамом або зачекайте кілька хвилин і повторіть спробу. Щоб отримати додаткову допомогу, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com).

3. Додайте пристрої.

    На хмарній платформі відкрийте **Devices** -> **Bound Devices** -> **Add Devices**.

    ![Додавання пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Є три способи прив’язати пристрій до облікового запису GoodCloud: Auto Discover, Manually Add і Bulk Import.

    ??? "Auto Discover"

        Скористайтеся **Auto discover**, якщо маршрутизатор і пристрій, з якого ви відкрили сайт GoodCloud, перебувають в одній мережі.

        Виберіть пристрій із розкривного списку та введіть **DDNS / Device ID**. Ці відомості можна знайти на нижній стороні маршрутизатора або на сторінці GoodCloud у вебпанелі адміністрування.

        ![Автоматичне виявлення пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Як знайти Device ID, описано за [цим посиланням](../faq/where_to_find_the_device_id_mac_sn.md).

    ??? "Manually Add"

        Якщо пристрою немає у списку, натисніть **Manually add** і введіть відомості про маршрутизатор. Усі потрібні дані можна знайти на нижній стороні маршрутизатора або на сторінці GoodCloud у вебпанелі адміністрування.

        ![Додавання пристрою вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** призначено для користувачів, які керують великою кількістю пристроїв. Можна імпортувати кілька пристроїв за допомогою файлу Microsoft Excel.

        ![Груповий імпорт](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Перегляньте відомості про прив’язування.

    Після успішного прив’язування поверніться до вебпанелі адміністрування маршрутизатора та відкрийте **APPLICATIONS** -> **GoodCloud**. На цій сторінці відображаються відомості про прив’язування, зокрема ім’я користувача та час прив’язування.

    ![Пристрій прив’язано до GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. Скасуйте прив’язування пристрою.

    Щоб скасувати прив’язування маршрутизатора, увійдіть у його вебпанель адміністрування, відкрийте **APPLICATION** -> **GoodCloud** і натисніть **Unbind**.

    ![Скасування прив’язування до GoodCloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    Також можна видалити пристрій зі списку Bound Devices на платформі GoodCloud. Вебпанель адміністрування маршрутизатора синхронізується та відобразить актуальний стан прив’язування.

    Якщо виникли труднощі, напишіть на [support@gl-inet.com](mailto:support@gl-inet.com), щоб отримати допомогу.

## Керування пристроями {#manage-devices}

### Системні відомості та дії {#system-info-and-actions}

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** можна переглядати системні відомості (наприклад, модель, версію, MAC-адресу, IP-адресу) та стан (наприклад, у мережі або поза мережею) усіх пристроїв, прив’язаних до вашого облікового запису.

![Відомості про пристрої](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Виберіть пристрій, щоб виконати дії у верхньому правому куті: змінити налаштування, оновити прошивку, отримати віддалений доступ до пристрою, перезавантажити його або скинути налаштування.

![Дії з пристроєм](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![Додаткові дії з пристроєм](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Натисніть піктограму шестерні праворуч у заголовку списку, щоб налаштувати видимість і порядок стовпців та зосередитися на потрібних відомостях про пристрої.

![Налаштування стовпців](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Докладні відомості про пристрій {#device-details}

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** натисніть назву пристрою. Відкриється сторінка з докладними відомостями про нього: основною інформацією про маршрутизатор, статистикою, мережевими налаштуваннями, списком клієнтів тощо.

![Докладні відомості про пристрій](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Основні відомості {#basic-info}

![Основні відомості](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Статистика {#statistics}

![Статистика](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Мережеві налаштування {#network-settings}

На цій сторінці відображаються конфігурація мережі та налаштування Wi-Fi маршрутизатора.

![Огляд стану](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Список клієнтів {#clients-list}

![Список клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Віддалений доступ {#remote-access}

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** натисніть назву потрібного пристрою, щоб відкрити сторінку з докладними відомостями. У верхньому правому куті відобразяться дії для віддаленого доступу.

![Віддалений доступ](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Віддалений доступ до вебінтерфейсу {#remote-gui}

Натисніть **Remote GUI**, щоб віддалено відкрити вебпанель адміністрування маршрутизатора.

![Віддалений доступ до вебпанелі адміністрування](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Якщо цей пункт сірий або недоступний, імовірно, функцію вимкнено. Спочатку увімкніть її у вебпанелі адміністрування маршрутизатора, а потім отримайте доступ через GoodCloud.

Якщо пункт доступний для натискання, але не реагує, спробуйте режим інкогніто/InPrivate у браузері.

### Віддалений доступ через SSH {#remote-ssh}

Натисніть **Remote SSH**, щоб віддалено підключитися до термінала маршрутизатора через SSH.

![Віддалений доступ до термінала пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Якщо цей пункт сірий або недоступний, імовірно, функцію вимкнено. Спочатку увімкніть її у вебпанелі адміністрування маршрутизатора, а потім отримайте доступ через GoodCloud.

Якщо пункт доступний для натискання, але не реагує, спробуйте режим інкогніто/InPrivate у браузері.

## Зміна налаштувань {#modify-settings}

Можна налаштувати різні параметри для одного або кількох пристроїв.

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** виберіть пристрій, який потрібно налаштувати, а у верхньому правому куті натисніть **Settings** -> **Modify Settings**.

![Налаштування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Тут можна перевіряти та змінювати мережеві налаштування маршрутизатора, зокрема параметри бездротової мережі, Ethernet, безпеки, перенаправлення портів, LAN і системи.

![Параметри пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Сповіщення електронною поштою {#email-alarm}

Можна налаштувати сповіщення електронною поштою про зміну стану пристрою (у мережі/поза мережею) або підключення нових клієнтів.

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** натисніть кнопку **Add Rule** у верхньому правому куті.

![Додавання правила сповіщення](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Виберіть пристрій для моніторингу та натисніть **Next**.

![Вибір пристрою для сповіщень](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Виберіть подію, що має викликати сповіщення, наприклад перехід пристрою в мережу або вихід із мережі, та натисніть **Next**.

![Вибір події для сповіщення](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![Налаштування події для сповіщення](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Перевірте налаштування правила та натисніть **Apply**.

![Підтвердження правила сповіщення](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

У списку Notifications можна переглядати створені правила сповіщень. Індивідуальні користувачі можуть створити лише одне правило. Якщо потрібно керувати пристроями групами, зверніться до нас, щоб перейти на розширений тарифний план.

![Список правил сповіщень](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## З’єднання між мережами {#site-to-site}

Див. [з’єднання між мережами через GoodCloud](../tutorials/goodcloud_site_to_site.md).

## GoodCloud і VPN {#goodcloud-and-vpn}

Якщо на маршрутизаторі одночасно увімкнено **GoodCloud** і **VPN client**, з’єднання між маршрутизатором і сервером GoodCloud за замовчуванням не проходить через VPN. Це забезпечує стабільніше підключення до сервісів GoodCloud.

Щоб з’єднання GoodCloud проходило через VPN, змініть відповідний параметр у вебпанелі адміністрування маршрутизатора. Відкрийте VPN -> VPN Dashboard -> VPN Client -> Options і увімкніть параметр «Services from GL.iNet Use VPN».

![Параметр Services from GL.iNet Use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Маршрутизація з’єднання GoodCloud через VPN може вплинути на стабільність підключення до хмари, особливо якщо:

* З’єднання VPN нестабільне
* Провайдер VPN фільтрує або блокує трафік GoodCloud
* VPN значно збільшує затримку з’єднання

Для оптимальної продуктивності та надійності зазвичай рекомендовано залишати налаштування за замовчуванням, за яких GoodCloud обходить VPN.

## Перегляд журналів {#view-logs}

За потреби можна переглядати журнали GoodCloud: Activity Logs, Device Logs, Upgrade Logs, Alert Logs і Device Settings Logs.

У розділі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** виберіть потрібні журнали з розкривного списку.

![Перегляд журналів](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Вимкнення хмарного сервісу {#disable-cloud}

Якщо більше не потрібно підключати пристрій до хмарної платформи, вимкніть хмарний сервіс у вебпанелі адміністрування маршрутизатора.

??? "Для прошивки v4.6 і попередніх версій"

    Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте **APPLICATIONS** -> **GoodCloud**, вимкніть GoodCloud за допомогою перемикача та натисніть **Apply**.

    ![Вимкнення хмарного сервісу](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Після вимкнення інтерфейс матиме такий вигляд.

    ![Хмарний сервіс вимкнено](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Для прошивки v4.7 і новіших версій"

    Увійдіть у вебпанель адміністрування маршрутизатора та натисніть піктограму хмари у верхньому правому куті. У спливному вікні **Cloud Service** натисніть піктограму шестерні та виберіть **Disable**.

    ![Вимкнення хмарного сервісу](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Після вимкнення інтерфейс матиме такий вигляд.

    ![Хмарний сервіс вимкнено](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Видалення облікового запису {#delete-account}

З міркувань безпеки можна видалити обліковий запис, якщо ви більше ним не користуєтеся.

На платформі [GoodCloud](https://www.goodcloud.xyz){target="_blank"} натисніть ім’я користувача у верхньому правому куті та виберіть **Personal Center**. Прокрутіть сторінку донизу та натисніть **Delete Account**.

![Видалення облікового запису](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Видалення назавжди зітре всі пов’язані послуги, дані та особисту інформацію без можливості відновлення.

    Якщо ваш обліковий запис належить до будь-яких організацій, спочатку вийдіть з усіх організацій, а потім видаліть обліковий запис.

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
