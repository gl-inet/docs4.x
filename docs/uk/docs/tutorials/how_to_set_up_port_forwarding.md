# Як налаштувати перенаправлення портів на основному маршрутизаторі? {#how-to-set-up-port-forwarding-on-your-primary-router}

Якщо ви налаштовуєте сервер на маршрутизаторі GL.iNet, наприклад [сервер OpenVPN](how_to_set_up_openvpn_server.md) або [сервер WireGuard](build_your_own_wireguard_home_server_with_two_glinet_routers.md), а GL.iNet підключено до основного маршрутизатора, налаштуйте перенаправлення портів на основному маршрутизаторі. Це забезпечить належний доступ до сервера.

Якщо між основним маршрутизатором і GL.iNet є інші маршрутизатори, налаштуйте перенаправлення портів на всіх цих проміжних маршрутизаторах.

## Підготовка {#preparation}

Перед налаштуванням перенаправлення портів рекомендовано **зарезервувати статичну IP-адресу** для GL.iNet на основному маршрутизаторі. Тоді GL.iNet завжди отримуватиме фіксовану IP-адресу.

Інакше після перезавантаження основного маршрутизатора або GL.iNet основний маршрутизатор може призначити GL.iNet нову адресу, через що правило перенаправлення портів не працюватиме.

Потім налаштуйте на основному маршрутизаторі перенаправлення портів для GL.iNet.

Кроки залежать від виробника та моделі маршрутизатора. Скористайтеся відповідним розділом нижче.

## Основний маршрутизатор GL.iNet {#using-a-glinet-router-as-your-primary-router}

Скористайтеся [цією інструкцією](../interface_guide/port_forwarding.md){target="_blank"}.

## Основний маршрутизатор іншого виробника {#using-another-router-brand-as-your-primary-router}

!!! note "Під час налаштування перенаправлення портів укажіть такі параметри"

    Надайте наведені нижче відомості. Назви параметрів можуть відрізнятися залежно від виробника та моделі.

    * **External port/Internal port:** Уведіть потрібний порт. Наприклад, порти за замовчуванням — **1194** для серверів OpenVPN і **51820** для серверів WireGuard.
    * **Protocol:** Виберіть **All** або **UDP/TCP**.
    * **Internal IP** (або **Host IP**): Уведіть IP-адресу WAN додаткового маршрутизатора або виберіть його з розкривного списку, якщо він доступний.

Нижче наведено покрокові інструкції для поширених виробників і моделей основних маршрутизаторів.

Якщо вашого виробника або моделі немає у списку, скористайтеся документацією маршрутизатора або зверніться до його служби підтримки.

### AT&T {#att}

* [NVG589](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010280/){target="_blank"}
* [Pace 5031](https://www.att.com/support/article/u-verse-high-speed-internet/KM1010292/){target="_blank"}
* [Pace 5268](https://www.att.com/support/article/u-verse-high-speed-internet/KM1123072/){target="_blank"}

### Comcast (Xfinity) {#comcast-xfinity}

* [Xfinity Gateway](https://www.xfinity.com/support/articles/xfi-port-forwarding){target="_blank"}

### TP-Link  {#tp-link}

* [Серія Deco](https://www.tp-link.com/us/support/faq/1797/){target="_blank"}
* [Серія бездротових маршрутизаторів](https://www.tp-link.com/us/support/faq/1379/){target="_blank"}

### Eero  {#eero}

Скористайтеся [цією інструкцією](https://support.eero.com/hc/en-us/articles/207908443-How-do-I-configure-port-forwarding){target="_blank"}.

### Linksys {#linksys}

Скористайтеся [цією інструкцією](https://support.linksys.com/kb/article/318-en/){target="_blank"}.

### Netgear  {#netgear}

Скористайтеся [цією інструкцією](https://kb.netgear.com/24290/How-do-I-add-a-custom-port-forwarding-service-on-my-NETGEAR-router){target="_blank"}.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
