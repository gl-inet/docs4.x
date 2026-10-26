# Підключення до інтернету через стільникову мережу (v4.8-v4.9) {#connect-to-the-internet-via-cellular-v48-v49}

Ця сторінка описує прошивки від v4.8 до v4.9. Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.8 - v4.9" markdown="1">

- [Прошивка v4.10 та новіші версії](internet_cellular_v4.10.md)
- [Прошивка v4.7 та раніші версії](internet_cellular_v4.7.md)

</div>

---

Більшість маршрутизаторів GL.iNet підтримують підключення до стільникової мережі. Цей посібник охоплює три типи моделей:

1. **Моделі з вбудованим модулем 4G та одним слотом SIM**

    Деякі моделі мають вбудований модуль 4G та один слот SIM-картки, наприклад GL-E750 (Mudi). Дивіться [Налаштування моделей з однією SIM-карткою](#setup-for-single-sim-models).

2. **Моделі з вбудованим модулем 5G та двома слотами SIM**

    Деякі моделі мають вбудований модуль 5G та два слоти SIM-карток, наприклад GL-X3000 (Spitz AX). Налаштування стільникової мережі у вебпанелі адміністрування можуть дещо відрізнятися. Дивіться [Налаштування моделей із двома SIM-картками](#setup-for-dual-sim-models).

3. **Моделі, сумісні з USB-модемами**

    Деякі моделі не мають вбудованого слота SIM-картки, проте оснащені портом USB та підтримують підключення до стільникової мережі через USB-модем, наприклад GL-MT3000 (Beryl AX). Дивіться [Налаштування USB-модема](#setup-for-usb-modem).

**Примітка:** Деякі SIM-картки потребують активації перед першим використанням. Щоб забезпечити сумісність, активуйте SIM-картку в смартфоні перед установленням у маршрутизатор.

## Налаштування моделей з однією SIM-карткою {#setup-for-single-sim-models}

Наведені нижче дії стосуються моделей із вбудованим стільниковим модемом та одним слотом SIM-картки.

У цьому прикладі використовується **GL-E750 (Mudi)**.

Рекомендуємо спочатку вимкнути маршрутизатор, вставити попередньо активовану SIM-картку в слот, а потім увімкнути його. Якщо вставити SIM-картку після завантаження маршрутизатора, вебпанель адміністрування може не оновитися автоматично. У такому разі оновіть сторінку або перезавантажте маршрутизатор.

### Автоматичне налаштування {#auto-setup}

Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **INTERNET** -> **Cellular**.

1. Якщо SIM-картку не вставлено, на сторінці відображається повідомлення "Your SIM card has not been detected".

    ![SIM-картку не виявлено на моделі з одним слотом](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Вставте SIM-картку. Пристрій почне встановлювати з’єднання, як показано нижче.

    ![Установлення з’єднання через одну SIM-картку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Якщо з’єднання не встановлюється автоматично, натисніть кнопку **Connect**, якщо вона доступна.

    Якщо SIM-картку не виявлено, спробуйте перезавантажити маршрутизатор і перевірте, чи буде її виявлено.

3. Після підключення до стільникової мережі на сторінці з’являться відомості про мережу та зелена крапка, яка вказує на успішне з’єднання.

    ![Успішне з’єднання через одну SIM-картку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Якщо автоматичне налаштування не спрацювало, спробуйте [налаштувати вручну](#manual-setup-single-sim).

### Налаштування вручну {#manual-setup-single-sim}

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** і натисніть **SIM Card Settings**.

![Відкриття налаштувань SIM-картки](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Тут можна переглянути або змінити налаштування стільникової мережі для поточної SIM-картки.

**Примітка**: Для деяких SIM-карток потрібен певний APN. Якщо SIM-картка не реєструється в мережі, зверніться до оператора, щоб перевірити наявність обмежень. За потреби налаштуйте правильний APN на маршрутизаторі.

Застосування змін спричинить повторне встановлення з’єднання.

![Налаштування стільникової мережі для однієї SIM-картки](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name, назва точки доступу) — параметр шлюзу, потрібний для підключення до стільникової мережі. Він дає маршрутизатору змогу підключатися до інтернету, який надає мобільний оператор. Можна використовувати APN за замовчуванням або задати власний APN, наданий оператором.

- **Protocol**: Протокол зв’язку зі стільниковою мережею (наприклад, 3G, QMI або QCM). Зазвичай визначається автоматично; його можна змінити відповідно до вимог модема й оператора.

- **Port**: Послідовний порт для зв’язку зі стільниковим модемом. Зазвичай визначається автоматично й не потребує налаштування вручну.

- **TTL**: TTL (Time To Live, час життя) визначає максимальний час перебування пакетів у мережі. За замовчуванням перед пересиланням маршрутизатор зменшує TTL вхідних пакетів від клієнтських пристроїв на 1. Налаштування TTL діє лише для IPv4.

    **Примітка**: Щоб перевизначити або підмінити TTL, задайте тут фіксоване значення. Для більшості моделей уведіть бажаний кінцевий TTL плюс 1, щоб компенсувати автоматичне зменшення. Mudi 7 (GL‑E5800) застосовує введене значення без змін.

- **HL**: У IPv6 параметр HL (Hop Limit, межа переходів) обмежує кількість мережевих переходів для пакетів даних і є аналогом TTL у IPv4.

- **MTU**: Значення MTU за замовчуванням — 1500 байтів.

- **Authentication**: Виберіть метод автентифікації, потрібний вашому оператору (наприклад, NONE, PAP або CHAP). Якщо облікові дані не потрібні, зазвичай вибирають NONE.

- **Band Masking**: Увімкніть вибір частотних діапазонів, якщо маршрутизатор має блокувати певні діапазони або використовувати лише визначені діапазони стільникової мережі. Докладніше дивіться [тут](#band-masking).

## Налаштування моделей із двома SIM-картками {#setup-for-dual-sim-models}

Наведені нижче дії стосуються моделей із вбудованим стільниковим модемом, що підтримує дві SIM-картки. Сторінки можуть дещо відрізнятися від моделей з однією SIM-карткою.

У цьому прикладі використовується **GL-X3000 (Spitz AX)**. Він підтримує Dual SIM, Single Standby: можна встановити дві SIM-картки для доступу до стільникової мережі, проте одночасно активною може бути лише одна. Перемикатися між SIM-картками можна вручну.

Рекомендуємо спочатку вимкнути маршрутизатор, вставити попередньо активовані SIM-картки в слоти, а потім увімкнути його. Якщо вставити SIM-картку після завантаження маршрутизатора, вебпанель адміністрування може не оновитися автоматично. У такому разі оновіть сторінку або перезавантажте маршрутизатор.

### Автоматичне налаштування {#auto-setup_1}

Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **INTERNET** -> **Cellular**.

1. Якщо SIM-картку не вставлено, на сторінці відображається повідомлення "Your SIM card has not been detected".

    ![SIM-картку не виявлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Коли SIM-картку вставлено, сторінка матиме такий вигляд. Натисніть **Connect**.

    ![Стільникове з’єднання не встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Якщо SIM-картку не виявлено, спробуйте перезавантажити маршрутизатор і перевірте, чи буде її виявлено.

3. Після підключення до стільникової мережі на сторінці з’являться відомості про мережу та зелена крапка, яка вказує на успішне з’єднання.

    ![Стільникове з’єднання встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Натисніть **View More Information**, щоб переглянути додаткові відомості про стільникове з’єднання: модем, SIM-картку, інтернет і сигнал стільникової мережі.

    ![Перегляд додаткової інформації про з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![Відомості про стільникове з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Якщо автоматичне налаштування не спрацювало, спробуйте [налаштувати вручну](#manual-setup-dual-sim).

### Налаштування вручну {#manual-setup-dual-sim}

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** і натисніть **SIM Card Settings**.

![Відкриття налаштувань SIM-картки](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Тут можна переглянути або змінити налаштування стільникової мережі для поточної SIM-картки.

**Примітка**: Для деяких SIM-карток потрібен певний APN. Якщо SIM-картка не реєструється в мережі, зверніться до оператора, щоб перевірити наявність обмежень. За потреби налаштуйте правильний APN на маршрутизаторі.

Застосування змін спричинить повторне встановлення з’єднання.

![Налаштування стільникової мережі для двох SIM-карток](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name, назва точки доступу) — параметр шлюзу, потрібний для підключення до стільникової мережі. Він дає маршрутизатору змогу підключатися до інтернету, який надає мобільний оператор. Можна використовувати APN за замовчуванням або задати власний APN, наданий оператором.

- **Protocol**: Протокол зв’язку зі стільниковою мережею (наприклад, QMI або QCM), автоматично визначений відповідно до модема й оператора.

- **Port**: Автоматично визначений послідовний порт для зв’язку зі стільниковим модемом.

- **TTL**: TTL (Time To Live, час життя) визначає максимальний час перебування пакетів у мережі. За замовчуванням перед пересиланням маршрутизатор зменшує TTL вхідних пакетів від клієнтських пристроїв на 1. Налаштування TTL діє лише для IPv4.

    **Примітка**: Щоб перевизначити або підмінити TTL, задайте тут фіксоване значення. Для більшості моделей уведіть бажаний кінцевий TTL плюс 1, щоб компенсувати автоматичне зменшення. Mudi 7 (GL‑E5800) застосовує введене значення без змін.

- **HL**: У IPv6 параметр HL (Hop Limit, межа переходів) обмежує кількість мережевих переходів для пакетів даних і є аналогом TTL у IPv4.

- **MTU**: Значення MTU за замовчуванням — 1500 байтів.

- **Authentication**: Виберіть метод автентифікації, потрібний вашому оператору (наприклад, NONE, PAP або CHAP). Якщо облікові дані не потрібні, зазвичай вибирають NONE.

- **Band Masking**: Увімкніть вибір частотних діапазонів, якщо маршрутизатор має блокувати певні діапазони або використовувати лише визначені діапазони стільникової мережі. Докладніше дивіться [тут](#band-masking).

### Налаштування слотів SIM-карток {#sim-card-slot-settings}

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** і натисніть **SIM Card Switch**.

![Відкриття налаштувань перемикання SIM-карток](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

З’являться перемикач автоматичного перемикання, активна SIM-картка, ICCID і оператор мережі.

![Стан слотів SIM-карток](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Якщо вставлено дві SIM-картки, можна ввімкнути **Auto Switch**.

![Увімкнення автоматичного перемикання SIM-карток](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

- **Auto Switch**: Умикає автоматичне перемикання між SIM 1 і SIM 2. Для автоматичного перемикання SIM використовується той самий метод перевірки мережі, який налаштовано на сторінці Multi-WAN.

- **Preferred SIM Card Slot**: Виберіть пріоритетну SIM-картку — SIM 1 або SIM 2.

- **Failover Interval**: Доступні значення від 5 хвилин до 24 годин.

    Якщо після аварійного перемикання доступу до інтернету досі немає, пристрій повернеться до пріоритетного слота SIM і зачекає цей інтервал перед повторною спробою аварійного перемикання.

    Цей параметр застосовується, коли ані пріоритетна, ані резервна SIM-картка не мають сигналу. Пристрій перемикатиметься між SIM-картками, доки одна з них не отримає придатний сигнал.

    ![Інтервал аварійного перемикання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Коли ввімкнено, пристрій щодня у встановлений час перевіряє пріоритетний слот SIM і намагається повернутися до нього, якщо пріоритетна SIM-картка знову отримала доступ до інтернету.

    Це запобігає надмірному використанню трафіку резервною SIM-карткою. Якщо пріоритетна SIM-картка досі не має сигналу, пристрій продовжить використовувати резервну SIM-картку.

    ![Перевірка пріоритетного слота за розкладом](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Примітка**: Функція Auto Switch не перемикає на іншу SIM-картку миттєво. По-перше, пристрою потрібен час, щоб підтвердити відсутність доступу до інтернету через поточну SIM-картку. По-друге, інша SIM-картка не перебуває в режимі очікування, тому її активація також потребує часу.

## Налаштування USB-модема {#setup-for-usb-modem}

Наведені нижче дії стосуються моделей без вбудованого слота SIM-картки, які мають порт USB для підключення зовнішнього USB-модема.

У цьому прикладі використовується **GL-MT3000 (Beryl AX)** із зовнішнім USB-модемом **SIMPoYo uFi**.

Рекомендуємо спочатку вимкнути маршрутизатор, вставити попередньо активовану SIM-картку в USB-модем, підключити модем до порту USB маршрутизатора, а потім увімкнути маршрутизатор. Якщо підключити USB-модем після завантаження маршрутизатора, вебпанель адміністрування може не оновитися автоматично. У такому разі оновіть сторінку або перезавантажте маршрутизатор.

### Швидке налаштування {#quick-setup}

1. Спочатку вимкніть маршрутизатор. Вставте SIM-картку в USB-модем, підключіть модем до порту USB маршрутизатора та ввімкніть маршрутизатор.

2. Увійдіть у вебпанель адміністрування маршрутизатора, перейдіть до **INTERNET** -> **Tethering** і натисніть **Connect**.

    ![Підключення USB-модема](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Якщо потрібно змінити додаткові параметри (наприклад, TTL, HL або MTU), натисніть **Advanced**, налаштуйте їх, а потім натисніть **Connect**.

    ![Додаткові налаштування USB-модема](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    Почнеться встановлення з’єднання.

    ![Установлення з’єднання через USB-модем](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Після підключення на сторінці з’являться відомості про мережу та зелена крапка, яка вказує на успішне з’єднання.

    ![Успішне з’єднання через USB-модем](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Примітка:** Після початкового налаштування, якщо перезавантажити маршрутизатор із підключеним USB-модемом або від’єднати й знову підключити модем, він розпізнаватиметься автоматично. Мережеве з’єднання встановлюватиметься без повторного натискання кнопки підключення.

### Сумісні модеми {#compatible-modems}

Нижче наведено список підтримуваних модемів, які ми раніше перевірили.

**SIMPoYo uFi** — компактний USB-модем із підтримкою plug & play та точкою доступу Wi-Fi, призначений для швидкого й надійного з’єднання в будь-якому місці. Він працює з більшістю маршрутизаторів GL.iNet, а також із ноутбуками, зовнішніми акумуляторами, автомобільними портами USB та іншими джерелами живлення USB. До комплекту входять 10GB безкоштовного трафіку на 30 днів, що діють у Великій Британії та 34 європейських країнах.

| Модель                                 | Мережа   | Тип        | Перевірено      | Примітки* |
| -------------------------------------- | -------- | ---------- | --------------- | --------- |
| [SIMPoYo SP-N150C4](https://www.gl-inet.com/campaign/simpoyo-ufi/)  | 4G    | USB-модем | GL.iNet |           |
| Quectel RM520N-GL                      | 5G       | Модуль     | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G       | Модуль     | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G       | Модуль     | GL.iNet         |           |
| Quectel EC200A series                  | 4G       | Модуль     | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G       | Модуль     | анонімний користувач |           |
| Quectel EM060K-GL, EM120K-GL           | 4G       | Модуль     | анонімний користувач |           |
| Quectel EM120R-GL, EM160R-GL           | 4G       | Модуль     | анонімний користувач |           |
| Huawei E3276                           | 4G       | USB-модем | GL.iNet         |           |
| Huawei E3372h-153                      | 4G       | USB-модем | GL.iNet         | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G       | USB-модем | анонімний користувач | Host-less |
| Huawei E3372h-607                      | 4G       | USB-модем | GL.iNet         |           |
| Huawei K5161h                          | 4G       | USB-модем | анонімний користувач |           |
| ZTE MF833U1                            | 4G       | USB-модем | анонімний користувач | Host-less |
| ZTE MF79U                              | 4G       | USB-модем | GL.iNet         | Host-less |
| ZTE M823                               | 4G       | USB-модем | Arnas Risqianto |           |
| MeiG O4H13 (Qualcomm MDM9207)          | 4G       | USB-модем | GL.iNet         | Host-less |
| XTRONS 4G LTE USB Dongle               | 4G       | USB-модем | GL.iNet         | Host-less |

- **QMI**: Цей модем підтримує режим QMI. У налаштуваннях SIM-картки виберіть QMI як протокол зв’язку зі стільниковою мережею та **/dev/cdc-wdm0** як послідовний порт.

- **Host-less**: Цей модем підтримує режим Tethering. Керуйте з’єднанням через інтерфейс Tethering маршрутизатора, а не через Cellular.

## Статистика трафіку {#traffic-statistics}

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** і натисніть **Data Used**.

![Відкриття статистики трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Відкриється сторінка статистики трафіку. Тут відображається використаний трафік SIM-карток і можна налаштувати його обмеження.

![Статистика трафіку SIM-карток](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Якщо Data Used перевищує Data Cap Amount, вручну змініть **Data Cap Amount** або **Data Used**. Інакше мережеве з’єднання може бути розірване або може відбутися автоматичне перемикання SIM-картки (для моделей із двома SIM-картками).

- **Зміна використаного трафіку**

    Натисніть **Modify** праворуч від SIM 1/2 Data Used.

    ![Зміна використаного трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Після цього можна змінити або скинути значення використаного трафіку.

    ![Редагування або скидання обліку трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **Налаштування обмеження трафіку SIM-картки**

    Щоб налаштувати обмеження трафіку SIM-картки, спочатку ввімкніть **Save data when power off**. Це дає змогу зберігати дані обліку трафіку навіть після вимкнення пристрою.

    ![Збереження обліку трафіку після вимкнення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Потім увімкніть Limit Settings для SIM 1 або SIM 2.

    ![Налаштування обмеження трафіку SIM-картки](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Для моделей із двома SIM-картками рекомендуємо одночасно ввімкнути **SIM Card Slot Auto Switch**. Якщо задано SIM 1 Data Cap Amount і ввімкнено SIM Card Slot Auto Switch, після перевищення ліміту трафіку SIM 1 автоматично перемкнеться на SIM 2, а SIM 1 буде вимкнено.

## Історія сигналу {#historical-signal-record}

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** і натисніть **Historical Signal Record**.

![Відкриття історії сигналу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Тут можна перевірити якість стільникового з’єднання. Якщо сигнал слабкий, спробуйте перемкнутися на іншу базову станцію, щоб отримати кращий сигнал.

![Історія сигналу стільникової мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![Показники сигналу стільникової мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Щоб переглянути історію рівня сигналу, виберіть потрібний проміжок часу у верхньому правому куті.

![Вибір періоду історії сигналу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Вибір частотних діапазонів {#band-masking}

Band Masking дає змогу блокувати певні частотні діапазони або використовувати лише бажані діапазони стільникової мережі, щоб поліпшити слабкий сигнал.

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular** -> **SIM Card Settings** та ввімкніть **Enable Band Masking**.

![Вибір частотних діапазонів](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Виберіть **Masking Mode** (Block або Open), а потім діапазони LTE Bands, 5G NSA Bands і 5G SA Bands.

## SMS {#sms}

Дивіться [SMS](../tutorials/sms.md).

## Перенаправлення SMS {#sms-forwarding}

Дивіться [Перенаправлення SMS](../tutorials/sms_forwarding.md).

## Фіксація базової станції {#lock-tower}

!!! note "Підтримувані моделі"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) підтримує цю функцію у прошивці v4.7 та новіших версіях.

Щоб отримати якісний сигнал і забезпечити стабільне стільникове з’єднання, спробуйте зафіксувати базову станцію.

**Примітка:** Вибрана базова станція має працювати в частотних діапазонах, які підтримують ваш оператор і пристрій; інакше з’єднання може не встановитися.

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular**. Натисніть значок із трьома крапками вгорі праворуч і виберіть **Lock Tower**.

![Відкриття фіксації базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Натисніть **Scan**, щоб почати пошук базових станцій стільникової мережі. Це займе кілька хвилин. Не оновлюйте сторінку під час пошуку.

![Пошук базових станцій](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

З’явиться список доступних базових станцій.

![Список доступних базових станцій](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Натисніть базову станцію, щоб переглянути відомості та зафіксувати її.

![Відомості про базову станцію та її фіксація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Примітка**:

1. Коли інтерфейс Cellular увімкнений, пристрій може не знайти всі базові станції.

2. Якщо зафіксована базова станція не відповідає параметрам вибору частотних діапазонів або APN у налаштуваннях стільникової мережі, маршрутизатор не зможе підключитися до стільникової мережі.

3. Якщо після фіксації базової станції перенести маршрутизатор в інше місце, після перезавантаження він і далі намагатиметься підключитися до зафіксованої станції. Через це він може не підключитися автоматично до стільникової мережі в новому місці. У такому разі скасуйте фіксацію поточної базової станції або вручну зафіксуйте нову.

## Фіксація оператора {#lock-operator}

!!! note "Підтримувані моделі"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) підтримує цю функцію у прошивці v4.8 та новіших версіях.

Якщо зафіксувати певного мобільного оператора, маршрутизатор використовуватиме лише його мережу. Це забезпечує стабільне з’єднання та запобігає непередбаченим витратам на роумінг, особливо в прикордонних районах, де пристрій інакше міг би підключатися до іноземних мереж.

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular**. Натисніть значок із трьома крапками вгорі праворуч і виберіть **Lock Operator**.

![Відкриття фіксації оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Доступні три режими фіксації:

- **Auto**: Автоматичне підключення до доступної мережі оператора.
- **Manual**: Фіксація певного оператора вручну.
- **Manual-Auto**: Автоматичне перемикання на доступну мережу оператора, якщо фіксація вручну не спрацювала.

![Режими фіксації оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## AT-команди модема {#modem-at-command}

AT-команди модема — стандартні інструкції для взаємодії зі стільниковим модемом. Ця функція дає змогу надсилати команди та перевіряти стан модема.

У вебпанелі адміністрування маршрутизатора перейдіть до **INTERNET** -> **Cellular**. Натисніть значок із трьома крапками вгорі праворуч і виберіть **Modem AT Command**.

![Відкриття сторінки AT-команд](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Відкриється сторінка AT Command.

![Сторінка AT-команд модема](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Якщо для Shortcut вибрано **Manual command**, уведіть потрібну команду в поле AT Command.

Також можна відкрити розкривний список Shortcut і вибрати одну з **готових команд**.

![Вибір готової AT-команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Доступні такі готові команди:

* Request IMEI
* Request QCCID
* Request IMSI
* Check Signal Quality
* Reset modem
* Operator Names
* Request SIM card status

У цьому прикладі вибрано команду "Request IMEI". Натисніть "Send", щоб отримати результат, як показано нижче.

![Результат виконання AT-команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

У нижньому правому куті натисніть **Export Debug Info**, щоб завантажити файл .json.

![Експорт інформації для налагодження](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Усунення несправностей {#troubleshooting}

Якщо не вдалося встановити стільникове з’єднання, натисніть відповідне повідомлення про помилку нижче, щоб переглянути способи усунення.

??? note "No SIM / Your SIM card has not been detected"

    ![SIM-картку не виявлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Спробуйте такі дії для усунення несправності.

    1. Оновіть сторінку та зачекайте кілька хвилин, щоб перевірити, чи буде виявлено SIM-картку.

    2. Переконайтеся, що SIM-картку встановлено правильно. Зіставте виріз на SIM-картці з відповідною позначкою на слоті, щоб перевірити напрямок установлення.

    3. Вимкніть маршрутизатор, вийміть і знову вставте SIM-картку, а потім увімкніть маршрутизатор.

    4. Якщо є інша SIM-картка, спробуйте використати її.

    Якщо проблема залишається, завантажте журнали та надішліть їх на адресу [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Ця проблема може супроводжуватися двома повідомленнями про помилку:

    - «SIM card not registered»

        ![SIM-картка не зареєстрована в мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - «The interface is connected, but the Internet can't be accessed»

        ![З’єднання встановлено, але інтернет недоступний](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Спробуйте такі дії для усунення несправності.

    1. Оновіть сторінку та зачекайте кілька хвилин, щоб перевірити, чи зникне помилка.

    2. Натисніть **Disconnect**/**Abort**, а потім **Connect**, щоб спробувати підключитися знову.

    3. Перезавантажте маршрутизатор.

    4. Перевірте стан SIM-картки та переконайтеся, що її активовано. Вставте SIM-картку в смартфон, щоб перевірити, чи працює доступ до інтернету за активного тарифного плану з мобільними даними, або зверніться до оператора для перевірки.

    5. Деяким операторам для підключення до мережі може бути потрібен протокол 3G. Перейдіть до **SIM Card Settings** -> **Protocol**, виберіть **3G** і натисніть **Apply**.

        ![Вибір протоколу зв’язку зі стільниковою мережею](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Пристрій автоматично спробує підключитися знову. Зачекайте кілька хвилин, щоб перевірити, чи встановлено з’єднання.

        ![Установлення з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Після успішного підключення сторінка матиме такий вигляд.

        ![Успішне з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Деякі SIM-картки можуть мати особливі обмеження використання (наприклад, потребувати певного APN). Якщо SIM-картка не реєструється в мережі, зверніться до оператора, щоб перевірити наявність обмежень.

        За потреби перейдіть до **SIM Card Settings** -> **APN**, налаштуйте правильний APN на маршрутизаторі та натисніть **Apply**.

        ![Налаштування APN](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Натисніть **View More Information**, щоб перевірити рівень сигналу стільникової мережі. Якщо сигнал слабкий, переконайтеся, що антену встановлено правильно. Перемістіть маршрутизатор у відкрите місце без перешкод для кращого приймання сигналу.

        ![Рівень сигналу стільникової мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

    8. Перевірте, чи ввімкнено **Band Masking** або **Lock Tower**. Якщо так, вимкніть функцію та спробуйте підключитися знову.

    Якщо проблема залишається, завантажте журнали та надішліть їх на адресу [support@gl-inet.com](mailto:support@gl-inet.com).

## Сертифікація IoT {#iot-certification}

### Сертифікація AT&T {#att-certification}

Перейдіть за посиланням [сертифікації пристроїв AT&T](https://iotdevices.att.com/certified-devices.aspx#) і введіть назву пристрою, щоб знайти його.

![Сертифікація пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![Сертифікація пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### Сертифікація T-Mobile {#t-mobile-certification}

Перейдіть за посиланням [сертифікації пристроїв T-Mobile](https://www.t-mobile.com/business/solutions/iot/device-certification){target="_blank"} і виберіть 5G у **Filter**, щоб знайти пристрій.

![Сертифікація пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}


---

Пов’язані статті

- [Сторінка інтернету](internet.md)
- [Як установити пріоритет кожного способу доступу до інтернету?](multi-wan.md)
- [Як налаштувати балансування навантаження за одночасного використання кількох способів доступу до інтернету?](multi-wan.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
