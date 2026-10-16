# Як додати Brume 2 до мобільного застосунку GLiNet? {#how-to-add-brume-2-into-glinet-mobile-app}

Brume 2 (GL-MT2500/GL-MT2500A) можна додати до мобільного застосунку GLiNet, навіть попри відсутність Wi-Fi. Маршрутизатор можна використовувати як основний або додатковий.

Наведені нижче способи також підходять для Brume (GL-MV1000).

## Brume 2 як додатковий маршрутизатор {#brume-2-as-the-secondary-router}

**Топологія**

У цьому прикладі основний маршрутизатор — Slate AX (GL-AXT1800), а додатковий — Brume 2 (GL-MT2500).

![Топологія з Brume 2 як додатковим маршрутизатором](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top1.jpg){class="glboxshadow"}

1. Увійдіть у вебпанель адміністрування Brume 2, перейдіть до **SYSTEM** -> **Security** -> **Open Ports on Router** і відкрийте порт **80**.

    ![Відкриття порту 80 у Security](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.png){class="glboxshadow"}

    Для деяких старіших моделей перейдіть до **Firewall** -> **Open Ports on Router** і відкрийте порт **80**.

    ![Відкриття порту 80 у Firewall](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/open80.jpg){class="glboxshadow"}

2. Увійдіть в основний маршрутизатор і запишіть **WAN IP** Brume 2.

    ![WAN IP Brume 2 на основному маршрутизаторі](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/assignip.jpg){class="glboxshadow"}

3. Підключіть телефон до Wi-Fi основного маршрутизатора.

    ![Підключення телефона до Wi-Fi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

4. Запустіть застосунок glinet і натисніть **Add New Device**.

    ![Додавання нового пристрою](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

5. Натисніть **Initialized Devices**.

    ![Вибір налаштованих пристроїв](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/initdevice.png){class="glboxshadow gl-50-desktop"}

6. Уведіть WAN IP, яку ви знайшли на основному маршрутизаторі.

    ![Уведення WAN IP](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputip.png){class="glboxshadow gl-50-desktop"}

7. Уведіть пароль для входу в Brume 2.

    ![Уведення пароля Brume 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 з’явиться в мобільному застосунку glinet.

    ![Brume 2 у мобільному застосунку](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

## Brume 2 як основний маршрутизатор {#brume-2-as-the-main-router}

**Топологія**

![Топологія з Brume 2 як основним маршрутизатором](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/top2.jpg){class="glboxshadow"}

1. Увійдіть у додатковий маршрутизатор (у цьому прикладі GL-AXT1800) і налаштуйте його в режимі Access Point.

    ![Режим точки доступу додаткового маршрутизатора](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setrouteap.jpg){class="glboxshadow"}

2. Підключіть телефон до Wi-Fi додаткового маршрутизатора.

    ![Підключення телефона до Wi-Fi](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/upperwifi.png){class="glboxshadow gl-50-desktop"}

3. Запустіть застосунок glinet і натисніть **Add New Device**.

    ![Додавання нового пристрою](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/adddevice.png){class="glboxshadow gl-50-desktop"}

4. Виберіть основний маршрутизатор.

    ![Вибір Brume 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/selectbrume2.png){class="glboxshadow gl-50-desktop"}

5. Натисніть **Next**.

    ![Продовження налаштування](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/setupap.png){class="glboxshadow gl-50-desktop"}

6. Якщо телефон досі підключено до Wi-Fi додаткового маршрутизатора, зачекайте. Інакше підключіться до цієї мережі Wi-Fi знову.

    ![Підключення до Wi-Fi точки доступу](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/connectap.png){class="glboxshadow gl-50-desktop"}

7. Уведіть пароль для входу в Brume 2.

    ![Уведення пароля Brume 2](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/inputpw.png){class="glboxshadow gl-50-desktop"}

    Brume 2 з’явиться в мобільному застосунку glinet.

    ![Brume 2 у мобільному застосунку](https://static.gl-inet.com/docs/router/en/4/faq/add_brume2_into_app/showup.png){class="glboxshadow gl-50-desktop"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
