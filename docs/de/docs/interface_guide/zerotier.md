# ZeroTier

ZeroTier ist ein softwarebasiertes virtuelles privates Netzwerk (VPN), das eine sichere, verschlüsselte Kommunikation zwischen Geräten über das Internet ermöglicht. Es erstellt ein privates, virtuelles Netzwerk, in dem Geräte so miteinander kommunizieren können, als befänden sie sich im selben lokalen Netzwerk – unabhängig von ihrem physischen Standort oder der Netzwerktopologie. ZeroTier ist auf eine einfache Einrichtung und Nutzung ausgelegt und bietet Funktionen wie Ende-zu-Ende-Verschlüsselung, Netzwerksegmentierung und Network Bridging.

Die ZeroTier-Funktion auf GL.iNet-Routern, verfügbar seit Firmware v4.2, ermöglicht es dem Router, einem virtuellen ZeroTier-Netzwerk beizutreten. Sobald die Verbindung hergestellt ist, können Sie per Fernzugriff auf den Router zugreifen, einschließlich seiner WAN- und LAN-Ressourcen.

**Hinweis**:

1. Es wird nicht empfohlen, ZeroTier gleichzeitig mit einer der folgenden Funktionen oder Dienste zu verwenden, da dies zu Routing-Konflikten führen kann: OpenVPN Client, WireGuard Client, GoodCloud Site-to-Site, Tailscale, AstroWarp.

2. Diese Funktion befindet sich derzeit in der Beta-Phase und kann einige Fehler enthalten.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
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
    - GL-X2000 (Spitz Plus)
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

## ZeroTier-Netzwerk einrichten

Es gibt zwei Versionen von ZeroTier Central: New Central und Legacy Central.

- **New Central**: Eine neuere Version von ZeroTier Central mit verbesserter Benutzerfreundlichkeit und neuen Funktionen. Für neue Benutzer wird diese Version empfohlen, um die beste Erfahrung und die neuesten Werkzeuge zu erhalten.

- **Legacy Central**: Für Konten, die vor November 2025 erstellt wurden. Legacy Central unterstützt weiterhin bestehende Benutzer bei der Verwaltung ihrer Netzwerke.

Beide Versionen können parallel verwendet werden, aber derzeit gibt es keinen direkten Migrationspfad.

Bitte wählen Sie die passende Version, um fortzufahren.

### New Central

Im Folgenden wird der GL-MT3600BE als Beispiel verwendet.

1. Besuchen Sie die [offizielle ZeroTier-Website](https://www.zerotier.com/){target="_blank"} und melden Sie sich mit Ihrem Konto an.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_login.jpg){class="glboxshadow"}

2. Erstellen Sie eine Organisation.

    ![create organization](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/create_org.png){class="glboxshadow"}

3. Wählen Sie einen Tarif aus. Hier verwenden wir als Beispiel den Personal-Plan, der 10 Geräte, 1 Netzwerkadministrator und 1 Netzwerk umfasst. Wenn Sie mehr Netzwerke erstellen, zusätzliche Geräte hinzufügen oder benutzerdefinierte Routen und DNS hinzufügen müssen, wählen Sie den Essential- oder Scale-Plan.

    ![select plan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/select_plan.png){class="glboxshadow"}

4. Jetzt wurde Ihr ZeroTier-Netzwerk erstellt. Notieren Sie sich die **Network ID**, eine 16-stellige alphanumerische Kombination oben rechts, da sie später benötigt wird, wenn Sie weitere Geräte verbinden.

    ![network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zt_network_id.png){class="glboxshadow"}

5. Aktivieren Sie ZeroTier auf dem GL.iNet-Router.

    Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **ZeroTier**.

    Aktivieren Sie ZeroTier, geben Sie auf derselben Seite die Network ID ein und klicken Sie auf **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/enable_zerotier.png){class="glboxshadow"}

    Nach kurzer Zeit zeigt die Oberfläche an, dass eine Autorisierung erforderlich ist. Klicken Sie auf den Hyperlink **ZeroTier Central**, um zu ZeroTier Central weitergeleitet zu werden.

    ![authorize 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize1.png){class="glboxshadow"}

6. Autorisieren Sie Ihr Gerät in ZeroTier Central.

    Suchen Sie in ZeroTier Central das ausstehende Gerät und autorisieren Sie es.

    ![authorize 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize2.png){class="glboxshadow"}

    Nach der Autorisierung wird die Seite wie folgt angezeigt.

    ![authorized 1](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized1.png){class="glboxshadow"}

