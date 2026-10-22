# GoodCloud Site to Site {#goodcloud-site-to-site}

## Вступ {#introduction}

GoodCloud Site to Site встановлює захищені інтернет-з’єднання між офісами в різних місцях. Функція розширює корпоративну мережу, надаючи працівникам інших офісів доступ до комп’ютерних ресурсів через спільну мережу.

![З’єднання між мережами](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Сценарій 1**: десятки філій однієї компанії потрібно об’єднати у приватну мережу для безперервного спільного використання ресурсів у всіх місцях.

**Сценарій 2**: дві партнерські компанії можуть співпрацювати у спільному захищеному мережевому середовищі через Site to Site.

**Сценарій 3**: у домашній мережі з IP-камерами Site to Site забезпечує віддалений доступ до пристроїв і моніторинг поза домом.

## Передумови {#conditions}

1. Для мережі Site to Site потрібні щонайменше два маршрутизатори GL.iNet.

2. Щонайменше один маршрутизатор повинен мати публічну IP-адресу, щоб працювати як головний вузол. [Перевірте, чи провайдер надає публічну IP-адресу](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    Для головного вузла краще вибрати маршрутизатор із високою продуктивністю та найкращою швидкістю мережі.

3. **НЕ** рекомендовано використовувати Site to Site, коли на додаткових вузлах одночасно працюють клієнт VPN / Tailscale / ZeroTier / AstroWarp. Це може значно ускладнити мережеву конфігурацію.

## Створення мережі Site to Site {#build-a-site-to-site-network}

1. Прив’яжіть маршрутизатори до облікового запису GoodCloud. Див. [Прив’язування пристроїв до хмари](../interface_guide/cloud.md#bind-devices-to-cloud).

2. Увійдіть у [GoodCloud](https://www.goodcloud.xyz/#/login){target="_blank"}, відкрийте **Site to Site** у лівому меню та натисніть **Create Network** у верхньому правому куті.

    ![Створення мережі](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Установіть прапорці ліворуч для вибору щонайменше двох пристроїв.

    ![Вибір пристроїв](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}

    Вибрані пристрої з’являться внизу сторінки.

    Порт Site to Site за замовчуванням — **51830**. Щоб змінити його, натисніть **Advanced** унизу ліворуч. Потім натисніть **Next**.

    ![Вибрані пристрої](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Для забезпечення стабільної роботи мережа Site to Site підтримує до 10 пристроїв.

4. Задайте назву мережі та натисніть **Next**.

    ![Назва мережі](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Розпочнеться Node Usability Testing для перевірки, чи може один із пристроїв працювати як Main Node.

    ![Перевірка придатності вузлів](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Якщо жоден пристрій не підходить для Main Node, перевірте такі умови:

    - Щонайменше один маршрутизатор має статичну або динамічну публічну IP-адресу.
    - Порт відкрито. Стандартний порт Site to Site — 51830. Спробуйте також змінити порт.
    - Якщо потрібний головний вузол перебуває за NAT, може знадобитися перенаправлення портів.

    ![Перевірка неуспішна](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Якщо головним вузлом можуть бути кілька пристроїв, виберіть один. Рекомендовано маршрутизатор із високою продуктивністю та найкращою швидкістю мережі.

    ![Перевірка успішна](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Якщо підходить лише один пристрій, одразу відкриється сторінка відомостей Site to Site.

6. За замовчуванням мережу вимкнено. Переконайтеся, що IP-адреси LAN всіх вузлів не конфліктують. За потреби змініть LAN IP через піктограму шестерні та натисніть **Start**.

    ![Стан мережі Site to Site](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Зачекайте кілька хвилин. Коли пунктирна лінія стане суцільною, мережу Site to Site встановлено успішно.

    ![Стан мережі Site to Site](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Перевірка з’єднання Site to Site {#testing-the-site-to-site-connection}

1. Підключіть комп’ютер або смартфон до одного з вузлів мережі Site to Site.

2. У браузері відкрийте LAN IP іншого вузла. Якщо сторінка входу доступна, з’єднання між вузлами працює.

## Маршрути та інші параметри {#route-and-other-options}

За замовчуванням кожен вузол має доступ до LAN інших вузлів. З міркувань безпеки рекомендовано відкривати лише IP-адреси потрібних сервісів.

Наприклад, у підмережі Node 1 є Server A (172.30.97.100). Щоб інші вузли мали доступ лише до Service A вузла Node 1, налаштуйте таке правило:

![IP-адреси LAN і маршрути](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Також можна додавати маршрути до мережі вищого рівня вузла.

Кожен додатковий вузол утворює шифрований тунель із головним вузлом. Щоб змінити IP-підмережу тунелю, натисніть **IP Address Range**.

Застосування нового діапазону IP-адрес спричинить відключення мережі на кілька хвилин.

![Діапазон IP-адрес тунелю](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
