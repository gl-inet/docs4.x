# Modem USB nie działa prawidłowo na routerze GL.iNet

Niektóre routery GL.iNet mają porty USB, dzięki czemu użytkownicy mogą podłączyć modem USB do portu USB, aby skonfigurować dostęp do Internetu, a po połączeniu z innymi metodami dostępu do Internetu nawet zrealizować scenariusze Multi-WAN.

Może się jednak zdarzyć, że niektóre modemy USB (takie jak ZTE F50 Mobile Wi-Fi Hotspot) nie będą działać prawidłowo z routerem, powodując częste rozłączanie sieci.

Może to wynikać z problemu zgodności między portem USB routera (zwykle USB3.0) a siecią Wi-Fi 2.4G, co powoduje ciągłe rozłączanie modemu USB i brak prawidłowego dostępu do Internetu.

Aby rozwiązać ten problem, możesz przełączyć specyfikację portu USB z USB 3.0 na USB 2.0.

Przejdź do panelu administracyjnego routera GL.iNet i otwórz **SYSTEM -> Overview -> External Storage**. 

Zobaczysz opcję USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Przełącz ją na USB 2.0, a pojawi się komunikat pokazany poniżej. Kliknij Switch, aby kontynuować.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Gdy zobaczysz, że protokół USB ma wartość USB 2.0, oznacza to, że przełączenie zakończyło się powodzeniem.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Następnie sprawdź, czy połączenie internetowe działa lepiej.

---

Powiązane artykuły

- [Kompatybilne modemy](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
