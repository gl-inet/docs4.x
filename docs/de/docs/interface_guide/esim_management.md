# eSIM-Verwaltung

Gehen Sie im webbasierten Admin Panel links zu **APPLICATIONS** -> **eSIM Management**.

Auf dieser Seite können Sie den Status der eSIM Physical Card prüfen und eSIM-Profile verwalten. Sie besteht aus zwei Bereichen: **Current eSIM Status** und **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Unterstützte Modelle

| Router-Modell                  | Unterstützung |
| :----------------------------- | :-----------: |
| GL-X2000 (Spitz Plus)          | √             |
| GL-X3000 (Spitz AX)            | √             |
| GL-XE3000 (Puli AX)            | √             |
| GL-E750V2 (Mudi V2)            | √             |
| GL-E750 (Mudi)                 | √             |
| GL-XE300 (Puli)                | ※            |
| GL-X750 (Spitz)                | ※            |
| GL-X300B (Collie)              | ※            |
| GL-E750V2 vSIM                 | X             |
| GL-E5800 (Mudi 7)              | X             |

**Für Modelle mit ※:**

1. Die aktuelle stabile Firmware unterstützt eSIM nicht. Um die eSIM-Funktion zu nutzen, müssen Sie eine eSIM-fähige Firmware installieren. [Kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"} für weitere Anweisungen.

2. Bei mit ※ gekennzeichneten Modellen mit EP06-A-Modul wird eSIM nicht unterstützt, da die Qualcomm-Software die erforderlichen AT-Befehle nicht unterstützt.

3. Für GL-E750 (Mudi) und mit ※ gekennzeichnete Modelle mit EP06-E-Modul lesen Sie bitte diesen [Beitrag](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"}, um zuerst die Firmware des Moduls zu aktualisieren. Installieren Sie anschließend die eSIM-fähige Firmware, um die eSIM-Funktion zu aktivieren.

**Für Modelle mit X:**

1. GL-E750V2 vSIM unterstützt keine eSIM-Funktionalität.

2. GL-E5800 (Mudi 7) verfügt über eine integrierte eSIM. Daher wird die eSIM Physical Card auf dem Mudi 7 nur als normale SIM-Karte ohne eSIM-Funktion erkannt.

## Current eSIM Status

Dieser Bereich zeigt grundlegende Informationen und Details zum aktuell aktiven eSIM-Profil an.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Die weltweit eindeutige Kennung der eUICC (eSIM-Chip), die zur Identifizierung und Profilverwaltung verwendet wird.
- **ICCID:** Die Integrated Circuit Card Identifier des aktuell aktiven eSIM-Profils.
- **IMSI:** Die International Mobile Subscriber Identity des aktuell aktiven eSIM-Profils.
- **eSIM OS Version:** Die Betriebssystemversion der eUICC, die deren Kompatibilität und unterstützte Funktionen definiert.
- **eSIM Storage (remain/total):** Verfügbarer und gesamter Speicherplatz auf der eUICC zum Speichern von eSIM-Profilen.
- **eSIM Profile Number:** Die Anzahl der aktuell auf der eUICC gespeicherten eSIM-Profile. Bitte beachten Sie, dass eSIM-Profile verschiedener Anbieter unterschiedlich groß sein können. Daher variiert auch die Anzahl der Profile, die auf der eUICC gespeichert werden können.

## eSIM Profile List

Dieser Bereich zeigt Informationen zum Seed-Profil und zu normalen Profilen an.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: Das Seed-Profil ist mit 1 GB kostenlosen Daten für die USA und Europa sowie 100 MB Global Data vorinstalliert und ab Aktivierungsdatum 1 Jahr gültig. Mit diesen Daten können Sie weltweit weitere Profile herunterladen. Außerdem können Sie die Nutzung des Seed-Profils überwachen, einschließlich verbleibender Daten, Gesamtdatenvolumen und Ablaufdatum.

- **Normal Profile**: Wenn Sie ein eSIM-Profil kaufen und per QR-Code oder Aktivierungscode hochladen, wird das Profil hier angezeigt.

### Seed-Profil aufladen

GL.iNet stellt ein vorinstalliertes Seed-Profil mit 100 MB Global Data sowie 1 GB Daten für Europa und die USA für die Ersteinrichtung und Aktivierung von eSIM-Profilen bereit. Dieser Tarif ist dafür gedacht, neue eSIM-Profile herunterzuladen, wenn Sie an einem Ort ohne Internetzugang ankommen.

Wenn Sie die vorinstallierten kostenlosen Daten aufgebraucht haben oder diese abgelaufen sind und Sie den Dienst weiter nutzen möchten, können Sie Ihr Seed-Profil aufladen.

Klicken Sie im Bereich **Seed Profile** rechts auf die Schaltfläche **Top-up**.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Scannen Sie im Pop-up-Fenster den QR-Code und folgen Sie den Anweisungen, um das Aufladen abzuschließen.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### eSIM-Profil kaufen

Sie können eSIM-Profile in unseren empfohlenen Stores, in getesteten Stores oder bei anderen Drittanbieter-eSIM-Anbietern kaufen.

??? note "Option 1: Kauf in unseren empfohlenen Stores"

    Es gibt zwei empfohlene Stores: den [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} und den [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Klicken Sie im Bereich **Normal Profile** rechts auf **eSIM Profile Recommended Store**.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Scannen Sie den QR-Code oder klicken Sie auf die Links, um eSIM-Profile zu kaufen.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Hinweis**: Alle in diesen beiden Stores gekauften eSIM-Profilpakete sind vollständig mit GL.iNet-Routern kompatibel. Bei Fragen wenden Sie sich bitte an unser Support-Team unter [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Option 2: Kauf in getesteten Stores"

    Eine Liste der von GL.iNet getesteten Stores finden Sie unter [diesem Link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"}.

    **Hinweis**: Wir können nicht garantieren, dass alle Profile oder Pakete aus diesen Stores vollständig mit GL.iNet-Routern kompatibel sind. Da GL.iNet keine Partnerschaften mit ihnen hat, können wir keinen After-Sales-Support anbieten und keine Rückerstattungen unterstützen.

??? note "Option 3: Kauf bei anderen Drittanbieter-eSIM-Anbietern"

    Sie können eSIM-Profile auch bei anderen Drittanbietern Ihrer Wahl kaufen.

    Wir können jedoch keine vollständige Kompatibilität mit GL.iNet-Routern für eSIM-Profile garantieren, die bei anderen Drittanbietern gekauft wurden. Kaufen Sie daher nach eigenem Ermessen. GL.iNet übernimmt keine Verantwortung für Inkompatibilitätsprobleme.

    Für After-Sales-Support oder Rückerstattungen wenden Sie sich bitte an den jeweiligen eSIM-Anbieter.

### eSIM-Profil hochladen

Nach dem Kauf eines eSIM-Profils erhalten Sie in der Regel einen QR-Code oder einen Aktivierungscode. Speichern Sie diesen QR-Code lokal und folgen Sie dann den untenstehenden Schritten, um Ihr eSIM-Profil hochzuladen.

1. Klicken Sie im Bereich **Normal Profile** unten auf **Add eSIM Profile**.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Laden Sie Ihren eSIM-QR-Code hoch oder geben Sie den Aktivierungscode ein und klicken Sie dann auf **Install**. Das Profil wird anschließend heruntergeladen und auf Ihrem Router installiert.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Hinweis:**

    1. Die meisten eSIM-Profile können nur einmal heruntergeladen und installiert werden.

    2. Ein korrekt formatierter QR-Code zeigt einen Aktivierungscode an, der mit **LPA:** beginnt. Einige nicht standardisierte QR-Codes liefern jedoch möglicherweise nur einen rohen Aktivierungscode ohne LPA-Präfix. Fügen Sie in diesem Fall vor dem Klicken auf **Install** manuell `LPA:` am Anfang des Codes hinzu.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Wenn Sie noch kein eSIM-Profil gekauft haben, können Sie eines im **eSIM Profile Recommended Store** kaufen. Details finden Sie [hier](#esim-profil-kaufen).

3. Aktivieren Sie Ihr eSIM-Profil.

    Nach erfolgreichem Upload erscheint Ihr neues eSIM-Profil in der Liste **Normal Profile**. Klicken Sie auf **Enable**, um es zu aktivieren.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Verbinden Sie sich mit dem Internet.

    Gehen Sie nach dem Aktivieren Ihres eSIM-Profils zu **INTERNET** -> **Cellular**. Klicken Sie auf **Connect**, um über Ihr eSIM-Profil eine Internetverbindung herzustellen.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Hinweis**: Einige eSIM-Profile erfordern möglicherweise zusätzliche Konfigurationen, z. B. APN-, PIN- oder TTL-Einstellungen. Klicken Sie bei Bedarf auf **Manual Setup** oder **SIM Card Settings**, um diese Parameter anzupassen. In manchen Fällen müssen Sie das Gerät neu starten, um eine Internetverbindung herzustellen.*

5. Sobald der Router erfolgreich über das eSIM-Profil verbunden ist, wird die Seite wie folgt angezeigt:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Log für den Support exportieren

Klicken Sie auf **Export Log for Support**, um alle eSIM-bezogenen Protokolle anzuzeigen. Wenn Probleme auftreten und Sie technischen Support benötigen, exportieren Sie die eSIM-Logs und senden Sie sie per E-Mail an unser Support-Team unter [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Verwandte Artikel:

- [So verwenden Sie die eSIM Physical Card mit GL.iNet-Routern](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [So verwenden Sie die eSIM Physical Card mit Android-Geräten](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
