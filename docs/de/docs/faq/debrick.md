# Verwenden von U-Boot zum Wiederherstellen Ihres Routers

Wenn Ihr Router durch DIY-Projekte oder das Flashen einer falschen Firmware unbrauchbar geworden ist, können Sie möglicherweise nicht mehr darauf zugreifen. In diesem Fall können Sie die Firmware mit dem U-Boot-Failsafe erneut installieren.

**Hinweis:** Durch den U-Boot-Vorgang werden die Einstellungen Ihres Routers und installierte Plugins entfernt.

---

## Vorbereitung

Bitte bereiten Sie einen Computer mit Ethernet-Anschluss vor. Wenn Ihr Computer keinen Ethernet-Anschluss hat, bereiten Sie bitte zusätzlich einen USB-Ethernet-Adapter vor.

## Schritte zur Wiederherstellung

Sehen Sie sich dieses Video-Tutorial an oder folgen Sie den unten stehenden Schritten, um auf die U-Boot-Web-Benutzeroberfläche zuzugreifen und die Firmware neu zu installieren.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>Die Schritte zur Neuinstallation der Firmware mit U-Boot sind im Wesentlichen gleich. In diesem Video wird Mudi/Mudi V2 als Beispiel verwendet. Bei anderen Modellen können Sie die unten stehenden Schritte befolgen.</small>

