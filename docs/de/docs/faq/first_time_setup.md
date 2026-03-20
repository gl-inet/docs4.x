# Ersteinrichtung

Die erste Einrichtung eines GL.iNet-Routers ist sehr ähnlich. Die meisten Modelle verfügen über ein Wi-Fi-Modul, einige jedoch nicht.

Daher ist die folgende Anleitung je nach Vorhandensein eines Wi-Fi-Moduls in zwei Fälle unterteilt.

* [Für Modelle mit Wi-Fi](#für-modelle-mit-wi-fi)
* [Für Modelle ohne Wi-Fi](#für-modelle-ohne-wi-fi)

## Für Modelle mit Wi-Fi

Hier verwenden wir GL-AXT1800 (Slate AX) als Beispiel.

Bitte legen Sie die folgenden im Paket enthaltenen Artikel bereit.

- GL-AXT1800
- Ein Netzteil
- Ein Ethernet-Kabel

Sehen Sie sich diese Videoanleitung an oder folgen Sie den nachstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Dieses Video verwendet zur Demonstration der Einrichtung einen anderen GL.iNet-Router, da die Schritte bei den meisten Routermodellen gleich sind.)</small>

1. Einschalten

    Wenn Sie eine TF-Karte verwenden möchten, setzen Sie sie bitte vor dem Einschalten des Routers ein. Hot-Swapping von TF-Karten wird nicht unterstützt.

    Stecken Sie ein Ende des Netzteils in den Router und das andere Ende in eine Steckdose. Der Router schaltet sich automatisch ein.

2. Mit dem Router verbinden

    Sie können sich über ein Ethernet-Kabel oder über Wi-Fi mit dem Router verbinden.

    * Verbindung per Kabel

        Verbinden Sie Ihren Computer über ein Ethernet-Kabel mit dem LAN-Port des Routers.

    * Verbindung über Wi-Fi

        Die Wi-Fi-SSID ist auf dem Etikett an der Unterseite des Routers in den folgenden Formaten aufgedruckt:

        **GL-AXT1800-XXX** oder **GL-AXT1800-XXX-5G**

        Der standardmäßige Wi-Fi Key befindet sich unterhalb der SSID.

        Suchen Sie auf Ihrem Computer, Telefon oder Tablet nach der SSID des Routers und geben Sie dann den Wi-Fi Key ein. Wenn sich das Wi-Fi-Passwort bei einigen Modellen nicht auf dem Etikett finden lässt, versuchen Sie bitte "**goodlife**".

        **Tipp:** Der QR-Code auf dem Etikett an der Unterseite enthält die standardmäßigen Wi-Fi-Informationen. Sie können die Verbindung schnell herstellen, indem Sie ihn mit dem QR-Code-Scanner Ihres Telefons scannen.

        **Hinweis:** Nach der Verbindung mit dem Wi-Fi haben Sie möglicherweise nicht sofort Internetzugang. Folgen Sie bitte zuerst dem nächsten Schritt, um Ihr Netzwerk zu konfigurieren, bevor Sie auf das Internet zugreifen.

3. Am web Admin Panel anmelden

    Öffnen Sie einen Webbrowser (wir empfehlen Chrome, Edge oder Safari) und rufen Sie [http://192.168.8.1](http://192.168.8.1) auf. Sie werden zur Ersteinrichtung des web Admin Panel weitergeleitet.
    
    Wenn Sie nicht auf das web Admin Panel zugreifen können, lesen Sie bitte [hier](cannot_access_web_admin_panel.md) nach.

    Wählen Sie eine Sprache aus und klicken Sie auf **Next**, um fortzufahren.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login.png){class="glboxshadow"}

    Richten Sie ein Admin-Passwort ein. Wir empfehlen die Verwendung eines sicheren Passworts. Klicken Sie auf **Apply**, um fortzufahren.

    **Hinweis**: Während der Initialisierung kann Wi-Fi ausgeschaltet werden. Stellen Sie bitte sicher, dass Sie die Verbindung zum Router erneut herstellen.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Nach der Ersteinrichtung gelangen Sie in das web Admin Panel des Routers.

    ![admin panel of gl-axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-axt1800.png){class="glboxshadow"}

4. Mit dem Internet verbinden

    * [Über ein Ethernet-Kabel mit dem Internet verbinden](../interface_guide/internet_ethernet.md)
    * [Über ein vorhandenes Wi-Fi mit dem Internet verbinden](../interface_guide/internet_repeater.md)
    * [Über USB-Tethering mit dem Internet verbinden](../interface_guide/internet_tethering.md)
    * [Über ein USB-Modem mit dem Internet verbinden](../interface_guide/internet_cellular.md)

## Für Modelle ohne Wi-Fi

Hier verwenden wir GL-MT2500A (Brume 2) als Beispiel.

1. Einschalten

    Stecken Sie ein Ende des Netzteils in den Router und das andere Ende in eine Steckdose. Der Router schaltet sich automatisch ein.

2. Mit dem Router verbinden

    Sie können sich über ein Ethernet-Kabel oder über Wi-Fi mit dem Router verbinden.

    * Direkte Verbindung über Ethernet-Kabel

        Verbinden Sie Ihren Computer über ein Ethernet-Kabel mit dem LAN-Port des Routers. Dies ist die empfohlene Konfigurationsmethode, da sie einfach und unkompliziert ist.

    * Verbindung über das Wi-Fi eines anderen Routers

        Da GL-MT2500A kein integriertes Wi-Fi-Modul hat, können wir einen anderen Router mit Wi-Fi-Funktion verwenden, um den GL-MT2500A zu initialisieren.

        * Methode 1: Stellen Sie den zweiten Router in den AP (Access Point)-Modus und verbinden Sie dann den LAN-Port des GL-MT2500A mit dem WAN-Port des zweiten Routers.

        * Methode 2: Belassen Sie den zweiten Router im Standard-Routermodus, jedoch mit einer anderen Router-IP-Adresse, die nicht mit 192.168.8.1/24 kollidiert, z. B. 192.168.10.1. Verbinden Sie dann den LAN-Port des GL-MT2500A mit dem WAN-Port des zweiten Routers.

        Verwenden Sie Ihren Computer oder Ihr Smartphone, um sich mit dem Wi-Fi des zweiten Routers zu verbinden.

        !!! Note
        
            Der hier erwähnte zweite Router ist ein normaler Router, z. B. ein GL.iNet GL-AXT1800, TP-LINK- oder Netgear-Router. Modems, optische Netzabschlüsse (Optical Network Terminals) oder von Internetanbietern bereitgestellte Geräte funktionieren in diesem Szenario möglicherweise nicht.

3. Auf das web Admin Panel zugreifen

    Öffnen Sie einen Webbrowser (wir empfehlen Chrome, Edge, Safari) und rufen Sie [http://192.168.8.1](http://192.168.8.1) auf. Sie werden zur Ersteinrichtung des web Admin Panel weitergeleitet. Wenn Sie nicht auf das web Admin Panel zugreifen können, lesen Sie bitte [hier](cannot_access_web_admin_panel.md) nach.

    Wählen Sie eine Sprache aus und klicken Sie auf **Next**, um fortzufahren.

    ![Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_first_time_login_gl-mt2500.png){class="glboxshadow"}

    Richten Sie ein Admin-Passwort ein. Wir empfehlen die Verwendung eines sicheren Passworts. Klicken Sie auf **Submit**, um fortzufahren.

    ![set up admin password](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/set_up_your_admin_password_gl-mt2500.png){class="glboxshadow"}

    Nach der Ersteinrichtung gelangen Sie in das web Admin Panel des Routers.

    ![admin panel of gl-mt2500](https://static.gl-inet.com/docs/router/en/4/tutorials/first_time_setup/admin_panel_gl-mt2500.png){class="glboxshadow"}

4. Mit dem Internet verbinden

    * [Über ein Ethernet-Kabel mit dem Internet verbinden](../interface_guide/internet_ethernet.md)
    * [Über USB-Tethering mit dem Internet verbinden](../interface_guide/internet_tethering.md)
    * [Über ein USB-Modem mit dem Internet verbinden](../interface_guide/internet_cellular.md)

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
