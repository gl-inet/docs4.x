# DNS {#dns}

**Примітка**: Ця сторінка описує прошивку v4.10 та раніші версії.

Якщо на пристрої встановлено іншу версію прошивки, скористайтеся перемикачем нижче, щоб відкрити відповідний посібник.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.10 та раніші версії" markdown="1">

- [Прошивка v4.11](dns_v4.11.md)

</div>

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **NETWORK** -> **DNS**.

Налаштування DNS маршрутизатора визначають, як доменні імена перетворюються на IP-адреси. На цій сторінці можна використовувати DNS-сервери, автоматично отримані від пристроїв вищого рівня, або задати власні та налаштувати пріоритети DNS.

Якщо ви задасте власні DNS-сервери, усі DNS-запити оброблятимуться через них, а не через DNS-сервери, отримані окремими мережевими інтерфейсами. Інакше використовуватимуться налаштування DNS кожного інтерфейсу.

![Налаштування DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_page.png){class="glboxshadow"}

- **DNS Rebinding Attack Protection:** Увімкнення цього параметра може спричинити збій DNS-пошуку в приватній мережі. Якщо мережа має портал авторизації, вимкніть цей параметр.

- **Override DNS Settings for All Clients:** Якщо ввімкнено, маршрутизатор перевизначатиме налаштування незашифрованого DNS для всіх клієнтів.

- **Allow Custom DNS to Override VPN DNS:** Якщо ввімкнено та задано власні DNS-сервери, для пакетів, що передаються через тунель VPN, використовуватимуться ці власні DNS-сервери замість налаштувань DNS з’єднання VPN.

## Налаштування DNS-серверів {#dns-server-settings}

Доступні чотири режими: Automatic, Encrypted DNS, Manual DNS і DNS Proxy.

### Автоматичний DNS {#automatic}

У цьому режимі маршрутизатор автоматично використовує DNS-сервер, наданий пристроєм вищого рівня (наприклад, модемом провайдера або основним маршрутизатором), чи налаштування DNS відповідного мережевого інтерфейсу.

![Автоматичний DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_auto.png){class="glboxshadow"}

### Зашифрований DNS {#encrypted-dns}

Дотримуйтеся наведених нижче інструкцій для вашої версії прошивки.

#### Для прошивки v4.8 та раніших версій {#for-firmware-v48-and-earlier}

Доступні чотири типи шифрування: DNS over TLS, DNSCrypt-Proxy, DNS over HTTPS і Oblivious DNS over HTTPS.

Спочатку виберіть **Encryption Type**. Решта параметрів змінюватимуться залежно від вибору.

![Типи шифрування DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_types.png){class="glboxshadow"}

- **Для DNS over TLS (DoT)** виберіть провайдера DNS: **Control D**, **NextDNS** або **Cloudflare**.

    ![DNS over TLS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_tls.png){class="glboxshadow"}

- **Для решти трьох типів (DNSCrypt-Proxy, DNS over HTTPS і Oblivious DNS over HTTPS)** виберіть щонайменше один DNS-сервер із репозиторію.

    ![DNSCrypt-Proxy](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dnscrypt-proxy.png){class="glboxshadow"}

#### Для прошивок від v4.9 до v4.10 {#for-firmware-v49-to-v410}

Окрім Control D, NextDNS і Cloudflare, у режимі Encrypted DNS тепер доступні й інші провайдери DNS: **Quad9**, **CleanBrowsing**, **AdGuard DNS**, **Google DNS** та **OpenDNS**. За потреби можна також указати сервер зашифрованого DNS вручну.

Спочатку виберіть **DNS Provider**. Решта параметрів змінюватимуться залежно від вибору.

![Провайдери зашифрованого DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_providers.png){class="glboxshadow"}

- Якщо ви вибрали конкретного провайдера DNS (наприклад, NextDNS), виберіть тип шифрування: **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)** або **DNS over QUIC (DoQ)**. DNS over QUIC (DoQ) з’явився у прошивці v4.9 і доступний лише для провайдерів DNS Control D, NextDNS або AdGuard DNS.

    ![Налаштування NextDNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/nextdns.png){class="glboxshadow"}

- Якщо як провайдера DNS вибрано **Manual**, виберіть тип шифрування: **DNS over TLS (DoT)**, **DNS over HTTPS (DoH)**, **DNS over QUIC (DoQ)**, **Oblivious DNS over HTTPS** або **DNSCrypt**.

    ![Вибір типу шифрування вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual1.png){class="glboxshadow"}

    Далі натисніть **Add a Server**, щоб додати щонайменше один DNS-сервер. Можна безпосередньо ввести URL-адресу або запис у форматі stamp для зашифрованого DNS. Список публічних серверів наведено на сторінці [https://dnscrypt.info/public-servers](https://dnscrypt.info/public-servers){target="_blank"}.

    ![Додавання сервера зашифрованого DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/encrypted_manual2.png){class="glboxshadow"}

#### Порівняння типів шифрування {#encryption-type-comparison}

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

### DNS, заданий вручну {#manual-dns}

У цьому режимі можна налаштувати власний DNS-сервер маршрутизатора. Виберіть щонайменше один DNS-сервер із розкривного списку.

![DNS, заданий вручну](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/manual_dns.png){class="glboxshadow"}

### Проксі DNS {#dns-proxy}

У цьому режимі маршрутизатор спрямовуватиме всі DNS-запити з LAN на вказану вами адресу проксі-сервера (наприклад, 8.8.8.8#53). Це може бути корисно, якщо в мережі працює інший DNS-сервер або Pi-hole.

![Проксі DNS](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/dns_proxy.png){class="glboxshadow"}

## Редагування правил для хостів {#edit-hosts}

Натисніть кнопку **Edit Hosts** угорі праворуч, щоб налаштувати статичні правила для хостів.

![Кнопка редагування правил для хостів](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts1.png){class="glboxshadow"}

Під час оброблення запитів від підключених клієнтів маршрутизатор надає цим правилам пріоритет.

![Статичні правила для хостів](https://static.gl-inet.com/docs/router/en/4/interface_guide/dns/edit_hosts2.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
