# Verbindung mit dem Internet über Mobilfunk (v4.10)

Der Inhalt dieser Seite basiert auf Firmwareversion v4.10 und höher. Wenn auf Ihrem Gerät eine andere Firmwareversion ausgeführt wird, verwenden Sie die folgende Auswahl, um zur entsprechenden Anleitung zu wechseln.

<div class="gl-link-select" data-label="Firmwareversion" data-placeholder="Firmware v4.10 und höher" markdown="1">

- [Firmware v4.8–v4.9](internet_cellular.md)
- [Firmware v4.7 und früher](internet_cellular_v4.7.md)

</div>

---

Die meisten GL.iNet-Router unterstützen Mobilfunkverbindungen. Diese Anleitung beschreibt Mobilfunkverbindungen für zwei Routertypen:

1. **Mobilfunkrouter**

    GL.iNet-Mobilfunkrouter verfügen über ein integriertes 4G-/5G-Modul und einen oder zwei SIM-Kartensteckplätze, beispielsweise Spitz AX (GL-X3000) und Mudi 7 (GL-E5800). Die Mobilfunkeinstellungen im Web-Admin-Panel können je nach Modell und Firmwareversion leicht variieren. Informationen zur Einrichtung dieser Modelle finden Sie unter [Mobilfunkrouter](#mobilfunkrouter).

2. **Router ohne Mobilfunkmodul**

    Hierzu gehören andere Routertypen wie Heim-, Reise- und Mini-Router sowie Sicherheits-Gateways. Sie verfügen üblicherweise über einen USB-Port, an den ein USB-Dongle (nicht im Lieferumfang enthalten) für Mobilfunkverbindungen angeschlossen werden kann. Informationen zur Einrichtung dieser Modelle finden Sie unter [Router ohne Mobilfunkmodul](#router-ohne-mobilfunkmodul).

**Hinweis:** Manche SIM-Karten müssen vor der ersten Verwendung aktiviert werden. Um die Kompatibilität sicherzustellen, aktivieren Sie die SIM-Karte in einem Smartphone, bevor Sie sie in den Router einsetzen.

## Mobilfunkrouter

In diesem Abschnitt wird **Mudi 7 (GL-E5800)** als Beispiel verwendet, um die Mobilfunkeinrichtung und die zugehörigen Funktionen zu erläutern.

Da Mudi 7 über eine integrierte eSIM und zwei Nano-SIM-Steckplätze verfügt und Dual SIM Dual Standby unterstützt, kann sich sein Web-Admin-Panel geringfügig von dem anderer Mobilfunkrouter unterscheiden, insbesondere von Modellen mit nur einem SIM-Steckplatz.

### Netzwerkeinrichtung

Melden Sie sich im Web-Admin-Panel des Routers an und navigieren Sie zu **INTERNET** -> **Cellular**.

1. Wenn keine SIM-Karte eingesetzt ist, wird auf der Seite „Your SIM card has not been detected“ angezeigt.

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/nosim.png){class="glboxshadow"}

2. Setzen Sie eine SIM-Karte ein. Der Router beginnt automatisch mit dem Verbindungsaufbau. Sobald die Verbindung hergestellt ist, werden der Mobilfunkanbieter, die Signalstärke, das Frequenzband, der Datenverbrauch und weitere Optionen angezeigt.

    ![sim active](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim1_active.png){class="glboxshadow"}

    Wenn Ihre SIM-Karte nicht erkannt wird, setzen Sie sie erneut in den Router ein oder starten Sie den Router neu.

3. Klicken Sie auf **Details & Configuration**, um die Netzwerkdetails anzuzeigen.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Unter **Network Information** werden SIM Operator, Phone Number, ICCID, APN, Max Bit Rate, IPv4 Address und IPv4 DNS Server angezeigt.

    ![network info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_info.png){class="glboxshadow"}

    !!! note "Was ist Max Bit Rate (AMBR)?"

        AMBR steht für Aggregate Maximum Bit Rate. Der Wert definiert die aggregierte Obergrenze der Bitrate für alle Non-GBR-Bearer Ihres Mobilfunkanbieters. Dieser Parameter wird vom Mobilfunknetzbetreiber bereitgestellt.

4. Klicken Sie auf **Details & Configuration**, um das Netzwerk manuell zu konfigurieren.

    ![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

    Unter **Network Settings** können Sie Netzwerkparameter wie den APN konfigurieren.

    ![network settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/network_settings_advanced.png){class="glboxshadow"}

    - **APN**: Die APN-Einstellungen werden in der Regel automatisch von der SIM-Karte abgerufen. Manche SIM-Karten erfordern einen bestimmten APN. Wenn Sie den richtigen APN nicht kennen, wenden Sie sich an Ihren Netzbetreiber.

    - **IP Type**: Der IP-Typ wird automatisch erkannt. Sie können IPv4, IPv6 oder beide Protokolle auswählen. Die Auswahl muss dem von Ihrer SIM-Karte unterstützten IP-Typ entsprechen. Unterstützt die SIM-Karte den ausgewählten Typ nicht oder ist hier IPv6 ausgewählt, während IPv6 auf dem Router deaktiviert ist, können Einwahlprobleme auftreten.

    - **International Data Roaming**: Diese Funktion ist standardmäßig aktiviert, um die Datennutzung bei internationalen Reisen zu ermöglichen. Sie können sie deaktivieren, wenn sie nicht benötigt wird oder wenn Sie hohe Roaming-Gebühren Ihres Anbieters vermeiden möchten.

    - **TTL**: Manche Netzbetreiber ermitteln anhand des TTL-Werts, ob die SIM-Karte in einem Router verwendet wird. Wenn Ihre SIM-Karte im Router nicht funktioniert, können Sie einen anderen TTL-Wert als 64 oder 128 festlegen, beispielsweise 65.

    - **HL**: Unter IPv6 begrenzt das Feld HL (Hop Limit) die Anzahl der Übertragungssprünge von Datenpaketen im Netzwerk und entspricht TTL unter IPv4.

    - **MTU**: Legen Sie den MTU-Wert entsprechend Ihrem Anwendungsszenario fest. Falsche Einstellungen können die Internetverbindung unterbrechen. Starten Sie das Gerät nach einer Änderung der MTU neu, damit die Einstellung wirksam wird.

    - **Authentication**: Wenn keine Anmeldedaten erforderlich sind, ist normalerweise NONE ausgewählt. Sie können PAP, CHAP oder PAP/CHAP festlegen.

### Datenverkehrsstatistiken

Klicken Sie auf **Data Usage**, um die Datenverkehrsstatistiken anzuzeigen.

![traffic_statistics1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics1.png){class="glboxshadow"}

Wenn Sie ein Datenlimit für Ihre SIM-Karte oder einen Zeitplan zum regelmäßigen Zurücksetzen des Datenverbrauchs festlegen möchten, aktivieren Sie **SIM Limit Settings**.

![traffic_statistics2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics2.jpg){class="glboxshadow"}

Legen Sie Data Cap Amount, Data Reset Period, Start Day und Start Hour fest und klicken Sie anschließend auf **Apply**.

![traffic_statistics3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/traffic_statistics3.png){class="glboxshadow"}

**Hinweis**:

1. Wenn Data Used den Wert von Data Cap Amount überschreitet, ändern Sie Data Cap Amount oder Data Used. Andernfalls kann die Netzwerkverbindung getrennt werden oder der Router zu einer anderen SIM-Karte wechseln, sofern [SIM Failover](#sim-failover) aktiviert ist.

2. Wenn für SIM 1 ein Data Cap Amount festgelegt und SIM Auto Switch aktiviert ist, wechselt der Router automatisch von SIM 1 zu SIM 2, sobald SIM 1 das Datenlimit überschreitet. SIM 1 wird dann deaktiviert.

3. Start Day: Die maximal auswählbare Anzahl von Tagen entspricht der tatsächlichen Anzahl der Tage im aktuellen Monat.

### Mobilfunkdetails

Klicken Sie auf **Details & Configuration**, um die Mobilfunkdetails anzuzeigen.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Unter **Cellular Information** werden Network Type, TAC, Cell ID, Band und Signal History angezeigt.

![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/cellular_info.png){class="glboxshadow"}

- **Network Type**: Der Netzwerktyp wird automatisch erkannt. Um ihn festzulegen, wechseln Sie zur Registerkarte **Cellular Settings** und wählen Sie den Netzwerktyp in der Dropdown-Liste aus.

    ![specify network type](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/specify_network_type.png){class="glboxshadow"}

    Wählen Sie 5G für eine höhere Geschwindigkeit (5G-Signal erforderlich) oder 4G für eine stabilere Verbindung.

    Wenn Sie einen Mobilfunkmast sperren, wird der Netzwerktyp festgelegt und kann nicht geändert werden.

- **TAC**: Abkürzung für Tracking Area Code. Diese vom Netzwerk zugewiesene Kennung bezeichnet einen Tracking-Bereich für die Mobilitätsverwaltung im Mobilfunknetz. Sie wird automatisch von der Mobilfunkbasisstation erkannt.

- **Cell ID**: Eindeutige Kennung einer einzelnen Zelle einer Mobilfunkbasisstation. Sie wird ebenfalls automatisch von der Basisstation erkannt.

- **Band Information**: Klicken Sie darauf, um weitere Parameter zum verwendeten Mobilfunkband anzuzeigen.

    ![band info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_info.png){class="glboxshadow"}

- **Signal History**: Klicken Sie darauf, um den Verlauf der Signalstärke anzuzeigen. Damit können Sie die Qualität Ihrer Mobilfunkverbindung überwachen.

    ![signal history](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/signal_history.png){class="glboxshadow"}

### Band Masking

Mit Band Masking können Sie bestimmte Mobilfunkbänder verwenden, um das Mobilfunksignal zu verbessern.

Klicken Sie auf **Details & Configuration**, um Band Masking zu aktivieren.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Aktivieren Sie unter **Cellular Settings** die Option **Band Masking**, wählen Sie die gewünschten Bänder aus und klicken Sie anschließend auf **Apply**.

![band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/band_masking.png){class="glboxshadow"}

### Lock Operator

!!! note "Unterstützte Modelle"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Der GL-X2000 (Spitz Plus) unterstützt diese Funktion ab Firmware v4.8.

Wenn Sie einen bestimmten Mobilfunkanbieter sperren, verwendet der Router ausschließlich dessen Netzwerk. Dies sorgt für eine stabile Verbindung und verhindert unbeabsichtigte Roaming-Gebühren, insbesondere in Grenzgebieten, in denen sich das Gerät sonst mit ausländischen Netzen verbinden könnte.

Klicken Sie auf **Details & Configuration**, um einen Anbieter zu sperren.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Klicken Sie unter **Cellular Settings** auf **Lock Operator**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator1.png){class="glboxshadow"}

Vor dem Scannen der Netze können Sie den **Lock Mode** auswählen.

![lock mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_mode.png){class="glboxshadow"}

- **Manual**: Sperrt manuell auf einen bestimmten Anbieter.

- **Manual-Auto**: Wechselt automatisch zu einem verfügbaren Anbieternetz, wenn die manuelle Sperre fehlschlägt.

Klicken Sie anschließend auf **Scan Networks**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator2.png){class="glboxshadow"}

Warten Sie etwa eine Minute. Die verfügbaren Anbieter werden angezeigt. Wählen Sie einen Anbieter aus und klicken Sie auf **Lock**.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator3.png){class="glboxshadow"}

