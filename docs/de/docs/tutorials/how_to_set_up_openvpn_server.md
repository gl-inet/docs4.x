# So richten Sie einen OpenVPN-Server auf GL.iNet-Routern ein

In diesem Tutorial erfahren Sie, wie Sie einen OpenVPN-Server auf GL.iNet-Routern einrichten. Mit einem VPN-Server können Sie aus der Ferne eine sichere Verbindung zu Ihrem Heim- oder Büronetzwerk herstellen. Mit einem GL.iNet-Router ist ein OpenVPN-Server in wenigen Minuten eingerichtet.

!!! note "Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Voraussetzungen erfüllen"
    
    **Öffentliche IP-Adresse**

    Zum Einrichten eines OpenVPN-Servers ist eine öffentliche IP-Adresse erforderlich. Unter [diesem Link](https://docs.gl-inet.com/router/en/4/tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address/) erfahren Sie, wie Sie prüfen können, ob Sie eine besitzen.

    **Portweiterleitung**

    Wenn Ihr GL.iNet-Router hinter einem primären Router verbunden ist, [richten Sie auf dem primären Router eine Portweiterleitung ein](https://docs.gl-inet.com/router/en/4/tutorials/how_to_set_up_port_forwarding/).

## 1. Am Router anmelden

Öffnen Sie einen Webbrowser und rufen Sie das Web-Admin-Panel des Routers auf (Standard-IP: 192.168.8.1). Melden Sie sich mit Ihrem Admin-Passwort an.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/router-login.jpeg){class="glboxshadow"}

## 2. Dynamic DNS aktivieren (optional)

Zum Einrichten eines OpenVPN-Servers wird in der Regel eine **statische öffentliche IP-Adresse** benötigt, die einen festen Endpunkt für andere Geräte bereitstellt, um auf Ihren VPN-Server zuzugreifen.

Wenn Sie jedoch keine statische öffentliche IP-Adresse haben, sondern stattdessen eine dynamische, sollten Sie auf Ihrem GL.iNet-Router **Dynamic DNS (DDNS)** aktivieren. Dadurch bleibt die Verbindung zum OpenVPN-Server auch dann bestehen, wenn sich Ihre öffentliche IP-Adresse dynamisch ändert.

Führen Sie die folgenden Schritte aus, um Dynamic DNS zu aktivieren.

1. Gehen Sie im Web-Admin-Panel des Routers zu **APPLICATIONS** > **Dynamic DNS**.
![dynamic DNS](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-dynamic-dns.jpeg){class="glboxshadow"}
2. Aktivieren Sie **Enable DDNS**, lesen Sie die **Terms of Service & Privacy Policy** und stimmen Sie ihnen zu. Klicken Sie dann auf **Apply**.
![apply](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/dynamic-dns-click-apply.png){class="glboxshadow"}

## 3. Konfigurationsdatei herunterladen

1. Gehen Sie im Web-Admin-Panel des Routers zu **VPN** > **OpenVPN Server**.
2. Klicken Sie auf **Generate Configuration**.
3. Behalten Sie die Standardeinstellungen bei und klicken Sie dann auf **Export Client Configuration**.
![click export](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-export-client-configuration.jpeg){class="glboxshadow"}
4. Aktivieren Sie im Pop-up-Fenster **Use DDNS Domain**, wenn Sie zuvor **Dynamic DNS** eingerichtet haben.
5. Klicken Sie auf **Download** und speichern Sie anschließend die Datei.
6. Klicken Sie oben auf der Seite **OpenVPN Server** auf **Start**.
![click start](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/openvpn-server-click-start.jpeg){class="glboxshadow"}

??? "(Optional) Aktivieren Sie diese Einstellungen, um auf das lokale Netzwerk des VPN-Servers zuzugreifen:"
    
    Für Firmware v4.7 und früher:

    1. Klicken Sie in der linken Seitenleiste auf **VPN** > **VPN Dashboard**.
    2. Klicken Sie auf das Optionssymbol.
    3. Aktivieren Sie **Remote Access LAN**.
    4. Klicken Sie auf **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/toggle-enable-remote-access-lan.png){class="glboxshadow"}

    Für Firmware v4.8 und höher:

    1. Klicken Sie in der linken Seitenleiste auf **VPN** > **OpenVPN Server**.
    2. Klicken Sie oben rechts auf **Options**.
    3. Aktivieren Sie **Allow Remote Access the LAN Subnet**.
    4. Klicken Sie auf **Apply**.

        ![remote access lan](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/enable-remote-access-lan-4.8.png){class="glboxshadow"}


