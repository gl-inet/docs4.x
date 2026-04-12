# IPv6

IPv6 (Internet Protocol version 6) to najnowsza wersja protokołu internetowego, zaprojektowana jako następca IPv4. Oferuje znacznie większą pulę unikalnych adresów IP, rozwiązując problem wyczerpywania się adresów IPv4 i wspierając rosnącą na całym świecie liczbę podłączonych urządzeń.

Po lewej stronie panelu administracyjnego WWW przejdź do **NETWORK** -> **IPv6**.

Ta strona umożliwia włączenie i skonfigurowanie IPv6 na routerze.

![ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6.png){class="glboxshadow"}

Po włączeniu IPv6 interfejsy WAN, takie jak Ethernet, będą pobierać swoje adresy IPv6 przez DHCPv6. Adres IPv6 możesz też zmienić ręcznie na stronie ustawień Ethernet.

**Uwaga**: Niektóre funkcje, na przykład firewall, GoodCloud i OpenVPN DCO, nie obsługują jeszcze IPv6. Jeśli korzystasz z tych funkcji i jednocześnie z IPv6, prawdopodobnie spowoduje to problemy z łącznością.

Włącz przełącznik **Enable IPv6**, wybierz tryb dla sieci głównej oraz metodę pobierania DNS, a następnie kliknij **Apply**.

![ipv6 enabled](https://static.gl-inet.com/docs/router/en/4/tutorials/ipv6/ipv6_enabled.png){class="glboxshadow"}

**Mode**: Dostępne są cztery tryby: **Native**, **Passthrough**, **NAT6** i **Static IPv6**.

- **Native**: Ten tryb ma zastosowanie, gdy router bezpośrednio pobiera publiczny adres IPv6, a następnie automatycznie przydziela adresy IPv6 urządzeniom w sieci. Tryb ten spełnia potrzeby związane z dostępem do IPv6 większości użytkowników.

- **Passthrough**: Ten tryb ma zastosowanie wtedy, gdy pakiety IPv6 muszą być przekazywane bezpośrednio, bez przetwarzania ani konwersji. Na przykład niektóre specjalistyczne aplikacje lub usługi sieciowe mogą wymagać pełnego zachowania zawartości pakietów IPv6 do dalszego przetwarzania lub analizy, co bywa wykorzystywane przez personel techniczny podczas debugowania sieci lub analizy bezpieczeństwa.

- **NAT6**: Ten tryb jest odpowiedni w scenariuszach, w których router jest używany jako brama zarządzająca do przydzielania dynamicznych wewnętrznych adresów IPv6 każdemu urządzeniu w sieci. W tym trybie urządzenia końcowe łączą się przez Optical Network Terminal i otrzymują adres IPv6 sieci lokalnej.

- **Static IPv6**: Ten tryb jest odpowiedni dla urządzeń lub usług wymagających stałego adresu IPv6, takich jak serwery lub drukarki sieciowe. Zapewnia, że urządzenie zawsze używa tego samego adresu IPv6, co ułatwia zarządzanie i dostęp.

**DNS acquisition method**: Określa, w jaki sposób router pobiera adresy serwerów DNS dla IPv6. Dostępne są dwie opcje: **Automatic** i **Manual**.

- **Automatic**: Router będzie dynamicznie pobierał adresy serwerów DNS dla IPv6, na przykład przez DHCPv6.

- **Manual**: Wprowadź własne adresy serwerów DNS dla IPv6. Ponieważ DNS służy do tłumaczenia nazw domen na odpowiadające im adresy IP, ręczna konfiguracja serwerów DNS może prowadzić do niepowodzeń w rozwiązywaniu nazw. Korzystaj z tej opcji ostrożnie.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
