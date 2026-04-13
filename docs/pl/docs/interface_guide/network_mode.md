# Tryb sieciowy

W lewym panelu administratora przejdź do **NETWORK** -> **Network Mode**.

Tryb sieciowy określa różne role i funkcje operacyjne, jakie może przyjąć router w celu spełnienia różnych wymagań dotyczących wdrożenia sieci. Tryby te są dostosowane do scenariuszy od domowego pokrycia Wi-Fi po wielołączową sieć na poziomie przedsiębiorstw; każdy tryb wyłącza lub włącza określone funkcje routera w celu optymalizacji wydajności.

!!! note

    1. Po zmianie trybu sieciowego routera może być konieczne ponowne połączenie wszystkich urządzeń klienckich.
    
    2. **Gdy router jest w trybie Access Point / WDS / Bridge, dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN nie będzie możliwy.** Zamiast tego należy zalogować się do routera nadrzędnego, aby znaleźć adres IP przypisany temu routerowi, a następnie użyć tego adresu do uzyskania dostępu do panelu administratora. Jeśli nie masz dostępu do routera nadrzędnego, naciśnij i przytrzymaj przycisk reset przez 4 sekundy, aby przywrócić domyślny tryb Router.

    3. **W trybie Extender** nadal możesz uzyskać dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN.
    
    4. **W trybie Non-Router następujące funkcje będą niedostępne**: Access Control (Allowlist i Blocklist), AstroWarp, VPN, AdGuard Home, Parental Control, ZeroTier, Tailscale, Port Forwarding, Multi-WAN, DHCP Server, Address Reservation, Guest Network, DNS, Port Management, IPv6, Drop-in Gateway, IGMP Snooping, Network Acceleration, NAT Settings.

## Modele z Wi-Fi

Z wyjątkiem określonych modeli większość bezprzewodowych routerów GL.iNet posiada funkcję Wi-Fi.

Modele z funkcją Wi-Fi zazwyczaj obsługują cztery tryby sieciowe: Router, Access Point, Extender i WDS. Należy pamiętać, że niektóre modele nie obsługują trybu WDS.

![network mode](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page.png){class="glboxshadow"}

- **Router**: Jest to domyślny tryb pracy większości routerów domowych i biurowych, zaprojektowany do tworzenia prywatnej sieci lokalnej i działania jako dedykowana brama między publicznym Internetem a podłączonymi urządzeniami.

    W trybie Router urządzenie włącza podstawowe funkcje, w tym NAT, DHCP i wbudowaną zaporę. Łączy się z łączem nadrzędnym, takim jak szerokopasmowy światłowód, automatycznie przypisuje prywatne adresy IP podłączonym urządzeniom i zapewnia bezpieczeństwo sieciowe całej sieci prywatnej.
    
    ---

- **Access Point**: Tryb ten umożliwia routerowi podłączenie do sieci przewodowej za pomocą kabla LAN i nadawanie sygnałów bezprzewodowych, rozszerzając zasięg Wi-Fi w dużych przestrzeniach i umożliwiając większej liczbie urządzeń dostęp do sieci.

    W trybie Access Point router wyłącza funkcje NAT i DHCP, działając wyłącznie jako nadajnik sygnału bezprzewodowego i przełącznik, a nie jako samodzielna brama.

    Po przełączeniu w tryb Access Point dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN nie będzie możliwy. Zamiast tego należy zalogować się do routera nadrzędnego, aby znaleźć adres IP przypisany temu punktowi dostępowemu, a następnie użyć go do uzyskania dostępu do panelu administratora. Jeśli nie masz dostępu do routera nadrzędnego, naciśnij i przytrzymaj przycisk reset przez 4 sekundy, aby przywrócić domyślny tryb Router.

    ---

