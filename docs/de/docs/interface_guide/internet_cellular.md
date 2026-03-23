# Verbindung mit dem Internet über Mobilfunk

**Hinweis**: Diese Anleitung basiert auf Firmware v4.8. Für frühere Versionen lesen Sie bitte [hier](internet_cellular_v4.7.md) weiter.

---

Die meisten GL.iNet-Router unterstützen Mobilfunkverbindungen. Diese Anleitung behandelt drei Modelltypen:

1. **Modelle mit integriertem 4G-Modem und Single-SIM**

    Einige Modelle verfügen über ein integriertes 4G-Modul mit einem einzelnen SIM-Kartensteckplatz, z. B. der GL-E750 (Mudi). Lesen Sie dazu bitte [Einrichtung für Single-SIM-Modelle](#einrichtung-für-single-sim-modelle).

2. **Modelle mit integriertem 5G-Modem und Dual-SIM**

    Einige Modelle verfügen über ein integriertes 5G-Modul mit zwei SIM-Kartensteckplätzen, z. B. der GL-X3000 (Spitz AX). Die Mobilfunkeinstellungen im webbasierten Admin Panel können sich leicht unterscheiden. Lesen Sie dazu bitte [Einrichtung für Dual-SIM-Modelle](#einrichtung-für-dual-sim-modelle).

3. **Modelle mit Unterstützung für USB-Modems**

    Einige Modelle besitzen keinen integrierten SIM-Kartensteckplatz, verfügen aber über einen USB-Port und unterstützen Mobilfunkverbindungen über ein USB-Modem, z. B. der GL-MT3000 (Beryl AX). Lesen Sie dazu bitte [Einrichtung für USB-Modem](#einrichtung-für-usb-modem).

**Hinweis:** Manche SIM-Karten müssen vor der ersten Verwendung aktiviert werden. Um die Kompatibilität sicherzustellen, aktivieren Sie die SIM-Karte in einem Smartphone, bevor Sie sie in den Router einsetzen.

## Einrichtung für Single-SIM-Modelle

Die folgenden Schritte gelten für Modelle mit integriertem Mobilfunkmodem und einem einzelnen SIM-Kartensteckplatz.

Hier verwenden wir den **GL-E750 (Mudi)** als Beispiel.

Wir empfehlen, den Router zunächst auszuschalten, eine bereits aktivierte SIM-Karte in den Steckplatz einzusetzen und ihn dann einzuschalten. Wenn Sie die SIM-Karte erst nach dem Start des Routers einsetzen, wird das webbasierte Admin Panel möglicherweise nicht automatisch aktualisiert. Aktualisieren Sie in diesem Fall die Seite oder starten Sie den Router neu.

### Automatische Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und navigieren Sie zu **INTERNET** -> **Cellular**.

1. Wenn keine SIM-Karte eingesetzt ist, zeigt die Seite die Meldung „Your SIM card has not been detected“ an.

    ![single no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_no_sim.png){class="glboxshadow"}

2. Setzen Sie eine SIM-Karte ein. Das Gerät beginnt dann wie unten dargestellt mit dem Verbindungsaufbau.

    ![single sim connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connecting.png){class="glboxshadow"}

    Wenn die Verbindung nicht automatisch aufgebaut wird, klicken Sie – falls verfügbar – auf die Schaltfläche **Connect**.

    Wenn die SIM-Karte nicht erkannt wird, versuchen Sie, den Router neu zu starten, um zu prüfen, ob sie dann erkannt wird.

3. Sobald die Mobilfunkverbindung hergestellt ist, zeigt die Seite die Netzwerkdetails mit einem grünen Punkt an, was auf eine erfolgreiche Verbindung hinweist.

    ![single sim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_connected.png){class="glboxshadow"}

Wenn **Auto Setup** fehlschlägt, versuchen Sie bitte die [manuelle Einrichtung](#manual-setup-single-sim).

### Manuelle Einrichtung {#manual-setup-single-sim}

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** und klicken Sie dann auf **SIM Card Settings**.

![sim card settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_1.png){class="glboxshadow"}

Sie können die Mobilfunkeinstellungen der aktuellen SIM-Karte anzeigen oder ändern.

**Hinweis**: Manche SIM-Karten benötigen einen bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, wenden Sie sich bitte an Ihren Anbieter, um eventuelle Einschränkungen zu prüfen. Konfigurieren Sie bei Bedarf den korrekten APN auf Ihrem Router.

Durch das Anwenden der Änderungen wird die Verbindung neu aufgebaut.

![single sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) ist ein Gateway-Parameter, der für eine Mobilfunkverbindung erforderlich ist. Er ermöglicht dem Router die Verbindung mit dem Internet Ihres Mobilfunkanbieters. Sie können den Standard-APN verwenden oder einen benutzerdefinierten APN Ihres Anbieters eintragen.

- **Protocol**: Das Mobilfunk-Kommunikationsprotokoll (z. B. 3G, QMI oder QCM). Es wird üblicherweise automatisch erkannt und kann bei Bedarf an Ihr Modem und die Anforderungen Ihres Anbieters angepasst werden.

- **Port**: Der serielle Port zur Kommunikation mit dem Mobilfunkmodem. Er wird in der Regel automatisch erkannt und muss normalerweise nicht manuell angepasst werden.

- **TTL**: TTL (Time To Live) definiert, wie lange Pakete maximal im Netzwerk überleben können. Standardmäßig verringert der Router die TTL eingehender Pakete von Client-Geräten vor der Weiterleitung um 1. Falls Sie dies überschreiben müssen, können Sie hier einen festen Wert festlegen. Die TTL-Einstellung gilt nur für IPv4.

- **HL**: Unter IPv6 begrenzt HL (Hop Limit) die Anzahl der Übertragungssprünge von Datenpaketen im Netzwerk und entspricht TTL bei IPv4.

- **MTU**: Der Standardwert für MTU beträgt 1500 Byte.

- **Authentication**: Wählen Sie die von Ihrem Anbieter geforderte Authentifizierungsmethode (z. B. NONE, PAP, CHAP). In der Regel bleibt diese Einstellung auf NONE, wenn keine Zugangsdaten erforderlich sind.

- **Band Masking**: Sie können Band Masking aktivieren, wenn der Router bestimmte Bänder blockieren oder nur bestimmte Mobilfunkbänder verwenden soll. Details finden Sie [hier](#band-masking).

## Einrichtung für Dual-SIM-Modelle

Die folgenden Schritte gelten für Modelle mit integriertem Mobilfunkmodem und Unterstützung für zwei SIM-Karten. Die Seiten können sich leicht von Single-SIM-Modellen unterscheiden.

Hier verwenden wir den **GL-X3000 (Spitz AX)** als Beispiel. Er unterstützt Dual SIM, Single Standby. Das bedeutet, dass zwei SIM-Karten für den Mobilfunkzugang eingesetzt werden können, aber jeweils nur eine SIM-Karte aktiv sein kann. Sie können manuell zwischen den beiden SIM-Karten wechseln.

Wir empfehlen, den Router zunächst auszuschalten, die bereits aktivierte(n) SIM-Karte(n) in die Steckplätze einzusetzen und ihn dann einzuschalten. Wenn Sie die SIM-Karte erst nach dem Start des Routers einsetzen, wird das webbasierte Admin Panel möglicherweise nicht automatisch aktualisiert. Aktualisieren Sie in diesem Fall die Seite oder starten Sie den Router neu.

### Automatische Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und navigieren Sie zu **INTERNET** -> **Cellular**.

1. Wenn keine SIM-Karte eingesetzt ist, zeigt die Seite die Meldung „Your SIM card has not been detected“ an.

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/no_sim.png){class="glboxshadow"}

2. Wenn eine SIM-Karte eingesetzt ist, wird die Seite wie folgt angezeigt. Klicken Sie auf **Connect**.

    ![cellular unconnected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_unconnected.png){class="glboxshadow"}

    Wenn die SIM-Karte nicht erkannt wird, versuchen Sie, den Router neu zu starten, um zu prüfen, ob sie dann erkannt wird.

3. Sobald die Mobilfunkverbindung hergestellt ist, zeigt die Seite die Netzwerkdetails mit einem grünen Punkt an, was auf eine erfolgreiche Verbindung hinweist.

    ![cellular connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_connected.png){class="glboxshadow"}

4. Klicken Sie auf **View More Information**, um weitere Mobilfunkinformationen anzuzeigen, einschließlich Modemdetails, SIM-Kartendetails, Internetdetails und Mobilfunksignal.

    ![view more info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/view_more_info.png){class="glboxshadow"}

    ![cellular info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/cellular_info.jpg){class="glboxshadow gl-90-desktop"}

Wenn **Auto Setup** fehlschlägt, versuchen Sie bitte die [manuelle Einrichtung](#manual-setup-dual-sim).

### Manuelle Einrichtung {#manual-setup-dual-sim}

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** und klicken Sie dann auf **SIM Card Settings**.

![sim card settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_1.png){class="glboxshadow"}

Sie können die Mobilfunkeinstellungen der aktuellen SIM-Karte anzeigen oder ändern.

**Hinweis**: Manche SIM-Karten benötigen einen bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, wenden Sie sich bitte an Ihren Anbieter, um eventuelle Einschränkungen zu prüfen. Konfigurieren Sie bei Bedarf den korrekten APN auf Ihrem Router.

Durch das Anwenden der Änderungen wird die Verbindung neu aufgebaut.

![sim card settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/sim_card_settings_2.png){class="glboxshadow"}

- **APN**: APN (Access Point Name) ist ein Gateway-Parameter, der für eine Mobilfunkverbindung erforderlich ist. Er ermöglicht dem Router die Verbindung mit dem Internet Ihres Mobilfunkanbieters. Sie können den Standard-APN verwenden oder einen benutzerdefinierten APN Ihres Anbieters eintragen.

- **Protocol**: Das automatisch erkannte Mobilfunk-Kommunikationsprotokoll (z. B. QMI oder QCM) auf Basis Ihres Modems und Ihres Anbieters.

- **Port**: Der automatisch erkannte serielle Port für die Kommunikation mit dem Mobilfunkmodem.

- **TTL**: TTL (Time To Live) definiert, wie lange Pakete maximal im Netzwerk überleben können. Standardmäßig verringert der Router die TTL eingehender Pakete von Client-Geräten vor der Weiterleitung um 1. Falls Sie dies überschreiben müssen, können Sie hier einen festen Wert festlegen. Die TTL-Einstellung gilt nur für IPv4.

- **HL**: Unter IPv6 begrenzt HL (Hop Limit) die Anzahl der Übertragungssprünge von Datenpaketen im Netzwerk und entspricht TTL bei IPv4.

- **MTU**: Der Standardwert für MTU beträgt 1500 Byte.

- **Authentication**: Wählen Sie die von Ihrem Anbieter geforderte Authentifizierungsmethode (z. B. NONE, PAP, CHAP). In der Regel bleibt diese Einstellung auf NONE, wenn keine Zugangsdaten erforderlich sind.

- **Band Masking**: Sie können Band Masking aktivieren, wenn der Router bestimmte Bänder blockieren oder nur bestimmte Mobilfunkbänder verwenden soll. Details finden Sie [hier](#band-masking).

### Einstellungen für SIM-Kartensteckplätze

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** und klicken Sie dann auf **SIM Card Switch**.

![sim card switch](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_0.png){class="glboxshadow"}

Dort werden die Schaltfläche für das automatische Umschalten, die aktive SIM-Karte, die ICCID und der Netzbetreiber angezeigt.

![slot_settings_1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_1.png){class="glboxshadow"}

Wenn zwei SIM-Karten eingesetzt sind, können Sie **Auto Switch** aktivieren.

![slot_settings_2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/slot_settings_2.png){class="glboxshadow"}

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

## Einrichtung für USB-Modem

Die folgenden Schritte gelten für Modelle ohne integrierten SIM-Kartensteckplatz, die jedoch einen USB-Port zum Anschluss eines externen USB-Modems besitzen.

Hier verwenden wir den **GL-MT3000 (Beryl AX)** mit dem externen USB-Modem **SIMPoYo uFi** als Beispiel.

Wir empfehlen, den Router zunächst auszuschalten, eine bereits aktivierte SIM-Karte in das USB-Modem einzusetzen, das Modem in den USB-Port des Routers zu stecken und den Router anschließend einzuschalten. Wenn Sie das USB-Modem erst nach dem Start des Routers anschließen, wird das webbasierte Admin Panel möglicherweise nicht automatisch aktualisiert. Aktualisieren Sie in diesem Fall die Seite oder starten Sie den Router neu.

### Schnelleinrichtung

1. Schalten Sie zunächst den Router aus. Setzen Sie eine SIM-Karte in das USB-Modem ein, stecken Sie das Modem in den USB-Port des Routers und schalten Sie den Router anschließend ein.

2. Melden Sie sich am webbasierten Admin Panel des Routers an, navigieren Sie zu **INTERNET** -> **Tethering** und klicken Sie dann auf **Connect**.

    ![usb modem 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_1.png){class="glboxshadow"}

    Wenn Sie erweiterte Einstellungen wie TTL, HL und MTU festlegen möchten, klicken Sie auf **Advanced**, passen die Einstellungen an und klicken anschließend auf **Connect**.

    ![usb modem 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_2.png){class="glboxshadow"}

    Der Verbindungsaufbau wird gestartet.

    ![usb modem 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_3.png){class="glboxshadow"}

3. Sobald die Verbindung hergestellt ist, zeigt die Seite die Netzwerkdetails mit einem grünen Punkt an, was auf eine erfolgreiche Verbindung hinweist.

    ![usb modem 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/usb_modem_4.png){class="glboxshadow"}

    **Hinweis:** Nach der Ersteinrichtung wird das USB-Modem automatisch erkannt, wenn Sie den Router mit eingestecktem Modem neu starten oder das Modem erneut einstecken. Die Netzwerkverbindung wird dann hergestellt, ohne dass Sie erneut auf **Connect** klicken müssen.

### Kompatible Modems

Hier ist eine Liste unterstützter Modems, die wir bereits getestet haben.

**SIMPoYo uFi** ist ein kompakter Plug-and-Play-USB-Dongle mit Wi-Fi-Hotspot, der für schnelle und zuverlässige Konnektivität unterwegs entwickelt wurde. Er funktioniert nahtlos mit den meisten GL.iNet-Routern sowie mit Laptops, Powerbanks, USB-Anschlüssen im Auto und anderen USB-Stromquellen. Er enthält 10 GB kostenloses Datenvolumen für 30 Tage, gültig im Vereinigten Königreich und in 34 europäischen Ländern.

| Modell                                 | Mobilfunk | Getestet | Getestet von    | Hinweise* |
| -------------------------------------- | --------- | -------- | --------------- | --------- |
| [SIMPoYo 5G uFi](https://www.gl-inet.com/campaign/simpoyo-5g-ufi/)          | 5G        | Ja       | GL.iNet         |           |
| [SIMPoYo 4G uFi (SP-N150C4)](https://www.gl-inet.com/campaign/simpoyo-ufi/) | 4G        | Ja       | GL.iNet         |           |
| Quectel EC20-E, EC20-A, EC20-C         | 4G        | Ja       | GL.iNet         |           |
| Quectel EC25-E, EC25-A, EC25-V, EC25-C | 4G        | Ja       | GL.iNet         |           |
| Quectel EC200A series                  | 4G        | Ja       | akw2312         | Host-less |
| Quectel EP06-E, EP06-A                 | 4G        | Ja       | akw2312         |           |
| Quectel EM060K-GL, EM120K-GL           | 4G        | Ja       | akw2312         |           |
| Quectel EM120R-GL, EM160R-GL           | 4G        | Ja       | akw2312         |           |
| Quectel RM520N-GL                      | 5G        | Ja       | akw2312         |           |
| Quectel UC20-E                         | 3G        | Ja       | GL.iNet         |           |
| ZTE ME909s-821                         | 4G        | Ja       | GL.iNet         |           |
| Huawei E1550                           | 3G        | Ja       | GL.iNet         |           |
| Huawei E3276                           | 4G        | Ja       | GL.iNet         |           |
| Huawei E3372                           | 4G        | Ja       | anonymous       |           |
| Huawei E3372h-320 (Ukraine)            | 4G        | Ja       | anonymous       | Host-less |
| TP-Link MA260                          | 3G        | Ja       | GL.iNet         |           |
| ZTE M823                               | 4G        | Ja       | Arnas Risqianto |           |
| ZTE MF190                              | 3G        | Ja       | Arnas Risqianto |           |
| Pantech UML290VW (Verizon)             | 4G        | Ja       | GL.iNet/steven  | QMI       |
| Pantech UML295 (Verizon)               | 4G        | Ja       | GL.iNet/steven  | Host-less |
| Novatel USB551L (Verizon)              | 4G        | Ja       | GL.iNet/steven  | QMI       |
| Verizon U620L (Verizon)                | 4G        | Ja       | anonymous       | Host-less |

- **QMI**: Dieses Modem unterstützt den QMI-Modus. Wählen Sie bitte QMI als Mobilfunk-Kommunikationsprotokoll und **/dev/cdc-wdm0** als seriellen Port in den SIM-Karteneinstellungen.

- **Host-less**: Dieses Modem unterstützt den Tethering-Modus. Verwalten Sie die Verbindung in diesem Fall über die Tethering-Oberfläche des Routers und nicht über die Cellular-Oberfläche.

## Verkehrsstatistiken

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** und klicken Sie dann auf **Data Used**.

![traffic statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_0.png){class="glboxshadow"}

Sie gelangen auf die Seite **Traffic Statistics**. Dort werden die von der/den SIM-Karte(n) verbrauchten Daten angezeigt, und es stehen Einstellungen für Datenlimits zur Verfügung.

![traffic statistics 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_1.png){class="glboxshadow"}

Wenn **Data Used** den Wert von **Data Cap Amount** überschreitet, passen Sie bitte **Data Cap Amount** oder **Data Used** manuell an. Andernfalls kann die Netzwerkverbindung getrennt werden oder die SIM-Karte automatisch umschalten (bei Dual-SIM-Modellen).

- **Data Used ändern**

    Klicken Sie rechts neben **SIM 1/2 Data Used** auf **Modify**.

    ![traffic statistics 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_2.jpg){class="glboxshadow"}

    Anschließend können Sie den Datenverbrauch ändern oder zurücksetzen.

    ![traffic statistics 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_3_new.png){class="glboxshadow"}

- **SIM-Datenlimit einrichten**

    Wenn Sie ein Datenlimit für die SIM-Karte festlegen möchten, aktivieren Sie zuerst **Save data when power off**. Dadurch bleiben die Daten auch nach dem Ausschalten des Geräts erhalten.

    ![traffic statistics 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_4.png){class="glboxshadow"}

    Aktivieren Sie anschließend die Limit Settings für SIM 1 oder SIM 2.

    ![traffic statistics 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/traffic_statistics_5.jpg){class="glboxshadow"}

Bei Dual-SIM-Modellen empfehlen wir, gleichzeitig **SIM Card Slot Auto Switch** zu aktivieren. Wenn für SIM 1 ein **Data Cap Amount** gesetzt ist und **SIM Card Slot Auto Switch** aktiviert ist, schaltet SIM 1 automatisch auf SIM 2 um, sobald das Datenvolumen von SIM 1 den Wert von **Data Cap Amount** überschreitet, und SIM 1 wird deaktiviert.

## Signalverlauf

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** und klicken Sie dann auf **Historical Signal Record**.

![historical signal record](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_0.png){class="glboxshadow"}

Hier können Sie die Qualität Ihrer Mobilfunkverbindung prüfen. Wenn das Signal schwach ist, versuchen Sie, auf einen anderen Mast zu wechseln, um ein besseres Signal zu erhalten.

![historical signal record 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_1.png){class="glboxshadow"}

![historical signal record 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_2.png){class="glboxshadow"}

Den Verlauf der Signalstärke können Sie anzeigen, indem Sie oben rechts unterschiedliche Zeiträume auswählen.

![historical signal record 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/historical_signal_record_3.png){class="glboxshadow"}

## Band Masking

Mit Band Masking können Sie bestimmte Bänder blockieren oder nur bevorzugte Mobilfunkbänder verwenden, um ein schwaches Mobilfunksignal zu verbessern.

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular** -> **SIM Card Settings** und aktivieren Sie **Enable Band Masking**.

![single sim band masking](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/single_sim_band_masking.png){class="glboxshadow"}

Wählen Sie den **Masking Mode** (Block oder Open) und anschließend die LTE-Bänder, 5G-NSA-Bänder und 5G-SA-Bänder aus.

## SMS

Bitte lesen Sie das [SMS-Tutorial](sms.md).

## SMS Forwarding

Bitte lesen Sie das Tutorial [SMS Forwarding](../tutorials/sms_forwarding.md).

## Lock Tower

!!! note "Unterstützte Modelle"

    - GL-E5800 (Mudi 7)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-X2000 (Spitz Plus)*

    *Der GL-X2000 (Spitz Plus) unterstützt diese Funktion ab Firmware v4.7.

Wenn Sie ein hochwertiges Signal empfangen und eine stabile Mobilfunkverbindung sicherstellen möchten, können Sie **Lock Tower** ausprobieren.

**Hinweis:** Der gesperrte Mobilfunkmast muss zu den von Ihrem Anbieter und Gerät unterstützten Frequenzbändern passen, andernfalls kann die Verbindung fehlschlagen.

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular**. Klicken Sie oben rechts auf das Symbol mit den drei Punkten und wählen Sie dann **Lock Tower**.

![lock tower 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_0.png){class="glboxshadow"}

Klicken Sie auf **Scan**, um die Mobilfunkmasten zu scannen. Dies dauert einige Minuten. Aktualisieren Sie die Seite während des Scanvorgangs nicht.

![lock tower 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_1.png){class="glboxshadow"}

Daraufhin werden die verfügbaren Masten angezeigt.

![lock tower 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_2.png){class="glboxshadow"}

Klicken Sie auf einen Mast, um die Details anzuzeigen und ihn zu sperren.

![lock tower 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_tower_3.png){class="glboxshadow"}

**Hinweis**:

1. Das Gerät kann möglicherweise nicht alle Masten scannen, wenn die Cellular-Oberfläche aktiviert ist.

2. Wenn der gesperrte Mast nicht zu den Parametern für Band Masking oder APN in Ihren Mobilfunkeinstellungen passt, kann sich der Router nicht mit dem Mobilfunknetz verbinden.

3. Wenn Sie nach dem Sperren eines Mobilfunkmasts den Router an einen anderen Standort versetzen, versucht er nach einem Neustart weiterhin, sich mit dem gesperrten Mast zu verbinden. Dadurch kann verhindert werden, dass sich der Router am neuen Standort automatisch mit dem Mobilfunknetz verbindet. In diesem Fall müssen Sie entweder den aktuellen Mobilfunkmast entsperren oder ihn manuell auf einen neuen Mast sperren.

## Lock Operator

Diese Funktion ist nur auf GL-X3000, GL-XE3000 und GL-X2000 verfügbar (Firmware v4.8 oder neuer).

Durch das Sperren auf einen bestimmten Mobilfunkanbieter verwendet der Router nur noch dessen Netzwerk. Das sorgt für eine stabilere Verbindung und vermeidet unbeabsichtigte Roaming-Kosten – insbesondere in Grenzgebieten, in denen sich das Gerät sonst möglicherweise mit ausländischen Netzen verbindet.

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular**. Klicken Sie oben rechts auf das Symbol mit den drei Punkten und wählen Sie dann **Lock Operator**.

![lock operator 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_0.png){class="glboxshadow"}

Es gibt drei Sperrmodi:

- **Auto**: Verbindet sich automatisch mit einem verfügbaren Betreibernetz.
- **Manual**: Sperrt manuell auf einen bestimmten Betreiber.
- **Manual-Auto**: Wechselt automatisch zu einem verfügbaren Betreibernetz, wenn die manuelle Sperre fehlschlägt.

![lock operator 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/lock_operator_1.png){class="glboxshadow"}

## Modem AT Command

AT-Befehle für das Modem sind Standardanweisungen zur Kommunikation mit dem Mobilfunkmodem. Mit dieser Funktion können Sie Befehle senden und den Modemstatus prüfen.

Navigieren Sie im webbasierten Admin Panel des Routers zu **INTERNET** -> **Cellular**. Klicken Sie oben rechts auf das Symbol mit den drei Punkten und wählen Sie dann **Modem AT Command**.

![AT command 0](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}

Sie gelangen auf die Seite **AT Command**.

![AT command 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Wenn Shortcut auf **Manual command** gesetzt ist, können Sie den gewünschten Befehl im Feld **AT Command** eingeben.

Sie können auch auf das Shortcut-Dropdown klicken und aus einer Liste mit **vordefinierten Befehlen** wählen.

![AT command 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_2.png){class="glboxshadow"}

Die folgenden Befehle sind als Voreinstellungen verfügbar:

* IMEI anfordern
* QCCID anfordern
* IMSI anfordern
* Signalqualität prüfen
* Modem zurücksetzen
* Betreibernamen
* SIM-Kartenstatus anfordern

Als Beispiel ist hier die Voreinstellung „Request IMEI“ ausgewählt. Klicken Sie auf „Send“, dann erhalten Sie das unten gezeigte Ergebnis.

![AT command 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_3.png){class="glboxshadow"}

Unten rechts können Sie auf **Export Debug Info** klicken, um eine `.json`-Datei herunterzuladen.

![AT command 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_4.png){class="glboxshadow"}

## Fehlerbehebung

Wenn Sie keine Mobilfunkverbindung herstellen können, klicken Sie auf die folgende Fehlermeldung, um passende Lösungen anzuzeigen.

??? note "No SIM / Your SIM card has not been detected"

    ![no sim](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}

    Hier sind einige Vorschläge zur Fehlerbehebung.

    1. Aktualisieren Sie die Seite und warten Sie einige Minuten, um zu prüfen, ob die SIM-Karte erkannt wird.

    2. Stellen Sie sicher, dass die SIM-Karte korrekt eingesetzt ist. Richten Sie die Kerbe der SIM-Karte an der entsprechenden Markierung des Kartenschachts aus, um die korrekte Einsetzrichtung zu bestätigen.

    3. Schalten Sie den Router aus, entfernen Sie die SIM-Karte, setzen Sie sie erneut ein und schalten Sie den Router wieder ein.

    4. Versuchen Sie nach Möglichkeit eine andere SIM-Karte.

    Wenn das Problem weiterhin besteht, laden Sie die Protokolle herunter und senden Sie sie an [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "SIM card not registered / The interface is connected, but the Internet can't be accessed"

    Dieses Problem kann mit zwei Arten von Fehlermeldungen auftreten:

    - SIM card not registered

        ![sim not registered](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_not_registered.png){class="glboxshadow"}

    - The interface is connected, but the Internet can't be accessed

        ![connected no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected_no_internet.png){class="glboxshadow"}

    Hier sind einige Vorschläge zur Fehlerbehebung.

    1. Aktualisieren Sie die Seite und warten Sie einige Minuten, um zu prüfen, ob der Fehler verschwindet.

    2. Klicken Sie auf **Disconnect**/**Abort** und anschließend auf **Connect**, um die Verbindung erneut aufzubauen.

    3. Starten Sie den Router neu.

    4. Prüfen Sie den Status der SIM-Karte und stellen Sie sicher, dass sie aktiviert ist. Testen Sie die SIM-Karte in einem Smartphone, um zu bestätigen, dass sie mit einem aktiven Datentarif normal auf das Internet zugreifen kann, oder wenden Sie sich zur Überprüfung an Ihren Netzbetreiber.

    5. Manche Netzbetreiber benötigen für die Netzverbindung möglicherweise das 3G-Protokoll. Gehen Sie zu **SIM Card Settings** -> **Protocol**, wählen Sie **3G** und klicken Sie anschließend auf **Apply**.

        ![sim protocol](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-80-desktop"}

        Das Gerät verbindet sich automatisch erneut. Warten Sie einige Minuten und prüfen Sie dann, ob die Verbindung erfolgreich hergestellt wurde.

        ![connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connecting.png){class="glboxshadow"}

        Wenn die Verbindung erfolgreich ist, wird die Seite wie folgt angezeigt.

        ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/connected.png){class="glboxshadow"}

    6. Manche SIM-Karten haben besondere Nutzungseinschränkungen, z. B. die Vorgabe eines bestimmten APN. Wenn Ihre SIM-Karte sich nicht registrieren kann, kontaktieren Sie Ihren Anbieter und prüfen Sie, ob Einschränkungen vorliegen.

        Gehen Sie bei Bedarf zu **SIM Card Settings** -> **APN**, konfigurieren Sie den korrekten APN auf dem Router und klicken Sie anschließend auf **Apply**.

        ![sim apn](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-80-desktop"}

    7. Klicken Sie auf **View More Information**, um die Mobilfunk-Signalstärke zu prüfen. Wenn das Signal schwach ist, stellen Sie sicher, dass die Antenne korrekt installiert ist. Platzieren Sie den Router an einem offenen und möglichst unverbauten Standort, um den Signalempfang zu verbessern.

        ![cells signal](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow gl-80-desktop"}

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