Das Mobilfunksignal wird daraufhin auf den ausgewählten Anbieter festgelegt.

![lock operator](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_operator4.jpg){class="glboxshadow"}

### Lock Tower

!!! note "Unterstützte Modelle"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Der GL-X2000 (Spitz Plus) unterstützt diese Funktion ab Firmware v4.7.

Um ein hochwertiges Signal und eine stabile Mobilfunkverbindung zu erhalten, können Sie einen Mobilfunkmast sperren. Der gesperrte Mast muss jedoch zu den Frequenzbändern passen, die Ihr Anbieter und Ihr Gerät unterstützen. Andernfalls kann die Verbindung fehlschlagen.

Klicken Sie auf **Details & Configuration**, um einen Mobilfunkmast zu sperren.

![details](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/details.png){class="glboxshadow"}

Klicken Sie unter **Cellular Settings** auf **Lock Tower**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower1.png){class="glboxshadow"}

Klicken Sie im eingeblendeten Fenster auf **Scan Networks**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower2.png){class="glboxshadow"}

Warten Sie etwa eine Minute. Die verfügbaren Mobilfunkmasten werden angezeigt.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower3.png){class="glboxshadow"}

Wählen Sie einen Mast aus, um Details anzuzeigen, und klicken Sie anschließend auf **Lock**.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower4.png){class="glboxshadow"}

