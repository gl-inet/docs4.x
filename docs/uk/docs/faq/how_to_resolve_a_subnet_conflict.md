# Як усунути конфлікт підмережі LAN? {#how-to-resolve-a-lan-subnet-conflict}

Після підключення кабелю Ethernet від домашнього маршрутизатора до порту WAN маршрутизатора GL.iNet іноді може з’явитися таке повідомлення:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![Повідомлення про конфлікт підмереж LAN і WAN](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Домашній маршрутизатор використовує ту саму IP-адресу LAN, що й маршрутизатор GL.iNet. Це спричиняє конфлікт LAN.

Виконайте наведені нижче дії, щоб змінити підмережу LAN.

## 1. Змініть підмережу LAN {#1-change-lan-subnet}

Натисніть посилання **Change LAN Subnet**, щоб відкрити сторінку налаштування **LAN**.

![Зміна IP-адреси LAN](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Змініть число після другої крапки (за замовчуванням — **8**) на інше. Наприклад, задайте 192.168.10.1 і натисніть **Apply**.

Зачекайте кілька секунд після зміни. Сторінка оновиться та автоматично відкриється за новою IP-адресою **192.168.10.1**. Повідомлення про конфлікт підмережі зникне.

Якщо автоматичне перенаправлення не відбулося, перейдіть до наступного кроку.

## 2. Увійдіть за новою IP-адресою LAN {#2-login-with-new-lan-ip}

Уведіть нову IP-адресу LAN в адресний рядок браузера та натисніть Enter.

![Вхід за новою IP-адресою LAN](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Увійдіть за допомогою пароля адміністратора. Повідомлення про конфлікт підмережі зникне.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
