# Як знайти всі MAC-адреси пристрою? {#how-can-i-find-all-mac-addresses-of-my-device}

## Сценарій використання {#usage-scenario}

Кожен мережевий інтерфейс пристрою GL.iNet має власну MAC-адресу, зокрема WAN 1, WAN 2, порти LAN, Wi-Fi 2.4G та Wi-Fi 5G.

У деяких готелях, кемпінгах або навчальних закладах адміністратор мережі може попросити MAC-адресу пристрою для внесення до списку дозволених перед наданням інтернет-доступу.

Знайдіть точні MAC-адреси пристрою одним із наведених нижче способів.

## Спосіб 1. Етикетка пристрою — лише MAC-адреса WAN {#method-1-via-product-label-for-wan-mac-only}

Знайдіть **MAC-адресу WAN** на нижній етикетці.

Наприклад, на зображенні нижче MAC-адреса WAN — E4:95:6E:40:DB:A9.

![MAC-адреса WAN на етикетці](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/wan_lan_wifi.png){class="glboxshadow"}

## Спосіб 2. SSH {#method-2-via-ssh}

Використання SSH описано [тут](https://docs.gl-inet.com/router/en/4/tutorials/ssh_log_in_to_the_router/).

Виконайте **ifconfig** через SSH. У результаті послідовно відобразяться інтерфейси, наприклад br-lan, ethx, wlanx тощо.

### MAC-адреси портів Ethernet {#find-the-mac-of-ethernet-ports}

Розгляньте приклад нижче.

![MAC-адреси портів Ethernet у ifconfig](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwan.jpg){class="glboxshadow"}

- **eth0** — порт WAN із MAC-адресою **94:83:C4:19:19:08**.

    Якщо є додатковий порт WAN, наприклад у GL-MT6000, буде ще одна MAC-адреса WAN.

- **eth1**, **eth2** та інші — порти LAN із MAC-адресою **94:83:C4:19:19:09**.

    Навіть за наявності кількох портів LAN буде лише одна MAC-адреса.

### MAC-адреси бездротових портів {#find-the-mac-of-wireless-ports}

Розгляньте приклад нижче.

![MAC-адреси Wi-Fi у ifconfig](https://static.gl-inet.com/docs/router/en/4/faq/how_can_i_know_the_lan_wifi_mac/ifcongwifi.jpg){class="glboxshadow"}

- **wlan0-1** — Wi-Fi 2.4G із MAC-адресою **96:83:C4:19:19:0B**.

- **wlan1** — Wi-Fi 5G із MAC-адресою **94:83:C4:19:19:0A**.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
