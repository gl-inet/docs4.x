# MAC-адреса {#mac-address}

Цей посібник стосується прошивки v4.5 та раніших версій.

Раніше сторінка MAC Address називалася MAC Clone; починаючи з v4.2, її перейменовано на MAC Address.

Починаючи з v4.6, налаштування MAC-адрес інтерфейсів Ethernet і Repeater перенесено відповідно на сторінки [Ethernet Port](ethernet_port.md) і [Repeater](internet_repeater.md).

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **NETWORK** -> **MAC Address**.

Тут можна переглянути MAC-адресу маршрутизатора за замовчуванням, клонувати MAC-адресу клієнта, ввести MAC-адресу вручну або створити випадкову MAC-адресу.

Якщо пристрій підтримує використання кількох портів Ethernet як портів WAN, можна задати MAC-адресу для кожного порту окремо. Налаштування MAC-адреси діє лише тоді, коли порт Ethernet використовується як порт WAN.

![Заводська MAC-адреса](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* Заводська MAC-адреса за замовчуванням.

    ![Заводська MAC-адреса](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Клонування MAC-адреси клієнта.

    ![Клонування MAC-адреси](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Примітка:** Багато сучасних пристроїв використовують різні випадкові MAC-адреси для підключення до різних мереж Wi-Fi. Тому показана тут MAC-адреса може не відповідати фізичній MAC-адресі пристрою користувача. На різних пристроях цей параметр може називатися Private Wi-Fi Address або random hardware address.

* Уведення MAC-адреси вручну або створення випадкової адреси.

    ![Уведення MAC-адреси вручну або створення випадкової адреси](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Сценарії використання {#usage-scenarios}

Під час підключення до публічної точки доступу використовуйте випадкову MAC-адресу, якщо не хочете, щоб точка доступу знала вашу справжню MAC-адресу або обмежувала доступ до інтернету на її основі. Дивіться посібник [Підключення до точки доступу з порталом авторизації](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
