# Firewall

Ten przewodnik dotyczy firmware v4.5 i wcześniejszych wersji.

Od wersji v4.6 strona Firewall została podzielona. Funkcje Port Forwarding i DMZ przeniesiono do [Port Forwarding](port_forwarding.md), a funkcję Open Ports przeniesiono do [Security](security.md).

---

Po lewej stronie webowego panelu administracyjnego przejdź do **NETWORK** -> **Firewall**.

Strona Firewall umożliwia konfigurację reguł zapory, takich jak **Port Forwarding**, **Open Ports on Router** i **DMZ**.

## Port Forwards

Port Forwarding umożliwia zdalnym komputerom łączenie się z lokalnym komputerem lub serwerem znajdującym się za zaporą routera w sieci LAN (na przykład z serwerem WWW lub FTP).

Aby skonfigurować przekierowanie portów, kliknij kartę **Port Forwards**, a następnie **Add**.

![firewall page](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/firewall.png){class="glboxshadow"}

W wyskakującym oknie dodaj nową regułę przekierowania portu i kliknij **Apply**.

![add new port forward rule](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_port_forward_rule.png){class="glboxshadow"}

**Name:** Nazwa reguły.

**Protocol:** Używany protokół. Możesz wybrać TCP, UDP albo jednocześnie TCP i UDP.

**External Zone:** Dostępne opcje strefy zewnętrznej to `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**External Port:** Numer lub numery portów zewnętrznych. Możesz wpisać tutaj konkretny numer portu.

**Internal Zone:** Dostępne opcje strefy wewnętrznej to `WAN`, `wgclient`, `wgserver`, `ovpnclient`, `ovpnserver`.

**Internal IP:** Adres IP przypisany przez router do urządzenia, do którego ma być możliwy zdalny dostęp.

**Internal Port:** Wewnętrzny numer portu urządzenia. Możesz wpisać konkretny numer portu. Pozostaw to pole puste, jeśli ma być taki sam jak port zewnętrzny.

**Enable:** Włącza lub wyłącza regułę.

## Open Ports on Router

Aby usługi routera, takie jak web i FTP, były publicznie dostępne, odpowiednie porty muszą zostać otwarte na routerze.

Aby otworzyć port, przejdź do karty **Open Ports on Router**, a następnie kliknij **Add**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/open_ports_on_router.png){class="glboxshadow"}

W wyskakującym oknie otwórz nowy port i kliknij **Apply**.

![open Ports on router](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/add_new_open_port.png){class="glboxshadow"}

**Name:** Nazwa reguły określana przez użytkownika.

**Protocol:** Używany protokół. Możesz wybrać TCP, UDP albo jednocześnie TCP i UDP.

**Port:** Numer portu, który chcesz otworzyć.

**Enable:** Włącza lub wyłącza regułę.

## DMZ

DMZ umożliwia wystawienie jednego komputera do Internetu, dzięki czemu wszystkie przychodzące pakiety będą przekierowywane do tego komputera.

Włącz **Enable DMZ**. Następnie wybierz wewnętrzny adres IP urządzenia hosta, które ma odbierać wszystkie przychodzące pakiety.

![Port Forwards](https://static.gl-inet.com/docs/router/en/4/tutorials/firewall/dmz.png){class="glboxshadow"}

---

Masz jeszcze pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
