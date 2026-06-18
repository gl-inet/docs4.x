# Tailscale

Tailscale ist ein VPN-Dienst, mit dem die Geräte und Anwendungen, die Ihnen gehören, überall auf der Welt sicher und mühelos erreichbar werden. Weitere Informationen zu Tailscale finden Sie auf der [offiziellen Tailscale-Website](https://tailscale.com/).

Die Tailscale-Funktion auf GL.iNet-Routern, verfügbar seit Firmware V4.2, ermöglicht es dem Router, einem virtuellen Tailscale-Netzwerk beizutreten. Sobald die Verbindung hergestellt ist, können Sie per Fernzugriff auf den Router zugreifen, einschließlich seiner WAN- und LAN-Ressourcen.

**Hinweis**:

1. Da Tailscale auf WireGuard basiert, wird nicht empfohlen, Tailscale gleichzeitig mit einer der folgenden Funktionen oder Dienste zu verwenden, da dies zu Routing-Konflikten führen kann: OpenVPN Client, WireGuard Client, GoodCloud Site-to-Site, ZeroTier, AstroWarp.

2. Diese Funktion befindet sich derzeit in der Beta-Phase und kann einige Fehler enthalten.

3. Einige Modelle unterstützen Tailscale trotz Firmware v4.2 oder höher aufgrund unzureichenden Arbeitsspeichers nicht.

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

    Nach dem Einbinden können Sie Ihre Geräte und deren Status in der Tailscale Admin Console sehen.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_1.png){class="glboxshadow"}

2. Aktivieren Sie Tailscale auf dem GL.iNet-Router.

    Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    ![glinet tailscale disabled](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_disabled.png){class="glboxshadow"}

    Aktivieren Sie Tailscale per Schalter und klicken Sie dann auf **Apply**.

    ![glinet enable tailscale](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_tailscale.png){class="glboxshadow"}

3. Nach kurzer Zeit zeigt die Oberfläche einen **Device Bind Link** an. Klicken Sie auf den Device Bind Link.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_1.png){class="glboxshadow"}

    In dem Pop-up-Fenster wird ein Tailscale-Link angezeigt. Klicken Sie auf den Link, um zur Tailscale-Website weitergeleitet zu werden und sich anzumelden.

    ![glinet bind link](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_bind_link_2.png){class="glboxshadow"}

    Nach der Anmeldung werden Sie aufgefordert, das Gerät zu bestätigen, mit dem Sie sich verbinden möchten. Klicken Sie auf **Connect**.

    ![tailscale confirm connect device](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_connect_device.png){class="glboxshadow gl-70-desktop"}

    Wenn die Verbindung erfolgreich ist, werden Sie automatisch zur Tailscale Admin Console weitergeleitet. Dort sehen Sie, dass die IP-Adresse des GL-MT2500 `100.88.54.21` ist. Diese IP können Sie nun verwenden, um auf den Router zuzugreifen.

    ![tailscale admin console](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_admin_console_2.png){class="glboxshadow"}

3. Konnektivität testen.

    Auf Geräten, die mit demselben Tailscale-Netzwerk verbunden sind, können Sie die Konnektivität auf die folgenden drei Arten testen.

    * Den `ping`-Befehl verwenden

        ![ping](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ping.png){class="glboxshadow"}

    * Per SSH auf den Router zugreifen

        ![ssh](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/ssh.png){class="glboxshadow"}

    * Auf das Web-Admin-Panel zugreifen

        ![web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/web_admin_panel.png){class="glboxshadow gl-80-desktop"}

## Fernzugriff auf WAN erlauben

> Diese Funktion wurde in Firmware v4.9 und höher in **Advertise WAN Subnets** umbenannt.

