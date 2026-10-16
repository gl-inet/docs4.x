# Пересилання SMS {#sms-forwarding}

Стільникові маршрутизатори GL.iNet підтримують пересилання SMS, автоматично надсилаючи вхідні повідомлення вказаним одержувачам.

**Примітка**: Ця функція працює лише на стільникових маршрутизаторах GL.iNet з оригінальним модулем 4G LTE/5G NR і не підтримується з іншими модулями або будь-якими іншими USB-модулями.

## Підтримувані моделі {#supported-models}

??? "Підтримувані моделі"
    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)

??? "Непідтримувані моделі"
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)

## Швидке налаштування {#quick-setup}

Розглянемо налаштування на прикладі GL-XE3000 (Puli AX).

1. Спочатку налаштуйте стільниковий маршрутизатор за [цим посібником](../interface_guide/internet_cellular.md).

2. Увійдіть до вебпанелі адміністрування маршрутизатора та перейдіть до **INTERNET** -> **Cellular**. Натисніть значок конверта у верхньому правому куті, щоб відкрити сторінку SMS із налаштуваннями пересилання повідомлень.

    ![Налаштування SMS](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms.png){class="glboxshadow"}

### Пересилання електронною поштою {#forward-via-email}

![Пересилання SMS електронною поштою](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_email.png){class="glboxshadow"}

- **SMTP Server Address**: У розкривному списку доступні попередньо задані адреси серверів Gmail, Outlook, iCloud і Yahoo. Для інших поштових сервісів зверніться до їхньої документації або служби підтримки.

- **Encryption Method**: Доступні три варіанти: none, SSL/TLS і STARTTLS.
- **Username**: Введіть адресу електронної пошти.
- **Password**: Використовуйте пароль програми або пароль облікового запису. Для Gmail, Outlook, iCloud і Yahoo див. інструкції нижче.
- **Subject**: Укажіть тему листа.

??? "Gmail"

    Для Gmail увійдіть до свого облікового запису Google і створіть **App Passwords**. Див. офіційний посібник [Вхід за допомогою паролів програм](https://support.google.com/accounts/answer/185833?hl=en){target="_blank"}. Перед створенням пароля програми потрібно ввімкнути двоетапну перевірку.

    Можна використовувати як порт 465, так і порт 587.

??? "Outlook"

    Outlook підтримує порт 587. Вимоги до автентифікації SMTP для свого облікового запису уточніть в офіційному посібнику [Налаштування POP, IMAP і SMTP для Outlook.com](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040){target="_blank"}.

??? "iCloud"

    Для входу в iCloud потрібно створити пароль програми; підтримується порт 587. Див. офіційні посібники [Налаштування сервера iCloud Mail для інших поштових програм](https://support.apple.com/en-hk/HT202304){target="_blank"} і [Створення пароля програми](https://support.apple.com/en-gb/HT204397){target="_blank"}.

??? "Yahoo"

    Для входу в Yahoo потрібно налаштувати пароль програми; підтримуються порти 465 і 587. Див. офіційні посібники [Налаштування та інструкції щодо доступу POP до Yahoo Mail](https://help.yahoo.com/kb/SLN4724.html){target="_blank"} і [Створення та керування паролями для сторонніх програм](https://help.yahoo.com/kb/SLN15241.html){target="_blank"}.

**Примітка**: Для кожного відправника можуть діяти обмеження на надсилання через SMTP, наприклад добовий ліміт кількості листів. Уточніть це у свого постачальника послуг.

Можна додати до 10 адрес електронної пошти.

### Пересилання через SMS {#forward-via-sms}

![Пересилання SMS на телефон](https://static.gl-inet.com/docs/router/en/4/tutorials/sms_forwarding/sms_forward_phone.png){class="glboxshadow"}

Виберіть код країни, введіть номер телефону та натисніть Apply.

Можна додати до 10 номерів мобільних телефонів.

---

Пов’язані статті

- [SMS](sms.md)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
