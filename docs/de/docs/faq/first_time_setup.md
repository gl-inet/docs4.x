# Ersteinrichtung

Die Ersteinrichtung von GL.iNet-Routern ist sehr ähnlich. Die meisten Modelle verfügen über ein Wi-Fi-Modul, einige jedoch nicht.

Daher ist die folgende Anleitung je nach Vorhandensein eines Wi-Fi-Moduls in zwei Fälle unterteilt.

* [Für Modelle mit Wi-Fi](#für-modelle-mit-wi-fi)
* [Für Modelle ohne Wi-Fi](#für-modelle-ohne-wi-fi)

## Für Modelle mit Wi-Fi

Die folgenden Schritte verwenden den GL-MT3000 (Beryl AX) als Beispiel.

Bitte halten Sie die folgenden im Lieferumfang enthaltenen Teile bereit.

- Einen Router GL-MT3000 (Beryl AX)
- Ein Netzteil
- Ein Ethernet-Kabel

Sehen Sie sich diese Videoanleitung an oder folgen Sie den nachstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WW8wGk68lEU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. **Einschalten**

    Stecken Sie ein Ende des Netzteils in den Router und das andere Ende in eine Steckdose. Der Router schaltet sich automatisch ein.
    
    Einige Modelle (z. B. Slate AX) sind mit einem TF-Kartensteckplatz ausgestattet. Wenn Sie eine TF-Karte verwenden müssen, setzen Sie die Karte vor dem Einschalten des Routers ein. Hot-Swapping von TF-Karten wird nicht unterstützt.

2. **Mit dem Router verbinden**

    Verbinden Sie ein Gerät (z. B. Smartphone, Laptop oder Computer) per Ethernet-Kabel oder per Wi-Fi mit dem Router.

    * Verbindung per Ethernet: Verbinden Sie ein Gerät über ein Ethernet-Kabel mit dem LAN-Port des Routers.

    * Verbindung per Wi-Fi: Suchen Sie die Wi-Fi-SSID und den Wi-Fi Key auf dem Etikett an der Unterseite des Routers. Suchen Sie auf Ihrem Gerät nach der SSID des Routers und geben Sie anschließend den Wi-Fi Key ein.

        !!! tip
        
            1. Der QR-Code auf dem Etikett an der Unterseite enthält die standardmäßigen Wi-Fi-Informationen. Sie können die Verbindung schnell herstellen, indem Sie ihn mit einem QR-Code-Scanner scannen.
            2. Wenn der Wi-Fi Key bei einigen älteren Modellen nicht auf dem Etikett zu finden ist, versuchen Sie "goodlife".
        
    Nach der Verbindung mit dem Wi-Fi haben Sie möglicherweise nicht sofort Internetzugang. Folgen Sie bitte zuerst dem nächsten Schritt, um Ihr Netzwerk zu konfigurieren, bevor Sie auf das Internet zugreifen.

3. **Am web Admin Panel anmelden**

    Öffnen Sie einen Webbrowser (Chrome, Edge und Safari werden für bessere Kompatibilität empfohlen) und rufen Sie [http://192.168.8.1](http://192.168.8.1) auf. Sie werden zur GL.iNet-Anmeldeseite weitergeleitet. Wenn Sie nicht auf das web Admin Panel zugreifen können, klicken Sie zur Fehlerbehebung [hier](cannot_access_web_admin_panel.md).

    Richten Sie Ihr Admin-Passwort ein und klicken Sie anschließend auf **Next**.

    ![mt3000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_password.png){class="glboxshadow"}

    Richten Sie Ihr Wi-Fi ein. Wenn Sie die Wi-Fi-Informationen ändern, stellen Sie sicher, dass Sie sich erneut mit dem aktualisierten Wi-Fi verbinden, und klicken Sie dann auf **Next**

    ![mt3000 set up wifi](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_set_up_wifi.png){class="glboxshadow"}

    Warten Sie, bis der Router die Initialisierung abgeschlossen hat.

    ![mt3000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_initializing.png){class="glboxshadow"}

    Anschließend greifen Sie auf das web Admin Panel Ihres Routers zu.

    ![mt3000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt3000_admin_panel.png){class="glboxshadow"}

4. **Mit dem Internet verbinden**

    * [Über ein Ethernet-Kabel mit dem Internet verbinden](../interface_guide/internet_ethernet.md)
    * [Über ein vorhandenes Wi-Fi mit dem Internet verbinden](../interface_guide/internet_repeater.md)
    * [Über USB-Tethering mit dem Internet verbinden](../interface_guide/internet_tethering.md)
    * [Über ein USB-Modem mit dem Internet verbinden](../interface_guide/internet_cellular.md)

## Für Modelle ohne Wi-Fi

Die folgenden Schritte verwenden den GL-MT5000 (Brume 3) als Beispiel.

1. **Einschalten**

    Stecken Sie ein Ende des Netzteils in den Router und das andere Ende in eine Steckdose. Der Router schaltet sich automatisch ein.

2. **Mit dem Router verbinden**

    Verbinden Sie ein Gerät (z. B. Laptop oder Computer) über ein Ethernet-Kabel mit dem LAN-Port des Routers.

3. **Am web Admin Panel anmelden**

    Öffnen Sie einen Webbrowser (Chrome, Edge und Safari werden für bessere Kompatibilität empfohlen) und rufen Sie [http://192.168.8.1](http://192.168.8.1) auf. Sie werden zur GL.iNet-Anmeldeseite weitergeleitet. Wenn Sie nicht auf das web Admin Panel zugreifen können, klicken Sie zur Fehlerbehebung [hier](cannot_access_web_admin_panel.md).

    Richten Sie Ihr Admin-Passwort ein und klicken Sie anschließend auf **Next**.

    ![mt5000 set up admin password](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_password.png){class="glboxshadow"}

    Warten Sie, bis der Router die Initialisierung abgeschlossen hat.

    ![mt5000 initializing](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_initializing.png){class="glboxshadow"}

    Anschließend greifen Sie auf das web Admin Panel Ihres Routers zu.

    ![mt5000 admin panel](https://static.gl-inet.com/docs/router/en/4/faq/first_time_setup/mt5000_admin_panel.png){class="glboxshadow"}

4. **Mit dem Internet verbinden**

    * [Über ein Ethernet-Kabel mit dem Internet verbinden](../interface_guide/internet_ethernet.md)
    * [Über USB-Tethering mit dem Internet verbinden](../interface_guide/internet_tethering.md)
    * [Über ein USB-Modem mit dem Internet verbinden](../interface_guide/internet_cellular.md)

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
