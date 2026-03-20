# Wie behebe ich einen LAN-Subnetzkonflikt?

Wenn Sie ein Ethernet-Kabel von Ihrem Heimrouter mit dem WAN-Port eines GL.iNet-Routers verbinden, wird manchmal folgende Meldung angezeigt:

**"LAN subnet is in conflict with the WAN subnet. Please Change LAN Subnet to a different address."**

![conflict](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/conflict.jpg){class="glboxshadow"}

Das liegt daran, dass Ihr Heimrouter dieselbe LAN-IP wie der GL.iNet-Router verwendet. Das wird als LAN-Konflikt bezeichnet.

Befolgen Sie die folgenden Schritte, um das LAN-Subnetz zu ändern.

## 1. LAN-Subnetz ändern

Klicken Sie bitte auf den Link **Change LAN Subnet**. Sie werden dann zur Einrichtungsseite **LAN** weitergeleitet.

![change lan ip](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/change_lan_ip.png){class="glboxshadow"}

Ändern Sie die Zahl nach dem zweiten Punkt (standardmäßig **8**) in eine andere Zahl, zum Beispiel 192.168.10.1, und klicken Sie dann auf **Apply**.

Nach der Änderung warten Sie einige Sekunden. Die Seite wird aktualisiert und automatisch auf die geänderte IP-Adresse **192.168.10.1** umgeleitet. Sie sehen dann, dass der Hinweis zum Subnetzkonflikt verschwindet.

Wenn die Seite nicht umgeleitet wird, fahren Sie mit dem nächsten Schritt fort.

## 2. Mit der neuen LAN-IP anmelden

Geben Sie die geänderte LAN-IP manuell in die Adressleiste ein und drücken Sie die Eingabetaste.

![login](https://static.gl-inet.com/docs/router/en/4/faq/what_should_i_do_with_subnet_conflict/login.png){class="glboxshadow gl-90-desktop"}

Melden Sie sich mit Ihrem Admin-Passwort an. Danach verschwindet der Hinweis zum Subnetzkonflikt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
