# Firmware v4.9

Ta wersja koncentruje się na bardziej precyzyjnym sterowaniu siecią, usprawnionym zarządzaniu ruchem, zwiększonym bezpieczeństwie sieci i odświeżonym interfejsie użytkownika, aby zapewnić lepsze ogólne doświadczenie.

Najnowsze firmware można pobrać z [Firmware Download Center](https://dl.gl-inet.com/){target="_blank"}.

## Flow Control

Flow Control to kluczowy moduł zarządzania siecią, który umożliwia precyzyjną identyfikację, monitorowanie, regulowanie i filtrowanie ruchu sieciowego. Skutecznie optymalizuje przydział zasobów sieciowych, eliminuje przeciążenia pasma i standaryzuje zachowania związane z dostępem do sieci, zapewniając płynniejsze, bezpieczniejsze i łatwiejsze do kontrolowania działanie sieci. W firmware v4.9 moduł ten integruje wiele praktycznych funkcji, umożliwiając kompleksowe zarządzanie ruchem.

Moduł Flow Control obejmuje DPI Engine, Data Statistics, Content Filter, QoS, SQM i Parental Control.

### DPI Engine

W przeciwieństwie do tradycyjnych routerów, które identyfikują jedynie adres źródłowy i docelowy, DPI (Deep Packet Inspection) przeprowadza szczegółową analizę zawartości pakietów oraz dokładnie identyfikuje aplikacje i strony internetowe za pomocą biblioteki dopasowywania cech. Umożliwia to szczegółową klasyfikację i kontrolę ruchu.

![dpi](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dpi.png){class="glboxshadow"}

### Data Statistics

Data Statistics udostępnia intuicyjny panel ruchu, który przedstawia użycie sieci według aplikacji i protokołu. Umożliwia wyświetlanie trendów historycznych z 1 godziny, 1 dnia i 7 dni, prezentuje rankingi wykorzystania, monitoruje ruch poszczególnych urządzeń oraz pozwala jednym kliknięciem blokować niepożądane aplikacje.

![data stats](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/data_statistics.png){class="glboxshadow"}

### Content Filter

Content Filter to inteligentna funkcja bezpieczeństwa online wykorzystująca klasyfikację DPI. Automatycznie blokuje szkodliwe i złośliwe strony internetowe, pomagając utrzymać czystość i bezpieczeństwo sieci. Obsługuje również niestandardowe reguły blokowania określonych aplikacji, domen i adresów IP.

![content filter](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/blocked_apps.png){class="glboxshadow"}

### QoS

QoS (Quality of Service) optymalizuje przydział pasma, nadając priorytet ważnym aktywnościom, takim jak rozmowy wideo i gry, podczas przeciążenia sieci. Zmniejsza w ten sposób opóźnienia i poprawia ogólną wydajność sieci.

![qos](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/qos.png){class="glboxshadow"}

### SQM

SQM (Smart Queue Management) inteligentnie zarządza ruchem sieciowym routera, aby zminimalizować opóźnienia i „bufferbloat”, zapewniając płynniejsze działanie gier i połączeń głosowych.

![sqm](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/sqm.png){class="glboxshadow"}

### Parental Control

Ta funkcja, wcześniej dostępna w menu **Applications**, została przeniesiona w firmware v4.9 do menu **Flow Control**. Wykorzystuje ulepszony DPI Engine do dokładnego identyfikowania i blokowania nieodpowiednich aplikacji oraz treści sieciowych, zapewniając bardziej zaawansowane i precyzyjne ograniczenia dostępu oparte na ruchu.

![parental control](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/parental_control.png){class="glboxshadow"}

## VPN

W firmware v4.9 kompleksowo ulepszono bazową logikę routingu i interfejs modułu VPN. Usunięto potencjalne konflikty routingu, uproszczono logikę konfiguracji i zwiększono intuicyjność obsługi.

Najważniejsze zmiany opisano poniżej.

### Izolowany tunel VPN

Każdy tunel VPN działa jako niezależna grupa bez przełączenia awaryjnego między grupami. Gdy ruch sieciowy zostanie dopasowany do określonej grupy VPN, nie przełączy się automatycznie do innych grup VPN nawet w przypadku awarii bieżącego tunelu. Zapewnia to stabilny i przewidywalny routing ruchu.

**Uwaga**: W firmware v4.9 usunięto tradycyjną politykę „Not Use VPN”. Eliminuje to zbędną konfigurację i pomaga uniknąć konfliktów routingu powodowanych przez liczne, złożone reguły tuneli.

![vpn tunnels](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_tunnels.png){class="glboxshadow"}

### Przełączenie awaryjne profili VPN

Jedna grupa tuneli VPN może zawierać wiele profili konfiguracji. Użytkownicy mogą dostosować priorytet każdego profilu w tej samej grupie, co umożliwia automatyczne wewnętrzne przełączenie awaryjne i utrzymanie łączności VPN, gdy pojedynczy profil ulegnie awarii.

![profile failover](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/profile_failover.png){class="glboxshadow"}

### Przeprojektowany panel

VPN Dashboard został całkowicie przeprojektowany i ma bardziej intuicyjny układ. Stan tuneli, szczegóły połączeń i wpisy konfiguracji są prezentowane czytelniej, co znacznie usprawnia codzienną obsługę i zarządzanie. Ponadto w nowej architekturze Kill Switch jest domyślnie włączony dla wszystkich tuneli VPN, aby stale chronić ruch.

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/vpn_dashboard.png){class="glboxshadow"}

