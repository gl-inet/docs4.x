# Порти Ethernet (прошивка v4.10) {#ethernet-port-firmware-v410}

**Примітка**: описані на цій сторінці можливості вперше з’явилися на Flint 4 (GL-BE14000) і будуть доступні на інших моделях у прошивці v4.10.

Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.10" markdown="1">

- [Прошивка v4.9 і попередні версії](ethernet_port.md)

</div>

---

У лівому меню вебпанелі адміністрування відкрийте **NETWORK** -> **Ethernet Port**.

На цій сторінці відображаються всі інтерфейси маршрутизатора. Можна переглядати стан підключення кожного інтерфейсу, керувати ролями портів Ethernet (WAN або LAN) і переглядати відомості про порти: MAC-адресу, узгоджену швидкість та поточний стан з’єднання. Також можна призначати фізичні інтерфейси будь-яким створеним підмережам.

![Порти Ethernet](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: синя піктограма порту означає, що фізичне з’єднання активне.

- **Link Down**: сіра піктограма порту означає, що фізичне з’єднання неактивне.

- **Speed**: узгоджена швидкість передавання даних порту Ethernet.

- **MAC**: MAC-адреса порту.

- **VLAN Mode**: для портів LAN можна вибрати режим Standard або Multiple VLANs.

- **Native Network**: підмережа для трафіку без тегів, призначена порту LAN за замовчуванням.

- **Allowed VLANs**: VLAN із тегами, трафік яких дозволено передавати через цей порт у режимі Multiple VLANs.

- **Settings**: натисніть, щоб відкрити сторінку налаштування окремого порту.

## WAN {#wan}

У цьому розділі відображаються Port Mode (WAN або LAN), MAC-адреса та узгоджена швидкість.

![Налаштування WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: поточний режим роботи фізичного порту WAN. За потреби можна змінити його на LAN.

- **MAC Mode**: за замовчуванням використовується Factory Mode. Можна вибрати Clone Mode або Random Mode.

- **MAC Address**: MAC-адреса інтерфейсу WAN.

- **Negotiated Network Port Rate**: узгоджена швидкість з’єднання інтерфейсу WAN; відображається лише за наявності дійсного з’єднання.

## LAN {#lan}

У цьому розділі відображаються налаштування порту LAN. За потреби для Ethernet Mode можна вибрати **Standard** або **Multiple VLANs**.

### Стандартний режим {#standard-mode}

Стандартний режим дозволяє лише одну VLAN без тегів (Untagged) і використовується для підключення кінцевих пристроїв.

![Стандартний режим LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: узгоджена швидкість з’єднання інтерфейсу LAN; відображається лише за наявності дійсного з’єднання.

- **Ethernet Mode**: за замовчуванням використовується Standard Mode.

- **Access Network**: дає змогу ізолювати мережі, призначаючи порти LAN різним підмережам.

Після налаштування поверніться на сторінку Ethernet Port, щоб перевірити параметри.

### Режим кількох VLAN {#multiple-vlans-mode}

Режим Multiple VLANs дозволяє використовувати кілька VLAN із тегами (Tagged) на одному порту. Зазвичай він використовується для підключення точок доступу або інших комутаторів.

![Режим кількох VLAN для LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: узгоджена швидкість з’єднання інтерфейсу LAN; відображається лише за наявності дійсного з’єднання.

- **VLAN Mode**: щоб перейти в режим Multiple VLANs, натисніть вкладку Multiple VLANs.

- **Untagged Traffic Handling**: налаштуйте обробку пакетів без тегів на порту. Можна відкидати такі пакети або пересилати їх в іншу підмережу, яка використовуватиметься як мережа PVID для трафіку без тегів.

- **Allowed Tagged Networks**: VLAN, трафік яких дозволено передавати через цей порт із тегами. Виберіть мережі VLAN зі списку; пересилатиметься лише відповідний трафік.

Після налаштування поверніться на сторінку Ethernet Port, щоб перевірити параметри.

Деякі моделі дозволяють змінити роль LAN 1 на WAN для використання двох Ethernet-з’єднань WAN. Докладніше див. [два Ethernet-з’єднання WAN](#dual-ethernet-wan).

## Два Ethernet-з’єднання WAN {#dual-ethernet-wan}

Функція Dual-Ethernet WAN дозволяє перетворити порт Ethernet, який за замовчуванням працює як LAN, на другий порт WAN для доступу до інтернету через два Ethernet-з’єднання. Вона забезпечує резервне підключення та підтримує агрегацію пропускної здатності за наявності сумісності для завдань із великим обсягом трафіку. Також можна одночасно підключатися до двох незалежних мереж (наприклад, робочої та особистої) без додаткового обладнання.

??? "Підтримувані моделі"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Примітка**: GL-E5800 (Mudi 7) має один порт Ethernet (за замовчуванням LAN, можна змінити на WAN) і **порт USB-C із підтримкою OTG**. Щоб додати другий порт Ethernet для Dual-Ethernet WAN, підключіть до порту USB-C адаптер USB-C–Ethernet, який продається окремо.

??? "Непідтримувані моделі"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Виконайте наведені нижче дії, щоб змінити роль порту LAN на WAN. У прикладі використано Flint 3 (GL-BE9300).

1. На сторінці **Ethernet Port** натисніть налаштування **LAN1**, щоб відкрити сторінку конфігурації. Змініть роль порту на WAN і натисніть **Apply**.

    ![Два Ethernet-з’єднання WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![Зміна ролі LAN1 на WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Поверніться на сторінку Ethernet Port, щоб перевірити, чи роль порту змінено на WAN.

    ![Роль порту змінено на WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. Вибраний порт тепер працюватиме як WAN. Далі можна налаштувати Multi-WAN за [цією інструкцією](multi-wan.md).

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
