# Не вдається виявити точку доступу Wi-Fi 5G на Android {#cannot-scan-android-5g-hotspot}

Підключення маршрутизатора GL.iNet як ретранслятора до точки доступу Wi-Fi 5G телефона Android — поширений спосіб доступу до інтернету.

Якщо точку доступу 5G телефона Android не вдається виявити, причина може бути в каналі Wi-Fi.

Деякі телефони Android за замовчуванням використовують для точки доступу 5G канал США. Якщо маршрутизатор GL.iNet придбано поза США, може виникнути ця проблема.

Щоб змінити код країни Wi-Fi маршрутизатора GL.iNet через LuCI, виконайте такі дії.

1. Увійдіть у маршрутизатор GL.iNet і відкрийте **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Увійдіть у LuCI з тим самим паролем адміністратора.

2. Змініть налаштування Wi-Fi.

    Відкрийте **Network** -> **Wireless**, знайдіть Wi-Fi 5G і натисніть **Edit** праворуч.

    ![Налаштування Wi-Fi 5G](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gwifi.jpg){class="glboxshadow"}

3. Виберіть код країни US.

    На сторінці Wireless відкрийте вкладку **Advanced Settings** у розділі **Device Configuration**. Виберіть US (United States) як код країни для Wi-Fi 5GHz.

    ![Код країни US для Wi-Fi 5G](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/5gus.jpg){class="glboxshadow"}

4. Перед виходом натисніть **Save & Apply**.

    ![Збереження налаштувань Wi-Fi](https://static.gl-inet.com/docs/router/en/4/faq/cannot_scan_android_5g_hotspot/saveapply.jpg){class="glboxshadow"}

    Після цього знову спробуйте знайти точку доступу 5G телефона Android.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
