# Бездротова мережа {#wireless}

Ця сторінка описує прошивку v4.9 та новіші версії. Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.9 та новіші версії" markdown="1">

- [Прошивка v4.8 та раніші версії](wireless_v4.8.md)

</div>

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **WIRELESS**.

На сторінці Wireless можна налаштувати різні мережі Wi-Fi: MLO Wi-Fi (доступна на окремих моделях), Main Network, Guest Network та IoT Network. Підтримувані діапазони Wi-Fi залежать від моделі.

## Багатоканальна робота (MLO) {#multi-link-operation-mlo}

??? "Підтримувані моделі"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Моделі без підтримки"
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation, багатоканальна робота) — одна з основних функцій Wi-Fi 7 (802.11be). Вона підвищує продуктивність мережі, значно зменшує затримку та поліпшує стабільність з’єднання, одночасно використовуючи кілька частотних діапазонів, зокрема 2.4 GHz, 5 GHz і 6 GHz.

Клієнтів Wi-Fi 7 рекомендовано підключати до MLO Wi-Fi: з’єднання в кількох діапазонах значно підвищують пропускну здатність і надійність мережі.

Натисніть **Add**, щоб налаштувати мережу MLO Wi-Fi, а потім **Apply**. Доступні діапазони Wi-Fi залежать від моделі.

![Додавання мережі MLO Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![Налаштування мережі MLO Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: Виберіть щонайменше два радіодіапазони.
- Wi-Fi Security: Якщо вибрано діапазон 6 GHz, єдиний доступний і рекомендований варіант — WPA3-SAE. Він найкраще працює з більшістю пристроїв із підтримкою MLO.
- Enable Randomized BSSID: Якщо вибрано діапазон 6 GHz, BSSID MLO Wi-Fi для цього діапазону синхронізується з Main Wi-Fi.

Після ввімкнення сторінка матиме такий вигляд:

![Увімкнена мережа MLO Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Основна мережа {#main-network}

Main Network — основна мережа Wi-Fi, яка підтримує одночасне передавання в різних радіодіапазонах. Усі вони ввімкнені за замовчуванням. Для кожного діапазону можна окремо налаштувати SSID Wi-Fi, режим безпеки, пароль, випадковий BSSID, потужність TX, ширину каналу та канал.

![Основна мережа Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

Натисніть значок шестірні праворуч, щоб переглянути або змінити налаштування Wi-Fi для кожного діапазону.

**Примітка**: Доступні діапазони Wi-Fi залежать від моделі.

- 6 GHz

    ![Основна мережа Wi-Fi 6 GHz](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![Основна мережа Wi-Fi 5 GHz](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![Основна мережа Wi-Fi 2.4 GHz](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Гостьова мережа {#guest-network}

Guest Network — окрема мережа Wi-Fi для відвідувачів. Усі діапазони вимкнені за замовчуванням. Для кожного діапазону можна ввімкнути мережу та налаштувати основні параметри: SSID Wi-Fi, режим безпеки, пароль і випадковий BSSID.

Натисніть **Add**, щоб налаштувати гостьову мережу Wi-Fi, а потім **Apply**.

**Примітка**: Доступні діапазони Wi-Fi залежать від моделі.

![Додавання гостьової мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![Налаштування гостьової мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

Після ввімкнення сторінка матиме такий вигляд:

![Увімкнена гостьова мережа Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## Мережа IoT {#iot-network}

IoT Network — окрема мережа Wi-Fi для розумних пристроїв. Усі діапазони вимкнені за замовчуванням. Для кожного діапазону можна ввімкнути мережу та налаштувати основні параметри: SSID Wi-Fi, режим безпеки, пароль і випадковий BSSID.

Натисніть **Add**, щоб налаштувати мережу Wi-Fi для IoT, а потім **Apply**.

**Примітка**: Мережа IoT не підтримує діапазон 6 GHz. Доступні діапазони Wi-Fi залежать від моделі.

![Додавання мережі Wi-Fi для IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![Налаштування мережі Wi-Fi для IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

Після ввімкнення сторінка матиме такий вигляд:

![Увімкнена мережа Wi-Fi для IoT](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"}.
