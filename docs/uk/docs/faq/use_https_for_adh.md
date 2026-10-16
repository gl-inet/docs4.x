# Доступ до маршрутизатора GL.iNet і AdGuard Home через HTTPS {#access-glinet-router-and-adguard-home-via-https}

Для доступу до маршрутизатора GL.iNet та AdGuard Home через HTTPS виконайте наведені нижче дії.

## 1. Оновлення сертифіката й ключа на маршрутизаторі GL.iNet {#1-update-certificate-and-key-in-glinet-router}

Спочатку отримайте сертифікат SSL або використайте самопідписаний сертифікат SSL.

Підключіться до маршрутизатора GL.iNet через SSH або використайте WinSCP, щоб завантажити оновлені сертифікат і ключ. Шляхи до файлів:

`/etc/nginx/nginx.cer`

`/etc/nginx/nginx.key`

## 2. Увімкнення AdGuard Home {#2-enable-adguard-home}

Увійдіть у вебпанель адміністрування GL.iNet -> APPLICATIONS -> AdGuard Home та увімкніть AdGuard Home.

![Увімкнення AdGuard Home](https://static.gl-inet.com/docs/router/en/4/faq/SSL/enableadh.jpg){class="glboxshadow"}

Натисніть **Settings Page** угорі цієї сторінки, щоб відкрити налаштування AdGuard Home.

![Відкриття налаштувань AdGuard Home](https://static.gl-inet.com/docs/router/en/4/faq/SSL/gosettings.jpg){class="glboxshadow"}

## 3. Зміна налаштувань шифрування {#3-edit-encryption-settings}

На сторінці налаштувань AdGuard Home відкрийте Settings -> Encryption settings.

![Налаштування шифрування](https://static.gl-inet.com/docs/router/en/4/faq/SSL/encryption.jpg){class="glboxshadow"}

Установіть прапорець Enable Encryption угорі ліворуч і задайте 3001 у полі HTTPS port.

![Порт HTTPS 3001](https://static.gl-inet.com/docs/router/en/4/faq/SSL/3001.jpg){class="glboxshadow"}

Додайте шляхи до оновленого сертифіката та ключа й натисніть Save.

![Шляхи до сертифіката й ключа](https://static.gl-inet.com/docs/router/en/4/faq/SSL/addcertpath.jpg){class="glboxshadow"}

Після цього через HTTPS можна відкрити **192.168.8.1** або **192.168.8.1:3001**.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
