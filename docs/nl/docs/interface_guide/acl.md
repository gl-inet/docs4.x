# ACL {#acl}

**Opmerking**: de ACL-functie is geïntroduceerd in firmware v4.9.

---

Met ACL, een afkorting van Access Control List, kun je regels maken om netwerkverkeer te beheren op basis van verbindingsprotocollen, apparaatadressen en poorten. De regels bepalen of netwerktoegang wordt toegestaan of geblokkeerd. Als meerdere ACL-regels conflicteren, past het systeem de regel met de hoogste prioriteit toe.

ACL werkt anders dan Port Forwarding: ACL staat netwerktoegang voornamelijk toe of blokkeert deze voor beveiligingsdoeleinden, terwijl Port Forwarding extern verkeer naar specifieke apparaten in je lokale netwerk doorstuurt om externe toegang tot lokale diensten mogelijk te maken.

---

Ga links in het webbeheerpaneel naar **SECURITY** -> **ACL**.

Klik rechts op de knop **Add Rule**.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Maak je ACL-regel in het pop-upvenster en klik op **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: voer een aangepaste naam voor de regel in.

- **Protocol**: geef op op welk type netwerkverkeer de regel van toepassing is. Selecteer een verbindingsprotocol uit `Any`, `TCP`, `UDP`, `TCP+UDP` en `ICMP`.

- **IP Type**: bepaal de IP-adresindeling voor netwerkverkeer. Selecteer het IP-type uit `IPv4 & IPv6`, `IPv4` en `IPv6`.

- **Source Zone**: selecteer de netwerkzone waar het verkeer vandaan komt. Beschikbare opties: `LAN`, `Guest`, `IoT` en `WAN`.

- **Source Address**: beperk de regel eventueel tot specifieke bronapparaten of IP-adressen. Je kunt een bronadres uit de vervolgkeuzelijst selecteren.

- **Destination Zone**: dit is de bestemming van het netwerkverkeer. Selecteer de doelnetwerkzone. Beschikbare opties: `LAN`, `Guest`, `IoT` en `WAN`.

- **Destination Address**: beperk de regel eventueel tot specifieke doelapparaten of IP-adressen. Je kunt een bestemmingsadres uit de vervolgkeuzelijst selecteren.

- **Action**: kies `Accept` of `Block` voor netwerkverkeer dat met deze regel overeenkomt.

- **Enable**: schakel deze regel in of uit.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
