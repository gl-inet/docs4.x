# Warum erhalte ich eine Meldung beim DDNS-Test?

Wenn Sie den DDNS-Test auf der Seite Dynamic DNS ausführen, erhalten Sie möglicherweise die unten gezeigte Meldung.

**"The IP address from DDNS domain resolution is not the same as the WAN IP of the device."**

**"You need an Internet Public IP address to use Dynamic DNS."**

![ddnstest](https://static.gl-inet.com/docs/router/en/4/faq/warning_on_ddns_test/ddnstest.jpg){class="glboxshadow"}

Es handelt sich nicht um eine **Warnung** oder einen **Fehler**, sondern um einen Hinweis auf den Netzwerkstatus Ihres Routers.

Dieses Ergebnis spiegelt in der Regel die Netzwerkposition des Routers wider. Wenn Ihr GL.iNet Router beispielsweise als sekundärer Router in Ihrem Heimnetzwerk konfiguriert ist, wird diese Meldung angezeigt.

Sie verschwindet auch dann nicht, wenn Sie auf Ihrem primären Router eine Portweiterleitung eingerichtet haben — sie zeigt lediglich an, dass sich der Router hinter NAT befindet.

Wenn Sie Dienste über NAT erreichbar machen möchten (z. B. für Fernzugriff), sind zusätzliche Einstellungen erforderlich.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
