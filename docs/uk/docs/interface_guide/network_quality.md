# Якість мережі {#network-quality}

**Примітка**: цю функцію додано у прошивці v4.11.

---

У лівому меню вебпанелі адміністрування відкрийте **FLOW CONTROL** -> **Network Quality**.

Панель Network Quality відстежує якість інтернет-з’єднання в реальному часі. Вона оцінює швидкість реагування, затримку та роботу DNS, а також виявляє розриви з’єднання й втрати пакетів. Ці показники допомагають виявляти нестабільність мережі та проблеми зі з’єднанням, які звичайна перевірка пропускної здатності може не показати.

На цій сторінці можна оцінювати інтернет-з’єднання за показником Network Quality Score та за потреби запускати локальні перевірки швидкості.

**Примітка**:

1. Загальний показник GL.iNet Network Quality Score обчислюється за зваженою формулою:

    `Overall Score = Response Score × 60% + Reliable Score × 40%`.

2. Speedtest — це локальна перевірка швидкості на маршрутизаторі. На неї поширюються правила обмеження швидкості таких функцій, як SQM і QoS.

## Оцінка якості мережі {#network-quality-score}

У цьому розділі відображається загальний показник Network Quality Score, обчислений на основі Response Score і Reliable Score. Кожну оцінку можна переглядати окремо. Панель також показує затримку, джитер і втрати пакетів, а також поточні швидкості завантаження та передавання в KB/s. За замовчуванням для перевірок інтернет-з’єднання та визначення IP-адрес доменів через DNS використовується `google.com`.

Натисніть піктограму налаштувань, щоб задати адреси для перевірок.

![Налаштування адрес для перевірок](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting1.png){class="glboxshadow"}

Для Internet Reachability і DNS Resolution можна вибрати Baidu, Tencent, Alibaba, Google, Microsoft або Cloudflare. Також можна вручну ввести власний домен.

Задані адреси використовуються для перевірок з’єднання та DNS і обчислення показника Network Quality Score.

![Вибір адрес для перевірок](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/probe_targets_setting2.png){class="glboxshadow"}

- **Internet Reachability Target**: адреса для перевірки доступу до інтернету та вимірювання затримки між кінцевими вузлами (ціль ping Hop2).

- **DNS Resolution Target**: домен, адреса якого визначається під час перевірок DNS. Виконуються запити записів A(IPv4) і AAAA(IPv6).

## Speedtest {#speedtest}

Вбудована перевірка швидкості використовує Cloudflare Speed Test для вимірювання швидкості завантаження й передавання, затримки ping та затримки через надмірну буферизацію (bufferbloat). Під час перевірки графіки швидкості відображаються в реальному часі.

Натисніть **Run Speedtest**, щоб розпочати перевірку швидкості.

![Запуск перевірки швидкості](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_1.png){class="glboxshadow"}

Після завершення перевірки на сторінці з’являться результати.

![Результати перевірки швидкості](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_quality/speedtest_2.png){class="glboxshadow"}

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
