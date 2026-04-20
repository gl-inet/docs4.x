# Dynamic DNS

Dynamic Domain Name Service (Dynamic DNS oder DDNS) ist ein Dienst, der dazu dient, einen Domainnamen einer dynamischen IP-Adresse eines Netzwerkgeräts zuzuordnen. Mit Dynamic DNS können Sie aus der Ferne auf Ihren Router zugreifen. Für diese Funktion ist eine öffentliche Internet-IP-Adresse erforderlich.

## DDNS aktivieren

Gehen Sie auf der linken Seite des webbasierten Admin Panels zu **APPLICATIONS** -> **Dynamic DNS**.

![ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns.png){class="glboxshadow"}

Aktivieren Sie **Enable DDNS**, stimmen Sie den **Terms of Services & Privacy Policy** zu und klicken Sie dann auf **Apply**.

![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

Klicken Sie unten rechts auf **Security Settings**.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-1.png){class="glboxshadow"}

Prüfen Sie im Pop-up-Fenster, ob das gewünschte Fernzugriffsprotokoll aktiviert ist. Falls nicht, gehen Sie zu SYSTEM -> Security -> Remote Access Control und aktivieren Sie es dort.

![security settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/security_settings-2.png){class="glboxshadow"}

Aktivieren Sie das gewünschte Fernzugriffsprotokoll und klicken Sie auf **Apply**.

![security remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_enabled.jpg){class="glboxshadow"}

Bei der Synchronisierung der Einträge zwischen DNS-Servern kann es zu einer Verzögerung von bis zu 10 Minuten kommen. Dadurch ist der Zugriff über den DDNS-Domainnamen möglicherweise nicht sofort nach der Aktivierung oder nach einer Änderung Ihrer öffentlichen IP möglich.

**Hinweis**: Wenn Sie DDNS und den VPN-Client gleichzeitig aktivieren, stellen Sie sicher, dass **Services From GL.iNet Use VPN** deaktiviert ist. Diese Option finden Sie in den [VPN Client Options](vpn_dashboard_v4.8.md#tunnel-options) des VPN Dashboard.

## Prüfen, ob DDNS funktioniert

Sie können prüfen, ob DDNS funktioniert, indem Sie das DDNS-Testwerkzeug verwenden oder es manuell per Befehlen überprüfen.

=== "DDNS-Testwerkzeug verwenden"

    Klicken Sie auf der Seite Dynamic DNS auf **DDNS Test**.

    ![ddns test](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test.png){class="glboxshadow"}

    Stellen Sie sicher, dass die per DDNS-Domainauflösung ermittelte IP-Adresse mit der WAN-IP des Routers übereinstimmt.

    Falls nicht, erscheint oben ein gelber Hinweis. Das bedeutet, dass sich der Router möglicherweise hinter NAT befindet und Sie auf dem vorgelagerten Router eine Portweiterleitung einrichten müssen.

    ![ddns test prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/ddns_test_no_public_ip.png){class="glboxshadow"}

=== "Manuell prüfen"

    1. Verwenden Sie den Befehl `nslookup`, um die Zuordnung zwischen Domainnamen und IP-Adresse zu ermitteln, wie unten dargestellt.

        ![nslookup 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup1.jpg){class="glboxshadow"}

        Ersetzen Sie `xxxxxxx.glddns.com` im obigen Bild durch Ihren Host Name.

        `8.8.8.8` im obigen Bild ist der Google-DNS. Verwenden Sie ihn oder ersetzen Sie ihn durch einen anderen DNS-Server und drücken Sie dann die Eingabetaste.

    2. Wenn Sie als Ausgabe eine öffentliche IP-Adresse erhalten, z. B. `103.81.180.10` im folgenden Bild, bedeutet dies, dass Ihre DDNS-Domain erfolgreich einer öffentlichen IP-Adresse zugeordnet wurde.

        ![nslookup 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup2.jpg){class="glboxshadow"}
        
        Suchen Sie auf einem mit dem Router verbundenen Gerät in einem Browser nach „what is my ip address“ oder besuchen Sie eine Website wie [What Is My IP Address](https://whatismyipaddress.com){target="_blank"}. Dort wird Ihre öffentliche IP-Adresse angezeigt. Vergleichen Sie die beiden in Schritt 1 und 2 erhaltenen IP-Adressen. Sind sie identisch, ist DDNS wirksam; andernfalls nicht.

    3. Wenn Sie die Meldung `** server can't find xxxxxxx.glddns.com: NXDOMAIN` erhalten, wie unten dargestellt, bedeutet dies, dass die Domainauflösung fehlgeschlagen ist und Ihre DDNS-Domain nicht erfolgreich einer öffentlichen IP-Adresse zugeordnet wurde.

        ![nslookup 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/nslookup3.png){class="glboxshadow"}

## HTTPS-Fernzugriff

!!! Note

    1. Für den HTTPS-Fernzugriff ist eine **öffentliche IP-Adresse** erforderlich.

        Klicken Sie [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), um zu prüfen, ob Ihr Internetdienstanbieter (ISP) Ihnen eine öffentliche IP-Adresse zuweist.

    2. Wenn sich Ihr Router hinter NAT befindet, richten Sie auf dem vorgelagerten Router eine Portweiterleitung für Port **443** für den HTTPS-Zugriff ein.

Führen Sie die folgenden Schritte aus, um den HTTPS-Fernzugriff für Ihren Router zu aktivieren.

1. Aktivieren Sie auf der Seite Dynamic DNS **Enable DDNS**, stimmen Sie den **Terms of Services & Privacy Policy** zu und klicken Sie anschließend auf **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Gehen Sie im webbasierten Admin Panel zu SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Aktivieren Sie **HTTPS Remote Access** und klicken Sie auf **Apply**.

    ![enable https remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_https_remote_access.png){class="glboxshadow"}

Nach der Aktivierung können Sie das Admin Panel des Routers von überall über den DDNS-Hostnamen per **HTTPS** aufrufen (z. B. `https://xxxxxxx.glddns.com`).

Wenn eine Portweiterleitung eingerichtet ist, greifen Sie über `https://xxxxxxx.glddns.com:external_port` darauf zu (ersetzen Sie `external_port` durch Ihre tatsächliche Portnummer).

**Hinweis**: Diese Funktion verwendet selbstsignierte Zertifikate. Deshalb zeigen Browser beim Zugriff auf das Admin Panel des Routers über den DDNS-Hostnamen per **HTTPS** den Hinweis **Your connection is not private** an, wie unten dargestellt (Port 8001 wird im folgenden Beispiel verwendet).

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_0.jpg){class="glboxshadow" width="400"}

Um mit dem HTTPS-Fernzugriff fortzufahren, klicken Sie unten auf **Advanced**.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_1.png){class="glboxshadow" width="400"}

