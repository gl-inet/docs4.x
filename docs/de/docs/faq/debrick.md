# U-Boot verwenden, um Ihren Router wiederherzustellen

Wenn Sie Ihren Router aufgrund von DIY-Projekten oder dem Flashen einer falschen Firmware beschädigt haben, kann der Zugriff fehlschlagen. In diesem Fall können Sie die Firmware über das U-Boot-Failsafe neu installieren.

**Hinweis:** Der U-Boot-Vorgang entfernt die Einstellungen Ihres Routers und installierte Plugins.

---

## Vorbereitung

Bitte bereiten Sie einen Computer oder Laptop mit einem Ethernet-Port vor. Falls Ihr Computer keinen Ethernet-Port besitzt, wird ein zusätzlicher USB-Ethernet-Adapter benötigt.

**Hinweis**: GL-E5800 (Mudi 7) unterstützt derzeit kein Firmware-Flashen über U-Boot.

## Schritte zur Wiederherstellung

Sehen Sie sich dieses Video-Tutorial an oder folgen Sie den nachstehenden Schritten, um auf die U-Boot-Web-Oberfläche zuzugreifen und die Firmware neu zu installieren.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Die Schritte zur Verwendung von U-Boot für die Neuinstallation der Firmware sind im Wesentlichen gleich, und dieses Video verwendet Mudi/Mudi V2 als Beispiel. Für andere Modelle können Sie den nachfolgenden Anweisungen folgen.</small>

