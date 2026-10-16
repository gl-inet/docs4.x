# Фільтрація вмісту {#content-filter}

**Примітка**: цю функцію додано у прошивці v4.9.

Деякі моделі, зокрема Mango 2 (GL-MG1300), не підтримують фільтрацію вмісту через недостатній обсяг пам’яті, навіть із прошивкою v4.9 або новішою. Докладніше див. [підтримувані моделі](#supported-models).

---

Фільтрація вмісту — це інтелектуальна функція безпеки в інтернеті на основі класифікації DPI. Вона автоматично блокує шкідливі та небезпечні вебсайти для захисту мережі, а також підтримує власні правила для блокування певних застосунків, доменів або IP-адрес.

**Примітка**:

1. Фільтрація вмісту не діє, коли маршрутизатор працює в режимі Drop-in Gateway.
2. Фільтрація вмісту несумісна з прискоренням мережі. Увімкнення фільтрації вмісту автоматично вимикає прискорення мережі для забезпечення стабільної роботи.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint2)
    - GL-MT3000 (Beryl AX)

??? "Непідтримувані моделі"
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

У лівому меню вебпанелі адміністрування відкрийте **FLOW CONTROL** -> **Content Filter**.

Увімкніть перемикач у верхньому правому куті, налаштуйте вміст для блокування (наприклад, застосунки, домени або IP-адреси) та натисніть **Apply**.

![Фільтрація вмісту](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Ця сторінка складається з двох частин:

- **Blocked Apps List**: цей розділ містить три попередньо вибрані категорії: Gambling, Adult і Malware. Після увімкнення блокуються всі вебсайти, сервіси та застосунки, пов’язані з цими трьома категоріями.

    За потреби натисніть **Edit App**, щоб додати інші категорії (наприклад, Game, Social Media).

    ![Редагування списку застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    У спливному вікні виберіть категорії для блокування. Три категорії за замовчуванням порожні; усі інші категорії містять списки застосунків.

    ![Вибір категорій застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Натисніть будь-яку категорію, щоб переглянути й вибрати застосунки для блокування, або натисніть **Select All** у верхньому правому куті, щоб заблокувати всі застосунки цієї категорії одночасно. Потім натисніть **Confirm**.

    ![Вибір застосунків для блокування](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    Вибрані застосунки з’являться у списку Blocked App List.

    ![Список заблокованих застосунків](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: у цьому розділі можна вручну ввести певні домени (наприклад, google.com), діапазони CIDR (наприклад, 192.168.8.0/24) або IP-адреси (наприклад, 192.168.10.10), щоб заблокувати доступ до них. Список підтримує до 10000 записів.

    Введіть домени або IP-адреси для блокування та натисніть **Apply**.

    ![Список заблокованих доменів та IP-адрес](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Перевірка фільтрації вмісту {#content-filter-test}

У цьому прикладі вибрано категорію **Game**, яка містить Nintendo.

![Вибір Nintendo для перевірки фільтрації](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

На ноутбуці, підключеному до маршрутизатора, сайт `nintendo.com` більше не відкривається, хоча до увімкнення фільтрації вмісту він був доступний.

![Блокування доступу до Nintendo](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

У вебпанелі адміністрування маршрутизатора можна переглянути кількість заблокованих запитів доступу.

![Кількість заблокованих запитів](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
