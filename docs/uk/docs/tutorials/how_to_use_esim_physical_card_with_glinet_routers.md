# Як використовувати фізичну картку eSIM із маршрутизаторами GL.iNet? {#how-to-use-the-esim-physical-card-with-glinet-routers}

У цій інструкції описано, як використовувати фізичну картку eSIM, придбану в інтернет-магазині GL.iNet, із маршрутизаторами GL.iNet.

![Фізична картка eSIM](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Можливості {#features}

Фізичні картки eSIM мають такі переваги:

- Підтримка мереж 4G і 5G для надійного та швидкого з’єднання.
- Керування профілями eSIM: додавання, видалення та ввімкнення.
- Можливість у будь-який час вибрати й придбати потрібні пакети даних у більшості магазинів eSIM у світі.
- Сумісність із профілями більшості світових магазинів eSIM.
- Придбання профілів eSIM онлайн без надання особистої інформації, що зменшує ризик порушення приватності.
- Попередньо встановлений початковий профіль із 1GB безкоштовного трафіку для США та Європи, а також 100MB глобального трафіку. Він дійсний протягом 1 року з дати активації.
- Сумісність із певними пристроями GL.iNet.

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

    **Примітка:**

    1. **Для моделей, позначених ※**, підтримка фізичних карток eSIM залежить від установленого модуля.

        - Якщо використовується модуль **EC25-AF**, **EC25-E** або **EG25-G**, перед використанням фізичної картки eSIM установіть прошивку з підтримкою eSIM. [Зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}, щоб отримати подальші інструкції.

        - Якщо використовується модуль **EP06-E**, спочатку оновіть прошивку модуля за [цією інструкцією](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, а потім установіть прошивку з підтримкою eSIM.

        - Модулі **EP06-A** не підтримують фізичні картки eSIM, оскільки програмне забезпечення Qualcomm не підтримує потрібні AT-команди.

    2. **GL-E750V2 <u>vSIM</u>** не підтримує фізичні картки eSIM.

    3. **GL-E5800 (Mudi 7)** має вбудовану eSIM. Тому фізична картка eSIM на Mudi 7 розпізнаватиметься як звичайна SIM-картка без функцій eSIM.

## Налаштування фізичної картки eSIM {#set-up-esim-physical-card}

Якщо ви використовуєте фізичну картку eSIM уперше, перегляньте це відео або виконайте наведені нижче кроки, щоб налаштувати її на маршрутизаторі GL.iNet.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Крок 1:** Вставте фізичну картку eSIM у маршрутизатор. Детальні вказівки наведено на зображеннях нижче.

![Вставлення картки в E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![Вставлення картки в X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![Вставлення картки в XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Крок 2:** Відкрийте браузер і введіть `192.168.8.1` в адресному рядку, щоб увійти до вебпанелі адміністрування GL.iNet.

![Вхід до вебпанелі адміністрування](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Крок 3:** Підключіть пристрій до інтернету.

Після входу перейдіть до **INTERNET** -> **Cellular**.

Для маршрутизаторів із двома SIM-картками переконайтеся, що слот із фізичною карткою eSIM вибрано як **Active SIM Card**. Якщо ні, натисніть **SIM Card Switch** і виберіть слот, у якому встановлено фізичну картку eSIM.

Потім натисніть **Connect** (або **Auto Setup** у старіших версіях прошивки), щоб підключитися до інтернету через стільникову мережу.

*Ця фізична картка eSIM має початковий профіль із 1GB безкоштовного трафіку для США та Європи, а також 100MB глобального трафіку, дійсний протягом 1 року з дати активації. Цей трафік призначено лише для придбання та завантаження профілів eSIM, а не для звичайного доступу до інтернету.*

![Початкове налаштування підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Після успішного підключення екран матиме такий вигляд.

![Успішне початкове підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Керування профілем eSIM {#manage-your-esim-profile}

**Крок 1:** Переконайтеся, що на пристрої GL.iNet встановлено останню версію прошивки.

Переконайтеся, що **Version** — 4.0 або новіша, а номер **Firmware Type** — 0319 або більший.

![Перевірка версії прошивки](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Якщо прошивка **застаріла**, її можна оновити автоматично онлайн або вручну.

<u>Варіант 1</u>: Оновлення прошивки онлайн

1. Переконайтеся, що пристрій підключено до інтернету.

2. У вебпанелі адміністрування перейдіть до **SYSTEM** -> **Upgrade** -> **Online Upgrade** і натисніть **Install**, щоб автоматично оновити прошивку до останньої версії.

    ![Оновлення прошивки онлайн](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Варіант 2</u>: Оновлення прошивки вручну

1. Завантажте [тут](https://dl.gl-inet.com/){target="_blank"} прошивку з підтримкою eSIM для відповідної моделі.

2. У вебпанелі адміністрування перейдіть до **SYSTEM** -> **Upgrade** -> **Local Upgrade**. Виберіть файл прошивки або перетягніть його у відповідну область, щоб оновити прошивку до останньої версії.

    ![Локальне оновлення прошивки](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Деякі моделі, зокрема Mudi (GL-E750), Puli (GL-XE300) і Spitz (GL-X750), не підтримують eSIM, якщо оснащені модулями Quectel EP06-A. Це пов’язано з відсутністю підтримки певних AT-команд у програмному забезпеченні Qualcomm.

    2. Якщо встановлено модулі EP06-E, скористайтеся [цією інструкцією](https://forum.gl-inet.com/t/48907){target="_blank"}, щоб оновити програмне забезпечення модуля до останньої версії з підтримкою eSIM.

**Крок 2:** Відкрийте **eSIM Management**.

Після оновлення прошивки дочекайтеся перезавантаження пристрою та увійдіть до вебпанелі адміністрування GL.iNet.

Перейдіть до **APPLICATIONS** -> **eSIM Management**. Тут можна переглядати стан eSIM і керувати профілями eSIM.

![Керування eSIM](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Одночасно може бути активним лише один профіль eSIM. Зелена крапка вказує, що вибраний профіль eSIM зараз активний.

---

Пов’язана стаття:

- [Керування eSIM](../interface_guide/esim_management.md){target="_blank"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
