# Як використовувати каскадне підключення VPN на маршрутизаторах GL.iNet? {#how-to-use-vpn-cascading-on-glinet-routers}

## Вступ {#introduction}

У деяких випадках каскадне підключення VPN називають «Double VPN», але на маршрутизаторах GL.iNet воно може дещо відрізнятися. Основну схему показано нижче.

![Каскадне підключення VPN GL.iNet](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (маршрутизатор як сервер VPN)**: коли маршрутизатор працює як сервер VPN, підключені до цього сервера клієнти за замовчуванням отримують доступ до інтернету через мережу інтернет-провайдера маршрутизатора.

**VPN 2 (маршрутизатор як клієнт VPN)**: маршрутизатор також працює як клієнт VPN і підключається до сторонньої служби VPN.

**Каскадне підключення VPN**: маршрутизатор пересилає трафік із тунелю VPN 1 до тунелю VPN 2. Завдяки цьому пристрої, підключені до маршрутизатора через VPN 1, отримують доступ до інтернету через сторонню службу VPN (VPN 2) замість мережі інтернет-провайдера маршрутизатора.

## Увімкнення каскадного підключення VPN {#how-to-enable-vpn-cascading}

### Для прошивки v4.7 і старіших версій {#for-firmware-v47-and-earlier}

1. Спочатку налаштуйте маршрутизатор як сервер VPN. Для вищої швидкості рекомендуємо протокол WireGuard. Див. [цю інструкцію](../interface_guide/wireguard_server.md){target="_blank"}.

2. Експортуйте файл конфігурації з маршрутизатора та завантажте його на клієнтський пристрій, який підключатиметься до маршрутизатора через VPN.

3. Налаштуйте маршрутизатор як клієнт VPN, підключений до сторонньої служби VPN. Для вищої швидкості рекомендуємо протокол WireGuard. Див. [цю інструкцію](../interface_guide/wireguard_client.md){target="_blank"}.

4. Після підключення сторінка **VPN Dashboard** матиме наведений нижче вигляд: маршрутизатор одночасно працює як сервер VPN і клієнт VPN.

    ![Панель керування VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    На цій самій сторінці перейдіть до розділу **VPN Server** і натисніть **Global Options**.

    ![Глобальні параметри](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Увімкніть **VPN Cascading** і натисніть **Apply**.

    ![Увімкнення каскадного підключення VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. Каскадне підключення VPN увімкнено. Пристрої, підключені до маршрутизатора через VPN, отримуватимуть доступ до інтернету через сторонню службу VPN замість мережі інтернет-провайдера маршрутизатора.

### Для прошивки v4.8 і новіших версій {#for-firmware-v48-and-higher}

1. Спочатку налаштуйте маршрутизатор як сервер VPN. Для вищої швидкості рекомендуємо протокол WireGuard. Див. [цю інструкцію](../interface_guide/wireguard_server.md){target="_blank"}.

2. Експортуйте файл конфігурації з маршрутизатора та завантажте його на клієнтський пристрій, який підключатиметься до маршрутизатора через VPN.

3. Налаштуйте маршрутизатор як клієнт VPN, підключений до сторонньої служби VPN. Для вищої швидкості рекомендуємо протокол WireGuard. Див. [цю інструкцію](../interface_guide/wireguard_client.md){target="_blank"}.

4. У вебпанелі адміністрування перейдіть до **VPN Dashboard**. Виберіть відповідні інструкції нижче залежно від режиму VPN.

    ??? "Global Mode"

        Якщо використовується **Global Mode**, каскадне підключення VPN вмикається автоматично після ввімкнення клієнта VPN (як показано нижче).

        Пристрої, підключені до маршрутизатора через VPN, отримуватимуть доступ до інтернету через сторонню службу VPN замість мережі інтернет-провайдера маршрутизатора.

        ![Підключення VPN у Global Mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"

        Якщо використовується **Policy Mode**, потрібно налаштувати правило VPN-тунелю.

        Натисніть сіре поле ліворуч.

        ![Джерело трафіку](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-traffic_from_1.png){class="glboxshadow"}

        Виберіть джерело трафіку, до якого застосовуватиметься це правило. Щоб увімкнути каскадне підключення VPN, виберіть **All Clients** або виберіть **Specified Connection Types**, а потім **WireGuard/OpenVPN Server**.

        ![Вибір джерела трафіку](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: охоплює всі пристрої локальної мережі, пристрої Drop-in Gateway, пристрої гостьової мережі та пристрої, підключені до маршрутизатора через VPN.

            Якщо потрібно застосувати однакове правило тунелю до трафіку всіх пристроїв, виберіть **All Clients** і натисніть **Apply**.

            ![Усі клієнти](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: дає змогу застосувати правило тунелю до пристроїв, підключених до маршрутизатора певним способом (наприклад, через VPN).

            Якщо для клієнтів VPN вашого маршрутизатора потрібно застосувати інше правило, ніж для решти пристроїв, виберіть **WireGuard/OpenVPN Server** і натисніть **Apply**.

            ![Вибрані типи підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}

            Нижче наведено приклад правил VPN-тунелю в режимі **Policy Mode**.

            ![Панель керування VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. Каскадне підключення VPN увімкнено. Пристрої, підключені до маршрутизатора через VPN, отримуватимуть доступ до інтернету через сторонню службу VPN замість мережі інтернет-провайдера маршрутизатора.

6. **Перевірка підключення**: на ноутбуці, підключеному до маршрутизатора через VPN, відкрийте браузер і перейдіть на [What Is My IP](https://whatismyipaddress.com/){target="_blank"}, щоб перевірити публічну IP-адресу.

    Якщо IP-адреса ноутбука відповідає регіону стороннього сервера VPN (у цій інструкції — Буенос-Айрес), каскадне підключення VPN працює.

    ![Перевірка VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