Das Mobilfunksignal wird daraufhin auf den ausgewählten Mast festgelegt.

![lock tower](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/lock_tower5.png){class="glboxshadow"}

**Hinweis**:

1. Das Gerät kann möglicherweise nicht alle Masten scannen, wenn die Cellular-Schnittstelle aktiviert ist.

2. Wenn der gesperrte Mast nicht zu Band Masking (sofern aktiviert) oder zu den APN-Parametern Ihrer Mobilfunkeinstellungen passt, kann der Router keine Verbindung zum Mobilfunknetz herstellen.

3. Wenn Sie den Router nach dem Sperren eines Mobilfunkmasts an einen anderen Standort versetzen, versucht er nach einem Neustart weiterhin, sich mit dem gesperrten Mast zu verbinden. Dadurch kann verhindert werden, dass er am neuen Standort automatisch eine Mobilfunkverbindung herstellt. Entsperren Sie in diesem Fall den aktuellen Mast oder sperren Sie den Router manuell auf einen neuen Mast.

### SMS

Lesen Sie [SMS](../tutorials/sms.md).

### SMS Forwarding

Lesen Sie [SMS Forwarding](../tutorials/sms_forwarding.md).

### Airplane Mode

Um Airplane Mode zu aktivieren, klicken Sie oben rechts auf das Zahnradsymbol und aktivieren Sie **Airplane Mode**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

