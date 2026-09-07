# GoodPAS

**Uwaga**: ta funkcja została wprowadzona w firmware v4.10, w którym nazwę AstroWarp zmieniono na GoodPAS. Jeśli urządzenie korzysta ze starszej wersji firmware, zapoznaj się z przewodnikiem [AstroWarp](./astrowarp.md).

---

W menu po lewej stronie webowego panelu administracyjnego przejdź do **CLOUD SERVICES** -> **GoodPAS**.

GoodPAS to zaawansowane rozwiązanie do zdalnego dostępu, zintegrowane z SDK routerów GL.iNet. Korzysta z protokołu AmneziaWG z wbudowanym maskowaniem ruchu, zapewniając stabilne i bezpieczne połączenia na potrzeby niezawodnego zdalnego dostępu w dowolnym miejscu i czasie.

Ta funkcja umożliwia płynny zdalny dostęp do sieci domowej. Urządzenia można skonfigurować i sparować bezpośrednio w webowym panelu administracyjnym za pomocą dynamicznego kodu dostępu. Pozwala to w kilka sekund zestawić bezpieczne połączenie między routerem podróżnym a siecią domową bez rejestracji i logowania.

**Uwaga**:

1. Nie zaleca się korzystania z GoodPAS jednocześnie z żadną z następujących funkcji, ponieważ może to powodować konflikty routingu: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.

2. Gdy GoodPAS jest włączony, nie można korzystać z funkcji Network Mode.

## Szybka konfiguracja

W poniższym przykładzie użyjemy routerów **Flint 3 (GL-BE9300)** i **Mango 2 (GL-MG1300)** do skonfigurowania sieci GoodPAS.

Flint 3 będzie pełnił rolę routera domowego, a Mango 2 — routera podróżnego kierującego ruch sieciowy z powrotem do Flint 3 w celu uzyskania dostępu do Internetu.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/topology.png){class="glboxshadow"}

1. Skonfiguruj połączenie Flint 3 z Internetem.

    Zaloguj się do webowego panelu administracyjnego Flint 3 i przejdź do strony INTERNET. Połącz router z Internetem przy użyciu jednej z obsługiwanych metod: Ethernet, Repeater, Tethering lub Cellular.

    Jak pokazano poniżej, router domowy Flint 3 jest połączony z modemem dostawcy Internetu (Hong Kong Broadband Network Ltd) za pomocą kabla Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/home_internet.png){class="glboxshadow"}

2. Wygeneruj kod dostępu.

    W webowym panelu administracyjnym Flint 3 przejdź do **CLOUD SERVICES** -> **GoodPAS**. Kliknij **Use At Home**.

    ![use at home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_home.png){class="glboxshadow"}

    Zostanie wygenerowany Access Code. Skopiuj go, aby użyć później.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/generate_access_code.png){class="glboxshadow"}

3. Skonfiguruj połączenie Mango 2 z Internetem.

    Zaloguj się do webowego panelu administracyjnego Mango 2 i przejdź do strony INTERNET. Połącz router z Internetem przy użyciu jednej z obsługiwanych metod: Ethernet, Repeater, Tethering lub Cellular.

    Jak pokazano poniżej, router podróżny Mango 2 jest połączony z hotspotem osobistym iPhone'a 17 (w Shenzhen, w sieci China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/travel_internet.png){class="glboxshadow"}

4. Wprowadź kod dostępu.

    W webowym panelu administracyjnym Mango 2 przejdź do **CLOUD SERVICES** -> **GoodPAS**. Kliknij **Use While Travelling**.

    ![use at travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/use_at_travel.png){class="glboxshadow"}

    Wprowadź Access Code uzyskany w kroku 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/enter_access_node.png){class="glboxshadow"}

    Poczekaj na zakończenie weryfikacji.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/verifying.png){class="glboxshadow"}

    Połączenie z routerem domowym Flint 3 zostanie nawiązane. Teraz możesz bezpiecznie korzystać z Internetu przez sieć domową.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_travel.png){class="glboxshadow"}

    Stan połączenia jest również widoczny w webowym panelu administracyjnym Flint 3, jak pokazano poniżej.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/connected_home.png){class="glboxshadow"}

## Test łączności

1. Połącz laptop lub smartfon z siecią Wi-Fi routera podróżnego Mango 2.

2. Otwórz przeglądarkę i odwiedź [ipcheck.ing](https://ipcheck.ing/){target="_blank"} lub inną stronę sprawdzającą adres IP.

    Zostanie wyświetlony publiczny adres IP Flint 3, co oznacza, że Mango 2 uzyskuje dostęp do Internetu przez domowy router Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_hk.png){class="glboxshadow"}

3. Rozłącz połączenie GoodPAS na Mango 2, a następnie odśwież stronę, aby ponownie wysłać zapytanie o adres IP.

    Zostanie wyświetlony publiczny adres IP Mango 2, co oznacza, że Mango 2 uzyskuje dostęp do Internetu przez swoją sieć lokalną.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/goodpas/ipcheck_sz.png){class="glboxshadow"}

## FAQ

1. **P: Jaki format ma dynamiczny kod dostępu i jak długo jest ważny?**

    O: Jest to 8-znakowy kod składający się z cyfr i wielkich liter, ważny przez 10 minut.

2. **P: Co stanie się z routerem podróżnym, jeśli zakończę połączenie na routerze domowym?**

    O: Router podróżny rozłączy się i przejdzie w stan oczekiwania bez dostępu do sieci. Gdy router domowy wznowi połączenie, router podróżny może automatycznie połączyć się ponownie bez ponownego wpisywania kodu dostępu.

3. **P: W jakich sytuacjach router podróżny przechodzi w stan oczekiwania?**

    O: Router podróżny przechodzi w stan oczekiwania, gdy router domowy spełni jeden z następujących warunków:

    - zakończy połączenie GoodPAS;
    - utraci dostęp do Internetu.

4. **P: Do czego służy przycisk Reset w prawym górnym rogu?**

    O: Usuwa wszystkie autoryzowane urządzenia i przywraca stronę wyboru roli routera, aby można było wybrać ją ponownie.

5. **P: Co stanie się z routerem podróżnym, jeśli zresetuję GoodPAS na routerze domowym?**

    O: Po zresetowaniu routera domowego urządzenia połączone zdalnie zostaną odłączone od sieci GoodPAS i wrócą do swojej sieci lokalnej w celu uzyskania dostępu do Internetu.

---

Masz dodatkowe pytania? Odwiedź nasze [forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
