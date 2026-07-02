# Jak uzyskać zdalny dostęp do panelu administracyjnego WWW routera GL.iNet?

Poniższa metoda wymaga wstępnej konfiguracji, gdy nadal znajdujesz się fizycznie przy routerze.

## Metoda 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} to platforma zaprojektowana w celu uproszczenia zdalnego wdrażania i zarządzania podłączonymi urządzeniami. Zapewnia prosty sposób zdalnego dostępu do routerów GL.iNet i zarządzania nimi. Wystarczy powiązać router GL.iNet z GoodCloud, a następnie można zdalnie uzyskiwać dostęp do panelu administracyjnego WWW routera w dowolnym czasie i miejscu.

Szczegółowe informacje znajdziesz w [tym przewodniku](../interface_guide/cloud.md){target="_blank"}.

## Metoda 2. VPN

Jeśli router ma **publiczny adres IP**, możesz zdalnie uzyskać dostęp do jego panelu administracyjnego WWW przez tunel VPN. Pamiętaj, że ta metoda obejmuje zaawansowaną konfigurację i wymaga dodatkowego czasu na przygotowanie.

1. Upewnij się, że router ma publiczny adres IP. [Jak sprawdzić, czy mam publiczny adres IP?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Skonfiguruj router jako WireGuard Server. Szczegóły znajdziesz [tutaj](../interface_guide/wireguard_server.md){target="_blank"}.

3. Wyeksportuj plik konfiguracyjny z WireGuard Server do późniejszego użycia.

4. W panelu administracyjnym WWW routera przejdź do **VPN** -> **WireGuard Server** i kliknij **Options** w prawym górnym rogu. Włącz **Allow Remote Access to the LAN Subnet**, a następnie kliknij **Apply**.

5. Skonfiguruj urządzenie, z którego chcesz zdalnie uzyskiwać dostęp do routera, jako WireGuard Client, ręcznie importując plik konfiguracyjny.

    - Jeśli WireGuard Client jest urządzeniem końcowym, takim jak smartfon lub laptop, [zainstaluj aplikację WireGuard](https://www.wireguard.com/install){target="_blank"}, a następnie zaimportuj plik, aby rozpocząć połączenie.

    - Jeśli WireGuard Client jest innym routerem GL.iNet, na przykład routerem podróżnym GL.iNet, zapoznaj się z [tym przewodnikiem](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"}, aby zaimportować do niego plik konfiguracyjny i rozpocząć połączenie.

---

Masz więcej pytań? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
