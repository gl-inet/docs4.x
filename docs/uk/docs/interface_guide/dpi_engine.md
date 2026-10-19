# Рушій DPI {#dpi-engine}

**Примітка**: Ця функція з’явилася у прошивці v4.9.

Деякі моделі, зокрема Mango 2 (GL-MG1300), не підтримують DPI Engine через недостатній обсяг пам’яті, навіть із прошивкою v4.9 або новішою. Докладніше дивіться в розділі [Підтримувані моделі](#supported-models).

---

DPI (Deep Packet Inspection, глибокий аналіз пакетів) — ключова технологія інтелектуального керування мережею. На відміну від традиційних маршрутизаторів, які визначають лише адреси джерела та призначення, DPI детально аналізує вміст пакетів і точно визначає застосунки та вебсайти за допомогою бібліотеки зіставлення ознак, що дає змогу детально класифікувати та контролювати трафік.

Рушій DPI GL.iNet працює локально на маршрутизаторі, забезпечуючи інтелектуальне керування мережею з повним збереженням конфіденційності. Він надає повний доступ до статистики трафіку, фільтрації вмісту та QoS для комплексного контролю трафіку.

Завдяки інтеграції з [Netify](https://www.netify.ai/){target="_blank"} DPI GL.iNet використовує легкий вбудований плагін для ефективного розгортання. База сигнатур Netify, що оновлюється через інтернет, забезпечує надійне керування та робить контроль мережі точнішим і ефективнішим.

**Примітка**:

1. Коли маршрутизатор працює в режимі Drop-in Gateway, функції DPI (зокрема Data Statistics, Content Filter і QoS) та SQM не діють.
2. Коли DPI ввімкнено, Network Acceleration автоматично вимикається для забезпечення стабільної роботи.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Моделі без підтримки"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Швидке налаштування {#quick-setup}

У меню ліворуч у вебпанелі адміністрування перейдіть до **FLOW CONTROL** -> **DPI Engine** і натисніть **Enable DPI Engine**.

![Початкова сторінка рушія DPI](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

У спливному вікні прочитайте та прийміть умови користування й політику конфіденційності, а потім натисніть **Apply**.

![Підтвердження активації DPI](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Зачекайте, поки маршрутизатор виконає системні операції. Він вимкне Network Acceleration та ввімкне Data Statistics і Content Filter.

![Виконання системних операцій](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Після активації натисніть **Done**.

![Успішна активація DPI](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Відкриється **DPI Engine Version Center**, де можна переглянути версії програми DPI та бази даних.

![Версії програми DPI та бази даних](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Примітка**: На цій сторінці відображаються лише основні показники стану системи. Оброблення трафіку почнеться після ввімкнення відповідних функцій.

## Оновлення бази даних {#database-upgrade}

Якщо доступна новіша версія бази даних, натисніть **Upgrade**, щоб оновити її.

![Оновлення бази даних](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
