# Батьківський контроль (прошивка v4.9) {#parental-control-firmware-v49}

**Примітка**: Цей посібник стосується прошивки v4.9 та новіших версій. Для раніших версій перейдіть [сюди](parental_control.md).

---

У меню ліворуч у вебпанелі адміністрування перейдіть до **FLOW CONTROL** -> **Parental Control**.

Батьківський контроль захищає дітей в інтернеті, блокуючи неприйнятні вебсайти та обмежуючи час перед екраном. Він фільтрує шкідливий вміст і сприяє відповідальному користуванню інтернетом.

Батьківський контроль GL.iNet дає змогу гнучко налаштувати розклад обмеження доступу до інтернету на пристроях, якими часто користуються діти. Неприйнятні застосунки та вебсайти можна блокувати одним натисканням. За потреби також можна вручну ввести домени для комплексного захисту в інтернеті.

---

Виконайте наведені нижче дії, щоб налаштувати батьківський контроль.

1. Увійдіть у вебпанель адміністрування маршрутизатора та перейдіть до **FLOW CONTROL** -> **Parental Control**. Переконайтеся, що час маршрутизатора правильний.

    ![Перевірка часу маршрутизатора](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/router_time.png){class="glboxshadow"}

    Інакше спочатку перейдіть до **SYSTEM** -> **Time Zone** і синхронізуйте його.

2. Увімкніть Parental Control і натисніть **Apply**.

    ![Увімкнення батьківського контролю](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/enable.png){class="glboxshadow"}

3. З’явиться список правил, як показано нижче. Натисніть **Add a New Rule**.

    ![Додавання правила](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/add_rules.png){class="glboxshadow"}

4. У спливному вікні створіть правило, задайте власну назву та натисніть **Next**.

    ![Створення правила](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. Виберіть пристрій дитини та натисніть **Next**.

    Пристрій з’явиться на цій сторінці лише після підключення до маршрутизатора через Wi-Fi або Ethernet. Блакитний колір означає, що пристрій у мережі, а сірий — що він поза мережею.

    ![Вибір пристрою дитини](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **Порада**: Щоб розрізняти підключені пристрої, відкрийте сторінку **CLIENTS** і задайте їм власні назви.

6. Налаштуйте час сну для пристрою дитини та натисніть **Next**.

    У цей період вибрані пристрої не матимуть доступу до інтернету. За замовчуванням час сну однаковий щодня.

    ![Час сну, однаковий щодня](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    Щоб задати різний час сну для кожного дня тижня, виберіть **Customize Days**, налаштуйте час і натисніть **Next**.

    ![Різний час сну за днями тижня](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. Виберіть фільтрацію вмісту.

    За замовчуванням вибрано три категорії: **Gambling**, **Malicious Content** і **Sexual Content**. За потреби виберіть інші категорії, наприклад **Games**, **Shopping**, **Social Media**, **Entertainment** тощо.

    ![Категорії фільтрації вмісту](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Якщо потрібний застосунок складно знайти, скористайтеся пошуком угорі, щоб швидко знайти його.

    ![Пошук застосунку](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. Щоб блокувати певні домени, натисніть **Advanced Settings** унизу праворуч.

    ![Додаткові налаштування блокування доменів](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    Уведіть домени вручну та натисніть **Finish**.

    ![Уведення доменів для блокування](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. Правило додано. У списку відображаються назва правила, кількість підключених пристроїв, розклад часу сну, фільтрований вміст і стан правила (увімкнено або вимкнено).

    ![Додане правило](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/rules_added.png){class="glboxshadow"}

    Для наявних правил доступні основні операції: Modify, Copy і Delete.

    ![Операції з правилами](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action.png){class="glboxshadow"}

    - **Modify**: Зміна вибраних пристроїв, часу сну та правил фільтрації вмісту.

        ![Зміна правила](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_modify.png){class="glboxshadow"}

    - **Copy**: Створення копії наявного правила, щоб не налаштовувати його повторно вручну.

        ![Копіювання правила](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_copy.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
