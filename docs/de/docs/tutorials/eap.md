# GL.iNet-Router mit einem EAP-Netzwerk verbinden {#connect-glinet-routers-to-an-eap-network}

Einige GL.iNet-Router unterstützen die Verbindung mit EAP-WLAN-Netzwerken (Extensible Authentication Protocol) als Repeater.

EAP ist ein Authentifizierungs-Framework, das häufig mit **802.1X-Authentifizierung** für **WPA2‑Enterprise / WPA3‑Enterprise**-Netzwerke verwendet wird. Ein typisches Beispiel ist **eduroam**, ein globaler WLAN-Roaming-Dienst für Bildung und Forschung, der auf 802.1X und EAP basiert.

Dieses Framework bietet mehrere EAP-Authentifizierungsmethoden, darunter EAP-PEAP, EAP-TLS, EAP-TTLS und EAP-FAST. Nicht alle EAP-Methoden werden von allen Router-Oberflächen und Modellen unterstützt.

Diese Anleitung beschreibt zwei Möglichkeiten, GL.iNet-Router mit einem EAP-WLAN-Netzwerk zu verbinden: über das GL.iNet Web-Admin-Panel und über LuCI. Die beiden Möglichkeiten bieten unterschiedliche EAP-Authentifizierungsmethoden: Das Web-Admin-Panel bietet nur **EAP-PEAP**, LuCI dagegen **EAP-TLS**, **EAP-TTLS**, **EAP-PEAP** und **EAP-FAST**.

Einige GL.iNet-Router unterstützen die EAP-Repeater-Funktion nur über eine dieser beiden Möglichkeiten. Prüfen Sie die unten aufgeführten unterstützten Modelle.

### Unterstützte Modelle {#supported-models}

