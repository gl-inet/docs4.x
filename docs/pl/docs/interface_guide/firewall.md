# Firewall

Ten przewodnik dotyczy firmware v4.5 i wcześniejszych wersji.

Od wersji v4.6 strona Firewall została podzielona. Funkcje Port Forwarding i DMZ przeniesiono do [Port Forwarding](port_forwarding.md), a funkcję Open Ports przeniesiono do [Security](security.md).

---

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Firewall**.

Strona Firewall umożliwia konfigurację reguł zapory, takich jak **Port Forwarding**, **Open Ports on Router** i **DMZ**.

## Port Forwards

Port Forwarding umożliwia zdalnym komputerom łączenie się z lokalnym komputerem lub serwerem znajdującym się za zaporą routera w sieci LAN (na przykład z serwerem WWW lub FTP).

Aby skonfigurować przekierowanie portów, kliknij kartę **Port Forwards**, a następnie **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/firewall.png){class="glboxshadow"}

W wyskakującym oknie dodaj regułę przekierowania portów i kliknij **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Wprowadź nazwę reguły.

**Protocol:** Wybierz protokół: TCP, UDP lub oba.

**External Zone:** Wybierz interfejs, przez który przychodzi ruch. Dostępne opcje to `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` i `wgserver`. Opcje związane z VPN pojawiają się dopiero po skonfigurowaniu połączenia VPN.

**External Port:** Wprowadź numer portu zewnętrznego.

**Internal Zone:** Wybierz interfejs, do którego przekazywany jest ruch. Dostępne opcje to `LAN`, `WAN`, `guest`, `ovpnclient`, `ovpnserver`, `wgclient` i `wgserver`. Opcje związane z VPN pojawiają się dopiero po skonfigurowaniu połączenia VPN.

**Internal IP:** Wprowadź adres IP w sieci LAN urządzenia, do którego chcesz uzyskać zdalny dostęp.

**Internal Port:** Wprowadź numer portu wewnętrznego urządzenia. Pozostaw pole puste, jeśli jest taki sam jak port zewnętrzny.

**Enable:** Użyj przełącznika, aby włączyć lub wyłączyć regułę.

## Open Ports on Router

Aby usługi routera, takie jak web i FTP, były publicznie dostępne, odpowiednie porty muszą zostać otwarte na routerze.

Aby otworzyć port, przejdź do karty **Open Ports on Router**, a następnie kliknij **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/open_ports_on_router.png){class="glboxshadow"}

W wyskakującym oknie otwórz nowy port i kliknij **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** Nazwa reguły określana przez użytkownika.

**Protocol:** Używany protokół. Możesz wybrać TCP, UDP albo jednocześnie TCP i UDP.

**Port:** Numer portu, który chcesz otworzyć.

**Enable:** Włącza lub wyłącza regułę.

## DMZ

DMZ umożliwia wystawienie jednego komputera do Internetu, dzięki czemu wszystkie przychodzące pakiety będą przekierowywane do tego komputera.

Włącz **Enable DMZ**. Następnie wybierz wewnętrzny adres IP urządzenia hosta, które ma odbierać wszystkie przychodzące pakiety.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/interface_guide/firewall/dmz.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
