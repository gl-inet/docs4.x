# Як налаштувати Urban Shield VPN на маршрутизаторі GL.iNet {#how-to-set-up-urban-shield-vpn-on-glinet-router}

[Urban Shield VPN](https://urbanshieldvpn.com/) — провайдер VPN, який пропонує користувачам у всьому світі безпечні та продуктивні рішення VPN. Він надає попередньо налаштовані VPN-маршрутизатори GL.iNet і гнучкі плани підписки для безпечного та конфіденційного перегляду вебсторінок. Активуйте Urban Shield VPN на маршрутизаторі, щоб отримати захищений доступ до серверів провайдера в різних країнах для перегляду вебсторінок і потокового відео.

## Посібник із налаштування {#setup-guide}

Нижче наведено приклад налаштування GL-B3000 як клієнта WireGuard для підключення до Urban Shield VPN.

### 1. Створіть обліковий запис Urban Shield VPN {#1-sign-up-urban-shield-vpn}

Відвідайте [офіційний вебсайт Urban Shield VPN](https://urbanshieldvpn.com/){target="_blank"}, щоб створити обліковий запис Urban Shield VPN.

![Реєстрація Urban Shield VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/sign_in.png){class="glboxshadow"}

### 2. Увімкніть маршрутизатор {#2-power-on-router}

Увімкніть маршрутизатор, а потім підключіть до нього пристрій (наприклад, ноутбук або смартфон) кабелем Ethernet або через Wi-Fi.

### 3. Відкрийте вебпанель адміністрування {#3-access-web-admin-panel}

Виконайте наведені нижче дії, щоб відкрити вебпанель адміністрування. Якщо ви вже ввійшли в неї, перейдіть до [наступного розділу](#4-network-setup).

Відкрийте веббраузер (рекомендовано Chrome, Edge або Safari) і перейдіть за адресою [192.168.8.1](http://192.168.8.1){target="_blank"}. Відкриється сторінка початкового налаштування вебпанелі адміністрування, як показано нижче. Задайте пароль адміністратора та натисніть **Next**, щоб продовжити.

![Налаштування пароля адміністратора](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/web_panel_signup.png){class="glboxshadow"}

Налаштуйте мережу Wi-Fi. На сторінці відображаються заводські налаштування Wi-Fi, зокрема назва мережі (SSID) і пароль. Їх можна змінити або залишити. Якщо ви зміните налаштування Wi-Fi, повторно підключіть пристрій до оновленої мережі Wi-Fi.

![Налаштування мережі Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/set_up_wifi.png){class="glboxshadow"}

Потім натисніть **Next** і ввійдіть за допомогою пароля адміністратора.

### 4. Налаштуйте мережу {#4-network-setup}

У верхньому правому куті розташований **Network Setup Wizard** (доступний у прошивці v4.7 та новіших версіях). Перед налаштуванням VPN скористайтеся майстром, щоб налаштувати доступ маршрутизатора до інтернету.

![Майстер налаштування мережі](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/network_setup_wizard.jpg){class="glboxshadow"}

### 5. Активуйте Urban Shield VPN {#5-activate-urban-shield-vpn}

У меню ліворуч перейдіть до **VPN** -> **WireGuard Client**. Відкриється сторінка входу в Urban Shield VPN.

![Сторінка входу в Urban Shield VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_1.png){class="glboxshadow"}

Уведіть облікові дані Urban Shield VPN (**Email** і **Password**) та натисніть **Save And Continue**. Буде створено файли конфігурації для кожного сервера.

![Уведення облікових даних Urban Shield VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/urban_shield_login_2.png){class="glboxshadow"}

Виберіть потрібний сервер і натисніть **Apply**.

![Вибір сервера](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/select_server.png){class="glboxshadow"}

Доступні сервери з’являться у списку.

![Список доступних серверів](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/get_servers.png){class="glboxshadow"}

Натисніть значок із трьома крапками, щоб установити з’єднання.

![Установлення з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/start_server.jpg){class="glboxshadow"}

Після підключення з’явиться синя крапка, яка вказує на успішне з’єднання.

![Успішне з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/server_started.jpg){class="glboxshadow"}

Також можна перевірити стан з’єднання на сторінці VPN Dashboard.

![Стан VPN на панелі керування](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/vpn_dashboard.png){class="glboxshadow"}

## Редагування облікових даних або вихід {#edit-account-info-or-logout}

Натисніть значок шестірні, щоб змінити облікові дані або вийти з облікового запису.

![Меню редагування облікових даних і виходу](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_1.jpg){class="glboxshadow"}

![Редагування облікових даних або вихід](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/edit_account_or_logout_2.jpg){class="glboxshadow"}

## Поновлення підписки {#go-renew}

Натисніть **Go Renew**, щоб перейти на офіційний вебсайт для поновлення підписки.

![Поновлення підписки](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/go_renew.jpg){class="glboxshadow"}

## Видалення {#delete}

Одним натисканням можна видалити всі файли конфігурації, а також приватний і публічний ключі.

![Видалення всіх конфігурацій](https://static.gl-inet.com/docs/router/en/4/interface_guide/setup_urban_shield_vpn/delete_all.jpg){class="glboxshadow"}

---
