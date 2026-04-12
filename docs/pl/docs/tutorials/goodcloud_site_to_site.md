# GoodCloud Site to Site

## Wprowadzenie

GoodCloud Site to Site umożliwia biurom w różnych lokalizacjach nawiązywanie bezpiecznych połączeń między sobą przez Internet. Rozszerza sieć firmową, udostępniając zasoby komputerowe z jednej lokalizacji pracownikom w innych lokalizacjach w całej sieci.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Scenariusz 1**: Dziesiątki oddziałów tej samej firmy wymagają integracji w jednolitą sieć prywatną, umożliwiającą bezproblemowe udostępnianie zasobów we wszystkich lokalizacjach.

**Scenariusz 2**: Gdy dwie firmy w bliskiej współpracy wymagają współpracy biznesowej, Site to Site ułatwia ich pracę we wspólnym i bezpiecznym środowisku sieciowym.

**Scenariusz 3**: Dla rodzin z kamerami IP, Site to Site umożliwia zdalny dostęp do urządzenia, gdy członkowie rodziny są poza domem, zapewniając łatwe monitorowanie z dowolnego miejsca.

## Wymagania

1. Do zbudowania sieci Site to Site wymagane są co najmniej dwa routery GL.iNet.

2. Co najmniej jeden router powinien posiadać publiczny adres IP, aby można go było ustawić jako węzeł główny. [Sprawdź, czy Twój dostawca internetowy przypisuje Ci publiczny adres IP](how_to_check_if_isp_assigns_you_a_public_ip_address.md). 

    Router o wysokiej wydajności i najlepszej prędkości sieciowej jest preferowany jako węzeł główny.

3. **NIE** zaleca się uruchamiania Site to Site, gdy węzły podrzędne również uruchamiają klient VPN / Tailscale / ZeroTier / AstroWarp, ponieważ może to znacznie skomplikować konfigurację sieci.

## Zbuduj sieć Site to Site

1. Powiąż swoje routery z kontem GoodCloud. [Jak to zrobić](../interface_guide/cloud.md/#setup-your-goodcloud-account)?

2. Zaloguj się do [GoodCloud](https://www.goodcloud.xyz/#/login), przejdź do **Site to Site** na lewym pasku bocznym. Kliknij **Create Network** w prawym górnym rogu.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Zaznacz pole po lewej stronie, aby wybrać co najmniej dwa urządzenia.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}
    
    Wybrane urządzenia zostaną wyświetlone w dolnej części strony. 

    Domyślny port Site to Site to **51830**. Jeśli chcesz użyć innego portu, kliknij **Advanced** w lewym dolnym rogu, aby go zmienić. Następnie kliknij **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Sieć Site to Site może obsługiwać maksymalnie 10 urządzeń, aby zapewnić stabilną wydajność.

4. Nadaj nazwę swojej sieci i kliknij **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Test użyteczności węzłów rozpocznie testowanie, aby sprawdzić, czy jakiekolwiek urządzenie może zostać ustawione jako węzeł główny.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Jeśli żadne z Twoich urządzeń nie może być użyte jako węzeł główny, upewnij się, że:

    - Co najmniej jeden router ma publiczny adres IP, statyczny lub dynamiczny.
    - Port jest otwarty. Domyślny port dla Site to Site to 51830. Możesz również zmienić port i spróbować ponownie.
    - Jeśli router, który chcesz ustawić jako węzeł główny, znajduje się za NAT, może być konieczne skonfigurowanie przekierowania portów.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Jeśli więcej niż jedno urządzenie może zostać ustawione jako węzeł główny, wybierz jedno, aby kontynuować. Zalecamy wybranie routera o wysokiej wydajności i najlepszej prędkości sieciowej jako węzła głównego.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Jeśli tylko jedno urządzenie może zostać ustawione jako węzeł główny, zostaniesz bezpośrednio przekierowany na stronę szczegółów Site to Site.

6. Sieć jest domyślnie wyłączona. Upewnij się, że adresy IP LAN wszystkich węzłów nie kolidują ze sobą. Kliknij ikonę zębatki, aby zmienić adres IP LAN, jeśli to konieczne, a następnie kliknij **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Poczekaj kilka minut. Gdy przerywana linia zmieni się na ciągłą, oznacza to, że sieć Site to Site została pomyślnie nawiązana.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Testowanie połączenia Site to Site

1. Podłącz swój komputer lub smartfon do jednego z węzłów w tej sieci Site to Site.

2. Uruchom przeglądarkę internetową, aby uzyskać dostęp do adresu IP LAN innego węzła. Jeśli możesz uzyskać dostęp do strony logowania, połączenie między tymi dwoma węzłami działa.

## Trasy i inne opcje

Domyślnie każdy węzeł może uzyskać dostęp do sieci LAN innych węzłów. Ze względów bezpieczeństwa zalecamy otwieranie tylko adresów IP określonych usług.

Na przykład w podsieci węzła 1 znajduje się serwer A (172.30.97.100). Jeśli chcesz, aby inne węzły miały dostęp tylko do serwera A w węźle 1, możesz skonfigurować to w następujący sposób:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Możesz również dodać trasy nadrzędne węzła.

Każdy węzeł podrzędny buduje zaszyfrowaną sieć tunelową do węzła głównego. Jeśli chcesz zmienić adres IP podsieci tunelu, kliknij **IP Address Range**, aby go zmodyfikować.

Zastosowanie zmiany zakresu adresów IP spowoduje rozłączenie sieci na kilka minut.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
