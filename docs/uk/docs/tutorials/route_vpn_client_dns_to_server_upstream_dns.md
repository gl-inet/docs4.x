# Як спрямувати DNS-запити VPN-клієнта до DNS-сервера у мережі вище VPN-сервера? {#how-to-route-vpn-client-dns-queries-to-the-vpn-servers-upstream-dns}

У цьому посібнику описано, як переспрямувати всі DNS-запити VPN-клієнтів до власного DNS-сервера в локальній мережі основного маршрутизатора, розташованого у мережі вище VPN-сервера.

## Топологія {#topology}

У цьому посібнику використано **Flint 3 (GL-BE9300)** і **Slate 7 (GL-BE3600)** як приклади.

Flint 3 працює як VPN-сервер, у мережі вище якого розташований основний маршрутизатор, а Slate 7 — як VPN-клієнт, що підключається до Flint 3.

Коли між VPN-сервером і клієнтом установлено VPN-тунель, за замовчуванням DNS-запити VPN-клієнта спочатку надходять до VPN-сервера, потім передаються основному маршрутизатору й зрештою обробляються DNS-серверами, призначеними інтернет-провайдером і налаштованими для WAN-з’єднання основного маршрутизатора.

![Топологія 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Якщо ж у мережі основного маршрутизатора розгорнуто власний DNS-сервер з IP-адресою `192.168.1.13`, потрібні додаткові налаштування, щоб спрямувати DNS-запити до цього сервера.

![Топологія 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Налаштування {#setup}

1. Увійдіть до вебпанелі адміністрування Flint 3 і перейдіть до **NETWORK** -> **DNS**. Установіть режим DNS-сервера **Manual DNS** і введіть IP-адресу свого DNS-сервера.

    ![Ручне налаштування DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Перейдіть до **VPN** -> **WireGuard Server** -> вкладка **Configuration** і запишіть IPv4-адресу. Зазвичай це `10.0.0.1/24` або `10.1.0.1/24`, залежно від моделі та версії прошивки.

    ![IP-адреса сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Перейдіть на вкладку **Profiles**, додайте конфігурацію клієнта та експортуйте профіль для Slate 7.

    ![Додавання профілю](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Відкрийте профіль і переконайтеся, що в полі DNS указано IP-адресу VPN-сервера, отриману на кроці 2.

    Щоб уникнути помилок розпізнавання DNS, видаліть «64.6.64.6», якщо ця адреса є у профілі, і збережіть зміни.

    ![Редагування конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. У вебпанелі адміністрування Flint 3 натисніть кнопку **Start** у верхній частині сторінки **WireGuard Server**, щоб запустити сервер.

    ![Запуск сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Увійдіть до вебпанелі адміністрування Slate 7 і перейдіть до **VPN** -> **WireGuard Client**.

    Натисніть **Add Manually** і завантажте відредагований профіль.

    ![Завантаження конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Натисніть значок із трьома крапками, щоб запустити VPN-з’єднання. Зелений індикатор стану означає, що VPN-з’єднання встановлено успішно.

    ![Запуск клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## Перевірка розпізнавання DNS {#verify-dns-resolution}

Виконайте наведену нижче команду, щоб перехопити DNS-трафік на VPN-клієнті. Результат покаже, що весь DNS-трафік VPN-клієнта надходить до VPN-сервера (у цьому прикладі — `10.0.0.1`).

![DNS-трафік клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Виконайте наведену нижче команду, щоб перехопити DNS-трафік на VPN-сервері. Результат покаже, що весь DNS-трафік VPN-клієнта зрештою надходить до власного DNS-сервера (у цьому прикладі — `192.168.1.13`).

![DNS-трафік сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.











