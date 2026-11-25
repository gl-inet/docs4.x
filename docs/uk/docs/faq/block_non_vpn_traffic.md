# Як спрямувати весь трафік через VPN? {#how-to-let-all-data-go-through-vpn}

Щоб весь мережевий трафік маршрутизатора проходив через VPN, а всі інтернет-з’єднання блокувалися у разі збою VPN, виконайте наведені нижче дії для увімкнення **VPN Kill Switch**.

**Примітка**: перед увімкненням аварійного блокування VPN (Kill Switch) спочатку налаштуйте клієнт VPN на маршрутизаторі GL.iNet.

## Для прошивки v4.7 і попередніх версій {#for-firmware-v47-or-earlier}

Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте **VPN** -> **VPN Dashboard** -> **VPN Client** і натисніть **Global Options**.

![Глобальні параметри VPN](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Увімкніть **Block Non-VPN Traffic** (у деяких версіях прошивки цей параметр називається Kill Switch) і натисніть **Apply**.

![Блокування трафіку поза VPN](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Примітка:** якщо Block Non-VPN Traffic / Kill Switch увімкнено, а VPN вимкнено або відключено, всі пристрої, підключені до маршрутизатора, втратять доступ до інтернету для запобігання витокам DNS.

## Для прошивки v4.8 {#for-firmware-v48}

У прошивці v4.8 аварійне блокування VPN розділено на два режими.

- **Tunnel Kill Switch**: увімкнено за замовчуванням після активації відповідного тунелю VPN.

- **Enhanced Kill Switch (in Policy Mode)**: вимкнено за замовчуванням, щоб трафік, який не охоплено тунелями VPN і політиками вище, міг отримувати доступ до інтернету. Це зберігає звичайний доступ до інтернету для трафіку поза VPN.

### Аварійне блокування тунелю {#tunnel-kill-switch}

У вебпанелі адміністрування маршрутизатора відкрийте **VPN** -> **VPN Dashboard**.

Якщо маршрутизатор налаштовано як клієнт VPN, Kill Switch цього тунелю увімкнено за замовчуванням після активації VPN.

![Аварійне блокування VPN у глобальному режимі](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Global Mode)</small>

![Аварійне блокування VPN у режимі політик](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-policy-mode-killswitch.png){class="glboxshadow"}
<small>(VPN Policy Mode)</small>

Натисніть піктограму шестерні біля назви тунелю, щоб відкрити **Tunnel Options**.

![Відкриття параметрів тунелю](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options1.png){class="glboxshadow"}

Kill Switch цього тунелю увімкнено за замовчуванням.

![Аварійне блокування тунелю](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-global-mode-options2.png){class="glboxshadow"}

### Розширене аварійне блокування {#enhanced-kill-switch}

Ця функція доступна в режимі політик (Policy Mode).

У вебпанелі адміністрування відкрийте **VPN** -> **VPN Dashboard**, виберіть **Policy Mode** і знайдіть розділ **All Other Traffic** унизу. Його вигляд може дещо відрізнятися залежно від версії прошивки.

![Увесь інший трафік](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.8-all-other-traffic.png){class="glboxshadow"}

**All Other Traffic** є тунелем за замовчуванням. Він забезпечує звичайний доступ до інтернету для трафіку, який не відповідає жодному з наведених вище тунелів VPN чи політик, і для трафіку, перенаправленого сюди під час аварійного перемикання VPN. Тунель увімкнено за замовчуванням. Якщо його вимкнути, увесь такий трафік буде заблоковано, зокрема трафік, який інакше перенаправлявся б сюди в разі збою VPN. Доступ до інтернету матиме лише трафік, який проходить через налаштовані тунелі VPN. Такий самий захист забезпечує **Enhanced Kill Switch**.

**Примітка:** Параметр **All Other Traffic** не перевизначає аварійне блокування окремих тунелів.

## Для прошивки v4.9 і новіших версій {#for-firmware-v49-and-above}

У прошивці v4.9 і новіших версіях доступні два види аварійного блокування VPN: **Tunnel Kill Switch** і **Enhanced Kill Switch**.

### Аварійне блокування тунелю {#for-firmware-v49-and-above-tunnel-kill-switch}

У вебпанелі адміністрування маршрутизатора відкрийте **VPN** -> **VPN Dashboard**.

Якщо маршрутизатор налаштовано як клієнт VPN, Kill Switch цього тунелю увімкнено за замовчуванням після активації VPN.

![tunnel kill switch](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-kill-switch.png){class="glboxshadow"}

Натисніть піктограму шестерні біля назви тунелю, щоб відкрити **Tunnel Options**.

![tunnel options 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-1.png){class="glboxshadow"}

Kill Switch цього тунелю увімкнено за замовчуванням.

![tunnel options 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-tunnel-options-2.png){class="glboxshadow" width=600}

### Розширене аварійне блокування {#for-firmware-v49-and-above-enhanced-kill-switch}

У вебпанелі адміністрування маршрутизатора перейдіть до **VPN** -> **VPN Dashboard** і натисніть піктограму шестерні в правому верхньому куті.

![all other traffic 1](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-1.png){class="glboxshadow"}

Для політики трафіку доступні два параметри: **Allow Non-VPN Traffic** і **Enhanced Kill Switch**.

![all other traffic 2](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.9-all-other-traffic-2.png){class="glboxshadow" width=600}

- **Allow Non-VPN Traffic**: Увімкнено за замовчуванням. Цей параметр забезпечує звичайний доступ до інтернету для трафіку, який не відповідає жодному з наведених вище тунелів VPN чи політик, і для трафіку, перенаправленого сюди під час аварійного перемикання VPN.

- **Enhanced Kill Switch**: Якщо цю функцію ввімкнено, усі пристрої можуть отримувати доступ до інтернету лише через VPN. Трафік, який не відповідає жодному тунелю VPN, блокується. Цей параметр не перевизначає аварійне блокування окремих тунелів VPN.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
