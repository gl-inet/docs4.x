# Як змінювати файли на маршрутизаторах GL.iNet за допомогою WinSCP {#how-to-use-winscp-to-modify-files-on-glinet-routers}

WinSCP — простий інструмент для редагування, копіювання та завантаження файлів і каталогів маршрутизатора. Він дає змогу копіювати файли між локальним комп’ютером і маршрутизатором за допомогою протоколів передавання файлів FTP, SCP, SFTP, WebDAV або S3. Програма працює в операційній системі Windows.

---

1. Завантажте WinSCP [тут](https://winscp.net/eng/download.php){target="_blank"} і встановіть його у Windows.

2. Підключіться до маршрутизатора та запустіть WinSCP.

    ![Вхід через WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/login.png){class="glboxshadow"}

    * **File protocol**: виберіть протокол `SCP`.
    * **Host name**: введіть IP-адресу маршрутизатора. Якщо ви не змінювали її, це має бути `192.168.8.1`.
    * **Port number**: `22`
    * **Username & Password**: введіть `root` як ім’я користувача та свій пароль.

    Потім натисніть кнопку `Login`.

3. Після входу ви матимете повний контроль над маршрутизатором.

    Ви можете вибирати, переглядати, редагувати й передавати файли та каталоги з маршрутизатора або на нього.

    ![Панель WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/winscp_panel_marked.png){class="glboxshadow"}

    Наприклад, щоб змінити конфігурацію міжмережевого екрана, відкрийте /etc/config, знайдіть файл firewall, натисніть його правою кнопкою миші та виберіть **Edit**.

    ![Вибір файлу для редагування у WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_1.png){class="glboxshadow"}

    Тепер можна редагувати вміст файлу. Будьте обережні, щоб не пошкодити налаштування.

    ![Редагування файлу у WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/winscp/edit_2.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
