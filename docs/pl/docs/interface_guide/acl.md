# ACL

> Funkcja ACL została wprowadzona w firmware v4.9.

ACL, czyli Access Control List, pozwala tworzyć reguły zarządzające ruchem sieciowym na podstawie protokołów połączeń, adresów urządzeń i portów. Kontroluje, czy dostęp do sieci ma być dozwolony czy blokowany. Jeśli kilka reguł ACL jest ze sobą sprzecznych, system zastosuje regułę o wyższym priorytecie.

ACL działa inaczej niż Port Forwarding: ACL głównie zezwala na dostęp do sieci lub go blokuje w celach bezpieczeństwa, natomiast Port Forwarding przekierowuje ruch zewnętrzny do konkretnych urządzeń w sieci lokalnej, aby umożliwić zdalny dostęp do usług lokalnych.

---

W lewym panelu bocznym panelu administracyjnego przejdź do **SECURITY** -> **ACL**.

Kliknij po prawej stronie przycisk **Add Rule**.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Utwórz regułę ACL w oknie podręcznym, a następnie kliknij **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: Wprowadź własną nazwę reguły.

- **Protocol**: Określ, jakiego typu ruchu sieciowego dotyczy ta reguła. Wybierz protokół połączenia spośród `Any`, `TCP`, `UDP`, `TCP+UDP` i `ICMP`.

- **IP Type**: Określa format adresu IP dla ruchu sieciowego. Wybierz typ spośród `IPv4 & IPv6`, `IPv4` i `IPv6`.

- **Source Zone**: Wybierz strefę sieci, z której pochodzi ruch. Dostępne opcje: `LAN`, `Guest`, `IoT` i `WAN`.

- **Source Address**: (Opcjonalnie) Ogranicz regułę do określonych urządzeń źródłowych lub adresów IP. Możesz wybrać adres źródłowy z listy rozwijanej.

- **Destination Zone**: Wybierz strefę sieci, do której kierowany jest ruch. Dostępne opcje: `LAN`, `Guest`, `IoT` i `WAN`.

- **Destination Address**: (Opcjonalnie) Ogranicz regułę do określonych urządzeń docelowych lub adresów IP. Możesz wybrać adres docelowy z listy rozwijanej.

- **Action**: Wybierz, czy ruch pasujący do tej reguły ma być `Accept`, czy `Block`.

- **Enable**: Włącz lub wyłącz tę regułę.

---

Masz pytania? Odwiedź nasze [Forum społeczności](https://forum.gl-inet.com){target="_blank"} lub [Skontaktuj się z nami](https://www.gl-inet.com/contacts/){target="_blank"}.
