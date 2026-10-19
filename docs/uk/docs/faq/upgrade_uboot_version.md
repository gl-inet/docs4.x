# Оновлення версії U-Boot {#upgrade-u-boot-version}

## Попередження {#warning}

**Оновлення U-Boot дуже небезпечне та зазвичай не рекомендується. Якщо воно завершиться невдало, пристрій стане непрацездатним і відновити його буде неможливо. Виконуйте цю дію лише за потреби або за вказівкою служби підтримки GL.iNet**.

**НЕ вимикайте живлення під час оновлення. Це може спричинити збій оновлення та зробити пристрій непрацездатним**.

## Підготовка {#preparation}

- Комп’ютер із портом Ethernet. Якщо такого порту немає, підготуйте додатковий адаптер USB Ethernet.
- Кабель Ethernet.
- Завантажте файл U-Boot за вказівками служби підтримки GL-iNet. Переконайтеся, що файл правильний. Якщо ви не знаєте, як його отримати, напишіть на support@gl-inet.com.

## Дії для оновлення {#upgrade-steps}

Виконайте наведені нижче дії, щоб відкрити сторінку оновлення U-Boot.

1. Відключіть живлення маршрутизатора та підключіть комп’ютер до його **порту Ethernet LAN**. **ОБОВ’ЯЗКОВО** залиште всі інші порти **непідключеними**.

    !!! note

        На деяких моделях окремі порти LAN можна перемкнути на WAN. Не використовуйте такий порт. Наприклад, на GL-MT6000 (Flint 2) не використовуйте LAN 1. Підключіться до LAN 2, LAN 3 або LAN 4.

2. Натисніть і утримуйте Reset та одночасно увімкніть маршрутизатор. Якщо кнопки живлення немає, він автоматично увімкнеться після підключення живлення.

    Дочекайтеся кількох повторень послідовності блимання індикатора. Відпустіть кнопку після зміни цієї послідовності.

3. Вручну задайте комп’ютеру IP-адресу **192.168.1.2**. Інструкції для різних операційних систем наведено нижче.

    ??? "Windows 7 / Windows 10"

        1. Відкрийте **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Натисніть **Local Area Connection** правою кнопкою миші та виберіть **Properties**.

        3. Виберіть **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Вручну задайте **IP address** `192.168.1.2`.

        5. Задайте **Subnet mask** `255.255.255.0`.

            ![Властивості IPv4](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/set_ip.jpg){class="glboxshadow"}

        6. Натисніть **OK**.

    ??? "Windows 11"

        1. Відкрийте Settings.

        2. Натисніть **Network & Internet**.

        3. Відкрийте вкладку **Ethernet**.

            ![Параметри Ethernet у Windows 11](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windwos11_ethernet.png){class="glboxshadow"}

        4. У розділі «IP assignment» натисніть **Edit**.

            ![Зміна IP-параметрів Ethernet у Windows 11](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Виберіть **Manual**.

            ![Зміна IP-параметрів Ethernet у Windows 11](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Увімкніть перемикач **IPv4 toggle**.

        7. Задайте статичну **IP address** **192.168.1.2**.

            ![Зміна IP-параметрів Ethernet у Windows 11](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Задайте **Subnet mask** **255.255.255.0**.

        9. Натисніть **Save**.

    ??? "macOS"

        1. Натисніть піктограму **Apple** у верхньому лівому куті та виберіть **System Preferences**.

            ![Системні налаштування macOS](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences.png){class="glboxshadow"}

        2. Натисніть **Network**.

            ![Мережеві налаштування macOS](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_system_preferences_network.png){class="glboxshadow"}

        3. Виберіть **Ethernet** ліворуч, відкрийте список біля **Configure IPv4** і виберіть **Manually**. Якщо використовується адаптер USB Ethernet, замість Ethernet може відображатися назва адаптера.

            ![Ручне налаштування IP у macOS](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_1.png){class="glboxshadow"}

        4. Задайте **IPv4 Address** `192.168.1.2`, **Subnet Mask** `255.255.255.0` і **Router** `192.168.1.1`, а потім натисніть Apply у нижньому правому куті.

            ![Ручне налаштування IP у macOS](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/macos_ip_manually_2.png){class="glboxshadow"}

4. **Використовуйте Google Chrome або Microsoft Edge, щоб відкрити `http://192.168.1.1/uboot.html`**. Введіть повний URL, щоб кешовані підказки не спрямували вас на неправильну адресу.

    **НЕ використовуйте Mozilla Firefox, оскільки це може зробити маршрутизатор непрацездатним.**

    ![Сторінка оновлення U-Boot для gl-ar750s](https://static.gl-inet.com/docs/router/en/4/faq/upgrade_uboot_version/u-boot_update.png){class="glboxshadow" width="700"}

5. Натисніть **Choose file** і виберіть завантажений файл U-Boot.

6. Натисніть **Update U-Boot**. НЕ вимикайте живлення під час оновлення. Процес триває кілька хвилин.

7. Після успішного оновлення маршрутизатор перезавантажиться. Поверніть попередні IP-параметри, змінені на кроці 3, та спробуйте відкрити вебпанель адміністрування за **192.168.8.1**. Якщо панель доступна, маршрутизатор перезавантажився.

    **Примітка:** для доступу може знадобитися режим інкогніто або видалення кешу й файлів cookie браузера.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
