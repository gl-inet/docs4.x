# Налаштування клієнта WireGuard на маршрутизаторах GL.iNet {#set-up-wireguard-client-on-glinet-routers}

Вміст цієї сторінки ґрунтується на прошивці v4.7 і новіших версіях. Якщо на пристрої встановлено іншу версію прошивки, виберіть відповідну інструкцію нижче.

<div class="gl-link-select" data-label="Версія прошивки" data-placeholder="Прошивка v4.7 і новіші версії" markdown="1">

- [Прошивка v4.6 і попередні версії](wireguard_client_v4.6.md)

</div>

---

WireGuard® — простий, швидкий і сучасний VPN, який використовує сучасні криптографічні технології. Його мета — працювати швидше, простіше й ефективніше за IPsec, бути кориснішим і не створювати зайвих складнощів. Він також має на меті забезпечити значно вищу продуктивність, ніж OpenVPN.

Щоб налаштувати клієнт WireGuard на маршрутизаторі GL.iNet, перегляньте це відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIRcjB9k62A" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Маршрутизатори GL.iNet мають вбудовану підтримку WireGuard для наведених нижче VPN-провайдерів. За наявності активної підписки введіть службові облікові дані на сторінці **WireGuard Client**, щоб швидко завершити налаштування.

Виберіть провайдера WireGuard нижче, щоб перейти до покрокової інструкції.

* [Налаштування AzireVPN](#set-up-azirevpn)
* [Налаштування Hide.me](#set-up-hideme)
* [Налаштування IPVanish](#set-up-ipvanish)
* [Налаштування Mullvad](#set-up-mullvad)
* [Налаштування NordVPN](#set-up-nordvpn)
* [Налаштування PIA (Private Internet Access)](#set-up-pia-private-internet-access)
* [Налаштування PureVPN](#set-up-purevpn)
* [Налаштування Surfshark](#set-up-surfshark)
* [Налаштування Windscribe](#set-up-windscribe)
* [Налаштування X-VPN](#set-up-x-vpn)

Якщо ви підписані на іншого провайдера WireGuard, завантажте файл конфігурації з його сайту, а потім передайте файл на маршрутизатор для встановлення з’єднання VPN.

* [Ручне налаштування клієнта WireGuard для інших провайдерів](#set-up-wireguard-client-manually-for-other-providers)

## Налаштування AzireVPN {#set-up-azirevpn}

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} — VPN-сервіс, орієнтований на конфіденційність, який надає захищені, сучасні й надійні тунелі, зокрема WireGuard.

Перегляньте це відео, щоб налаштувати AzireVPN на маршрутизаторі GL.iNet через вебпанель адміністрування або мобільний застосунок.

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ra93wlDIekA" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Або виконайте наведені нижче дії для налаштування AzireVPN через вебпанель адміністрування.

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **AzireVPN**.

1. Введіть **Username** і **Password** AzireVPN, які ви використовуєте для входу до AzireVPN, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn1.png){class="glboxshadow"}

2. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn2.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn3.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

3. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn5.png){class="glboxshadow"}

4. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn6.png){class="glboxshadow"}

5. Поновіть підписку.

    Натисніть **Go Renew**, щоб перейти на офіційний сайт і поновити підписку.

    ![Поновлення підписки AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn7.png){class="glboxshadow"}

6. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_azirevpn/azirevpn8.png){class="glboxshadow"}

## Налаштування Hide.me {#set-up-hideme}

[Офіційний сайт](https://hide.me/en/){target="_blank"}

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **Hide.me**.

1. Введіть **Username** і **Password** Hide.me, які ви використовуєте для входу до Hide.me, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme1.png){class="glboxshadow"}

2. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme2.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme3.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

3. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme5.png){class="glboxshadow"}

4. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme6.png){class="glboxshadow"}

5. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій Hide.me](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_hidemevpn/hideme7.png){class="glboxshadow"}

## Налаштування IPVanish {#set-up-ipvanish}

[Офіційний сайт](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **IPVanish**.

1. Введіть **Username** і **Password** IPVanish, які ви використовуєте для входу до IPVanish, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish1.png){class="glboxshadow"}

2. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish2.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish6.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish7.png){class="glboxshadow"}

6. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій IPVanish](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_ipvanish/ipvanish8.png){class="glboxshadow"}

## Налаштування Mullvad {#set-up-mullvad}

[Mullvad](https://mullvad.net/){target="_blank"} — VPN-сервіс, який допомагає зберігати конфіденційність вашої активності в інтернеті, особи та розташування.

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **Mullvad**.

1. Введіть **Account** Mullvad (16-значний номер) і натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad1.png){class="glboxshadow"}

2. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad2.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad6.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad7.png){class="glboxshadow"}

