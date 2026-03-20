# Warnung Ihres Browsers: Ihre Verbindung ist nicht privat

Möglicherweise wird Ihnen bei der ersten Einrichtung Ihres GL.iNet-Routers diese Browserwarnung angezeigt: Ihre Verbindung ist nicht privat.

![alert](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/alert.jpg){class="glboxshadow"}

Dies ist eine standardmäßige Sicherheitswarnung des Browsers, wenn er eine Website ohne vertrauenswürdiges SSL/TLS-Zertifikat erkennt.

Browser sind in der Regel so konzipiert, dass sie Zertifikaten vertrauen, die von externen Zertifizierungsstellen (CAs) ausgestellt wurden. GL.iNet-Router verwenden jedoch selbstsignierte Zertifikate, die nicht von CAs ausgestellt werden. Daher stufen Browser sie als unsicher ein und zeigen diese Warnung an.

## Ist das Öffnen von 192.168.8.1 sicher?

Die Sicherheit Ihres Netzwerks hat für uns oberste Priorität. Während der Ersteinrichtung benötigen Sie keine Internetverbindung, da der gesamte Vorgang vollständig lokal abläuft.

Wenn Sie sich während der Einrichtung mit dem Wi-Fi des GL.iNet-Routers verbinden, sehen Sie möglicherweise **"Connected, No internet"**. Das ist zu erwarten, da der Router während der Konfiguration in einem eigenständigen lokalen Netzwerk arbeitet.

![nointernet](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/nointernet.jpg){class="glboxshadow"}

Ebenso ist die IP **192.168.8.1** eine private lokale IP-Adresse, die dem Router selbst zugewiesen ist. Sie wird verwendet, um auf das lokale Admin Panel des Geräts zuzugreifen, nicht auf eine öffentliche Website.

Da die Verbindung rein lokal ist und während der Einrichtung kein Internetzugang erforderlich ist, besteht **kein Risiko einer Preisgabe privater Daten**. Dadurch wird eine sichere, isolierte Umgebung für die Konfiguration Ihres Routers gewährleistet.

## Warum wird mir trotzdem eine Warnung angezeigt?

Browser unterscheiden normalerweise nicht zwischen einer voreingestellten Einrichtungs-IP-Adresse und normalen Websites. Sie behandeln alle IP-Adressen wie Websites und erwarten, dass HTTPS-Verbindungen durch SSL/TLS-Zertifikate abgesichert sind.

GL.iNet-Router verwenden zwar SSL/TLS-Zertifikate, diese sind jedoch selbstsigniert und nicht von externen Zertifizierungsstellen (CAs) ausgestellt. Obwohl der Zugriff auf diese IP sicher ist (da sie sich in einem privaten lokalen Netzwerk befindet), wird sie vom Browser dennoch als "unsicher" eingestuft, weshalb die Warnung angezeigt wird.

## Was kann ich bei dieser Warnung tun?

Klicken Sie bitte auf **Advanced** und **Continue to 192.168.8.1**.

![continue](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/continue.jpg){class="glboxshadow"}

Anschließend werden Sie zum Web-Admin-Panel weitergeleitet.

![setup](https://static.gl-inet.com/docs/router/en/4/faq/warning_from_your_browser/setup.jpg){class="glboxshadow"}

## Kann ich dem Router ein SSL-Zertifikat hinzufügen?

Ja, Sie können Ihrem GL.iNet-Router ein SSL-Zertifikat hinzufügen.

[So fügen Sie ein SSL-Zertifikat hinzu](../faq/use_https_for_adh.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.

