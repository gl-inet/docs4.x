# USB-Modem funktioniert auf dem GL.iNet Router nicht richtig

Einige GL.iNet Router verfügen über USB-Ports. Benutzer können ein USB-Modem an den USB-Port anschließen, um den Internetzugang zu konfigurieren oder in Kombination mit einer weiteren Internetverbindung sogar Multi-WAN-Szenarien umzusetzen.

Es kann jedoch vorkommen, dass einige USB-Modems (z. B. der ZTE F50 Mobile Wi-Fi Hotspot) am Router nicht ordnungsgemäß verwendet werden können, was zu häufigen Verbindungsabbrüchen führt.

Die Ursache kann ein Kompatibilitätsproblem zwischen dem USB-Port des Routers (normalerweise USB 3.0) und dem 2,4G Wi-Fi sein. Dadurch wird das USB-Modem ständig getrennt und kann keine stabile Internetverbindung aufbauen.

Um dieses Problem zu beheben, können Sie die USB-Port-Spezifikation von USB 3.0 auf USB 2.0 umschalten.

Öffnen Sie das Admin Panel Ihres GL.iNet Routers und gehen Sie zu **SYSTEM -> Overview -> External Storage**.

Dort sehen Sie eine Option für den USB Protocol Switch.

![External Storage 1](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_1.png){class="glboxshadow"}

Schalten Sie auf USB 2.0 um. Anschließend wird der folgende Hinweis angezeigt. Klicken Sie auf Switch, um fortzufahren.

![External Storage 2](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_2.png){class="glboxshadow"}

Wenn als USB-Protokoll USB 2.0 angezeigt wird, wurde die Umstellung erfolgreich durchgeführt.

![External Storage 3](https://static.gl-inet.com/docs/router/en/4/faq/usb_modem_not_working_properly/external_storage_3.png){class="glboxshadow"}

Prüfen Sie anschließend, ob sich die Internetverbindung verbessert hat.

---

Verwandte Artikel

- [Kompatible Modems](https://docs.gl-inet.com/router/en/4/interface_guide/internet_cellular/#compatible-modems)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