Wenn diese Option aktiviert ist, kann über das virtuelle Tailscale-Netzwerk auf Ressourcen auf der WAN-Seite des Geräts zugegriffen werden. Routen werden erst wirksam, nachdem sie in der Tailscale Admin Console genehmigt wurden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` über seine IP-Adresse (`192.168.29.1`) auf den `GL-AXT1800` zugreifen. Der Grund ist, dass der GL-AXT1800 das übergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben Tailscale-Netzwerk wie leo-phone verbunden ist.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_wan_topology.png){class="glboxshadow"}

Die Schritte sind wie folgt.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    Aktivieren Sie **Allow Remote Access WAN** und klicken Sie auf **Apply**.

    ![enable remote access wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_wan.png){class="glboxshadow"}

2. Gehen Sie zur Tailscale Admin Console. Dort wird ein Hinweis angezeigt, dass der GL-MT2500 Subnetze hat.

    Klicken Sie rechts neben dem GL-MT2500 auf das Dreipunkt-Symbol und wählen Sie **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

3. Aktivieren Sie die Subnetzrouten.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

4. Jetzt können Sie auf anderen Geräten über seine IP-Adresse (`192.168.29.1`) auf den GL-AXT1800 zugreifen. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.29.0/24` zugreifen.

    ![tailscale access axt1800](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Fernzugriff auf LAN erlauben

> Diese Funktion wurde in Firmware v4.9 und höher in **Advertise LAN Subnets** umbenannt.

Wenn diese Option aktiviert ist, kann über das virtuelle Tailscale-Netzwerk auf Ressourcen auf der LAN-Seite des Geräts zugegriffen werden. Routen werden erst wirksam, nachdem sie in der Tailscale Admin Console genehmigt wurden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` aus per SSH über die IP-Adresse (`192.168.8.110`) eine Anmeldung bei `Ubuntu` durchführen. Der Grund ist, dass `Ubuntu` das untergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben Tailscale-Netzwerk wie leo-phone verbunden ist.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_lan_topology.png){class="glboxshadow"}

Die Schritte sind wie folgt.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **Tailscale**.

    Aktivieren Sie **Allow Remote Access LAN** und klicken Sie auf **Apply**.

    ![enable remote access lan](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/enable_allow_remote_access_lan.png){class="glboxshadow"}

2. Gehen Sie zur Tailscale Admin Console. Dort wird ein Hinweis angezeigt, dass der GL-MT2500 Subnetze hat.

    Klicken Sie rechts neben dem GL-MT2500 auf das Dreipunkt-Symbol und wählen Sie **Edit route settings**.

    ![tailscale subnet alert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_lan.png){class="glboxshadow"}

3. Aktivieren Sie die Subnetzrouten.

    ![tailscale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes_lan.png){class="glboxshadow"}

4. Jetzt können Sie auf anderen Geräten `ping` an Ubuntu senden oder sich per SSH über dessen IP-Adresse (`192.168.8.110`) bei Ubuntu anmelden. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.8.0/24` zugreifen.

    ![tailscale access ubuntu](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_access_ubuntu.png){class="glboxshadow gl-80-desktop"}

## Benutzerdefinierte Exit Nodes

Standardmäßig arbeitet Tailscale als Overlay-Netzwerk: Es leitet nur Datenverkehr zwischen Geräten weiter, auf denen Tailscale ausgeführt wird, und verarbeitet keinen öffentlichen Internetverkehr, etwa beim Aufrufen von Websites wie Google.

Es gibt jedoch Situationen, in denen Tailscale auch Ihren öffentlichen Internetverkehr leiten soll. Wenn Sie beispielsweise unterwegs oder im Ausland sind und auf Online-Dienste wie Banking zugreifen möchten, die nur in Ihrem Heimatland verfügbar sind, können Sie Ihren Heim-Desktop mit öffentlicher IP als Exit Node einrichten und andere Geräte im selben Tailnet – wie den unten gezeigten GL-AXT1800 und GL-MT3000 – so konfigurieren, dass ihr Datenverkehr über dieses Gerät geleitet wird. Dadurch wird Ihr gesamter öffentlicher Internetverkehr über die Exit Node weitergeleitet.

![exitnode](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/exitnode.jpg){class="glboxshadow"}

Wenn der gesamte Datenverkehr über eine Exit Node geleitet wird, verwenden Sie effektiv die Standardrouten (0.0.0.0/0, ::/0), was ähnlich wie eine gewöhnliche VPN-Verbindung funktioniert.

Kurz gesagt: Eine Exit Node leitet ausgehenden Internetverkehr von Ihren Tailnet-Geräten weiter und fungiert damit praktisch als VPN-Server. Wenn Sie mit einer Exit Node verbunden sind, scheint Ihr gesamter nicht über Tailscale laufender Internetverkehr von deren Standort aus zu stammen. Das hilft beim Zugriff auf geografisch eingeschränkte Inhalte und verbessert Ihre Privatsphäre. Das Gerät, das diese Weiterleitung übernimmt, wird als „Exit Node“ bezeichnet.

**Hinweis**: Wenn der DNS-Server des Routers eine private IP-Adresse verwendet, die nur im lokalen Netzwerk erreichbar ist, können Sie beim Verwenden einer Exit Node den Internetzugang verlieren. Melden Sie sich in diesem Fall am Router an, gehen Sie zu **NETWORK** -> **DNS** und setzen Sie manuell einen öffentlichen DNS-Server wie 8.8.8.8.

---

Im folgenden Beispiel befinden sich ein GL.iNet-Router **GL-MT2500** und ein **Leo-Desktop** im selben Tailnet. Im Folgenden wird beschrieben, wie Sie Leo-Desktop als Exit Node einrichten.

1. Aktivieren Sie die Subnetzrouten des GL-MT2500 in der Tailscale Admin Console.

    Gehen Sie zur Tailscale Admin Console, klicken Sie rechts neben GL-MT2500 auf das Symbol mit den drei Punkten und wählen Sie **Edit route settings**.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_subnet_alert_wan.png){class="glboxshadow"}

    Aktivieren Sie im Pop-up-Fenster die Subnetzrouten.

    ![tailcale enable subnet route](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/tailscale_enable_subnet_routes.png){class="glboxshadow"}