1. Laden Sie die U-Boot-Firmware [hier](https://dl.gl-inet.com/){target="_blank"} auf Ihren Computer herunter.

    Einige Modelle bieten zwei Firmware-Varianten. Bitte laden Sie die U‑Boot-kompatible Firmware herunter.

2. Schalten Sie Ihren Router aus. Verbinden Sie einen Computer mit dem **Ethernet-LAN-Port** des Routers und lassen Sie alle anderen Ports unverbunden.

    !!! note

        Bei einigen Modellen kann ein bestimmter einzelner LAN-Port auf WAN umgeschaltet werden. Bitte verwenden Sie diesen LAN-Port nicht zum Flashen der Firmware. Zum Beispiel beim GL-MT6000 (Flint 2) verwenden Sie nicht LAN 1. Bitte verwenden Sie stattdessen LAN 2, LAN 3 oder LAN 4.

3. Drücken und halten Sie die Reset-Taste fest, **schalten Sie gleichzeitig den Router ein**. Falls Ihr Router keinen Power-Schalter hat, wird das Einstecken des Netzsteckers ihn automatisch einschalten.

    Warten Sie, bis die LED mehrmals in einer regelmäßigen Sequenz blinkt. Lassen Sie die Reset-Taste **nach** dem Wechsel des Blinkmusters los.

    !!! note "LED-Blinkmuster nach Gerätemodell"

        **Hinweis:** Identische Router-Modelle aus verschiedenen Produktionschargen können unterschiedliche LED-Farben oder Blinksequenzen aufweisen. Dies beeinflusst den U-Boot-Wiederherstellungsprozess nicht. Bitte achten Sie auf die Änderung des LED-Blinkzustands.

        - Für **GL-MT3600BE (Beryl 7)**: Die blaue LED blinkt 7-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-MT5000 (Brume 3)**: Die Power-LED blinkt 7-mal blau, dann leuchtet sie dauerhaft weiß.

        - Für **GL-BE6500 (Flint 3e)**: Die blaue LED blinkt 6-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-BE9300 (Flint 3)**: Die blaue LED blinkt 6-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-BE3600 (Slate 7)**: Nach etwa 5 Sekunden gedrückter Reset-Taste erscheint ein 5-Sekunden-Countdown auf dem Touchscreen. Halten Sie die Reset-Taste weiter gedrückt, bis die nächste Aufforderung auf dem Bildschirm erscheint, z. B. die IP-Adresse Ihres Computers manuell auf 192.168.1.2 setzen und mit dem Browser http://192.168.1.1 besuchen. Fahren Sie mit Schritt 4 fort.

        - Für **GL-X2000 (Spitz Plus)**: Die Internet-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-B3000 (Marble)**: Die blaue LED blinkt 7-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-MT6000 (Flint 2)**: Die blaue LED blinkt 6-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-MT3000 (Beryl AX)**: Die blaue LED blinkt 6-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-MT2500/GL-MT2500A (Brume 2)**: Die Power-LED blinkt 5-mal blau, dann leuchtet sie dauerhaft weiß.

        - Für **GL-X3000 (Spitz AX)**: Die Internet-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-XE3000 (Puli AX)**: Die Internet-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-XE300 (Puli)**: Die LAN-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-E750 (Mudi)**: Auf dem Bildschirm wird zunächst „Booting" angezeigt, gefolgt von „Reset Counting 1 to 4" und schließlich „Please Open Web 192.168.1.1".

        - Für **GL-X750 (Spitz)**: Die Internet-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-AX1800 (Flint)**: Die blaue LED blinkt 5-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-AXT1800 (Slate AX)**: Die blaue LED blinkt 5-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-SFT1200 (Opal)**: Die blaue LED blinkt 5-mal, dann leuchtet sie dauerhaft weiß.

        - Für **GL-MT1300 (Beryl)**: Die blaue LED blinkt zweimal langsam, dann blinkt sie 5-mal schneller und leuchtet dauerhaft weiß.

        - Für **GL-A1300 (Slate Plus)**: Die LED blinkt 5-mal langsam, bleibt dann kurz an, dann blinkt sie die ganze Zeit schnell.

        - Für **GL-MT300N-V2 (Mango)** und **GL-AR300M (Shadow)**: Die LED blinkt 5-mal.

        - Für **GL-X300B (Collie)**: Die WAN-LED blinkt 5-mal, dann bleibt die Wi-Fi-LED an.

        - Für **GL-AP1300 (Cirrus)**: Die Power-LED blinkt 5-mal langsam, bleibt dann kurz an, dann blinkt sie die ganze Zeit schnell.

        - Für **GL-B1300 (Convexa-B)** und **GL-S1300 (Convexa-S, EOL)**: Die LED blinkt 4-mal.

            Die ganz linke Power-LED bleibt die ganze Zeit an, während die ganz rechte Wi-Fi-LED 4-mal blinkt, dann leuchtet die mittlere Mesh-LED dauerhaft.

            (Bei einigen älteren GL-B1300 bleibt die ganz linke Power-LED die ganze Zeit an, und sowohl die mittlere LED als auch die ganz rechte LED blinken gleichzeitig 5-mal, dann bleiben sie an.)

        - Für **GL-B2200 (Velica)**: Die beiden LEDs starten blau, werden dann weiß und blinken 5-mal, dann leuchten sie dauerhaft blau.

        - Für **GL-SF1200**: Die 5G-LED blinkt 5-mal, dann leuchtet sie dauerhaft.

        - Für **GL-S200** blinkt die cyan-farbene LED 5-mal, wird dann kurz violett, dann leuchtet sie dauerhaft cyan.

        - Für **GL-AR750 (Creta)** und **GL-AR750S-EXT (Slate)**: Die LED blinkt 5-mal.

        - Für **GL-USB150 (Microuter)**, **microuter-N300** und **GL-AR150 (White)**: Die LED blinkt 5-mal.

        - Für **GL-MV1000/GL-MV1000W (Brume)**: Keine wiederholten LED-Blinksignale. Power- und WAN-LEDs bleiben die ganze Zeit an.

        - Für **GL-MiFi**: Die LED blinkt 6-mal.

        - Für **GL-MT300N** und **GL-MT300A**: Die LED blinkt 3-mal.

4. Setzen Sie die IP-Adresse Ihres Computers manuell auf **192.168.1.2**. Bitte prüfen Sie die schrittweise Anleitung für verschiedene Betriebssysteme unten:

    ??? "Windows 7 / Windows 10"

        1. Gehen Sie zu **Systemsteuerung** -> **Netzwerk und Internet** -> **Netzwerk- und Freigabecenter** -> **Adaptereinstellungen ändern**.

        2. Rechtsklick auf **LAN-Verbindung** -> **Eigenschaften**.

        3. Klicken Sie auf **Internetprotokoll, Version 4 (TCP/IPv4)** -> **Eigenschaften**.

        4. Setzen Sie die **IP-Adresse** manuell auf `192.168.1.2`.

        5. Setzen Sie die **Subnetzmaske** auf `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Klicken Sie auf die Schaltfläche **OK**.

    ??? "Windows 11"

        7. Öffnen Sie Einstellungen.

        8. Klicken Sie auf **Netzwerk & Internet**.

        9. Klicken Sie auf die Registerkarte **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Klicken Sie unter dem Abschnitt „IP-Zuweisung" auf die Schaltfläche **Bearbeiten**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Wählen Sie die Option **Manuell**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Schalten Sie den **IPv4-Schalter** ein.

        13. Setzen Sie die statische **IP-Adresse** auf **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Geben Sie die **Subnetzmaske** als **255.255.255.0** an.

        15. Klicken Sie auf die Schaltfläche **Speichern**.

    ??? "macOS"

        16. Klicken Sie auf das **Apple**-Symbol in der oberen linken Ecke des Bildschirms und wählen Sie **Systemeinstellungen**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Klicken Sie auf **Netzwerk**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Klicken Sie links auf **Ethernet** und dann auf die Dropdown-Box neben **IPv4 konfigurieren** und wählen Sie **Manuell**. Falls Sie einen USB-Ethernet-Adapter verwenden, wird Ethernet möglicherweise nicht gefunden und es kann unter dem Namen des USB-Ethernet-Adapters angezeigt werden.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Geben Sie die **IPv4-Adresse** mit `192.168.1.2`, **Subnetzmaske** mit `255.255.255.0`, **Router** mit `192.168.1.1` ein und klicken Sie dann auf die Schaltfläche „Anwenden" in der unteren rechten Ecke.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Verwenden Sie einen Browser, um **http://192.168.1.1** zu besuchen. Dies ist die U-Boot-Web-Oberfläche.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note

        - Falls Sie nicht auf die U-Boot-Web-Oberfläche zugreifen können, prüfen Sie, ob Sie VPN- oder Proxy-Software verwenden. Deaktivieren Sie jegliche VPN- oder Proxy-Software, einschließlich Tailscale und ZeroTier.

        - Die oben gezeigte U-Boot-Web-Oberfläche entspricht möglicherweise nicht genau dem, was Sie sehen, da die U-Boot-Version für verschiedene Produktionsdaten unterschiedlich ist. In einigen Extremfällen empfehlen wir, die U-Boot-Version zu aktualisieren. Bitte beziehen Sie sich auf das Tutorial [hier](upgrade_uboot_version.md).

6. Klicken Sie auf die Schaltfläche **Choose file**, um die Firmware-Datei zu finden. Klicken Sie dann auf die Schaltfläche **Update firmware**.

7. Warten Sie etwa 3 Minuten. Schalten Sie Ihr Gerät während des Firmware-Updates nicht aus.

    Der Router ist bereit, wenn die LED kontinuierlich blau blinkt; bei einigen Mobilfunkmodellen ist er bereit, sobald sowohl die Power- als auch die Wi‑Fi-LEDs dauerhaft leuchten.

8. Machen Sie die IP-Einstellungen aus Schritt 4 rückgängig und verbinden Sie Ihren Computer mit dem LAN oder Wi-Fi des Routers. Sie können dann über **192.168.8.1** wieder auf das Web-Admin-Panel des Routers zugreifen.

    **Hinweis:** Es kann erforderlich sein, den Inkognito-Modus zu verwenden oder den Browser-Cache und Cookies zu löschen, um auf den Router zuzugreifen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
