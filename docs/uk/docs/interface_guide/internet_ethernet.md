# Підключення до інтернету кабелем Ethernet {#connect-to-the-internet-via-an-ethernet-cable}

Підключіть маршрутизатор до широкосмугової мережі кабелем Ethernet через порт WAN. Зазвичай він автоматично отримує IP-адресу за допомогою DHCP. Також можна вручну налаштувати статичну IP-адресу або PPPoE. Цей спосіб забезпечує високу стабільність і швидкість та підходить для домашніх і офісних мереж зі стаціонарним широкосмуговим доступом.

Виконайте наведені нижче дії, щоб підключити маршрутизатор до інтернету кабелем Ethernet.

1. З’єднайте порт WAN маршрутизатора з пристроєм вищого рівня (наприклад, модемом провайдера, маршрутизатором, мережевим комутатором або розеткою Ethernet) кабелем Ethernet.

2. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до розділу **INTERNET** -> **Ethernet**.

    Після успішного підключення в розділі Ethernet відображатимуться відомості про мережу, зокрема Protocol, IP Address, Gateway і DNS Server.

    ![З’єднання Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_1.png){class="glboxshadow"}

**Порада**: За потреби можна змінити роль порту WAN на LAN. Це корисно, коли маршрутизатор використовується як [ретранслятор](internet_repeater.md), оскільки фізичний порт WAN не задіяний. Після перемикання WAN на LAN ви отримаєте додатковий порт LAN.

## Протокол {#protocol}

Доступні три протоколи: DHCP, Static і PPPoE. Натисніть **Modify**, щоб змінити протокол.

![Зміна протоколу Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_2.png){class="glboxshadow"}

* DHCP

    DHCP — протокол за замовчуванням і найпоширеніший варіант. Він автоматично призначає IP-адреси та інші параметри зв’язку мережевим пристроям за допомогою клієнт-серверної архітектури в IP-мережах.

    ![Налаштування DHCP для Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_3.png){class="glboxshadow"}

* Static

    Static потрібен, якщо інтернет-провайдер (ISP) надає фіксовану IP-адресу або ви хочете вручну налаштувати мережеві параметри, наприклад IP-адресу, шлюз і маску підмережі.

    ![Статична IP-адреса для Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_4.png){class="glboxshadow"}

* PPPoE

    PPPoE — протокол, який використовує більшість інтернет-провайдерів. Зазвичай вони надають модем, ім’я користувача та пароль, потрібні для налаштування інтернету.

    ![Налаштування PPPoE для Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_5.png){class="glboxshadow"}

## Додаткові налаштування {#advanced}

Окрім основних параметрів, для всіх трьох протоколів доступні необов’язкові додаткові налаштування.

* **VLAN ID**: Цей параметр потрібен лише тоді, коли сервер провайдера вимагає використання певного тегованого VLAN ID на інтерфейсі.

* **TTL**: TTL (Time To Live, час життя) визначає максимальний час перебування пакетів у мережі. За замовчуванням перед пересиланням маршрутизатор зменшує TTL вхідних пакетів від клієнтських пристроїв на 1. Налаштування TTL діє лише для IPv4.

    **Примітка**: Щоб перевизначити або підмінити TTL, задайте тут фіксоване значення. Для більшості моделей уведіть бажаний кінцевий TTL плюс 1, щоб компенсувати автоматичне зменшення. Mudi 7 (GL‑E5800) застосовує введене значення без змін.

* **HL**: У IPv6 поле HL (Hop Limit, межа переходів) обмежує кількість мережевих переходів для пакетів даних і є аналогом TTL у IPv4.

* **MTU**: Значення MTU за замовчуванням — 1500 байтів.

## Порти Ethernet {#ethernet-port}

Натисніть значок шестірні у верхньому правому куті, щоб відкрити сторінку [Порти Ethernet](ethernet_port.md) та керувати портами Ethernet маршрутизатора.

![Відкриття налаштувань портів Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_6.png){class="glboxshadow"}

На сторінці **WAN** відображаються роль порту (WAN або LAN), режим MAC, MAC-адреса та узгоджена швидкість мережевого порту.

![Параметри порту WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/wan.png){class="glboxshadow"}

На сторінці **LAN** відображаються роль порту та узгоджена швидкість мережевого порту.

![Параметри порту LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/lan.png){class="glboxshadow"}

Докладніше дивіться [Порти Ethernet](ethernet_port.md).

## Усунення несправностей {#troubleshooting}

Якщо кабель Ethernet підключено до порту WAN, але інтернет недоступний, з’явиться жовте повідомлення, як показано нижче.

**"The interface is connected, but the Internet can't be accessed."**

![Попередження про відсутність доступу до інтернету](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_ethernet/ethernet_9.jpg){class="glboxshadow gl-90-desktop"}

Щоб усунути проблему:

1. Перевірте, чи має пристрій вищого рівня доступ до інтернету.

2. Відкрийте сторінку [Multi-WAN](multi-wan.md) і перевірте стан інтерфейсу Ethernet.

---

Пов’язані статті

- [Сторінка інтернету](internet.md)
- [Як установити пріоритет кожного способу доступу до інтернету?](multi-wan.md)
- [Як налаштувати балансування навантаження за одночасного використання кількох способів доступу до інтернету?](multi-wan.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
