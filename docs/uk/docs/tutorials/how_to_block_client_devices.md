# Як заблокувати певні клієнтські пристрої на маршрутизаторі GL.iNet? {#how-to-block-specific-client-devices-on-a-glinet-router}

У цьому посібнику описано блокування певних клієнтських пристроїв на маршрутизаторі GL.iNet. Блокування запобігає несанкціонованому доступу до мережі, підвищує її безпеку та допомагає керувати доступом сім’ї до інтернету.

Маршрутизатори GL.iNet блокують клієнтські пристрої за MAC-адресами — унікальними 12-символьними ідентифікаторами, призначеними окремим пристроям мережі. Цей спосіб також називається фільтрацією MAC-адрес.

Блокувати клієнтські пристрої можна через [панель адміністрування маршрутизатора](#block-client-devices-via-the-admin-panel) або [мобільний застосунок GL.iNet](#block-client-devices-via-the-glinet-mobile-app).

## Блокування клієнтських пристроїв через панель адміністрування {#block-client-devices-via-the-admin-panel}

### 1. Увійдіть у панель адміністрування {#1-sign-in-to-the-admin-panel}

У веббраузері відкрийте `192.168.8.1`. Уведіть пароль і натисніть **Login**.

### 2. Заблокуйте клієнтські пристрої {#2-block-client-devices}

Є два способи блокування залежно від того, чи знаєте ви MAC-адреси пристроїв:

* Якщо MAC-адреси невідомі, скористайтеся [першим способом](#method-1-block-devices-without-their-mac-addresses), щоб заблокувати пристрої, які відображаються у списках.
* Якщо MAC-адреси відомі, скористайтеся [другим способом](#method-2-block-devices-with-their-mac-addresses).

#### Спосіб 1: блокування без MAC-адрес пристроїв {#method-1-block-devices-without-their-mac-addresses}

1. У меню ліворуч натисніть **Clients**.
![Відкриття списку клієнтів](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-clients.jpeg){class="glboxshadow"}

2. Увімкніть перемикач біля пристрою.
![Увімкнення блокування пристрою](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/toggle-block.jpeg){class="glboxshadow"}

Якщо потрібних пристроїв немає у списках, [додайте їхні MAC-адреси до списку блокування](#method-2-block-devices-with-their-mac-addresses).

#### Спосіб 2: блокування за MAC-адресами пристроїв {#method-2-block-devices-with-their-mac-addresses}

Для цього способу спочатку визначте MAC-адресу пристрою за інструкціями його виробника.
Отримавши MAC-адресу, виконайте такі дії:

1. У меню ліворуч натисніть **Clients**.
2. Угорі натисніть **Blocklist**.
![Відкриття списку блокування](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-blocklist.jpeg){class="glboxshadow"}
3. Виберіть один зі способів блокування:
    - Щоб увести MAC-адреси окремо, введіть їх у порожнє поле.
    - Щоб імпортувати список MAC-адрес, натисніть **Import Clients**, завантажте файл і натисніть **Import**.
4. Натисніть **Apply**.
![Застосування списку блокування](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/click-apply.jpeg){class="glboxshadow"}

## Блокування клієнтських пристроїв через мобільний застосунок GL.iNet {#block-client-devices-via-the-glinet-mobile-app}

**Примітка:** Перед початком установіть і налаштуйте мобільний застосунок GL.iNet на пристрої.

Є два способи блокування залежно від того, чи знаєте ви MAC-адреси пристроїв:

* Якщо MAC-адреси невідомі, скористайтеся [першим способом](#mobile-1), щоб заблокувати пристрої, які відображаються у списку.
* Якщо MAC-адреси відомі, скористайтеся [другим способом](#mobile-2).

### Спосіб 1: блокування без MAC-адрес пристроїв {#mobile-1}

1. На головному екрані застосунку натисніть потрібний пристрій у розділах **Connected Clients** і **Offline Clients**.
![Вибір пристрою в мобільному застосунку](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-a-device.jpeg){class="glboxshadow"}

2. У розділі **Settings** увімкніть перемикач **Block**.
![Увімкнення перемикача Block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/settings-toggle-block-to-on.jpeg){class="glboxshadow"}

Якщо потрібних пристроїв немає у списках, [додайте їхні MAC-адреси до списку блокування](#mobile-2).

### Спосіб 2: блокування за MAC-адресами пристроїв {#mobile-2}

Для цього способу спочатку визначте MAC-адресу потрібного пристрою за інструкціями його виробника.
Отримавши MAC-адресу, виконайте такі дії:

1. На головному екрані застосунку натисніть значок Settings > **Access Control**.
![Відкриття Access Control](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-access-control.jpeg){class="glboxshadow"}

2. Натисніть **Block**.
![Відкриття списку Block](https://static.gl-inet.com/docs/router/en/4/tutorials/how-to-block-client-devices/tap-block.jpeg){class="glboxshadow"}

3. Виберіть один зі способів блокування:
    - Щоб увести MAC-адреси окремо, натисніть **Add MAC address**, уведіть MAC-адресу та натисніть **Done**.
    - Щоб імпортувати список MAC-адрес, натисніть **Import Clients** > **Import Clients** і виберіть файл.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
