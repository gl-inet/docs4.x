# Два дротові з’єднання Ethernet WAN через адаптер Ethernet–USB-A {#configure-dual-wired-ethernet-wan-via-an-ethernet-to-usb-a-adapter}

На маршрутизаторі з одним портом WAN можна налаштувати два дротові з’єднання Ethernet WAN за допомогою адаптера Ethernet–USB-A.

Маршрутизатори GL.iNet підтримують поширені адаптери Ethernet–USB-A. Вони перетворюють дротове Ethernet-підключення від маршрутизатора провайдера на з’єднання через USB і надають додатковий дротовий доступ поряд із портом WAN.

## Топологія {#topology}

![Топологія](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/adaptor.png){class="glboxshadow"}

## Налаштування {#setup-steps}

1. Підключіть адаптер Ethernet–USB-A до порту USB маршрутизатора GL.iNet, а інший кінець — до маршрутизатора провайдера.

2. Встановіть драйвер USB.

    У вебпанелі адміністрування відкрийте **Application** -> **Plug-ins** і встановіть мережевий драйвер USB для свого адаптера.

    Наприклад, для адаптера Realtek встановіть **kmod-usb-net-rtl8152**.

    ![Драйвер USB у плагінах](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/plugins_usb.png){class="glboxshadow"}

    Дочекайтеся завершення встановлення.

    ![Встановлення завершено](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/suceeded.png){class="glboxshadow"}

3. Підключіться через USB Tethering.

    Після встановлення драйвера відкрийте **INTERNET** -> **Tethering**.

    USB-з’єднання буде виявлено, і ви зможете підключитися до маршрутизатора провайдера.

    ![USB-з’єднання виявлено](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/detected.png){class="glboxshadow"}

    Натисніть **Connect** і зачекайте хвилину. Зелена крапка та відомості про IP-адресу означають успішне підключення через USB Tethering.

    ![З’єднання Tethering встановлено](https://static.gl-inet.com/docs/router/en/4/tutorials/multiwan_wire/tether.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