## 4. Mit dem OpenVPN-Server verbinden

Um eine Verbindung mit dem OpenVPN-Server herzustellen, benötigen Sie einen OpenVPN-Client. Dafür können Sie eine der folgenden Methoden verwenden:

??? "Methode 1: Eine OpenVPN-Client-App eines Drittanbieters (verwenden Sie diese Methode, wenn Sie keinen zusätzlichen Router haben, der die Einrichtung eines OpenVPN-Clients unterstützt)"

    In diesem Tutorial verwenden wir als Beispiel die App OpenVPN Connect, die offizielle App von OpenVPN Inc.

    1. Verbinden Sie ein anderes Gerät mit einem anderen WLAN-Netzwerk (oder mit dem Mobilfunknetz, wenn Sie ein mobiles Gerät verwenden).
    2. Senden Sie die zuvor heruntergeladene Konfigurationsdatei an dieses Gerät (z. B. per E-Mail) und laden Sie die Datei dort herunter.
    3. Laden Sie OpenVPN Connect für das Betriebssystem Ihres Geräts herunter:
        * [Windows](https://openvpn.net/client/client-connect-vpn-for-windows/)
        * [Mac](https://openvpn.net/client/client-connect-vpn-for-mac-os/)
        * [Android](https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US&pli=1)
        * [iOS](https://apps.apple.com/us/app/openvpn-connect-openvpn-app/id590379981)
        * [Linux](https://openvpn.net/openvpn-client-for-linux/)
    4. Lesen Sie in der App die Nutzungsbedingungen und wählen Sie dann **Agree**.
    5. Wählen Sie **Upload File**.
    ![upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-upload-file.png){class="glboxshadow"}
    6. Wählen Sie **Browse** und anschließend die zuvor heruntergeladene Konfigurationsdatei aus.
    7. Wählen Sie **OK**.
        ![tap ok](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/tap-ok.png){class="glboxshadow"}
    8. Wählen Sie **Connect** > **OK** > **Allow**.

    Oben im VPN-Profil wird dann der Status „Connected“ angezeigt.
    ![connected status](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/connected-status.png){class="glboxshadow"}

??? "Methode 2: Ein Router, der die Einrichtung eines OpenVPN-Clients unterstützt"

    Sie können jeden Router verwenden, der die manuelle Konfiguration eines OpenVPN-Clients unterstützt. In diesem Tutorial verwenden wir als Beispiel den GL.iNet-Reiserouter [Beryl AX (GL-MT3000)](https://www.gl-inet.com/products/gl-mt3000/).

    1. Verbinden Sie ein anderes Gerät mit einem anderen WLAN-Netzwerk (oder mit dem Mobilfunknetz, wenn Sie ein mobiles Gerät verwenden).
    2. Geben Sie in die Adresszeile eines Webbrowsers die URL zum Admin-Panel Ihres Routers ein (z. B. 192.168.8.1).
    3. Geben Sie Ihr Passwort ein und klicken Sie dann auf **Login**.
    4. Klicken Sie in der linken Seitenleiste auf **VPN** > **OpenVPN Client**.
    ![click openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-openvpn-client.png){class="glboxshadow"}
    5. Klicken Sie auf **Add Manually**.
    ![click add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-add-manually.png){class="glboxshadow"}
    6. Geben Sie im Feld einen Namen ein und klicken Sie dann auf das Häkchensymbol.
    7. Laden Sie die zuvor heruntergeladene Konfigurationsdatei hoch.
    ![select a file](https://static.gl-inet.com/docs/router/en/4/tutorials/build_your_own_openvpn_server/click-select-a-file.png){class="glboxshadow"}
    8. Klicken Sie auf **Apply**.
    9. Klicken Sie auf das Symbol mit den drei Punkten und anschließend auf **Start**.
    10. Verbinden Sie ein Gerät mit dem Router, auf dem der OpenVPN-Client ausgeführt wird.

## 5. VPN-Verbindung überprüfen

Öffnen Sie einen Webbrowser und suchen Sie nach Ihrer IP-Adresse und Ihrem Standort. Wenn beide mit der IP des VPN-Servers (und nicht mit der IP Ihres Internetdienstanbieters) sowie dessen Standort übereinstimmen, wurde die VPN-Verbindung erfolgreich hergestellt.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
