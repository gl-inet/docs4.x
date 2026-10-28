# Підключення маршрутизаторів GL.iNet до мережі EAP {#connect-glinet-routers-to-an-eap-network}

Деякі маршрутизатори GL.iNet підтримують мережі Wi-Fi з EAP (Extensible Authentication Protocol).

EAP — механізм автентифікації, який зазвичай використовується з **автентифікацією 802.1X** у мережах **WPA2‑Enterprise / WPA3‑Enterprise**. Приклад — **eduroam**, глобальний роумінг Wi-Fi для освіти та досліджень на основі 802.1X і EAP.

Нижче описано два способи підключення маршрутизатора GL.iNet до Wi-Fi EAP: через вебпанель адміністрування GL.iNet і через LuCI.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-MG1300 (Mango 2)
    - <u>GL-BE14000 (Flint 4)</u><sup>1</sup>
    - <u>GL-BE10000 (Slate 7 Pro)</u><sup>1</sup>
    - <u>GL-MT3600BE (Beryl 7)</u><sup>1</sup>
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - <u>GL-BE3600 (Slate 7)</u><sup>1</sup>
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>

    ---

    **Примітки:**

    1. У мережах WPA/WPA2/WPA3-Enterprise моделі GL-BE14000 (Flint 4), GL-BE10000 (Slate 7 Pro), GL-MT3600BE (Beryl 7) і GL-BE3600 (Slate 7) підтримують лише автентифікацію PEAP. Інші методи EAP, зокрема EAP-TLS, EAP-TTLS і EAP-MD5, не підтримуються.

    2. GL-MT6000 (Fortify), GL-MT6000 (Flint 2) і GL-MT3000 (Beryl AX) не підтримують мережі EAP у стандартній прошивці. GL.iNet надає для них прошивку на основі оригінального OpenWrt 24 із підтримкою EAP. Знайдіть модель у [центрі завантажень](https://dl.gl-inet.com/){target="_blank"} та відкрийте вкладку OPENWRT 24.

    3. GL-SFT1200 (Opal) підтримує мережі EAP починаючи з прошивки v4.8.

??? "Непідтримувані моделі"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Підключення через вебпанель адміністрування {#connect-via-web-admin-panel}

1. Увійдіть у вебпанель адміністрування, відкрийте **INTERNET** -> **Repeater** і натисніть **Connect**.

    ![Підключення ретранслятора](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Розпочнеться пошук доступних мереж. Знайдіть і виберіть SSID мережі EAP.

    ![Пошук доступних мереж](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Або натисніть **Join Other Network** у верхньому правому куті, щоб додати мережу EAP вручну.

    ![Ручне додавання мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Введіть **SSID**.

    ![Введення SSID](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Для **Security** виберіть WPA/WPA2/WPA3 Enterprise.

    ![Вибір типу захисту](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Введіть **Username** і **Password** та натисніть **Apply** для підключення.

    ![Введення імені користувача та пароля](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Підключення через LuCI {#connect-via-luci}

Вебпанель адміністрування GL.iNet підтримує лише обмежену кількість типів EAP.

Якщо через неї не вдається підключитися до потрібної мережі EAP, спробуйте LuCI.

> Примітка: ці дії надано лише для довідки. Орієнтуйтеся на фактичну сторінку LuCI свого пристрою.

1. У вебпанелі адміністрування відкрийте **SYSTEM** -> **Advanced Settings**. Встановіть LuCI та натисніть **Go to LuCI**.

    ![Перехід до LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Увійдіть у LuCI з тим самим паролем адміністратора та відкрийте Network -> Wireless.

    ![Бездротові мережі LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Натисніть **Scan** у розділі 2.4G або 5G.

    ![Пошук мереж у LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Підключіться до потрібної мережі.

    ![Підключення до мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Усунення несправностей {#troubleshooting}

Якщо мережі EAP потрібні додаткові параметри, наприклад тип EAP (PEAP, TTLS), відповідність суфікса домену, identity або anonymous identity, підключення через вебпанель адміністрування може не вдатися.

![Підключення не вдалося](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Щоб підключити маршрутизатор GL.iNet до мережі EAP із додатковими параметрами через LuCI, виконайте наведені нижче дії.

1. Отримайте параметри конфігурації.

    Заздалегідь отримайте параметри потрібної мережі EAP, зокрема:

    - Тип EAP, наприклад PEAP, TTLS або TLS
    - Суфікс домену автентифікації, наприклад @company.com
    - Identity — зазвичай повне ім’я користувача
    - Anonymous Identity — за потреби
    - Тип внутрішньої автентифікації, наприклад MSCHAPv2 або PAP
    - Сертифікат CA — за потреби підготуйте файл .crt

    Нижче наведено приклад Xfinity Mobile Wi-Fi.

    ![Параметри Xfinity Wi-Fi](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Увійдіть у LuCI.

    Увійдіть у вебпанель адміністрування. Якщо попередня спроба підключення до мережі EAP через WebGUI не вдалася, припиніть її.

    ![Припинення спроби підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    Відкрийте **SYSTEM** -> **Advanced Settings** -> **Go to LuCI** та увійдіть із тим самим паролем адміністратора.

    ![Вхід до LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Налаштуйте ретранслятор у LuCI.

    У LuCI відкрийте Network -> Wireless.

    ![Параметри Xfinity Wi-Fi](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Натисніть **Scan** у розділі 5G або 2.4G для пошуку доступних мереж Wi-Fi.

    ![Пошук бездротових мереж](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Знайдіть потрібну мережу EAP у результатах і натисніть **Join Network**.

    ![Результати пошуку мереж](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    На сторінці «Joining Network» введіть **WPA passphrase** та натисніть **Submit**.

    ![Додавання мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    Відкриється конфігурація Wireless Client.

4. Відкрийте **Interface Configuration** -> **Wireless Security**.

    ![Захист бездротової мережі](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Виберіть або введіть правильні параметри своєї мережі EAP, як показано нижче. **Поки не натискайте Save**.

    ![Приклад параметрів EAP](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Відкрийте вкладку **Advanced Settings**, задайте ім’я інтерфейсу, наприклад **wlan0**, та натисніть **Save** у нижньому правому куті.

    ![Додаткові налаштування](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Відкриється сторінка Wireless із незастосованими змінами. Натисніть **Save & Apply** у нижньому правому куті.

    ![Збереження та застосування](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Маршрутизатор підключиться до потрібної мережі EAP.

7. Перевірте з’єднання.

    ??? "Перевірка у WebGUI"

        Після успішного підключення до мережі EAP у WebGUI засвітиться піктограма ретранслятора, як показано нижче.

        ![Стан підключення](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Примітка**: конфігурація LuCI не синхронізується з WebGUI, тому відомості інтерфейсу ретранслятора, наприклад IP-адреса та шлюз, не відображатимуться у WebGUI.

        На зображенні розділ ретранслятора внизу порожній, але маршрутизатор уже підключено до EAP як ретранслятор: піктограма вгорі світиться.

    ??? "Перевірка через SSH"

        1. Увійдіть у маршрутизатор через [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"}.

        2. Виконайте **ifconfig** і натисніть Enter.

            ![Перевірка інтерфейсу командою ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            Перевірте стан інтерфейсу **wlan0**.

            ![Перевірка інтерфейсу командою ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
