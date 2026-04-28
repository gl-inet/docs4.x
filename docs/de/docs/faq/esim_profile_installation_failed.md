# Was sollte ich tun, wenn die Installation des eSIM-Profils fehlschlägt?

Wenn Sie versuchen, auf Ihrem GL.iNet-Router ein eSIM-Profil hinzuzufügen, die Installation aber fehlschlägt, führen Sie bitte die folgenden Schritte zur Fehlerbehebung aus:

1. Stellen Sie sicher, dass der Router mit dem Internet verbunden ist.

    Bitte stellen Sie sicher, dass Ihr Router erfolgreich mit dem Internet verbunden ist. Eine instabile Netzwerkverbindung kann den Upload des eSIM-Profils beeinträchtigen, sodass der Router das Profil nicht abrufen und installieren kann.

    Versuchen Sie nach Möglichkeit, den Router mit einer anderen Netzwerkquelle zu verbinden, z. B. mit dem Hotspot Ihres Smartphones oder einem öffentlichen WLAN. Laden Sie Ihr eSIM-Profil anschließend erneut hoch.

2. DNS-Einstellungen ändern.

    Wenn das Internet ordnungsgemäß funktioniert, melden Sie sich im webbasierten Admin Panel des Routers an und gehen Sie zu **NETWORK** -> **DNS**.

    Stellen Sie den DNS-Modus auf **Manual DNS** um und konfigurieren Sie zum Testen andere öffentliche DNS-Server, z. B. Google DNS (`8.8.8.8`, `8.8.4.4`) oder Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Klicken Sie auf **Apply**, um die Änderungen zu speichern, und versuchen Sie dann erneut, Ihr eSIM-Profil hochzuladen.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. AdGuard Home deaktivieren.

    Falls AdGuard Home auf Ihrem Router verfügbar und aktiviert ist, deaktivieren Sie es und versuchen Sie dann erneut, Ihr eSIM-Profil zu installieren.

4. Verfügbarkeit des eSIM-Profils prüfen.

    Prüfen Sie, ob dieses eSIM-Profil oder dieser QR-Code bereits auf einem anderen Gerät aktiviert oder installiert wurde.

    Die meisten eSIM-Profile können nur einmal installiert werden und lassen sich nicht auf mehreren Geräten aktivieren. Kontaktieren Sie nach Möglichkeit Ihren eSIM-Anbieter, um zu bestätigen, ob das aktuelle eSIM-Profil noch verfügbar ist. Wenn der eSIM-QR-Code oder Aktivierungscode abgelaufen ist, beantragen Sie einen neuen und versuchen Sie es erneut.

5. Aktivierungscode prüfen.

    Ein korrekt formatierter QR-Code zeigt einen Aktivierungscode an, der mit **LPA:** beginnt. Einige nicht standardisierte QR-Codes liefern jedoch möglicherweise nur einen rohen Aktivierungscode ohne LPA-Präfix. Fügen Sie in diesem Fall vor dem Klicken auf **Install** manuell `LPA:` am Anfang des Codes hinzu.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Prüfen, ob ein Bestätigungscode erforderlich ist.

    Einige eSIM-Profile erfordern während der Installation die Eingabe eines Bestätigungscodes, z. B. Smarty eSIM. Prüfen Sie Ihr eSIM-Paket oder die Installationsanleitung, um festzustellen, ob ein Bestätigungscode benötigt wird. Falls ja, geben Sie den richtigen Code ein.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Wenn die oben genannten Schritte das Problem nicht lösen, exportieren Sie bitte das eSIM-Log auf der Seite **eSIM Management**.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Senden Sie das Log anschließend zusammen mit den folgenden wichtigen Informationen an [support@gl-inet.com](mailto:support@gl-inet.com), um weitere Unterstützung zu erhalten.

    - Das aufgetretene Problem
    - Bereits ausprobierte Methoden zur Fehlerbehebung
    - Ihr eSIM-Anbieter

---
