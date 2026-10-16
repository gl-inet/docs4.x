# Як перевірити наявність публічної IP-адреси? {#how-to-check-if-you-have-a-public-ip-address}

На відміну від приватної IP-адреси, публічна адреса — унікальний числовий ідентифікатор пристрою, підключеного до інтернету. Публічна IP-адреса потрібна для розміщення вебсайту, налаштування сервера VPN або надання онлайн-служб. Зазвичай її надає інтернет-провайдер.

Якщо ви не впевнені, чи маєте публічну IP-адресу, перевірте це одним із таких способів.

**Спосіб 1: зверніться безпосередньо до інтернет-провайдера**

**Спосіб 2: порівняйте IP-адресу в панелі адміністрування маршрутизатора та в інтернеті**

1. Увійдіть у панель адміністрування маршрутизатора.
    * Для маршрутизаторів GL.iNet відкрийте `192.168.8.1` у веббраузері та ввійдіть.
    * Якщо в мережі кілька маршрутизаторів, увійдіть у панель адміністрування основного.
2. Знайдіть IP-адресу WAN у панелі адміністрування, наприклад 42.XXX.XX.
![Пошук IP-адреси WAN](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/locate-ip-address.png){class="glboxshadow"}
3. У веббраузері виконайте пошук `what is my ip`.
![Пошук what is my ip](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/search-what-is-my-ip.png){class="glboxshadow"}

Якщо дві IP-адреси збігаються, ви маєте публічну IP-адресу.
![Порівняння двох IP-адрес](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/two-ip-addresses-match.png){class="glboxshadow"}

Якщо публічної IP-адреси немає, можна скористатися засобом тунелювання для доступу до внутрішньої мережі. Він дає змогу зробити вебсайт, сервер VPN або служби доступними з інтернету навіть без публічної IP-адреси.

---

Пов’язані статті

- [Налаштування сервера WireGuard на маршрутизаторі GL.iNet](../interface_guide/wireguard_server.md)
- [Налаштування сервера OpenVPN на маршрутизаторі GL.iNet](../interface_guide/openvpn_server.md)
- [Перенаправлення портів](../interface_guide/port_forwarding.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
