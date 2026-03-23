# GL.iNet-Router mit einem EAP-Netzwerk verbinden

Einige GL.iNet-Router unterstützen die Verbindung mit EAP-WLAN-Netzwerken (Extensible Authentication Protocol).

EAP ist ein Authentifizierungs-Framework, das häufig mit **802.1X-Authentifizierung** für **WPA2‑Enterprise / WPA3‑Enterprise**-Netzwerke verwendet wird. Ein typisches Beispiel ist **eduroam**, ein globaler WLAN-Roaming-Dienst für Bildung und Forschung, der auf 802.1X und EAP basiert.

In dieser Anleitung werden zwei Möglichkeiten beschrieben, wie Sie GL.iNet-Router mit einem EAP-WLAN-Netzwerk verbinden können: über das Admin Panel und über LuCI.

## Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
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
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)
    - ※GL-SFT1200 (Opal)

    **Hinweis:** 
    
    1. GL-MT6000 (Flint 2) und GL-MT3000 (Beryl AX) unterstützen mit der Standard-Firmware keine Verbindung zu EAP-Netzwerken. GL.iNet stellt jedoch native OpenWrt-24-Firmware für diese Modelle bereit, die installiert werden kann, um EAP-Verbindungen zu unterstützen. Suchen Sie im [Download Center](https://dl.gl-inet.com/){target="_blank"} nach dem Modell und wechseln Sie zur Registerkarte **OPENWRT 24**, um weitere Details zu erhalten.

    2. GL-SFT1200 (Opal) unterstützt mit Firmware v4.8 die Verbindung zu EAP-Netzwerken.

??? "Nicht unterstützte Modelle"
    - GL-MT5000 (Brume 3)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT1300 (Beryl)
    - GL-MT300N-V2 (Mango)

## Verbindung über das Web-Admin-Panel

1. Melden Sie sich im Web-Admin-Panel an, gehen Sie zum Abschnitt **INTERNET** -> **Repeater** und klicken Sie dann auf **Connect**.

    ![repeater connect](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/repeater_connect.png){class="glboxshadow"}

    Es werden die verfügbaren Netzwerke gescannt. Suchen Sie die EAP-SSID und wählen Sie sie aus, um eine Verbindung herzustellen.

    ![scan available networks](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/scan_available_wifi.png){class="glboxshadow"}

    Oder klicken Sie oben rechts auf **Join Other Network**, um dem EAP-Netzwerk manuell beizutreten.

    ![join other network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/join_other_network.png){class="glboxshadow"}

2. Geben Sie die **SSID** ein.

    ![input ssid](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/ssid.png){class="glboxshadow"}

3. Wählen Sie bei **Security** die Option **WPA/WPA2/WPA3 Enterprise**.

    ![select security](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/select_security.jpg){class="glboxshadow"}

4. Geben Sie **Username** und **Password** ein und klicken Sie dann auf **Apply**, um die Verbindung herzustellen.

    ![input username and Password](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/username_and_password.jpg){class="glboxshadow"}

## Verbindung über LuCI

Das GL.iNet Web-Admin-Panel unterstützt nur eine begrenzte Anzahl von EAP-Typen.

Wenn sich Ihr gewünschtes EAP-Netzwerk nicht über das Web-Admin-Panel verbinden lässt, versuchen Sie bitte die Verbindung über die LuCI-Oberfläche.

1. Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **SYSTEM** -> **Advanced Settings**. Installieren Sie LuCI und klicken Sie auf **Go to LuCI**.

    ![gotoluci](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/gotoluci.png){class="glboxshadow"}

2. Melden Sie sich mit demselben Admin-Passwort an der LuCI-Oberfläche an und gehen Sie zu **Network** -> **Wireless**.

    ![wireless](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_network_wireless.png){class="glboxshadow"}

3. Klicken Sie im Abschnitt 2.4G oder 5G auf **Scan**.

    ![scan](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_wireless_scan.png){class="glboxshadow"}

4. Treten Sie dem gewünschten Netzwerk bei.

    ![join network](https://static.gl-inet.com/docs/router/en/4/tutorials/eap/luci_join_network.png){class="glboxshadow"}

## Fehlerbehebung

Wenn das gewünschte EAP-Netzwerk zusätzliche Parameter erfordert, etwa den EAP-Typ (z. B. PEAP, TTLS), eine Domain-Suffix-Übereinstimmung, die Identität, die anonyme Identität usw., kann die EAP-Verbindung über das Web-Admin-Panel fehlschlagen.

![connection failed](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connection_failed.png){class="glboxshadow"}

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

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/xfinity_mobile_config.png){class="glboxshadow gl-50-desktop"}

2. Bei LuCI anmelden.

    Melden Sie sich am Web-Adminbereich des Routers an. Falls Sie zuvor versucht haben, sich über die WebGUI mit dem gewünschten EAP-Netzwerk zu verbinden und dies fehlgeschlagen ist, brechen Sie die Verbindung bitte ab.

    ![abort connection](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/abort_connection.png){class="glboxshadow"}

    Gehen Sie dann zu **SYSTEM** -> **Advanced Settings** -> **Go to LuCI**. Melden Sie sich mit demselben Admin-Passwort bei LuCI an.

    ![luci login](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/luci_login.jpg){class="glboxshadow gl-70-desktop"}

3. Repeater in LuCI konfigurieren.

    Gehen Sie in der LuCI-Oberfläche zu **Network** -> **Wireless**.

    ![xfinity wifi configs](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless.png){class="glboxshadow"}

    Klicken Sie im 5G- oder 2.4G-Bereich auf die Schaltfläche **Scan**, um nach verfügbaren WLAN-Netzwerken zu suchen.

    ![wireless scan](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_scan.png){class="glboxshadow"}

    Suchen Sie in den Scan-Ergebnissen das gewünschte EAP-Netzwerk und klicken Sie auf **Join Network**.

    ![scan results](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/scan_results.png){class="glboxshadow"}

    Geben Sie auf der Seite "Joining Network" die **WPA passphrase** ein und klicken Sie auf **Submit**.

    ![joining network](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/joining_network.png){class="glboxshadow"}

    Sie werden zur Konfiguration des Wireless Clients weitergeleitet.

4. Suchen Sie **Interface Configuration** -> **Wireless Security**.

    ![wireless security](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security.jpg){class="glboxshadow"}

    Wählen bzw. geben Sie die korrekten Konfigurationsparameter entsprechend Ihrem Ziel-EAP-Netzwerk ein, wie unten gezeigt. **Klicken Sie noch nicht auf Save**.

    ![wireless security example](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/wireless_security_example.png){class="glboxshadow"}

5. Wechseln Sie zur Registerkarte **Advanced Settings**, geben Sie einen Schnittstellennamen wie **wlan0** an und klicken Sie dann unten rechts auf **Save**.

    ![advanced settings](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/advanced_settings.png){class="glboxshadow"}

6. Sie kehren zur Seite **Wireless** zurück, auf der ausstehende Änderungen angezeigt werden. Klicken Sie unten rechts auf **Save & Apply**.

    ![save abd apply](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/save_apply.png){class="glboxshadow"}

    Ihr Router wird nun erfolgreich mit dem gewünschten EAP-Netzwerk verbunden.

7. Verbindung überprüfen.

    ??? "Verbindung in der WebGUI prüfen"

        Sobald der Router erfolgreich mit dem gewünschten EAP-Netzwerk verbunden ist, leuchtet in der WebGUI ein Repeater-Symbol auf, wie unten dargestellt.

        ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/connected_status.png){class="glboxshadow"}

        **Hinweis**: Da die Konfiguration in LuCI nicht mit der in der WebGUI synchronisiert wird, erscheinen Details der Repeater-Schnittstelle (z. B. verbundene IP, Gateway usw.) nicht in der WebGUI.
        
        Wie im Bild zu sehen, ist der Repeater-Bereich unten leer. Der Router ist jedoch bereits als Repeater mit dem gewünschten EAP-Netzwerk verbunden, da das Repeater-Symbol oben leuchtet.

    ??? "Verbindung per SSH prüfen"

        1. Melden Sie sich per [SSH](../tutorials/ssh_log_in_to_the_router.md){target="_blank"} an Ihrem Router an.

        2. Geben Sie **ifconfig** ein und drücken Sie die Eingabetaste.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig.png){class="glboxshadow"}

            Sie können dann den Status der Schnittstelle **wlan0** prüfen.

            ![ifconfig](https://static.gl-inet.com/docs/router/en/4/tutorials/connect_to_eap_network_with_advanced_settings/ifconfig_2.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
