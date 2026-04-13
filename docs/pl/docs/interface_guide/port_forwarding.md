# Przekierowanie portów

Ta strona jest dostępna od wersji firmware v4.6. W przypadku wcześniejszych wersji zapoznaj się z sekcją [Zapora sieciowa](firewall.md).

---

W lewym panelu bocznym panelu administracyjnego przejdź do **NETWORK** -> **Port Forwarding**.

Ta strona umożliwia konfigurację reguł zapory sieciowej, takich jak **DMZ** i **Port Forwarding**.

Aby skonfigurować ustawienia **Open Ports on Router**, przejdź do SYSTEM -> Security.

## DMZ

DMZ umożliwia wystawienie jednego komputera bezpośrednio na Internet – wszystkie przychodzące pakiety zostaną przekierowane do tego komputera.

Włącz opcję **Enable DMZ**. Wybierz wewnętrzny adres IP urządzenia hosta, które ma odbierać wszystkie przychodzące pakiety.

Możesz ustawić priorytet strefy DMZ. Jeśli priorytet DMZ jest wyższy niż reguły przekierowania portów, wszystkie reguły przekierowania portów zostaną unieważnione. W przeciwnym razie żądania będą przekazywane do hosta DMZ tylko wtedy, gdy dla danego portu nie istnieje odpowiednia reguła przekierowania portów.

![dmz](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/dmz.png){class="glboxshadow"}

## Przekierowanie portów

Przekierowanie portów umożliwia zdalnym komputerom łączenie się z lokalnym komputerem lub serwerem znajdującym się za zaporą routera w sieci LAN (np. serwery WWW, serwery FTP itp.).

Aby skonfigurować przekierowanie portów, kliknij **Add** w sekcji Port Forwarding.

![port forwarding add](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add1.png){class="glboxshadow"}

W wyświetlonym oknie dodaj nową regułę przekierowania portów i kliknij **Apply**.

![add new port forwarding rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/port_forwarding/port_forwarding_add2.png){class="glboxshadow"}

**Protocol:** Używany protokół – możesz wybrać TCP, UDP lub oba jednocześnie.

**External Zone:** Dostępne opcje strefy zewnętrznej: `WAN`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `LAN`, `Guest`.

**External Port:** Numery portów zewnętrznych. Możesz podać konkretny numer portu. Zakres portów wynosi od 1 do 65535. Możesz podać pojedynczy port lub zakres portów, łącząc pierwszy i ostatni numer portu znakiem - (np. 501-510).

**Internal Zone:** Dostępne opcje strefy wewnętrznej: `LAN`, `Guest`, `WireGuard Client`, `WireGuard Server`, `OpenVPN Client`, `OpenVPN Server`, `WAN`.

**Internal IP:** Adres IP przypisany przez router urządzeniu, do którego ma odbywać się zdalny dostęp. Jeśli w polu **External Port** podano pojedynczy port, tu również podaj pojedynczy port. Jeśli podano zakres portów, tu podaj odpowiadający zakres portów.

**Internal Port:** Numer portu wewnętrznego urządzenia. Możesz podać konkretny numer portu. Pozostaw puste, jeśli jest taki sam jak port zewnętrzny.

**Description:** Nadaj nazwę lub dodaj opis reguły przekierowania portów (opcjonalne).

**Enable:** Włącz lub wyłącz regułę.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
