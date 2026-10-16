# Tor {#tor}

Tor (скорочення від **The Onion Router**) — безкоштовне програмне забезпечення з відкритим вихідним кодом для анонімного зв’язку. Воно допомагає зберігати конфіденційність під час користування інтернетом. [Докладніше про Tor](https://www.torproject.org/){target="_blank"}.

**Примітка**: Ця функція наразі перебуває в бета-тестуванні та може мати проблеми в деяких країнах. Коли Tor увімкнено, такі функції працюватимуть некоректно:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Примітка**: Моделі, позначені *, не мають вбудованої підтримки Tor, але на них можна вручну встановити Tor через плагін. Докладніше дивіться [тут](#manual-install).

??? "Моделі без підтримки"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Швидке налаштування {#quick-setup}

У меню ліворуч у вебпанелі адміністрування перейдіть до **VPN** -> **Tor**.

Для прошивки 4.8.4 та новіших версій перейдіть до **APPLICATIONS** -> **Tor**.

Увімкніть функцію за допомогою перемикача, за потреби ввімкніть **Custom Exit Nodes** і натисніть **Apply**.

![Увімкнення Tor](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/enable_tor.png){class="glboxshadow"}

Почнеться встановлення з’єднання. Якщо мережа відповідає вимогам, з’явиться стан успішного підключення.

![Успішне з’єднання Tor](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/connected.png){class="glboxshadow" width="672"}

## Установлення вручну {#manual-install}

**Примітка**: На деякі моделі можна вручну встановити Tor через плагін, проте це може збільшити навантаження на процесор і сповільнити роботу системи.

У меню ліворуч у вебпанелі адміністрування перейдіть до **APPLICATIONS** -> **Plug-ins**.

Знайдіть **gl-sdk4-ui-torview** і встановіть його.

![Установлення плагіна Tor](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torview.jpg){class="glboxshadow"}

![Сторінка Tor після встановлення](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torpage.jpg){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