Klicken Sie anschließend auf **Proceed to xxxxxxx.glddns.com**, um fortzufahren.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_2.png){class="glboxshadow" width="400"}

Danach können Sie das webbasierte Admin Panel über den DDNS-Hostnamen per HTTPS aufrufen.

![HTTPS-Remote-Access-on-Android-Chrome](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/https_remote_access_android_chrome_3.png){class="glboxshadow" width="400"}

## SSH-Fernzugriff

!!! Note

    1. Für den SSH-Fernzugriff ist eine **öffentliche IP-Adresse** erforderlich.

        Klicken Sie [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), um zu prüfen, ob Ihr Internetdienstanbieter (ISP) Ihnen eine öffentliche IP-Adresse zuweist.

    2. Wenn sich Ihr Router hinter NAT befindet, richten Sie auf dem vorgelagerten Router eine Portweiterleitung für Port **22** für den SSH-Zugriff ein.

Führen Sie die folgenden Schritte aus, um den SSH-Fernzugriff für Ihren Router zu aktivieren.

1. Aktivieren Sie auf der Seite Dynamic DNS **Enable DDNS**, stimmen Sie den **Terms of Services & Privacy Policy** zu und klicken Sie anschließend auf **Apply**.

    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}

2. Gehen Sie im webbasierten Admin Panel zu SYSTEM -> Security -> Remote Access Control.

    ![remote access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/remote_access_disabled.png){class="glboxshadow"}

3. Aktivieren Sie **SSH Remote Access** und klicken Sie auf **Apply**.

    ![enable ssh remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ssh_remote_access.png){class="glboxshadow"}

Nach der Aktivierung können Sie den Router von überall über den DDNS-Hostnamen per **SSH** erreichen (z. B. `ssh root@xxxxxxx.glddns.com`).

Wenn eine Portweiterleitung eingerichtet ist, greifen Sie über `ssh root@xxxxxxx.glddns.com:external_port` darauf zu (ersetzen Sie `external_port` durch Ihre tatsächliche Portnummer).

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