### Modem Information

Um die Modemdetails anzuzeigen, klicken Sie oben rechts auf das Zahnradsymbol und wählen Sie **Modem Information**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![modem info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/modem_info.png){class="glboxshadow"}

### SIM Failover

Diese Funktion ist nur auf Mobilfunkroutern verfügbar, die Dual-SIM unterstützen.

SIM Failover ermöglicht das automatische Umschalten zwischen SIM 1 und SIM 2. Wenn der Datenverbrauch der SIM-Karte mit der höchsten Priorität den Data Cap Amount überschreitet oder die SIM-Karte keine Internetverbindung herstellen kann, wechselt der Router zur Backup-SIM, um einen unterbrechungsfreien Netzwerkzugang zu gewährleisten.

Um SIM Failover zu aktivieren, klicken Sie oben rechts auf das Zahnradsymbol und wählen Sie **SIM Failover**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

Aktivieren Sie im eingeblendeten Fenster **Auto Switch**. Ziehen Sie die Schaltfläche auf der rechten Seite, um die SIM-Priorität anzupassen.

![sim auto switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_auto_switch.png){class="glboxshadow"}

Wenn der Router zu einer bestimmten Tageszeit zur bevorzugten SIM-Karte zurückwechseln soll, aktivieren Sie **Scheduled Switch to Preferred SIM**, legen Sie die **Daily Execution Time** fest und klicken Sie anschließend auf **Apply**.

