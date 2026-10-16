# Доступ із клієнта до пристроїв LAN сервера OpenVPN за доменними іменами {#how-to-access-openvpn-server-lan-devices-from-the-client-via-domain-names}

У цій інструкції описано доступ клієнта до домашніх пристроїв, наприклад NAS або IP-камер, у LAN сервера OpenVPN за доменними іменами.

## Топологія {#topology}

Як показано нижче, комп’ютер у LAN клієнта може відкривати NAS, IP-камери та інші пристрої в LAN сервера OpenVPN за відповідними доменними іменами.

![Топологія](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/topology_be9300_be3600.png){class="glboxshadow"}

## Налаштування {#setup-steps}

### 1. Зміна Hosts на сервері — за потреби {#1-edit-hosts-on-server-optional}

Цей крок потрібний, якщо сервер VPN не може належним чином визначати адреси локальних доменів. Якщо ви не впевнені, пропустіть його.

У вебпанелі адміністрування маршрутизатора-сервера VPN відкрийте **NETWORK** -> **DNS** -> **Edit Hosts**.

![Редагування Hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_hosts.png){class="glboxshadow"}

Введіть IP-адреси та доменні імена потрібних домашніх пристроїв і натисніть **Apply**.

![IP-адреси й доменні імена](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/input_ip_domain.png){class="glboxshadow gl-80-desktop"}

### 2. Віддалений доступ до LAN на сервері {#2-allow-remote-access-lan-on-server}

У вебпанелі сервера відкрийте **VPN** -> **OpenVPN Server** і натисніть **Options** у верхньому правому куті.

![Параметри сервера OpenVPN у 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_options.png){class="glboxshadow"}

Увімкніть **Allow Remote Access the LAN Subnet** і натисніть **Apply**.

![Віддалений доступ до LAN у 4.8](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/allow_remote_access_lan.png){class="glboxshadow"}

Після увімкнення маршрутизатор і пристрої LAN будуть доступні віддалено через VPN.

### 3. Експорт конфігурації VPN {#3-export-vpn-configuration}

У вебпанелі сервера відкрийте **VPN** -> **OpenVPN Server** -> **Configuration** і натисніть **Export Client Configuration** унизу.

![Експорт конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export1.png){class="glboxshadow"}

У спливному вікні натисніть **Export**.

**Примітка**: якщо публічна IP-адреса сервера динамічна, перед експортом клієнтської конфігурації відкрийте **APPLICATIONS** -> **Dynamic DNS** та увімкніть **DDNS**.

![Експорт конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/export2.png){class="glboxshadow"}

Буде отримано файл **.ovpn**, як показано нижче.

![Завантажений файл](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/download.png){class="glboxshadow"}

Якщо сервер використовує прошивку v4.8 або новішу, змінювати конфігурацію не потрібно. Перейдіть до наступного кроку.

У прошивці v4.7 і попередніх версіях відкрийте файл і додайте наведений нижче рядок, щоб задати DNS-сервером IP-адресу тунелю сервера OpenVPN. Потім збережіть зміни.

`dns server 1 address 10.8.0.1`

![Зміна конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/edit_config.png){class="glboxshadow"}

Порада: підмережу IPv4 тунелю сервера OpenVPN наведено на вкладці **Configuration** сторінки OpenVPN Server. Вона залежить від прошивки, тому перевірте IP-адресу тунелю свого сервера.

![IP-підмережа тунелю OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_tunnel_ip.png){class="glboxshadow"}

### 4. Запуск сервера VPN {#4-enable-vpn-server}

На сторінці **OpenVPN Server** натисніть **Start** у верхньому правому куті.

![Запуск сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnserver_start.png){class="glboxshadow"}

### 5. Завантаження конфігурації VPN {#5-upload-vpn-configuration}

Увійдіть у вебпанель адміністрування маршрутизатора-клієнта VPN, відкрийте **VPN** -> **OpenVPN Client** і натисніть **Add Manually**.

![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload1.png){class="glboxshadow"}

Задайте назву групи та завантажте файл конфігурації.

![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload2.png){class="glboxshadow"}

Після успішного завантаження натисніть **Apply**.

![Застосування](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload3.png){class="glboxshadow"}

Файл конфігурації з’явиться у списку.

![Конфігурацію застосовано](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_upload4.png){class="glboxshadow"}

### 6. Підключення клієнта VPN {#6-start-vpn-client-connection}

Натисніть піктограму з трьома крапками, щоб встановити з’єднання VPN.

![Запуск клієнта VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_start.png){class="glboxshadow"}

Коли сіра крапка стане зеленою, клієнт OpenVPN успішно підключився до сервера.

![Клієнт OpenVPN підключено](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ovpnclient_connected.png){class="glboxshadow"}

Тепер комп’ютер у LAN клієнта може відкривати домашні пристрої, наприклад NAS, у LAN сервера за їхніми доменними іменами.

![Перевірка за доменним ім’ям](https://static.gl-inet.com/docs/router/en/4/tutorials/access_ovpnserver_lan_via_domain_names/ping_test.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
