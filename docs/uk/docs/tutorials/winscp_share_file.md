# Як отримати доступ до спільних файлів через WinSCP {#use-winscp-to-access-your-share-files}

За допомогою **WinSCP** можна отримати доступ до спільних файлів через функцію спільного доступу до файлів на **GL-Routers**.

Налаштуйте посилання **WebDAV** у розділі мережевого сховища. Докладніше див. [інструкцію з налаштування WebDAV](../interface_guide/network_storage.md#set-up-webdav).

## Налаштування посилань у WinSCP {#setup-links-in-winscp}

Після налаштування WebDAV поверніться на сторінку **Share Folders** мережевого сховища.

![Сторінка Share Folders](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav1.png){class="glboxshadow gl-80-desktop"}

Натисніть значок **"..."** правою кнопкою миші та скопіюйте посилання HTTPS.

![Копіювання посилання HTTPS](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav2.png){class="glboxshadow"}

Запустіть WinSCP, виберіть **WebDAV** і шифрування **TLS/SSL**. Потім вставте посилання в поле **Host name**. Номер порту автоматично зміниться на 6008.

![Налаштування WebDAV у WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav3.png){class="glboxshadow"}

Введіть ім’я користувача та пароль, збережіть налаштування й увійдіть. Відкриється спільна папка.

![Спільна папка у WinSCP](https://static.gl-inet.com/docs/router/en/4/tutorials/network_storage/webdav_client/webdav4.png){class="glboxshadow"}

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