![sim failover](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/sim_failover.png){class="glboxshadow"}

### AT Command

AT-Befehle sind Standardanweisungen zur Kommunikation mit dem Mobilfunkmodem. Mit dieser Funktion können Sie Befehle senden und den Modemstatus prüfen.

Klicken Sie oben rechts auf das Zahnradsymbol und wählen Sie **AT Command**.

![settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/settings.png){class="glboxshadow"}

![atcommand](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/atcommand.png){class="glboxshadow"}

- **Shortcut**: Wenn Shortcut auf **Manual command** gesetzt ist, geben Sie den gewünschten Befehl in das Feld **AT Command** ein und klicken Sie unten auf **Send**. Das System zeigt das Ergebnis im darunterliegenden Ausgabefeld an.

    Sie können auch auf das Feld klicken und einen **preset command** aus der Dropdown-Liste auswählen.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut1.png){class="glboxshadow"}

    Wenn Sie beispielsweise den Shortcut „Request SIM card status“ und den SIM-Steckplatz SIM1 auswählen, klicken Sie auf „Send“. Das Ergebnis wird wie unten dargestellt angezeigt.

    ![shortcut](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/command_shortcut2.png){class="glboxshadow"}

- **SIM Slot**: Wählen Sie, ob der Befehl für SIM1 oder SIM2 gilt.

- **AT Command**: Geben Sie den gewünschten Befehl in dieses Feld ein, wenn Shortcut auf „Manual command“ gesetzt ist.

## Router ohne Mobilfunkmodul

In diesem Abschnitt werden **Flint 3 (GL-BE9300)** und der externe USB-Dongle [SIMPoYo uFi](https://www.gl-inet.com/products/simpoyo-ufi){target="_blank"} als Beispiel für die Mobilfunkeinrichtung verwendet.

**Hinweis**:

1. Einige USB-Mobilfunk-Dongles, darunter SIMPoYo uFi, arbeiten im **Host-less-Modus**. In diesem Modus stellt der Dongle die Mobilfunkverbindung intern her und stellt dem Router eine virtuelle USB-Ethernet-Schnittstelle bereit. Der Router behandelt ihn als angebundenes WAN und nicht als steuerbares Mobilfunkmodem. Die Verbindung wird daher über die Tethering-Schnittstelle statt über die Cellular-Schnittstelle hergestellt.

2. Im Host-less-Tethering-Modus kann der Router nicht auf Mobilfunkdaten der unteren Ebene wie Signalstärke, Cell ID und TAC zugreifen und weder APN- noch SIM-bezogene Parameter steuern. Konfigurieren Sie diese Einstellungen über die integrierte Weboberfläche des Dongles.

---

Führen Sie die folgenden Schritte aus, um eine Mobilfunkverbindung einzurichten.

1. Stecken Sie den USB-Dongle in den USB-Port des Routers.

2. Melden Sie sich im Web-Admin-Panel des Routers an, navigieren Sie zu **INTERNET** -> **Tethering** und klicken Sie auf **Connect**.

    ![tethering 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering1.png){class="glboxshadow"}

    Wenn Sie erweiterte Einstellungen wie TTL, HL und MTU festlegen möchten, klicken Sie auf **Advanced**, passen Sie die Einstellungen an und klicken Sie anschließend auf **Connect**.

    ![tethering 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering2.png){class="glboxshadow"}

3. Sobald die Verbindung hergestellt ist, werden Netzwerkdetails und ein grüner Punkt angezeigt. Dieser weist auf eine erfolgreiche Verbindung hin.

    ![tethering 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.10/tethering3.png){class="glboxshadow"}

Nach der Ersteinrichtung wird der USB-Dongle automatisch erkannt, wenn Sie den Router mit eingestecktem Dongle neu starten oder den Dongle erneut einstecken. Die Netzwerkverbindung wird hergestellt, ohne dass Sie erneut auf **Connect** klicken müssen.
