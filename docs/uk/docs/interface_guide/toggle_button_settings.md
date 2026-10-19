# Налаштування кнопки-перемикача {#toggle-button-settings}

У Toggle Button Settings можна призначити певні функції фізичному перемикачу маршрутизатора (на деяких моделях він також називається перемикачем режимів). Це забезпечує швидкий доступ і зручне керування поширеними операціями.

Налаштуйте поведінку перемикача у вебпанелі адміністрування.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-MT1300 (Beryl)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-S200
    - GL-E750V2 (Mudi V2)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)

??? "Моделі без підтримки"

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Налаштування {#setup}

У меню ліворуч у вебпанелі адміністрування перейдіть до **SYSTEM** -> **Toggle Button Settings**.

![Налаштування кнопки-перемикача](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_settings.jpg){class="glboxshadow"}

До прошивки v4.8 для налаштування функції кнопки-перемикача доступні п’ять варіантів.

- No Function
- AdGuard Home
- OpenVPN Client
- Tor
- WireGuard Client

Починаючи з прошивки v4.8, додано нові варіанти: Repeater, Wi-Fi і LED. Налаштуйте функції кнопки-перемикача відповідно до потреб.

- No Function
- Repeater
- Wi-Fi (Main/Guest Wi-Fi)
- VPN
- Tor
- AdGuard Home
- LED

![Варіанти функцій перемикача у прошивці v4.8](https://static.gl-inet.com/docs/router/en/4/interface_guide/toggle_button_settings/toggle_button_4.8.png){class="glboxshadow"}

Під час застосування налаштувань можна вибрати, чи одразу вмикати або вимикати вибрану функцію відповідно до положення перемикача: увімкнено або вимкнено (ліворуч або праворуч).

**Примітка**: Після перезавантаження пристрою система автоматично встановлює стан функції відповідно до положення перемикача.

Наприклад, якщо налаштувати керування WireGuard Client за допомогою перемикача, у положенні LEFT (ON) WireGuard Client запускається автоматично. У положенні RIGHT (OFF) WireGuard Client залишається вимкненим.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