??? "Unterstützte Modelle"
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - <u>GL-BE14000 (Flint 4)</u><sup>1</sup>
    - <u>GL-BE10000 (Slate 7 Pro)</u><sup>1</sup>
    - <u>GL-MT3600BE (Beryl 7)</u><sup>1</sup>
    - <u>GL-BE6500 (Flint 3e)</u><sup>1</sup>
    - <u>GL-BE9300 (Flint 3)</u><sup>1</sup>
    - <u>GL-BE3600 (Slate 7)</u><sup>1</sup>
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - <u>GL-MT6000 (Flint 2)</u><sup>2</sup>
    - <u>GL-MT3000 (Beryl AX)</u><sup>2</sup>
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - <u>GL-SFT1200 (Opal)</u><sup>3</sup>
    - GL-A1300 (Slate Plus)
    - GL-XE300 (Puli)
    - GL-E750/GL-E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

    ---

    **Hinweis**:

    1. GL-BE14000 (Flint 4), GL-BE10000 (Slate 7 Pro), GL-MT3600BE (Beryl 7), GL-BE6500 (Flint 3e), GL-BE9300 (Flint 3) und GL-BE3600 (Slate 7) unterstützen EAP-PEAP-Netzwerke als Repeater nur über das GL.iNet Web-Admin-Panel. Andere EAP-Methoden (EAP-TLS, EAP-TTLS, EAP-FAST usw.) werden nicht unterstützt.

    2. GL-MT6000 (Flint 2) und GL-MT3000 (Beryl AX) unterstützen mit der Standard-Firmware keine EAP-Netzwerke als Repeater, weder über das GL.iNet Web-Admin-Panel noch über LuCI. GL.iNet stellt jedoch OpenWrt-Firmware mit EAP-Unterstützung (einschließlich EAP-PEAP, EAP-TLS, EAP-TTLS und EAP-FAST) für diese Modelle bereit. Suchen Sie im [Download Center](https://dl.gl-inet.com/){target="_blank"} nach Ihrem Modell und wählen Sie die Registerkarte OPENWRT, um weitere Details zu erhalten.

    3. GL-SFT1200 (Opal) unterstützt ab Firmware v4.8 EAP-Netzwerke als Repeater. Die EAP-Authentifizierungsmethoden umfassen EAP-PEAP, EAP-TLS, EAP-TTLS und EAP-FAST.

    4. Mit Ausnahme der in den obigen Hinweisen genannten Modelle können alle anderen unterstützten Modelle als Repeater eine Verbindung zu EAP-Netzwerken herstellen. Die EAP-Authentifizierungsmethoden umfassen EAP-PEAP, EAP-TLS, EAP-TTLS und EAP-FAST.

??? "Nicht unterstützte Modelle"
    - GL-MT6000 (Fortify)
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Verbindung über das Web-Admin-Panel {#connect-via-web-admin-panel}

Über das GL.iNet Web-Admin-Panel können Sie Ihren Router als Repeater mit EAP-PEAP-Netzwerken verbinden.

1. Melden Sie sich im Web-Admin-Panel an, gehen Sie zum Abschnitt **INTERNET** -> **Repeater** und klicken Sie dann auf **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Es werden die verfügbaren Netzwerke gescannt. Suchen Sie die EAP-SSID und wählen Sie sie aus, um eine Verbindung herzustellen.

    ![scan available networks](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Oder klicken Sie oben rechts auf **Join Other Network**, um dem EAP-Netzwerk manuell beizutreten.

    ![join other network](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Geben Sie die **SSID** ein.

    ![input ssid](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Wählen Sie bei **Security** die Option **WPA/WPA2/WPA3 Enterprise**.

    ![select security](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Apply**, um die Verbindung herzustellen.

    ![input username and Password](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Verbindung über LuCI {#connect-via-luci}

Über LuCI können Sie Ihren Router als Repeater mit einem EAP-TLS-, EAP-TTLS-, EAP-PEAP- oder EAP-FAST-Netzwerk verbinden.

Die folgenden Schritte dienen nur als Referenz. Orientieren Sie sich an der tatsächlichen LuCI-Seite Ihres Geräts.

1. Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **SYSTEM** -> **Advanced Settings**. Installieren Sie LuCI und klicken Sie auf **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Melden Sie sich mit demselben Admin-Passwort an der LuCI-Oberfläche an und gehen Sie zu **Network** -> **Wireless**.

    ![wireless](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Klicken Sie im Abschnitt 2.4G oder 5G auf **Scan**.

    ![scan](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Treten Sie dem gewünschten Netzwerk bei.

    ![join network](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Fehlerbehebung {#troubleshooting}

Wenn das gewünschte EAP-Netzwerk zusätzliche Parameter erfordert, etwa den EAP-Typ (z. B. PEAP, TTLS), eine Domain-Suffix-Übereinstimmung, die Identität, die anonyme Identität usw., kann die EAP-Verbindung über das Web-Admin-Panel fehlschlagen.

![connection failed](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/connection_failed.png){class="glboxshadow"}

Befolgen Sie die folgenden Schritte, um Ihren GL.iNet-Router über die LuCI-Oberfläche mit EAP-Netzwerken zu verbinden, die erweiterte Einstellungen erfordern.

1. Konfigurationsdaten beschaffen.

    Beschaffen Sie sich die Konfigurationsparameter für das gewünschte EAP-Netzwerk im Voraus. Zum Beispiel:

    - EAP-Typ (z. B. PEAP, TTLS, TLS)
    - Authentifizierungs-Domain-Suffix (z. B. @company.com)
    - Identität (in der Regel der vollständige Benutzername)
    - Anonyme Identität (optional)
    - Innerer Authentifizierungstyp (z. B. MSCHAPv2, PAP)
    - CA-Zertifikat (falls erforderlich, bereiten Sie eine Datei im Format `.crt` vor)

    Dies ist ein Beispiel für Xfinity Mobile Wi-Fi als Referenz.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Bei LuCI anmelden.

    Melden Sie sich am Web-Adminbereich des Routers an. Falls Sie zuvor versucht haben, sich über die WebGUI mit dem gewünschten EAP-Netzwerk zu verbinden und dies fehlgeschlagen ist, brechen Sie die Verbindung bitte ab.

    ![abort connection](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/abort_connection.png){class="glboxshadow"}

    Gehen Sie dann zu **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Melden Sie sich mit demselben Admin-Passwort bei LuCI an.

    ![luci login](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Repeater in LuCI konfigurieren.

    Gehen Sie in der LuCI-Oberfläche zu Network -> Wireless.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/wireless.png){class="glboxshadow"}

    Klicken Sie im 5G- oder 2.4G-Bereich auf die Schaltfläche **Scan**, um nach verfügbaren WLAN-Netzwerken zu suchen.

    ![wireless scan](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/wireless_scan.png){class="glboxshadow"}

    Suchen Sie in den Scan-Ergebnissen das gewünschte EAP-Netzwerk und klicken Sie auf **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/scan_results.png){class="glboxshadow"}

    Geben Sie auf der Seite "Joining Network" die **WPA passphrase** ein und klicken Sie auf **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/joining_network.png){class="glboxshadow"}

    Sie werden zur Konfiguration des Wireless Clients weitergeleitet.

4. Suchen Sie **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/wireless_security.jpg){class="glboxshadow"}

    Wählen bzw. geben Sie die korrekten Konfigurationsparameter entsprechend Ihrem Ziel-EAP-Netzwerk ein, wie unten gezeigt. **Klicken Sie noch nicht auf Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/wireless_security_example.png){class="glboxshadow"}

5. Wechseln Sie zur Registerkarte **Advanced Settings**, geben Sie einen Schnittstellennamen wie **wlan0** an und klicken Sie dann unten rechts auf **Save**.

    ![advanced settings](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/advanced_settings.png){class="glboxshadow"}

6. Sie kehren zur Seite **Wireless** zurück, auf der ausstehende Änderungen angezeigt werden. Klicken Sie unten rechts auf **Save & Apply**.

    ![save abd apply](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/save_apply.png){class="glboxshadow"}

    Ihr Router wird nun erfolgreich mit dem gewünschten EAP-Netzwerk verbunden.

7. Verbindung überprüfen.

    ??? "Verbindung in der WebGUI prüfen"

        Sobald der Router erfolgreich mit dem gewünschten EAP-Netzwerk verbunden ist, leuchtet in der WebGUI ein Repeater-Symbol auf, wie unten dargestellt.

        ![connected status](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/connected_status.png){class="glboxshadow"}

        **Hinweis**: Da die Konfiguration in LuCI nicht mit der in der WebGUI synchronisiert wird, erscheinen Details der Repeater-Schnittstelle (z. B. verbundene IP, Gateway usw.) nicht in der WebGUI.
        
        Wie im Bild zu sehen, ist der Repeater-Bereich unten leer. Der Router ist jedoch bereits als Repeater mit dem gewünschten EAP-Netzwerk verbunden, da das Repeater-Symbol oben leuchtet.

    ??? "Verbindung per SSH prüfen"

        1. Melden Sie sich per [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} an Ihrem Router an.

        2. Geben Sie **ifconfig** ein und drücken Sie die Eingabetaste.

            ![ifconfig](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/ifconfig.png){class="glboxshadow"}

            Sie können dann den Status der Schnittstelle **wlan0** prüfen.

            ![ifconfig](https://static.gl-inet.com/docs/router/de/4/tutorials/eap/ifconfig_2.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
