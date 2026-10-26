# USB-модем працює некоректно на маршрутизаторі GL.iNet {#usb-modem-is-not-working-properly-on-glinet-router}

Деякі маршрутизатори GL.iNet мають порти USB для підключення USB-модема та налаштування доступу до інтернету. Разом з іншими способами доступу можна використовувати Multi-WAN.

Однак деякі USB-модеми, наприклад ZTE F50 Mobile Wi-Fi Hotspot, можуть працювати некоректно та спричиняти часті розриви мережевого з’єднання.

Причиною можуть бути проблеми сумісності між портом USB маршрутизатора (зазвичай USB3.0) і Wi-Fi 2.4G, через які модем постійно відключається та не забезпечує належний доступ до інтернету.

Для усунення проблеми змініть режим порту з USB 3.0 на USB 2.0.

У вебпанелі адміністрування маршрутизатора GL.iNet відкрийте **SYSTEM -> Overview -> External Storage**.

Відобразиться параметр USB Protocol Switch.

![Зовнішній накопичувач 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Виберіть USB 2.0. З’явиться повідомлення, показане нижче. Натисніть Switch, щоб продовжити.

![Зовнішній накопичувач 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Якщо відображається протокол USB 2.0, зміну виконано успішно.

![Зовнішній накопичувач 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Після цього перевірте, чи стало інтернет-з’єднання стабільнішим.

---

Пов’язані статті

- [Сумісні модеми](../interface_guide/internet_cellular.md#compatible-modems)

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
