# WLAN (Firmware v4.9)

> Diese Anleitung gilt für Firmware v4.9 und höher. Für frühere Versionen klicken Sie bitte [hier](wireless.md).

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **WIRELESS**.

Auf der Wireless-Seite können Sie verschiedene Wi-Fi-Netzwerke konfigurieren, darunter MLO Wi-Fi (bei ausgewählten Modellen verfügbar), Main Network, Guest Network und IoT Network. Die unterstützten Wi-Fi-Bänder variieren je nach Modell.

## Multi-Link Operation (MLO)

??? "Unterstützte Modelle"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Nicht unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) ist eine der Kernfunktionen von Wi-Fi 7 (802.11be). Es wurde entwickelt, um die Netzwerkleistung zu verbessern, die Latenz deutlich zu verringern und die Verbindungsstabilität zu erhöhen, indem mehrere Frequenzbänder wie 2,4 GHz, 5 GHz und 6 GHz gleichzeitig genutzt werden.

Es wird empfohlen, Wi-Fi-7-Clients mit MLO Wi-Fi zu verbinden, da dies den Netzwerkdurchsatz und die Zuverlässigkeit durch Mehrbandverbindungen deutlich verbessert.

Klicken Sie auf **Add**, um ein MLO-Wi-Fi-Netzwerk einzurichten, und anschließend auf **Apply**. Beachten Sie, dass die verfügbaren Wi-Fi-Bänder je nach Modell variieren.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: Wählen Sie mindestens zwei Funkbänder aus.
- Wi-Fi Security: Wenn das 6-GHz-Band ausgewählt ist, ist WPA3-SAE die einzige verfügbare und empfohlene Option. Sie funktioniert mit den meisten MLO-fähigen Geräten am besten.
- Enable Randomized BSSID: Wenn das 6-GHz-Band ausgewählt ist, wird die 6-GHz-BSSID des MLO Wi-Fi mit dem Main Wi-Fi synchronisiert.

Nach der Aktivierung wird die Seite wie folgt angezeigt.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/mlo3.png){class="glboxshadow"}

## Main Network

Das Main Network ist Ihr primäres Wi-Fi-Netzwerk und unterstützt die gleichzeitige Ausstrahlung über verschiedene Funkbänder, die standardmäßig alle aktiviert sind. Sie können für jedes Band separate Einstellungen konfigurieren, z. B. Wi-Fi-SSID, Sicherheitsmodus, Passwort, Randomized BSSID, TX-Leistung, Bandbreite und Kanal.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main.png){class="glboxshadow"}

Klicken Sie rechts auf das Zahnradsymbol, um die Wi-Fi-Einstellungen für jedes Band anzuzeigen oder zu ändern. Beachten Sie, dass die verfügbaren Wi-Fi-Bänder je nach Modell variieren.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/main_2.4g.png){class="glboxshadow"}

## Guest Network

Das Guest Network ist ein dediziertes Wi-Fi-Netzwerk für Besucher; standardmäßig sind alle Bänder deaktiviert. Sie können für jedes Band grundlegende Netzwerkeinstellungen aktivieren und konfigurieren, z. B. Wi-Fi-SSID, Sicherheitsmodus, Passwort und Randomized BSSID.

Klicken Sie auf **Add**, um ein Guest-Wi-Fi-Netzwerk einzurichten, und anschließend auf **Apply**. Beachten Sie, dass die verfügbaren Wi-Fi-Bänder je nach Modell variieren.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest2.png){class="glboxshadow"}

Nach der Aktivierung wird die Seite wie folgt angezeigt.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/guest3.png){class="glboxshadow"}

## IoT Network

Das IoT Network ist ein dediziertes Wi-Fi-Netzwerk für Smart-Home-Geräte; standardmäßig sind alle Bänder deaktiviert. Sie können für jedes Band grundlegende Netzwerkeinstellungen aktivieren und konfigurieren, z. B. Wi-Fi-SSID, Sicherheitsmodus, Passwort und Randomized BSSID.

Klicken Sie auf **Add**, um ein IoT-Wi-Fi-Netzwerk einzurichten, und anschließend auf **Apply**. Beachten Sie, dass dieses Netzwerk kein 6-GHz-Band umfasst und die verfügbaren Wi-Fi-Bänder je nach Modell variieren.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot2.png){class="glboxshadow"}

Nach der Aktivierung wird die Seite wie folgt angezeigt.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/4.9/iot3.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"}.
