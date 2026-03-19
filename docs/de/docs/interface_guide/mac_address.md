# MAC-Adresse

Diese Anleitung gilt für Firmware v4.5 und älter.

Seit v4.6 wurden die MAC-Adresseneinstellungen für Ethernet- und Repeater-Schnittstellen auf die Seiten [Ethernet Port](ethernet_port.md) bzw. [Repeater](internet_repeater.md) verschoben.

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **NETWORK** -> **MAC Address**.

Die Seite **MAC Address** hieß früher „MAC Clone“ und wurde ab v4.2 in „MAC Address“ umbenannt.

Auf dieser Seite können Sie die Standard-MAC-Adresse des Routers einsehen, die MAC-Adresse eines Clients klonen, eine MAC-Adresse manuell eingeben oder eine zufällige MAC-Adresse erzeugen.

Wenn das Gerät unterstützt, dass mehrere Ethernet-Ports als WAN-Ports verwendet werden, können Sie die MAC-Adresse für jeden Port separat festlegen. Beachten Sie, dass die MAC-Adresseneinstellung nur dann wirksam ist, wenn der Ethernet-Port als WAN-Port verwendet wird.

![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/mac_address.png){class="glboxshadow"}

* Die werkseitige Standard-MAC-Adresse.

    ![default mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/factory_default.png){class="glboxshadow"}

* Die MAC-Adresse eines Clients klonen.

    ![clone mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/clone.png){class="glboxshadow"}

    **Hinweis:** Viele neue Geräte verwenden inzwischen unterschiedliche zufällige MAC-Adressen, um sich mit verschiedenen Wi-Fi-Netzwerken zu verbinden. Daher entspricht die hier angezeigte MAC-Adresse möglicherweise nicht der tatsächlichen MAC-Adresse des Geräts. Diese zufällige MAC kann je nach Gerät auch als „Private Wi-Fi Address“ oder „random hardware address“ bezeichnet werden.

* Eine MAC-Adresse manuell eingeben oder eine zufällige MAC-Adresse erzeugen.

    ![Manual input or generate a random mac address](https://static.gl-inet.com/docs/router/en/4/interface_guide/mac_address/manual.png){class="glboxshadow"}

## Anwendungsszenarien

Wenn Sie sich mit einem öffentlichen Hotspot verbinden, verwenden Sie eine zufällige MAC-Adresse, wenn der Hotspot Ihre echte MAC-Adresse nicht kennen oder Ihren Internetzugang nicht anhand dieser Adresse einschränken soll. Lesen Sie dazu diese Anleitung: [Verbindung mit einem Hotspot mit Captive Portal](../faq/connect_to_a_hotspot_with_captive_portal.md).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