6. Поновіть підписку.

    Натисніть **Go Renew**, щоб перейти на офіційний сайт і поновити підписку.

    ![Поновлення підписки Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad8.png){class="glboxshadow"}

7. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій Mullvad](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_mullvad/mullvad9.png){class="glboxshadow"}

## Налаштування NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} — VPN-сервіс, який поєднує швидкість і безпеку.

1. Увійдіть у свій обліковий запис на сайті NordVPN за [цим посиланням](https://my.nordaccount.com/){target="_blank"}.

    ![Вхід до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn_login.png){class="glboxshadow"}

    Після входу на Nord Dashboard натисніть **NordVPN** у лівому меню, знайдіть **Access Token** і натисніть **Get Access token**.

    ![Токен доступу NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token1.png){class="glboxshadow"}

    На наступній сторінці натисніть **Generate new token**.

    ![Токен доступу NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token2.png){class="glboxshadow"}

    У спливному вікні виберіть дату завершення дії токена та натисніть **Generate token**.

    ![Токен доступу NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token3.png){class="glboxshadow"}

    Відобразиться токен доступу, як показано нижче. Скопіюйте його для подальшого використання.

    **Примітка**: токен доступу відображається лише один раз. Скопіюйте та використайте його зараз. Після закриття вікна токен більше не буде видно. Якщо ви його не збережете, потрібно буде створити новий.

    ![Токен доступу NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nord_token4.png){class="glboxshadow"}

2. Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **VPN** -> **WireGuard Client** -> **NordVPN**.

    Введіть **Token** і натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn1.png){class="glboxshadow"}

3. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn2.png){class="glboxshadow"}

4. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

5. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn6.png){class="glboxshadow"}

6. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn7.png){class="glboxshadow"}

7. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_nordvpn/nordvpn8.png){class="glboxshadow"}

## Налаштування PIA (Private Internet Access) {#set-up-pia-private-internet-access}

[Офіційний сайт](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **PIA**.

1. Введіть **Username** і **Password** PIA, які ви використовуєте для входу до PIA, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia1.png){class="glboxshadow"}

2. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia2.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia6.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia7.png){class="glboxshadow"}

6. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій PIA](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_pia/pia8.png){class="glboxshadow"}

## Налаштування PureVPN {#set-up-purevpn}

[Офіційний сайт](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

[15-денний безкоштовний пробний період PureVPN](https://purevpn.com/refer-a-friend-v2?referrer=bEZTci9KcmtQSTFPbXlPak03NWtENWZaL1BHNENlR0JOMzV6RURhWFhSOD0=){target="_blank"}

1. Увійдіть на панель PureVPN за [цим посиланням](https://www.purevpn.com/){target="_blank"}.

    ![Вхід до PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_login.png){class="glboxshadow"}

    Після входу натисніть **Subscriptions** у лівому меню та прокрутіть униз до **credentials**. Скопіюйте ім’я користувача та пароль для подальшого використання.

    ![Облікові дані PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn_credentials.png){class="glboxshadow"}

2. Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **VPN** -> **WireGuard Client** -> **PureVPN**.

    Введіть скопійовані **Username** і **Password** та натисніть **Save and Continue**.

    ![Вхід до PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn1.png){class="glboxshadow"}

    Буде створено всі доступні файли конфігурації.

    ![Файли конфігурації PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn2.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn6.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn7.png){class="glboxshadow"}

6. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_purevpn/purevpn8.png){class="glboxshadow"}

## Налаштування Surfshark {#set-up-surfshark}

[Офіційний сайт](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **Surfshark**.

1. Введіть **Username** і **Password** Surfshark, які ви використовуєте для входу до Surfshark, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark1.png){class="glboxshadow"}

2. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark2.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark3.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark4.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark6.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark7.png){class="glboxshadow"}

6. Оновіть публічний ключ.

    Натисніть **Refresh**, щоб оновити публічний ключ, якщо не вдається підключитися до сервера VPN.

    ![Оновлення публічного ключа Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark8.png){class="glboxshadow"}

7. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark/surfshark9.png){class="glboxshadow"}

