# Konfiguracja klienta WireGuard na routerach GL.iNet (oprogramowanie v4.6 i starsze)

**Uwaga**: Ten przewodnik dotyczy oprogramowania v4.6 i starszego. W przypadku nowszych wersji zapoznaj się z dokumentacją [tutaj](wireguard_client.md).

---

WireGuard® to wyjątkowo prosty, a zarazem szybki i nowoczesny VPN wykorzystujący najnowsze rozwiązania kryptograficzne. Został zaprojektowany tak, aby był szybszy, prostszy, lżejszy i bardziej użyteczny niż IPsec, a przy tym pozwalał uniknąć jego złożoności. Ma również zapewniać wyraźnie wyższą wydajność niż OpenVPN.

Jeśli masz już wykupioną usługę WireGuard u dostawcy, ale nie wiesz, jak pobrać pliki konfiguracyjne, zapoznaj się z przewodnikiem [jak pobrać pliki konfiguracyjne od dostawców usług WireGuard](../tutorials/how_to_get_configuration_files_from_wireguard_service_providers.md) lub skontaktuj się z pomocą techniczną dostawcy.

Klienta WireGuard możesz skonfigurować za pomocą panelu administracyjnego lub [aplikacji mobilnej](../faq/mobile_app.md).

- Aplikacja mobilna ma integrację z kilkoma dostawcami usług WireGuard, takimi jak AzireVPN, Mullvad, OVPN, StrongVPN i PIA VPN.

- Panel administracyjny obsługuje mniej dostawców usług WireGuard (np. AzireVPN i Mullvad), ale oferuje bardziej intuicyjne i szczegółowe strony konfiguracji.

Poniżej znajdziesz kroki konfiguracji w panelu administracyjnym.

---

Zaloguj się do panelu administracyjnego i przejdź do **VPN** -> **WireGuard Client**.

Jeśli masz subskrypcję **AzireVPN** lub **Mullvad**, możesz zalogować się bezpośrednio przy użyciu danych konta. W przeciwnym razie kliknij **Add Manually**, aby ręcznie przesłać profile WireGuard.

![wireguard client no initialized](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wireguard_client_no_initialized.png){class="glboxshadow"}

## Konfiguracja AzireVPN

[AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} to usługa VPN nastawiona na prywatność, oferująca bezpieczne, nowoczesne i niezawodne tunele, takie jak WireGuard.

![azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn.png){class="glboxshadow"}

1. Wprowadź **Username** i **Password**, a następnie kliknij **Save Credentials & Get Servers**. System wygeneruje pliki konfiguracyjne dla wszystkich serwerów.

    ![azirevpn profiles](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_generated_profiles.png){class="glboxshadow"}

2. Przejdź do VPN Dashboard, aby włączyć połączenie.

    ![vpn dashboard azirevpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn.png){class="glboxshadow"}

    Po połączeniu zobaczysz adres IP użytkownika oraz liczbę wysłanych i odebranych bajtów.

    ![vpn dashboard azirevpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_azirevpn_connected.png){class="glboxshadow"}

3. Aktualizacja serwerów

    AzireVPN może czasowo wyłączać lub serwisować niektóre serwery, co może powodować problemy z połączeniem. Kliknij **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów.

    ![azirevpn update servers](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_update_servers.png){class="glboxshadow"}

4. Edycja danych logowania

    Kliknij ikonę koła zębatego, aby edytować dane logowania.

    ![azirevpn edit credential](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/azirevpn_edit_credential.png){class="glboxshadow"}

## Konfiguracja Mullvad

