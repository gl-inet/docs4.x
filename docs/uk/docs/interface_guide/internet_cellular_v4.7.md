# Підключення до інтернету через стільникову мережу (v4.7 і попередні версії) {#connect-to-the-internet-via-cellular-v47-and-earlier}

Вміст цієї сторінки ґрунтується на прошивці v4.7 і попередніх версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.7 і попередні версії" markdown="1">

- [Прошивка v4.10 і новіші версії](internet_cellular_v4.10.md)
- [Прошивка v4.8–v4.9](internet_cellular.md)

</div>

---

Більшість маршрутизаторів GL.iNet підтримують стільникове підключення. У цій інструкції описано три типи моделей:

1. **Моделі з вбудованим модулем 4G та однією SIM-картою**

    Деякі моделі, наприклад GL-XE300 (Puli), мають вбудований модуль 4G з одним слотом SIM. Див. [налаштування моделей з однією SIM-картою](#setup-for-single-sim-models).

2. **Моделі з підтримкою USB-модемів**

    Деякі моделі, наприклад GL-AXT1800 (Slate AX), мають порт USB і підтримують стільникове підключення через USB-модем. Налаштування подібне до моделей із вбудованим модулем 4G та однією SIM-картою. Див. [налаштування моделей з однією SIM-картою](#setup-for-single-sim-models).

3. **Моделі з вбудованим модулем 5G та двома SIM-картами**

    Деякі моделі, наприклад GL-X3000 (Spitz AX), мають вбудований модуль 5G із двома слотами SIM. Налаштування стільникового підключення у вебпанелі адміністрування можуть дещо відрізнятися. Див. [налаштування моделей із двома SIM-картами](#setup-for-dual-sim-models).

**Примітка:** деякі SIM-карти потрібно активувати перед першим використанням. Для забезпечення сумісності активуйте SIM-карту у смартфоні, перш ніж вставляти її в маршрутизатор.

## Налаштування моделей з однією SIM-картою {#setup-for-single-sim-models}

Наведені нижче дії стосуються моделей із вбудованим стільниковим модемом та одним слотом SIM (наприклад, GL-XE300 Puli) або портом USB для підключення зовнішнього USB-модема (наприклад, GL-AXT1800 Slate AX).

У цьому прикладі використано **GL-AXT1800 (Slate AX)** із зовнішнім USB-модемом.

Спочатку рекомендовано вимкнути маршрутизатор. Вставте попередньо активовану SIM-карту в USB-модем, підключіть модем до порту USB маршрутизатора, а потім увімкніть маршрутизатор.

Якщо підключити USB-модем після запуску маршрутизатора, вебпанель адміністрування може не оновитися автоматично. У такому разі оновіть сторінку або перезапустіть маршрутизатор.

### Автоматичне налаштування {#auto-setup}

Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **INTERNET** -> **Cellular**.

1. Під час першого відкриття сторінки з’єднання може не встановитися автоматично, але у верхньому лівому куті мають відображатися назва оператора та IMEI. Натисніть **Auto Setup**.

    Ігноруйте попередження *Incompatible Modem*.

    ![Автоматичне налаштування USB-модема](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Маршрутизатор розпочне підключення.

    **Примітка:** деякі SIM-карти можуть мати особливі обмеження, наприклад потребувати певної APN. Якщо SIM-карту не вдається зареєструвати, зверніться до оператора, щоб перевірити наявність таких обмежень.

    ![USB-модем підключається](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Після встановлення з’єднання на сторінці відобразяться відомості про мережу та зелена крапка, яка означає успішне підключення.

    ![USB-модем підключено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Примітка:** після початкового налаштування USB-модем автоматично розпізнаватиметься, якщо перезапустити маршрутизатор із підключеним модемом або підключити модем повторно. Мережеве з’єднання встановиться без повторного натискання Auto Setup.

Якщо автоматичне налаштування не вдається, спробуйте [ручне налаштування](#manual-setup).

### Ручне налаштування {#manual-setup}

У розділі Cellular натисніть **Manual Setup**, щоб переглянути або змінити налаштування стільникового підключення поточної SIM-карти.

**Примітка**: для деяких SIM-карт потрібна певна APN. Якщо SIM-карту не вдається зареєструвати, зверніться до оператора, щоб перевірити наявність обмежень. За потреби задайте правильну APN на маршрутизаторі.

Застосування змін призведе до повторного підключення.

![Ручне налаштування модема 4G](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: протокол стільникового зв’язку, наприклад 3G, QMI або QCM. Зазвичай визначається автоматично; за потреби змініть його відповідно до вимог модема й оператора.

- **Port**: послідовний порт для взаємодії зі стільниковим модемом. Зазвичай визначається автоматично й не потребує ручної зміни.

- **APN**: APN (Access Point Name) — параметр шлюзу, потрібний для підключення до стільникової мережі. Він дає змогу маршрутизатору підключатися до інтернету через мобільного оператора. Використовуйте APN за замовчуванням або задайте значення, надане оператором.

- **PIN**: якщо SIM-карту захищено PIN-кодом, введіть його тут. Якщо PIN-код не задано, поле можна залишити порожнім.

- **TTL**: TTL (Time To Live) визначає максимальний час існування пакетів у мережі. За замовчуванням маршрутизатор зменшує TTL вхідних пакетів від клієнтських пристроїв на 1 перед пересиланням. Цей параметр діє лише для IPv4.

    **Примітка**: щоб перевизначити або підмінити TTL, задайте тут фіксоване значення. Для більшості моделей введіть бажаний фактичний TTL плюс 1, щоб компенсувати автоматичне зменшення.

- **Service**: виберіть тип стільникового сервісу, щоб визначити мережеві технології, які використовуватиме модем.

- **Dial Number**: введіть номер для встановлення з’єднання, наданий оператором. Зазвичай його вже задано, а в більшості сучасних мереж поле можна залишити порожнім.

- **Authentication**: виберіть потрібний оператору метод автентифікації, наприклад NONE, PAP або CHAP. Якщо облікові дані не потрібні, зазвичай використовується NONE.

### Сумісні модеми {#compatible-modems}

Нижче наведено список підтримуваних модемів, які ми перевіряли раніше.

**SIMPoYo uFi** — компактний USB-модем із точкою доступу Wi-Fi, який підтримує підключення без додаткового налаштування для швидкого й надійного доступу до мережі. Він працює з більшістю маршрутизаторів GL.iNet, ноутбуками, зовнішніми акумуляторами, автомобільними портами USB та іншими джерелами живлення USB. До комплекту входить 10GB безкоштовних даних на 30 днів для використання у Великій Британії та 34 європейських країнах.

| Модель                                  | Стільниковий зв’язок | Тип       | Перевірено       | Примітки* |
| -------------------------------------- | -------- | ---------- | --------------- | --------- |
| [SIMPoYo SP-N150C4](https://www.gl-inet.com/campaign/simpoyo-ufi/)  | 4G    | USB-модем | GL.iNet |           |
| Quectel RM520N-GL                      | 5G       | Модуль     | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | Модуль     | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | Модуль     | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | Модуль     | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | Модуль     | anonymous       |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | Модуль     | anonymous       |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | Модуль     | anonymous       |           |
| Huawei E3276                           | 4G       | USB-модем | GL.iNet         |           |
| Huawei E3372h-153                      | 4G       | USB-модем | GL.iNet         | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G       | USB-модем | anonymous       | Host-less |
| Huawei E3372h-607                      | 4G       | USB-модем | GL.iNet         |           |
| Huawei K5161h                          | 4G       | USB-модем | anonymous       |           |
| ZTE MF833U1                            | 4G       | USB-модем | anonymous       | Host-less |
| ZTE MF79U                              | 4G       | USB-модем | GL.iNet         | Host-less |
| ZTE M823                               | 4G       | USB-модем | Arnas Risqianto |           |
| MeiG O4H13 (Qualcomm MDM9207)          | 4G       | USB-модем | GL.iNet         | Host-less |
| XTRONS 4G LTE USB Dongle               | 4G       | USB-модем | GL.iNet         | Host-less |

- **QMI**: цей модем підтримує режим QMI. Виберіть QMI як протокол і **/dev/cdc-wdm0** як послідовний порт стільникового маршрутизатора.

- **Host-less**: цей модем підтримує режим Tethering. Керуйте з’єднанням через інтерфейс Tethering маршрутизатора, а не через Cellular.

## Налаштування моделей із двома SIM-картами {#setup-for-dual-sim-models}

Наведені нижче дії стосуються моделей із вбудованим стільниковим модемом, який підтримує дві SIM-карти. Вебпанель адміністрування може дещо відрізнятися від моделей з однією SIM-картою.

У цьому прикладі використано **GL-X3000 (Spitz AX)**. Він підтримує Dual SIM, Single Standby: можна вставити дві SIM-карти для стільникового доступу, але одночасно активною може бути лише одна. Між SIM-картами можна перемикатися вручну.

Спочатку рекомендовано вимкнути маршрутизатор, вставити попередньо активовані SIM-карти у слоти, а потім увімкнути його. Якщо вставити SIM-карту після запуску маршрутизатора, вебпанель адміністрування може не оновитися автоматично. У такому разі оновіть сторінку або перезапустіть маршрутизатор.

### Автоматичне налаштування {#auto-setup_1}

Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **INTERNET** -> **Cellular**.

1. Якщо SIM-карту не вставлено, сторінка має такий вигляд.

    ![Модель із двома SIM: SIM-карту не виявлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Після вставлення SIM-карти маршрутизатор автоматично розпочне підключення.

    Якщо підключення успішне, сторінка має такий вигляд.

    ![Модель із двома SIM: підключення 5G](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Якщо з’єднання не встановлюється автоматично, натисніть **Auto Setup** і дочекайтеся підключення або спробуйте **Manual Setup**.

### Ручне налаштування {#manual-setup_1}

У розділі Cellular натисніть **Manual Setup**, щоб відкрити Cellular Settings.

![Налаштування стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Можна переглядати або змінювати налаштування стільникового підключення поточної SIM-карти. Тут також зберігаються попередньо налаштовані профілі; власні конфігурації можна вручну додавати до «Saved Settings».

### Налаштування слотів SIM-карт {#sim-card-slot-settings}

У розділі Cellular натисніть **Current SIM Card**.

![Модель із двома SIM: поточна SIM-карта](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Відкриється **SIM Card Slot Settings**.

![Налаштування слотів SIM-карт](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Якщо вставлено дві SIM-карти, можна увімкнути **Auto Switch**.

![Автоматичне перемикання SIM-карт](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **Auto Switch**: автоматичне перемикання між SIM 1 і SIM 2. Метод перевірки мережі для SIM Auto Switch такий самий, як на сторінці Multi-WAN.

- **Preferred SIM Card Slot**: виберіть пріоритетну SIM-карту — SIM 1 або SIM 2.

- **Failover Interval**: доступний діапазон — від 5 хвилин до 24 годин.

    Якщо після аварійного перемикання доступ до інтернету не відновився, пристрій повернеться до пріоритетного слота SIM і зачекає заданий інтервал перед наступною спробою перемикання.

    Цей параметр застосовується, коли ні пріоритетна, ні резервна SIM-карта не мають сигналу. Пристрій перемикатиметься між SIM-картами, доки одна з них не отримає придатний сигнал.

    ![Інтервал аварійного перемикання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Після увімкнення пристрій щодня перевірятиме пріоритетний слот SIM у заданий час і намагатиметься повернутися до нього, якщо пріоритетна SIM-карта знову матиме доступ до інтернету.

    Це запобігає надмірному використанню даних резервної SIM-карти. Якщо пріоритетна SIM-карта досі не має сигналу, пристрій продовжить використовувати резервну.

    ![Перевірка пріоритетного слота за розкладом](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Примітка**: Auto Switch не перемикає SIM-карту миттєво. Спочатку пристрою потрібен час, щоб переконатися, що поточна SIM-карта не має доступу до інтернету. Крім того, інша SIM-карта не перебуває в режимі очікування й потребує часу для активації.

## Статистика трафіку {#traffic-statistics}

У розділі Cellular натисніть **Traffic Statistics**.

![Статистика трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Відкриється сторінка Traffic Statistics.

![Статистика трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS {#sms}

Див. [SMS](../tutorials/sms.md).

## Пересилання SMS {#sms-forwarding}

Див. [пересилання SMS](../tutorials/sms_forwarding.md).

## Керування модемом {#modem-management}

У розділі Cellular натисніть кнопку **Tool** у верхньому правому куті, щоб відкрити сторінку Modem Management.

![Кнопка керування модемом](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Сторінка містить два розділи: **Modem Info** і **AT Command**.

![Керування модемом](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

Команди AT — стандартні інструкції для взаємодії зі стільниковим модемом.

Якщо для Shortcut вибрано **Manual command**, введіть потрібну команду в поле AT Command, щоб перевірити стан модема.

Також можна відкрити розкривний список Shortcut і вибрати одну з **попередньо заданих команд**.

![Попередньо задані команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/at_command_1.png){class="glboxshadow"}

Доступні такі попередньо задані команди:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

У цьому прикладі вибрано «Request IMEI». Натисніть «Send», щоб отримати результат, показаний нижче.

![Приклад попередньо заданої команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/at_command_2.png){class="glboxshadow"}

## Профілі оператора {#carrier-profile}

Можна зберігати різні профілі для одного або кількох операторів.

У розділі Cellular натисніть кнопку **Profile** у верхньому правому куті, щоб керувати профілями.

![Керування профілями](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Додайте новий профіль або збережіть поточний.

![Додавання профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Створіть власний профіль відповідно до вимог оператора.

![Створення профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Наступного разу можна вибрати збережений профіль.

![Вибір збереженого профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Виберіть потрібні профілі.

![Вибір профілів](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Фіксація базової станції {#lock-tower}

Ця функція доступна лише на деяких моделях, зокрема GL-X3000, GL-XE3000 і GL-X2000 (прошивка v4.7 або новіша).

Для поліпшення сигналу та стабільності стільникового з’єднання спробуйте зафіксувати базову станцію.

**Примітка:** зафіксована базова станція повинна відповідати частотним діапазонам, які підтримують оператор і пристрій; інакше з’єднання може не встановитися.

У розділі Cellular натисніть піктограму **Tower** у верхньому правому куті.

![Вибір базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Відобразяться доступні базові станції.

![Доступні базові станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Натисніть станцію, щоб переглянути відомості про неї та зафіксувати підключення до неї.

![Відомості про базову станцію](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

Угорі відобразиться стан станції, наприклад Locked/Unlocked.

![Стан фіксації базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Примітка**:

1. Коли інтерфейс Cellular увімкнено, пристрій може не виявити всі базові станції під час пошуку.

2. Якщо зафіксована базова станція не відповідає вибору діапазонів або параметрам APN у налаштуваннях стільникового підключення, маршрутизатор не зможе підключитися до стільникової мережі.

3. Якщо після фіксації базової станції перенести маршрутизатор в інше місце, після перезавантаження він і далі намагатиметься підключитися до цієї станції. Через це маршрутизатор може не підключитися автоматично до стільникової мережі на новому місці. У такому разі скасуйте поточну фіксацію або вручну зафіксуйте нову базову станцію.

## Історія рівня сигналу {#historical-signal-record}

У розділі Cellular натисніть піктограму **Signal** у верхньому правому куті, щоб переглянути історію рівня сигналу.

![Історія рівня сигналу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Це допомагає оцінити якість стільникового з’єднання. Якщо сигнал слабкий, спробуйте вибрати іншу базову станцію для кращого прийому.

Виберіть різні періоди, щоб переглянути історію рівня стільникового сигналу.

![Перегляд рівня сигналу за період](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Вибір частотних діапазонів {#band-masking}

У розділі Cellular натисніть **View More** і виберіть **Cells Info**, щоб переглянути відомості про комірки.

Відобразяться поточні діапазони та їхній стан сигналу.

![Відомості про комірки](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Якщо сигнал слабкий, увімкніть Band Masking для блокування певних діапазонів. Якщо сигнал добрий, можна дозволити маршрутизатору використовувати лише певні стільникові діапазони.

Натисніть **Manual Setup**, щоб відкрити Cellular Settings, і увімкніть **Band Masking**.

![Вибір частотних діапазонів](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Виберіть **Masking Mode** (Block або Open), а потім LTE Bands, 5G NSA Bands і 5G SA Bands.

## Усунення несправностей {#troubleshooting}

Якщо стільникове з’єднання не встановлюється, виберіть повідомлення про помилку нижче, щоб переглянути відповідні рішення.

??? note "No SIM / Your SIM card has not been detected"

    1. Оновіть сторінку та зачекайте кілька хвилин, щоб перевірити, чи виявлено SIM-карту.

    2. Переконайтеся, що SIM-карту встановлено правильно. Зіставте виріз на SIM-карті з відповідною позначкою слота, щоб перевірити орієнтацію вставлення.

    3. Вимкніть маршрутизатор, вийміть і знову вставте SIM-карту, а потім увімкніть маршрутизатор.

    4. За можливості спробуйте іншу SIM-карту.

    Якщо проблема не зникає, завантажте журнали та надішліть їх на [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Оновіть сторінку та зачекайте кілька хвилин, щоб перевірити, чи зникла помилка.

    2. Натисніть **Disconnect**/**Abort**, а потім **Connect**, щоб повторити підключення.

    3. Перезапустіть маршрутизатор.

    4. Перевірте стан SIM-карти й переконайтеся, що її активовано. Вставте її у смартфон, щоб перевірити доступ до інтернету з активним тарифним планом мобільних даних, або зверніться до оператора для перевірки.

    5. Деякі оператори можуть вимагати протокол 3G для мережевого підключення. Відкрийте **Manual Setup** -> **Cellular Settings** -> **Protocol**, виберіть **3G** і натисніть **Apply**.

        ![Вибір протоколу стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Пристрій автоматично спробує підключитися повторно. Зачекайте кілька хвилин, щоб перевірити успішність підключення.

    6. Деякі SIM-карти можуть мати особливі обмеження, наприклад потребувати певної APN. Якщо SIM-карту не вдається зареєструвати, зверніться до оператора, щоб перевірити наявність обмежень.

        За потреби відкрийте **Manual Setup** -> **Cellular Settings** -> **APN**, задайте правильну APN на маршрутизаторі та натисніть **Apply**.

    7. Натисніть **View More** і виберіть **Cells Info**, щоб перевірити рівень стільникового сигналу. Якщо сигнал слабкий, переконайтеся, що антену встановлено правильно. Перемістіть маршрутизатор на відкрите місце без перешкод для кращого прийому сигналу.

    8. Перевірте, чи увімкнено **Band Masking** або **Lock Tower**. Якщо так, вимкніть відповідну функцію та спробуйте підключитися знову.

    Якщо проблема не зникає, завантажте журнали та надішліть їх на [support@gl-inet.com](mailto:support@gl-inet.com).

## Сертифікація IoT {#iot-certification}

### Сертифікація AT&T {#att-certification}

Відкрийте сторінку [сертифікації пристроїв AT&T](https://iotdevices.att.com/certified-devices.aspx#) і введіть назву пристрою, щоб знайти його.

![Сертифікація AT&T](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![Сертифікація AT&T](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Сертифікація T-Mobile {#t-mobile-certification}

Відкрийте сторінку [сертифікації пристроїв T-Mobile](https://www.t-mobile.com/business/solutions/iot/device-certification){target="_blank"} і виберіть 5G у **Filter**, щоб знайти пристрій.

![Сертифікація T-Mobile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Пов’язані статті

- [Сторінка Internet](internet.md)
- [Налаштування пріоритету способів доступу до інтернету](multi-wan.md)
- [Налаштування балансування навантаження за одночасного використання кількох способів доступу до інтернету](multi-wan.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
