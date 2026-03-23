# Verbindung mit dem Internet über Mobilfunk (Firmware v4.7 und älter)

**Hinweis**: Diese Anleitung basiert auf Firmware v4.7 und älter. Für neuere Versionen lesen Sie bitte [hier](internet_cellular.md) weiter.

---

Die meisten GL.iNet-Router unterstützen Mobilfunkverbindungen. Diese Anleitung behandelt drei Modelltypen:

1. **Modelle mit integriertem 4G-Modem und Single-SIM**

    Einige Modelle verfügen über ein integriertes 4G-Modem mit einem einzelnen SIM-Kartensteckplatz, z. B. der GL-XE300 (Puli). Lesen Sie dazu bitte [Einrichtung für Single-SIM-Modelle](#einrichtung-für-single-sim-modelle).

2. **Modelle mit Unterstützung für USB-Modems**

    Einige Modelle besitzen einen USB-Port und unterstützen Mobilfunkverbindungen über ein USB-Modem, z. B. der GL-AXT1800 (Slate AX). Die Einrichtung ist ähnlich wie bei Modellen mit integriertem 4G-Modem und Single-SIM. Lesen Sie dazu bitte [Einrichtung für Single-SIM-Modelle](#einrichtung-für-single-sim-modelle).

3. **Modelle mit integriertem 5G-Modem und Dual-SIM**

    Einige Modelle verfügen über ein integriertes 5G-Modem mit zwei SIM-Kartensteckplätzen, z. B. der GL-X3000 (Spitz AX). Die Mobilfunkeinstellungen im webbasierten Admin Panel können sich leicht unterscheiden. Lesen Sie dazu bitte [Einrichtung für Dual-SIM-Modelle](#einrichtung-für-dual-sim-modelle).

**Hinweis:** Manche SIM-Karten müssen vor der ersten Verwendung aktiviert werden. Um die Kompatibilität sicherzustellen, aktivieren Sie die SIM-Karte in einem Smartphone, bevor Sie sie in den Router einsetzen.

## Einrichtung für Single-SIM-Modelle

Die folgenden Schritte gelten für Modelle mit integriertem Mobilfunkmodem und einem SIM-Kartensteckplatz (z. B. GL-XE300 Puli) oder mit USB-Port zum Anschluss eines externen USB-Modems (z. B. GL-AXT1800 Slate AX).

Hier verwenden wir den **GL-AXT1800 (Slate AX)** mit einem externen USB-Modem als Beispiel.

Wir empfehlen, den Router zunächst auszuschalten. Setzen Sie eine bereits aktivierte SIM-Karte in das USB-Modem ein und stecken Sie das Modem dann in den USB-Port des Routers. Schalten Sie den Router anschließend ein.

Wenn Sie das USB-Modem erst nach dem Start des Routers anschließen, wird das webbasierte Admin Panel möglicherweise nicht automatisch aktualisiert. Aktualisieren Sie in diesem Fall die Seite oder starten Sie den Router neu.

### Automatische Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und navigieren Sie zu **INTERNET** -> **Cellular**.

1. Beim ersten Zugriff verbindet sich der Router möglicherweise nicht automatisch, sollte aber oben links den Namen Ihres Mobilfunkanbieters sowie die IMEI anzeigen. Klicken Sie auf **Auto Setup**.

    Ignorieren Sie die Warnung *Incompatible Modem*.

    ![usb modem auto setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_auto_setup.png){class="glboxshadow"}

2. Der Verbindungsaufbau wird gestartet.

    **Hinweis:** Manche SIM-Karten haben besondere Nutzungseinschränkungen, etwa die Vorgabe eines bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, wenden Sie sich an Ihren Anbieter und prüfen Sie, ob besondere Einschränkungen vorliegen.

    ![usb modem connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connecting.png){class="glboxshadow"}

3. Sobald die Verbindung hergestellt ist, zeigt die Seite die Netzwerkdetails mit einem grünen Punkt an, was auf eine erfolgreiche Verbindung hinweist.

    ![usb modem connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/usb_modem_connected.png){class="glboxshadow"}

    **Hinweis:** Nach der Ersteinrichtung wird das USB-Modem automatisch erkannt, wenn Sie den Router mit eingestecktem USB-Modem neu starten oder das Modem erneut einstecken. Die Netzwerkverbindung wird dann hergestellt, ohne dass Sie erneut auf **Auto Setup** klicken müssen.

Wenn **Auto Setup** fehlschlägt, versuchen Sie bitte [Manuelle Einrichtung](#manuelle-einrichtung).

### Manuelle Einrichtung

Klicken Sie im Bereich Cellular auf **Manual Setup**, um die Mobilfunkeinstellungen der aktuellen SIM-Karte anzuzeigen oder zu ändern.

**Hinweis**: Manche SIM-Karten benötigen einen bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, wenden Sie sich bitte an Ihren Anbieter, um eventuelle Einschränkungen zu prüfen. Konfigurieren Sie bei Bedarf den korrekten APN auf Ihrem Router.

Durch das Anwenden der Änderungen wird die Verbindung neu aufgebaut.

![4g modem manual setup](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

- **Protocol**: Das Mobilfunk-Kommunikationsprotokoll (z. B. 3G, QMI oder QCM). Es wird in der Regel automatisch erkannt. Sie können es bei Bedarf an Ihr Modem und die Anforderungen Ihres Anbieters anpassen.

- **Port**: Der serielle Port für die Kommunikation mit dem Mobilfunkmodem. Dieser wird normalerweise automatisch erkannt und muss in der Regel nicht manuell angepasst werden.

- **APN**: APN (Access Point Name) ist ein Gateway-Parameter, der für eine Mobilfunkverbindung erforderlich ist. Er ermöglicht dem Router die Verbindung mit dem Internet Ihres Mobilfunkanbieters. Sie können den Standard-APN verwenden oder einen benutzerdefinierten APN Ihres Anbieters eintragen.

- **PIN**: Wenn Ihre SIM-Karte durch einen PIN-Code geschützt ist, geben Sie ihn hier ein. Wenn keine PIN gesetzt ist, ist dieses Feld optional.

- **TTL**: TTL (Time To Live) definiert, wie lange Pakete maximal im Netzwerk überleben können. Standardmäßig verringert der Router die TTL eingehender Pakete von Client-Geräten vor der Weiterleitung um 1. Falls Sie dies überschreiben müssen, können Sie hier einen festen Wert festlegen. Die TTL-Einstellung gilt nur für IPv4.

- **Service**: Wählen Sie den Mobilfunkdiensttyp aus, um festzulegen, welche Netzwerktechnologien das Modem verwenden soll.

- **Dial Number**: Geben Sie die von Ihrem Anbieter bereitgestellte Einwahlnummer ein. Diese ist oft bereits vorkonfiguriert und kann bei den meisten modernen Netzen leer bleiben.

- **Authentication**: Wählen Sie die von Ihrem Anbieter geforderte Authentifizierungsmethode (z. B. NONE, PAP, CHAP). In der Regel bleibt diese Einstellung auf NONE, wenn keine Zugangsdaten erforderlich sind.

### Kompatible Modems

Hier ist eine Liste unterstützter Modems, die wir bereits getestet haben.

| Modell                                 | 3G/4G | Getestet | Getestet von    | Hinweise* |
| -------------------------------------- | ----- | -------- | --------------- | --------- |
| Quectel EC20-E, EC20-A, EC20-C         | 4G    | Ja       | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G    | Ja       | GL.iNet         |           |
| Quectel EC200A series                  | 4G    | Ja       | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G    | Ja       | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G    | Ja       | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G    | Ja       | akw2312         |           |
| Quectel RM520N-GL                      | 5G    | Ja       | akw2312         |           |
| Quectel UC20-E                         | 3G    | Ja       | GL.iNet         |           |
| ZTE ME909s-821                         | 4G    | Ja       | GL.iNet         |           |
| Huawei E1550                           | 3G    | Ja       | GL.iNet         |           |
| Huawei E3276                           | 4G    | Ja       | GL.iNet         |           |
| TP-Link MA260                          | 3G    | Ja       | GL.iNet         |           |
| ZTE M823                               | 4G    | Ja       | Arnas Risqianto |           |
| ZTE MF190                              | 3G    | Ja       | Arnas Risqianto |           |
| Huawei E3372                           | 4G    | Ja       | anonymous       |           |
| Pantech UML290VW (Verizon)             | 4G    | Ja       | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G    | Ja       | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G    | Ja       | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G    | Ja       | anonymous       | Host-less |
| Huawei E3372h-320 (Ukraine)            | 4G    | Ja       | anonymous       | Host-less |

- **QMI**: Dieses Modem unterstützt den QMI-Modus. Wählen Sie bitte QMI als Protokoll und **/dev/cdc-wdm0** als seriellen Port für Ihren Mobilfunkrouter.

- **Host-less**: Dieses Modem unterstützt den Tethering-Modus. Verwalten Sie die Verbindung in diesem Fall über die Tethering-Oberfläche des Routers und nicht über die Cellular-Oberfläche.

## Einrichtung für Dual-SIM-Modelle

Die folgenden Schritte gelten für Modelle mit integriertem Mobilfunkmodem und Unterstützung für zwei SIM-Karten. Das webbasierte Admin Panel kann sich leicht von Single-SIM-Modellen unterscheiden.

Hier verwenden wir den **GL-X3000 (Spitz AX)** als Beispiel. Er unterstützt Dual SIM, Single Standby. Das bedeutet, dass zwei SIM-Karten für Mobilfunkzugang eingesetzt werden können, aber jeweils nur eine SIM-Karte aktiv sein kann. Sie können manuell zwischen den beiden SIM-Karten wechseln.

Wir empfehlen, den Router zunächst auszuschalten, die bereits aktivierte(n) SIM-Karte(n) einzusetzen und ihn dann wieder einzuschalten. Wenn Sie die SIM-Karte erst nach dem Start des Routers einsetzen, wird das webbasierte Admin Panel möglicherweise nicht automatisch aktualisiert. Aktualisieren Sie in diesem Fall die Seite oder starten Sie den Router neu.

### Automatische Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und navigieren Sie zu **INTERNET** -> **Cellular**.

1. Wenn keine SIM-Karte eingesetzt ist, wird die Seite wie folgt angezeigt.

    ![dual-sim, no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/no_sim.png){class="glboxshadow"}

2. Sobald eine SIM-Karte eingesetzt ist, beginnt der Router automatisch mit dem Verbindungsaufbau.

    Wenn die Verbindung erfolgreich ist, wird die Seite wie folgt angezeigt.

    ![dual-sim, 5g sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/5g_sim.png){class="glboxshadow"}

Wenn die Verbindung nicht automatisch aufgebaut wird, klicken Sie auf **Auto Setup** und warten Sie, bis der Router verbunden ist, oder versuchen Sie **Manual Setup**.

### Manuelle Einrichtung

Klicken Sie im Bereich Cellular auf **Manual Setup**, um die Cellular Settings zu öffnen.

![cellular settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/manual_setup/cellular_settings.png){class="glboxshadow gl-90-desktop"}

Sie können die Mobilfunkeinstellungen der aktuellen SIM-Karte anzeigen oder ändern. Außerdem werden einige vorkonfigurierte Profile gespeichert, und Sie können manuell Konfigurationen zu den **Saved Settings** hinzufügen.

### Einstellungen für SIM-Kartensteckplätze

Klicken Sie im Bereich Cellular auf **Current SIM Card**.

![dual-sim, current sim card](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/current_sim_card.png){class="glboxshadow"}

Sie gelangen dann zu den **SIM Card Slot Settings**.

![dual-sim, sim card slot settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/sim_card_slot_settings.png){class="glboxshadow"}

Wenn zwei SIM-Karten eingesetzt sind, können Sie **Auto Switch** aktivieren.

![dual-sim, auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/auto_switch.png){class="glboxshadow"}

- **Auto Switch**: Aktiviert das automatische Umschalten zwischen SIM 1 und SIM 2. Die Methode zur Netzwerkerkennung für das automatische SIM-Umschalten entspricht der Konfiguration auf der Multi-WAN-Seite.

- **Preferred SIM Card Slot**: Legen Sie fest, ob SIM 1 oder SIM 2 bevorzugt verwendet werden soll.

- **Failover Interval**: Verfügbare Werte reichen von 5 Minuten bis 24 Stunden.

    Wenn die Internetverbindung nach einem Failover weiterhin nicht verfügbar ist, wechselt das Gerät zurück zum bevorzugten SIM-Steckplatz und wartet dieses Intervall ab, bevor erneut ein Failover versucht wird.

    Diese Option greift, wenn sowohl die bevorzugte als auch die Backup-SIM kein Signal haben. Das Gerät wechselt dann zwischen den SIM-Karten, bis eine von ihnen ein gültiges Signal erhält.

    ![failover interval](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/sim_failover_interval.png){class="glboxshadow"}

- **Checking Preferred Slot Status Scheduled**

    Wenn diese Option aktiviert ist, prüft das Gerät täglich zur konfigurierten Uhrzeit den bevorzugten SIM-Steckplatz und versucht, wieder darauf zurückzuschalten, sobald die bevorzugte SIM erneut Internetzugang hat.

    Dadurch wird verhindert, dass die Backup-SIM übermäßig viel Datenvolumen verbraucht. Wenn die bevorzugte SIM weiterhin kein Signal hat, nutzt das Gerät weiterhin die Backup-SIM.

    ![checking preferred slot status scheduled](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/check_preferred_slot_status.png){class="glboxshadow"}

**Hinweis**: Die Funktion **Auto Switch** schaltet nicht sofort auf eine andere SIM-Karte um. Erstens benötigt das Gerät Zeit, um zu bestätigen, dass die aktuelle SIM keinen Internetzugang hat. Zweitens befindet sich die andere SIM nicht im Standby-Modus und benötigt Zeit zur Aktivierung.

## Verkehrsstatistiken

Klicken Sie im Bereich Cellular auf **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics_option.png){class="glboxshadow gl-90-desktop"}

Sie gelangen auf die Seite **Traffic Statistics**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/dual_sim/traffic_statistics.png){class="glboxshadow gl-90-desktop"}

## SMS

Bitte lesen Sie das [SMS-Tutorial](sms.md).

## SMS Forwarding

Bitte lesen Sie das Tutorial [SMS Forwarding](../tutorials/sms_forwarding.md).

## Modem Management

Klicken Sie im Bereich Cellular oben rechts auf die Schaltfläche **Tool**, um die Seite **Modem Management** zu öffnen.

![modem management button](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}

Sie enthält zwei Bereiche: **Modem Info** und **AT Command**.

![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management.png){class="glboxshadow"}

AT-Befehle sind Standardanweisungen zur Kommunikation mit dem Mobilfunkmodem.

Wenn Shortcut auf **Manual command** gesetzt ist, geben Sie den gewünschten Befehl im Feld **AT Command** ein, um den Modemstatus zu prüfen.

Sie können auch auf das Shortcut-Dropdown klicken und aus einer Liste mit **vordefinierten Befehlen** wählen.

![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Die folgenden Befehle sind als Voreinstellungen verfügbar:

* IMEI anfordern
* QCCID anfordern
* IMSI anfordern
* Signalqualität prüfen
* Modem zurücksetzen
* Betreibernamen
* SIM-Kartenstatus anfordern

Als Beispiel ist hier die Voreinstellung „Request IMEI“ ausgewählt. Klicken Sie auf „Send“, dann erhalten Sie das unten gezeigte Ergebnis.

![shortcut example](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

## Anbieterprofil

Sie können verschiedene Profile für denselben oder für unterschiedliche Netzbetreiber speichern.

Klicken Sie im Bereich Cellular oben rechts auf die Schaltfläche **Profile**, um Profile zu verwalten.

![manageprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/manage_profile.jpg){class="glboxshadow"}

Fügen Sie ein neues Profil hinzu oder speichern Sie das aktuelle Profil.

![addprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/add_profile.jpg){class="glboxshadow"}

Erstellen Sie Ihr eigenes Profil entsprechend den Anforderungen Ihres Netzbetreibers.

![createprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/create_profile.jpg){class="glboxshadow"}

Beim nächsten Mal können Sie ein gespeichertes Profil auswählen.

![selectprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/select_profile.jpg){class="glboxshadow"}

Wählen Sie die benötigten Profile aus.

![chooseprofile](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/carrier_profile/choose_profile.jpg){class="glboxshadow"}

## Lock Tower

Diese Funktion ist nur auf GL-X3000, GL-XE3000 und GL-X2000 verfügbar (Firmware v4.7 oder neuer).

Wenn Sie ein hochwertiges Signal empfangen und eine stabile Mobilfunkverbindung sicherstellen möchten, können Sie **Lock Tower** ausprobieren.

**Hinweis:** Der gesperrte Mobilfunkmast muss zu den von Ihrem Anbieter und Gerät unterstützten Frequenzbändern passen, andernfalls kann die Verbindung fehlschlagen.

Klicken Sie im Bereich Cellular oben rechts auf das Symbol **Tower**.

![signal_tower_lock](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_1.jpg){class="glboxshadow"}

Daraufhin werden die verfügbaren Masten angezeigt.

![signal_tower_lock1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_2.jpg){class="glboxshadow"}

Klicken Sie auf einen Mast, um die Details anzuzeigen und ihn zu sperren.

![signal_tower_lock2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_3.jpg){class="glboxshadow"}

Der Maststatus (z. B. Locked/Unlocked) wird oben angezeigt.

![signal_tower_lock3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/signal_tower_lock_4.jpg){class="glboxshadow"}

**Hinweis**:

1. Das Gerät kann möglicherweise nicht alle Masten scannen, wenn die Cellular-Oberfläche aktiviert ist.

2. Wenn der gesperrte Mast nicht zu den Parametern für Band Masking oder APN in Ihren Mobilfunkeinstellungen passt, kann sich der Router nicht mit dem Mobilfunknetz verbinden.

3. Wenn Sie nach dem Sperren eines Mobilfunkmasts den Router an einen anderen Standort versetzen, versucht er nach einem Neustart weiterhin, sich mit dem gesperrten Mast zu verbinden. Dadurch kann verhindert werden, dass sich der Router am neuen Standort automatisch mit dem Mobilfunknetz verbindet. In diesem Fall müssen Sie entweder den aktuellen Mobilfunkmast entsperren oder ihn manuell auf einen neuen Mast sperren.

## Signalverlauf

Klicken Sie im Bereich Cellular oben rechts auf das Symbol **Signal**, um die Verlaufshistorie der Signalstärke zu prüfen.

![historical_signal_record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_1.jpg){class="glboxshadow"}

Dies hilft Ihnen dabei, die Qualität Ihrer Mobilfunkverbindung zu beurteilen. Wenn das Signal schwach ist, versuchen Sie, auf einen anderen Mast zu wechseln, um ein besseres Signal zu erhalten.

Sie können den Verlauf der Mobilfunk-Signalstärke anzeigen, indem Sie unterschiedliche Zeiträume auswählen.

![historical_signal_record1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/historical_signal_record_2.jpg){class="glboxshadow"}

## Band Masking

Klicken Sie im Bereich Cellular auf **View More** und wählen Sie **Cells Info**, um die Zelldetails zu prüfen.

Dort sehen Sie die aktuell verwendeten Bänder und ihren Signalstatus.

![cellinfo](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/cell_info.jpg){class="glboxshadow"}

Wenn das Signal schwach ist, können Sie **Band Masking** aktivieren, um bestimmte Bänder zu blockieren. Alternativ können Sie bei gutem Signal festlegen, dass der Router nur bestimmte Mobilfunkbänder verwendet.

Klicken Sie auf **Manual Setup**, um die Seite **Cellular Settings** zu öffnen, und aktivieren Sie anschließend **Band Masking**.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/band_masking/band_masking.jpg){class="glboxshadow"}

Wählen Sie den **Masking Mode** (Block oder Open) und anschließend die LTE-Bänder, 5G-NSA-Bänder und 5G-SA-Bänder aus.

## Fehlerbehebung

Wenn Sie keine Mobilfunkverbindung herstellen können, klicken Sie auf die folgende Fehlermeldung, um passende Lösungen anzuzeigen.

??? note "No SIM / Your SIM card has not been detected"

    1. Aktualisieren Sie die Seite und warten Sie einige Minuten, um zu prüfen, ob die SIM-Karte erkannt wird.

    2. Stellen Sie sicher, dass die SIM-Karte korrekt eingesetzt ist. Richten Sie die Kerbe der SIM-Karte an der entsprechenden Markierung des Kartenschachts aus, um die korrekte Einsetzrichtung zu bestätigen.

    3. Schalten Sie den Router aus, entfernen Sie die SIM-Karte, setzen Sie sie erneut ein und schalten Sie den Router wieder ein.

    4. Versuchen Sie nach Möglichkeit eine andere SIM-Karte.

    Wenn das Problem weiterhin besteht, laden Sie die Protokolle herunter und senden Sie sie an [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    1. Aktualisieren Sie die Seite und warten Sie einige Minuten, um zu prüfen, ob der Fehler verschwindet.

    2. Klicken Sie auf **Disconnect**/**Abort** und anschließend auf **Connect**, um die Verbindung erneut aufzubauen.

    3. Starten Sie den Router neu.

    4. Prüfen Sie den Status der SIM-Karte und stellen Sie sicher, dass sie aktiviert ist. Testen Sie die SIM-Karte in einem Smartphone, um zu bestätigen, dass sie mit einem aktiven Datentarif normal auf das Internet zugreifen kann, oder wenden Sie sich zur Überprüfung an Ihren Netzbetreiber.

    5. Manche Netzbetreiber benötigen für die Netzverbindung möglicherweise das 3G-Protokoll. Gehen Sie zu **Manual Setup** -> **Cellular Settings** -> **Protocol**, wählen Sie **3G** und klicken Sie anschließend auf **Apply**.

        ![manual setup, sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/cellular_settings.png){class="glboxshadow"}

        Das Gerät verbindet sich automatisch erneut. Warten Sie einige Minuten und prüfen Sie dann, ob die Verbindung erfolgreich hergestellt wurde.

    6. Manche SIM-Karten haben besondere Nutzungseinschränkungen, z. B. die Vorgabe eines bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, kontaktieren Sie Ihren Anbieter und prüfen Sie, ob Einschränkungen vorliegen.

        Gehen Sie bei Bedarf zu **Manual Setup** -> **Cellular Settings** -> **APN**, konfigurieren Sie den korrekten APN auf dem Router und klicken Sie anschließend auf **Apply**.

    7. Klicken Sie auf **View More** und wählen Sie **Cells Info**, um die Mobilfunk-Signalstärke zu prüfen. Wenn das Signal schwach ist, stellen Sie sicher, dass die Antenne korrekt installiert ist. Platzieren Sie den Router an einem offenen und möglichst unverbauten Standort, um den Signalempfang zu verbessern.

    8. Prüfen Sie, ob **Band Masking** oder **Lock Tower** aktiviert ist. Falls ja, deaktivieren Sie die Funktion und versuchen Sie, die Verbindung erneut herzustellen.

    Wenn das Problem weiterhin besteht, laden Sie die Protokolle herunter und senden Sie sie an [support@gl-inet.com](mailto:support@gl-inet.com).

## IoT-Zertifizierung

### AT&T-Zertifizierung

Klicken Sie auf den Link [att device certification](https://iotdevices.att.com/certified-devices.aspx#) und geben Sie den Gerätenamen ein; dort können Sie das Gerät finden.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification.png){class="glboxshadow"}

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/at&t_certification_2.png){class="glboxshadow"}

### T-Mobile-Zertifizierung

Klicken Sie auf den Link [t-mobile device certification](https://www.t-mobile.com/business/solutions/iot/device-certification) und wählen Sie bei **Filter** die Option **5G** aus; dort können Sie das Gerät finden.

![bandmasking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/certification/t-mobile_certification.png){class="glboxshadow"}

---

Verwandte Artikel

- [Internet-Seite](internet.md)
- [Wie legt man die Priorität der einzelnen Internetzugangsmethoden fest?](multi-wan.md)
- [Wie richtet man Lastausgleich ein, wenn mehrere Internetzugangsmethoden gleichzeitig verwendet werden?](multi-wan.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
