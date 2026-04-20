# U-Boot-Version aktualisieren

## Warnung

**Das Aktualisieren von U-Boot ist sehr gefährlich und wird im Allgemeinen nicht empfohlen. Wenn dabei etwas schiefgeht, wird Ihr Gerät unbrauchbar und kann nicht wiederhergestellt werden. Führen Sie dies nur durch, wenn es notwendig ist oder Sie vom GL.iNet-Support dazu aufgefordert wurden**.

**Schalten Sie die Stromversorgung während des Aktualisierungsvorgangs NICHT aus, da das Upgrade sonst fehlschlagen und das Gerät unbrauchbar werden kann**.

## Vorbereitung

- Ein Computer mit Ethernet-Port. Falls nicht vorhanden, bereiten Sie bitte zusätzlich einen USB-Ethernet-Adapter vor.
- Ein Ethernet-Kabel.
- Laden Sie die Uboot-Datei gemäß den Anweisungen des GL.iNet-Supportteams herunter. Stellen Sie sicher, dass Sie die richtige Uboot-Datei verwenden. Wenn Sie nicht wissen, wie Sie die Uboot-Datei herunterladen, kontaktieren Sie uns per E-Mail unter support@gl-inet.com.

## Schritte zur Aktualisierung

Bitte befolgen Sie die untenstehenden Schritte, um die U-Boot-Aktualisierungsseite aufzurufen.

1. Trennen Sie den Router von der Stromversorgung. Verbinden Sie Ihren Computer mit dem **Ethernet LAN port** des Routers. Alle anderen Ports **MÜSSEN** **getrennt** bleiben.

    !!! note

        Bei einigen Modellen sind bestimmte einzelne LAN-Ports und der WAN-Port austauschbar. Bitte verwenden Sie diesen LAN-Port nicht. Verwenden Sie beim GL-MT6000 (Flint 2) zum Beispiel nicht LAN 1. Nutzen Sie stattdessen LAN 2, LAN 3 oder LAN 4.

2. Halten Sie die Reset-Taste gedrückt und schalten Sie den Router gleichzeitig ein. Wenn Ihr Router keinen Netzschalter hat, schaltet er sich automatisch ein, sobald Sie ihn an die Stromversorgung anschließen.

    Danach sehen Sie, dass eine LED einige Male in einer regelmäßigen Folge blinkt. Bitte nehmen Sie den Finger weg, nachdem sich die Folge geändert hat.
    
3. Stellen Sie die IP-Adresse Ihres Computers manuell auf **192.168.1.2** ein. Eine Schritt-für-Schritt-Anleitung für die verschiedenen Betriebssysteme finden Sie unten:

    ??? "Windows 7 / Windows 10"

        1. Gehen Sie zu **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Klicken Sie mit der rechten Maustaste auf **Local Area Connection** -> **Properties**.

        3. Klicken Sie auf **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Stellen Sie die **IP adress** manuell auf `192.168.1.2` ein.

        5. Stellen Sie die **Subnet mask** auf `255.255.255.0` ein.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Klicken Sie auf die Schaltfläche **OK**.

    ??? "Windows 11"

        7. Öffnen Sie **Settings**.

        8. Klicken Sie auf **Network & Internet**.

        9. Klicken Sie auf die Registerkarte **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Klicken Sie im Abschnitt "IP assignment" auf die Schaltfläche **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Wählen Sie die Option **Manual**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Aktivieren Sie den Schalter **IPv4 toggle**.

        13. Stellen Sie die statische **IP address** auf **192.168.1.2** ein.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Geben Sie als **Subnet mask** **255.255.255.0** an.

        15. Klicken Sie auf die Schaltfläche **Save**.

    ??? "macOS"

        16. Klicken Sie oben links auf dem Bildschirm auf das **Apple**-Symbol und wählen Sie **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Klicken Sie auf **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Klicken Sie links auf **Ethernet**, klicken Sie dann auf das Dropdown-Menü neben **Configure IPv4** und wählen Sie **Manually**. Wenn Sie einen USB-Ethernet-Adapter verwenden, wird Ethernet möglicherweise nicht angezeigt; stattdessen kann dort der Name des USB-Ethernet-Adapters erscheinen.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Geben Sie bei **IPv4 Address** `192.168.1.2`, bei **Subnet Mask** `255.255.255.0` und bei **Router** `192.168.1.1` ein und klicken Sie dann rechts unten auf die Schaltfläche Apply.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

4. **Verwenden Sie Google Chrome/Microsoft Edge, um `http://192.168.1.1/uboot.html` aufzurufen**. Achten Sie darauf, die vollständige URL einzugeben, damit keine zwischengespeicherten Vorschläge auf eine falsche Adresse verweisen.

    **Verwenden Sie NICHT Mozilla/Firefox, da Ihr Router dadurch unbrauchbar werden kann.**

    ![gl-ar750s u-boot update page](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/u-boot_update.png){class="glboxshadow" width="700"}

5. Klicken Sie auf die Schaltfläche **Choose file** und wählen Sie die heruntergeladene Uboot-Datei aus.

6. Klicken Sie auf die Schaltfläche **Update U-Boot**. Schalten Sie die Stromversorgung während des Aktualisierungsvorgangs NICHT aus. Die Aktualisierung dauert mehrere Minuten. 

7. Nach einer erfolgreichen Aktualisierung startet der Router neu. Anschließend können Sie die IP-Einstellung aus Schritt 3 wieder zurücksetzen und versuchen, über **192.168.8.1** auf das Web-Admin-Panel zuzugreifen. Wenn Sie normal auf das Web-Admin-Panel zugreifen können, bedeutet dies, dass der Router neu gestartet wurde.

    **Hinweis:** Möglicherweise müssen Sie den Inkognito-Modus verwenden oder den Browser-Cache und die Cookies löschen, um auf den Router zugreifen zu können.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [Kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
