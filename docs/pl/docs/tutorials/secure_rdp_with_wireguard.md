# Zabezpieczanie RDP z sieci zewnętrznej za pomocą WireGuard {#securing-rdp-from-an-external-network-with-wireguard}

Możesz potrzebować zdalnego dostępu do komputera z sieci zewnętrznej lub odwrotnie. Bezpiecznym sposobem jest użycie własnego tunelu WireGuard. Zapewnia to większe bezpieczeństwo niż przekierowanie portów i bezpośredni dostęp do komputera przez publiczny adres IP. Po skonfigurowaniu tunelu możesz użyć **Windows Remote Desktop**, aby uzyskać dostęp do komputera z dowolnego miejsca.

Ten samouczek pokazuje na przykładzie dwóch routerów GL.iNet, jak zabezpieczyć Windows RDP przez sieć WireGuard.

## Topologia {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Kroki konfiguracji {#setup-steps}

1. Skonfiguruj sieć WireGuard.

    Najpierw skonfiguruj własny serwer WireGuard i klienta WireGuard za pomocą dwóch routerów GL.iNet. Zobacz [Tworzenie własnego serwera WireGuard z dwoma routerami GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Zezwól serwerowi WireGuard na dostęp do sieci LAN klienta.

    Aby umożliwić dwukierunkowy dostęp między serwerem a klientem, najpierw zezwól serwerowi na dostęp do sieci LAN klienta. Zobacz [Dostęp do sieci LAN klienta WireGuard z serwera](wireguard_server_access_to_client_lan_side.md).

    Kroki mogą się różnić w zależności od wersji firmware.

3. Zezwól klientowi WireGuard na dostęp do sieci LAN serwera.

    Ten krok może się różnić w zależności od wersji firmware. Wybierz poniżej wersję firmware routera skonfigurowanego jako klient WireGuard.

    ??? note "Dla firmware v4.7 i starszego"

        Zaloguj się do klienta WireGuard i przejdź do **VPN** -> **VPN Dashboard**. Znajdź **VPN Server** i kliknij ikonę koła zębatego po prawej stronie.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        W wyskakującym oknie włącz **Remote Access LAN** i kliknij **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Dla firmware v4.8 i nowszego"

        Zaloguj się do klienta WireGuard i przejdź do **VPN** -> **WireGuard Server**. Kliknij **Options** w prawym górnym rogu.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        W wyskakującym oknie włącz **Allow Remote Access to the LAN Subnet** i kliknij **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Podłącz komputer, do którego chcesz uzyskać dostęp, do serwera VPN i sprawdź jego adres IP w sieci LAN.

    W poniższym przykładzie adres IP komputera po stronie serwera to **192.168.29.123**.

5. Skonfiguruj komputer po stronie serwera, aby był dostępny.

    Na komputerze po stronie serwera otwórz **System Settings** i kliknij **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Włącz **Remote Desktop** i kliknij **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Uzyskaj zdalny dostęp z laptopa po stronie klienta.

    Wyszukaj **Remote Desktop Connection** na pasku wyszukiwania.

    ![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Uruchom aplikację i wprowadź adres IP komputera po stronie serwera, np. **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Wprowadź dane logowania komputera po stronie serwera, aby się połączyć.

    ![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Możesz teraz zdalnie sterować komputerem po stronie serwera.

    Jeśli chcesz zrobić odwrotnie, po prostu odwróć kroki dla komputera serwera i laptopa klienta.

---

Masz jeszcze pytania? Odwiedź nasze [Forum społecznościowe](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