2. Wählen Sie auf dem Gerät, das Sie als Exit Node verwenden möchten – in diesem Beispiel Leo-Desktop – **Run exit node** aus. Nachfolgend sehen Sie ein Beispiel unter Windows.

    ![tailscale windows run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node.png){class="glboxshadow"}

    Klicken Sie dann auf **Yes**.

    ![tailscale windows run exit ndoe](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_run_exit_node_alert.png){class="glboxshadow"}

3. Richten Sie Leo-Desktop in der Tailscale Admin Console als Exit Node ein.

    ![tailscale edit route settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_exit_node_alert.png){class="glboxshadow"}

    ![tailscale use as exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/tailscale_use_as_exit_node.png){class="glboxshadow"}

4. Melden Sie sich im Web-Admin-Panel des GL-MT2500 an, gehen Sie zu **APPLICATIONS** -> **Tailscale** und aktivieren Sie **Custom Exit Nodes**. Klicken Sie auf die Schaltfläche zum Aktualisieren, wählen Sie im Dropdown-Menü die IP-Adresse des Leo-Desktop aus und klicken Sie dann auf **Apply**.

    ![glinet tailscale custom exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/custom_exit_node.png){class="glboxshadow"}

    Geräte, die mit dem Router verbunden sind, leiten ihren Datenverkehr dann über die Exit Node ins Internet, und Ihr gesamter Internetverkehr scheint vom Standort der Exit Node aus zu stammen.

5. **Fehlerbehebung**: Wenn Geräte, die mit dem GL.iNet-Router verbunden sind, nach dem Aktivieren von **Custom Exit Node** nicht auf das Internet zugreifen können, prüfen Sie in der Tailscale Admin Console, ob die Subnetzrouten des Routers aktiviert sind.

    Im Web-Admin-Panel des Routers kann ein entsprechender Hinweis wie unten dargestellt erscheinen.

    ![exit node troubleshooting](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/custom_exit_nodes/troubleshooting.jpg){class="glboxshadow"}

    Aktivieren Sie zur Behebung die Subnetzrouten des Routers in der Tailscale Admin Console wie in **Schritt 1** oben beschrieben.

## Run Exit Node

> Diese Funktion wurde mit Firmware v4.9 eingeführt.

Wenn der Router als Exit Node ausgeführt wird, können andere Geräte in Ihrem Tailnet ihren gesamten ausgehenden Internetverkehr über die öffentliche IP dieses Routers leiten.

In der folgenden Topologie befindet sich ein Laptop in Boston, während der GL-BE9300-Router in Hongkong eingesetzt wird. Beide Geräte wurden demselben Tailscale-Tailnet hinzugefügt. Wenn Sie den GL-BE9300 als Exit Node festlegen, verlässt der gesamte ausgehende Datenverkehr des Laptops das Internet über diesen Router in Hongkong, und die externe öffentliche IP-Adresse des Laptops wird als Hongkong-IP statt als Boston-IP erkannt.

![topology run exit node](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/topology.png){class="glboxshadow"}

***Tipp**: Wir empfehlen, den Ablauf des Schlüssels für den Exit Node zu deaktivieren, um Verbindungsunterbrechungen nach Ablauf des Authentifizierungsschlüssels zu vermeiden.*

Führen Sie die folgenden Schritte aus, um den GL-BE9300 als Exit Node festzulegen.

1. Fügen Sie GL-BE9300 und den Reise-Laptop demselben Tailscale-Tailnet hinzu.

    ![tailnet](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tailnet.png){class="glboxshadow"}

