# Посібник користувача Cirrus (GL-AP1300) {#cirrus-gl-ap1300-user-guide}

<span id="hardware-info"></span>

## Огляд пристрою {#product-overview}

Стельова бездротова точка доступу Cirrus (GL-AP1300) — висококласний шлюз для бізнесу з підтримкою Wi-Fi MU-MIMO. Живлення PoE та вбудований сторожовий таймер Watchdog призначені для більшості корпоративних сценаріїв використання. Система керування GoodCloud спрощує керування пристроєм. Ви можете ввімкнути захищений віддалений доступ із будь-якого місця в будь-який час.

![Інтерфейси gl-ap1300](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-ap1300/hardware_info/ap1300_interface.jpg){class="glboxshadow"}

## Технічні характеристики {#specifications}

[Технічні характеристики GL-AP1300](https://www.gl-inet.com/products/gl-ap1300/#specs){target="_blank"}

---

## Початкове налаштування {#first-time-setup}

Усі маршрутизатори GL.iNet мають подібний процес налаштування. [Дізнайтеся, як виконати початкове налаштування](../../faq/first_time_setup.md/).

---

## Інтернет {#internet}

Увійдіть до вебпанелі адміністрування маршрутизатора та виберіть **INTERNET** у меню ліворуч.

На цій сторінці можна вибрати тип інтернет-підключення, наприклад Ethernet, Repeater, Tethering або Cellular, залежно від моделі.

Cirrus (GL-AP1300) підтримує два типи підключення: Ethernet і Repeater.

### Ethernet {#ethernet}

Щоб отримати доступ до інтернету, підключіть маршрутизатор кабелем Ethernet до активного модема або іншого мережевого пристрою. Зазвичай цей спосіб забезпечує найшвидше та найнадійніше інтернет-з’єднання.

[Дізнайтеся, як підключитися до інтернету через кабель Ethernet](../../interface_guide/internet_ethernet.md)

### Ретранслятор {#repeater}

Налаштуйте маршрутизатор як ретранслятор для розширення покриття наявної мережі Wi-Fi. У цьому режимі він приймає та повторно передає бездротові сигнали в межах досяжності, збільшуючи покриття. Цей спосіб корисний, якщо одного маршрутизатора недостатньо для покриття всієї потрібної площі.

[Дізнайтеся, як підключитися до інтернету через наявну мережу Wi-Fi](../../interface_guide/internet_repeater.md)

### Multi-WAN {#multi-wan}

Multi-WAN дає змогу одночасно налаштувати на маршрутизаторі кілька інтернет-підключень (наприклад, Ethernet і Repeater). Якщо підключення з найвищим пріоритетом перестане працювати, маршрутизатор автоматично перемкнеться на інше. Це називається **Failover** — аварійне перемикання, яке забезпечує безперервний доступ до інтернету.

Перейдіть до [Multi-WAN](../../interface_guide/multi-wan.md), щоб установити пріоритет кожного інтернет-підключення.

Також можна змінити режим Multi-WAN із **Failover** на **Load Balance**. Це дає змогу одночасно використовувати кілька мережевих інтерфейсів для збільшення загальної пропускної здатності маршрутизатора.

---

## Бездротова мережа {#wireless}

Налаштування бездротової мережі дають змогу керувати безпекою основної та гостьової мереж Wi-Fi. Щоб відкрити їх, виберіть **WIRELESS** у бічному меню.

[Дізнайтеся більше про налаштування бездротової мережі](../../interface_guide/wireless.md)

---

## Клієнти {#clients}

Клієнти — це пристрої, підключені до маршрутизатора. Ви можете блокувати клієнтів або обмежувати швидкість їхнього з’єднання. Щоб відкрити цей інтерфейс, натисніть **CLIENTS** у бічному меню вебпанелі адміністрування маршрутизатора.

[Дізнайтеся більше про керування клієнтськими пристроями](../../interface_guide/clients.md)

---

## VPN {#vpn}

На маршрутизаторах GL.iNet попередньо встановлено OpenVPN і WireGuard® із підтримкою 30+ служб VPN. Коли VPN увімкнено, трафік підключених пристроїв, зокрема гостьових, шифрується, якщо його спрямовано через VPN-тунель відповідно до налаштованих правил маршрутизації. Наші маршрутизатори також можуть працювати як сервери VPN: трафік клієнтських пристроїв у віддалених місцях спочатку спрямовується через VPN-тунель на сервер VPN, а потім — до публічного інтернету.

### Панель керування VPN {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Покрокові інструкції з налаштування наведено за такими посиланнями:

- [**Налаштування клієнта OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Налаштування сервера OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Покрокові інструкції з налаштування наведено за такими посиланнями:

- [**Налаштування клієнта WireGuard**](../../interface_guide/wireguard_client.md)
- [**Налаштування сервера WireGuard**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## Застосунки {#applications}

Маршрутизатори GL.iNet мають широкий набір додаткових функцій, які спрощують керування пристроєм, покращують роботу з інтернетом, автоматизують оновлення прошивки тощо.

### Плагіни {#plug-ins}

Перегляньте інструкцію [**Plug-ins**](../../interface_guide/plugins.md).

### Динамічний DNS {#dynamic-dns}

Перегляньте інструкцію [**Dynamic DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Перегляньте інструкцію [**GoodCloud**](../../interface_guide/cloud.md).

### AdGuard Home {#adguard-home}

Перегляньте інструкцію [**AdGuard Home**](../../interface_guide/adguardhome.md).

---

## Мережа {#network}

### Міжмережевий екран {#firewall}

Маршрутизатори GL.iNet мають кілька функцій міжмережевого екрана для захищеного з’єднання та контролю з боку користувача. Вони дають змогу налаштовувати правила міжмережевого екрана, зокрема **Port Forwarding**, **Open Ports** і **DMZ**.

[Дізнайтеся більше про міжмережевий екран маршрутизаторів GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Перегляньте інструкцію [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Перегляньте інструкцію [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Перегляньте інструкцію [**DNS**](../../interface_guide/dns.md).

### Режим мережі {#network-mode}

Перегляньте інструкцію [**Network Mode**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Перегляньте інструкцію [**IPv6**](../../interface_guide/ipv6.md).

### MAC-адреса {#mac-address}

Раніше сторінка **Mac Address** називалася **Mac Clone**. Починаючи з v4.2 її назву змінено на **Mac Address**.

Перегляньте інструкцію [**MAC Address**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Перегляньте інструкцію [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Перегляньте інструкцію [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## Система {#system}

### Огляд {#overview}

Перегляньте інструкцію [**System Overview**](../../interface_guide/system_overview.md).

### Оновлення {#upgrade}

GL.iNet регулярно оновлює прошивку маршрутизаторів, щоб покращувати продуктивність, усувати помилки та виправляти вразливості.

Перегляньте інструкцію [**Upgrade**](../../interface_guide/upgrade.md).

### Заплановані завдання {#scheduled-tasks}

Перегляньте інструкцію [**Scheduled Tasks**](../../interface_guide/scheduled_tasks.md).

### Пароль адміністратора {#admin-password}

Починаючи з v4.5 цю функцію перенесено до [**Security**](../../interface_guide/security.md).

Перегляньте інструкцію [**Admin Password**](../../interface_guide/admin_password.md).

### Часовий пояс {#time-zone}

Перегляньте інструкцію [**Time Zone**](../../interface_guide/time_zone.md).

### Журнал {#log}

Перегляньте інструкцію [**Log**](../../interface_guide/log.md).

### Безпека {#security}

Ця функція доступна починаючи з v4.5.

Перегляньте інструкцію [**Security**](../../interface_guide/security.md).

### Скидання налаштувань прошивки {#reset-firmware}

Перегляньте інструкцію [**Reset Firmware**](../../interface_guide/reset_firmware.md).

### Розширені налаштування {#advanced-settings}

Перегляньте інструкцію [**Advanced Settings**](../../interface_guide/advanced_settings.md).

