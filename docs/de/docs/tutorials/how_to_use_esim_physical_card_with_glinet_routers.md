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

Es kann jeweils nur ein eSIM-Profil gleichzeitig aktiv sein. Ein grüner Punkt zeigt an, dass das ausgewählte eSIM-Profil aktuell aktiv ist.

## Leitfaden zur eSIM-Verwaltung

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-management-interface-guide.jpg){class="glboxshadow"}

**A. Aktueller eSIM-Status:**

Dieser Bereich zeigt die grundlegenden Informationen der eSIM sowie Details zum aktuell aktiven Profil an.

- **EID:** Die weltweit eindeutige Kennung der eUICC (eSIM-Chip), die zur Identifikation und Profilsteuerung verwendet wird.
- **ICCID:** Die Integrated Circuit Card Identifier des aktuell aktiven eSIM-Profils.
- **IMSI:** Die International Mobile Subscriber Identity des aktuell aktiven eSIM-Profils.
- **eSIM OS Version:** Die Betriebssystemversion der eUICC, die deren Kompatibilität und Fähigkeiten definiert.
- **eSIM Storage (remain/total):** Der verfügbare und gesamte Speicherplatz auf der eUICC zum Speichern von eSIM-Profilen.
- **eSIM Profile Number:** Die Anzahl der aktuell auf der eUICC gespeicherten eSIM-Profile.

**B. Seed-Profil:**

Dieser Bereich zeigt Details zum Seed-Profil an. Das Seed-Profil enthält 1 GB kostenlose Daten für die USA und Europa sowie 100 MB Global Data, gültig für 1 Jahr ab dem Aktivierungsdatum. Mit diesen Daten können Sie weltweit weitere Profile herunterladen. Außerdem können Sie die Nutzung des Seed-Profils überwachen, einschließlich verbleibender Daten, Gesamtdaten und Ablaufdatum.

**C. Normales Profil:**

Dieser Bereich zeigt Informationen zu normalen Profilen an. Wenn Sie ein eSIM-Profil in einem Onlinestore kaufen und den eSIM-QR-Code mit der Funktion **Add eSIM Profile (QR Code Install)** hochladen, erscheint das Profil hier, sobald der Upload abgeschlossen ist.

**D. Add eSIM Profile (QR Code Install):**

Dies ist die zentrale Funktion zum Hochladen und Installieren von eSIM-Profilen. Wenn Sie ein eSIM-Profil in einem Onlinestore kaufen, erhalten Sie einen QR-Code. Klicken Sie auf diese Schaltfläche, um den QR-Code hochzuladen. Anschließend wird das eSIM-Profil auf Ihren Router heruntergeladen und installiert.

**E. Export Log for Support:**

In diesem Bereich können Sie alle Protokolle anzeigen, die sich auf den Betrieb der eSIM beziehen. Wenn Probleme auftreten und Sie technischen Support benötigen, können Sie diese Protokolle exportieren und per E-Mail an support@gl-inet.com mit unserem Support-Team teilen.

**F. Top-up:**

Wenn die von GL.iNet bereitgestellten kostenlosen und vorinstallierten Daten aufgebraucht oder abgelaufen sind und Sie den Dienst weiter nutzen möchten, können Sie auf die Schaltfläche **Top-up** klicken, einen QR-Code scannen und zusätzliche Daten kaufen.

**G. Empfohlene eSIM-Profil-Stores:**

GL.iNet empfiehlt Ihnen der Einfachheit halber zwei Partner-eSIM-Stores: EIOTCLUB und Tuge. Sie können die QR-Codes scannen oder auf die Links klicken ([den EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} oder [den Tuge eSIM Store](https://esim_store.gl-inet.com/){target="_blank"}), um entsprechend Ihrem Bedarf einen Kauf zu tätigen. Sie können auch eSIM-Pakete von anderen Drittanbietern Ihrer Wahl kaufen.

**H. Aktionen:**

In diesem Bereich können Sie eSIM-Profile bequem verwalten, einschließlich Aktivieren, Wechseln und Löschen.

## eSIM-Seed-Profil aufladen

Für die Ersteinrichtung oder den Kauf eines eSIM-Profils stellt GL.iNet vorinstallierte Daten bereit: 100 MB für die weltweite Nutzung und 1 GB für Europa und die USA. Diese Tarife sind bewusst teurer ausgelegt und für Situationen gedacht, in denen Sie nach Ihrer Ankunft an einem Ort ohne Internetzugang ein neues eSIM-Profil herunterladen müssen.

Um Ihr eSIM-Seed-Profil aufzuladen, klicken Sie einfach auf die Schaltfläche **Top-up**, scannen den QR-Code und folgen den Anweisungen.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim_top-up.jpg){class="glboxshadow"}

## eSIM-Profil kaufen und installieren

Nachdem Sie Ihren Router eingerichtet haben, folgen Sie den untenstehenden Schritten, um Ihr eSIM-Profil zu kaufen und zu aktivieren.

**Schritt 1:** Kaufen Sie ein eSIM-Profil in einem eSIM-Store.

<u>Option 1</u>: Kaufen Sie ein eSIM-Profil in einem unserer empfohlenen Stores, [dem EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} oder [dem Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}. Direkte Links zu den Stores finden Sie im Bild unten.


*Alle in diesen beiden Stores gekauften eSIM-Profilpakete sind vollständig mit unseren Routern kompatibel. Wenn Sie Fragen haben, wenden Sie sich bitte an unser Support-Team unter support@gl-inet.com.*

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-1.jpg){class="glboxshadow"}