- **Extender**: Tryb ten jest przeznaczony do rozszerzania zasięgu Wi-Fi istniejącej sieci bezprzewodowej i eliminowania martwych stref sygnału w obszarach o słabej łączności.

    Umożliwia routerowi bezprzewodowe odbieranie sygnałów z routera głównego, ich wzmacnianie i retransmisję wzmocnionego sygnału. W odróżnieniu od trybu Access Point nie wymaga przewodowego połączenia z routerem głównym, jednak może prowadzić do zmniejszenia przepustowości o połowę, ponieważ urządzenie musi jednocześnie odbierać i nadawać sygnał.

    W trybie Extender nadal możesz uzyskać dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN.

    ---

- **WDS**: Tryb Wireless Distribution System (WDS) jest podobny do trybu Extender – rozszerza zasięg Wi-Fi bezprzewodowo – lecz obsługuje mostkowanie bezprzewodowe między wieloma zgodnymi routerami. Zalecany jest do rozszerzania sieci bezprzewodowej, gdy router nadrzędny obsługuje funkcję WDS.
    
    Tryb ten jest idealny w scenariuszach takich jak pokrycie budynków wielopiętrowych lub małych kampusów biurowych, gdzie wiele routerów musi współpracować, tworząc zunifikowaną sieć bezprzewodową. W odróżnieniu od trybu Extender, który transmituje sygnał tylko z jednego routera głównego do jednego urządzenia rozszerzającego, tryb WDS umożliwia wzajemne wysyłanie i odbieranie sygnałów przez wzajemnie połączone routery, zapewniając płynne pokrycie na większych obszarach z wieloma węzłami sygnałowymi.

    Po przełączeniu w tryb WDS dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN nie będzie możliwy. Zamiast tego należy zalogować się do routera nadrzędnego, aby znaleźć adres IP przypisany temu routerowi WDS, a następnie użyć go do uzyskania dostępu do panelu administratora. Jeśli nie masz dostępu do routera nadrzędnego, naciśnij i przytrzymaj przycisk reset przez 4 sekundy, aby przywrócić domyślny tryb Router.

## Modele bez Wi-Fi

GL-MT2500/GL-MT2500A nie obsługuje trybów Access Point, Extender ani WDS, ponieważ nie posiada funkcji Wi-Fi. Obsługuje jednak tryb Router i tryb Bridge.

![network mode of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/network_mode/network_mode_page_mt2500.png){class="glboxshadow"}

- **Router**: Jest to domyślny tryb pracy większości routerów domowych i biurowych, zaprojektowany do tworzenia prywatnej sieci lokalnej (LAN) i działania jako dedykowana brama między publicznym Internetem a podłączonymi urządzeniami.

    W trybie Router urządzenie włącza podstawowe funkcje, w tym NAT, DHCP i wbudowaną zaporę. Łączy się z łączem nadrzędnym, takim jak szerokopasmowy światłowód, automatycznie przypisuje prywatne adresy IP podłączonym urządzeniom i zapewnia bezpieczeństwo sieciowe całej sieci prywatnej.
    
    ---

- **Bridge**: Umożliwia routerowi podłączenie do sieci przewodowej i działanie jako most między urządzeniami sieciowymi.

    W tym trybie router działa zasadniczo jako przełącznik, przekazując dane między podłączonymi urządzeniami bez wykonywania usług NAT, zapory ani DHCP. Umożliwia to bezproblemową komunikację między urządzeniami w tej samej sieci poprzez działanie jako proste miejsce połączenia, a nie brama sieciowa.

    Po przełączeniu w tryb Bridge dostęp do panelu administratora za pomocą oryginalnego adresu IP sieci LAN nie będzie możliwy. Zamiast tego należy zalogować się do routera nadrzędnego, aby znaleźć adres IP przypisany temu routerowi Bridge, a następnie użyć go do uzyskania dostępu do panelu administratora. Jeśli nie masz dostępu do routera nadrzędnego, naciśnij i przytrzymaj przycisk reset przez 4 sekundy, aby przywrócić domyślny tryb Router.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.