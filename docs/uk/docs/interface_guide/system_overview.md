# Огляд системи {#system-overview}

У лівому меню вебпанелі адміністрування відкрийте **SYSTEM** -> **Overview**.

На сторінці Overview відображається стан обладнання та доступні прості дії керування:

- Стан CPU, оперативної пам’яті, флешпам’яті та зовнішніх накопичувачів.
- Стан обладнання, зокрема вентилятора, акумулятора тощо.
- Керування світлодіодними індикаторами та вентилятором.
- Відомості про пристрій.

У цьому прикладі використано GL-MT3000.

![Огляд системи](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/overview.png){class="glboxshadow"}

## Середнє навантаження CPU {#cpu-average-load}

Для більшості моделей без вентилятора середнє навантаження CPU відображається так:

![Середнє навантаження CPU на моделі без вентилятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/cpu_average_load_no_fan.jpg){class="glboxshadow"}

Для деяких моделей із вбудованим вентилятором середнє навантаження CPU відображається так:

![Середнє навантаження CPU на моделі з вентилятором](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/cpu_average_load.png){class="glboxshadow gl-70-desktop"}

Наведіть вказівник миші на графік, щоб переглянути точні значення.

Натисніть температуру праворуч, щоб перемикатися між градусами Цельсія та Фаренгейта.

Натисніть піктограму вентилятора у верхньому правому куті, щоб відкрити Fan Settings.

![Налаштування вентилятора](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/fan_settings.png){class="glboxshadow gl-70-desktop"}

!!! note "Моделі з вбудованими вентиляторами"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-BE9300 (Flint 3)
    - GL-BE6500 (Flint 3e)
    - GL-MT3600BE (Beryl 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-BE3600 (Slate 7)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

## Використання пам’яті {#memory-usage}

Наведіть вказівник миші на графік, щоб переглянути точні значення.

**Примітка**: тут показано пам’ять, доступну системі Linux. Її загальний обсяг менший за фізичний, оскільки частина виділяється підсистемі Wi-Fi або іншим областям завантаження.

![Використання пам’яті](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/memory_usage.png){class="glboxshadow gl-70-desktop"}

## Світлодіодні індикатори {#led}

Натисніть піктограму шестерні, щоб відкрити [завдання за розкладом](scheduled_tasks.md) для світлодіодних індикаторів.

![Керування світлодіодними індикаторами](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/led.png){class="glboxshadow gl-70-desktop"}

## Флешпам’ять {#flash}

Тут показано загальний обсяг флешпам’яті, зокрема використання системою (System used), застосунками (Apps used) і залишок вільної пам’яті (Available).

![Використання флешпам’яті](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/flash.png){class="glboxshadow"}

## Відомості про пристрій {#device-info}

У цьому розділі відображаються основні відомості про пристрій.

Device ID, MAC-адресу пристрою та його S/N додано у прошивці v4.7 і новіших версіях.

![Відомості про пристрій](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/device_info.jpg){class="glboxshadow gl-80-desktop"}

## Зовнішній накопичувач {#external-storage}

Цей розділ доступний починаючи з v4.5. Тут показано загальну й доступну місткість диска USB.

Деякі моделі з прошивкою v4.7 і новішою підтримують перемикання протоколу USB.

![Зовнішній накопичувач](https://static.gl-inet.com/docs/router/en/4/interface_guide/system_overview/external_storage.jpg){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
