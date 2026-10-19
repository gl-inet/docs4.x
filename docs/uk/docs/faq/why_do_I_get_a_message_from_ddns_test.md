# Чому з’являється повідомлення під час перевірки DDNS? {#why-do-i-get-a-message-from-ddns-test}

Під час перевірки DDNS на сторінці Dynamic DNS може з’явитися повідомлення, як показано нижче.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![Повідомлення перевірки DDNS](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Це не **попередження** або **помилка**, а нагадування про стан мережі маршрутизатора.

Такий результат зазвичай відображає місце маршрутизатора в мережі. Наприклад, повідомлення з’являється, якщо GL.iNet налаштовано як додатковий маршрутизатор домашньої мережі.

Воно не зникне навіть після налаштування перенаправлення портів на основному маршрутизаторі. Повідомлення лише вказує, що маршрутизатор перебуває за NAT.

Щоб надати доступ до служб через NAT, наприклад для віддаленого доступу, потрібні додаткові налаштування.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