7. Fügen Sie ein weiteres Gerät (z. B. einen Computer oder ein Smartphone) demselben ZeroTier-Netzwerk hinzu, indem Sie [dieser Anleitung](https://docs.zerotier.com/platforms/){target="_blank"} folgen.

    Nachfolgend sehen Sie ein Beispiel mit einem Laptop unter Windows 10 Pro.

    1. Installieren Sie ZeroTier auf dem Laptop [hier](https://www.zerotier.com/download/){target="_blank"}.

    2. Starten Sie ZeroTier. Das ZeroTier-Symbol erscheint im Infobereich unten rechts auf dem Desktop.

    3. Klicken Sie mit der rechten Maustaste auf das Symbol, wählen Sie **Join New Network** und geben Sie im Pop-up-Fenster die **Network ID** ein, die Sie in Schritt 4 erhalten haben.

        ![laptop join network](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/laptop_join_network.png){class="glboxshadow"}

        Wechseln Sie anschließend zu ZeroTier Central, suchen Sie das ausstehende Gerät und autorisieren Sie es.

        ![authorize 3](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorize3.png){class="glboxshadow"}

    4. Nach der Autorisierung wird die Seite wie folgt angezeigt. Sie sehen die Details der Mitgliedsgeräte, z. B. **Device ID**, **Name**, **Status**, **Managed IP** und **Public IP**.

        ![authorized 2](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/authorized2.png){class="glboxshadow"}

        **Tipps**: Sie können rechts auf das Dreipunkt-Symbol klicken, um die Einstellungen des Mitgliedsgeräts zu bearbeiten, einschließlich Gerätename, Managed IP(s) und erweiterter Einstellungen.

8. Klicken Sie auf die **Managed IP** des Routers, um sie zu kopieren. Anschließend können Sie diese Managed IP verwenden, um von Ihrem Laptop aus auf den Router zuzugreifen, der sich im selben ZeroTier-Netzwerk befindet.

    ![zerotier virtual ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/zerotier_virtual_ip.png){class="glboxshadow"}

9. Testen Sie die Konnektivität.

    Öffnen Sie auf dem Laptop, der mit demselben ZeroTier-Netzwerk verbunden ist, einen Webbrowser und geben Sie die Managed IP des Routers ein, die Sie im vorherigen Schritt erhalten haben.

    Wenn Sie auf die Web-Adminoberfläche des Routers zugreifen können, ist die ZeroTier-Verbindung erfolgreich.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test1.png){class="glboxshadow"}

    Sie können auch die Managed IP des Routers von Ihrem Laptop aus mit `ping` testen. Wenn Sie eine erfolgreiche Antwort erhalten, wurde die ZeroTier-Verbindung erfolgreich hergestellt.

    ![ping test](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/new_central/connectivity_test2.png){class="glboxshadow"}

### Legacy Central

Im Folgenden wird der GL-MT2500 als Beispiel verwendet.

1. Erstellen Sie Ihr erstes ZeroTier-Netzwerk.

    Lesen Sie die offizielle ZeroTier-[Getting Started Guide](https://docs.zerotier.com/getting-started/getting-started/){target="_blank"}, um ein ZeroTier-Konto und ein Netzwerk zu erstellen. Denken Sie daran, sich die Network ID zu notieren, eine 16-stellige alphanumerische Kombination, da sie später benötigt wird, wenn Sie weitere Geräte verbinden.

    ![zerotier network id](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_network_id.png){class="glboxshadow"}

2. Aktivieren Sie ZeroTier auf dem GL.iNet-Router.

    Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **ZeroTier**.

    Aktivieren Sie ZeroTier, geben Sie auf derselben Seite die Network ID ein und klicken Sie auf **Apply**.

    ![enable zerotier](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_enable.png){class="glboxshadow"}

    Nach kurzer Zeit zeigt die Oberfläche an, dass eine Autorisierung erforderlich ist.

    Klicken Sie auf den Hyperlink **ZeroTier Central**, um zu ZeroTier Central weitergeleitet zu werden.

    ![zerotier central](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_central.png){class="glboxshadow"}

3. Autorisieren Sie Ihr Gerät in ZeroTier Central.

    Gehen Sie in ZeroTier Central zum Abschnitt **Members**. Suchen Sie das neue Gerät und klicken Sie auf das Kontrollkästchen **Auth**, um es zu autorisieren. Wenn gewünscht, können Sie den Namen des Geräts anpassen.

    ![zerotier members, auth](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_members_auth.png){class="glboxshadow"}

    Nach kurzer Zeit weist ZeroTier dem Gerät eine **Managed IP** zu. Notieren Sie sich diese IP-Adresse, da sie im Testschritt benötigt wird.

    ![zerotier managed ip](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/managed_ip.png){class="glboxshadow"}

4. Fügen Sie ein weiteres Gerät (z. B. einen Computer oder ein Smartphone) demselben ZeroTier-Netzwerk hinzu, indem Sie [dieser Anleitung](https://docs.zerotier.com/platforms/){target="_blank"} folgen.

5. Testen Sie die Konnektivität.

    Öffnen Sie auf einem anderen Gerät, das mit demselben ZeroTier-Netzwerk verbunden ist, einen Webbrowser und geben Sie die ZeroTier-Managed-IP des Routers ein, die Sie im vorherigen Schritt erhalten haben.

    Sie können auf die Web-Adminoberfläche des Routers zugreifen.

    ![web admin panel](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/web_admin_panel.png)

    Sie können die Konnektivität auch mit dem Befehl `ping` testen. Lesen Sie dazu bitte die ZeroTier-[Quickstart Guide](https://docs.zerotier.com/quickstart/#6-test-your-connection){target="_blank"}.

## Fernzugriff auf WAN erlauben

Wenn diese Option aktiviert ist, kann über das virtuelle ZeroTier-Netzwerk auf Ressourcen auf der WAN-Seite des Geräts zugegriffen werden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` über seine IP-Adresse (`192.168.29.1`) auf den `GL-AXT1800` zugreifen. Der Grund ist, dass der GL-AXT1800 das übergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben ZeroTier-Netzwerk wie leo-phone verbunden ist.

![remote access wan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_wan_topology.png){class="glboxshadow"}

**Hinweis**: Damit diese Funktion wirksam wird, müssen dem ZeroTier-Netzwerk Routing-Regeln hinzugefügt werden. In Legacy Central kann kostenlos eine benutzerdefinierte Route hinzugefügt werden, während Sie in New Central benutzerdefinierte Routen nur mit einem Essential-Plan oder höher konfigurieren können. Klicken Sie [hier](https://www.zerotier.com/pricing/) für Details.

Die folgenden Schritte verwenden Legacy Central als Beispiel.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **ZeroTier**.

    Aktivieren Sie **Allow Remote Access WAN** und klicken Sie auf **Apply**.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_1.png){class="glboxshadow"}

    Es erscheint eine Aufforderung, Routing-Regeln zu konfigurieren. Lassen Sie diese Webseite geöffnet oder notieren Sie sich die Routendetails (Destination und Via), da diese im nächsten Schritt benötigt werden.

    ![enable allow remote access wan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_wan_2.png){class="glboxshadow"}

2. Gehen Sie zu **ZeroTier Central** und suchen Sie den Abschnitt **Advanced**.

    Geben Sie die Routendetails (Destination und Via) aus dem vorherigen Schritt ein und klicken Sie dann auf **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_1.png){class="glboxshadow"}

    Nach dem Hinzufügen der Route wird der Abschnitt **Managed Routes** wie unten gezeigt angezeigt.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_2.png){class="glboxshadow"}

3. Sie können nun auf anderen Geräten über seine IP-Adresse (`192.168.29.1`) auf den `GL-AXT1800` zugreifen. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.29.0/24` zugreifen.

    ![access axt1800](https://static.gl-inet.com/docs/router/en/4/tutorials/tailscale/tailscale_access_axt1800.jpg){class="glboxshadow gl-50-desktop"}

## Fernzugriff auf LAN erlauben

Wenn diese Option aktiviert ist, kann über das virtuelle ZeroTier-Netzwerk auf Ressourcen auf der LAN-Seite des Geräts zugegriffen werden.

Wie in der folgenden Topologie gezeigt, können Sie bei aktivierter Funktion beispielsweise vom `leo-phone` aus per SSH über seine IP-Adresse (`192.168.8.110`) eine Anmeldung bei `Ubuntu` durchführen. Der Grund ist, dass `Ubuntu` das untergeordnete Gerät des `GL-MT2500` ist und letzterer mit demselben ZeroTier-Netzwerk wie leo-phone verbunden ist.

![remote access lan topology](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_lan_topology.png){class="glboxshadow"}

**Hinweis**: Damit diese Funktion wirksam wird, müssen dem ZeroTier-Netzwerk Routing-Regeln hinzugefügt werden. In Legacy Central kann kostenlos eine benutzerdefinierte Route hinzugefügt werden, während Sie in New Central benutzerdefinierte Routen nur mit einem Essential-Plan oder höher konfigurieren können. Klicken Sie [hier](https://www.zerotier.com/pricing/) für Details.

Die folgenden Schritte verwenden Legacy Central als Beispiel.

1. Melden Sie sich in der Web-Adminoberfläche Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **ZeroTier**.

    Aktivieren Sie **Allow Remote Access LAN** und klicken Sie auf **Apply**.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_1.png){class="glboxshadow"}

    Es erscheint eine Aufforderung, Routing-Regeln zu konfigurieren. Lassen Sie diese Webseite geöffnet oder notieren Sie sich die Routendetails (Destination und Via), da diese im nächsten Schritt benötigt werden.

    ![enable allow remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/enable_allow_remote_access_lan_2.png){class="glboxshadow"}

2. Gehen Sie zu **ZeroTier Central** und suchen Sie den Abschnitt **Advanced**.

    Geben Sie die Routendetails (Destination und Via) aus dem vorherigen Schritt ein und klicken Sie dann auf **Submit**.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_3.png){class="glboxshadow"}

    Nach dem Hinzufügen der Route wird der Abschnitt **Managed Routes** wie unten gezeigt angezeigt.

    ![add route](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/add_routes_4.png){class="glboxshadow"}

3. Sie können nun auf anderen Geräten per `ping` oder SSH über die IP-Adresse (`192.168.8.110`) auf `Ubuntu` zugreifen. Tatsächlich können Sie auf alle Geräte innerhalb des Subnetzes `192.168.8.0/24` zugreifen.

    ![access ubuntu](https://static.gl-inet.com/docs/router/en/4/tutorials/zerotier/zerotier_access_ubuntu.jpg){class="glboxshadow gl-80-desktop"}

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
