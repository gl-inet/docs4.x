# Keine Verbindung zu einem verschleierten WireGuard-Server möglich

VPN-Verschleierung ist eine Technik, bei der VPN-Datenverkehr wie normaler Internetverkehr aussieht. Derzeit unterstützen einige GL.iNet-Router das AmneziaWG-Protokoll, sodass Sie einen WireGuard-Server mit aktivierter Datenverkehrsverschleierung einrichten können.

Wenn keine Verbindung zu einem verschleierten WireGuard-Server hergestellt werden kann, führen Sie die folgenden Schritte zur Fehlerbehebung aus.

1. **Stellen Sie sicher, dass die in jeden Client importierte WireGuard-Konfiguration dediziert ist.**

    Jeder Client benötigt eine eigene Peer-Konfigurationsdatei. Wenn mehrere Clients dieselbe Konfiguration verwenden, schlägt die Verbindung fehl.

    Falls erforderlich, gehen Sie zu **VPN** -> **WireGuard Server** -> **Profiles**, um Ihre exportierten Profile anzuzeigen.

    ![wg profiles](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/wg_profiles.png){class="glboxshadow"}

2. **Stellen Sie sicher, dass die verschleierten Parameter vom Client verifiziert werden können.**

    Das AmneziaWG-Protokoll ist abwärtskompatibel. Wenn Ihr WireGuard-Server nur AmneziaWG v1.0 unterstützt, besteht die Konfigurationsdatei beim Import in einen Client mit v2.0-Unterstützung trotzdem die Verifizierung.
        
    Wenn Ihre Konfigurationsdatei jedoch Verschleierungsparameter von AmneziaWG v2.0 enthält, stellen Sie sicher, dass Ihr WireGuard-Client AmneziaWG v2.0 unterstützt. Andernfalls kann die Parameterverifizierung fehlschlagen.

    !!! tip "Wie erkennt man die AmneziaWG-Version?"

        **V1.0**: Keine S3-S4-Parameter; H1-H4 sind feste einzelne Ganzzahlen.
        
        **V2.0**: Es handelt sich um V2.0, wenn eine der folgenden Bedingungen erfüllt ist:
        
        - Enthält S3-S4-Parameter
        - H1-H4 sind als Zahlenbereiche festgelegt
        - Enthält angepasste I1-I5-Parameter.
        
        > Hinweis: I1-I5 werden nicht automatisch generiert. Benutzer können sie manuell als zusätzliche Zeilen in der Konfigurationsdatei ergänzen, damit AmneziaWG-Datenverkehr wie andere gängige Protokolle wie QUIC oder WebRTC aussieht.

    Wenn Ihr WireGuard-Client ein GL.iNet-Router ist, prüfen Sie dessen AmneziaWG-Version mit den folgenden zwei Methoden.

    ??? note "Über das Router Web Admin Panel prüfen"

        1. Melden Sie sich am Web Admin Panel Ihres Routers an.

        2. Gehen Sie zu **VPN** -> **WireGuard Server** -> **Configuration** und prüfen Sie die Verschleierungsparameter. Wenn die Konfiguration **S3-S4** und **H1-H4** als variable Bereiche enthält, statt fester Werte, läuft auf dem Router AmneziaWG 2.0, wie unten gezeigt.

            ![awg 2.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_web.png){class="glboxshadow"}

            Andernfalls wird AmneziaWG 1.0 verwendet, wie unten gezeigt.

            ![awg 1.0 web](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_web.png){class="glboxshadow"}

    ??? note "Über SSH-Befehl prüfen"

        1. Melden Sie sich per SSH am Router an.

        2. Führen Sie `opkg list|grep awg` aus und prüfen Sie das Suffix des Pakets **kmod-amneziawg** in der Ausgabe. Wenn es mit **2.0** gekennzeichnet ist, unterstützt der Router AmneziaWG 2.0, wie unten gezeigt.

            ![awg 2.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_2.0_ssh.png){class="glboxshadow"}

            Andernfalls wird AmneziaWG 1.0 ausgeführt, wie unten gezeigt.

            ![awg 1.0 ssh](https://static.gl-inet.com/docs/router/en/4/faq/cannot_connect_to_obfuscated_wgserver/awg_1.0_ssh.png){class="glboxshadow"}

3. **Passen Sie die Verschleierungsparameter an.**

    Wenn Sie [Verschleierungsparameter](amneziawg_obfuscation.md#parameter-overview) wie Jc, Jmin oder Jmax auf Ihrem WireGuard-Server manuell konfiguriert haben, können falsche Parameter zu Handshake-Fehlern führen.

    Ändern Sie diese Verschleierungsparameter testweise und stellen Sie die Verbindung erneut her, um Parameterabweichungen auszuschließen. Sie können zum Testen auch die Standardwerte für die Verschleierung wiederherstellen.

4. **Testen Sie die Verbindung mit der offiziellen AmneziaWG App.**

    Führen Sie einen Vergleichstest durch: Installieren Sie die offizielle AmneziaWG App, importieren Sie die original vom Server exportierte Konfigurationsdatei in die App und versuchen Sie, eine Verbindung herzustellen.

    - Wenn die Verbindung in der offiziellen App funktioniert, ist die Konfigurationsdatei gültig. Das Problem liegt möglicherweise beim ursprünglichen Client-Gerät. Prüfen Sie dessen Netzwerkverbindung oder wenden Sie sich an den Support.

    - Wenn die Verbindung weiterhin fehlschlägt, liegt das Problem an der Router-Server-Konfiguration. Prüfen Sie die Servereinstellungen und Verschleierungsparameter.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
