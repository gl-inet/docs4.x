# Посібник користувача Brume (GL-MV1000) {#brume-gl-mv1000-user-guide}

<span id="hardware-info"></span>

## Огляд пристрою {#product-overview}

Brume (GL-MV1000) і Brume-W (GL-MV1000W) — це потужні та стабільні мережеві пристрої для сучасних обчислювальних завдань. Високопродуктивний чипсет Marvell дає змогу Brume і Brume-W* виконувати сучасні криптографічні операції з високою швидкістю для ефективної VPN-маршрутизації. Попередньо встановлений OpenWrt і підтримка Ubuntu забезпечують можливості поглибленої розробки для комерційних проєктів IoT на Brume і Brume-W*.

<span id="wireless"></span>

Brume-W (GL-MV1000W) — це спеціальна версія Brume (GL-MV1000) із вбудованим модулем Wi-Fi, який забезпечує швидкість до 300Mbps у діапазоні 2.4GHz.

## Технічні характеристики {#specifications}

[Технічні характеристики GL-MV1000](https://www.gl-inet.com/products/gl-mv1000/#specs){target="_blank"}

---

## Перше налаштування {#first-time-setup}

Процедура налаштування всіх маршрутизаторів GL.iNet подібна. Див. [посібник із першого налаштування](../../faq/first_time_setup.md).

---

## Інтернет {#internet}

Увійдіть до вебпанелі адміністрування маршрутизатора та виберіть **INTERNET** у меню ліворуч.

На цій сторінці можна вибрати тип інтернет-з’єднання, наприклад Ethernet, Repeater, Tethering або Cellular, залежно від моделі.

Brume (GL-MV1000) підтримує три типи з’єднання: Ethernet, Tethering і Cellular.

### Ethernet {#ethernet}

Підключіть маршрутизатор до працюючого модема або мережевого пристрою за допомогою кабелю Ethernet для доступу до інтернету. Цей спосіб зазвичай забезпечує найшвидше та найнадійніше інтернет-з’єднання.

[Підключення до інтернету через кабель Ethernet](../../interface_guide/internet_ethernet.md)

![З’єднання Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_ethernet.png){class="glboxshadow"}

### Tethering {#tethering}

Підключіть USB-порт маршрутизатора кабелем USB до смартфона з активним мобільним інтернетом. Завдяки цьому кілька пристроїв, підключених до маршрутизатора, зможуть користуватися мобільним інтернетом смартфона.

[Підключення до інтернету через USB-модем смартфона](../../interface_guide/internet_tethering.md)

![З’єднання Tethering](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_tethering.png){class="glboxshadow"}

### Cellular {#cellular}
 
Підключіть маршрутизатор до інтернету, вставивши стільниковий USB-модем у його USB-порт. Цей спосіб дає змогу надати доступ до інтернету через USB-модем усім підключеним пристроям.

[Підключення до інтернету через USB-модем](../../interface_guide/internet_cellular.md)

![Стільникове з’єднання](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-mv1000/internet/mv1000_cellular.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN — це мережева функція, яка дає змогу одночасно налаштувати кілька інтернет-з’єднань, наприклад Ethernet і Repeater. Якщо з’єднання з найвищим пріоритетом перестане працювати, маршрутизатор автоматично перемкнеться на інше. Це також називається аварійним перемиканням (Failover) і забезпечує безперервний доступ до інтернету.

Перейдіть до [Multi-WAN](../../interface_guide/multi-wan.md), щоб установити пріоритет кожного інтернет-з’єднання.

Також можна змінити режим Multi-WAN із Failover на Load Balance. У цьому режимі кілька мережевих інтерфейсів використовуються одночасно для збільшення сумарної пропускної здатності маршрутизатора.

---

## Клієнти {#clients}

Клієнти — це пристрої, підключені до маршрутизатора. Їх можна блокувати або обмежувати швидкість їхнього з’єднання. Щоб відкрити цей розділ, натисніть **CLIENTS** у бічному меню вебпанелі адміністрування маршрутизатора.

[Докладніше про керування клієнтськими пристроями](../../interface_guide/clients.md)

---

## VPN {#vpn}

На маршрутизаторах GL.iNet попередньо встановлено OpenVPN і WireGuard® із підтримкою 30+ VPN-сервісів. Під час використання VPN трафік підключеної мережі обробляється відповідно до налаштованої політики маршрутизації, а трафік, спрямований через VPN, шифрується. Це також стосується трафіку гостьових пристроїв і клієнтів, які не можуть самостійно виконувати VPN-шифрування. Маршрутизатори також можуть працювати як VPN-сервери: трафік клієнтських пристроїв у віддалених місцях спрямовується через VPN-тунель до VPN-сервера, перш ніж виходити до загальнодоступного інтернету.

### VPN Dashboard {#vpn-dashboard}

- [**VPN Dashboard**](../../interface_guide/vpn_dashboard_v4.7.md)

### OpenVPN {#openvpn}

Покрокові інструкції з налаштування див. за такими посиланнями:

- [**Налаштування клієнта OpenVPN**](../../interface_guide/openvpn_client.md)
- [**Налаштування сервера OpenVPN**](../../interface_guide/openvpn_server.md)

### WireGuard {#wireguard}

Покрокові інструкції з налаштування див. за такими посиланнями:

- [**Налаштування клієнта WireGuard**](../../interface_guide/wireguard_client.md)
- [**Налаштування сервера WireGuard**](../../interface_guide/wireguard_server.md)

### Tor {#tor}

- [**Tor**](../../interface_guide/tor.md)

---

## Застосунки {#applications}

Маршрутизатори GL.iNet мають різноманітні додаткові функції, які спрощують керування пристроєм, поліпшують роботу в інтернеті, автоматизують оновлення прошивки тощо.

### Плагіни {#plug-ins}

Докладні інструкції див. у посібнику [**Плагіни**](../../interface_guide/plugins.md).

### Динамічний DNS {#dynamic-dns}

Докладні інструкції див. у посібнику [**Динамічний DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Докладні інструкції див. у посібнику [**GoodCloud**](../../interface_guide/cloud.md).

### Мережеве сховище {#network-storage}

Докладні інструкції див. у посібнику [**Мережеве сховище**](../../interface_guide/network_storage.md).

### AdGuard Home {#adguard-home}

Докладні інструкції див. у посібнику [**AdGuard Home**](../../interface_guide/adguardhome.md).

### Батьківський контроль {#parental-control}

Докладні інструкції див. у посібнику [**Батьківський контроль**](../../interface_guide/parental_control.md).

### ZeroTier {#zerotier}

Докладні інструкції див. у посібнику [**ZeroTier**](../../interface_guide/zerotier.md).

### Tailscale {#tailscale}

Докладні інструкції див. у посібнику [**Tailscale**](../../interface_guide/tailscale.md).

---

## Мережа {#network}

### Міжмережевий екран {#firewall}

Маршрутизатори GL.iNet містять кілька функцій міжмережевого екрана для захищеного з’єднання та повного контролю з боку користувача. Вони дають змогу налаштувати правила, зокрема Port Forwarding, Open Ports і DMZ.

[Докладніше про міжмережевий екран маршрутизаторів GL.iNet](../../interface_guide/firewall.md)

### Multi-WAN {#multi-wan_1}

Докладні інструкції див. у посібнику [**Multi-WAN**](../../interface_guide/multi-wan.md).

### LAN {#lan}

Докладні інструкції див. у посібнику [**LAN**](../../interface_guide/lan.md).

### DNS {#dns}

Докладні інструкції див. у посібнику [**DNS**](../../interface_guide/dns.md).

### Режим роботи мережі {#network-mode}

Докладні інструкції див. у посібнику [**Режим роботи мережі**](../../interface_guide/network_mode.md).

### IPv6 {#ipv6}

Докладні інструкції див. у посібнику [**IPv6**](../../interface_guide/ipv6.md).

### MAC-адреса {#mac-address}

Сторінка Mac Address раніше називалася Mac Clone. Починаючи з v4.2, її перейменовано на Mac Address.

Докладні інструкції див. у посібнику [**MAC-адреса**](../../interface_guide/mac_address.md).

### Drop-in Gateway {#drop-in-gateway}

Докладні інструкції див. у посібнику [**Drop-in Gateway**](../../interface_guide/drop-in_gateway.md).

### IGMP Snooping {#igmp-snooping}

Докладні інструкції див. у посібнику [**IGMP Snooping**](../../interface_guide/igmp_snooping.md).

---

## Система {#system}

### Огляд {#overview}

Докладні інструкції див. у посібнику [**Огляд системи**](../../interface_guide/system_overview.md).

### Оновлення {#upgrade}

GL.iNet регулярно оновлює прошивки маршрутизаторів, щоб поліпшувати продуктивність, усувати помилки та виправляти вразливості.

Докладні інструкції див. у посібнику [**Оновлення**](../../interface_guide/upgrade.md).

### Завдання за розкладом {#scheduled-tasks}

Докладні інструкції див. у посібнику [**Завдання за розкладом**](../../interface_guide/scheduled_tasks.md).

### Пароль адміністратора {#admin-password}

Починаючи з v4.5, цю функцію перенесено до розділу [**Security**](../../interface_guide/security.md).

Докладні інструкції див. у посібнику [**Пароль адміністратора**](../../interface_guide/admin_password.md).

### Часовий пояс {#time-zone}

Докладні інструкції див. у посібнику [**Часовий пояс**](../../interface_guide/time_zone.md).

### Налаштування кнопки перемикання {#toggle-button-settings}

Докладні інструкції див. у посібнику [**Налаштування кнопки перемикання**](../../interface_guide/toggle_button_settings.md).

### Журнали {#log}

Докладні інструкції див. у посібнику [**Журнали**](../../interface_guide/log.md).

### Безпека {#security}

Ця функція доступна починаючи з v4.5.

Докладні інструкції див. у посібнику [**Безпека**](../../interface_guide/security.md).

### Скидання налаштувань прошивки {#reset-firmware}

Докладні інструкції див. у посібнику [**Скидання налаштувань прошивки**](../../interface_guide/reset_firmware.md).

### Додаткові налаштування {#advanced-settings}

Докладні інструкції див. у посібнику [**Додаткові налаштування**](../../interface_guide/advanced_settings.md).
