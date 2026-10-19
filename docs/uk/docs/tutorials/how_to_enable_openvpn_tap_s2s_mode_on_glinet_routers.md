# Як увімкнути режим OpenVPN TAP-S2S на маршрутизаторах GL.iNet? {#how-to-enable-openvpn-tap-s2s-mode-on-glinet-routers}

## Сценарії використання {#usage-scenarios}

Після ввімкнення режиму TAP-S2S пристрій із клієнтом OpenVPN може віддалено отримувати доступ до пристрою із сервером OpenVPN, і навпаки. Однак у цьому режимі власні правила VPN, налаштовані на пристрої з клієнтом OpenVPN, не діють.

## Порівняння режимів TAP-S2S і TUN {#tap-s2s-vs-tun-mode}

Топологія мережі

![Топологія TAP-S2S](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tap_s2s_topology.png){class="glboxshadow"}

![Топологія TUN](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tun_topology.png){class="glboxshadow"}

У режимах TAP-S2S і TUN використовується однаковий спосіб фізичного підключення, але логічні з’єднання відрізняються:

1. Коли пристрої в локальній мережі GL-X3000 отримують доступ до панелі керування GL-MT6000, у режимі TAP-S2S віртуальна IP-адреса не використовується, а в режимі TUN — використовується.
2. Коли пристрої в локальній мережі GL-X3000 отримують доступ до панелі керування GL-X3000, у режимі TAP-S2S використовується віртуальна IP-адреса, а в режимі TUN — ні.
3. Якщо пристрою в локальній мережі GL-X3000 відома IP-адреса пристрою в локальній мережі GL-MT6000, режим TAP-S2S дає змогу отримати до нього прямий віддалений доступ. У режимі TUN для прямого доступу потрібно ввімкнути додаткові налаштування.
4. У режимі TAP-S2S GL-X3000 отримує доступ до інтернету через GL-MT6000, тоді як у режимі TUN Gl-X3000 може підключатися до інтернету безпосередньо. Тому в режимі TAP-S2S правила VPN, налаштовані на GL-X3000, не діють: натомість застосовуються правила VPN маршрутизатора GL-MT6000.

## Інструкції з налаштування {#tutorials}

Спочатку на маршрутизаторі з публічною IP-адресою (у цьому прикладі — GL-MT6000) відкрийте розділ **OpenVPN Server**. Установіть режим пристрою **TAP-S2S**, натисніть **Apply**, а потім **Export Client Configuration**.

![Вибір режиму TAP-S2S](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_mode.png){class="glboxshadow"}

![Експорт конфігурації клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_export.png){class="glboxshadow"}

На іншому маршрутизаторі з публічною IP-адресою (у цьому прикладі — GL-X3000) відкрийте розділ клієнта OpenVPN. Імпортуйте файл конфігурації, завантажений на попередньому кроці, натисніть **Apply** і ввімкніть клієнт.

![Вибір файлу конфігурації](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_select_file.png){class="glboxshadow"}

![Увімкнення клієнта OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_start.png){class="glboxshadow"}

Після цього IP-адреса маршрутизатора GL-X3000 зміниться. Щоб знайти нову адресу GL-X3000, увійдіть до панелі керування GL-MT6000 і відкрийте **Clients**.

![Нова IP-адреса клієнта](https://static.gl-inet.com/docs/router/en/4/tutorials/tap_s2s_vs_tun/tutorials_new_IP_address.png){class="glboxshadow"}

Якщо GL-MT6000 втратить мережеве з’єднання або на ньому буде вимкнено сервер OpenVPN, чи якщо на GL-X3000 буде вимкнено клієнт OpenVPN, IP-адреса GL-X3000 повернеться до попереднього значення.

Зверніть увагу:

- Обидва пристрої потрібно оновити до версії v4.5, інакше вони не зможуть підключитися.
- TAP-S2S працює лише в режимі **Global Proxy Mode**; налаштування автоматично змінюється після ввімкнення OpenVPN.
- Після ввімкнення цієї функції недоступні: сервер VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Tor, Firewall, Multi-WAN, LAN, DNS, Network Mode, IPv6, MAC Address, Drop-in Gateway, IGMP Snooping тощо.

---

Залишилися запитання? Відвідайте наш [форум спільноти](https://forum.gl-inet.com){target="_blank"} або [зв’яжіться з нами](https://www.gl-inet.com/contacts/){target="_blank"}.
