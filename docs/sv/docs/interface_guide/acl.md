# ACL {#acl}

**Note**: The ACL feature was introduced in firmware v4.9.

---

ACL, en förkortning av Access Control List, låter dig skapa regler för att hantera nätverkstrafik utifrån anslutningsprotokoll, enhetsadresser och portar. Funktionen styr om nätverksåtkomst ska tillåtas eller blockeras. Om flera ACL-regler står i konflikt tillämpar systemet regeln med högst prioritet.

ACL works differently from Port Forwarding: ACL mainly allows or blocks network access for security purposes, while Port Forwarding redirects external traffic to specific devices on your local network to enable remote access to local services.

---

Öppna **SECURITY** -> **ACL** på vänster sida i webbadministrationspanelen.

Klicka på knappen **Add Rule** till höger.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Skapa ACL-regeln i popup-fönstret och klicka sedan på **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: Enter a custom name for the rule.

- **Protocol**: Ange vilken typ av nätverkstrafik regeln gäller för. Välj ett anslutningsprotokoll: `Any`, `TCP`, `UDP`, `TCP+UDP` eller `ICMP`.

- **IP Type**: Ange IP-adressformatet för nätverkstrafiken. Välj IP-typ: `IPv4 & IPv6`, `IPv4` eller `IPv6`.

- **Source Zone**: Select the network zone where traffic originates. Available options: `LAN`, `Guest`, `IoT`, and `WAN`.

- **Source Address**: (Valfritt) Begränsa regeln till vissa källenheter eller IP-adresser. Du kan välja en källadress i listrutan.

- **Destination Zone**: Anger vart nätverkstrafiken skickas. Välj målnätverkszon. Tillgängliga alternativ är `LAN`, `Guest`, `IoT` och `WAN`.

- **Destination Address**: (Valfritt) Begränsa regeln till vissa destinationsenheter eller IP-adresser. Du kan välja en destinationsadress i listrutan.

- **Action**: Choose to `Accept` or `Block` network traffic matching this rule.

- **Enable**: Toggle to enable or disable this rule.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