![eSIM recommend store](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-profile-recommend-store-2.jpg){class="glboxshadow"}

<u>Option 2</u>: Unter [diesem Link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} finden Sie eine Liste von Stores, die von GL.iNet getestet wurden. Bitte beachten Sie, dass wir nicht garantieren können, dass alle Pakete aus diesen Stores vollständig mit GL.iNet-Routern kompatibel sind.

*Da GL.iNet keine Partnerschaften mit diesen Stores hat, können wir keinen After-Sales-Support und keine Rückerstattungen für diese Pakete anbieten.*

<u>Option 3</u>: Kaufen Sie ein eSIM-Profil bei einem anderen Drittanbieter Ihrer Wahl.

**Schritt 2**: Installieren Sie Ihr eSIM-Profil

Nach dem Kauf des eSIM-Profils erhalten Sie einen QR-Code. Speichern Sie diesen QR-Code auf Ihrem Computer. Klicken Sie dann auf die Schaltfläche **Add eSIM Profile (QR Code Install)**, um Ihr gekauftes eSIM-Profil hochzuladen und zu installieren.

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-1.jpg){class="glboxshadow"}

![add eSIM profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/add-esim-profile-2.jpg){class="glboxshadow"}

**Hinweis:** Wie der grüne Pfeil im Bild oben zeigt, wird bei einem korrekt formatierten QR-Code ein Aktivierungscode angezeigt, der mit **LPA:** beginnt.

*Einige nicht standardisierte QR-Codes erzeugen jedoch möglicherweise nur einen reinen Aktivierungscode ohne das Präfix LPA.
Tritt dies auf, fügen Sie bitte manuell „LPA:“ am Anfang des Codes ein, bevor Sie auf die Schaltfläche Download & Install klicken.*

**Schritt 3:** Aktivieren Sie Ihr neues Profil

Nachdem der QR-Code erfolgreich hochgeladen wurde, sehen Sie Ihr neues eSIM-Profil unter **Normal Profile**. Klicken Sie auf **Enable**, um Ihr neues eSIM-Profil zu aktivieren.

![enable your new profile](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile.jpg){class="glboxshadow"}

**Schritt 4:** Wenden Sie Ihr neues eSIM-Profil an und verbinden Sie sich mit dem Internet

Nachdem Sie Ihr eSIM-Profil aktiviert haben, gehen Sie zu **INTERNET** und klicken auf **Connect**, um Ihr eSIM-Profil anzuwenden und die Internetverbindung herzustellen.

![connect to internet](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-connect.jpg){class="glboxshadow"}

*Hinweis: Einige eSIM-Profile erfordern möglicherweise zusätzliche Einstellungen wie APN, PIN oder TTL. Klicken Sie bei Bedarf auf **Manual Setup** oder **SIM Card Settings**, um diese Einstellungen zu konfigurieren. In manchen Fällen müssen Sie das Gerät neu starten, um eine Internetverbindung herzustellen.*

Sobald das eSIM-Profil erfolgreich eingerichtet wurde, sieht der Bildschirm wie folgt aus:

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/enable-your-new-profile-successfully.jpg){class="glboxshadow"}

**Schritt 5:** eSIM-Profile einfach wechseln oder löschen

Sie können problemlos zwischen eSIM-Profilen wechseln, indem Sie neben dem Profil, das Sie aktivieren möchten, auf **Enable** klicken. Um ein eSIM-Profil zu entfernen, klicken Sie einfach auf **Delete**.

![eSIM profile is successfully set up](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/switch-or-delete-esim-profile.jpg){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
