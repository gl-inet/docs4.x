# Як спрямувати весь трафік через VPN? {#how-to-let-all-data-go-through-vpn}

Щоб весь мережевий трафік маршрутизатора проходив через VPN, а всі інтернет-з’єднання блокувалися у разі збою VPN, виконайте наведені нижче дії для увімкнення **VPN Kill Switch**.

**Примітка**: перед увімкненням аварійного блокування VPN (Kill Switch) спочатку налаштуйте клієнт VPN на маршрутизаторі GL.iNet.

## Для прошивки v4.7 і попередніх версій {#for-firmware-v47-or-earlier}

Увійдіть у вебпанель адміністрування маршрутизатора, відкрийте **VPN** -> **VPN Dashboard** -> **VPN Client** і натисніть **Global Options**.

![Глобальні параметри VPN](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-1.png){class="glboxshadow"}

Увімкніть **Block Non-VPN Traffic** (у деяких версіях прошивки цей параметр називається Kill Switch) і натисніть **Apply**.

![Блокування трафіку поза VPN](https://static.gl-inet.com/docs/router/en/4/faq/block_non_vpn_traffic/4.7-global-options-2.png){class="glboxshadow gl-80-desktop"}

**Примітка:** якщо Block Non-VPN Traffic / Kill Switch увімкнено, а VPN вимкнено або відключено, всі пристрої, підключені до маршрутизатора, втратять доступ до інтернету для запобігання витокам DNS.

## Для прошивки v4.8 і новіших версій {#for-firmware-v48-or-later}

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

All Other Traffic — тунель за замовчуванням, який забезпечує звичайний доступ до інтернету для трафіку, не охопленого тунелями VPN і політиками вище, а також для трафіку, який перейшов із з’єднань VPN унаслідок аварійного перемикання. Цей тунель увімкнено за замовчуванням і взаємовиключний з Enhanced Kill Switch.

**Примітка**: якщо вимкнути All Other Traffic, доступ до інтернету буде можливий лише через VPN. Увесь трафік, який не відповідає правилам тунелів, буде заблоковано. Цей параметр не перевизначає окремий Kill Switch кожного тунелю.

---

Маєте запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
