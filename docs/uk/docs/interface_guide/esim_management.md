# Керування eSIM {#esim-management}

**Примітка**:

1. Цей посібник стосується моделей, що підтримують фізичну картку eSIM GL.iNet.

2. GL-E5800 (Mudi 7) має вбудовану eSIM і не підтримує фізичну картку eSIM GL.iNet. На Mudi 7 фізична картка eSIM розпізнаватиметься як звичайна SIM-картка без функцій eSIM.

## Підтримувані моделі {#supported-models}

!!! note "Підтримувані моделі"

    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750V2 (Mudi V2)
    - ※ GL-E750 (Mudi)
    - ※ GL-XE300 (Puli)
    - ※ GL-X750 (Spitz)
    - ※ GL-X300B (Collie)

    **Примітка**:

    1. **Для моделей, позначених ※**, підтримка фізичних карток eSIM залежить від установленого модуля.

        - Якщо використовується модуль **EC25-AF**, **EC25-E** або **EG25-G**, перед використанням фізичної картки eSIM установіть прошивку з підтримкою eSIM. Щоб отримати додаткові інструкції, [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.

        - Якщо використовується модуль **EP06-E**, спочатку оновіть прошивку модуля за інструкціями [за цим посиланням](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, а потім установіть прошивку з підтримкою eSIM.

        - Модуль **EP06-A** не підтримує фізичну картку eSIM, оскільки в програмному забезпеченні Qualcomm немає підтримки потрібних AT-команд.

    2. **GL-E750V2 <u>vSIM</u>** не підтримує фізичну картку eSIM.

    3. **GL-E5800 (Mudi 7)** має вбудовану eSIM. Тому на Mudi 7 фізична картка eSIM розпізнаватиметься як звичайна SIM-картка без функцій eSIM.

## Керування eSIM {#esim-management_1}

У меню ліворуч у вебпанелі адміністрування перейдіть до **APPLICATIONS** -> **eSIM Management**.

На цій сторінці можна перевірити стан фізичної картки eSIM і керувати профілями eSIM. Вона складається з двох розділів: **Current eSIM Status** і **eSIM Profile List**.

![Виявлена картка eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Поточний стан eSIM {#current-esim-status}

У цьому розділі відображаються основні відомості та детальна інформація про поточний активний профіль eSIM.

![Поточний стан eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Глобально унікальний ідентифікатор eUICC (чипа eSIM), що використовується для ідентифікації та керування профілями.
- **ICCID:** Ідентифікатор картки з інтегральною схемою поточного активного профілю eSIM.
- **IMSI:** Міжнародний ідентифікатор мобільного абонента поточного активного профілю eSIM.
- **eSIM OS Version:** Версія операційної системи eUICC, яка визначає сумісність і підтримувані можливості.
- **eSIM Storage (remain/total):** Доступний і загальний обсяг пам’яті eUICC для зберігання профілів eSIM.
- **eSIM Profile Number:** Кількість профілів eSIM, що зберігаються на eUICC. Профілі eSIM різних операторів мають різний розмір, тому кількість профілів, які можна зберегти на eUICC, також відрізняється.

## Список профілів eSIM {#esim-profile-list}

У цьому розділі відображаються відомості про початковий профіль eSIM і звичайні профілі.

![Список профілів eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: Початковий профіль містить 1GB безкоштовного трафіку для США та Європи, а також 100MB глобального трафіку, що діють протягом 1 року з дати активації. Цей трафік дає змогу завантажувати інші профілі в будь-якій країні світу. Також можна відстежувати використання початкового профілю: залишок трафіку, загальний обсяг пакета та дату завершення терміну дії.

- **Normal Profile**: Якщо ви придбаєте профіль eSIM і завантажите його за допомогою QR-коду або коду активації, він відображатиметься тут.

### Поповнення початкового профілю {#top-up-seed-profile}

GL.iNet надає попередньо завантажений початковий профіль зі 100MB глобального трафіку та 1GB трафіку для Європи й США для початкового налаштування та активації профілів eSIM. Цей пакет призначений для завантаження нових профілів eSIM після прибуття до місця, де немає доступу до інтернету.

Якщо попередньо наданий безкоштовний трафік вичерпано або термін його дії минув, а ви хочете продовжувати користуватися послугою, поповніть початковий профіль.

У розділі Seed Profile натисніть кнопку **Top-up** праворуч.

![Поповнення початкового профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

У спливному вікні відскануйте QR-код і дотримуйтеся інструкцій, щоб завершити поповнення.

![Поповнення початкового профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Придбання профілю eSIM {#purchase-esim-profile}

Профілі eSIM можна придбати в рекомендованих або перевірених нами магазинах, а також в інших сторонніх постачальників eSIM.

??? note "Варіант 1: придбання в рекомендованих магазинах"

    Є два рекомендовані магазини: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} та [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    У розділі Normal Profile натисніть **eSIM Profile Recommended Store** праворуч.

    ![Рекомендовані магазини профілів eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Відскануйте QR-код або перейдіть за посиланнями, щоб придбати профілі eSIM.

    ![Рекомендовані магазини профілів eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Примітка**: Усі пакети профілів eSIM, придбані в цих двох магазинах, повністю сумісні з маршрутизаторами GL.iNet. Якщо виникнуть запитання, зверніться до нашої служби підтримки за адресою [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Варіант 2: придбання в перевірених магазинах"

    Перелік магазинів, перевірених GL.iNet, наведено [за цим посиланням](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}.

    **Примітка**: Ми не можемо гарантувати повну сумісність усіх профілів або пакетів із цих магазинів із маршрутизаторами GL.iNet. Оскільки GL.iNet не має партнерських відносин із ними, ми не можемо надавати підтримку після продажу або допомагати з поверненням коштів.

??? note "Варіант 3: придбання в інших сторонніх постачальників eSIM"

    Також можна придбати профілі eSIM в інших сторонніх постачальників на ваш вибір.

    Однак ми не можемо гарантувати повну сумісність профілів eSIM від інших сторонніх постачальників із маршрутизаторами GL.iNet. Рішення про придбання приймайте на власний розсуд. GL.iNet не несе відповідальності за проблеми несумісності.

    Для отримання підтримки після продажу або повернення коштів зверніться до відповідного постачальника eSIM.

### Завантаження профілю eSIM {#upload-esim-profile}

Після придбання профілю eSIM зазвичай надається QR-код або код активації. Збережіть QR-код на своєму пристрої, а потім виконайте наведені нижче дії, щоб завантажити профіль eSIM.

1. У розділі Normal Profile натисніть **Add eSIM Profile** внизу.

    ![Додавання профілю eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Завантажте QR-код eSIM або введіть код активації та натисніть **Install**. Профіль eSIM буде завантажено та встановлено на маршрутизатор.

    ![Додавання профілю eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Примітка:**

    1. Більшість профілів eSIM можна завантажити та встановити лише один раз.

    2. QR-код у правильному форматі містить код активації, який починається з **LPA:**. Проте деякі нестандартні QR-коди можуть містити лише код активації без префікса LPA. У такому разі вручну додайте `LPA:` на початку коду, перш ніж натискати кнопку Install.

        ![Код активації eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Якщо ви ще не придбали профіль eSIM, зробіть це в eSIM Profile Recommended Store. Докладніше дивіться в розділі [Придбання профілю eSIM](#purchase-esim-profile).

3. Увімкніть профіль eSIM.

    Після успішного завантаження новий профіль eSIM з’явиться в списку **Normal Profile**. Натисніть **Enable**, щоб активувати його.

    ![Увімкнення профілю eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Підключіться до інтернету.

    Після ввімкнення профілю eSIM перейдіть до **INTERNET** -> **Cellular**. Натисніть **Connect**, щоб установити з’єднання з інтернетом через цей профіль eSIM.

    ![Підключення до інтернету через eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Примітка**: Для деяких профілів eSIM можуть знадобитися додаткові налаштування, наприклад APN, PIN або TTL. За потреби натисніть **Manual Setup** або **SIM Card Settings**, щоб змінити ці параметри. У деяких випадках для встановлення з’єднання з інтернетом потрібно перезавантажити пристрій.

5. Після успішного підключення маршрутизатора через профіль eSIM сторінка матиме такий вигляд:

    ![Установлене з’єднання через eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Експорт журналу для підтримки {#export-log-for-support}

Натисніть **Export Log for Support**, щоб переглянути всі журнали, пов’язані з eSIM. Якщо виникли проблеми й потрібна технічна підтримка, експортуйте журнали eSIM та надішліть їх нашій службі підтримки електронною поштою на адресу [support@gl-inet.com](mailto:support@gl-inet.com).

![Експорт журналу eSIM](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Пов’язані статті:

- [Як використовувати фізичну картку eSIM з маршрутизаторами GL.iNet?](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Як використовувати фізичну картку eSIM з пристроями Android?](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