[Mullvad](https://mullvad.net/){target="_blank"} to usługa VPN, która pomaga chronić prywatność Twojej aktywności online, tożsamości i lokalizacji.

Oprogramowanie 4.x ma zintegrowaną usługę Mullvad WireGuard.

![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad.png){class="glboxshadow"}

1. Wprowadź **Account**, a następnie kliknij **Save Credentials & Get Servers**.

    Numer konta Mullvad to 16-cyfrowy numer dziesiętny z zakresu od „1000 0000 0000 0000” do „9999 9999 9999 9999”.

    Pojawi się okno dialogowe wyboru lokalizacji.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_select_servers.png){class="glboxshadow"}

    Następnie zostaną wygenerowane pliki konfiguracyjne dla serwera w wybranej lokalizacji.
    
    **Public Key** to publiczny klucz WireGuard wysyłany do serwera Mullvad. Jednocześnie możesz mieć maksymalnie pięć kluczy. Kluczami WireGuard możesz zarządzać na [stronie Mullvad](https://mullvad.net/en/account/#/ports){target="_blank"}.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_generated_profiles.png){class="glboxshadow"}

2. Przejdź do VPN Dashboard, aby włączyć połączenie.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvadvpn.png){class="glboxshadow"}

    Po połączeniu zobaczysz adres IP użytkownika oraz liczbę wysłanych i odebranych bajtów.

    ![vpn dashboard mullvad connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/vpn_dashboard_mullvad_connected.png){class="glboxshadow"}

3. Aktualizacja serwerów

    Mullvad może czasowo wyłączać lub serwisować niektóre serwery, co może powodować problemy z połączeniem. Kliknij **Update Servers**, aby pobrać najnowszą listę dostępnych serwerów.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_update_servers.png){class="glboxshadow"}

4. Edycja danych logowania

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/mullvad_edit_credential.png){class="glboxshadow"}

5. Usuwanie informacji o koncie

    Jeśli klikniesz **Delete**, zostaną usunięte z routera dane konta, klucz prywatny, klucz publiczny oraz pliki konfiguracyjne.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all.png){class="glboxshadow"}

6. Usuwanie

    Ta opcja umożliwia usunięcie wszystkich plików konfiguracyjnych jednym kliknięciem i wyświetla monit z pytaniem, czy usunąć także klucz prywatny i klucz publiczny.

    ![mullvad vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/wgclient_delete_all_configuration_file.png){class="glboxshadow"}

## Konfiguracja klienta WireGuard

Od oprogramowania 4.0 profile WireGuard można organizować w grupy.

1. Kliknij **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/wireguard_client_add_manually.png){class="glboxshadow"}

2. Zostanie utworzona grupa.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_a_new_group.png){class="glboxshadow"}

3. Nadaj grupie opisową nazwę, np. azirevpn. Następnie możesz przesłać pliki konfiguracyjne lub dodać konfigurację ręcznie.

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/set_new_group_name.png){class="glboxshadow"}

    1. **Upload configuration files**

        Prześlij plik konfiguracyjny WireGuard i kliknij **Apply**.

        ![upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/upload_profile.png){class="glboxshadow"}

        ![after upload profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/after_upload_profile.png){class="glboxshadow"}

    2. **Manually Add Configuration**, użyj tej opcji, jeśli chcesz wkleić konfigurację WireGuard lub wypełnić poszczególne pola ręcznie.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/manually_add_configuration.png){class="glboxshadow"}

        Nadaj konfiguracji opisową nazwę, wklej jej treść i kliknij **Apply**, aby kontynuować.

        ![add wireguard by text](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_by_text.png){class="glboxshadow"}

        Możesz też dodać konfigurację, wypełniając poszczególne pola. W tym celu kliknij **Item Mode**.

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_1.png){class="glboxshadow"}

        ![add wireguard by item mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/add_wg_item_mode_2.png){class="glboxshadow"}

4. Kliknij ikonę trzech kropek, aby uruchomić, edytować lub usunąć profil.

    ![start the profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/start_the_profile.png){class="glboxshadow"}

5. Sprawdź stan połączenia, przechodząc do strony [VPN Dashboard](vpn_dashboard_v4.7.md).

    ![vpn dashboard page](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client_v4.6/set_up_wireguard_client/vpn_dashboard_wireguard_status.png){class="glboxshadow"}

---

WireGuard® jest zastrzeżonym znakiem towarowym Jasona A. Donenfelda.

---

Nadal masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
