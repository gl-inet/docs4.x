# QoS (якість обслуговування) {#qos-quality-of-service}

**Примітка**: Ця функція з’явилася у прошивці v4.9.

Деякі моделі, зокрема Mango 2 (GL-MG1300), не підтримують QoS через недостатній обсяг пам’яті, навіть із прошивкою v4.9 або новішою. Докладніше дивіться в розділі [Підтримувані моделі](#supported-models).

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **FLOW CONTROL** -> **QoS**.

QoS (Quality of Service, якість обслуговування) оптимізує розподіл пропускної здатності, надаючи пріоритет важливим завданням (наприклад, відеодзвінкам або іграм) під час перевантаження мережі. Це зменшує затримку та підвищує загальну продуктивність мережі.

**Примітка**:

1. Ця функція впливає лише на трафік, який проходить через маршрутизатор, коли він працює як шлюз, зокрема на трафік локальних клієнтів і клієнтів VPN. Вона не застосовується до вхідного трафіку, коли маршрутизатор працює як сервер VPN.
2. QoS не діє, коли маршрутизатор працює в режимі Drop-in Gateway.
3. QoS і SQM не можна ввімкнути одночасно.
4. QoS не працює разом із Network Acceleration. Увімкнення QoS автоматично вимикає Network Acceleration для забезпечення стабільної роботи.

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

## Для прошивки v4.11 та новіших версій {#for-firmware-v411-and-above}

Увімкніть QoS за допомогою перемикача та виконайте наведені нижче кроки налаштування.

![QoS у прошивці v4.11](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/QoS.png){class="glboxshadow" width=600}

1. **WAN Bandwidth**

    Уведіть швидкості передавання та завантаження WAN вручну (діапазон введення: 1 - 10000) або натисніть **Run Speedtest**, щоб виміряти їх і автоматично заповнити поля. Для перевірки швидкості потрібне активне з’єднання з інтернетом.

    ![Пропускна здатність WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/wan_bandwidth.png){class="glboxshadow" width=600}

    **Примітка**: Значення в полях введення задаються в **Mbps** (мегабітах за секунду). Еквівалент у **MB/s** (мегабайтах за секунду) відображається для довідки.

2. **Scheduling Policy**

    Можна вибрати один режим політики. Розширені правила мають пріоритет над основною політикою для трафіку, який їм відповідає.

    - **Device Priority**

        У цьому режимі вибрані локальні клієнти отримують вищий мережевий пріоритет, коли з’єднання WAN перевантажене. Натисніть **Add Device** і виберіть пристрої, які отримуватимуть пріоритет у розподілі пропускної здатності за високого навантаження на WAN.

        ![Пріоритет пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/device_priority.png){class="glboxshadow" width=600}

        Пристрої можна шукати за назвою клієнта, MAC-адресою або IP-адресою. Виберіть потрібні пристрої та натисніть **Apply**.

        ![Вибір пристроїв](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/select_devices.png){class="glboxshadow" width=500}

    - **Application Priority**

        У цьому режимі можна задати пріоритети різним застосункам. Маршрутизатор розподілятиме пропускну здатність відповідно до них.

        ![Пріоритет застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/application_priority.png){class="glboxshadow" width=600}

        Щоб налаштувати власні пріоритети застосунків, виберіть **Customize** і натисніть **Pre-Set up**.

        ![Вибір власних пріоритетів застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority_1.png){class="glboxshadow" width=600}

        У спливному вікні для всіх категорій за замовчуванням установлено Medium Priority.

        ![Категорії із середнім пріоритетом](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

        Перетягніть категорії, щоб змінити їхній пріоритет за потреби, та натисніть **Confirm**.

        ![Зміна пріоритетів категорій](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow" width=600}

    - **Advanced QoS**

        У цьому режимі можна створити розширені правила QoS для трафіку з високим пріоритетом. Натисніть **Add Rule**, щоб визначити правила за протоколом, портом та IP-адресою джерела.

        ![Розширені правила QoS](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos.png){class="glboxshadow" width=600}

        Задайте Name, Protocol, Source Address і Destination Port, а потім натисніть **Apply**.

        ![Налаштування розширеного правила QoS](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/advanced_qos_rule.png){class="glboxshadow" width=500}

## Для прошивок від v4.9 до v4.10 {#for-firmware-v49-to-v410}

Увімкніть QoS за допомогою перемикача. Сторінка матиме такий вигляд:

![Налаштування QoS](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/qos.png){class="glboxshadow" width=600}

Для керування трафіком задайте максимальні швидкості передавання та завантаження (діапазон введення: 1 - 10000). Для найкращих результатів вони мають відповідати фактичній пропускній здатності з’єднання з інтернетом.

![Швидкості передавання та завантаження](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/up_down_speed.png){class="glboxshadow" width=600}

**Примітка**: Значення в полях введення задаються в **Mbps** (мегабітах за секунду). Еквівалент у **MB/s** (мегабайтах за секунду) відображається для довідки.

Потім задайте пріоритети різним застосункам. Маршрутизатор розподілятиме пропускну здатність відповідно до них.

![Пріоритети застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/app_priority.png){class="glboxshadow" width=600}

Щоб налаштувати власні пріоритети застосунків, виберіть **Customize** і натисніть **Pre-Set up**.

![Вибір власних пріоритетів застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority1.png){class="glboxshadow" width=600}

У спливному вікні для всіх категорій за замовчуванням установлено Medium Priority.

![Категорії із середнім пріоритетом](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority2.png){class="glboxshadow" width=600}

Перетягніть категорії, щоб змінити їхній пріоритет за потреби, та натисніть **Confirm**.

![Зміна пріоритетів категорій](https://static.gl-inet.com/docs/router/en/4/interface_guide/qos/customize_priority3.png){class="glboxshadow"  width=600}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
