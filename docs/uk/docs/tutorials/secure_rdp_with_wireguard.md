# Захист RDP із зовнішньої мережі за допомогою WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Вам може знадобитися віддалений доступ до свого ПК із зовнішньої мережі або у зворотному напрямку. Безпечний спосіб — доступ через власний тунель WireGuard. Він забезпечує вищий рівень безпеки, ніж перенаправлення портів і прямий доступ до ПК через публічну IP-адресу. Після налаштування тунелю можна використовувати **Windows Remote Desktop** для доступу до ПК звідусіль.

У цій інструкції на прикладі двох маршрутизаторів GL.iNet показано, як захистити Windows RDP через мережу WireGuard.

## Топологія {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Кроки налаштування {#setup-steps}

1. Налаштуйте мережу WireGuard. <span id="setup-your-own-wireguard-network"></span>

    Спочатку налаштуйте власні сервер і клієнт WireGuard за допомогою двох маршрутизаторів GL.iNet. Див. [створення власного сервера WireGuard із двома маршрутизаторами GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Дозвольте серверу WireGuard доступ до локальної мережі клієнта. <span id="allow-your-server-access-to-the-client-lan-side"></span>

    Щоб забезпечити двосторонній доступ між сервером і клієнтом, спочатку дозвольте серверу доступ до локальної мережі клієнта. Див. [доступ до локальної мережі клієнта WireGuard із сервера](wireguard_server_access_to_client_lan_side.md).

    Кроки можуть відрізнятися залежно від версії прошивки.

3. Дозвольте клієнту WireGuard доступ до локальної мережі сервера. <span id="allow-your-client-access-to-the-server-lan-side"></span>

    Цей крок може відрізнятися залежно від версії прошивки. Нижче виберіть версію прошивки маршрутизатора, який налаштовано як клієнт WireGuard.

    ??? note "Для прошивки v4.7 і попередніх версій"

        Увійдіть у клієнт WireGuard і відкрийте **VPN** -> **VPN Dashboard**. Знайдіть **VPN Server** і натисніть значок шестірні праворуч.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        У спливному вікні ввімкніть **Remote Access LAN** і натисніть **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Для прошивки v4.8 і новіших версій"

        Увійдіть у клієнт WireGuard і відкрийте **VPN** -> **WireGuard Server**. Натисніть **Options** у верхньому правому куті.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        У спливному вікні ввімкніть **Allow Remote Access to the LAN Subnet** і натисніть **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Підключіть комп’ютер, до якого потрібен доступ, до сервера VPN і з’ясуйте його локальну IP-адресу.

    У наведеному нижче прикладі IP-адреса ПК на боці сервера — **192.168.29.123**.

5. Налаштуйте доступ до ПК на боці сервера. <span id="setup-the-server-side-pc-become-accessable"></span> <span id="server-side-pc"></span>

    На ПК на боці сервера відкрийте **System Settings** і натисніть **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Увімкніть **Remote Desktop** і натисніть **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Підключіться віддалено з ноутбука на боці клієнта. <span id="start-up-remote-app-at-client-laptop"></span> <span id="client-side-laptop"></span>

    Знайдіть **Remote Desktop Connection** у рядку пошуку.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Запустіть застосунок і введіть IP-адресу ПК на боці сервера, наприклад **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Введіть облікові дані ПК на боці сервера, щоб підключитися.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Після цього ви зможете віддалено керувати ПК на боці сервера.

    Для доступу у зворотному напрямку поміняйте місцями кроки для серверного ПК і клієнтського ноутбука.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