## Налаштування Windscribe {#set-up-windscribe}

[Офіційний сайт](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client** -> **Windscribe**.

1. Введіть **Username** і **Password** Windscribe, які ви використовуєте для входу до Windscribe, та натисніть **Save and Continue**. Буде створено файли конфігурації для кожного сервера.

    ![Вхід до Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe1.png){class="glboxshadow"}

2. Виберіть сервери.

    Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe2.png){class="glboxshadow"}

    Відобразиться список файлів конфігурації для вибраного сервера.

    ![Файли конфігурації Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe3.png){class="glboxshadow"}

3. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe4.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe5.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

4. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe7.png){class="glboxshadow"}

5. Змініть облікові дані або вийдіть з облікового запису.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу або вийти з облікового запису.

    ![Зміна облікових даних або вихід із Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe8.png){class="glboxshadow"}

6. Оновіть публічний ключ.

    Натисніть **Refresh**, щоб оновити публічний ключ, якщо не вдається підключитися до сервера VPN.

    ![Оновлення публічного ключа Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe9.png){class="glboxshadow"}

7. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням. Також можна вибрати, чи видаляти одночасно приватний і публічний ключі.

    ![Видалення конфігурацій Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_windscribe/windscribe10.png){class="glboxshadow"}

## Налаштування X-VPN {#set-up-x-vpn}

[Офіційний сайт](https://xvpn.io/){target="_blank"}

**Примітка**: X-VPN інтегровано в маршрутизатори GL.iNet починаючи з прошивки v4.11.

1. Спочатку отримайте токен X-VPN на офіційному сайті.

    Увійдіть у свій обліковий запис на сайті X-VPN за [цим посиланням](https://xvpn.io/login){target="_blank"}.

    ![Вхід до X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn1.png){class="glboxshadow"}

    Після входу натисніть **Settings** у лівому меню. Знайдіть **Login Token** і натисніть **Generate**.

    ![Налаштування X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn2.png){class="glboxshadow"}

    Буде створено токен, який діє 15 хвилин. Скопіюйте його для подальшого використання.

    ![Створення токена X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn3.png){class="glboxshadow"}

2. Увійдіть у вебпанель адміністрування маршрутизатора GL.iNet та відкрийте **VPN** -> **VPN Client Profile**. Натисніть **X-VPN**.

    ![Введення токена X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn4.png){class="glboxshadow"}

    Введіть токен і натисніть **Save and Continue**.

    ![Введення токена X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn5.png){class="glboxshadow"}

3. Виберіть сервери, до яких потрібно підключитися, та натисніть **Apply**.

    ![Вибір серверів X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn6.png){class="glboxshadow"}

    Відобразиться список файлів конфігурації для вибраного сервера.

    ![Файли конфігурації X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn7.png){class="glboxshadow"}

4. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn8.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання встановлено: X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn9.png){class="glboxshadow"}

    На **VPN Dashboard** також можна переглядати відомості про з’єднання VPN, створювати тунелі й політики VPN та керувати ними.

5. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn10.png){class="glboxshadow"}

6. Поновіть підписку.

    Натисніть **Go Renew**, щоб перейти на офіційний сайт і поновити підписку.

    ![Поновлення підписки X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn11.png){class="glboxshadow"}

7. Видаліть конфігурації.

    Натисніть піктограму шестерні праворуч і виберіть **Delete Configurations**, щоб одним натисканням видалити певні або всі файли конфігурації.

    ![Видалення конфігурацій X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn12.png){class="glboxshadow"}

