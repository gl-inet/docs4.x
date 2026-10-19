# Як захистити RDP через WireGuard під час доступу із зовнішньої мережі {#use-wireguard-to-secure-rdp-from-outside-network}

Вам може знадобитися віддалений доступ до свого ПК із зовнішньої мережі або у зворотному напрямку. Найбезпечніший спосіб — доступ через власний тунель WireGuard. Він забезпечує вищий рівень безпеки, ніж перенаправлення портів і доступ через публічну IP-адресу. Після налаштування тунелю можна використовувати **Remote Desktop App** у Windows для доступу до ПК звідусіль.

## Топологія {#topology}

![Топологія доступу RDP через WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Налаштування власної мережі WireGuard {#setup-your-own-wireguard-network}

Перш ніж використовувати тунель WireGuard для RDP, налаштуйте власні сервер і клієнт WireGuard. Тунель можна налаштувати за допомогою двох маршрутизаторів GL.iNet. Див. [інструкцію зі створення власного домашнього сервера WireGuard із двома маршрутизаторами GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Надання серверу доступу до локальної мережі клієнта {#allow-your-server-access-to-the-client-lan-side}

Щоб забезпечити взаємний доступ із боку сервера та клієнта, спочатку дозвольте серверу доступ до локальної мережі клієнта. Див. [інструкцію з доступу до локальної мережі клієнта з боку сервера](wireguard_server_access_to_client_lan_side.md).

## Надання клієнту доступу до локальної мережі сервера {#allow-your-client-access-to-the-server-lan-side}
Потім увімкніть **Allow Remote LAN Access** на сторінці **VPN Dashboard** як сервера, так і клієнта. Докладніше для клієнта — [тут](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options), для сервера — [тут](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Налаштування доступу до ПК на боці сервера {#setup-the-server-side-pc-become-accessable}

### ПК на боці сервера {#server-side-pc}

Щоб отримати доступ до ПК у локальній мережі сервера з IP-адресою **192.168.29.123**, відкрийте налаштування Windows на цьому ПК і натисніть **Remote Desktop**.

![Налаштування Remote Desktop у Windows](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Увімкніть віддалений робочий стіл.

![Увімкнення Remote Desktop](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Натисніть **Confirm**.

![Підтвердження ввімкнення Remote Desktop](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Запуск застосунку віддаленого доступу на клієнтському ноутбуці {#start-up-remote-app-at-client-laptop}

### Ноутбук на боці клієнта {#client-side-laptop}

Знайдіть **Remote Desktop Connection App**.

![Пошук Remote Desktop Connection App](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Запустіть застосунок і введіть у поле IP-адресу ПК на боці сервера: **192.168.29.123**.

![Введення IP-адреси ПК на боці сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Введіть облікові дані ПК на боці сервера.

![Введення облікових даних ПК](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Після цього ви зможете віддалено керувати ПК на боці сервера.

Для доступу у зворотному напрямку поміняйте ролі серверного ПК і клієнтського ноутбука в наведених кроках.
