# Firmware v4.9

Ta wersja koncentruje się na bardziej precyzyjnym sterowaniu siecią, usprawnionym zarządzaniu ruchem, zwiększonym bezpieczeństwie sieci i odświeżonym interfejsie użytkownika, aby zapewnić lepsze ogólne doświadczenie. [Centrum pobierania firmware](https://dl.gl-inet.com/){target="_blank"}

## Flow Control

Flow Control to kluczowy moduł zarządzania siecią, który umożliwia precyzyjną identyfikację, monitorowanie, regulowanie i filtrowanie ruchu sieciowego. Optymalizuje przydział zasobów sieciowych, eliminuje przeciążenia pasma i standaryzuje zachowania dostępu do sieci, zapewniając płynniejsze, bezpieczniejsze i łatwiejsze do kontrolowania działanie sieci. W firmware v4.9 moduł ten integruje się z wieloma praktycznymi funkcjami, zapewniając kompleksowe zarządzanie ruchem.

Moduł Flow Control obejmuje następujące funkcje:

!!! note "DPI Engine"
    
    Technologia Deep Packet Inspection do dokładnej identyfikacji protokołów aplikacji, typów ruchu i zachowań sieciowych.

!!! note "Statystyki danych"
    
    Zbieranie, analiza i wizualizacja danych o ruchu sieciowym w czasie rzeczywistym i w ujęciu historycznym, ułatwiające intuicyjne monitorowanie stanu sieci.

!!! note "Filtrowanie treści"
    
    Inteligentne przechwytywanie i filtrowanie nieodpowiednich treści sieciowych w celu standaryzacji dostępu do sieci.

!!! note "QoS (Quality of Service)"
    
    Przydział pasma i harmonogram priorytetów ruchu w celu zagwarantowania jakości sieci dla kluczowych aplikacji.

!!! note "SQM (Smart Queue Management)"
    
    Optymalizuje harmonogram kolejek sieciowych, aby zmniejszyć opóźnienia i utratę pakietów oraz zapewnić płynniejszą transmisję sieciową.

!!! note "Kontrola rodzicielska"
    
    Ta funkcja, wcześniej sklasyfikowana w menu **Applications**, została przeniesiona w v4.9 do menu **Flow Control**. Wykorzystuje zaktualizowany DPI Engine do dokładnego identyfikowania i blokowania nieodpowiednich aplikacji oraz treści sieciowych, zapewniając bardziej profesjonalne i precyzyjne ograniczenia dostępu oparte na ruchu.

## VPN

Firmware v4.9 kompleksowo ulepsza bazową logikę routingu i interaktywny interfejs modułu VPN. Usuwa potencjalne konflikty routingu, upraszcza logikę konfiguracji i zwiększa intuicyjność obsługi.
    
Szczegółowe zmiany są następujące:

!!! note "Niezależne grupowanie VPN"

    Każdy tunel VPN działa jako niezależna grupa bez przełączenia awaryjnego między grupami. Gdy ruch sieciowy pasuje do określonej grupy VPN, nie zostanie automatycznie przełączony do innych grup VPN nawet w przypadku awarii bieżącego tunelu. Zapewnia to stabilny i przewidywalny routing ruchu.

!!! note "Przełączenie awaryjne profili w grupie"
    
    Jedna grupa tuneli VPN może zawierać wiele profili konfiguracji. Użytkownicy mogą dostosować priorytet każdego profilu w tej samej grupie, co umożliwia automatyczne wewnętrzne przełączenie awaryjne i utrzymanie łączności VPN, gdy pojedynczy profil ulegnie awarii.
    
!!! note "Usunięto politykę \"Not Use VPN\""
    
    Tradycyjna opcja "Not Use VPN" w konfiguracji polityk VPN została usunięta w v4.9. Eliminuje to zbędne wpisy konfiguracji i skutecznie zapobiega złożonym konfliktom logiki routingu powodowanym przez wiele ustawień polityk.
    
!!! note "Przeprojektowany VPN Dashboard"
        
    VPN Dashboard został całkowicie przeprojektowany i ma bardziej intuicyjny układ. Wyraźniej pokazuje stan tuneli, informacje o połączeniu i wpisy konfiguracji, co znacząco usprawnia codzienną obsługę i zarządzanie.

## Protokół AmneziaWG 2.0

Firmware v4.9 oficjalnie wprowadza protokół AmneziaWG 2.0 wyposażony w wiele nowych parametrów zaciemniania ruchu. Ulepszony protokół skutecznie omija wykrywanie przez DPI i inne systemy identyfikacji ruchu, znacznie zwiększając ukrywanie połączenia i odporność na zakłócenia. Umożliwia to ustanawianie stabilnych i niezawodnych połączeń VPN w regionach z ograniczeniami sieciowymi oraz w złożonych środowiskach sieciowych.

## Sieć IoT

Nowa funkcja sieci IoT umożliwia utworzenie niezależnej, dedykowanej sieci Wi-Fi dla inteligentnych urządzeń IoT. Dzięki fizycznej i logicznej izolacji od sieci głównej pozwala uniknąć zajmowania zasobów sieciowych i ryzyk bezpieczeństwa wynikających z dostępu urządzeń IoT do głównej sieci. Ta optymalizacja zapewnia szerszą zgodność z różnymi inteligentnymi klientami IoT i ogólnie wzmacnia bezpieczeństwo sieci domowej.

## ACL (Access Control List)

ACL, czyli Access Control List, to kluczowa funkcja zarządzania bezpieczeństwem sieci, która pozwala tworzyć niestandardowe reguły dostępu do zarządzania ruchem wewnętrznym i zewnętrznym na podstawie protokołów połączeń, adresów IP urządzeń i portów. Obsługuje precyzyjną kontrolę uprawnień, aby zezwalać na określone zachowania dostępu do sieci lub je blokować. Gdy wiele reguł ACL powoduje konflikty, system automatycznie wykonuje regułę o wyższym priorytecie, aby zapewnić prawidłowe wdrożenie polityki.

ACL różni się od Port Forwarding pod względem głównego zastosowania: ACL koncentruje się na zarządzaniu bezpieczeństwem sieci przez kontrolowanie uprawnień dostępu urządzeń i ruchu, natomiast Port Forwarding służy do przekierowywania zasobów sieciowych, przesyłając zewnętrzny ruch sieciowy do określonych lokalnych urządzeń końcowych w celu realizacji zdalnego dostępu do usług sieci lokalnej.

## Inne ulepszenia

!!! note "Przeprojektowanie interfejsu Wireless"
    
    Interfejs ustawień Wireless został całkowicie przeprojektowany z użyciem uproszczonego układu i spójnego stylu wizualnego. Zmniejsza to złożoność obsługi i znacząco poprawia prostotę oraz wygodę korzystania z interfejsu.

!!! note "Ulepszony szyfrowany DNS"
    
    Szyfrowany DNS został rozszerzony o obsługę większej liczby protokołów szyfrowania, w tym DoH, DoT i DoQ. Jednocześnie zintegrowano więcej oficjalnych dostawców DNS oraz dodano ręczną konfigurację niestandardowych szyfrowanych serwerów DNS, aby spełnić różne wymagania dotyczące bezpiecznego rozwiązywania domen.
    
!!! note "Obsługa Tailscale Exit Node"
    
    Routery GL.iNet obsługują teraz działanie jako Tailscale Exit Node. Cały wychodzący ruch internetowy z urządzeń w Tailnet może być routowany przez publiczny adres IP routera, co zapewnia jednolite i bezpieczne zarządzanie wyjściem sieciowym dla całej sieci Tailscale.
    
!!! note "Integracja AstroWarp"
    
    AstroWarp został oficjalnie zintegrowany z GL.iNet Router SDK w v4.9. Oparty na protokole AmneziaWG z natywną funkcją zaciemniania ruchu, zapewnia stabilny, szyfrowany i bezpieczny zdalny dostęp. Użytkownicy mogą szybko ukończyć parowanie urządzenia i konfigurację połączenia za pomocą dynamicznego kodu dostępu w web Admin Panel. Obsługuje bezpieczne połączenie jednym kliknięciem między routerami podróżnymi i sieciami domowymi w ciągu kilku sekund, bez rejestracji konta ani logowania.
