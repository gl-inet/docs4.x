# DNS {#dns}

**Примітка**: Описані на цій сторінці можливості вперше з’явилися у прошивці v4.11.

Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.11" markdown="1">

- [Прошивка v4.10 та раніші версії](dns.md)

</div>

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **DNS**.

Налаштування DNS маршрутизатора визначають, як доменні імена перетворюються на IP-адреси. На цій сторінці можна використовувати DNS-сервери, автоматично отримані від пристроїв вищого рівня, або задати власні. Також можна налаштувати параметри DNS і змінити статичні правила для хостів.

![Налаштування DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_v4.11.png){class="glboxshadow"}

За замовчуванням DNS-запити для трафіку, що відповідає політиці VPN, використовують DNS-сервери, надані тунелем VPN. DNS-запити для трафіку поза VPN використовують DNS-сервери, отримані від активного інтерфейсу WAN. Якщо ви задасте власні DNS-сервери, їх можна застосувати до тунелів VPN, самого маршрутизатора або до обох. Коли ці параметри ввімкнено, DNS-запити в межах вибраної області оброблятимуться через указані сервери замість серверів, отриманих відповідними мережевими інтерфейсами. Якщо власні DNS-сервери не задано, маршрутизатор використовує сервери, отримані відповідними мережевими інтерфейсами.

## DNS для WAN {#wan-dns}

Розділ WAN DNS показує DNS-сервери, отримані від кожного каналу WAN: Ethernet, ретранслятора, спільного доступу до інтернету через USB та стільникового з’єднання.

![Список DNS-серверів WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_1.png){class="glboxshadow" width=550}

Якщо канал WAN активний, адреси його DNS-серверів відображаються праворуч, як показано нижче.

![DNS-сервери активного каналу WAN](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/wan_dns_2.png){class="glboxshadow" width=550}

## DNS для VPN {#vpn-dns}

Розділ VPN DNS показує DNS-сервери, отримані від кожного активного тунелю VPN.

![Список DNS-серверів VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_1.png){class="glboxshadow" width=550}

Якщо тунель VPN працює, DNS-запити трафіку VPN використовують налаштування VPN DNS, як показано нижче.

![DNS-сервери активного тунелю VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/vpn_dns_2.png){class="glboxshadow" width=550}

## DNS, заданий вручну {#manual-dns}

Manual DNS підтримує два типи налаштувань: **Static DNS** і **Encrypted DNS**.

![DNS, заданий вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/manual_dns.png){class="glboxshadow" width=550}

- **Apply Manual DNS to VPN tunnels**: Якщо ввімкнено, для пакетів, що передаються через тунель VPN, використовуватимуться власні налаштування Manual DNS замість налаштувань DNS мережі VPN.

- **Apply Manual DNS to Router Itself**: Цей параметр увімкнено за замовчуванням. Коли він увімкнений, вбудовані служби маршрутизатора (наприклад, GoodCloud) використовують власні налаштування DNS, задані вручну.

### Статичний DNS {#static-dns}

Static DNS дає змогу вручну ввести IPv4- або IPv6-адреси DNS-серверів. Щоб налаштувати DNS-сервери маршрутизатора, введіть адреси безпосередньо або виберіть готові публічні DNS-сервери з розкривного списку.

![Налаштування статичного DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_1.png){class="glboxshadow" width=550}

Можна ввести до чотирьох адрес DNS-серверів. Натисніть **Apply**, щоб зберегти зміни.

![Введення адрес DNS-серверів](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/static_dns_2.png){class="glboxshadow" width=550}

### Зашифрований DNS {#encrypted-dns}

Режим Encrypted DNS підтримує кількох провайдерів DNS: Control D, NextDNS, Quad9, CleanBrowsing, Cloudflare, AdGuard DNS, Google DNS та OpenDNS. За потреби можна також указати сервер зашифрованого DNS вручну.

Спочатку виберіть DNS Provider. Решта параметрів змінюватимуться залежно від вибору.

![Провайдери зашифрованого DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_provider.png){class="glboxshadow"}

- Якщо ви вибрали конкретного провайдера DNS (наприклад, NextDNS), виберіть тип шифрування: DNS over TLS (DoT), DNS over HTTPS (DoH) або DNS over QUIC (DoQ). DNS over QUIC (DoQ) з’явився у прошивці v4.9 і доступний лише для провайдерів DNS Control D, NextDNS або AdGuard DNS.

    ![Налаштування NextDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/nextdns.png){class="glboxshadow" width=550}

- Якщо як провайдера DNS вибрано Manual, виберіть тип шифрування: DNS over TLS (DoT), DNS over HTTPS (DoH), DNS over QUIC (DoQ), Oblivious DNS over HTTPS або DNSCrypt.

    ![Вибір типу шифрування вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_1.png){class="glboxshadow"}

    Далі натисніть **Add a Server**, щоб додати щонайменше один DNS-сервер. Можна безпосередньо ввести URL-адресу або запис у форматі stamp для зашифрованого DNS. Список публічних серверів наведено на сторінці [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![Додавання сервера зашифрованого DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/encrypted_manual_2.png){class="glboxshadow" width=550}

!!! tip "Порівняння типів шифрування"

    1. **DNS over TLS (DoT)**

        Шифрує DNS-запити через окремий порт TLS. Відокремлює DNS-трафік від звичайного вебтрафіку, тому оператори мережі можуть легко його ідентифікувати.

    2. **DNS over HTTPS (DoH)**

        Передає дані DNS усередині стандартного HTTPS-трафіку. Поєднує DNS-запити зі звичайним вебтрафіком, забезпечуючи високий рівень конфіденційності та обходячи просту фільтрацію трафіку.

    3. **DNS over QUIC (DoQ)**

        Інкапсулює DNS у протокол QUIC. Забезпечує низьку затримку, швидке відновлення з’єднання та стабільну роботу в нестабільних мережах.

    4. **Oblivious DNS over HTTPS (ODoH)**

        Удосконалена версія DoH. Відокремлює IP-адресу користувача від DNS-запитів, щоб ані сервер, ані мережевий провайдер не могли відстежувати відвідувані вебсторінки.

    5. **DNSCrypt**

        Зрілий протокол шифрування DNS. Автентифікує та шифрує DNS-трафік, зосереджуючись на захисті від підміни та сумісності із застарілими мережевими середовищами.

## Параметри DNS {#dns-options}

Натисніть **Options** угорі праворуч, щоб налаштувати додаткові параметри DNS.

![Кнопка параметрів DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_1.png){class="glboxshadow"}

Увімкніть або вимкніть ці параметри за потреби.

![Додаткові параметри DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/dns_options_2.png){class="glboxshadow" width=550}

- **DNS Rebinding Attack Protection**: Увімкнення цього параметра може спричинити збій DNS-пошуку в приватній мережі. Якщо мережа має портал авторизації, вимкніть цей параметр.

- **Override DNS Settings of All Clients**: Якщо ввімкнено, маршрутизатор перевизначатиме налаштування незашифрованого DNS для всіх клієнтів.

## Редагування правил для хостів {#edit-hosts}

Натисніть кнопку **Edit Hosts** угорі праворуч, щоб налаштувати статичні правила для хостів.

![Кнопка редагування правил для хостів](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_host_1.png){class="glboxshadow"}

Під час оброблення запитів від підключених клієнтів маршрутизатор надає цим правилам пріоритет.

![Статичні правила для хостів](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns_v4.11/edit_hosts_2.png){class="glboxshadow" width=550}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