2. Aktivieren Sie im Web Admin Panel des GL-BE9300 **Run Exit Node** und klicken Sie auf **Apply**.

    ![run exit node1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node1.png){class="glboxshadow"}

3. In der Tailscale Admin Console erscheint unter dem GL-BE9300 das Tag "Exit Node".

    ![run exit node2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node2.png){class="glboxshadow"}

4. Klicken Sie rechts neben GL-BE9300 auf das Dreipunkt-Symbol und wählen Sie **Edit route settings**.

    ![run exit node3](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node3.png){class="glboxshadow"}

5. Aktivieren Sie im Pop-up-Fenster **Use as exit node** und klicken Sie auf **Save**.

    ![run exit node4](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node4.png){class="glboxshadow"}

6. Deaktivieren Sie den Ablauf des Schlüssels.

    Aus Sicherheitsgründen müssen sich Benutzer regelmäßig auf ihren Geräten erneut authentifizieren. Um Verbindungsunterbrechungen zu vermeiden, wenn der Authentifizierungsschlüssel des Exit Node abläuft, empfehlen wir, den Ablauf des Schlüssels für den Exit Node zu deaktivieren. Weitere Details zum Schlüsselablauf finden Sie [hier](https://tailscale.com/docs/features/access-control/key-expiry){target="_blank"}.

    Klicken Sie rechts neben GL-BE9300 auf das Dreipunkt-Symbol und wählen Sie **Disable key expiry**.

    ![disable key expiry1](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry1.png){class="glboxshadow"}

    Danach erscheint unter dem GL-BE9300 das Tag "Expiry disabled".

    ![disable key expiry2](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/disable_key_expiry2.png){class="glboxshadow"}

7. Wählen Sie GL-BE9300 als Exit Node für Ihren Reise-Laptop aus.

    Führen Sie Tailscale auf dem Reise-Laptop aus. Das Tailscale-Symbol erscheint unten rechts im Infobereich.

    Klicken Sie mit der rechten Maustaste auf das Symbol, klicken Sie auf **Exit nodes** und wählen Sie **gl-be9300**.

    ![run exit node5](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/run_exit_node5.png){class="glboxshadow"}

    Jetzt verlässt der gesamte ausgehende Datenverkehr dieses Reise-Laptops das Internet über GL-BE9300.

8. Testen Sie die Verbindung.

    1. Öffnen Sie auf dem Reise-Laptop einen Webbrowser und besuchen Sie [ipcheck.ing](https://ipcheck.ing/){target="_blank"} oder eine andere IP-Prüfseite. Die Seite zeigt die öffentliche IP-Adresse Ihres Tailscale Exit Node an und bestätigt damit, dass der Laptop über den Exit Node auf das Internet zugreift, in diesem Beispiel über den GL-BE9300 in Hongkong.

        ![ip hk](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_hk.png){class="glboxshadow"}

    2. Drücken Sie `Win+R`, geben Sie `cmd` ein, um die Eingabeaufforderung zu öffnen, und führen Sie dann `tracert google.com` aus, um die Route des ausgehenden Datenverkehrs zu verfolgen. Die Befehlsausgabe listet alle Routing-Hops für Ihren Internetverkehr auf. Bei korrekter Konfiguration läuft der erste externe Hop über den Exit Node, wie unten gezeigt.

        ![tracert](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/tracert.png){class="glboxshadow"}

    3. Trennen Sie den Exit Node für einen Vergleichstest.

        Klicken Sie mit der rechten Maustaste auf das Tailscale-Symbol unten rechts im Infobereich, klicken Sie auf **Exit nodes** und wählen Sie **None**, um den Exit Node nicht mehr zu verwenden.

        ![comparative test](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/comparison_test.png){class="glboxshadow"}

        Öffnen Sie einen neuen Browser-Tab und besuchen Sie [ipcheck.ing](https://ipcheck.ing/){target="_blank"} oder einen anderen IP-Prüfdienst. Nun wird die ursprüngliche öffentliche IP-Adresse des Laptops angezeigt. Damit wird bestätigt, dass das Gerät stattdessen seine lokale Internetverbindung verwendet, in diesem Beispiel Boston.

        ![ip boston](https://static.gl-inet.com/docs/router/en/4/interface_guide/tailscale/run_exit_node/ip_boston.png){class="glboxshadow"}

---

Referenzen: [Exit Nodes (route all traffic)](https://tailscale.com/kb/1103/exit-nodes/){target="_blank"}

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
