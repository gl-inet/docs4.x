# Użyj WireGuard do zabezpieczenia RDP z zewnętrznej sieci

Możesz potrzebować zdalnego dostępu do komputera z zewnętrznej sieci lub odwrotnie. Najbezpieczniejszym sposobem jest dostęp przez własny tunel WireGuard. Zapewnia to większe bezpieczeństwo niż używanie przekierowania portów i dostęp przez publiczny adres IP. Po skonfigurowaniu tunelu możesz użyć aplikacji **Remote Desktop** systemu Windows, aby uzyskać dostęp do komputera z dowolnego miejsca.

## Topologia

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Skonfiguruj własną sieć WireGuard

Przed użyciem tunelu WireGuard dla RDP musisz skonfigurować własny serwer WireGuard i klienta WireGuard. Możesz skonfigurować tunel za pomocą dwóch routerów GL.iNet. [Zbuduj własny domowy serwer WireGuard z dwoma routerami GL.iNet](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Zezwól serwerowi na dostęp do sieci LAN klienta

Jeśli chcesz mieć wzajemny dostęp zarówno z serwera, jak i klienta, musisz najpierw zezwolić serwerowi na dostęp do sieci LAN klienta. [Dostęp do sieci LAN klienta z serwera](wireguard_server_access_to_client_lan_side.md).

## Zezwól klientowi na dostęp do sieci LAN serwera
Następnie włącz "Allow Remote LAN Access" zarówno w VPN Dashboard serwera, jak i klienta. Szczegóły po stronie klienta kliknij [tutaj](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options); po stronie serwera kliknij [tutaj](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Skonfiguruj komputer po stronie serwera jako dostępny

### Komputer po stronie serwera

Jeśli chcesz uzyskać dostęp do komputera podłączonego do sieci LAN serwera z adresem IP **192.168.29.123**, przejdź do ustawień systemu Windows tego komputera i kliknij **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Włącz tę opcję

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Kliknij **Confirm**

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Uruchom aplikację Remote App na laptopie klienta

### Laptop po stronie klienta

Wyszukaj aplikację **Remote Desktop Connection App**

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Uruchom ją i wpisz adres IP komputera po stronie serwera **192.168.29.123** w polu.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Wprowadź dane logowania komputera po stronie serwera.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Natychmiast zdalnie sterujesz komputerem po stronie serwera.

Jeśli chcesz zrobić odwrotnie, po prostu odwróć kroki dla komputera serwera i laptopa klienta.
