# So verwenden Sie die eSIM Physical Card mit GL.iNet-Routern

Diese Anleitung zeigt Ihnen, wie Sie die im GL.iNet-Onlineshop gekaufte eSIM Physical Card mit GL.iNet-Routern verwenden.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/set_up_the_simpoyo_esim_physical_card_with_android_devices/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Funktionen

Die wichtigsten Merkmale der eSIM Physical Card sind:

- Unterstützung von 4G- und 5G-Netzen für zuverlässige und schnelle Verbindungen.
- Einfache Verwaltung Ihrer eSIM-Profile durch Hinzufügen, Entfernen oder Aktivieren.
- Jederzeit Auswahl und Kauf passender Datenpakete in den meisten eSIM-Stores weltweit.
- Funktioniert mit eSIM-Profilen aus den meisten globalen eSIM-Stores.
- Kauf von eSIM-Profilen online ohne Angabe persönlicher Daten, wodurch das Risiko von Datenschutzverletzungen sinkt.
- Enthält ein Seed-Profil mit 1 GB kostenlosen Daten für die USA und Europa sowie 100 MB Global Data, gültig für 1 Jahr ab dem Aktivierungsdatum.
- Kompatibel mit ausgewählten GL.iNet-Geräten.

## Unterstützte Modelle

| Router-Modell                  | Unterstützung |
| :----------------------------- | :-----------: |
| GL-X2000 (Spitz Plus)          | √             |
| GL-X3000 (Spitz AX)            | √             |
| GL-XE3000 (Puli AX)            | √             |
| GL-E750V2 (Mudi V2)            | √             |
| GL-E750 (Mudi)                 | ※            |
| GL-XE300 (Puli)                | ※            |
| GL-X750 (Spitz)                | ※            |
| GL-X300B (Collie)              | ※            |
| GL-E750V2 vSIM                 | X             |
| GL-E5800 (Mudi 7)              | X             |

**Für Modelle mit ※:**

1. Die aktuelle stabile Firmware unterstützt eSIM nicht. Um die eSIM-Funktion zu verwenden, müssen Sie eine eSIM-fähige Firmware installieren. [Kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"} für weitere Anweisungen.
    
2. Wenn Sie ein mit ※ gekennzeichnetes Modell mit EP06-A-Modul verwenden, wird eSIM nicht unterstützt, da der Qualcomm-Software die Unterstützung für bestimmte AT-Befehle fehlt.
    
3. Wenn Sie ein mit ※ gekennzeichnetes Modell mit EP06-E-Modul verwenden, lesen Sie bitte [diese Anleitung](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, um die Firmware des Moduls zu aktualisieren und anschließend die eSIM-fähige Firmware zu installieren, damit eSIM genutzt werden kann.

**Für Modelle mit X:**

1. GL-E750V2 vSIM unterstützt keine eSIM-Funktionalität.

2. GL-E5800 (Mudi 7) verfügt über eine integrierte eSIM. Deshalb wird die eSIM Physical Card auf dem Mudi 7 nur als normale SIM-Karte ohne eSIM-Funktion erkannt.

## eSIM Physical Card einrichten

Wenn Sie die eSIM Physical Card zum ersten Mal verwenden, sehen Sie sich bitte dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten, um sie auf Ihrem GL.iNet-Router einzurichten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Schritt 1:** Setzen Sie die eSIM Physical Card in Ihren Router ein. Detaillierte Hinweise finden Sie in den Bildern unten.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Schritt 2:** Öffnen Sie einen Browser und geben Sie „192.168.8.1“ in die Adressleiste ein, um sich beim GL.iNet Admin Panel anzumelden.

![log in to the GL.iNet Admin Panel](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Schritt 3:** Verbinden Sie Ihr Gerät mit dem Internet.

Gehen Sie zu **INTERNET** und klicken Sie auf **Connect** (oder bei älteren Firmware-Versionen auf **Auto Setup**), um über Cellular eine Internetverbindung herzustellen.

*Diese eSIM Physical Card enthält ein Seed-Profil mit 1 GB kostenlosen Daten für die USA und Europa sowie 100 MB Global Data, gültig für 1 Jahr ab dem Aktivierungsdatum. Bitte beachten Sie, dass diese Daten nur für den Kauf und das Herunterladen von eSIM-Profilen vorgesehen sind und nicht für den allgemeinen Internetzugang.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Wenn die Internetverbindung erfolgreich hergestellt wurde, sieht der Bildschirm wie folgt aus.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Ihr eSIM-Profil verwalten

**Schritt 1:** Stellen Sie sicher, dass auf Ihrem GL.iNet-Gerät die neueste Firmware installiert ist.

Achten Sie darauf, dass die Version 4.0 oder höher ist und die Firmware Type number 0319 oder höher lautet.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Wenn Ihre Firmware **nicht aktuell** ist, können Sie sie entweder automatisch online oder manuell aktualisieren.

<u>Option 1</u>: Online-Firmware-Upgrade

1. Stellen Sie sicher, dass Ihr Gerät mit dem Internet verbunden ist.
    
2. Gehen Sie im Web-Admin-Panel zu **SYSTEM** > **Upgrade** > **Online Upgrade** und klicken Sie auf die Schaltfläche **Install**, um automatisch auf die neueste Firmware zu aktualisieren.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Option 2</u>: Manuelles Firmware-Update

1. Laden Sie [hier](https://dl.gl-inet.com/){target="_blank"} die Firmware für das entsprechende Modell herunter, das eSIM-Funktionalität unterstützt.
    
2. Gehen Sie im Web-Admin-Panel zu **SYSTEM** > **Upgrade** > **Local Upgrade**. Wählen Sie die Firmware-Datei aus oder ziehen Sie sie in den vorgesehenen Bereich, um auf die neueste Version zu aktualisieren.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Einige Modelle wie Mudi (GL-E750), Puli (GL-XE300) und Spitz (GL-X750) unterstützen eSIM nicht, wenn sie mit Quectel-EP06-A-Modulen ausgestattet sind, da die Qualcomm-Software bestimmte AT-Befehle nicht unterstützt.
    
    2. Falls ein EP06-E-Modul installiert ist, lesen Sie bitte [diese Anleitung](https://forum.gl-inet.com/t/48907){target="_blank"}, um das Modul auf die neueste Software für eSIM-Funktionalität zu aktualisieren.

**Schritt 2:** Öffnen Sie die eSIM-Verwaltung.

Warten Sie nach dem Firmware-Update, bis Ihr Gerät neu gestartet wurde, und melden Sie sich dann erneut beim GL.iNet Admin Panel an.

Gehen Sie zu **APPLICATIONS** > **eSIM Management**. Dort können Sie den aktuellen Status Ihrer eSIM einsehen.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Hier können Sie Ihren eSIM-Status einsehen und eSIM-Profile verwalten.

Es kann jeweils nur ein eSIM-Profil gleichzeitig aktiv sein. Ein grüner Punkt zeigt an, dass das ausgewählte eSIM-Profil aktuell aktiv ist.

---

Verwandter Artikel:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
