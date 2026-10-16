# Підключення до інтернету через стільникову мережу (v4.10) {#connect-to-the-internet-via-cellular-v410}

Вміст цієї сторінки ґрунтується на прошивці v4.10 і новіших версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.10 і новіші версії" markdown="1">

- [Прошивка v4.8–v4.9](internet_cellular.md)
- [Прошивка v4.7 і попередні версії](internet_cellular_v4.7.md)

</div>

---

Більшість маршрутизаторів GL.iNet підтримують стільникове підключення. У цій інструкції описано підключення до стільникової мережі для двох типів маршрутизаторів:

1. **Маршрутизатори з вбудованим стільниковим модемом**

    Маршрутизатори GL.iNet зі стільниковим підключенням мають вбудований модуль 4G/5G та один або два слоти для SIM-карт, наприклад Spitz AX (GL-X3000) і Mudi 7 (GL-E5800). Налаштування стільникового підключення у вебпанелі адміністрування можуть дещо відрізнятися залежно від моделі та версії прошивки. Налаштування цих моделей описано в розділі [маршрутизатори з вбудованим стільниковим модемом](#cellular-routers).

2. **Маршрутизатори без вбудованого стільникового модема**

    До цієї категорії належать інші типи маршрутизаторів, зокрема домашні, дорожні, мініатюрні маршрутизатори та шлюзи безпеки. Зазвичай вони мають порт USB, до якого можна підключити USB-модем (не входить до комплекту) для стільникового доступу. Налаштування цих моделей описано в розділі [маршрутизатори без вбудованого стільникового модема](#non-cellular-routers).

**Примітка:** деякі SIM-карти потрібно активувати перед першим використанням. Для забезпечення сумісності активуйте SIM-карту у смартфоні, перш ніж вставляти її в маршрутизатор.

## Маршрутизатори з вбудованим стільниковим модемом {#cellular-routers}

У цьому розділі налаштування стільникового підключення та пов’язані функції описано на прикладі **Mudi 7 (GL-E5800)**.

Mudi 7 має вбудовану eSIM і два слоти Nano-SIM із підтримкою Dual SIM Dual Standby, тому його вебпанель адміністрування може дещо відрізнятися від інших стільникових маршрутизаторів, особливо моделей з одним слотом SIM.

### Налаштування мережі {#network-setup}

Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **INTERNET** -> **Cellular**.

1. Якщо SIM-карту не вставлено, на сторінці з’являється повідомлення «Your SIM card has not been detected».

    ![SIM-карту не виявлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Вставте SIM-карту. Маршрутизатор автоматично розпочне підключення. Після встановлення з’єднання на сторінці відобразяться оператор SIM-карти, рівень сигналу, діапазон, використання даних і додаткові параметри.

    ![Активна SIM-карта](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Якщо SIM-карту не виявлено, вставте її повторно або перезапустіть маршрутизатор і повторіть спробу.

3. Щоб переглянути відомості про мережу, натисніть **Details & Configuration**.

    ![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    У розділі **Network Information** відображаються SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address та IPv4 DNS Server.

    ![Відомості про мережу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Що таке Max Bit Rate (AMBR)?"

        Max Bit Rate (AMBR) — Aggregate Maximum Bit Rate, сукупна максимальна швидкість передавання даних. Вона визначає сумарну верхню межу швидкості для всіх каналів передавання даних без гарантованої бітової швидкості (non-GBR), які надає оператор. Цей параметр задає оператор мобільної мережі.

4. Щоб налаштувати мережу вручну, натисніть **Details & Configuration**.

    ![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    У розділі **Network Settings** можна налаштувати мережеві параметри, зокрема APN.

    ![Налаштування мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: налаштування APN зазвичай отримуються автоматично з SIM-карти. Для деяких SIM-карт потрібна певна APN. Якщо ви не знаєте правильне значення, зверніться до свого оператора.

    - **IP Type**: визначається автоматично. Можна вибрати IPv4, IPv6 або обидва типи. Переконайтеся, що вибраний варіант відповідає типу IP, який підтримує SIM-карта. Якщо SIM-карта не підтримує поточний тип IP або тут вибрано IPv6, а на маршрутизаторі IPv6 вимкнено, можуть виникнути проблеми зі встановленням з’єднання.

    - **International Data Roaming**: увімкнено за замовчуванням для використання даних під час закордонних подорожей. Вимкніть цю функцію, якщо вона не потрібна або щоб уникнути високої плати за роумінг у свого оператора.

    - **TTL**: деякі провайдери визначають, чи використовується SIM-карта в маршрутизаторі, за значенням TTL. Якщо SIM-карта не працює в маршрутизаторі, спробуйте задати TTL, відмінний від 64 і 128, наприклад 65.

    - **HL**: у IPv6 поле HL (Hop Limit) обмежує кількість переходів пакета мережею та відповідає TTL у IPv4.

    - **MTU**: задайте MTU відповідно до сценарію використання. Неправильне значення може призвести до втрати доступу до інтернету. Після зміни MTU перезавантажте пристрій, щоб застосувати параметр.

    - **Authentication**: зазвичай використовується NONE, якщо облікові дані не потрібні. Можна вибрати PAP, CHAP або PAP/CHAP.

### Статистика трафіку {#traffic-statistics}

Щоб переглянути статистику трафіку, натисніть **Data Usage**.

![Статистика трафіку](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Щоб задати ліміт даних Data Cap Amount для SIM-карти або розклад періодичного скидання лічильника її даних, увімкніть **SIM Limit Settings**.

![Увімкнення ліміту SIM-карти](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Задайте Data Cap Amount, Data Reset Period, Start Day і Start Hour, а потім натисніть **Apply**.

![Налаштування ліміту даних SIM-карти](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Примітка**:

1. Якщо Data Used перевищує Data Cap Amount, змініть Data Cap Amount або Data Used. Інакше мережеве з’єднання може відключитися або маршрутизатор може перейти на іншу SIM-карту, якщо увімкнено [SIM Failover](#sim-failover).

2. Якщо для SIM 1 задано Data Cap Amount і увімкнено SIM Auto Switch, після перевищення ліміту даних маршрутизатор автоматично перейде із SIM 1 на SIM 2, а SIM 1 буде вимкнено.

3. Start Day: максимальне значення відповідає фактичній кількості днів у поточному місяці.

### Відомості про стільникове підключення {#cellular-details}

Щоб переглянути відомості про стільникове підключення, натисніть **Details & Configuration**.

![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

У розділі **Cellular Information** відображаються Network Type, TAC, Cell ID, Band і Signal History.

![Відомості про стільникове підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: визначається автоматично. Щоб задати його вручну, відкрийте вкладку **Cellular Settings** і виберіть тип мережі з розкривного списку.

    ![Вибір типу мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Виберіть 5G для більшої швидкості за наявності сигналу 5G або 4G для стабільності.

    Після фіксації базової станції тип мережі буде зафіксовано й змінити його буде неможливо.

- **TAC**: Tracking Area Code — призначений мережею код зони відстеження, який використовується для керування мобільністю у стільниковій мережі. Визначається автоматично за даними базової станції.

- **Cell ID**: унікальний ідентифікатор окремої комірки базової станції. Також визначається автоматично за даними базової станції.

- **Band Information**: натисніть, щоб переглянути додаткові параметри поточного стільникового діапазону.

    ![Відомості про діапазон](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: натисніть, щоб переглянути історію рівня сигналу та оцінити якість стільникового з’єднання.

    ![Історія рівня сигналу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Вибір частотних діапазонів {#band-masking}

Функція Band Masking дозволяє використовувати певні стільникові діапазони для поліпшення сигналу.

Щоб увімкнути Band Masking, натисніть **Details & Configuration**.

![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

У розділі **Cellular Settings** увімкніть **Band Masking**, виберіть потрібні діапазони та натисніть **Apply**.

![Вибір частотних діапазонів](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Фіксація оператора {#lock-operator}

!!! note "Підтримувані моделі"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) підтримує цю функцію у прошивці v4.8 і новіших версіях.

Після фіксації певного мобільного оператора маршрутизатор використовуватиме лише його мережу. Це забезпечує стабільне з’єднання та допомагає уникнути непередбаченої плати за роумінг, особливо у прикордонних районах, де пристрій може підключитися до іноземної мережі.

Щоб зафіксувати оператора, натисніть **Details & Configuration**.

![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

У розділі **Cellular Settings** натисніть **Lock Operator**.

![Фіксація оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Перед пошуком мереж можна вибрати **Lock Mode**.

![Режим фіксації оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: ручна фіксація певного оператора.

- **Manual-Auto**: автоматичний перехід на доступну мережу оператора, якщо ручна фіксація не вдається.

Потім натисніть **Scan Networks**.

![Фіксація оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Зачекайте хвилину, поки з’явиться список доступних операторів. Виберіть оператора та натисніть **Lock**.

![Фіксація оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Після цього стільникове підключення буде зафіксовано на вибраному операторі.

![Фіксація оператора](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Фіксація базової станції {#lock-tower}

!!! note "Підтримувані моделі"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *GL-X2000 (Spitz Plus) підтримує цю функцію у прошивці v4.7 і новіших версіях.

Для поліпшення сигналу та стабільності стільникового з’єднання спробуйте зафіксувати базову станцію. Зафіксована станція повинна відповідати частотним діапазонам, які підтримують оператор і пристрій; інакше з’єднання може не встановитися.

Щоб зафіксувати базову станцію, натисніть **Details & Configuration**.

![Відомості та конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

У розділі **Cellular Settings** натисніть **Lock Tower**.

![Фіксація базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

У спливному вікні натисніть **Scan Networks**.

![Фіксація базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Зачекайте хвилину, поки з’явиться список доступних базових станцій.

![Фіксація базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Виберіть станцію, щоб переглянути відомості про неї, і натисніть **Lock**.

![Фіксація базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Після цього стільникове підключення буде зафіксовано на вибраній базовій станції.

![Фіксація базової станції](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Примітка**:

1. Коли інтерфейс Cellular увімкнено, пристрій може не виявити всі базові станції під час пошуку.

2. Якщо зафіксована базова станція не відповідає вибору діапазонів (якщо Band Masking увімкнено) або параметрам APN у налаштуваннях стільникового підключення, маршрутизатор не зможе підключитися до стільникової мережі.

3. Якщо після фіксації базової станції перенести маршрутизатор в інше місце, після перезавантаження він і далі намагатиметься підключитися до цієї станції. Через це маршрутизатор може не підключитися автоматично до стільникової мережі на новому місці. У такому разі скасуйте поточну фіксацію або вручну зафіксуйте нову базову станцію.

### SMS {#sms}

Див. [SMS](../tutorials/sms.md).

### Пересилання SMS {#sms-forwarding}

Див. [пересилання SMS](../tutorials/sms_forwarding.md).

### Режим польоту {#airplane-mode}

Щоб увімкнути режим польоту, натисніть піктограму шестерні у верхньому правому куті та увімкніть **Airplane Mode**.

![Налаштування стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Відомості про модем {#modem-information}

Щоб переглянути відомості про модем, натисніть піктограму шестерні у верхньому правому куті та виберіть **Modem Information**.

![Налаштування стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![Відомості про модем](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### Аварійне перемикання SIM {#sim-failover}

Ця функція доступна лише на стільникових маршрутизаторах із підтримкою двох SIM-карт.

SIM Failover дозволяє маршрутизатору автоматично перемикатися між SIM 1 і SIM 2. Якщо використання даних пріоритетної SIM-карти перевищує Data Cap Amount або вона не може підключитися до інтернету, маршрутизатор переходить на резервну SIM-карту для підтримання мережевого доступу.

Щоб увімкнути аварійне перемикання SIM, натисніть піктограму шестерні у верхньому правому куті та виберіть **SIM Failover**.

![Налаштування стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

У спливному вікні увімкніть **Auto Switch**. Щоб змінити пріоритет SIM-карт, перетягніть кнопку праворуч.

![Автоматичне перемикання SIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Щоб маршрутизатор повертався до пріоритетної SIM-карти в певний час доби, увімкніть **Scheduled Switch to Preferred SIM**, задайте **Daily Execution Time** та натисніть **Apply**.

![Аварійне перемикання SIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### Команди AT {#at-command}

Команди AT — стандартні інструкції для взаємодії зі стільниковим модемом. Ця функція дає змогу надсилати команди та перевіряти стан модема.

Натисніть піктограму шестерні у верхньому правому куті та виберіть **AT Command**.

![Налаштування стільникового підключення](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![Команди AT](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: якщо вибрано **Manual command**, введіть потрібну команду в поле **AT Command** і натисніть **Send** унизу. Результат з’явиться в полі виведення нижче.

    Також можна натиснути це поле та вибрати **попередньо задану команду** з розкривного списку.

    ![Попередньо задані команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Наприклад, виберіть «Request SIM card status» і слот SIM1, а потім натисніть «Send». Результат матиме вигляд, показаний нижче.

    ![Попередньо задані команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: виберіть SIM1 або SIM2, до якої застосовуватиметься команда. Доступні варіанти залежать від кількості слотів SIM у стільниковому маршрутизаторі.

- **AT Command**: введіть потрібну команду в це поле, якщо для Shortcut вибрано «Manual command».

## Маршрутизатори без вбудованого стільникового модема {#non-cellular-routers}

Якщо маршрутизатор не має вбудованого стільникового модема, підключіть зовнішній USB-модем (не входить до комплекту) до порту USB для доступу до стільникової мережі.

USB-модеми можуть працювати в різних режимах: стандартному режимі USB-модема або Host-less.

- **Стандартний режим USB-модема**: маршрутизатор працює як хост USB, а модем — як підпорядкований пристрій USB. Модем надає інтерфейси команд AT/QMI/MBIM і віртуальний порт USB Ethernet, тому ним можна керувати через вбудований інтерфейс Cellular WAN маршрутизатора. Маршрутизатор зчитує низькорівневі параметри стільникового підключення, зокрема ICCID, рівень сигналу та діапазон, а налаштування SIM задаються безпосередньо у вебінтерфейсі маршрутизатора.

- **Режим Host-less**: модем самостійно встановлює стільникове з’єднання та надає маршрутизатору віртуальний інтерфейс USB Ethernet. Маршрутизатор розпізнає його як WAN через спільний доступ до інтернету через USB, а не як керований модем, тому з’єднання встановлюється через інтерфейс Tethering замість Cellular. Низькорівневі параметри стільникового підключення на маршрутизаторі недоступні. Усі налаштування APN і SIM потрібно виконувати у вбудованому вебінтерфейсі самого модема.

Виберіть відповідний розділ залежно від режиму роботи USB-модема.

### Стандартний USB-модем {#standard-usb-modem}

У цьому розділі налаштування стільникового підключення та пов’язані функції описано на прикладі **Mango 2 (GL-MG1300)** і плати розробки 5G [GL-M2](https://www.gl-inet.com/products/gl-m2){target="_blank"} із модулем 5G NR RM520N-GL.

1. Вставте SIM-карту в плату GL-M2, а потім підключіть GL-M2 до порту USB маршрутизатора.

2. Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **INTERNET** -> **Cellular**.

    Маршрутизатор автоматично спробує підключитися до інтернету. Після встановлення з’єднання на сторінці відобразяться відомості про мережу та зелена крапка, яка означає успішне підключення.

    ![Активне стільникове підключення GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_active.png){class="glboxshadow"}

3. Налаштування SIM-карти.

    Щоб переглянути конфігурацію SIM-карти, натисніть **SIM Card Settings**.

    ![Налаштування SIM-карти GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings1.png){class="glboxshadow"}

    Відобразяться автоматично визначені налаштування SIM-карти, зокрема APN, тип IP і тип мережі. Зміна цих параметрів призведе до повторного встановлення з’єднання.

    ![Налаштування SIM-карти GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_settings2.png){class="glboxshadow"}

4. Відомості про SIM-карту.

    Щоб переглянути відомості про SIM-карту, натисніть **SIM Information**.

    ![Відомості про SIM-карту GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info1.png){class="glboxshadow"}

    Відобразяться відомості про мережу SIM-карти: ICCID, IP-адреса, DNS, стільниковий діапазон, рівень сигналу тощо.

    ![Відомості про SIM-карту GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_sim_info2.png){class="glboxshadow gl-80-desktop"}

5. SMS і пересилання SMS.

    Використання SMS і пересилання SMS описано в розділах [SMS](../tutorials/sms.md) і [пересилання SMS](../tutorials/sms_forwarding.md).

6. Керування профілями стільникового підключення.

    Щоб керувати профілями SIM, натисніть піктограму шестерні у верхньому правому куті та виберіть **Manage Cellular Profiles**.

    ![Налаштування стільникового підключення GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    Відобразиться поточний профіль.

    ![Керування профілями GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_manage_profiles.png){class="glboxshadow"}

    За потреби натисніть **Add a New Profile**, щоб додати інші профілі.

    ![Додавання профілю GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile1.png){class="glboxshadow"}

    Введіть потрібні параметри та натисніть **Apply**.

    ![Додавання профілю GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_add_profile2.png){class="glboxshadow"}

7. Команди AT модема.

    Команди AT — стандартні інструкції для взаємодії зі стільниковим модемом. Ця функція дає змогу надсилати команди та перевіряти стан модема.

    Щоб виконати команду AT, натисніть піктограму шестерні у верхньому правому куті та виберіть **Modem AT Command**.

    ![Налаштування стільникового підключення GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_cellular_settings.png){class="glboxshadow"}

    ![Команди AT модема GL-M2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/m2_atcommand.png){class="glboxshadow"}

    - **Shortcut**: якщо вибрано **Manual command**, введіть потрібну команду в поле **AT Command** і натисніть **Send** унизу. Результат з’явиться в полі виведення нижче.

        Також можна натиснути це поле та вибрати **попередньо задану команду** з розкривного списку.

        ![Попередньо задані команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

        Наприклад, виберіть «Request SIM card status» і слот SIM1, а потім натисніть «Send». Результат матиме вигляд, показаний нижче.

        ![Попередньо задані команди](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

    - **SIM Slot**: виберіть SIM1 або SIM2, до якої застосовуватиметься команда. Доступні варіанти залежать від слотів SIM у зовнішньому USB-модемі, підключеному до маршрутизатора.

    - **AT Command**: введіть потрібну команду в це поле, якщо для Shortcut вибрано «Manual command».

### Модем у режимі Host-less {#hostless-dongle}

У цьому розділі налаштування стільникового підключення описано на прикладі **Flint 3 (GL-BE9300)** і зовнішнього USB-модема [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"}.

1. Підключіть USB-модем до порту USB маршрутизатора.

2. Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте **INTERNET** -> **Tethering** і натисніть **Connect**.

    ![Підключення через Tethering](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Щоб задати додаткові параметри, зокрема TTL, HL і MTU, натисніть **Advanced** і налаштуйте їх перед натисканням **Connect**.

    ![Додаткові параметри Tethering](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Після встановлення з’єднання на сторінці відобразяться відомості про мережу та зелена крапка, яка означає успішне підключення.

    ![З’єднання Tethering встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

4. Налаштування APN і параметрів SIM-карти в SIMPoYo uFi описано в розділі [керування SIMPoYo uFi](../user_guide/simpoyo-4g-ufi/index.md#manage-simpoyo-ufi).

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
