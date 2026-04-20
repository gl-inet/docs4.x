# AstroWarp

**Uwaga**: Ten przewodnik przedstawia nową wersję AstroWarp, zintegrowaną z panelem administracyjnym GL.iNet.

Dokumentację starszej wersji AstroWarp znajdziesz pod [tym linkiem](https://docs.astrowarp.net/){target="_blank"}.

---

AstroWarp to zaawansowana funkcja sieciowa zintegrowana z routerami GL.iNet. Umożliwia wygodny zdalny dostęp do sieci domowej bez rejestracji i logowania. Korzysta z protokołu AmneziaWG z wbudowanym maskowaniem ruchu, dzięki czemu połączenie pozostaje stabilne i bezpieczne, dlatego AstroWarp świetnie sprawdza się jako rozwiązanie do niezawodnego zdalnego dostępu z dowolnego miejsca.

Użytkownicy mogą skonfigurować sieć AstroWarp bezpośrednio z poziomu panelu administracyjnego routera GL.iNet. Wystarczy sparować routery przy użyciu kodu dostępu, aby bezpiecznie połączyć router podróżny z siecią domową w kilka sekund.

**Uwaga:**

1. Nie zaleca się korzystania z AstroWarp jednocześnie z żadną z następujących funkcji, ponieważ może to powodować konflikty routingu: GoodCloud Site to Site, ZeroTier, Tailscale, Tor.
2. Gdy AstroWarp jest włączony, funkcja Network Mode nie może być używana.

## Obsługiwane modele

??? "Obsługiwane modele"

    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - ※GL-X3000 (Spitz AX)
    - ※GL-XE3000 (Puli AX)
    - ※GL-AX1800 (Flint)
    - ※GL-AXT1800 (Slate AX)
    - ※GL-MT3000 (Beryl AX)

    **Uwaga**: Modele oznaczone symbolem ※ obsługują zintegrowany AstroWarp w wersji beta firmware.

??? "Nieobsługiwane modele"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

## Szybka konfiguracja

W poniższym przykładzie użyjemy **Flint 3 (GL-BE9300)** i **Slate 7 (GL-BE3600)** do skonfigurowania sieci AstroWarp. 

Flint 3 będzie pełnił rolę routera domowego, a Slate 7 — routera podróżnego, który kieruje ruch sieciowy z powrotem do Flint 3, aby uzyskać dostęp do Internetu.

![topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/aw_topology.png){class="glboxshadow"}

**Uwaga**: Każdy router GL.iNet otrzymuje **10 GB bezpłatnego transferu miesięcznie** na potrzeby sieci AstroWarp. Urządzenia w sieci AstroWarp korzystają z transferu danych routera domowego, aby uzyskać dostęp do Internetu. W razie potrzeby możesz przejść na plan AstroWarp+ z nielimitowanym transferem.
 
1. Skonfiguruj Flint 3 do połączenia z Internetem.

    Zaloguj się do webowego panelu administracyjnego Flint 3 i przejdź do strony **INTERNET**. Połącz go z Internetem przy użyciu jednej z obsługiwanych metod: Ethernet, Repeater, Tethering lub Cellular.

    Jak pokazano poniżej, router domowy Flint 3 jest podłączony do modemu dostawcy Internetu (Hong Kong Broadband Network Ltd) za pomocą kabla Ethernet.

    ![home internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_internet.png){class="glboxshadow"}

2. Wygeneruj kod dostępu.

    W panelu administracyjnym Flint 3 przejdź do **CLOUD SERVICES** -> **AstroWarp**. Kliknij **Use At Home**.

    ![use as home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_at_home.png){class="glboxshadow"}

    Zostanie wygenerowany **Access Code**. Skopiuj ten kod, aby użyć go później.

    ![generate access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/home_generate_code.png){class="glboxshadow"}

3. Skonfiguruj Slate 7 do połączenia z Internetem.

    Zaloguj się do webowego panelu administracyjnego Slate 7 i przejdź do strony **INTERNET**. Połącz go z Internetem przy użyciu jednej z obsługiwanych metod: Ethernet, Repeater, Tethering lub Cellular.

    Jak pokazano poniżej, router podróżny Slate 7 jest połączony z hotspotem osobistym iPhone'a 15 Pro (w Shenzhen, w sieci China Unicom Guangdong Province).

    ![travel internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/travel_internet.png){class="glboxshadow"}

4. Wprowadź kod dostępu.

    W panelu administracyjnym Slate 7 przejdź do **CLOUD SERVICES** -> **AstroWarp**. Kliknij **Use While Travelling**.

    ![use for travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/use_for_travel.png){class="glboxshadow"}

    Wprowadź **Access Code** uzyskany w kroku 2.

    ![enter access code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/enter_access_code.png){class="glboxshadow"}

    Poczekaj na zakończenie weryfikacji.

    ![verifying](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/verifying.png){class="glboxshadow"}

    Następnie połączenie z domowym routerem Flint 3 zostanie pomyślnie nawiązane. Teraz możesz bezpiecznie korzystać z Internetu przez swoją sieć domową.

    ![connected travel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_travel.png){class="glboxshadow"}

    W webowym panelu administracyjnym Flint 3 również będzie wyświetlany stan połączenia, jak pokazano poniżej.

    ![connected home](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/connected_home.png){class="glboxshadow"}

## Test łączności

1. Podłącz laptop lub smartfon do Wi-Fi routera podróżnego Slate 7.

2. Otwórz przeglądarkę i odwiedź [ipcheck.ing](https://ipcheck.ing/){target="_blank"} lub dowolną inną stronę sprawdzającą adres IP.

    Zobaczysz publiczny adres IP routera Flint 3, co oznacza, że Slate 7 uzyskuje dostęp do Internetu przez domowy router Flint 3.

    ![ipcheck hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_hk.png){class="glboxshadow"}

3. Rozłącz połączenie AstroWarp na Slate 7, a następnie odśwież stronę, aby ponownie wysłać zapytanie o adres IP. 

    Zobaczysz publiczny adres IP routera Slate 7, co oznacza, że Slate 7 uzyskuje dostęp do Internetu przez swoją lokalną sieć.

    ![ipcheck sz](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/ipcheck_sz.png){class="glboxshadow"}

## Zmiana planu

Każdy router GL.iNet otrzymuje **10 GB darmowych danych miesięcznie** na potrzeby sieci AstroWarp. Urządzenia w sieci AstroWarp korzystają z transferu danych routera domowego, aby uzyskać dostęp do Internetu. 

W razie potrzeby możesz przejść na plan **AstroWarp+** z nielimitowanym transferem.

![upgrade plan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astrowarp/upgrade_plan.png){class="glboxshadow"}

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
