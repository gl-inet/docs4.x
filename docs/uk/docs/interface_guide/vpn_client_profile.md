# Профіль клієнта VPN {#vpn-client-profile}

**Примітка**: Ця сторінка з’явилася у прошивці v4.9.

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **VPN** -> **VPN Client Profile**.

Починаючи з прошивки v4.9, сторінки [OpenVPN Client](openvpn_client.md) і [WireGuard Client](wireguard_client.md) об’єднано в одну сторінку **VPN Client Profile** для зручнішого керування. Компонування дещо змінено, проте основні можливості залишилися ті самі. За потреби можна й надалі користуватися окремими посібниками.

На цій сторінці можна ввійти в інтегровані служби VPN і завантажити їхні профілі для з’єднання VPN або вручну завантажити файли конфігурації, експортовані з вебсайту іншого провайдера VPN. За потреби перемкніть протокол VPN у верхньому правому куті.

## WireGuard {#wireguard}

WireGuard® — сучасний, легкий і продуктивний протокол VPN із передовою криптографією. Він забезпечує вищу швидкість, простоту та практичність порівняно з IPsec і значно перевершує OpenVPN за продуктивністю.

Маршрутизатори GL.iNet мають вбудовану підтримку WireGuard для наведених нижче провайдерів VPN. Якщо у вас є активна підписка, уведіть облікові дані служби на сторінці **VPN Client Profile**, щоб швидко завершити налаштування.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![Провайдери WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

Якщо ви користуєтеся іншим провайдером WireGuard, завантажте файл конфігурації з його вебсайту, а потім натисніть **Add Manually**, щоб завантажити файл на маршрутизатор для з’єднання VPN.

![Ручне додавання профілю WireGuard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

Якщо ви не знаєте, як завантажити файли конфігурації, дивіться інструкції [тут](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) або зверніться до підтримки провайдера.

---

Нижче наведено приклад для [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}.

1. На сторінці **VPN Client Profile** натисніть **AzireVPN**.

    ![Вибір AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Уведіть **Username** і **Password** та натисніть **Save and Continue**.

    ![Уведення облікових даних AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    Система створить файли конфігурації для всіх доступних серверів.

    ![Конфігурації доступних серверів](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Виберіть відповідні інструкції нижче залежно від ваших потреб.

    !!! note "Варіант 1. Щоб усі підключені клієнти використовували VPN для доступу до інтернету, виконайте такі дії."

        1. Виберіть потрібний сервер і натисніть значок із трьома крапками праворуч, щоб установити з’єднання.

            ![Установлення з’єднання AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Після підключення біля файла конфігурації з’явиться зелена крапка.

            ![Успішне з’єднання AzireVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            З’єднання VPN активовано. Усі клієнти, підключені до цього маршрутизатора, мають використовувати VPN для захищеного доступу до інтернету.

        3. (Необов’язково) Щоб система автоматично блокувала весь доступ до інтернету для локальної мережі в разі несподіваного розриву з’єднання VPN, запобігаючи розкриттю справжньої IP-адреси та даних і забезпечуючи безперервну конфіденційність та безпеку, перейдіть до **VPN Dashboard** і ввімкніть **Kill Switch**.

            * Щоб налаштувати Kill Switch для окремого тунелю VPN, дивіться інструкції [тут](vpn_dashboard.md#tunnel-options).

            * Щоб налаштувати Kill Switch для глобального з’єднання VPN (Enhanced Kill Switch), дивіться інструкції [тут](vpn_dashboard.md#all-other-traffic).

    !!! note "Варіант 2. Щоб налаштувати власну політику VPN, виконайте такі дії."

        1. Натисніть **Go to Dashboard** унизу.

            ![Перехід до панелі керування VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Відкриється **VPN Dashboard** для налаштування політики VPN. Докладніше дивіться [тут](vpn_dashboard.md#add-vpn-tunnel).

## OpenVPN {#openvpn}

OpenVPN — протокол VPN із відкритим вихідним кодом, який використовує технології віртуальних приватних мереж для встановлення захищених з’єднань між мережами (site-to-site) або між двома вузлами (point-to-point).

Маршрутизатори GL.iNet мають вбудовану підтримку OpenVPN для [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Якщо у вас є активна підписка, уведіть облікові дані служби на сторінці **VPN Client Profile**, щоб швидко завершити налаштування.

![Провайдери OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Якщо ви користуєтеся іншим провайдером OpenVPN, завантажте файл конфігурації з його вебсайту, а потім натисніть **Add Manually**, щоб завантажити файл на маршрутизатор для з’єднання VPN.

![Ручне додавання профілю OpenVPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

Якщо ви не знаєте, як завантажити файли конфігурації, дивіться інструкції [тут](openvpn_client.md#get-configuration-files-from-openvpn-service-providers) або зверніться до підтримки провайдера.

---

Пов’язані статті

- [Панель керування VPN (прошивка v4.9)](vpn_dashboard.md)
- [Налаштування клієнта WireGuard на маршрутизаторах GL.iNet](wireguard_client.md)
- [Налаштування клієнта OpenVPN на маршрутизаторах GL.iNet](openvpn_client.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
