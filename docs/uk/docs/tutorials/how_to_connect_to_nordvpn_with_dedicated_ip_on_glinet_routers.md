# Як підключитися до NordVPN із виділеною IP-адресою на маршрутизаторах GL.iNet? {#how-to-connect-to-nordvpn-with-a-dedicated-ip-on-glinet-routers}

У цій статті описано налаштування з’єднання NordVPN із виділеною IP-адресою на маршрутизаторах GL.iNet.

У прикладі використовується GL-AXT1800.

1. Увійдіть у Nord Account і перевірте відомості про виділену IP-адресу. У цьому прикладі призначена IP-адреса — **193.32.211.142**, а сервер — **United Kingdom #1625**.

    ![Відомості про виділену IP-адресу NordVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/dedicated_ip_info.png){class="glboxshadow"}

2. Перейдіть на [https://nordvpn.com/ovpn/](https://nordvpn.com/ovpn/){target="_blank"} і знайдіть файл конфігурації для **United Kingdom #1625**. Завантажте конфігурацію UDP або TCP.

    ![Завантаження конфігурації виділеної IP-адреси NordVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/download_dedicated_ip_config.png){class="glboxshadow"}

3. Поверніться до Nord Account, перейдіть до **Manual Setup** і натисніть **Set up NordVPN Manually**, щоб отримати **облікові дані служби**.

    ![Ручне налаштування NordVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup.png){class="glboxshadow"}

    ![Облікові дані служби NordVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/nordvpn_manual_setup_service_credential.png){class="glboxshadow"}

4. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **VPN** > **OpenVPN Client**. Створіть нову групу, завантажте файл конфігурації з кроку 2 та введіть облікові дані служби з кроку 3.

    ![Налаштування NordVPN на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/set_up_nordvpn_on_glinet_router.png){class="glboxshadow"}

    Як показано вище, виявлено дійсний файл конфігурації. Уведіть облікові дані служби NordVPN.

5. Натисніть значок із трьома крапками праворуч, щоб підключитися. Також можна відкрити **VPN Dashboard**, вибрати файл конфігурації та натиснути **Apply** для встановлення з’єднання.

6. Після підключення перевірте публічну IP-адресу [тут](https://whatismyipaddress.com/){target="_blank"} та переконайтеся, що вона збігається з виділеною IP-адресою NordVPN.

    ![Перевірка IP-адреси після підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_nordvpn_dedicated_ip/check_ip_after_connected.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
