# Jak połączyć się z Surfshark z dedykowanym IP na routerach GL.iNet?

Ten artykuł przedstawia kroki konfiguracji połączenia Surfshark z dedykowanym IP na routerach GL.iNet.

Używamy GL-AXT1800 jako przykładu.

1. Zaloguj się do swojego konta Surfshark, następnie wybierz **Dedicated IP**.

    ![manualdip](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/manualdip.jpg){calss="glboxshadow"}

2. W sekcji Dedicated IP kliknij **Settings**.

    ![setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/setting.jpg){calss="glboxshadow"}

3. Wybierz protokół (WireGuard lub OpenVPN) i pobierz pliki konfiguracyjne do ręcznego połączenia.

    ![protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/protocol.jpg){calss="glboxshadow"}
    
    W przypadku konfiguracji WireGuard strona pobierania wyświetla adres IP serwera i klucz publiczny serwera, jak pokazano poniżej.
    
    ![loadwg](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireguard_client/set_up_surfshark_dip/loadwg.jpg){calss="glboxshadow"}

    W przypadku konfiguracji OpenVPN strona pobierania wyświetla adres IP serwera i dane logowania (nazwa użytkownika i hasło), jak pokazano poniżej. Skopiuj dane logowania do późniejszego użycia.
    
    ![loadovpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/loadovpn.jpg){calss="glboxshadow"}

4. Zapoznaj się z poniższymi linkami, aby przesłać pliki konfiguracyjne do routera GL.iNet. W razie potrzeby wprowadź dane logowania.

    - [Prześlij konfigurację WireGuard](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers)

    - [Prześlij konfigurację OpenVPN](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers)

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
