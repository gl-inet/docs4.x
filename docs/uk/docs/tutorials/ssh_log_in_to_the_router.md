# Вхід до маршрутизатора через SSH {#ssh-log-in-to-the-router}

Secure Shell (SSH) — це криптографічний мережевий протокол для безпечної роботи мережевих служб у незахищеній мережі. Найвідоміше застосування SSH — віддалений вхід користувачів до комп’ютерних систем. Для підключення до сервера через SSH іноді потрібні базові інструменти. У цьому посібнику описано, як увійти до маршрутизаторів GL.iNet через SSH.

---

## Для користувачів Windows {#for-windows-user}

У Windows доступ до термінала маршрутизатора можна отримати через Windows Cmd, PowerShell, Bitvise або PuTTY.

### Використання Windows Cmd {#using-windows-cmd}

1. Відкрийте командний рядок

    Натисніть **Win** + **R** (клавішу Windows і клавішу R), щоб відкрити вікно Run. Введіть **cmd** і натисніть Enter.

    ![Командний рядок](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_1.png){class="glboxshadow gl-60-desktop"}

    Відкриється чорне вікно командного рядка.

    ![Командний рядок](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_2.jpg){class="glboxshadow"}

2. Увійдіть до маршрутизатора

    У вікні командного рядка введіть `ssh root@192.168.8.1` і натисніть Enter.

    ![Вхід як root через SSH у командному рядку](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_ssh_root.jpg){class="glboxshadow"}

    **Примітка**: 192.168.8.1 — це IP-адреса маршрутизатора за замовчуванням. Якщо ви її змінили, використовуйте свою IP-адресу.

    Потім введіть пароль адміністратора маршрутизатора та натисніть Enter. **З міркувань безпеки пароль не відображається на екрані**.

    ![Введення пароля в командному рядку](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_psw.jpg){class="glboxshadow"}

    Якщо пароль правильний, ви успішно ввійдете до маршрутизатора.

    ![Успішний вхід у командному рядку](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/cmd_login.png){class="glboxshadow"}

??? "Усунення несправностей"

    1. **Помилка: Connection timed out**
    
        Переконайтеся, що ваш пристрій (наприклад, ноутбук) підключено до маршрутизатора. Повторно підключіться до Wi-Fi або LAN-порту маршрутизатора й спробуйте ще раз.

    2. **Помилка: Permission denied**

        Переконайтеся, що ви вводите правильний пароль адміністратора. Якщо ви забули пароль, скиньте налаштування маршрутизатора, утримуючи кнопку RESET протягом 10 секунд.

### Використання PowerShell {#using-powershell}

1. Відкрийте Windows PowerShell

    Натисніть значок пошуку на панелі завдань, введіть **PowerShell**, виберіть **Windows PowerShell** і **запустіть його від імені адміністратора**.

    ![Запуск PowerShell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/run_as_administrator.png){class="glboxshadow gl-90-desktop"}

2. Увійдіть до маршрутизатора

    У вікні PowerShell введіть `ssh root@192.168.8.1` і натисніть Enter.

    ![Вхід як root через SSH у PowerShell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_ssh_root.jpg){class="glboxshadow gl-90-desktop"}

    **Примітка**: 192.168.8.1 — це IP-адреса маршрутизатора за замовчуванням. Якщо ви її змінили, використовуйте свою IP-адресу.

    Система запропонує підтвердити підключення. Введіть `yes` і натисніть Enter.

    ![Підтвердження підключення в PowerShell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_confirm.png){class="glboxshadow gl-90-desktop"}

    Вам буде запропоновано ввести пароль адміністратора маршрутизатора. Введіть правильний пароль і натисніть Enter. **З міркувань безпеки пароль не відображається на екрані**.
    
    ![Введення пароля в PowerShell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_psw.png){class="glboxshadow gl-90-desktop"}
    
    Після цього ви успішно ввійдете до термінала маршрутизатора.

    ![Успішний вхід у PowerShell](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_login.png){class="glboxshadow gl-90-desktop"}

??? "Усунення несправностей"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Це трапляється, якщо ключ безпеки маршрутизатора змінився (наприклад, після скидання до заводських налаштувань або оновлення прошивки) чи ви раніше підключалися до іншого маршрутизатора, через що перевірка ключа хоста не проходить.

        ![Попередження](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/powershell_warning.jpg){class="glboxshadow gl-90-desktop"}

        Щоб усунути проблему, відкрийте Провідник, перейдіть до `C:\Users\Administrator\.ssh` і знайдіть файл **known_hosts**.

        ![Файл known_hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/known_hosts.png){class="glboxshadow gl-90-desktop"}

        Двічі натисніть файл known_hosts і відкрийте його в Блокноті.

        ![Відкриття в Блокноті](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/open_notepad.png){class="glboxshadow"}

        Видаліть запис, що стосується IP-адреси маршрутизатора (наприклад, 192.168.8.1), і збережіть файл. Закрийте Провідник.

        ![Видалення запису з known_hosts](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/delete_known_hosts.png){class="glboxshadow gl-90-desktop"}

        Поверніться до PowerShell і знову виконайте команду `ssh root@192.168.8.1` для підключення до маршрутизатора. Коли з’явиться запит на підтвердження підключення, введіть `yes` і натисніть Enter, а потім введіть пароль для входу до маршрутизатора. Після цього ви успішно ввійдете до його термінала.

    2. **Що робити, якщо я змінив SSH-порт маршрутизатора?**
    
        Якщо ви змінили SSH-порт маршрутизатора, укажіть його за допомогою параметра «-p» у команді ssh. Наприклад:
        
        ``ssh -p [new port number] [username]@[router IP address]``

