# Як спрямувати DNS-трафік AdGuard Home в обхід VPN-тунелю {#how-to-make-adguard-home-dns-bypass-the-vpn-tunnel}

Зазвичай VPN і AdGuard Home можуть працювати одночасно на маршрутизаторах GL.iNet. Проблем не виникає, якщо AdGuard Home не налаштовано на обробку DNS-запитів.

Однак якщо AdGuard Home керує всім DNS-трафіком і пересилає запити на **публічні сервери DNS вищого рівня**, увімкнення VPN призведе до збоїв розпізнавання DNS.

![Налаштування AdGuard Home](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguardhome.jpg){class="glboxshadow"}
<br><small>(AdGuard Home увімкнено та обробляє DNS-запити)</small>

![Налаштування серверів DNS AdGuard Home](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/upstream_dns.png){class="glboxshadow"}
<br><small>(Налаштування серверів DNS вищого рівня в AdGuard Home)</small>

За замовчуванням увесь вихідний трафік проходить через VPN-тунель. Через це DNS-трафік AdGuard Home до серверів вищого рівня також спрямовується у VPN і не може досягти публічних серверів DNS. Як наслідок, усі підключені клієнти не можуть розпізнавати доменні імена.

Щоб AdGuard Home працював із активним VPN, можна додати статичний маршрут у LuCI та спрямувати трафік до серверів DNS вищого рівня через звичайний шлюз WAN в обхід VPN-тунелю. Виконайте наведені нижче кроки.

1. Увійдіть до вебпанелі адміністрування маршрутизатора та перейдіть до **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**.

    ![Відкриття LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci1.png){class="glboxshadow"}

    Увійдіть із тим самим паролем адміністратора.

    ![Вхід до LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/luci2.png){class="glboxshadow"}

2. У LuCI перейдіть до **Network** -> **Routing** і натисніть **Add**.

    ![Маршрутизація LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing1.png){class="glboxshadow"}

3. Створіть новий статичний маршрут до адрес серверів DNS вищого рівня.

    ![Створення статичного маршруту](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/routing2.png){class="glboxshadow"}

    - **Interface**: виберіть фізичний інтерфейс WAN **wan**.
    
    - **Route type**: залиште значення за замовчуванням.
    
    - **Target**: `[Your Public Upstream DNS Server]/32`
    
        За допомогою `nslookup` можна перевірити фактичну IP-адресу публічного сервера DNS вищого рівня.
    
    - **Gateway**: `[Your WAN Upstream Gateway IP]`
    
        Зазвичай це IP-адреса модема або шлюзу інтернет-провайдера, наприклад `192.168.0.1`. Її можна знайти на сторінці стану інтернет-підключення маршрутизатора.

    Цей маршрут спрямовує запити AdGuard Home до серверів DNS вищого рівня безпосередньо через з’єднання WAN в обхід VPN-тунелю.

4. Збережіть і застосуйте налаштування. Після цього AdGuard Home знову нормально розпізнаватиме DNS-імена.

5. Перевірте сервери DNS вищого рівня.

    Перевірити сервери DNS вищого рівня можна безпосередньо в інтерфейсі AdGuard Home.
    
    У вебпанелі адміністрування маршрутизатора перейдіть до **APPLICATIONS** -> **AdGuard Home** і натисніть **Settings Page**, щоб відкрити панель керування AdGuard Home.

    ![Налаштування AdGuard Home](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/adguard_settings.png){class="glboxshadow"}

    У панелі керування AdGuard Home перейдіть до **Settings** -> **DNS settings** -> **Upstream DNS servers** і натисніть **Test upstreams**. Результати з’являться праворуч.

    ![Перевірка серверів DNS вищого рівня](https://static.gl-inet.com/docs/router/en/4/tutorials/make_adguard_home_dns_bypass_vpn/test_upstreams.png){class="glboxshadow"}

---

**Порада:** Якщо у вас кілька серверів DNS і серед їхніх адрес є як IP-адреси, так і доменні імена, можна відокремити DNS-трафік AdGuard від DNS-трафіку VPN. Це може бути простіше, ніж використання статичного маршруту.

Підключіться до маршрутизатора GL.iNet через SSH і виконайте наведені нижче команди, щоб AdGuard Home надсилав DNS-запити лише через WAN.

```
sed -i 's/explict_vpn/nonevpn/g' /etc/init.d/adguardhome
/etc/init.d/adguardhome restart

# To restore:
cp -r /rom/etc/init.d/adguardhome /etc/init.d/adguardhome
/etc/init.d/adguardhome restart
```

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
