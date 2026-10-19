# Підключення до інтернету за допомогою спільного доступу через USB {#connect-to-the-internet-via-usb-tethering}

Спільний доступ до інтернету зі смартфона для маршрутизатора за допомогою кабелю USB називається Tethering. Модем Host-less також працює в режимі Tethering під час налаштування.

**Примітка:** Деякі мобільні оператори обмежують спільний доступ до інтернету або стягують за нього додаткову плату. Рекомендуємо уточнити умови у вашого оператора.

## Налаштування {#setup}

=== "iPhone"

    1. Підключіть iPhone до порту USB маршрутизатора кабелем USB. З’явиться системне діалогове вікно із запитом, чи довіряти пристрою. Натисніть **Trust**, щоб продовжити.

        ![Підтвердження довіри до пристрою на iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. На iPhone перейдіть до **Settings** -> **Personal Hotspot**. Увімкніть **Allow Others to Join**.

        ![Увімкнення персональної точки доступу iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Підключіть комп’ютер або інший телефон до маршрутизатора, увійдіть у вебпанель адміністрування маршрутизатора, перейдіть до розділу **INTERNET** -> **Tethering** і натисніть **Connect**.

        ![Підключення до інтернету через iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connect.png){class="glboxshadow"}

        Якщо потрібно змінити додаткові параметри, зокрема TTL, HL або MTU, натисніть **Advanced**, налаштуйте їх і натисніть **Connect**.

        ![Додаткові налаштування з’єднання з iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_advanced.png){class="glboxshadow"}

        Почнеться встановлення з’єднання.

        ![Установлення з’єднання з iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Після підключення стан персональної точки доступу (наприклад, кількість підключених пристроїв) відображатиметься в рядку стану вгорі екрана телефона.

        ![Стан персональної точки доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        У вебпанелі адміністрування також відображатиметься стан з’єднання Tethering.

        ![Успішне з’єднання Tethering з iPhone](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Підключіть телефон Android до порту USB маршрутизатора кабелем USB. Може з’явитися системне діалогове вікно з параметрами USB. Якщо з’явиться запит, виберіть **USB Tethering** або **File Transfer**.

        ![Вибір режиму USB на Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. На телефоні перейдіть до **Settings** -> **Network & Internet** -> **Personal Hotspot**. Увімкніть **Personal Hotspot** або **USB Tethering**.

        (Кроки ввімкнення USB Tethering відрізняються залежно від виробника. Знайдіть потрібний пункт у налаштуваннях пристрою та за потреби зверніться до служби підтримки виробника.)

        ![Персональна точка доступу Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Підключіть комп’ютер або інший телефон до маршрутизатора, увійдіть у вебпанель адміністрування маршрутизатора, перейдіть до розділу **INTERNET** -> **Tethering** і натисніть **Connect**.

        ![Підключення до інтернету через Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connect.png){class="glboxshadow"}

        Якщо потрібно змінити додаткові параметри, зокрема TTL, HL або MTU, натисніть **Advanced**, налаштуйте їх і натисніть **Connect**.

        ![Додаткові налаштування з’єднання з Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_advanced.png){class="glboxshadow"}

        Почнеться встановлення з’єднання.

        ![Установлення з’єднання з Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Після підключення стан персональної точки доступу (наприклад, кількість підключених пристроїв) відображатиметься в рядку стану вгорі екрана телефона.

        У вебпанелі адміністрування також відображатиметься стан з’єднання Tethering.

        ![Успішне з’єднання Tethering з Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connected.png){class="glboxshadow"}

    Офіційні інструкції Android наведено в статті [Спільний доступ до мобільного з’єднання через точку доступу або Tethering на Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}.

## Попередження {#warning}

Якщо доступу до інтернету немає, з’явиться відповідне попередження:

**"The interface is connected, but the Internet can't be accessed."**

Способи усунення:

1. Перевірте, чи має смартфон доступ до інтернету.

2. Відкрийте сторінку [Multi-WAN](multi-wan.md), щоб визначити, чи є доступ до інтернету.

## Усунення несправностей {#troubleshooting}

Якщо з’єднання не встановлюється, спробуйте такі дії:

- Використовуйте оригінальний блок живлення маршрутизатора.
- Від’єднайте та знову підключіть кабель USB.
- Спробуйте інший кабель USB. Переконайтеся, що він підтримує передавання даних, а не лише заряджання.
- Кілька разів вимкніть і знову ввімкніть "USB Tethering" (для телефона Android).
- Кілька разів вимкніть і знову ввімкніть "Allow Others to Join" (для iPhone).
- Перезавантажте смартфон і спробуйте знову.

---

Пов’язані статті

- [Сторінка інтернету](internet.md)
- [Як установити пріоритет кожного способу доступу до інтернету?](multi-wan.md)
- [Як налаштувати балансування навантаження за одночасного використання кількох способів доступу до інтернету?](multi-wan.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
