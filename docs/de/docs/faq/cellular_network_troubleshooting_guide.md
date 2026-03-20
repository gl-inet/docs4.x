# Leitfaden zur Fehlerbehebung bei Mobilfunknetzwerken

Wenn Sie keine Mobilfunkverbindung herstellen können, prüfen Sie bitte die folgenden Punkte.

??? "Gerätehardware prüfen"

    **1.1** Verwenden Sie für Ihr Gerät ein Standard-Netzteil. Nicht standardisierte Netzteile können zu einer unzureichenden Stromversorgung führen.
    
    **1.2** Stellen Sie sicher, dass **Modem name**, **IMEI** und **SIM ICCID** im web Admin Panel angezeigt werden.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/no_sim.png){class="glboxshadow"}
    
    Klicken Sie bei Firmware ver.4.8 und höher auf **View More Information**, um die SIM ICCID zu finden.

    Wenn Sie diese Angaben nicht finden können, starten Sie Ihren Router neu. Wenn **Modem name** und IMEI weiterhin nicht erkannt werden, kontaktieren Sie uns bitte unter [support@gl-inet.com](mailto:support@gl-inet.com).
    
    **1.3** Klicken Sie auf **View More**, um **Cells Info** zu prüfen und zu bestätigen, dass das Signal stabil ist. Wenn das Signal sehr schwach ist, stellen Sie sicher, dass die Antennen korrekt installiert sind, oder bringen Sie den Router in einen Bereich mit gutem Signal und testen Sie erneut.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/cells_info.png){class="glboxshadow"}
    
    **1.4** Klicken Sie auf **View More**, um zu prüfen, ob das von Ihrem Gerät unterstützte Frequenzband mit Ihrer Region kompatibel ist.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Softwareeinstellungen prüfen"

    **2.1** Melden Sie sich im web Admin Panel an und stellen Sie sicher, dass das Programm für die Mobilfunkverbindung gestartet wurde. Sie können auch auf **Abort** klicken und anschließend auf **Connect**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/2.png){class="glboxshadow gl-90-desktop"}
    
    **2.2** Einige Netzbetreiber erfordern möglicherweise das **3G**-Protokoll, um eine Verbindung herzustellen. Wechseln Sie zum 3G-Protokoll und testen Sie erneut.

    Gehen Sie bei Firmware ver.4.7 und früher zu **Manual Setup** -> **Protocol**, wählen Sie **3G** aus und klicken Sie dann auf **Apply**.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/3.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/4.png){class="glboxshadow gl-90-desktop"}

    Gehen Sie bei Firmware ver.4.8 und höher zu **SIM Card Settings** -> **Protocol**, wählen Sie **3G** aus und klicken Sie dann auf **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    Das Gerät wird die Verbindung automatisch erneut herstellen. Warten Sie einige Minuten und prüfen Sie dann, ob die Verbindung erfolgreich ist.

    **2.3** Einige SIM-Karten erfordern eine bestimmte APN. Wenn Ihre SIM-Karte nicht registriert werden kann, wenden Sie sich an Ihren Netzbetreiber, um mögliche Einschränkungen zu prüfen. Konfigurieren Sie bei Bedarf die korrekte APN auf Ihrem Router und klicken Sie dann auf **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}
    
    **2.4** Aktivieren Sie **Band Maksing** und testen Sie erneut. Informationen für Firmware ver.4.7 und früher finden Sie [unter diesem Link](../interface_guide/internet_cellular_v4.7.md/#band-masking). Informationen für Firmware ver.4.8 und höher finden Sie [unter diesem Link](../interface_guide/internet_cellular.md/#band-masking).

    **2.5** Sperren oder entsperren Sie einen Sendemast und testen Sie erneut. Diese Funktion ist nur auf GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) und GL-X2000 (Spitz Plus) verfügbar. Klicken Sie [hier](../interface_guide/internet_cellular.md/#lock-tower) für weitere Anweisungen.
    
    Die Sperrung auf einen bestimmten Sendemast ermöglicht dem Router den Zugriff auf eine hochwertige Netzwerkressource und sorgt für eine stabile Mobilfunkverbindung.
    
    Sobald ein Sendemast jedoch gesperrt ist, versucht der Router nach einem Neustart weiterhin, sich erneut mit diesem Mast zu verbinden, selbst wenn er an einen neuen Standort gebracht wurde. Dadurch kann verhindert werden, dass sich der Router automatisch mit dem Mobilfunknetz verbindet. In diesem Fall können Sie entweder den aktuellen Sendemast über das web Admin Panel des Routers entsperren oder ihn manuell auf einen neuen Sendemast festlegen.

    **Hinweis:** Der gesperrte Sendemast muss zu den von Ihrem Netzbetreiber und Ihrem Gerät unterstützten Frequenzbändern passen, andernfalls kann die Verbindung fehlschlagen.

??? "SIM-Kompatibilität prüfen"
    
    **3.1** Bestätigen Sie den SIM-Typ. GL.iNet-Mobilfunkrouter sind als IoT-Geräte zertifiziert. Theoretisch unterstützt das Gerät nur SIM-Karten vom IoT-Typ. Wenn Sie sich beim SIM-Typ nicht sicher sind, wenden Sie sich bitte an Ihren Netzbetreiber.
    
    Gängige SIM-Typen sind: data-only, data-only + voice, IoT und hotspot. Wir empfehlen die Verwendung von IoT- oder hotspot-SIM-Karten. Für data-only- oder data-only + voice-SIM-Karten kann die Funktion nicht garantiert werden.
    
    **3.2** Einige SIM-Karten müssen zunächst aktiviert werden. Stellen Sie sicher, dass die SIM-Karte auf das Internet zugreifen kann, wenn sie in ein Telefon eingelegt ist, und setzen Sie sie dann in den Router ein.
    
    **3.3** Einige angepasste SIM-Karten können nur in Mobiltelefonen oder bestimmten Geräten verwendet werden. Bitte prüfen Sie, ob die SIM-Karte an ein bestimmtes Gerät gebunden ist.
    
    **3.4** In einigen Bundesstaaten oder Städten der Vereinigten Staaten (z. B. AT&T in Seattle) müssen Sie möglicherweise die IMEI des Geräts bei Ihrem Netzbetreiber registrieren. Wenn Sie sich bezüglich der Registrierung nicht sicher sind, wenden Sie sich bitte an Ihren Netzbetreiber.
    
    **3.5** Wenn im web Admin Panel "SIM card not registered" angezeigt wird, versuchen Sie zuerst die oben genannten Schritte.

    Wir empfehlen, den Router auszuschalten, die SIM-Karte einzulegen und den Router anschließend neu zu starten. Einige Modelle unterstützen kein Hot-Swapping und erkennen die SIM-Karte möglicherweise nicht, wenn sie bei eingeschaltetem Gerät eingelegt wird.

    Stellen Sie sicher, dass alle Antennen ordnungsgemäß installiert sind, und testen Sie dann erneut in einem Außenbereich mit starkem Mobilfunksignal. Ein schwaches Signal kann verhindern, dass die SIM-Karte im Netzwerk registriert wird.

    Wenn das Problem weiterhin besteht, ist die SIM-Karte möglicherweise nicht mit dem Router kompatibel. Wenden Sie sich für weitere Unterstützung an Ihren Netzbetreiber.

    Wenn Ihr Netzbetreiber bestätigt, dass das Problem nicht mit der SIM-Karte zusammenhängt, kontaktieren Sie bitte unser Support-Team unter [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Wenn sich die SIM-Karte registrieren kann und eine IP-Adresse erhält, aber nicht auf das Internet zugreifen kann (Upload funktioniert, Download jedoch nicht), wird die SIM-Karte höchstwahrscheinlich von Ihrem Netzbetreiber eingeschränkt. Bitten Sie Ihren Netzbetreiber, die Einschränkung aufzuheben, oder setzen Sie TTL auf 65 und testen Sie erneut, wie unten gezeigt.
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/5.png){class="glboxshadow gl-90-desktop"}
    
    ![](https://static.gl-inet.com/docs/router/en/4/faq/x3000_xe3000_connection/6.png){class="glboxshadow gl-90-desktop"}

    Wenn Sie Ihren Netzbetreiber kontaktieren, geben Sie bitte **Modem name**, IMEI, SIM ICCID und das Routermodell Ihres Geräts an.
    
Wenn keine der oben genannten Maßnahmen das Problem löst, kontaktieren Sie bitte unser Support-Team unter [support@gl-inet.com](mailto:support@gl-inet.com).
