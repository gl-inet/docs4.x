# Підключення до інтернету через наявну мережу Wi-Fi за допомогою ретранслятора {#connect-to-the-internet-via-an-existing-wi-fi-by-repeater}

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Режим Repeater дає змогу підключити маршрутизатор до іншої наявної бездротової мережі, наприклад до безкоштовного Wi-Fi у готелі або кафе.

За замовчуванням він працює в режимі WISP (Wireless Internet Service Provider). Маршрутизатор створює власну підмережу та діє як міжмережевий екран, захищаючи вас від публічної мережі.

## Основні кроки {#basic-steps}

Увійдіть у вебпанель адміністрування маршрутизатора, перейдіть до розділу **INTERNET** -> **Repeater** і натисніть **Connect**.

![Розділ ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

У списку доступних мереж виберіть мережу Wi-Fi, до якої хочете підключитися.

![Вибір мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

!!! note

    1. На сторінці показано канали Wi-Fi, які підтримує маршрутизатор. Переконайтеся, що мережа Wi-Fi, до якої ви підключаєтеся, використовує один із цих каналів; інакше вона може не відображатися у списку доступних мереж.

    2. Під час пошуку Personal Hotspot на iPhone залишайте екран iPhone розблокованим, щоб підтримувати безперервне передавання сигнальних кадрів Wi-Fi. Інакше маршрутизатор може не виявити цю точку доступу.

Уведіть правильний пароль Wi-Fi та натисніть **Apply**.

![Уведення пароля Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Якщо потрібного SSID Wi-Fi немає у списку Available Network, натисніть **Join Other Network** угорі праворуч і вручну введіть SSID Wi-Fi та інші потрібні відомості. Докладні кроки наведено [тут](#join-other-network).

![Підключення до іншої мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Для підключення до публічних точок доступу, наприклад у готелях, аеропортах або торговельних центрах, дивіться розділ [Публічні точки доступу](#for-public-hotspot).

Інші параметри описано в розділі [Додаткові налаштування](#advanced-settings).

Якщо пароль правильний, за деякий час з’єднання буде встановлено.

![Установлене з’єднання ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## Публічні точки доступу {#for-public-hotspot}

Під час підключення маршрутизатора до публічної точки доступу з порталом авторизації ввімкнення наведених нижче функцій може підвищити ймовірність успішного з’єднання.

![Налаштування для публічної точки доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    Ця функція доступна починаючи з v4.6.

    Якщо цей параметр увімкнено, маршрутизатор автоматично перейде в Login Mode for Public Hotspots після успішного підключення до точки доступу, якщо доступу до інтернету немає. **У цьому режимі роботу деяких служб буде призупинено, а режим DNS зміниться на автоматичний**, через що відомості про вашу мережеву активність можуть стати доступними постачальнику точки доступу (наприклад, готелю або торговельному центру).

    Навіть якщо цей параметр вимкнено, маршрутизатор запропонує перейти в цей режим, коли виявить портал авторизації точки доступу та не зможе успішно ввійти.

    ![Режим входу для публічних точок доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    Якщо ввімкнено, маршрутизатор маскуватиметься під клієнтський пристрій, з якого ви відкрили панель адміністрування, імітуючи його MAC-адресу.

- **MAC Mode**

    Виберіть MAC-адресу, яку маршрутизатор використовуватиме для підключення до публічної точки доступу.

    - **Factory**: Використовує початкову MAC-адресу пристрою, призначену виробником.

    - **Clone**: Клонує MAC-адресу клієнтського пристрою для підключення. Якщо потрібної MAC-адреси немає у списку, введіть її вручну.

        **Примітка**: Багато сучасних пристроїв використовують випадкові MAC-адреси під час підключення до мереж Wi-Fi (часто цей параметр називається Private Wi-Fi Address або random hardware address). Через це показана тут MAC-адреса може не збігатися з фізичною MAC-адресою пристрою.

    - **Random**: Автоматично створює випадкову MAC-адресу для підключення.

    Під час збереження конфігурації мережі MAC Mode, зокрема клонована або випадкова MAC-адреса, прив’язується до конкретного збереженого SSID. Ці параметри можна вручну змінити для кожного SSID у будь-який час.

- **Auto Update MAC**: Якщо ввімкнено, MAC-адреса може оновлюватися автоматично.

## Додаткові налаштування {#advanced-settings}

Під час підключення до мережі доступні додаткові параметри.

![Додаткові налаштування ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: Увімкніть цей параметр, щоб запам’ятати поточну мережу Wi-Fi, до якої підключено ретранслятор.

* **Lock BSSID**: Якщо ввімкнено, маршрутизатор підключатиметься лише до конкретної точки доступу (AP), що відповідає вибраному BSSID, навіть якщо інші точки доступу мають той самий SSID.

* **Manually Set Static IP**: Якщо ввімкнено, можна вручну задати фіксовану IPv4-адресу, маску підмережі, шлюз і DNS-сервери для з’єднання ретранслятора замість автоматичного отримання цих параметрів.

    ![Задання статичної IP-адреси](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live, час життя) визначає максимальний час перебування пакетів у мережі та задається відповідно до вимог оператора. За замовчуванням маршрутизатор пересилає пакети від клієнтських пристроїв, зменшуючи їхній TTL на 1. Налаштування TTL діє лише для IPv4.

    **Примітка**: Якщо потрібно замаскувати TTL, задайте тут фіксоване значення. Для більшості моделей уведіть бажаний кінцевий TTL плюс 1, щоб компенсувати автоматичне зменшення. Mudi 7 (GL‑E5800) застосовує введене значення без змін.

* **HL**: У IPv6 поле HL (Hop Limit, межа переходів) обмежує кількість мережевих переходів для пакетів даних і є аналогом TTL у IPv4.

* **MTU**: Значення за замовчуванням — 1500.

## Параметри ретранслятора {#repeater-options}

Натисніть значок шестірні у верхньому правому куті, щоб налаштувати параметри ретранслятора.

![Параметри ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Вигляд сторінки може відрізнятися залежно від версії прошивки.

![Параметри ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching to Other Saved Networks**: Якщо ввімкнено, маршрутизатор автоматично підключатиметься до інших збережених мереж, коли поточна мережа Wi-Fi стане недоступною.

* **Band Selection**: Якщо вручну вибрати діапазон, маршрутизатор шукатиме мережі Wi-Fi та підключатиметься до них лише в цьому частотному діапазоні.

## Керування відомими мережами {#manage-known-network}

Щоб керувати відомими мережами, натисніть **Switch Network**.

![Перемикання мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Якщо з’єднання з мережею не встановлено, можна також натиснути **Connect** у розділі Repeater.

![Розділ ретранслятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

У розділі **Known Networks** натисніть значок кошика, щоб видалити відому мережу, або значок шестірні, щоб налаштувати її.

![Керування відомими мережами](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Підключення до іншої мережі {#join-other-network}

Якщо SSID немає у списку Available Networks або його приховано, натисніть **Join Other Network**.

![Відкриття підключення до іншої мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Уведіть SSID, виберіть Security та введіть пароль, якщо він потрібен.

![Уведення параметрів іншої мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

Для **Security** доступні два або три варіанти залежно від моделі.

* None — пароль не потрібен.
* WPA/WPA2/WPA3 — поширений варіант, який підтримує майже кожна мережа Wi-Fi.
* WPA/WPA2/WPA3 Enterprise — потребує автентифікації за протоколом Extensible Authentication Protocol (EAP). Для підключення потрібні дійсні ім’я користувача та пароль; зазвичай цей варіант використовується в корпоративних мережах або мережах навчальних закладів.

    ![Підключення до мережі з EAP](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    Докладні інструкції з підключення ретранслятора до мереж EAP наведено [тут](../tutorials/eap.md){target="_blank"}.

## Повторне підключення {#reconnection}

У наведених нижче випадках маршрутизатор періодично намагатиметься автоматично підключитися до Wi-Fi знову. За потреби це можна вимкнути вручну. Якщо помилка пов’язана з SSID або паролем, видаліть мережу з Known Networks, щоб усунути її.

1. Під час налаштування ретранслятора введено неправильний SSID або пароль.

2. Після початкового підключення маршрутизатор переміщено за межі покриття маршрутизатора вищого рівня.

3. Після підключення маршрутизатор вищого рівня змінив SSID або пароль чи обмежив доступ.

Повторне підключення має три окремі етапи: очікування, пошук і встановлення з’єднання.

1. Очікування: проблем немає; маршрутизатор очікує умов для повторного підключення.

2. Пошук: у частотному діапазоні, який сканується, можуть втрачатися пакети. Нові пристрої можуть мати проблеми з підключенням. На моделях GL-AXT1800/GL-AX1800 гостьову мережу Wi-Fi буде тимчасово вимкнено.

3. Установлення з’єднання: основна мережа Wi-Fi у цільовому діапазоні може перерватися на кілька секунд під час відновлення з’єднання.

**Примітка**: Проблеми зазвичай виникають на етапах пошуку та встановлення з’єднання.

## Усунення несправностей {#troubleshooting}

Якщо маршрутизатор підключено до мережі Wi-Fi як ретранслятор, але інтернет недоступний, з’явиться жовте повідомлення, як показано нижче.

**"The interface is connected, but the Internet can't be accessed."**

![З’єднання встановлено, але інтернет недоступний](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

Щоб усунути проблему:

1. Перевірте, чи має пристрій вищого рівня (тобто мережа Wi-Fi, до якої підключено маршрутизатор) доступ до інтернету.

2. Відкрийте сторінку [Multi-WAN](multi-wan.md) і перевірте стан інтерфейсу ретранслятора.

## DFS {#dfs}

**DFS** (Dynamic Frequency Selection, динамічний вибір частоти) — механізм автоматичного перемикання каналів Wi-Fi для уникнення перешкод радіолокаційним сигналам. Під час підключення до мережі Wi-Fi вищого рівня в діапазоні 5 ГГц маршрутизатор використовуватиме або не використовуватиме канал DFS відповідно до цієї мережі.

* Якщо мережа Wi-Fi вищого рівня використовує канал DFS і доступна для пошуку, маршрутизатор використовуватиме той самий канал для своєї мережі Wi-Fi у діапазоні 5 ГГц.

* Якщо мережа Wi-Fi вищого рівня недоступна для пошуку або з’єднання не встановлюється, маршрутизатор перемкне свою мережу Wi-Fi у діапазоні 5 ГГц на канал без DFS.

??? "Підтримувані моделі"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Моделі без підтримки"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Пов’язані статті

- [Сторінка інтернету](internet.md)
- [Як установити пріоритет кожного способу доступу до інтернету?](multi-wan.md)
- [Як налаштувати балансування навантаження за одночасного використання кількох способів доступу до інтернету?](multi-wan.md)
- [Як дізнатися MAC-адреси LAN і Wi-Fi](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
