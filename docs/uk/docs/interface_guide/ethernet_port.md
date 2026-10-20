# Порти Ethernet {#ethernet-port}

Ця сторінка описує прошивки v4.7-4.9. Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.9 та раніші версії" markdown="1">

- [Прошивка v4.10](ethernet_port_v4.10.md)

</div>

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **NETWORK** -> **Ethernet Port** або **Port Management**.

Тут можна керувати ролями портів Ethernet (WAN/LAN) і переглядати відомості про порти, зокрема MAC-адресу та узгоджену швидкість.

## WAN {#wan}

У цьому розділі відображаються роль порту (WAN або LAN), MAC-адреса та узгоджена швидкість.

![Параметри порту WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

- **WAN/LAN**: Поточний режим роботи фізичного порту WAN. За потреби можна змінити його на LAN.

- **MAC Mode**: За замовчуванням вибрано Factory Mode. Можна змінити його на Clone Mode або Random Mode.

- **MAC Address**: MAC-адреса інтерфейсу WAN.

- **Negotiated Network Port Rate**: Узгоджена швидкість з’єднання інтерфейсу WAN. Відображається лише за наявності активного з’єднання.

## LAN {#lan}

У цьому розділі відображається узгоджена швидкість порту LAN. Розділ відображається лише за наявності активного з’єднання.

![Параметри порту LAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Деякі моделі підтримують перемикання LAN 1 у режим порту WAN для використання двох каналів WAN через Ethernet. Докладніше дивіться в розділі [Два канали WAN через Ethernet](#dual-ethernet-wan).

## Два канали WAN через Ethernet {#dual-ethernet-wan}

Функція Dual-Ethernet WAN дає змогу перетворити порт Ethernet, який за замовчуванням працює як LAN, на другий порт WAN для доступу до інтернету через два канали Ethernet. Це забезпечує надійне резервне з’єднання та підтримує об’єднання пропускної здатності (за наявності сумісності) для завдань з інтенсивним використанням мережі. Також можна одночасно підключатися до двох незалежних мереж (наприклад, робочої та особистої), що додає гнучкості без додаткового обладнання.

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
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Примітка**: GL-E5800 (Mudi 7) має один порт Ethernet (за замовчуванням LAN, який можна перемкнути на WAN) і **порт USB-C з підтримкою OTG**. Щоб додати другий порт Ethernet для Dual-Ethernet WAN, підключіть до порту USB-C адаптер USB‑C‑to‑Ethernet, який продається окремо.

??? "Моделі без підтримки"
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

Виконайте наведені нижче дії, щоб перемкнути порт LAN у режим WAN.

1. На сторінці **Port Management** або **Ethernet Port** відкрийте вкладку **LAN**, змініть роль порту на WAN і натисніть **Apply**.

    ![Зміна ролі порту LAN на WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. У спливному вікні натисніть **Apply**.

    ![Підтвердження зміни ролі порту](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. Тепер вибраний порт працюватиме як порт WAN. Далі можна перейти до [налаштування Multi-WAN](multi-wan.md).

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
