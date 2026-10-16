# Як дозволити доступ до WAN, коли клієнт VPN увімкнений? {#how-to-allow-access-to-wan-when-vpn-client-is-enabled}

Коли на маршрутизаторі GL.iNet клієнт VPN увімкнено в глобальному режимі за замовчуванням, пристрої LAN не можуть отримувати доступ до локальних пристроїв або служб WAN. Щоб запобігти витокам DNS, увесь трафік LAN спрямовується через тунель VPN, а не через мережу вищого рівня (WAN).

У цьому посібнику описано, як надати пристроям LAN клієнта VPN доступ до локальних служб WAN, наприклад принтера або NAS.

![Схема доступу до WAN під час використання VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

## Для прошивки v4.7 та раніших версій {#for-firmware-v47-and-earlier}

Увійдіть у вебпанель адміністрування клієнта VPN та перейдіть до **VPN** -> **VPN Dashboard** -> **VPN Client**. Натисніть **Global Options** угорі праворуч.

![Глобальні параметри VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-global-options.png){class="glboxshadow"}

Увімкніть **Allow Access WAN** і натисніть **Apply**.

![Дозвіл доступу до WAN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/4.7-allow-access-wan.png){class="glboxshadow"}

Якщо цей параметр увімкнено, під час з’єднання VPN клієнтські пристрої й далі матимуть доступ до служб WAN у підмережі вищого рівня, наприклад принтера або NAS.

## Для прошивки v4.8 та новіших версій {#for-firmware-v48-and-higher}

Параметр **Allow Access WAN** видалено з VPN Dashboard у прошивці v4.8. Проте доступ до локальної WAN можна налаштувати за допомогою політики VPN.

Виконайте наведені нижче дії.

1. Увійдіть у вебпанель адміністрування клієнта VPN та перейдіть до **VPN** -> **VPN Dashboard**.

    Натисніть режим угорі праворуч.

    ![Перемикання режиму VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-1.png){class="glboxshadow"}

    Змініть режим на **Policy Mode** і натисніть **Apply**.

    ![Перемикання режиму VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/switch-mode-2.png){class="glboxshadow"}

    Сторінка оновиться та матиме такий вигляд:

    ![Режим політик VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/primary-tunnel.png){class="glboxshadow"}

2. Натисніть середнє поле, щоб задати призначення тунелю.

    ![Вибір призначення тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-target.png){class="glboxshadow"}

    Виберіть **Exclude specified Domain / IP List**, уведіть підмережу WAN маршрутизатора та натисніть **Apply**.

    Трафік до підмережі WAN проходитиме через локальний WAN замість тунелю VPN.

    ![Виключення підмережі WAN із тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/exclude-target.png){class="glboxshadow"}

    У цьому прикладі використовується підмережа 192.168.0.1/24. Уведіть її та застосуйте налаштування. Тунель VPN матиме такий вигляд:

    ![Застосування виключеної підмережі WAN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/target-apply.png){class="glboxshadow"}

    ??? "Як визначити підмережу WAN маршрутизатора GL.iNet?"

        Підмережу WAN маршрутизатора GL.iNet зазвичай можна знайти на сторінці INTERNET. Її визначає пристрій вищого рівня, до якого підключено інтерфейс WAN, наприклад модем провайдера або шлюз вищого рівня.

        Наприклад, маршрутизатор працює як додатковий, а його порт WAN підключено до іншої локальної мережі, зокрема модема провайдера або порту LAN основного маршрутизатора. Якщо WAN IP маршрутизатора — 192.168.1.165, Gateway — 192.168.1.1, а Subnet Mask — 255.255.255.0 (поширена маска для малих мереж), відповідна підмережа WAN — 192.168.1.0/24. Це також підмережа LAN пристрою вищого рівня.

        ![Відомості про локальну підмережу WAN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/local-wan-details.png){class="glboxshadow gl-80-desktop"}

        **Примітка**: Довжина префікса 192.168.1.0/24 — 24, що відповідає масці підмережі 255.255.255.0. Якщо WAN Subnet Mask маршрутизатора відрізняється від 255.255.255.0, довжина префікса WAN не буде "/24". Визначайте підмережу WAN за фактичною конфігурацією WAN.

3. Натисніть праве поле, щоб задати дію тунелю: використовувати VPN чи ні.

    ![Вибір дії тунелю](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-1.png){class="glboxshadow"}

    Виберіть **Use VPN** і файл конфігурації VPN. Потім натисніть **Apply**.

    Якщо доступної конфігурації немає, спочатку завантажте її, щоб налаштувати маршрутизатор як клієнт VPN. Поверніться на цю сторінку, виберіть Use VPN і файл конфігурації VPN, а потім натисніть Apply.

    ![Вибір конфігурації VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/select-config-2.jpg){class="glboxshadow"}

4. Увімкніть перемикач угорі праворуч, щоб увімкнути цей тунель VPN. Почнеться встановлення з’єднання.

    ![Увімкнення тунелю VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/enable_vpn.png){class="glboxshadow"}

    Зачекайте кілька хвилин. Після успішного підключення індикатор стане зеленим.

    ![Установлене з’єднання VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/vpn_connected.png){class="glboxshadow"}

    Перевірте з’єднання VPN за публічною IP-адресою. Наприклад, відкрийте браузер і перейдіть на [whatismyip](https://whatismyipaddress.com/){target="_blank"}. Відобразяться публічна IP-адреса та місце розташування, як показано нижче.

    ![Перевірка публічної IP-адреси VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ipcheck.png){class="glboxshadow"}

5. Відкрийте пристрої або служби в підмережі WAN та перевірте, чи доступні вони.

    Для перевірки з’єднання можна скористатися командою ping.

    ![Перевірка доступу до WAN командою ping](https://static.gl-inet.com/docs/router/en/4/tutorials/allow_access_to_vpn_server_wan/ping-test.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
