# VPN Dashboard (Firmware v4.7 i wcześniejsze)

Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **VPN Dashboard**.

Strona VPN Dashboard wyświetla szczegóły połączenia VPN, takie jak adres serwera, statystyki ruchu, wirtualny adres IP klienta i dziennik połączeń. Umożliwia także konfigurację zaawansowanych ustawień, takich jak VPN Kill Switch, polityka VPN, maskowanie IP, MTU i kaskadowanie VPN.

Ta strona jest podzielona na dwie sekcje: [Klient VPN](#vpn-client) i [Serwer VPN](#vpn-server).

![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpn_dashboard_initial.png){class="glboxshadow"}

## Klient VPN {#vpn-client}

Przy pierwszym wejściu na tę stronę, jeśli nie ma dostępnego pliku konfiguracyjnego dla OpenVPN ani WireGuard, strona będzie wyglądać jak poniżej. Kliknij **Set Up Now**, a zostaniesz przeniesiony do strony [Klient OpenVPN](openvpn_client.md) lub [Klient WireGuard](wireguard_client.md), aby przesłać plik konfiguracyjny VPN.

![konfiguracja klienta VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_setup.png){class="glboxshadow"}

Po przesłaniu konfiguracja będzie widoczna w kolumnie **Configuration File**. Jeśli przesłano wiele plików konfiguracyjnych, możesz przełączać się między nimi, klikając pole.

![pliki konfiguracyjne](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_config.png){class="glboxshadow"}

### Opcje klienta

Kliknij ikonę koła zębatego po prawej stronie, aby uzyskać dostęp do opcji klienta OpenVPN lub WireGuard.

![opcje klienta VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options.png){class="glboxshadow"}

Opcje klienta OpenVPN są wyświetlane jak poniżej.

![opcje klienta OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_ovpn.png){class="glboxshadow"}

Opcje klienta WireGuard są wyświetlane jak poniżej.

![opcje klienta WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_options_wg.png){class="glboxshadow"}

- **Zdalny dostęp do LAN**: Jeśli ta opcja jest włączona, zdalny dostęp do tego routera i jego urządzeń LAN przez VPN będzie dozwolony. Serwer VPN musi rozgłaszać trasę do podsieci LAN tego routera.

    Na przykład, jak pokazano na poniższym diagramie, router GL.iNet działa jako klient VPN i łączy się z serwerem VPN przez tunel VPN. Gdy ta opcja jest włączona, zarówno router GL.iNet, jak i urządzenia po jego stronie LAN mogą być dostępne dla urządzeń po stronie serwera VPN (np. NAS). Wymaga to dodania na serwerze VPN reguły routingu do podsieci LAN routera GL.iNet.

    ![zezwól na zdalny dostęp do LAN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_remote_access_lan_diagram.png){class="glboxshadow gl-80-desktop"}

- **Maskowanie IP**: Jeśli ta opcja jest włączona, źródłowe adresy IP klientów LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w konfiguracjach site-to-site, w których zdalny węzeł zna Twoje podsieci LAN.

- **MTU**: Skrót od Maximum Transmission Unit. To opcjonalne ustawienie pozwala dostosować MTU tunelu VPN, nadpisując wartość zdefiniowaną w pliku konfiguracyjnym.

### Tryb proxy

Domyślnym trybem proxy dla połączenia VPN jest **Global Proxy**. Możesz kliknąć pole w prawym górnym rogu, aby przełączyć się na inne tryby proxy.

![tryb proxy VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_proxy.png){class="glboxshadow"}

Dostępne są trzy tryby proxy: **Global Proxy**, **Policy Mode** i **Route Mode**.

1. Global Proxy

    W tym trybie cały ruch będzie kierowany przez VPN. Może być aktywna tylko jedna instancja klienta VPN.

2. Policy Mode

    Ten tryb można dalej podzielić na trzy polityki.

    - Na podstawie docelowej domeny lub adresu IP.

        W tym trybie przez VPN będzie kierowany tylko ruch określonych witryn, zidentyfikowanych na podstawie adresu IP lub nazwy domeny. Może być aktywna tylko jedna instancja klienta VPN.

    - Na podstawie urządzenia klienckiego.

        W tym trybie przez VPN będzie kierowany tylko ruch wybranych urządzeń LAN, zidentyfikowanych na podstawie adresów MAC. Może być aktywna tylko jedna instancja klienta VPN.

    - Na podstawie sieci VLAN.

        W tym trybie przez VPN będzie kierowany tylko ruch określonej sieci VLAN. Może być aktywna tylko jedna instancja klienta VPN.

3. Route Mode

    - Auto Detect

        Zostaną użyte reguły routingu zdefiniowane w każdym pliku konfiguracyjnym klienta VPN lub wydane przez serwer VPN.

    - Customize Routing Rules

        Możesz ręcznie skonfigurować reguły routingu dla każdej instancji klienta VPN.

### Opcje globalne

Kliknij **Global Options** w prawym górnym rogu, aby skonfigurować zaawansowane ustawienia klienta VPN.

![opcje globalne klienta VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_1.png){class="glboxshadow"}

![opcje globalne](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnclient_global_options_2.png){class="glboxshadow"}

- **Block Non-VPN Traffic**: Jeśli ta opcja jest włączona, cały ruch internetowy jest wymuszany wyłącznie przez tunel VPN i nie może być kierowany przez inne interfejsy, takie jak lokalny WAN dostawcy Internetu. Jeśli połączenie VPN niespodziewanie się zerwie, cały ruch internetowy zostanie całkowicie zablokowany, aby zapobiec powrotowi do zwykłego WAN. Pozwala to uniknąć wycieków VPN spowodowanych awarią VPN, nieprawidłowymi ustawieniami DNS klienta i podobnymi problemami.

    Ta funkcja jest także znana jako [VPN Kill Switch](https://cybernews.com/what-is-vpn/vpn-kill-switch/){target="_blank"}. Chroni dane użytkownika przed ujawnieniem w sieci. Typowy Kill Switch automatycznie odcina dostęp do Internetu, gdy połączenie VPN przestaje działać. Funkcja **Block Non-VPN Traffic** w routerach GL.iNet zapewnia szerszą ochronę przed wyciekami i obejmuje następujące scenariusze:

    1. Wyciek DNS

    2. Wyciek IPv6

    3. Wyciek WebRTC

    4. Zerwanie połączenia VPN

    5. Aplikacje uruchomione przed ustanowieniem połączenia VPN

    6. Wycieki ruchu specyficzne dla aplikacji

- **Allow Access WAN**: Jeśli ta opcja jest włączona, lokalne urządzenia klienckie nadal mogą uzyskiwać dostęp do usług po stronie WAN (np. drukarek, NAS i innych urządzeń w podsieci nadrzędnej), gdy VPN jest aktywny.

    ![zezwól na dostęp do WAN klienta VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/allow_access_wan_diagram.jpg){class="glboxshadow gl-90-desktop"}

    Jak pokazano na powyższym diagramie, włączenie tej funkcji pozwala urządzeniom lokalnym dotrzeć do hostów w podsieci nadrzędnej, takich jak drukarki i NAS.

    Ta opcja została zaprojektowana przede wszystkim po to, aby klienci mogli uzyskiwać dostęp do urządzeń w podsieci nadrzędnej. Router nie potrafi jednak odróżnić ruchu do podsieci nadrzędnej od zwykłego ruchu internetowego. Jeśli urządzenia klienckie uzyskują dostęp do zasobów bezpośrednio przez publiczne adresy IP, istnieje ryzyko wycieku ruchu. Z tego powodu **Allow Access WAN** i **Block Non-VPN Traffic** wzajemnie się wykluczają i nie mogą być włączone jednocześnie.

- **Services From GL.iNet Use VPN**: Jeśli ta opcja jest włączona, usługi GoodCloud, DDNS i rtty będą przesyłać pakiety przez tunele VPN. Opcja jest domyślnie wyłączona, ponieważ usługi te zwykle wymagają prawdziwego adresu IP urządzenia do prawidłowego działania.

## Serwer VPN {#vpn-server}

Jeśli router nigdy nie był skonfigurowany jako serwer OpenVPN lub WireGuard, strona będzie wyglądać jak poniżej. Kliknij **Set Up Now**, a zostaniesz przeniesiony do strony **OpenVPN Server** lub **WireGuard Server**, aby zainicjować serwer VPN.

![konfiguracja serwera VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_setup.png){class="glboxshadow"}

Po włączeniu serwera OpenVPN lub WireGuard strona wyświetli stan serwera jak poniżej.

![serwer VPN włączony](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_connected.png){class="glboxshadow"}

### Opcje serwera

Kliknij ikonę koła zębatego po prawej stronie, aby uzyskać dostęp do opcji serwera OpenVPN lub WireGuard.

![opcje serwera VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options.png){class="glboxshadow"}

Opcje serwera OpenVPN są wyświetlane jak poniżej.

![opcje serwera OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_ovpn.png){class="glboxshadow"}

Opcje serwera WireGuard są wyświetlane jak poniżej.

![opcje serwera WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_options_wg.png){class="glboxshadow"}

- **Zdalny dostęp do LAN**: Jeśli ta opcja jest włączona, zasoby w podsieci LAN serwera mogą być dostępne przez tunel VPN.

- **Maskowanie IP**: Jeśli ta opcja jest włączona, źródłowe adresy IP klientów LAN zostaną przepisane na adres IP tunelu VPN routera. Wyłącz tę opcję tylko w konfiguracjach site-to-site, w których zdalny węzeł zna Twoje podsieci LAN.

- **MTU**: Skrót od Maximum Transmission Unit. Wartość MTU ustawiona dla tunelu nadpisze ustawienia MTU w pliku konfiguracyjnym.

- **Client to Client**: Jeśli ta opcja jest włączona, klienci VPN podłączeni do tego serwera mogą uzyskiwać dostęp do siebie nawzajem przez swoje adresy IP tunelu VPN. Jeśli chcesz, aby klienci mogli również uzyskiwać dostęp do swoich podsieci LAN, serwer VPN musi rozgłaszać odpowiednie trasy do tych zdalnych podsieci LAN.

### Reguła trasy serwera

Kliknij ikonę trasy po prawej stronie, aby dostosować reguły tras OpenVPN lub WireGuard zgodnie z potrzebami.

![reguła trasy serwera](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule.png){class="glboxshadow"}

Reguła trasy serwera OpenVPN jest wyświetlana jak poniżej. Kliknij **Add Route Rule**, wprowadź **Target Address** oraz **Gateway**, a następnie kliknij zieloną ikonę potwierdzenia, aby zastosować ustawienie.

![reguła trasy serwera OpenVPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_ovpn.png){class="glboxshadow"}

Reguła trasy serwera WireGuard jest wyświetlana jak poniżej. Kliknij **Add Route Rule**, wprowadź **Target Address** oraz **Gateway**, a następnie kliknij zieloną ikonę potwierdzenia, aby zastosować ustawienie.

![reguła trasy serwera WireGuard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_route_rule_wg.png){class="glboxshadow"}

**Uwaga**: W trybie niestandardowych tras klient VPN zignoruje plik konfiguracyjny oraz konfigurację routingu wydaną przez serwer. To, czy podczas uzyskiwania dostępu do dowolnego segmentu sieci będzie używany szyfrowany tunel VPN, zależy od reguł routingu ustawionych ręcznie.

### Opcje globalne

Kliknij **Global Options** w prawym górnym rogu, aby skonfigurować zaawansowane ustawienia serwera VPN.

![globalne opcje serwera VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_1.png){class="glboxshadow"}

![globalne opcje serwera VPN](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_dashboard/vpnserver_global_options_2.png){class="glboxshadow"}

- **Kaskadowanie VPN**: Jeśli ta opcja jest włączona i router działa jednocześnie jako serwer VPN oraz klient VPN, ruch zdalnych klientów VPN podłączonych do serwera VPN tego routera będzie kierowany przez nadrzędny tunel VPN, którego router używa jako klient VPN. [Dowiedz się więcej o kaskadowaniu VPN](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