8. Змініть дані автентифікації.

    За потреби натисніть піктограму шестерні праворуч і виберіть **Modify Authentication Information**, щоб змінити токен для входу.

    ![Зміна облікових даних X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn13.png){class="glboxshadow"}

    ![Зміна облікових даних X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn14.png){class="glboxshadow" width="600"}

9. Вийдіть з облікового запису.

    За потреби натисніть піктограму шестерні праворуч і виберіть **Logout**. Буде видалено збережені на маршрутизаторі облікові дані, пов’язані публічний і приватний ключі та файли конфігурації. Виконуйте цю дію обережно.

    ![Вихід із облікового запису X-VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_xvpn/xvpn15.png){class="glboxshadow"}

## Ручне налаштування клієнта WireGuard для інших провайдерів {#set-up-wireguard-client-manually-for-other-providers}

Якщо ви підписані на іншого провайдера WireGuard, завантажте файл конфігурації з його сайту та виконайте наведені нижче дії. Як отримати файл конфігурації, описано в [цій інструкції](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md). Також можна звернутися до служби підтримки провайдера.

У вебпанелі адміністрування відкрийте **VPN** -> **WireGuard Client**.

1. Натисніть **Add Manually**.

    ![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/add_manually.png){class="glboxshadow"}

2. На лівій бічній панелі буде створено групу.

    ![Додавання групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/create_a_group.png){class="glboxshadow"}

3. Задайте зрозумілу назву групи, наприклад azirevpn. Завантажте файл конфігурації (підтримувані формати: zip, tar, gz, conf, txt) або вручну додайте конфігурацію як текст.

    ![Назва нової групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/set_a_name.png){class="glboxshadow"}

    1. **Завантажте файл конфігурації**.

        Натисніть область завантаження, виберіть файл конфігурації WireGuard і натисніть **Apply**.

        ![Завантаження профілю](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file.png){class="glboxshadow"}

        ![Завантажений профіль](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/upload_configuration_file_apply.png){class="glboxshadow"}

    2. **Додайте конфігурацію вручну**.

        Натисніть **Manually Add Configuration** унизу області завантаження.

        ![Текстова конфігурація WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Задайте зрозумілу назву та вставте конфігурацію в текстове поле. Потім натисніть **Apply**.

        ![Текстова конфігурація WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/text_mode.png){class="glboxshadow"}
        <small>(Text Mode)</small>

        Щоб перевірити окремі параметри, перейдіть у режим Item і перегляньте конфігурацію. Потім натисніть **Apply**.

        ![Конфігурація WireGuard за окремими параметрами](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/item_mode.png){class="glboxshadow"}
        <small>(Item Mode)</small>

4. Натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Дії з профілем](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_wireguard_client/start_edit_delete.png){class="glboxshadow"}

    Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

## Налаштування клієнта WireGuard через мобільний застосунок {#set-up-wireguard-client-via-mobile-app}

Клієнт WireGuard також можна налаштувати через [мобільний застосунок](https://www.gl-inet.com/app/#download-app-glinet).

У мобільний застосунок інтегровано деяких провайдерів WireGuard, зокрема AzireVPN, Mullvad VPN, OVPN, StrongVPN і PIA VPN. Щоб налаштувати клієнт WireGuard, введіть облікові дані сервісу WireGuard, на який ви підписані.

Встановіть застосунок і виконайте інструкції на екрані для потрібного налаштування.

## Налаштування сервера WireGuard на маршрутизаторі GL.iNet {#set-up-wireguard-server-on-glinet-router}

Щоб обійтися без підписки на сторонні VPN-сервіси, можна придбати два маршрутизатори GL.iNet: налаштуйте один як сервер WireGuard, а інший — як клієнт WireGuard.

Цей варіант особливо підходить, якщо провайдер домашньої мережі надає публічну IP-адресу, а ви хочете підключатися до домашньої мережі через VPN поза домом для захищеного доступу до внутрішніх ресурсів. Так можна уникнути витрат і потреби постійно поновлювати підписки на комерційні VPN-сервіси.

Налаштування сервера WireGuard описано [тут](wireguard_server.md).

---

WireGuard® — зареєстрована торговельна марка Jason A.Donenfeld.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
