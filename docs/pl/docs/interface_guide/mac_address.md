# Adres MAC

Ten przewodnik dotyczy firmware v4.5 i starszych wersji.

Strona **MAC Address** nosiła wcześniej nazwę **MAC Clone** i od wersji v4.2 została przemianowana na **MAC Address**.

Od wersji v4.6 ustawienia adresu MAC dla interfejsów Ethernet i Repeater zostały przeniesione odpowiednio do [Ethernet Port](ethernet_port.md) oraz [Repeater](internet_repeater.md).

---

Po lewej stronie panelu administracyjnego WWW przejdź do **NETWORK** -> **MAC Address**.

Możesz sprawdzić domyślny adres MAC routera, sklonować adres MAC klienta, ręcznie wprowadzić adres MAC albo wygenerować losowy adres MAC.

Jeśli urządzenie obsługuje ustawienie wielu portów Ethernet jako portów WAN, możesz skonfigurować adres MAC osobno dla każdego portu. Pamiętaj, że ustawienie adresu MAC działa tylko wtedy, gdy port Ethernet jest używany jako port WAN.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* Fabryczny domyślny adres MAC.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Sklonowanie adresu MAC klienta.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Uwaga:** Wiele nowych urządzeń używa obecnie różnych losowych adresów MAC do łączenia się z różnymi sieciami Wi‑Fi, dlatego wyświetlany tutaj adres MAC może nie być rzeczywistym adresem MAC urządzenia użytkownika. Losowy adres MAC może być również nazywany Private Wi‑Fi Address lub random hardware address, zależnie od urządzenia.

* Ręczne wprowadzenie lub wygenerowanie losowego adresu MAC.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Scenariusze użycia

Podczas łączenia z publicznym hotspotem użyj losowego adresu MAC, jeśli nie chcesz, aby hotspot znał Twój rzeczywisty adres MAC lub ograniczał na jego podstawie dostęp do Internetu. Przeczytaj poradnik [Łączenie z hotspotem z captive portalem](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
