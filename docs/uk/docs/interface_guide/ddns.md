# Динамічний DNS {#dynamic-dns}

Динамічна служба доменних імен (Dynamic DNS або DDNS) зіставляє доменне ім’я з динамічною IP-адресою мережевого пристрою. За допомогою Dynamic DNS можна отримувати віддалений доступ до маршрутизатора. Для цієї функції потрібна публічна IP-адреса в інтернеті.

## Увімкнення DDNS {#enable-ddns}

У лівому меню вебпанелі адміністрування відкрийте **APPLICATIONS** -> **Dynamic DNS**.

![Динамічний DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Увімкніть **Enable DDNS**, прийміть **Terms of Services & Privacy Policy** та натисніть **Apply**.

![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Натисніть **Security Settings** у нижньому правому куті.

![Налаштування безпеки](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

У спливному вікні перевірте, чи увімкнено потрібний протокол віддаленого доступу. Якщо ні, відкрийте SYSTEM -> Security -> Remote Access Control, щоб його увімкнути.

![Налаштування безпеки](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Увімкніть потрібний протокол віддаленого доступу та натисніть **Apply**.

![Налаштування віддаленого доступу](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Синхронізація записів між DNS-серверами може тривати до 10 хвилин. Через це доступ за доменним ім’ям DDNS може бути недоступний одразу після увімкнення функції або зміни публічної IP-адреси.

**Примітка**: якщо одночасно увімкнено DDNS і клієнт VPN, переконайтеся, що **Services From GL.iNet Use VPN** вимкнено. Цей параметр міститься в [параметрах клієнта VPN](vpn_dashboard_v4.8.md#tunnel-options) на сторінці VPN Dashboard.

## Перевірка роботи DDNS {#check-if-ddns-works}

Перевірте роботу DDNS за допомогою засобу перевірки DDNS або вручну за допомогою команд.

=== "За допомогою засобу перевірки DDNS"

    На сторінці Dynamic DNS натисніть **DDNS Test**.

    ![Перевірка DDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Переконайтеся, що IP-адреса, отримана під час визначення адреси домену DDNS, збігається з WAN IP-адресою маршрутизатора.

    Якщо адреси не збігаються, угорі з’явиться жовте повідомлення про те, що маршрутизатор, можливо, перебуває за NAT і потрібно налаштувати перенаправлення портів на маршрутизаторі вищого рівня.

    ![Повідомлення перевірки DDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "За допомогою команд"

    1. Скористайтеся командою `nslookup`, щоб визначити відповідність між доменним ім’ям та IP-адресою, як показано нижче.

        ![Перевірка домену командою nslookup](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup.png){class="glboxshadow" width="600"}

        **Поради:**

        - Замініть «xxxxxxx.glddns.com» на зображенні вище своїм значенням Host Name.

        - «8.8.8.8» на зображенні вище — це DNS-сервер Google. Використайте його або замініть іншим DNS-сервером і натисніть Enter.

    2. За отриманим результатом визначте, чи успішно зіставлено домен DDNS із публічною IP-адресою.

        - Якщо отримано публічну IP-адресу, наприклад «183.178.10.100» на зображенні вище, домен DDNS успішно зіставлено з публічною IP-адресою.

        - Повідомлення «server can't find xxxxxxx.glddns.com» може означати, що визначити адресу домену не вдалося та домен DDNS не зіставлено з публічною IP-адресою. Перейдіть до наступного кроку для перевірки.

    3. Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **INTERNET**. Знайдіть WAN IP-адресу маршрутизатора в поточному активному інтерфейсі. Порівняйте її з публічною IP-адресою, отриманою вище. Якщо адреси збігаються, DDNS працює; якщо ні — не працює.

## Віддалений доступ через HTTPS {#https-remote-access}

!!! Note

    1. Для віддаленого доступу через HTTPS потрібна **публічна IP-адреса**.

        Перевірте за [цим посиланням](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), чи ваш інтернет-провайдер (ISP) надає публічну IP-адресу.

    2. Якщо маршрутизатор перебуває за NAT, налаштуйте перенаправлення порту **443** на маршрутизаторі вищого рівня для доступу через HTTPS.

Виконайте наведені нижче дії, щоб увімкнути віддалений доступ до маршрутизатора через HTTPS.

1. На сторінці Dynamic DNS увімкніть **Enable DDNS**, прийміть **Terms of Services & Privacy Policy** та натисніть **Apply**.

    ![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. У вебпанелі адміністрування відкрийте SYSTEM -> Security -> Remote Access Control.

    ![Керування віддаленим доступом](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Увімкніть **HTTPS Remote Access** і натисніть **Apply**.

    ![Увімкнення віддаленого доступу через HTTPS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Після увімкнення можна отримувати віддалений доступ до термінала маршрутизатора за допомогою імені хоста DDNS через **HTTPS** (наприклад, `https://xxxxxxx.glddns.com`).

Якщо налаштовано перенаправлення портів, використовуйте адресу `https://xxxxxxx.glddns.com:external_port ` (замініть external_port фактичним номером порту).

**Примітка**: ця функція використовує самопідписані сертифікати. Тому під час доступу до панелі адміністрування маршрутизатора за іменем хоста DDNS через **HTTPS** браузер показує повідомлення **Your connection is not private**, як на зображенні нижче (у прикладі використано порт 8001).

![Віддалений доступ через HTTPS у Chrome для Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Щоб продовжити віддалений доступ через HTTPS, натисніть **Advanced** унизу сторінки.

![Віддалений доступ через HTTPS у Chrome для Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Потім натисніть **Proceed to xxxxxxx.glddns.com**, щоб продовжити.

![Віддалений доступ через HTTPS у Chrome для Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Після цього можна буде відкрити вебпанель адміністрування за іменем хоста DDNS через HTTPS.

![Віддалений доступ через HTTPS у Chrome для Android](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## Віддалений доступ через SSH {#ssh-remote-access}

!!! Note

    1. Для віддаленого доступу через SSH потрібна **публічна IP-адреса**.

        Перевірте за [цим посиланням](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), чи ваш інтернет-провайдер (ISP) надає публічну IP-адресу.

    2. Якщо маршрутизатор перебуває за NAT, налаштуйте перенаправлення порту **22** на маршрутизаторі вищого рівня для доступу через SSH.

Виконайте наведені нижче дії, щоб увімкнути віддалений доступ до маршрутизатора через SSH.

1. На сторінці Dynamic DNS увімкніть **Enable DDNS**, прийміть **Terms of Services & Privacy Policy** та натисніть **Apply**.

    ![Увімкнення DDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. У вебпанелі адміністрування відкрийте SYSTEM -> Security -> Remote Access Control.

    ![Керування віддаленим доступом](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Увімкніть **SSH Remote Access** і натисніть **Apply**.

    ![Увімкнення віддаленого доступу через SSH](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Після увімкнення можна отримувати віддалений доступ до термінала маршрутизатора за допомогою імені хоста DDNS через **SSH** (наприклад, `ssh root@xxxxxxx.glddns.com`).

Якщо налаштовано перенаправлення портів, використовуйте `ssh -p external_port root@xxxxxxx.glddns.com` (замініть external_port фактичним номером порту).

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
