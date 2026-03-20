# Tailscale

Tailscale ist ein VPN-Dienst, mit dem die Geräte und Anwendungen, die Ihnen gehören, überall auf der Welt sicher und mühelos erreichbar werden. Weitere Informationen zu Tailscale finden Sie auf der [offiziellen Tailscale-Website](https://tailscale.com/).

Die Tailscale-Funktion auf GL.iNet-Routern, verfügbar seit Firmware V4.2, ermöglicht es dem Router, einem virtuellen Tailscale-Netzwerk beizutreten. Sobald die Verbindung hergestellt ist, können Sie per Fernzugriff auf den Router zugreifen, einschließlich seiner WAN- und LAN-Ressourcen.

**Hinweis**:

1. Da Tailscale auf WireGuard basiert, wird nicht empfohlen, Tailscale gleichzeitig mit einer der folgenden Funktionen oder Dienste zu verwenden, da dies zu Routing-Konflikten führen kann: OpenVPN Client, WireGuard Client, GoodCloud Site-to-Site, ZeroTier, AstroWarp.

2. Diese Funktion befindet sich derzeit in der Beta-Phase und kann einige Fehler enthalten.

3. GL.iNet-Router sind **noch nicht als Exit Nodes verfügbar**.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Nicht unterstützte Modelle"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-X300B (Collie)

## Tailscale-Netzwerk einrichten

Im folgenden Beispiel wird der GL-MT2500 verwendet.

1. Binden Sie Ihre Geräte ein.

    Registrieren Sie zunächst ein Tailscale-Konto und binden Sie dann ein oder zwei Geräte (z. B. Smartphone oder Laptop) zu Testzwecken an Ihr Tailscale-Konto.

    Nach dem Einbinden können Sie Ihre Geräte und deren Status in der Tailscale-Admin-Konsole sehen.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Aktivieren Sie Tailscale auf dem GL.iNet-Router.

    Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Aktivieren Sie Tailscale per Schalter und klicken Sie dann auf **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Nach kurzer Zeit zeigt die Oberfläche einen **Device Bind Link** an. Klicken Sie auf den Device Bind Link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    In dem Pop-up-Fenster wird ein Tailscale-Link angezeigt. Klicken Sie auf den Link, um zur Tailscale-Website weitergeleitet zu werden und sich anzumelden.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Nach der Anmeldung werden Sie aufgefordert, das Gerät zu bestätigen, mit dem Sie sich verbinden möchten. Klicken Sie auf **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Wenn die Verbindung erfolgreich ist, werden Sie automatisch zur Tailscale-Admin-Konsole weitergeleitet. Dort sehen Sie, dass die IP-Adresse des GL-MT2500 `100.88.54.21` ist. Diese IP können Sie nun verwenden, um auf den Router zuzugreifen.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Konnektivität testen.

    Auf Geräten, die mit demselben Tailscale-Netzwerk verbunden sind, können Sie die Konnektivität auf die folgenden drei Arten testen.

    * Den `ping`-Befehl verwenden

        ![ping](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ping.png){class="glboxshadow"}

    * Per SSH auf den Router zugreifen

        ![ssh](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/ssh.png){class="glboxshadow"}

    * Auf das Web-Admin-Panel zugreifen

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Fernzugriff auf WAN erlauben

Wenn diese Option aktiviert ist, kann über das virtuelle Tailscale-Netzwerk auf Ressourcen auf der WAN-Seite des Geräts zugegriffen werden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` über seine IP-Adresse (`192.168.29.1`) auf den `GL-AXT1800` zugreifen. Der Grund ist, dass der GL-AXT1800 das übergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben Tailscale-Netzwerk wie leo-phone verbunden ist.

![tailscale, remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Die Schritte sind wie folgt.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    Aktivieren Sie **Allow Remote Access WAN** und klicken Sie auf **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Gehen Sie zur Tailscale-Admin-Konsole. Dort wird ein Hinweis angezeigt, dass der GL-MT2500 Subnetze hat.

    Klicken Sie rechts neben dem GL-MT2500 auf das Dreipunkt-Symbol und wählen Sie **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Aktivieren Sie die Subnetzrouten.

    ![tailcale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Jetzt können Sie auf anderen Geräten über seine IP-Adresse (`192.168.29.1`) auf den GL-AXT1800 zugreifen. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.29.0/24` zugreifen.

    ![tailscale, access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Fernzugriff auf LAN erlauben

Wenn diese Option aktiviert ist, kann über das virtuelle Tailscale-Netzwerk auf Ressourcen auf der LAN-Seite des Geräts zugegriffen werden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` aus per SSH über die IP-Adresse (`192.168.8.110`) eine Anmeldung bei `Ubuntu` durchführen. Der Grund ist, dass `Ubuntu` das untergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben Tailscale-Netzwerk wie leo-phone verbunden ist.

![tailscale, remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Die Schritte sind wie folgt.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    Aktivieren Sie **Allow Remote Access LAN** und klicken Sie auf **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Gehen Sie zur Tailscale-Admin-Konsole. Dort wird ein Hinweis angezeigt, dass der GL-MT2500 Subnetze hat.

    Klicken Sie rechts neben dem GL-MT2500 auf das Dreipunkt-Symbol und wählen Sie **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Aktivieren Sie die Subnetzrouten.

    ![tailscale, enable subnet route](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Jetzt können Sie auf anderen Geräten `ping` an Ubuntu senden oder sich per SSH über dessen IP-Adresse (`192.168.8.110`) bei Ubuntu anmelden. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.8.0/24` zugreifen.

    ![tailscale, access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Benutzerdefinierte Exit Nodes

Mit der Funktion für Exit Nodes können Sie den gesamten Internetverkehr, der nicht über Tailscale läuft, über ein bestimmtes Gerät in Ihrem Netzwerk leiten. Das Gerät, das Ihren Datenverkehr routet, wird als "Exit Node" bezeichnet.

![exitnode](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

**Hinweis**: Wenn der DNS-Server des Routers eine private IP-Adresse ist, die nur im lokalen Netzwerk erreichbar ist, verlieren Sie möglicherweise den Internetzugang, wenn Sie Exit Nodes verwenden. Gehen Sie in diesem Fall bitte zu Network > DNS und setzen Sie als Lösung einen manuellen öffentlichen DNS-Server wie 8.8.8.8.

Einrichtungsschritte:

1. Wählen Sie auf dem Gerät, das Sie als Exit Node verwenden möchten, **Run exit node** aus. Unter Windows befolgen Sie die folgenden Schritte.

    ![tailscale windows, run exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Klicken Sie auf **Yes**.

    ![tailscale windows, run exit ndoe alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

2. Richten Sie das Gerät in der Admin-Konsole als Exit Node ein.

    ![tailscale exit node alert](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

3. Aktivieren Sie **Custom Exit Nodes** auf Ihrem GL-Router, klicken Sie auf die Schaltfläche zum Aktualisieren und wählen Sie im Dropdown-Menü die IP-Adresse des Geräts aus, das als Exit Node eingerichtet wurde. Klicken Sie anschließend auf **Apply**. Das ist alles.

    ![glinet tailscale, custom exit node](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

4. Die Geräte unter diesem GL-Router verwenden dann die Heim-IP der **Exit Node**.

[Weiterführender Link: Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/)

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
