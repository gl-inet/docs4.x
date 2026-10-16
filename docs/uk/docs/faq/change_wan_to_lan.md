# Зміна ролі WAN на LAN {#change-wan-to-lan}

Порт WAN маршрутизатора можна перетворити на порт LAN. Це особливо корисно під час роботи маршрутизатора як ретранслятора, коли порт WAN не потрібний. Так ви отримаєте додатковий порт LAN для підключення пристроїв.

Виконайте наведені нижче дії, щоб змінити WAN на LAN.

## Для прошивки 4.10 {#for-firmware-410}

1. Залиште порт WAN непідключеним.

2. Підключіть пристрій до маршрутизатора та відкрийте його вебпанель адміністрування.

3. У вебпанелі адміністрування відкрийте **INTERNET** -> **Ethernet 1** і натисніть піктограму шестерні у верхньому правому куті.

	![Налаштування Ethernet 1](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_1.png){class="glboxshadow"}

4. Відкриється сторінка **Ethernet Port**. Натисніть піктограму шестерні під портом WAN.

    ![Порти Ethernet](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_2.png){class="glboxshadow"}

5. Натисніть **LAN**, щоб змінити роль порту Ethernet, і натисніть **Apply**.

    ![Зміна ролі порту на LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_3.png){class="glboxshadow"}

6. Поверніться на сторінку Ethernet Port або до розділу Ethernet. Відобразиться, що порт WAN тепер використовується як LAN.

    ![Порт використовується як LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_4.png){class="glboxshadow"}

	![Інтерфейс Ethernet після зміни ролі](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_port_5.png){class="glboxshadow"}

Щоб повернути роль WAN, змініть її на сторінці Ethernet Port або утримуйте кнопку RESET протягом 4 секунд для відновлення інтерфейсу WAN.

## Для прошивки 4.7–4.9 {#for-firmware-47-49}

1. Залиште порт WAN непідключеним.

2. Підключіть пристрій до маршрутизатора та відкрийте його вебпанель адміністрування.

3. У вебпанелі адміністрування відкрийте **INTERNET** -> **Ethernet** і натисніть піктограму шестерні у верхньому правому куті.

	![Керування портами](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_gear_icon.png){class="glboxshadow"}

	Відкриється сторінка **Port Management**, на якій показано, що порт WAN використовується для WAN.

	![Керування портами](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/port_management.jpg){class="glboxshadow"}

4. Натисніть **LAN**, щоб змінити роль порту Ethernet, і натисніть **Apply**.

	![Застосування ролі LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/switch_to_lan_apply.jpg){class="glboxshadow"}

	У вікні попередження натисніть **Apply** для підтвердження.

	![Попередження про зміну ролі порту](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/caution.png){class="glboxshadow"}

	**Примітка**: під час цієї дії Wi-Fi може тимчасово відключитися. Після завершення підключіться до маршрутизатора повторно.

5. Поверніться до розділу Ethernet. Відобразиться, що порт WAN тепер використовується як LAN.

	![Порт WAN використовується як LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/wan_using_as_lan.png){class="glboxshadow"}

	Щоб повернути роль WAN, змініть її на сторінці **Port Management** або утримуйте кнопку RESET протягом 4 секунд для відновлення інтерфейсу WAN.

## Для прошивки 4.6 і попередніх версій {#for-firmware-46-and-earlier}

1. Залиште порт WAN непідключеним.

2. Підключіть пристрій до маршрутизатора та відкрийте вебпанель адміністрування.

3. У вебпанелі адміністрування відкрийте **INTERNET** -> **Ethernet**. Для порту WAN відображається стан **Using as WAN**. Натисніть **Change to LAN**.

	![Сторінка Internet](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_no_cable.png){class="glboxshadow"}

4. Натисніть **Apply** для підтвердження.

	![Підтвердження зміни WAN на LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_change_to_lan_caution.png){class="glboxshadow"}

	**Примітка**: під час цієї дії Wi-Fi може тимчасово відключитися. Після завершення підключіться до маршрутизатора повторно.

5. Поверніться до розділу Ethernet. Відобразиться `Using as LAN`.

	![Стан Using as LAN](https://static.gl-inet.com/docs/router/en/4/faq/change_wan_to_lan/ethernet_using_as_lan.png){class="glboxshadow"}

	Щоб повернути попереднє налаштування, повторіть наведені вище дії.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
