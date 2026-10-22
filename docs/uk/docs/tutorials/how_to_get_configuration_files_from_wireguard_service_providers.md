# Як отримати файли конфігурації від постачальників послуг WireGuard {#how-to-get-configuration-files-from-wireguard-service-providers}

??? "AzireVPN"
    ### AzireVPN {#azirevpn}

    [Офіційний сайт](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Відкрийте [офіційний сайт AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}, увійдіть до облікового запису, а потім відкрийте [генератор конфігурацій WireGuard](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![Генератор конфігурацій WireGuard AzireVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. У параметрі IP виберіть **IPv4**. Потім натисніть **Download Configuration**.

        ![Генератор конфігурацій WireGuard AzireVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-azirevpn).

    4. Ви також можете налаштувати AzireVPN через [мобільний застосунок](../faq/mobile_app.md).

??? "Hide.me VPN"
    ### Hide.me VPN {#hideme-vpn}

    [Офіційний сайт](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN пропонує простий спосіб використання своєї служби WireGuard на маршрутизаторі GL.iNet.

    1. Підключіться до маршрутизатора через [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"}.

    2. Скопіюйте наведену нижче команду встановлення, вставте її в термінал і натисніть Enter. (Щоб вставити команду, натисніть праву кнопку миші.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. Почнеться встановлення, після чого вам буде запропоновано ввести ім’я користувача та пароль. Під час введення або вставлення пароля символи в терміналі не відображаються. Після введення натисніть Enter.

    4. Після завершення відкрийте вебпанель адміністрування. У ній буде створено групу hide.me VPN із файлами конфігурації. Підключіться за допомогою одного з цих файлів, як зазвичай.

    **Примітка:** Ключ у файлі конфігурації Hide.me VPN генерується заново перед кожним підключенням і стає недійсним після відключення. Тому копіювання цього файлу конфігурації на інші пристрої не дасть змоги встановити з’єднання.

    [Джерело](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad {#mullvad}

    [Офіційний сайт](https://mullvad.net/){target="_blank"}

    1. Відкрийте [офіційний сайт Mullvad](https://mullvad.net/){target="_blank"}, увійдіть до облікового запису, а потім відкрийте [генератор файлів конфігурації WireGuard](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-mullvad).

    3. Ви також можете налаштувати Mullvad через [мобільний застосунок](../faq/mobile_app.md).

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access) {#pia-private-internet-access}

    [Офіційний сайт](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    Завантажити конфігурації WireGuard із сайту PIA неможливо. Для налаштування PIA VPN скористайтеся [мобільним застосунком](../faq/mobile_app.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark {#surfshark}

    [Офіційний сайт](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Якщо ви користуєтеся [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}, увійдіть до облікового запису, відкрийте [цю сторінку](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}, натисніть **Router** і виберіть **WireGuard**.

        ![Ручне налаштування WireGuard Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. У наступному вікні виберіть **I don't have a key pair**.

        ![Ручне налаштування WireGuard Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Виберіть **Generate a new key pair**.

        ![Ручне налаштування WireGuard Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Після створення ключа виберіть **Choose a location**.

        ![Ручне налаштування WireGuard Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Виберіть потрібне розташування та натисніть кнопку **download** поруч із ним, щоб завантажити файли конфігурації.

        ![Ручне налаштування WireGuard Surfshark](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-surfshark).

    [Джерело](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN {#airvpn}

    [Офіційний сайт](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Якщо ви користуєтеся [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"}, увійдіть до облікового запису на сайті, перейдіть до [Client Area](https://airvpn.org/client/){target="_blank"} і натисніть [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![Генератор конфігурацій AirVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. На сторінці **Config Generator** у розділі **Protocols** виберіть **WireGuard**.

        ![Вибір протоколу AirVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Виберіть сервер, прокрутіть сторінку донизу та натисніть **Generate**. Буде завантажено файл конфігурації.

        ![Вибір сервера AirVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Astrill"
    ### Astrill {#astrill}

    [Офіційний сайт](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Якщо ви користуєтеся [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}, увійдіть до облікового запису та відкрийте [цю сторінку](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}, щоб створити конфігурації WireGuard.

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "IVPN"
    ### IVPN {#ivpn}

    [Офіційний сайт](https://www.ivpn.net/){target="_blank"}

    Якщо ви користуєтеся [IVPN](https://www.ivpn.net/){target="_blank"}, конфігурацію WireGuard потрібно створити вручну. Дотримуйтеся інструкції для своєї операційної системи.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "NVPN"
    ### NVPN {#nvpn}

    [Офіційний сайт](https://www.nvpn.net/){target="_blank"}

    Щоб створити конфігурацію, скористайтеся [цією інструкцією](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"}.

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "OVPN"
    ### OVPN {#ovpn}

    [Офіційний сайт](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Увійдіть на [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} і знайдіть показане нижче меню для отримання файлів конфігурації WireGuard.

        ![Панель керування OVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Натисніть **Generate WireGuard keys**, виберіть потрібний сервер і завантажте конфігурацію.

        ![Створення ключів WireGuard OVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Відкрийте конфігурацію в текстовому редакторі та скопіюйте її вміст.

        Конфігурація може містити параметри IPv6. Оскільки підтримка IPv6 на маршрутизаторах GL.iNet недостатньо повна, видаліть параметри IPv6. На прикладі нижче їх виділено.

        ![Видалення параметрів IPv6 із конфігурації WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}
    
    4. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    5. Ви також можете налаштувати OVPN через [мобільний застосунок](../faq/mobile_app.md).

??? "PrivateVPN"
    ### PrivateVPN {#privatevpn}

    [Офіційний сайт](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Увійдіть до облікового запису та відкрийте [Control panel](https://privatevpn.com/control-panel){target="_blank"}.
    
        ![Панель керування PrivateVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}
    
    2. Виберіть сервер.
    
        ![Вибір сервера](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}
    
    3. Натисніть **GENERATE CONFIG** і скопіюйте конфігурацію.
    
        ![Створення конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PrivadoVPN"
    ### PrivadoVPN {#privadovpn}

    [Офіційний сайт](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Відкрийте сайт PrivadoVPN та увійдіть до облікового запису.

    На панелі керування знайдіть розділ **Manual Configuration** і натисніть **WireGuard**. Виберіть сервер, до якого потрібно підключитися, а потім натисніть **Download Configuration**.

    ![Ручна конфігурація WireGuard PrivadoVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![Завантаження ручної конфігурації WireGuard PrivadoVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "Proton VPN"
    ### Proton VPN {#proton-vpn}

    [Офіційний сайт](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Якщо ви користуєтеся [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}, скористайтеся [цією інструкцією](https://protonvpn.com/support/wireguard-configurations/){target="_blank"}, щоб створити файл конфігурації WireGuard.

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "PureVPN"
    ### PureVPN {#purevpn}

    [Офіційний сайт](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Щоб отримати файл конфігурації PureVPN вручну, скористайтеся [цією інструкцією](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} або виконайте наведені нижче кроки.

    1. Увійдіть до [PureVPN Member Area](https://my.puremember.com/){target="_blank"} зі своїм обліковим записом. Після входу натисніть **Manual Configuration** у меню ліворуч.

        ![Ручна конфігурація PureVPN: меню](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Виберіть потрібне місто та натисніть **Download** праворуч.

        ![Ручна конфігурація PureVPN: вибір міста](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. У спливному вікні виберіть протокол **WireGuard**.

        ![Ручна конфігурація PureVPN: вибір протоколу](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Виберіть тип пристрою **Linux**, а потім натисніть **Generate Configuration**. Файл конфігурації буде завантажено на ваш локальний пристрій.

        ![Ручна конфігурація PureVPN: створення файлу](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

        **Примітка:** Конфігурація WireGuard дійсна протягом 30 хвилин. Активуйте підключення до завершення цього терміну, інакше потрібно буде створити нову конфігурацію.

    Для завершення налаштування скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    [Джерело](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN {#spidervpn}

    [Офіційний сайт](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Увійдіть на [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) і знайдіть розділ для отримання конфігурації VPN. Дотримуйтеся наведених там кроків.

        ![Отримання конфігурації SpiderVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Завантажте конфігурацію VPN.

        ![Завантаження конфігурації SpiderVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "StarVPN"
    ### StarVPN {#starvpn}

    [Офіційний сайт](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Зареєструйте обліковий запис StarVPN**

        Перегляньте [тарифні плани](https://www.starvpn.com/#pricing){target="_blank"} і виберіть відповідний план VPN. Зареєструватися можна під час оформлення замовлення або безпосередньо [тут](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. **Завантажте конфігурацію WireGuard**

        Увійдіть до [панелі керування](https://www.starvpn.com/dashboard){target="_blank"} в особистому кабінеті StarVPN. Натисніть **WireGuard Config**, щоб завантажити файл конфігурації. Кожен слот містить окремий унікальний файл конфігурації WireGuard.

        ![Завантаження конфігурації WireGuard StarVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Порада:** Щоб використовувати обфускацію AmneziaWG, натисніть **AmneziaWG Config** і завантажте файл конфігурації. Кожен слот містить окремий унікальний файл конфігурації AmneziaWG.
    
        ![Завантаження конфігурації AmneziaWG StarVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Відредагуйте файл конфігурації (необов’язково)**
    
        Конфігурація може містити адресу IPv6. Щоб уникнути проблем із сумісністю та підключенням, відкрийте файл .conf і видаліть адресу IPv6, як показано нижче.

        ![Видалення адреси IPv6 із конфігурації WireGuard StarVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), щоб завантажити файл конфігурації на маршрутизатор GL.iNet.

    Додаткові матеріали:
    
    - [Налаштування WireGuard VPN зі StarVPN на маршрутизаторі GL.iNet](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [Налаштування AmneziaWG VPN зі StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN {#strongvpn}

    [Офіційний сайт](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Якщо ви користуєтеся [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}, увійдіть на [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"}.
    
    2. Виберіть розташування з розкривного меню, натисніть **GENERATE** і відкрийте завантажений текстовий файл.
    
        ![Генератор конфігурацій WireGuard StrongVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}
    
    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

    4. Ви також можете налаштувати StrongVPN через [мобільний застосунок](../faq/mobile_app.md).

??? "TRUST.ZONE"
    ### TRUST.ZONE {#trustzone}

    [Офіційний сайт](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Відкрийте [https://trust.zone/setup](https://trust.zone/setup) та увійдіть до облікового запису.
    
    2. Прокрутіть сторінку до розділу WireGuard, виберіть потрібний порт і завантажте конфігурацію окремого сервера або ZIP-архів усіх конфігурацій.

    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN.AC"
    ### VPN.AC {#vpnac}

    [Офіційний сайт](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Якщо ви користуєтеся [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"}, увійдіть до панелі керування та знайдіть **WireGuard Manager** у меню **Services**.
    
        ![Менеджер WireGuard VPN.AC](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}
    
    2. Створіть і завантажте конфігурацію.
    
        ![Створення профілів WireGuard VPN.AC](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid) {#vpn-unlimitedkeepsolid}

    [Офіційний сайт](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Якщо ви користуєтеся [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}, увійдіть до [User Office](https://my.keepsolid.com/){target="_blank"} > виберіть застосунок VPN Unlimited® > натисніть **Manage**.
    
        ![Налаштування VPN Unlimited на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/01.jpg){class="glboxshadow"}
    
    2. Натисніть поле під **Device** і виберіть **Manually create a new device…** > задайте власну назву, наприклад WireGuard > виберіть потрібне розташування **Server** > виберіть протокол **WireGuard**® з розкривного меню > натисніть **Generate**.
    
        ![Налаштування VPN Unlimited на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/02.jpg){class="glboxshadow"}
    
    3. Нижче з’являться параметри конфігурації у текстовому форматі.
    
        ![Налаштування VPN Unlimited на маршрутизаторі GL.iNet](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/vpnunlimited/03.jpg){class="glboxshadow"}

        Складіть конфігурацію за наведеним нижче зразком.

        <p>
        [Interface]<br>
        PrivateKey = <i>вставте PrivateKey із User Office</i><br>
        ListenPort = <i>вставте значення ListenPort</i><br>
        Address = <i>вставте значення Address</i><br>
        DNS = <i>вставте значення DNS із User Office</i><br>
        <br>
        [Peer]<br>
        PublicKey = <i>вставте PublicKey із User Office</i><br>
        PresharedKey = <i>вставте значення PresharedKey</i><br>
        AllowedIPs = <i>вставте значення AllowedIPs</i><br>
        Endpoint = <i>вставте значення Endpoint</i><br>
        </p>

    4. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).
 
    [Джерело 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Джерело 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe {#windscribe}

    [Офіційний сайт](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Увійдіть до свого облікового запису Windscribe [тут](https://windscribe.com/login?auth_required){target="_blank"}, а потім відкрийте [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.
    
    2. Виберіть потрібне розташування сервера та порт, а потім натисніть **Download Config**.

        ![Генератор конфігурацій WireGuard Windscribe](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "X-VPN"
    ### X-VPN {#x-vpn}

    [Офіційний сайт](https://xvpn.io/go?aff_id=nk5bu995){target="_blank"}

    X-VPN інтегровано в маршрутизатори GL.iNet починаючи з прошивки v4.11.
    
    Якщо на маршрутизаторі встановлено прошивку v4.11 або новішу, ви можете увійти до X-VPN безпосередньо у вебпанелі адміністрування GL.iNet за допомогою токена входу. Докладніше — [тут](../interface_guide/wireguard_client.md#set-up-x-vpn).

    Якщо на маршрутизаторі встановлено прошивку, старішу за v4.11, або ви хочете завантажити файл конфігурації X-VPN вручну, виконайте наведені нижче кроки.

    1. [Увійдіть](https://xvpn.io/login){target="_blank"} до X-VPN і перейдіть до **VPN** -> **VPN on Router**.

        ![Конфігурація WireGuard X-VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn1.png){class="glboxshadow"}

    2. Праворуч знайдіть **Step 1** і виберіть протокол **WireGuard**.

        ![Конфігурація WireGuard X-VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn2.png){class="glboxshadow"}

    3. У **Step 2** виберіть потрібні **Region** і **State/City**, а потім натисніть **Search**.

        ![Конфігурація WireGuard X-VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/xvpn/xvpn3.png){class="glboxshadow"}

    4. У результатах пошуку натисніть кнопку завантаження, щоб отримати файл конфігурації потрібного сервера.

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

??? "12VPX"
    ### 12VPX {#12vpx}

    [Офіційний сайт](https://12vpx.com/?aff=1174){target="_blank"}

    Якщо ви користуєтеся [12VPX](https://12vpx.com/?aff=1174){target="_blank"}, увійдіть до облікового запису та відкрийте [цю сторінку](https://12vpx.com/setup/wireguard){target="_blank"}, де наведено конфігурації всіх серверів.

    Для продовження скористайтеся [цією інструкцією](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers).

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
