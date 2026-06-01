# ACL

> Die ACL-Funktion wurde mit Firmware v4.9 eingeführt.

ACL, kurz für Access Control List, ermöglicht es Ihnen, Regeln zu erstellen, um den Netzwerkverkehr anhand von Verbindungsprotokollen, Geräteadressen und Ports zu verwalten. Damit steuern Sie, ob der Netzwerkzugriff erlaubt oder blockiert wird. Wenn mehrere ACL-Regeln miteinander in Konflikt stehen, wendet das System die Regel mit der höheren Priorität an.

ACL arbeitet anders als Port Forwarding: ACL erlaubt oder blockiert Netzwerkzugriff hauptsächlich zu Sicherheitszwecken, während Port Forwarding externen Datenverkehr an bestimmte Geräte in Ihrem lokalen Netzwerk weiterleitet, um Fernzugriff auf lokale Dienste zu ermöglichen.

---

Gehen Sie in der Web-Adminoberfläche auf der linken Seite zu **SECURITY** -> **ACL**.

Klicken Sie rechts auf die Schaltfläche **Add Rule**.

![acl add rule 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule1.png){class="glboxshadow"}

Erstellen Sie im Pop-up-Fenster Ihre ACL-Regel und klicken Sie dann auf **Apply**.

![acl add rule 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/acl/add_rule2.png){class="glboxshadow"}

- **Name**: Geben Sie einen benutzerdefinierten Namen für die Regel ein.

- **Protocol**: Legen Sie fest, auf welchen Netzwerkverkehrstyp diese Regel angewendet wird. Wählen Sie ein Verbindungsprotokoll aus `Any`, `TCP`, `UDP`, `TCP+UDP` und `ICMP`.

- **IP Type**: Definiert das IP-Adressformat für den Netzwerkverkehr. Wählen Sie den IP-Typ aus `IPv4 & IPv6`, `IPv4` und `IPv6`.

- **Source Zone**: Wählen Sie die Netzwerkzone, aus der der Datenverkehr stammt. Verfügbare Optionen: `LAN`, `Guest`, `IoT` und `WAN`.

- **Source Address**: (Optional) Beschränken Sie die Regel auf bestimmte Quellgeräte oder IP-Adressen. Sie können eine Quelladresse aus der Dropdown-Liste auswählen.

- **Destination Zone**: Hierhin ist der Netzwerkverkehr gerichtet. Wählen Sie die Ziel-Netzwerkzone. Verfügbare Optionen: `LAN`, `Guest`, `IoT` und `WAN`.

- **Destination Address**: (Optional) Beschränken Sie die Regel auf bestimmte Zielgeräte oder IP-Adressen. Sie können eine Zieladresse aus der Dropdown-Liste auswählen.

- **Action**: Wählen Sie, ob der zu dieser Regel passende Netzwerkverkehr `Accept` oder `Block` sein soll.

- **Enable**: Aktivieren oder deaktivieren Sie diese Regel.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