## AmneziaWG 2.0

Firmware v4.9 oficjalnie wprowadza protokół AmneziaWG 2.0 wyposażony w wiele nowych parametrów zaciemniania ruchu. Ulepszony protokół skutecznie omija wykrywanie przez DPI i inne systemy identyfikacji ruchu, znacznie zwiększając ukrywanie połączenia i odporność na zakłócenia. Umożliwia to ustanawianie stabilnych i niezawodnych połączeń VPN w regionach z ograniczeniami sieciowymi oraz w złożonych środowiskach sieciowych.

![amneziawg](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/amneziawg.png){class="glboxshadow"}

## Sieć IoT

W firmware v4.9 można utworzyć niezależną, dedykowaną sieć Wi-Fi dla inteligentnych urządzeń IoT. Dzięki fizycznej i logicznej izolacji od sieci głównej pozwala ona uniknąć zajmowania zasobów sieciowych i zagrożeń bezpieczeństwa wynikających z dostępu urządzeń IoT do sieci głównej. To rozwiązanie zapewnia szerszą zgodność z różnymi inteligentnymi klientami IoT i ogólnie wzmacnia bezpieczeństwo sieci domowej.

![iot network](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/iot_network.png){class="glboxshadow"}

## ACL

ACL, czyli Access Control List, to kluczowa funkcja zarządzania bezpieczeństwem sieci, która pozwala tworzyć niestandardowe reguły dostępu do zarządzania ruchem wewnętrznym i zewnętrznym na podstawie protokołów połączeń, adresów IP urządzeń i portów. Obsługuje precyzyjną kontrolę uprawnień, aby zezwalać na określone zachowania dostępu do sieci lub je blokować. Gdy wiele reguł ACL powoduje konflikty, system automatycznie wykonuje regułę o wyższym priorytecie, aby zapewnić prawidłowe wdrożenie polityki.

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl1.png){class="glboxshadow"}

![acl](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/acl2.png){class="glboxshadow"}

ACL różni się od Port Forwarding pod względem głównego zastosowania: ACL koncentruje się na zarządzaniu bezpieczeństwem sieci przez kontrolowanie uprawnień dostępu urządzeń i ruchu, natomiast Port Forwarding służy do przekierowywania zasobów sieciowych, przesyłając zewnętrzny ruch sieciowy do określonych lokalnych urządzeń końcowych w celu realizacji zdalnego dostępu do usług sieci lokalnej.

## Wireless UI

Interfejs Wireless został całkowicie przeprojektowany z użyciem uproszczonego układu i spójnego stylu wizualnego. Zmniejsza to złożoność obsługi i znacząco poprawia prostotę oraz wygodę korzystania z interfejsu.

![wireless](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/wireless.png){class="glboxshadow"}

## Szyfrowany DNS

Szyfrowany DNS został rozszerzony o obsługę większej liczby protokołów szyfrowania, w tym DoH, DoT i DoQ. Jednocześnie zintegrowano więcej oficjalnych dostawców DNS oraz dodano ręczną konfigurację niestandardowych szyfrowanych serwerów DNS, aby spełnić różne wymagania dotyczące bezpiecznego rozwiązywania domen.

![dns provider](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns1.png){class="glboxshadow"}

![dns encryption type](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/dns2.png){class="glboxshadow"}

## Tailscale Exit Node

Routery GL.iNet obsługują teraz działanie jako Tailscale Exit Node. Cały wychodzący ruch internetowy z urządzeń w Tailnet może być kierowany przez publiczny adres IP routera, co umożliwia ujednolicone i bezpieczne zarządzanie wyjściem sieciowym w całej sieci Tailscale. Szczegółowe informacje znajdziesz [tutaj](../interface_guide/tailscale.md#run-exit-node).

![tailscale exit node](https://static.gl-inet.com/docs/router/en/4/features_update/4.9/tailscale_exit_node.png){class="glboxshadow"}

---

Masz dodatkowe pytania? Odwiedź nasze [Community Forum](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
