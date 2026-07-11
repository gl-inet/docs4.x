# Profil klienta VPN

> Ten przewodnik dotyczy firmware v4.9 i nowszego.

Po lewej stronie webowego panelu administracyjnego przejdź do **VPN** -> **VPN Client Profile**.

Od firmware v4.9 strony [OpenVPN Client](openvpn_client.md) i [WireGuard Client](wireguard_client.md) zostały połączone w jedną stronę **VPN Client Profile**, aby usprawnić zarządzanie. Układ został nieznacznie zmieniony, ale podstawowa funkcjonalność pozostaje bez zmian. W razie potrzeby możesz nadal korzystać z osobnych przewodników.

Ta strona umożliwia logowanie do niektórych zintegrowanych usług VPN i łatwe pobieranie ich profili do połączeń VPN albo ręczne przesyłanie plików konfiguracyjnych wyeksportowanych ze strony innego dostawcy VPN. W razie potrzeby możesz przełączać protokoły VPN w prawym górnym rogu.

## WireGuard

WireGuard® to lekki, wydajny i nowoczesny VPN oparty na najnowszej kryptografii. Zapewnia lepszą szybkość, prostotę i praktyczność niż IPsec, a także znacznie przewyższa OpenVPN pod względem wydajności.

Routery GL.iNet oferują wbudowaną obsługę WireGuard dla następujących dostawców VPN. Jeśli masz aktywną subskrypcję, wystarczy wprowadzić dane logowania do usługi na stronie **VPN Client Profile**, aby szybko zakończyć konfigurację.

* AzireVPN
* Hide.me
* IPVanish
* Mullvad
* NordVPN
* PIA (Private Internet Access)
* PureVPN
* Surfshark
* Windscribe

![wireguard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg.png){class="glboxshadow"}

Jeśli korzystasz z innego dostawcy usług WireGuard, pobierz plik konfiguracyjny z jego strony internetowej, a następnie kliknij **Add Manually**, aby przesłać plik do routera i nawiązać połączenie VPN. Jeśli nie wiesz, jak pobrać pliki konfiguracyjne, zapoznaj się z [tym przewodnikiem](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) lub skontaktuj się z pomocą techniczną dostawcy.

![wireguard add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_manual.png){class="glboxshadow"}

---

Weźmy [AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} jako przykład.

1. Kliknij **AzireVPN**.

    ![wg azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/wg_azirevpn.png){class="glboxshadow"}

2. Wprowadź **Username** i **Password**, a następnie kliknij **Save and Continue**.

    ![azirevpn1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn1.png){class="glboxshadow"}

    System wygeneruje pliki konfiguracyjne dla wszystkich dostępnych serwerów.

    ![azirevpn2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn2.png){class="glboxshadow"}

3. Skorzystaj z odpowiednich wskazówek poniżej, zależnie od swoich potrzeb.

    !!! note "Przypadek 1. Jeśli chcesz, aby wszyscy podłączeni klienci korzystali z VPN do dostępu do Internetu, wykonaj poniższe kroki."

        1. Wybierz preferowany serwer i kliknij ikonę trzech kropek po prawej stronie, aby rozpocząć połączenie.

            ![azirevpn3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn3.png){class="glboxshadow"}

        2. Po nawiązaniu połączenia obok pliku konfiguracyjnego pojawi się zielona kropka.

            ![azirevpn4](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn4.png){class="glboxshadow"}

            Teraz połączenie VPN jest aktywne, a wszyscy klienci podłączeni do tego routera powinni korzystać z VPN, aby uzyskać bezpieczny dostęp do Internetu.

        3. (Opcjonalnie) Jeśli chcesz, aby system automatycznie odcinał cały dostęp do Internetu dla Twojej sieci lokalnej w przypadku nieoczekiwanego zerwania połączenia VPN, zapobiegając ujawnieniu prawdziwego adresu IP i danych online oraz zapewniając ciągłą prywatność i bezpieczeństwo, przejdź do **VPN Dashboard**, aby włączyć **Kill Switch**.

            * Aby skonfigurować Kill Switch dla pojedynczego tunelu VPN, zapoznaj się z [tym](vpn_dashboard.md#tunnel-options).
            
            * Aby skonfigurować Kill Switch dla globalnego połączenia VPN (czyli rozszerzonego Kill Switch), zapoznaj się z [tym](vpn_dashboard.md#all-other-traffic).

    !!! note "Przypadek 2. Jeśli wolisz zamiast tego dostosować politykę VPN, wykonaj poniższe kroki."

        1. Kliknij **Go to Dashboard** na dole.

            ![azirevpn5](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/azirevpn5.png){class="glboxshadow"}

        2. Zostaniesz przekierowany do **VPN Dashboard**, aby skonfigurować politykę VPN. Szczegóły znajdziesz [tutaj](vpn_dashboard.md#set-up-vpn-policy).

## OpenVPN

OpenVPN to otwartoźródłowy protokół VPN, który wykorzystuje techniki wirtualnych sieci prywatnych do ustanawiania bezpiecznych połączeń site-to-site lub punkt-punkt.

Routery GL.iNet oferują wbudowaną obsługę OpenVPN dla [NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&aff_id=12016&url_id=902){target="_blank"}. Jeśli masz aktywną subskrypcję, wystarczy wprowadzić dane logowania do usługi na stronie **VPN Client Profile**, aby szybko zakończyć konfigurację.

![ovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn.png){class="glboxshadow"}

Jeśli korzystasz z innego dostawcy usług OpenVPN, pobierz plik konfiguracyjny z jego strony internetowej, a następnie kliknij **Add Manually**, aby przesłać plik do routera i nawiązać połączenie VPN. Jeśli nie wiesz, jak pobrać pliki konfiguracyjne, zapoznaj się z [tym przewodnikiem](openvpn_client.md#get-configuration-files-from-openvpn-service-providers) lub skontaktuj się z pomocą techniczną dostawcy.

![ovpn add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_client_profile/ovpn_manual.png){class="glboxshadow"}

---

Powiązane artykuły

- [VPN Dashboard (Firmware v4.9)](vpn_dashboard.md)
- [Konfiguracja klienta WireGuard na routerach GL.iNet](wireguard_client.md)
- [Konfiguracja klienta OpenVPN na routerach GL.iNet](openvpn_client.md)

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