1. Laden Sie die Firmware [hier](https://dl.gl-inet.com/){target="_blank"} auf Ihren Computer herunter.

    Für einige Modelle, z. B. GL-AR750S-EXT, stehen zwei Firmware-Formate zur Verfügung. Verwenden Sie bitte die Firmware für U-Boot, deren Dateiendung **.img** ist.

2. Trennen Sie den Router von der Stromversorgung. Verbinden Sie Ihren Computer mit dem **Ethernet-LAN-Port** des Routers. Alle anderen Ports **MÜSSEN** unverbunden bleiben.

    !!! note

        Bei einigen Modellen sind bestimmte einzelne LAN-Ports und der WAN-Port austauschbar. Verwenden Sie diesen LAN-Port bitte nicht. Beim GL-MT6000 (Flint 2) dürfen Sie zum Beispiel nicht LAN 1 verwenden. Nutzen Sie stattdessen LAN 2, LAN 3 oder LAN 4.

3. Halten Sie die Reset-Taste gedrückt und **schalten Sie den Router gleichzeitig ein**. Wenn Ihr Router keinen Netzschalter hat, wird er automatisch eingeschaltet, sobald Sie ihn mit Strom versorgen.

    Anschließend sehen Sie, dass die LED einige Male in einer regelmäßigen Folge blinkt. Lassen Sie den Finger **erst dann** los, wenn sich diese Folge ändert.

    Im Folgenden wird die Blinkfolge der LEDs für jedes Modell beschrieben.

    **Hinweis:** Dasselbe Routermodell kann je nach Produktionsdatum unterschiedliche LED-Farben oder Blinkfolgen haben. Das hat keinen Einfluss auf den U-Boot-Vorgang. Achten Sie daher besonders auf die Änderung der blinkenden LED.

    - Bei **GL-BE9300(Flint 3)** blinkt die blaue LED 6-mal und leuchtet danach dauerhaft weiß.
    
    - Bei **GL-BE3600(Slate 7)** erscheint nach etwa 5 Sekunden gedrückter Reset-Taste ein 5-Sekunden-Countdown auf dem LED-Display. Halten Sie die Reset-Taste weiter gedrückt, bis der nächste Schritt auf dem Display angezeigt wird:

        1. Stellen Sie die IP-Adresse Ihres Computers manuell auf 192.168.1.2 ein.
        2. Rufen Sie im Browser http://192.168.1.1 auf.

        Fahren Sie anschließend mit Schritt 4 fort.

    - Bei **GL-B3000(Marble)** blinkt die blaue LED 7-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-MT6000(Flint 2)** blinkt die blaue LED 6-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-MT3000(Beryl AX)** blinkt die blaue LED 6-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-MT2500/GL-MT2500A(Brume 2)** blinkt die blaue LED 5-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-S200** blinkt die cyanfarbene LED 5-mal, leuchtet dann kurz violett und anschließend dauerhaft cyanfarben.

    - Bei **GL-A1300(Slate Plus)** blinkt die LED 5-mal langsam, bleibt dann kurz an und blinkt danach dauerhaft schnell.

    - Bei **GL-AR150**, **GL-AR300M**, **GL-USB150(Microuter)**, **GL-AR750(Creta)**, **GL-AR750S-EXT(Slate)**, **GL-X750(Spitz)**, **GL-MT300N-V2(Mango)** und **microuter-N300** blinkt die LED 5-mal.

    - Bei **GL-E750(Mudi)** zeigt das Display zuerst „Booting“, anschließend „Reset Counting 1 to 4“ und schließlich „Please Open Web 192.168.1.1“ an.

    - Bei **GL-S1300(Convexa-S)** und **GL-B1300(Convexa-B)** blinkt die LED 4-mal.
        
        Die ganz linke Power-LED kann die ganze Zeit eingeschaltet bleiben, während die ganz rechte Wi-Fi-LED 4-mal blinkt und danach die mittlere Mesh-LED dauerhaft leuchtet.
        
        (Bei einigen älteren GL-B1300 bleibt die ganz linke Power-LED die ganze Zeit eingeschaltet, während sowohl die mittlere als auch die ganz rechte LED gleichzeitig 5-mal blinken und danach dauerhaft leuchten.)

    - Bei **GL-SF1200** blinkt die 5G-LED 5-mal und leuchtet danach dauerhaft.

    - Bei **GL-AX1800(Flint)** blinkt die blaue LED 5-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-AXT1800(Slate AX)** blinkt die blaue LED 5-mal und leuchtet danach dauerhaft.

    - Bei **GL-XE300(Puli)** blinkt die LAN-LED 5-mal, danach bleibt die Wi-Fi-LED eingeschaltet.

    - Bei **GL-X300B(Collie)** blinkt die WAN-LED 5-mal, danach bleibt die Wi-Fi-LED eingeschaltet.

    - Bei **GL-X3000(Spitz AX)** blinkt die WAN-LED 5-mal, danach bleibt die Wi-Fi-LED eingeschaltet.

    - Bei **GL-XE3000(Puli AX)** blinkt die WAN-LED 5-mal, danach bleibt die Wi-Fi-LED eingeschaltet.

    - Bei **GL-SFT1200(Opal)** blinkt die blaue LED 5-mal und leuchtet danach dauerhaft weiß.

    - Bei **GL-AP1300(Cirrus)** blinkt die Power-LED 5-mal langsam, bleibt dann kurz an und blinkt danach dauerhaft schnell.

    - Bei **GL-MT1300(Beryl)** leuchtet die LED zunächst blau, blinkt zweimal langsam, blinkt dann 5-mal schneller und leuchtet anschließend dauerhaft weiß.

    - Bei **GL-B2200(Velica)** leuchten die beiden LEDs zunächst blau, wechseln dann zu weiß und blinken 5-mal, danach leuchten sie dauerhaft blau.

    - Bei **GL-MV1000/GL-MV1000W(Brume)** gibt es kein wiederholtes LED-Blinksignal. (Power- und WAN-LED bleiben die ganze Zeit eingeschaltet.)

    - Bei **GL-MiFi** blinkt die LED 6-mal.

    - Bei **GL-MT300N** und **GL-MT300A** blinkt die LED 3-mal.

4. Stellen Sie die IP-Adresse Ihres Computers manuell auf **192.168.1.2** ein. Eine Schritt-für-Schritt-Anleitung für verschiedene Betriebssysteme finden Sie unten:

    ??? "Windows 7 / Windows 10"

        1. Gehen Sie zu **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Klicken Sie mit der rechten Maustaste auf **Local Area Connection** -> **Properties**.

        3. Klicken Sie auf **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Stellen Sie die **IP-Adresse** manuell auf `192.168.1.2` ein.

        5. Stellen Sie die **Subnet mask** auf `255.255.255.0` ein.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/2/troubleshooting/src/debrick/set_ip.jpg){class="glboxshadow"}

        6. Klicken Sie auf **OK**.

    ??? "Windows 11"

        7. Öffnen Sie die Einstellungen.

        8. Klicken Sie auf **Network & Internet**.

        9. Klicken Sie auf den Reiter **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windwos11_ethernet.png){class="glboxshadow"}

        10. Klicken Sie im Abschnitt „IP assignment“ auf **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        11. Wählen Sie die Option **Manual** aus.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        12. Aktivieren Sie den Schalter **IPv4**.

        13. Stellen Sie die statische **IP address** auf **192.168.1.2** ein.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        14. Geben Sie als **Subnet mask** **255.255.255.0** an.

        15. Klicken Sie auf **Save**.

    ??? "macOS"
    
        16. Klicken Sie oben links auf das **Apple**-Symbol und wählen Sie **System Preferences** aus.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences.png){class="glboxshadow"}

        17. Klicken Sie auf **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        18. Klicken Sie links auf **Ethernet** und anschließend im Auswahlfeld neben **Configure IPv4** auf **Manually**. Wenn Sie einen USB-Ethernet-Adapter verwenden, wird Ethernet möglicherweise nicht angezeigt und stattdessen unter dem Namen des USB-Ethernet-Adapters aufgeführt.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        19. Geben Sie bei **IPv4 Address** `192.168.1.2`, bei **Subnet Mask** `255.255.255.0` und bei **Router** `192.168.1.1` ein und klicken Sie dann unten rechts auf **Apply**.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Rufen Sie im Browser **http://192.168.1.1** auf. Dies ist die U-Boot-Web-Benutzeroberfläche.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/tutorials/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note 
    
        - Wenn Sie nicht auf die U-Boot-Web-Benutzeroberfläche zugreifen können, prüfen Sie, ob VPN- oder Proxy-Software läuft. Deaktivieren Sie alle VPN- oder Proxy-Programme, einschließlich Tailscale und ZeroTier.
    
        - Die oben gezeigte U-Boot-Web-Benutzeroberfläche kann von Ihrer Ansicht abweichen, da je nach Produktionsdatum unterschiedliche U-Boot-Versionen verwendet werden. In einigen Ausnahmefällen empfehlen wir, die U-Boot-Version zu aktualisieren. Bitte lesen Sie dazu die Anleitung [hier](upgrade_uboot_version.md).

6. Klicken Sie auf **Choose file**, um die Firmware-Datei auszuwählen. Klicken Sie anschließend auf **Update firmware**.

7. Warten Sie etwa 3 Minuten. Schalten Sie das Gerät während der Aktualisierung nicht aus. Der Router ist bereit, wenn sowohl die Power- als auch die Wi-Fi-LED leuchten oder wenn Sie seine SSID auf Ihrem Gerät sehen können.

8. Stellen Sie die in Schritt 4 geänderten IP-Einstellungen wieder zurück und verbinden Sie Ihr Gerät mit dem LAN oder Wi-Fi des Routers. Anschließend können Sie wieder über **192.168.8.1** auf den Router zugreifen.

    **Hinweis:** Möglicherweise müssen Sie den Inkognito-Modus verwenden oder den Browser-Cache und die Cookies löschen, um auf den Router zugreifen zu können.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
