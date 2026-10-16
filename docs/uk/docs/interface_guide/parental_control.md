# Батьківський контроль {#parental-control}

**Примітка**: Цей посібник стосується прошивки v4.8 та раніших версій. Для новіших версій перейдіть [сюди](parental_control_v4.9.md).

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **APPLICATIONS** -> **Parental Control**.

Батьківський контроль допомагає захищати дітей в інтернеті, блокуючи неприйнятні вебсайти та обмежуючи час користування пристроями. Він запобігає доступу до шкідливого вмісту, дає змогу керувати часом перед екраном і сприяє відповідальному користуванню інтернетом.

**Примітка**: Деякі моделі не підтримують Parental Control через недостатній обсяг пам’яті, зокрема Mango (GL-MT300N-V2) і Shadow (GL-AR300M series).

Перегляньте це відео або виконайте наведені нижче дії, щоб налаштувати батьківський контроль на маршрутизаторі GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Локальна версія {#local-version}

Локальну версію надає GL.iNet. Наразі вона перебуває в бета-тестуванні та не потребує додаткової оплати. Щоб фільтрувати запити застосунків у цій версії, потрібно вручну ввести домен.

### Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"

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
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
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
    - GL-X300B (Collie)

### Кроки налаштування {#setup-steps}

Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **Parental Control**.

Переконайтеся, що час маршрутизатора правильний. Інакше спочатку перейдіть до **SYSTEM** -> **Time Zone** і синхронізуйте його.

![Перевірка часу маршрутизатора](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Увімкніть Parental Control і натисніть **Apply**.

![Увімкнення батьківського контролю](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Блокує доступ до інтернету для всіх пристроїв, яких немає у списку Parental Control.

Далі дотримуйтеся інструкцій майстра, щоб налаштувати батьківський контроль.

---

Нижче наведено приклад використання. Змініть налаштування відповідно до ваших потреб.


**Сценарій**: Пристроям у профілі дозволено доступ до інтернету лише для навчання з 08:00 до 11:00 у будні та для ігор з 18:00 до 20:00 у вихідні. У решту часу доступ до інтернету за замовчуванням заблоковано.

Виконайте наведені нижче дії, щоб налаштувати батьківський контроль.

1. Створіть профіль і задайте йому назву.

    ![Створення профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Виберіть пристрої, якими потрібно керувати. Спочатку підключіть їх до маршрутизатора. Якщо вони ще не підключалися, додайте їх вручну, ввівши MAC-адреси.

    ![Вибір пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Налаштуйте обмеження доступу.

    За замовчуванням є два набори правил: **Block Internet Access** і **No Limit**.

    ![Набори правил за замовчуванням](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Натисніть **Add a New Ruleset**, щоб створити ще два набори правил для подальшого використання: **Learning** і **Play**.

    ![Додавання набору правил](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Задайте назву набору правил (наприклад, Learning) і колір, уведіть вебсайти для блокування та натисніть **Apply**.

    ![Створення набору правил Learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Примітка**: Доменні імена у списку блокування також охоплюють їхні піддомени. Наприклад, запис "example.com" охоплює всі піддомени, зокрема "subdomain.example.com".

    Аналогічно створіть інший набір правил. Задайте його назву (наприклад, Play) і колір, уведіть вебсайти для блокування та натисніть **Apply**.

    ![Створення набору правил Play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    Після застосування буде чотири набори правил. Виберіть **Block Internet Access** як **Default Ruleset** і натисніть **Finish**.

    ![Чотири набори правил](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Налаштуйте розклад для профілю. Натисніть **Go to Set**.

    ![Налаштування розкладу](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    Додайте набір правил **Learning** до розкладу. Установіть **Execution Time** з 08:00 до 11:00 у будні та натисніть **Apply**.

    ![Розклад для навчання](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. Відкриється сторінка редагування щойно створеного профілю.

    ![Створений профіль](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Прокрутіть униз, щоб побачити створений розклад. Натисніть значок шестірні вгорі праворуч і виберіть **Add Schedule**.

    ![Додавання розкладу до профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Додайте інший набір правил **Play** до розкладу. Установіть **Execution Time** з 18:00 до 20:00 у вихідні та натисніть **Apply**.

    ![Розклад для ігор](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    Набір правил Play буде додано до розкладу.

    ![Налаштовані розклади](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Примітка**: Червона пунктирна лінія позначає поточний час.

    Щоб змінити час виконання, натисніть відповідний набір правил у розкладі.

    ![Редагування розкладу](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Натисніть **Parental Control** угорі, щоб повернутися на сторінку батьківського контролю.

    ![Сторінка батьківського контролю](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    Відобразиться кінцева конфігурація. Батьківський контроль діє відповідно до розкладу. За потреби змініть наявні профілі та набори правил або додайте нові.

    ![Кінцева конфігурація](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Усунення несправностей {#troubleshooting}

Якщо задані налаштування не діють, перевірте можливі причини нижче.

1. Проблема з кешем DNS.

    Браузери й операційні системи зберігають кеш DNS, що може затримувати застосування змін конфігурації. Очистьте кеш DNS, щоб зміни набули чинності одразу.

      * [Очищення кешу DNS у Chrome на комп’ютері](https://support.google.com/accounts/answer/32050){target="_blank"}

      * [Очищення кешу DNS в Edge на комп’ютері](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. Час дії розкладу профілю ще не настав.

3. Уведено неправильне доменне ім’я.

    Публічний домен вебсайту легко знайти, але домени API, які використовують застосунки, часто не оприлюднені. Щоб визначити правильний домен, скористайтеся засобом захоплення пакетів, наприклад Wireshark, або знайдіть відповідні відомості про домени.

    Наприклад, для блокування `www.google.com` запис `google.com` дає кращі результати, ніж `www.google.com`.

4. Цільовий пристрій використовує випадкову MAC-адресу для кожного мережевого з’єднання, через що правила доступу не діють. Вимкніть випадкову MAC-адресу на цьому пристрої та знову додайте його до профілю.

## Версія Bark {#bark-version}

Цей посібник стосується прошивки v4.8 та раніших версій. Для новіших версій перейдіть [сюди](bark.md).

Служба [Bark](https://www.bark.us/){target="_blank"} допомагає захистити дитину в цифровому середовищі та забезпечує комплексний захист в інтернеті. Зазвичай для неї потрібна платна підписка. Однак у межах партнерства з Bark компанія GL.iNet безкоштовно надає план Bark Home **на окремих моделях маршрутизаторів**, забезпечуючи розширені можливості моніторингу та сповіщень без додаткової оплати.

**Примітка**:

1. Служба Bark доступна **лише у Сполучених Штатах, Австралії та Південній Африці**. Докладніше див. [тут](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"}.

2. Дві версії батьківського контролю не можна ввімкнути одночасно. Увімкнення однієї автоматично вимикає іншу.

### Підтримувані моделі {#supported-models_1}

??? "Підтримувані моделі"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Моделі без підтримки"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
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
    - GL-X300B (Collie)

### Кроки налаштування {#setup-steps_1}

Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **APPLICATIONS** -> **Parental Control**. Виберіть версію Bark.

![Вибір версії Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

Увімкніть Bark за допомогою перемикача та натисніть **Apply**.

![Увімкнення Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

Прив’яжіть пристрій до облікового запису Bark. Натисніть **Device Pairing Link** або перейдіть [сюди](https://www.bark.us/app/signup/?ref=glinet&home=glinet), щоб прив’язати маршрутизатор до облікового запису Bark.

![Посилання для прив’язування пристрою Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Вас буде перенаправлено на сайт Bark. Дотримуйтеся вказівок на екрані, щоб увійти, прив’язати пристрій, створити профіль і завершити початкове налаштування.

![Початкова сторінка Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_welcome.png){class="glboxshadow"}
<small>(Вхід у Bark)</small>

![Налаштування Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow"}
<small>(Пристрій прив’язано)</small>

![Налаштування Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_create_profile.png){class="glboxshadow"}
<small>(Створення профілю)</small>

![Налаштування Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_get_started.png){class="glboxshadow"}
<small>(Початкове налаштування)</small>

Після підключення пристрою до хмарних служб Bark і прив’язування до облікового запису вебпанель адміністрування маршрутизатора виглядатиме так:

![Пристрій прив’язано до Bark](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Натисніть **Go to Bark** або перейдіть за [цим посиланням](https://www.bark.us/app/children/?ref=glinet&home=glinet){target="_blank"}, щоб увійти в панель керування Bark і налаштувати правила батьківського контролю.

GL.iNet не є постачальником цієї служби. Якщо під час використання Bark виникли проблеми, зверніться безпосередньо до [технічної підтримки Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet){target="_blank"}.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
