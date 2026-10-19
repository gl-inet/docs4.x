# Як підключитися до Surfshark із виділеною IP-адресою на маршрутизаторах GL.iNet? {#how-to-connect-to-surfshark-with-a-dedicated-ip-on-glinet-routers}

У цій статті описано, як налаштувати підключення до Surfshark із виділеною IP-адресою на маршрутизаторах GL.iNet.

Як приклад використано GL-AXT1800.

1. Увійдіть до свого облікового запису Surfshark і виберіть **Dedicated IP**.

    ![Виділена IP-адреса Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/manualdip.jpg){class="glboxshadow"}

2. У розділі **Dedicated IP** натисніть **Settings**.

    ![Налаштування виділеної IP-адреси](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/setting.jpg){class="glboxshadow"}

3. Виберіть протокол (WireGuard або OpenVPN) і завантажте файли конфігурації для ручного підключення.

    ![Вибір протоколу](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/protocol.jpg){class="glboxshadow"}
    
    Для конфігурації WireGuard на сторінці завантаження відображаються **Server IP** і **Server Public Key**, як показано нижче.
    
    ![Завантаження конфігурації WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadwg.jpg){class="glboxshadow"}

    Для конфігурації OpenVPN на сторінці завантаження відображаються **Server IP** та облікові дані (**Username & Password**), як показано нижче. Скопіюйте облікові дані для подальшого використання.
    
    ![Завантаження конфігурації OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/surfshark_dedicated_ip/loadovpn.jpg){class="glboxshadow"}

4. Скористайтеся наведеними нижче посиланнями, щоб завантажити файли конфігурації на маршрутизатор GL.iNet. За потреби введіть облікові дані.

    - [Завантаження конфігурації WireGuard](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Завантаження конфігурації OpenVPN](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