### Використання Bitvise {#using-bitvise}

Перегляньте це відео, щоб увійти до маршрутизатора через Bitvise.

<iframe width="560" height="315" src="https://www.youtube.com/embed/7yVd5UkKJ74" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Використання PuTTY {#using-putty}

1. Завантажте PuTTY

    Завантажте найновішу версію PuTTY за [цим посиланням](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html){target="blank"}.

2. Установіть PuTTY

    ![Установлення PuTTY 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_1.png){class="glboxshadow"}

    ![Установлення PuTTY 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_2.png){class="glboxshadow"}

    ![Установлення PuTTY 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_3.png){class="glboxshadow"}

    ![Установлення PuTTY 4](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/putty_install_4.png){class="glboxshadow"}

3. Запустіть PuTTY

    Виберіть **PuTTY** у меню «Пуск».

    ![Запуск PuTTY](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/launch_putty.png){class="glboxshadow"}

    Відкриється наведене нижче вікно налаштувань.

    ![Налаштування PuTTY 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_1.png){class="glboxshadow"}

    У полі Host Name (or IP address) введіть `192.168.8.1`, залиште значення Port за замовчуванням `22` і виберіть тип підключення `SSH`.

    У полі збережених сеансів введіть `Your Session` і натисніть `Save`, щоб зберегти налаштування.

    Потім натисніть `Open` унизу вікна.

    ![Налаштування PuTTY 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_2.png){class="glboxshadow"}

    З’явиться наведене нижче попередження безпеки. Натисніть `Yes`.

    ![Налаштування PuTTY 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/setup_putty_3.png){class="glboxshadow"}

    У запиті login as введіть `root`.

    Потім введіть пароль адміністратора. **З міркувань безпеки пароль не відображається на екрані**.

    ![Успішний вхід через SSH](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ar750s_ssh_successfully.jpg){class="glboxshadow"}

    Якщо ви бачите екран, показаний вище, ви успішно ввійшли до маршрутизатора через SSH.

---

## Для користувачів Linux/Mac {#for-linuxmac-user}

Процедура в Linux і Mac OS загалом однакова. Нижче наведено приклад для Ubuntu.

### Використання Ubuntu {#using-ubuntu}

1. Запустіть термінал.

    Запустіть Ubuntu. Двічі натисніть значок Terminal, щоб відкрити термінал.
    
    ![Запуск Ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_login.png){class="glboxshadow"}

2. Увійдіть до маршрутизатора.

    Введіть команду входу через SSH: `ssh root@192.168.8.1`

    ![Вхід до маршрутизатора через SSH в Ubuntu 1](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_1.png){class="glboxshadow"}

    Система запропонує підтвердити підключення. Введіть «yes» і натисніть Enter.

    ![Вхід до маршрутизатора через SSH в Ubuntu 2](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_2.png){class="glboxshadow"}

    Потім введіть пароль адміністратора маршрутизатора. **З міркувань безпеки пароль не відображається на екрані**.

    ![Вхід до маршрутизатора через SSH в Ubuntu 3](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/ubuntu_sshin_router_3.png){class="glboxshadow"}

    Якщо ви бачите екран, показаний вище, ви успішно ввійшли до маршрутизатора.

??? "Усунення несправностей"

    1. **WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!** / **Host key verification failed**

        Це трапляється, якщо ключ безпеки маршрутизатора змінився (наприклад, після скидання до заводських налаштувань або оновлення прошивки) чи ви раніше підключалися до іншого маршрутизатора, через що перевірка ключа хоста не проходить.

        ![Видалення ключа SSH за допомогою ssh-keygen](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/remove_ssh_keygen.png){class="glboxshadow gl-90-desktop"}

        У такому разі виконайте команду в червоній рамці вище. Скопіюйте саме ту команду, яку показано у вашому терміналі.

        `ssh-keygen -f ~/.ssh/known_hosts -R "192.168.8.1"`

        ![Видалений ключ хоста](https://static.gl-inet.com/docs/router/en/4/tutorials/ssh_log_in_to_the_router/removed_host_keygen.png){class="glboxshadow gl-90-desktop"}

        Потім спробуйте підключитися знову.

    2. **Unable to negotiate with 10.0.0.1 port 22: no matching host key type found. Their offer: ssh-rsa**
    
        Ця помилка може виникнути під час підключення через зміни в пакеті OpenSSH, починаючи з версії 8.8. Щоб усунути її, відкрийте файл **~/.ssh/config** у текстовому редакторі (наприклад, Nano або Vim) і додайте такі рядки:

            host 192.168.8.1
                HostkeyAlgorithms +ssh-rsa
                PubkeyAcceptedAlgorithms +ssh-rsa

        Якщо IP-адреса хоста відрізняється від адреси за замовчуванням, обов’язково змініть її.

        Обговорення цієї проблеми див. за [цим посиланням](https://forum.gl-inet.com/t/can-no-longer-ssh-into-router-no-matching-host-key-type-found-their-offer-ssh-rsa/20915){target="_blank"}.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
