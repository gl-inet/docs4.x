# Посібник користувача GL-S200 {#gl-s200-user-guide}

<span id="hardware-info"></span>

## Огляд пристрою {#product-overview}

GL-S200 — це мініатюрний шлюз Thread із підтримкою протоколу BLE. Він працює на операційній системі OpenWrt із широкими можливостями налаштування та підтримує хмарне керування пристроями. Універсальний дизайн дає змогу підключати різні пристрої розумного дому або велику кількість пристроїв у розумних будівлях.

![Інтерфейси gl-s200](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_interface.jpg){class="glboxshadow"}

## Комплект постачання {#package-contents}

Зверніть увагу, що адаптер у комплекті залежить від країни доставки.

До комплекту входять:

- 1 x Посібник користувача
- 1 x GL-S200
- 1 x Кабель Ethernet
- 1 x Картка з подякою
- 1 x Гарантійна картка
- 1 x Адаптер живлення (вибраний тип вилки)

![Комплект gl-s200](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/first_time_setup/s200_unboxing.jpg){class="glboxshadow"}

Перегляньте [відео розпакування](../../video_library/unboxing_first_set_up.md#gl-s200) GL-S200.

## Технічні характеристики {#specifications}

[Технічні характеристики GL-S200](https://www.gl-inet.com/products/gl-s200/#specs){target="_blank"}

## Розпінування друкованої плати {#pcb-pinout}

<div class="gl-lightbox" itemscope itemtype="http://schema.org/ImageGallery">
  <figure itemprop="associatedMedia" itemscope itemtype="http://schema.org/ImageObject">
    <a href="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="contentUrl" data-size="1500x1235">
      <img src="https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl-s200_pinout.jpg" itemprop="thumbnail" alt="Розпінування gl-s200" loading="lazy" />
    </a>
  </figure>
</div>

## Розпінування плати розробки GL Thread {#gl-thread-dev-board-pinout}

![Розпінування плати розробки GL Thread](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/hardware_info/gl_thread_dev_board_pinout.jpg){class="glboxshadow"}

---

## Перше налаштування {#first-time-setup}

Процедура налаштування всіх маршрутизаторів GL.iNet подібна. Див. [посібник із першого налаштування](../../faq/first_time_setup.md).

---

## Інтернет {#internet}

Увійдіть до вебпанелі адміністрування маршрутизатора та виберіть **INTERNET** у меню ліворуч.

На цій сторінці можна вибрати тип інтернет-з’єднання, наприклад Ethernet, Repeater, Tethering або Cellular, залежно від моделі.

GL-S200 підтримує два типи з’єднання: Ethernet і Repeater.

### Ethernet {#ethernet}

Підключіть маршрутизатор до працюючого модема або мережевого пристрою за допомогою кабелю Ethernet для доступу до інтернету. Цей спосіб зазвичай забезпечує найшвидше та найнадійніше інтернет-з’єднання.

[Підключення до інтернету через кабель Ethernet](../../interface_guide/internet_ethernet.md)

![З’єднання Ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_ethernet.png){class="glboxshadow"}

### Repeater {#repeater}

Налаштуйте маршрутизатор як повторювач для розширення покриття наявної мережі Wi-Fi. У цьому режимі він приймає та повторно передає бездротові сигнали у своєму радіусі дії, збільшуючи зону покриття. Цей спосіб корисний, коли один маршрутизатор не охоплює всю потрібну територію.

[Підключення до інтернету через наявну мережу Wi-Fi](../../interface_guide/internet_repeater.md)

![З’єднання Repeater](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-s200/internet/s200_repeater.png){class="glboxshadow"}

### Multi-WAN {#multi-wan}

Multi-WAN — це мережева функція, яка дає змогу одночасно налаштувати кілька інтернет-з’єднань, наприклад Ethernet і Repeater. Якщо з’єднання з найвищим пріоритетом перестане працювати, маршрутизатор автоматично перемкнеться на інше. Це також називається аварійним перемиканням (Failover) і забезпечує безперервний доступ до інтернету.

Перейдіть до [Multi-WAN](../../interface_guide/multi-wan.md), щоб установити пріоритет кожного інтернет-з’єднання.

Також можна змінити режим Multi-WAN із Failover на Load Balance. У цьому режимі кілька мережевих інтерфейсів використовуються одночасно для збільшення сумарної пропускної здатності маршрутизатора.

---

## Бездротова мережа {#wireless}

Налаштування бездротової мережі дають змогу керувати безпекою основної та гостьової мереж Wi-Fi. Щоб відкрити їх, виберіть **WIRELESS** у бічному меню.

[Докладніше про налаштування бездротової мережі](../../interface_guide/wireless.md)

---

## Клієнти {#clients}

Клієнти — це пристрої, підключені до маршрутизатора. Їх можна блокувати або обмежувати швидкість їхнього з’єднання. Щоб відкрити цей розділ, натисніть **CLIENTS** у бічному меню вебпанелі адміністрування маршрутизатора.

[Докладніше про керування клієнтськими пристроями](../../interface_guide/clients.md)

---

## Мережа Thread Mesh {#thread-mesh}

Див. [Thread Mesh](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/thread_mesh/) у документації IoT.

---

## Плата розробки GL {#gl-dev-board}

Див. [Плата розробки GL](https://docs.gl-inet.com/iot/en/iot_dev_board/) у документації IoT.

---

## Bluetooth {#bluetooth}

Див. [Bluetooth](https://docs.gl-inet.com/iot/en/thread_board_router/gl-s200/bluetooth/) у документації IoT.

---

## VPN {#vpn}

На маршрутизаторах GL.iNet попередньо встановлено OpenVPN і WireGuard® із підтримкою 30+ служб VPN. Коли клієнт VPN увімкнено, маршрутизатор може шифрувати трафік пристроїв у мережі, зокрема пристроїв, на яких не можна запускати застосунки VPN, відповідно до налаштувань політики VPN. Наші маршрутизатори також можуть працювати як сервери VPN: трафік клієнтських пристроїв у віддалених місцях спочатку спрямовується через VPN-тунель на сервер VPN, а потім — до публічного інтернету.

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

---

## Застосунки {#applications}

Маршрутизатори GL.iNet мають різноманітні додаткові функції, які спрощують керування пристроєм, поліпшують роботу в інтернеті, автоматизують оновлення прошивки тощо.

### Плагіни {#plug-ins}

Докладні інструкції див. у посібнику [**Плагіни**](../../interface_guide/plugins.md).

### Динамічний DNS {#dynamic-dns}

Докладні інструкції див. у посібнику [**Динамічний DNS**](../../interface_guide/ddns.md).

### GoodCloud {#goodcloud}

Докладні інструкції див. у посібнику [**GoodCloud**](../../interface_guide/cloud.md).

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

### IPv6 {#ipv6}

Докладні інструкції див. у посібнику [**IPv6**](../../interface_guide/ipv6.md).

### MAC-адреса {#mac-address}

Сторінка Mac Address раніше називалася Mac Clone. Починаючи з v4.2, її перейменовано на Mac Address.

Докладні інструкції див. у посібнику [**MAC-адреса**](../../interface_guide/mac_address.md).

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
