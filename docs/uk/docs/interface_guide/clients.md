# Клієнти {#clients}

У лівому меню вебпанелі адміністрування відкрийте **CLIENTS**.

На сторінці **Clients** відображаються відомості про підключені пристрої: назва пристрою, тип з’єднання, IP-адреса, MAC-адреса, швидкість і трафік. Ці дані розташовано зліва направо.

## Назва пристрою {#device-name}

У першому стовпці відображаються назва та тип пристрою, які залежать від імені хоста пристрою.

![Назва пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Щоб змінити назву та тип пристрою, натисніть значок із трьома крапками у стовпці **Action**, а потім виберіть **Modify** у розкривному меню.

![Зміна параметрів](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![Зміна параметрів клієнтського пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Тип з’єднання {#connection-type}

Синій значок праворуч від назви пристрою позначає тип або спосіб його підключення.

Він показує, як пристрій підключено до мережі: через Wi-Fi чи кабель Ethernet.

![Тип з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP-адреса та MAC-адреса {#ip-and-mac-address}

У другому стовпці наведено IP-адресу та MAC-адресу підключеного пристрою.

![IP-адреса та MAC-адреса](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Багато пристроїв використовують випадкові MAC-адреси. Якщо підключені пристрої використовують такі адреси, з’явиться наведене нижче повідомлення.

![Повідомлення про випадкову MAC-адресу](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Примітка**: Якщо другий символ MAC-адреси — 2, 6, A або E (без урахування регістру), адреса вважається випадковою. Однак деякі пристрої можуть генерувати випадкові MAC-адреси за іншим правилом, тому цей спосіб виявлення може бути неточним.

## Швидкість {#speed}

У третьому стовпці відображається швидкість інтернет-з’єднання підключеного пристрою. Це середня швидкість за останні 3 хвилини.

![Швидкість](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

**Примітка**: Система починає обчислювати середню швидкість після відкриття цієї сторінки. Наприклад, якщо сторінку відкрито протягом 10 секунд, середню швидкість буде обчислено лише за даними цих 10 секунд.

## Трафік {#traffic}

У четвертому стовпці відображається інтернет-трафік підключеного пристрою.

![Трафік](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Зарезервована IP-адреса {#reserved-ip}

У п’ятому стовпці можна одним натисканням зарезервувати IP-адресу для певного підключеного пристрою. Цю функцію додано в прошивці v4.8.

Якщо ви задасте зарезервовану IP-адресу для клієнта в локальній мережі LAN, він отримуватиме ту саму IP-адресу під час кожного звернення до DHCP-сервера маршрутизатора.

Зарезервовані IP-адреси можна призначати комп’ютерам або серверам, які потребують постійних налаштувань IP.

![Зарезервована IP-адреса](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Список блокування {#blocklist}

У шостому стовпці можна одним натисканням заблокувати певний підключений пристрій.

За замовчуванням використовується правило контролю доступу **Blocklist**. За потреби його можна перемкнути на **Allowlist** угорі сторінки.

![Список блокування](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![Контроль доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Пристроям із MAC-адресами зі списку блокування заборонено підключатися до цього маршрутизатора.

- **Allowlist**: Підключатися можуть лише пристрої з визначеними MAC-адресами. Цей варіант підходить для пристроїв IoT і керування корпоративними мережами.

Щоб створити список блокування, імпортуйте список MAC-адрес із файлу в ділянці **(1)** або введіть MAC-адреси вручну в ділянці **(2)**.

![Створення списку блокування](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Спосіб 1. Імпорт клієнтів**

На сторінці **Access Control** натисніть **Import Clients**.

![Імпорт клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Натисніть **Download Import Template**, щоб завантажити файл шаблону з назвою «mac-template.csv».

![Завантаження шаблону](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Відкрийте файл, додайте MAC-адреси та збережіть його.

![Додавання MAC-адрес до файлу](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Виберіть збережений файл або перетягніть його в ділянку завантаження.

![Завантаження файлу](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Після успішного завантаження натисніть **Import**, щоб завершити пакетний імпорт MAC-адрес.

![Файл успішно завантажено](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Спосіб 2. Введення вручну**

На сторінці **Access Control** вручну введіть MAC-адреси пристроїв, які потрібно заблокувати, і натисніть **Apply**.

![Введення MAC-адреси вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Примітка**: Блокування клієнта виконується за MAC-адресою пристрою. Якщо наступного разу заблокований пристрій використовуватиме іншу MAC-адресу, він усе одно зможе підключитися до маршрутизатора.

## Дії {#action}

### Перегляд відомостей {#view-details}

Щоб переглянути відомості про клієнтський пристрій, натисніть значок із трьома крапками у крайньому правому стовпці **Action**, а потім виберіть **View Details** у розкривному меню.

![Перегляд відомостей](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

На сторінці, що відкриється, відображаються всі відомості про клієнтський пристрій, зокрема всі його IPv6-адреси, якщо вони є.

![Відомості про клієнта](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Зміна параметрів {#modify}

Натисніть значок із трьома крапками у стовпці **Action**, а потім виберіть **Modify** у розкривному меню.

![Зміна параметрів](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![Зміна параметрів клієнтського пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Обмеження швидкості {#limit-speed}

Натисніть значок із трьома крапками у стовпці **Action**, а потім виберіть **Limit Speed** у розкривному меню.

![Обмеження швидкості](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed1.png){class="glboxshadow"}

![Налаштування обмеження швидкості](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Якщо для клієнта встановлено обмеження швидкості, стрілки швидкості завантаження та передавання стануть жовтими.

![Швидкість обмежено](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed2.png){class="glboxshadow"}

Щоб вимкнути обмеження швидкості, натисніть значок із трьома крапками у стовпці **Action**.

### Використання тунелю VPN {#use-vpn-tunnel}

**Примітка**: Цей параметр доступний із прошивки v4.8 і з’являється в меню **Action**, лише якщо налаштовано політику на основі MAC-адрес.

Додайте клієнта до списку тунелю VPN із політикою на основі MAC-адрес. Для докладного налаштування тунелів відкрийте **VPN Dashboard**.

![Використання тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Сортування {#sort}

Поточне правило сортування відображається у правому верхньому куті. Його можна змінити.

![Сортування](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.jpg){class="glboxshadow"}

За замовчуванням використовується такий порядок сортування:

- Пристрій, з якого ви відкрили панель адміністрування, завжди відображається першим.
- У розділі **Online Clients** пристрої, які підключилися раніше, відображаються вище.
- У розділі **Offline Clients** пристрої, які від’єдналися раніше, відображаються вище.

## Налаштування {#settings}

Натисніть кнопку **Settings** у правому верхньому куті, щоб виконати додаткові операції.

![Налаштування](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/settings.png){class="glboxshadow"}

- **Clear Traffic Statistics**: Очистьте статистику трафіку всіх підключених клієнтів одним натисканням. Після застосування значення у стовпці статистики трафіку буде скинуто до нуля, і збір статистики почнеться знову.

    ![Статистику трафіку очищено](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic_cleared.png){class="glboxshadow"}

- **Toggle Rate Unit**: Перемкніть одиниці вимірювання у стовпці швидкості між **KB/s** і **Kbps**.

- **Auto Remove Offline Clients**: Цю функцію додано в прошивці v4.9. Після її ввімкнення всі від’єднані клієнти буде негайно видалено, і вони не відображатимуться в розділі **Offline Clients**.

    ![Автоматичне видалення від’єднаних клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/auto_removal.png){class="glboxshadow"}

## Видалення клієнтів {#remove-clients}

У розділі від’єднаних клієнтів натисніть **Delete All** у правому верхньому куті, щоб видалити всіх від’єднаних клієнтів.

Щоб видалити певного клієнта, натисніть значок із трьома крапками у стовпці **Action**, а потім виберіть **Remove Client** у розкривному меню.

![Видалення від’єднаних клієнтів](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
