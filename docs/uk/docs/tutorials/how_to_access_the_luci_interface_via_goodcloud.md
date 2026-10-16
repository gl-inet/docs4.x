# Доступ до LuCI через GoodCloud {#how-to-access-the-luci-interface-via-goodcloud}

GL.iNet [GoodCloud](https://www.goodcloud.xyz/){target="_blank"} надає зручне віддалене керування маршрутизаторами незалежно від місця перебування. Через GoodCloud можна відкривати LuCI, змінювати налаштування маршрутизатора та керувати мережею.

## Підготовка {#preparation}

- Обладнання: маршрутизатор GL.iNet із налаштованим інтернет-доступом, який працює належним чином.
- Мережа: стабільне з’єднання з належним доступом до інтернету.
- Прив’язування: [прив’яжіть маршрутизатор GL.iNet до облікового запису GoodCloud](../interface_guide/cloud.md/#setup-your-goodcloud-account). Якщо облікового запису немає, [зареєструйте його](https://www.goodcloud.xyz/){target="_blank"}.

## Дії для доступу до LuCI через GoodCloud {#steps-to-access-the-luci-interface-via-goodcloud}

### Для прошивки 4.7 і новіших версій {#for-firmware-version-47-or-above}

Починаючи з v4.7, LuCI можна відкрити безпосередньо через GoodCloud, без переходу до вебпанелі адміністрування маршрутизатора.

1. Увійдіть у GoodCloud за [цим посиланням](https://www.goodcloud.xyz/){target="_blank"}.

2. У лівому меню відкрийте **Devices** -> **Bound Devices** і натисніть назву потрібного пристрою. Відобразяться піктограми Remote Web Access.

    ![Віддалений вебдоступ](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_mt6000.png){class="glboxshadow"}

    У спливному вікні вказано порт 80. Змініть його на **8080** та натисніть Apply.

    ![Зміна порту](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/change_port.png){class="glboxshadow"}

3. Відкриється сторінка входу LuCI. Введіть пароль адміністратора.

    ![Вхід до LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

4. Вхід до LuCI виконано успішно.

    ![Інтерфейс LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci_mt6000.png){class="glboxshadow"}

### Для прошивки 4.6 і попередніх версій {#for-firmware-version-46-or-below}

1. Увійдіть у GoodCloud за [цим посиланням](https://www.goodcloud.xyz/){target="_blank"}.

2. У лівому меню відкрийте **Devices** -> **Bound Devices** і натисніть назву потрібного пристрою. Відобразяться піктограми Remote Web Access.

    ![Віддалений вебдоступ](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/remote_gui_of_bound_device.png){class="glboxshadow"}

    У спливному вікні вказано порт 80. Натисніть Apply.

    ![Підтвердження вебдоступу](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/visit_web_apply.png){class="glboxshadow"}

3. Відкриється сторінка входу до вебпанелі адміністрування GL.iNet. Введіть пароль адміністратора.

    ![Вхід до вебпанелі адміністрування](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/admin_panel_login.png){class="glboxshadow"}

4. Після входу відкрийте SYSTEM -> Advanced Settings у лівому меню та натисніть посилання для переходу до LuCI.

    ![Додаткові налаштування](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/advanced_settings.png){class="glboxshadow"}

    Відкриється сторінка входу LuCI. Введіть той самий пароль адміністратора.

    ![Вхід до LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/log_in_luci.png){class="glboxshadow gl-80-desktop"}

5. Вхід до LuCI виконано успішно.

    ![Інтерфейс LuCI](https://static.gl-inet.com/docs/router/en/4/tutorials/access_luci_via_goodcloud/luci_interface_example.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
