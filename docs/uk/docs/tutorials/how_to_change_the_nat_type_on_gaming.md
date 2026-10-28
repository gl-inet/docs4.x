# Як змінити тип NAT для ігор? {#how-to-change-the-nat-type-on-gaming}

Деякі розробники ігор рекомендують увімкнути UPnP на маршрутизаторі для кращого типу NAT. Однак UPnP має потенційні ризики для безпеки.

Тієї самої мети можна досягти, налаштувавши DMZ або перенаправлення портів на маршрутизаторі. Перш ніж увімкнути будь-яку з цих функцій, ознайомтеся з принципом її роботи й пов’язаними ризиками для безпеки.

## Перевірка IP-адреси ігрового пристрою {#check-your-game-ip}

Спочатку увійдіть до маршрутизатора. Відкрийте список клієнтів і перевірте IP-адресу ігрового пристрою. Вона знадобиться для подальшого налаштування.

![IP-адреса ігрового пристрою](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/gameip.png){class="glboxshadow"}

## Спосіб 1: DMZ {#method-1-dmz}

У меню ліворуч відкрийте **Network** -> **Port Forwarding** і ввімкніть DMZ для IP-адреси ігрового пристрою.

![DMZ для ігрового пристрою](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/dmzgame.png){class="glboxshadow"}

## Спосіб 2: перенаправлення портів {#method-2-port-forward}

У меню ліворуч відкрийте **Network** -> **Port Forwarding** і додайте потрібні порти для IP-адреси ігрового пристрою.

![Перенаправлення ігрових портів](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/inputport.png){class="glboxshadow"}

Приклад: порти для PS5

UDP 3074, 3478-3479

TCP 1935, 3478-3480


![Порти PS5](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/ps5port.png){class="glboxshadow"}

Порти Xbox

UDP 88, 3074

TCP 3074

Для деяких ігор потрібно перенаправити інші порти. Докладніше дивіться на цьому вебсайті.

[Перенаправлення портів для різних ігор](https://portforward.com/games/)

## Full Cone NAT {#full-cone-nat}

Щоб зменшити затримку, можна ввімкнути Full Cone NAT. Ця функція доступна починаючи з прошивки v4.5.

Перейдіть до **Network** -> **NAT Settings**, за потреби ввімкніть **Full Cone NAT** і натисніть **Apply**.

![Увімкнення Full Cone NAT](https://static.gl-inet.com/docs/router/en/4/tutorials/gamling/conenat.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
