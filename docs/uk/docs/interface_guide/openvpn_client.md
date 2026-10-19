# Налаштування клієнта OpenVPN на маршрутизаторах GL.iNet {#set-up-openvpn-client-on-glinet-routers}

OpenVPN — протокол VPN із відкритим вихідним кодом, який використовує технології віртуальних приватних мереж для встановлення захищених з’єднань між мережами (site-to-site) або між двома вузлами (point-to-point).

Щоб налаштувати клієнт OpenVPN на маршрутизаторі GL.iNet, перегляньте це відео або виконайте наведені нижче дії.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="Відеопрогравач YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Перед початком переконайтеся, що маєте активну підписку на VPN-сервіс, який підтримує ручне налаштування OpenVPN. Перелік провайдерів OpenVPN, сумісних із GL.iNet, наведено [тут](https://www.gl-inet.com/solutions/vpn/){target="_blank"}.

Зазвичай спочатку потрібно відкрити офіційний сайт свого VPN-провайдера, завантажити файл конфігурації, а потім передати його на маршрутизатор для налаштування клієнта OpenVPN. Якщо ви не знаєте, як отримати файл конфігурації, див. [цей розділ](#get-configuration-files-from-openvpn-service-providers) або зверніться до служби підтримки провайдера.

Клієнт OpenVPN можна налаштувати через вебпанель адміністрування або [мобільний застосунок](../faq/mobile_app.md). Нижче описано налаштування через вебпанель адміністрування.

---

<span id="setup-openvpn-client"></span>

У вебпанелі адміністрування відкрийте **VPN** -> **OpenVPN Client**.

Якщо у вас є підписка NordVPN, натисніть **NordVPN** для входу. Інакше натисніть **Add Manually**, щоб завантажити файли конфігурації OpenVPN.

![Клієнт OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## Налаштування NordVPN {#set-up-nordvpn}

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} — популярний VPN-сервіс для швидкого й захищеного доступу до інтернету.

Швидке налаштування NordVPN інтегровано у вебпанель адміністрування маршрутизаторів GL.iNet. Введіть облікові дані, отримані на сторінці NordVPN Dashboard, у вебпанелі маршрутизатора або мобільному застосунку, щоб отримати файли конфігурації всіх серверів NordVPN онлайн без ручного завантаження файлів.

1. Увійдіть у свій обліковий запис на сайті NordVPN за [цим посиланням](https://my.nordaccount.com/){target="_blank"}.

    ![Вхід до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

    Після входу на Nord Dashboard виберіть **NordVPN** у лівому меню та натисніть **Set up NordVPN manually**.

    ![Ручне налаштування NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Знайдіть **service credentials** — службові облікові дані. Спочатку підтвердьте адресу електронної пошти, щоб отримати їх, а потім скопіюйте для подальшого використання.

    ![Службові облікові дані NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Увійдіть у вебпанель адміністрування маршрутизатора та відкрийте **VPN** -> **OpenVPN Client** -> **NordVPN**.

    Введіть **service credentials**, отримані на кроці 1. Ці службові облікові дані **НЕ** є адресою електронної пошти та паролем для входу до облікового запису. Потім натисніть **Save and Continue**.

    ![Введення службових облікових даних NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Виберіть протокол, максимальну кількість серверів для кожного розташування та потрібні розташування, а потім натисніть **Apply**.

    ![Вибір серверів NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn2.png){class="glboxshadow"}

    Буде завантажено файли конфігурації.

    ![Файли конфігурації NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Встановіть з’єднання.

    Виберіть потрібний сервер і натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Підключення до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання NordVPN встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

6. Оновіть список серверів.

    Натисніть **Update Servers**, щоб отримати актуальний список доступних серверів і уникнути збоїв підключення через технічне обслуговування або вимкнення серверів.

    ![Оновлення серверів NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Змініть облікові дані.

    Натисніть піктограму шестерні, щоб змінити облікові дані для входу.

    ![Зміна облікових даних NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Видаліть усі файли.

    Натисніть **Delete All**, щоб видалити всі файли конфігурації одним натисканням.

    ![Видалення всіх конфігурацій NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nordvpn9.png){class="glboxshadow"}

## Ручне налаштування клієнта OpenVPN для інших провайдерів {#set-up-openvpn-client-manually-for-other-providers}

Якщо ваш провайдер OpenVPN не інтегрований у вебпанель адміністрування, спочатку отримайте файл конфігурації на його офіційному сайті. Потім завантажте файл на маршрутизатор для налаштування клієнта OpenVPN.

У цьому прикладі використано [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}.

1. Завантажте файл конфігурації з офіційного сайту Private Internet Access.

2. Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте VPN -> OpenVPN Client і натисніть **Add Manually**.

    ![Ручне додавання конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual1.png){class="glboxshadow"}

3. На лівій бічній панелі буде створено групу.

    ![Додавання групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual2.png){class="glboxshadow"}

4. Задайте зрозумілу назву групи, наприклад private internet access.

    ![Назва нової групи](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual3.png){class="glboxshadow"}

5. Завантажте файл конфігурації OpenVPN. За потреби введіть облікові дані та натисніть **Apply**.

    ![Ручне завантаження файлів](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual4.png){class="glboxshadow"}

    - Доступні 4 варіанти облікових даних для автентифікації:

        1. Без автентифікації.

        2. Лише ім’я користувача та пароль (Username і Password).

        3. Лише парольна фраза (Passphrase).

        4. Ім’я користувача, пароль і парольна фраза (Username, Password і Passphrase).

    Після цього відобразиться завантажений файл конфігурації.

    ![Ручне завантаження файлів](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual5.png){class="glboxshadow"}

6. Натисніть піктограму з трьома крапками праворуч, щоб розпочати підключення.

    ![Встановлення з’єднання](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual6.png){class="glboxshadow"}

7. Після встановлення з’єднання біля файлу конфігурації з’явиться зелена крапка.

    ![З’єднання OpenVPN встановлено](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manual7.png){class="glboxshadow"}

    Відомості про з’єднання VPN також можна переглянути на **VPN Dashboard**.

## Налаштування сервера OpenVPN на маршрутизаторі GL.iNet {#set-up-openvpn-server-on-glinet-router}

Якщо у вас два маршрутизатори GL.iNet, налаштуйте один як сервер OpenVPN (потрібна публічна IP-адреса), а інший — як клієнт OpenVPN. Так можна створити власне з’єднання VPN без підписки на сторонні VPN-сервіси.

Налаштування сервера OpenVPN описано [тут](openvpn_server.md).

<span id="get-configuration-files-from-openvpn-service-providers-get-configuration-files-from-openvpn-service-providers"></span>

## Отримання файлів конфігурації від провайдерів OpenVPN {#get-configuration-files-from-openvpn-service-providers}

Ми перевірили понад 30 провайдерів OpenVPN та описали отримання файлів конфігурації. Якщо ви не знаєте, як отримати потрібний файл, виконайте наведені нижче дії.

Якщо вашого провайдера немає у списку, зверніться до його служби підтримки.

??? "NordVPN"
    ### NordVPN {#nordvpn}

    [Офіційний сайт](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Увійдіть у свій обліковий запис NordVPN**

        Увійдіть на [офіційний сайт](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} та відкрийте Nord Account Dashboard, де містяться службові облікові дані.

        ![Вхід до NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_login.png){class="glboxshadow"}

        Після входу на Nord Dashboard натисніть NordVPN ліворуч, а потім **Set up NordVPN manually**.

        ![Панель NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![Ручне налаштування NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Знайдіть **Service credentials**. Скопіюйте їх для використання під час завантаження конфігурації на маршрутизатор.

        ![Службові облікові дані NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Виберіть сервер NordVPN і завантажте файл конфігурації**

        Відкрийте вкладку **Server recommendation**. На ній буде рекомендовано сервер відповідно до вашої мережі та запропоновано доступні протоколи для завантаження. Натисніть **Get setup configuration**, щоб продовжити.

        ![Завантаження конфігурації NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_config_download.png){class="glboxshadow"}

        У спливному вікні виберіть протокол **OpenVPN** і завантажте конфігурацію UDP або TCP.

        ![Вибір протоколу NordVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Конфігурації всіх серверів можна завантажити [тут](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip).

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

    [Додаткова інструкція](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Також можна налаштувати NordVPN через [мобільний застосунок](../faq/mobile_app.md).

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Офіційний сайт](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Увійдіть у свій обліковий запис AirVPN.

        ![Відомості облікового запису AirVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Виберіть Config Generator ліворуч, а потім Linux як операційну систему. Далі виберіть потрібний сервер.

        ![Генератор конфігурацій OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Відкриється сторінка завантаження файлу конфігурації.

        ![Завантаження конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill {#astrill}

    [Офіційний сайт](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Інформацію наведено за [офіційною інструкцією Astrill](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}.

    1. Створіть і завантажте ZIP-архів конфігурації OpenVPN для Astrill.

        ![Інструменти Astrill VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![Створення сертифіката](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Введіть Description, наприклад OPENVPN_GUI.

    3. Натисніть кнопку ADD to my certificates.

        ![Створення сертифіката](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Після додавання сертифіката OpenVPN натисніть кнопку Download.

        ![Завантаження сертифіката](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN {#bolehvpn}

    [Офіційний сайт](https://www.bolehvpn.net/){target="_blank"}

    Увійдіть на [Dashboard](https://users.bolehvpn.net/){target="_blank"}, завантажте файли конфігурації та виберіть формат [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Після завантаження розпакуйте ZIP-архіви.

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

    [Додаткова інструкція](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN {#cactusvpn}

    [Офіційний сайт](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Завантажте конфігурації](https://www.cactusvpn.com/downloads/){target="_blank"} безпосередньо.

    ![Завантаження профілів OpenVPN для CactusVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm {#cryptostorm}

    [Офіційний сайт](https://cryptostorm.is/){target="_blank"}

    [Завантажте конфігурації](https://cryptostorm.is/configs/ecc/){target="_blank"} безпосередньо.

??? "CyberGhost"
    ### CyberGhost {#cyberghost}

    [Офіційний сайт](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Інформацію наведено за [офіційною інструкцією CyberGhost](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}.

    1. Увійдіть у свій обліковий запис на сайті CyberGhost VPN.

        ![Вхід до облікового запису](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Виберіть «**VPN**» у лівому меню, натисніть «**Configure Device**» і створіть конфігурацію сервера, як описано нижче:

        ![Налаштування пристрою](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![Збереження конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Створіть конфігурацію сервера:

        * **Protocol** : **OpenVPN**
        * **Country** : для прямих підключень за протоколом можна використовувати лише один сервер. Виберіть країну, через яку хочете отримувати доступ до інтернету; CyberGhost автоматично вибере сервер у цій країні.
        * **Server group** : виберіть групу серверів і потрібний протокол OpenVPN (UDP або TCP).

        **OpenVPN UDP** забезпечує вищу швидкість, ніж TCP, але в деяких випадках може спричиняти переривання завантажень. Цей варіант використовується за замовчуванням.

        **OpenVPN TCP** забезпечує стабільніші з’єднання, ніж UDP, але працює дещо повільніше. Виберіть його, якщо регулярно виникають проблеми зі з’єднанням, наприклад раптові відключення.

        Після вибору потрібних параметрів збережіть їх за допомогою **Save Configuration**.

    4. Щоб переглянути створені облікові дані **OpenVPN** на панелі конфігурації, натисніть **View Configuration**.

        ![Перегляд конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Після налаштування з’єднання врахуйте такі відомості:

        * **Server Group** : адреса країни (сервера), до якої ви підключатиметеся, наприклад '12345-1-ca.cg-dialup.net'. Вона змінюється залежно від вибраної на попередньому кроці країни. CyberGhost автоматично вибирає конкретний сервер.
        * **Username** : ім’я користувача, створене лише для цього протоколу. Це НЕ звичайне ім’я користувача облікового запису CyberGhost. Воно використовується лише для автентифікації на серверах CyberGhost через ручні конфігурації та потрібне під час налаштування OpenVPN на маршрутизаторах GL.iNet.
        * **Password** : пароль, створений лише для цього протоколу. Це НЕ звичайний пароль облікового запису CyberGhost. Він використовується лише для автентифікації на серверах CyberGhost через ручні конфігурації та потрібний під час налаштування OpenVPN на маршрутизаторах GL.iNet.

        Після завершення натисніть *Download Configuration*, щоб завантажити файл конфігурації на комп’ютер.

        ![Збереження конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN {#expressvpn}

    [Офіційний сайт](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"} | [30 днів безкоштовно](https://www.expressvpn.com/refer-a-friend/30-days-free?referrer_id=97477587){rel="sponsored" target="_blank"}

    1. Відкрийте сайт [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"} і увійдіть зі своїми обліковими даними ExpressVPN.

        ![Вхід до облікового запису ExpressVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        **Введіть код підтвердження**, надісланий на вашу електронну пошту.

    2. У лівому меню натисніть **Set up your devices**.

        ![Налаштування пристроїв ExpressVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. У розділі **Applications** розгорніть **Advanced setup** і натисніть **Manual Configuration**.

        ![Ручна конфігурація ExpressVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Відобразяться **username**, **password** і список **файлів конфігурації OpenVPN**.

        ![Облікові дані та конфігурації ExpressVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Натисніть потрібні розташування, щоб завантажити відповідні файли .ovpn.

        **Залиште це вікно браузера відкритим**. Ці відомості знадобляться для подальшого налаштування.

    [Додаткова інструкція](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN {#fastestvpn}

    [Офіційний сайт](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Завантажте файли конфігурації FastestVPN (ZIP-архів) для OpenVPN TCP і UDP за [цим посиланням](https://support.fastestvpn.com/download/fastestvpn_ovpn/).

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

    [Додаткова інструкція](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN {#finchvpn}

    [Офіційний сайт](https://www.finchvpn.com/){target="_blank"}

    1. Увійдіть у свій обліковий запис FinchVPN.

        ![Вхід до FinchVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Відкрийте сторінку Download і натисніть Download у розділі FinchVPN OpenVPN Config.

        ![Сторінка завантаження FinchVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Виберіть Linux.

        ![Налаштування FinchVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Виберіть потрібний протокол. Зазвичай можна вибрати перший варіант — **Port 8484 over UDP**.

        ![Налаштування FinchVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Перед завантаженням файлу встановіть прапорець включення імені користувача та пароля.

        ![Налаштування FinchVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN {#hideipvpn}

    [Офіційний сайт](https://www.hideipvpn.com/){target="_blank"}

    1. Увійдіть у свій обліковий запис HideIPVPN.

    2. Відкрийте Package ліворуч, виберіть свій пакет і переконайтеся, що він активний.

        ![Обліковий запис HideIPVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. На вкладці VPN у розділі VPN Login Details відображаються ім’я користувача та пароль для підключення OpenVPN.

        ![Обліковий запис HideIPVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Прокрутіть униз, щоб завантажити файли конфігурації OpenVPN.

        ![Обліковий запис HideIPVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Офіційний сайт](https://hide.me/?friend=glinet){target="_blank"}

    1. Увійдіть у свій обліковий запис Hide.me та знайдіть Server Locations ліворуч.

    2. Завантажте конфігурацію OpenVPN для Windows.

        ![Панель Hide.me VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield {#hotspot-shield}

    [Офіційний сайт](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Примітка: файли конфігурації Hotspot Shield для маршрутизаторів більше недоступні та не підтримуються. Наведені нижче дії збережено для користувачів, у яких ці файли вже встановлено.**

    1. Відкрийте [https://www.hotspotshield.com/](https://www.hotspotshield.com/){target="_blank"} і натисніть Account. За потреби увійдіть.

        ![Вхід до Hotspot Shield](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Відкрийте [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router){target="_blank"}.

        У розкривному списку Select location виберіть віртуальне розташування маршрутизатора. Натисніть «Download file», щоб завантажити файл конфігурації config.ovpn на комп’ютер. Ім’я користувача та пароль потрібно буде ввести під час налаштування клієнта OpenVPN на маршрутизаторі.

        ![Підключення маршрутизатора до Hotspot Shield](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Додаткова інструкція](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router){target="_blank"}

??? "IPVANISH"
    ### IPVANISH {#ipvanish}

    [Офіційний сайт](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Завантажте конфігурації всіх серверів [тут](https://configs.ipvanish.com/configs/configs.zip). Архів містить усі файли конфігурації серверів (.ovpn) і файл сертифіката (.crt). Для деяких моделей .zip може бути завеликим; видаліть файли .ovpn серверів, які не використовуватимете.

        ![Усі конфігурації OpenVPN для IPVANISH](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Також можна завантажити конфігурації окремих серверів [тут](https://www.ipvanish.com/software/configs/){target="_blank"}, але разом із ними потрібно завантажити **ca.ipvanish.com.crt**. Перед передаванням на маршрутизатор запакуйте **ca.ipvanish.com.crt** і файли конфігурації .ovpn у ZIP-архів .zip.

        ![Конфігурація та сертифікат IPVANISH](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Додаткова інструкція](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup){target="_blank"}

??? "IVACY"
    ### IVACY {#ivacy}

    [Офіційний сайт](https://billing.ivacy.com/page/22852){target="_blank"}

    Для налаштування клієнта OpenVPN із Ivacy потрібні:

    - Ім’я користувача для ручної конфігурації OpenVPN, наведене у вікні «Download Configuration»
     ![Ім’я користувача OpenVPN для Ivacy](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Пароль, який ви використовуєте для входу до облікового запису Ivacy
    - Файл конфігурації OpenVPN

    [Додаткова інструкція](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/){target="_blank"}

??? "IVPN"
    ### IVPN {#ivpn}

    [Офіційний сайт](https://www.ivpn.net/){target="_blank"}

    1. Завантажте [файли конфігурації OpenVPN](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip).

    2. Знайдіть Account ID у [IVPN Client Area](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Після перетягування файлу конфігурації в Add a New OpenVPN Configuration потрібно ввести User Name і Password. User Name — це ваш Account ID, який починається з **ivpn**. Пароль може бути будь-яким, наприклад **ivpn**.

        ![Налаштування IVPN на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Додаткова інструкція](https://www.ivpn.net/setup/gnu-linux-terminal.html){target="_blank"}

??? "OVPN"
    ### OVPN {#ovpn}

    [Офіційний сайт](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Увійдіть і виберіть наведений нижче пункт меню, щоб отримати файли конфігурації OpenVPN.

    ![Отримання конфігурацій OVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Виберіть сервер і завантажте конфігурацію.

    ![Завантаження конфігурацій OpenVPN для OVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Ім’я користувача та пароль збігаються з обліковими даними для входу до OVPN.

??? "OysterVPN"
    ### OysterVPN {#oystervpn}

    [Офіційний сайт](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Відкрийте [список серверів OysterVPN](https://support.oystervpn.com/server-list/){target="_blank"} і натисніть **Download .ovpn file**, щоб завантажити файл конфігурації.

        ![Завантаження файлу .ovpn для OysterVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Ім’я користувача та пароль для з’єднання OpenVPN збігаються з обліковими даними для входу до OysterVPN.

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

??? "PIA (Private Internet Access)"
    ### PIA {#pia}

    [Офіційний сайт](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Завантажте конфігурації](https://www.privateinternetaccess.com/openvpn/openvpn.zip) безпосередньо.

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Офіційний сайт](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Увійдіть і знайдіть **Download VPN Configuration**.

    ![Конфігурація OpenVPN для PrivadoVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Офіційний сайт](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Завантажте конфігурації](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank"} безпосередньо.

    Офіційне посилання для завантаження наведено [тут](https://privatevpn.com/client/PrivateVPN-TUN.zip). Ім’я файлу в архіві містить спеціальні символи 'Bogotá', які спричиняють помилку імпорту на маршрутизатор. Ми перейменували файл і надали посилання вище. Помилку буде виправлено в майбутніх версіях.

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Офіційний сайт](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN підтримує WireGuard. Рекомендовано використовувати WireGuard; див. [цей розділ](wireguard_client.md#wireguard-providers)**.

    1. Увійдіть у свій обліковий запис [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}.

    2. Натисніть **Download** ліворуч.

    3. Виберіть платформу Router, протокол та інші параметри, знайдіть потрібну країну й завантажте файл конфігурації.

        ![Файл конфігурації OpenVPN для Proton VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. Облікові дані для підключення OpenVPN відрізняються від даних для входу на панель сайту Proton. Їх можна знайти в **Account -> OpenVPN/IKEv2 username**.

        ![Облікові дані OpenVPN для Proton VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Офіційний сайт](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Для налаштування клієнта OpenVPN із PureVPN потрібні ім’я користувача та пароль OpenVPN і файл конфігурації. Їх можна знайти у своєму обліковому записі PureVPN.

    1. [Увійдіть у свій обліковий запис PureVPN.](https://my.purevpn.com/){target="_blank"}
    2. На лівій бічній панелі натисніть **Subscriptions**.
    3. Прокрутіть униз, щоб знайти ім’я користувача та пароль OpenVPN.
        ![Ім’я користувача та пароль PureVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. На лівій бічній панелі натисніть **Manual Configuration**.
    5. Виберіть розташування VPN і натисніть **Download**, щоб завантажити файл конфігурації.

    [Додаткова інструкція](https://support.purevpn.com/openvpn-files){target="_blank"}

    Маршрутизатори GL.iNet не підтримують функцію [виділеної IP-адреси](https://www.purevpn.com/dedicated-ip){target="_blank"} PureVPN, оскільки для неї потрібен PPTP.

??? "SaferVPN"
    ### SaferVPN {#safervpn}

    [Офіційний сайт](https://safervpn.com/?a_aid=563){target="_blank"}

    Натисніть [тут](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup){target="_blank"}, щоб безпосередньо завантажити файли конфігурації.

    ![Конфігурація OpenVPN для SaferVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN {#starvpn}

    [Офіційний сайт](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN пропонує VPN-сервіс із протоколами OpenVPN і WireGuard. Рекомендовано WireGuard, оскільки він зазвичай швидший за OpenVPN. Див. [цей розділ](wireguard_client.md#starvpn).

    Щоб використовувати OpenVPN, виконайте наведені нижче дії для завантаження файлу конфігурації.

    1. **Зареєструйте обліковий запис StarVPN**

        Відкрийте [тарифні плани](https://www.starvpn.com/#pricing){target="_blank"} і виберіть потрібний план VPN. Зареєструйтеся під час оформлення підписки або за [цим посиланням](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Завантажте конфігурацію OpenVPN**

        Увійдіть на [панель облікового запису](https://www.starvpn.com/dashboard){target="_blank"} StarVPN. Знайдіть розділ **VPN Configuration** і натисніть **OpenVPN Config**. Скопіюйте ім’я користувача та пароль OVPN. Ці дані потрібні для автентифікації під час завантаження файлу на маршрутизатор GL.iNet.

        ![Завантаження конфігурації OpenVPN для StarVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/ovpnconfigdl.png){class="glboxshadow"}

        Виберіть UDP або TCP і завантажте файл конфігурації.

        ![Вибір UDP або TCP](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/udp_tcp.png){class="glboxshadow"}

    3. **Змініть файл конфігурації**

        Деякі маршрутизатори GL.iNet не підтримують IPv6. Щоб уникнути проблем сумісності та з’єднання, відкрийте файл конфігурації .ovpn і видаліть вміст, пов’язаний з IPv6, як показано нижче.

        ![Вилучення налаштувань IPv6](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/starvpn/remove_ipv6.png){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN {#streamvpn}

    [Офіційний сайт](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Увійдіть у свій обліковий запис [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}, щоб переглянути відомості про підписку. Натисніть **Install & Guides**.

        ![Відомості про підписку StreamVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Натисніть **VPN Router**, щоб завантажити ZIP-архів `StreamVPN.zip`.

        ![Конфігурація StreamVPN для маршрутизатора](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Примітка:** працюють лише файли конфігурації, назва яких містить «Primary».

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Офіційний сайт](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Увійдіть у свій обліковий запис [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, щоб переглянути VPN Accounts Summary. Натисніть **Account Setup Instructions**.

        ![Налаштування StrongVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Знайдіть розділ Manual setup і виконайте дії для отримання конфігурації.

        ![Отримання конфігурації StrongVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Офіційний сайт](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Знайдіть облікові дані для входу**

        Службові облікові дані Surfshark відрізняються від адреси електронної пошти та пароля вашого облікового запису Surfshark. Для ручного налаштування OpenVPN на маршрутизаторі потрібні саме службові облікові дані.

        Увійдіть на [офіційний сайт](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} і відкрийте [цю сторінку](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, де наведено всі дані для ручного підключення.

        ![Службові облікові дані Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Виберіть сервер Surfshark**

        Відкрийте вкладку **Locations**, щоб переглянути всі сервери Surfshark.

        ![Розташування серверів Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Виберіть TCP або UDP. Відмінності описано [тут](../faq/openvpn_tcp_udp.md).

        ![Вибір TCP або UDP для Surfshark](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}


    Усі конфігурації можна безпосередньо завантажити [тут](https://api.surfshark.com/v1/server/configurations).

    Порада: якщо ZIP-архів завеликий для завантаження на маршрутизатор, видаліть із .zip частину файлів .ovpn або завантажте один файл .ovpn.

    [Додаткова інструкція](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Офіційний сайт](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Завантажте конфігурації](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="Завантаження конфігурації VPN.AC" src="https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate {#vpngate}

    [Офіційний сайт](https://www.vpngate.net/en/){target="_blank"}

    Файли конфігурації OpenVPN наведено на [сайті VPN Gate](https://www.vpngate.net/en/) за розташуванням серверів.

    1. Натисніть OpenVPN Config file у стовпці **OpenVPN**.

        ![Список серверів VPNGate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Відкриється сторінка завантаження.

        ![Сторінка завантаження VPNGate](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Офіційний сайт](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Інформацію наведено за [офіційною інструкцією VPN unlimited](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}.

    Увійдіть у User Office, натисніть Manage для сервісу VPN Unlimited і виконайте такі дії:

    1. Виберіть пристрій.

        Виберіть пристрій зі списку або створіть новий. Якщо вільних слотів немає, видаліть старий пристрій або придбайте додаткові слоти.

        ![Конфігурація OpenVPN для VPN Unlimited](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Виберіть потрібне розташування сервера.

        VPN Unlimited пропонує понад 400 серверів у понад 70 розташуваннях. У цьому прикладі виберіть Німеччину.

    3. Виберіть протокол VPN.

        Виберіть протокол OpenVPN.

        ![Вибір протоколу VPN Unlimited](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Створіть конфігурацію.

        Натисніть Generate, щоб отримати всі дані для налаштування з’єднання VPN.

        ![Створення конфігурації VPN Unlimited](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN {#vyprvpn}

    Файли OpenVPN для VyprVPN доступні тут: [де знайти файли OpenVPN — підтримка VyprVPN](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}.

    ZIP-архів містить дві папки з файлами .ovpn: OpenVPN160 і OpenVPN256. Видаліть папку OpenVPN160 з архіву, а потім завантажте його на маршрутизатор GL.iNet звичайним способом.

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Офіційний сайт](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Увійдіть у свій обліковий запис Windscribe за [цим посиланням](https://windscribe.com/login?auth_required){target="_blank"} і відкрийте [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Виберіть розташування сервера, протокол (UDP/TCP), потрібний порт (наприклад, 1194) і версію OpenVPN (бажано новішу), а потім натисніть **Download Config**. Файл із розширенням «.ovpn» буде завантажено на ваш пристрій.

        ![Генератор конфігурацій OpenVPN для Windscribe](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Натисніть **Get Credentials** на цій самій сторінці, щоб отримати відповідні облікові дані. Вони потрібні для автентифікації у вебпанелі адміністрування під час завантаження конфігурації на маршрутизатор. Скопіюйте їх або залиште сторінку відкритою.

    4. Далі виконайте [цю інструкцію](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers).

??? "ZoogVPN"
    ### ZoogVPN {#zoogvpn}

    [Офіційний сайт](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Увійдіть на [офіційний сайт](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"} і відкрийте [сторінку файлів конфігурації OpenVPN](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}, де наведено всі сервери. Завантажте файл конфігурації зі стовпця TCP або UDP.

    ![Файли конфігурації OpenVPN для ZoogVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Далі виконайте [інструкцію з налаштування клієнта OpenVPN на маршрутизаторі GL.iNet](#setup-openvpn-client). Ім’я користувача та пароль збігаються з даними для входу на сайт ZoogVPN.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
