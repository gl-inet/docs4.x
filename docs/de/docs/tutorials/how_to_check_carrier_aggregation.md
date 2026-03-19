# So prüfen Sie den Carrier-Aggregation-Status an Ihrem Mobilfunkrouter

Carrier Aggregation kombiniert mehrere Netzbänder, um für Ihre Mobilfunkverbindung mehr Bandbreite und höhere Geschwindigkeiten bereitzustellen.

Diese Funktion kann im Web-Admin-Panel des Routers nicht aktiviert werden, da sie von der Unterstützung Ihres Mobilfunkanbieters abhängt.

Sie können den Carrier-Aggregation-Status jedoch mithilfe von AT-Befehlen im Web-Admin-Panel des Routers prüfen.

!!! note "Unterstützte Modelle"

    - GL-E5800 (Mudi 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-X300B (Collie)
    - GL-AP1300LTE (Cirrus)

Befolgen Sie die folgenden Schritte, um den Carrier-Aggregation-Status zu prüfen.

1. Setzen Sie eine SIM-Karte in den Router ein.
2. Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an.
3. Gehen Sie zum Bereich **INTERNET** -> **Cellular**, klicken Sie oben rechts auf das Dreipunkt-Symbol und anschließend auf **Modem AT Command**.
    
    ![Modem-AT-Befehl](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/modem-at-command.png){class="glboxshadow"}

4. Geben Sie im Pop-up-Fenster **AT+QCAINFO** ein und klicken Sie auf **Send**.

    Wenn Carrier Aggregation aktiv ist, werden in der Liste mehrere Netzbänder angezeigt.
    
    ![AT+QCAINFO](https://static.gl-inet.com/docs/router/en/4/tutorials/carrier_aggregation/carrier-aggregation-info.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
