# Міжмережевий екран {#firewall}

Ця інструкція стосується прошивки v4.5 і попередніх версій.

Починаючи з v4.6, сторінку Firewall розділено: функції Port Forwarding і DMZ перенесено на сторінку [Port Forwarding](port_forwarding.md), а функцію Open Ports — на сторінку [Security](security.md).

---

У лівому меню вебпанелі адміністрування відкрийте **NETWORK** -> **Firewall**.

На сторінці Firewall можна налаштовувати правила міжмережевого екрана: **Port Forwarding**, **Open Ports on Router** і **DMZ**.

## Перенаправлення портів {#port-forwards}

Перенаправлення портів дозволяє віддаленим комп’ютерам підключатися до локального комп’ютера або сервера в LAN за міжмережевим екраном маршрутизатора, наприклад до вебсервера або FTP-сервера.

Щоб налаштувати перенаправлення портів, відкрийте вкладку **Port Forwards** і натисніть **Add**.

![Сторінка міжмережевого екрана](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

У спливному вікні додайте нове правило перенаправлення портів і натисніть **Apply**.

![Додавання правила перенаправлення портів](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** назва правила.

**Protocol:** протокол. Можна вибрати TCP, UDP або TCP і UDP одночасно.

**External Zone:** доступні зовнішні зони: `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** номери зовнішніх портів. Тут можна ввести певний номер порту.

**Internal Zone:** доступні внутрішні зони: `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** IP-адреса, яку маршрутизатор призначив пристрою, до якого потрібен віддалений доступ.

**Internal Port:** номер внутрішнього порту пристрою. Можна ввести певний номер порту. Залиште поле порожнім, якщо він збігається із зовнішнім портом.

**Enable:** увімкнення або вимкнення правила.

## Відкриття портів на маршрутизаторі {#open-ports-on-router}

Щоб служби маршрутизатора, наприклад вебслужба або FTP, були доступні ззовні, на маршрутизаторі потрібно відкрити відповідні порти.

Щоб відкрити порт, виберіть вкладку **Open Ports on Router** і натисніть **Add**.

![Відкриття портів на маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

У спливному вікні відкрийте новий порт і натисніть **Apply**.

![Відкриття портів на маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** назва правила, яку задає користувач.

**Protocol:** протокол. Можна вибрати TCP, UDP або TCP і UDP одночасно.

**Port:** номер порту, який потрібно відкрити.

**Enable:** увімкнення або вимкнення правила.

## DMZ {#dmz}

DMZ дозволяє надати доступ до одного комп’ютера з інтернету: усі вхідні пакети перенаправлятимуться на цей комп’ютер.

Увімкніть **Enable DMZ**. Виберіть внутрішню IP-адресу пристрою, який отримуватиме всі вхідні пакети.

![Налаштування DMZ](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
