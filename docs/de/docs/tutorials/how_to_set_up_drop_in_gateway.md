# So richten Sie Drop-in Gateway auf einem GL.iNet-Router ein

GL.iNet bietet die Funktion Drop-in Gateway, die die Funktionalität Ihres primären Routers um Features erweitert, die er möglicherweise nicht besitzt, darunter AdGuard Home, verschlüsseltes DNS und VPN. Mit dieser Funktion können Sie Ihren primären Router wie gewohnt weiterverwenden und gleichzeitig zusätzliche Funktionen nutzen.

Sie können Drop-in Gateway für [alle Ihre Geräte](#drop-in-gateway-fur-alle-gerate-aktivieren) oder [bestimmte Geräte](#drop-in-gateway-fur-bestimmte-gerate-aktivieren) aktivieren, die mit Ihrem primären Router verbunden sind. Folgen Sie dem passenden Abschnitt für Ihre Einrichtung.

**Hinweis**: Modelle mit Firmware-Versionen unter v4.5.0 unterstützen nur die Aktivierung von Drop-in Gateway für alle Geräte. Wenn Drop-in Gateway aktiviert ist, werden alle Client-Geräte über Drop-in Gateway ins Netzwerk eingebunden. Das bedeutet, dass der gesamte Datenverkehr verbundener Clients zuerst von diesem Router verarbeitet wird.

---

## Drop-in Gateway für alle Geräte aktivieren

### 1. GL.iNet-Router mit dem Hauptrouter verbinden

Verbinden Sie den WAN-Port des GL.iNet-Routers mit einem Ethernet-Kabel mit dem LAN-Port des Hauptrouters.

### 2. Drop-in Gateway aktivieren

Es gibt zwei Methoden, um Drop-in Gateway zu aktivieren: über das Router-Admin-Panel oder über die GL.iNet Mobile App.

??? "Verwendung des Web-Admin-Panels"

    1. Geben Sie in einem Webbrowser `192.168.8.1` ein.

    2. Geben Sie Ihr Passwort ein und klicken Sie dann auf **Login**.

    3. Klicken Sie in der linken Seitenleiste auf **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Schalten Sie den Schalter neben **Enable Drop-in Gateway Mode** ein.

    5. Wählen Sie **All devices are networked through drop-in gateway**.

        ![click all devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-all-devices.jpeg){class="glboxshadow"}

    6. Klicken Sie auf **Apply**.

??? "Verwendung der GL.iNet Mobile App"

    **Hinweis:** Bevor Sie beginnen, installieren Sie die GL.iNet Mobile App auf Ihrem Gerät.

    1. Tippen Sie auf dem Hauptbildschirm der App auf die Registerkarte **System** > **Drop-in Gateway**.

        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}

    2. Tippen Sie auf **Enable**.

    3. Tippen Sie bei **Devices are networked via drop-in gateway** auf **All**.

        ![tap all](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-all.jpeg){class="glboxshadow"}

    4. Tippen Sie auf **Done**.

### 3. DHCP-Server auf dem Hauptrouter deaktivieren

Melden Sie sich bitte an Ihrem primären Router an, um den DHCP-Server zu deaktivieren. Sie können sich an den Anweisungen Ihres Routerherstellers orientieren oder dessen Support kontaktieren.

### 4. AdGuard, DNS, VPN und andere Funktionen einrichten

Befolgen Sie diese Anleitungen, um die gewünschten Funktionen auf Ihrem GL.iNet-Router zu aktivieren.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

## Drop-in Gateway für bestimmte Geräte aktivieren

### 1. GL.iNet-Router mit dem Hauptrouter verbinden

Verbinden Sie den WAN-Port des GL.iNet-Routers mit einem Ethernet-Kabel mit dem LAN-Port des Hauptrouters.

### 2. Drop-in Gateway aktivieren

Es gibt zwei Methoden, um Drop-in Gateway zu aktivieren: über das Router-Admin-Panel oder über die GL.iNet Mobile App.

??? "Verwendung des Web-Admin-Panels"

    1. Geben Sie in einem Webbrowser `192.168.8.1` ein.

    2. Geben Sie Ihr Passwort ein und klicken Sie dann auf **Login**.

    3. Klicken Sie in der linken Seitenleiste auf **Network** > **Drop-in Gateway**.

        ![click drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/click-drop-in-gateway.jpeg){class="glboxshadow"}

    4. Schalten Sie den Schalter neben **Enable Drop-in Gateway Mode** ein.
    
    5. Wählen Sie **Some devices select their own networking gateway**.

        ![click some devices](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/select-some-devices.jpeg){class="glboxshadow"}

    6. Klicken Sie auf **Apply**.

    **Hinweis:** Bitte schließen Sie diese Registerkarte **NICHT**. Sie müssen im nächsten Schritt die angezeigte IP-Adresse eingeben.

??? "Verwendung der GL.iNet Mobile App"

    **Hinweis:** Bevor Sie beginnen, installieren Sie die GL.iNet Mobile App auf Ihrem Gerät.

    1. Tippen Sie auf dem Hauptbildschirm der App auf die Registerkarte **System** > **Drop-in Gateway**.
    
        ![tap drop-in gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/tap-drop-in-gateway.jpeg){class="glboxshadow"}
    
    2. Tippen Sie auf **Enable**.
    
    3. Tippen Sie bei **Devices are networked via drop-in gateway** auf **part**.
    
        ![tap part](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_drop_in_gateway/drop-in-gateway-tap-part.jpeg){class="glboxshadow"}

    4. Tippen Sie auf **Done**.

    **Hinweis:** Bitte schließen Sie diese Registerkarte **NICHT**. Sie müssen im nächsten Schritt die angezeigte IP-Adresse eingeben.

### 3. Gateway und DNS auf einem bestimmten Gerät festlegen

??? "Windows"
    
    1. Verbinden Sie Ihr Gerät mit dem Hauptrouter.
    2. Öffnen Sie unter Windows **Settings** > **Network & Internet**.
    3. Gehen Sie je nach Verbindungsart wie folgt vor:
        * Ethernet: Klicken Sie auf **Ethernet**.
        * Wi-Fi: Klicken Sie auf **Wi-Fi** und dann auf den Namen des WLAN-Netzwerks.
    4. Kopieren Sie die IPv4-Adresse. Klicken Sie neben **IP assignment** auf **Edit**.
    5. Klicken Sie auf **Manual**.
    6. Schalten Sie **IPv4** ein.
    7. Geben Sie die folgenden Informationen ein:
        * **IP address:** Fügen Sie die IP-Adresse ein, die Sie in Schritt 4 kopiert haben.
        * **Subnet mask:** Geben Sie **255.255.255.0** ein.
        * **Gateway:** Geben Sie die IP-Adresse ein, die auf der Seite **Drop-in Gateway** angezeigt wird.
        * **Preferred DNS:** Geben Sie die IP-Adresse ein, die auf der Seite **Drop-in Gateway** angezeigt wird.
    8. Klicken Sie auf **Save**.

??? "Android"
    1. Verbinden Sie Ihr Gerät mit dem Hauptrouter.
    2. Öffnen Sie auf Ihrem Android-Gerät **Settings**.
    3. Tippen Sie auf **Connections** > **Wi-Fi**.
    4. Tippen Sie auf das Symbol **Settings** neben dem Netzwerk, mit dem Sie verbunden sind.
    5. Tippen Sie auf **View more**.
    6. Tippen Sie auf **IP settings** > **Static**.
    7. Geben Sie bei **Gateway** und **DNS 1** die IP-Adresse ein, die auf dem Bildschirm **Drop-in Gateway** angezeigt wird.
    8. Tippen Sie auf **Save**.

??? "iOS"
    1. Verbinden Sie Ihr Gerät mit dem Hauptrouter.
    2. Öffnen Sie auf Ihrem iOS-Gerät **Settings**.
    3. Tippen Sie auf **Wi-Fi**.
    4. Tippen Sie auf das WLAN-Netzwerk, mit dem Sie verbunden sind.
    5. Notieren Sie sich unter **IPv4 Address** die Werte von **IP Address** und **Subnet Mask**.
    6. Tippen Sie auf **Configure IP** > **Manual**.
    7. Geben Sie die folgenden Informationen ein:
        * **IP Address:** Geben Sie die IP Address ein, die Sie in Schritt 5 ermittelt haben.
        * **Subnet Mask:** Geben Sie die Subnet Mask ein, die Sie in Schritt 5 ermittelt haben.
        * **Router:** Geben Sie die IP-Adresse ein, die auf dem Bildschirm **Drop-in Gateway** angezeigt wird.
    8. Tippen Sie auf **Save**.
    9. Tippen Sie auf **Configure DNS** und dann auf **Manual**.
    10. Tippen Sie auf **Add Server** und geben Sie dann die IP-Adresse ein, die auf dem Bildschirm **Drop-in Gateway** angezeigt wird.
    11. Tippen Sie auf **Save**.

??? "Mac"
    1. Verbinden Sie Ihr Gerät mit dem Hauptrouter.
    2. Klicken Sie auf Ihrem Mac auf das Apple-Symbol > **System Settings**.
    3. Klicken Sie in der linken Seitenleiste auf **Network**.
    4. Klicken Sie neben dem Netzwerk, mit dem Sie verbunden sind, auf **Details**.
    5. Klicken Sie auf **TCP/IP**.
    6. Notieren Sie sich **IP Address** und **Subnet Mask**.
    7. Klicken Sie neben **Configure IPv4** auf **Manually**.
    8. Geben Sie die folgenden Informationen ein:
        * **IP address:** Geben Sie die IP Address ein, die Sie in Schritt 6 ermittelt haben.
        * **Subnet mask:** Geben Sie die Subnet Mask ein, die Sie in Schritt 6 ermittelt haben.
        * **Router:** Geben Sie die IP-Adresse ein, die auf der Seite **Drop-in Gateway** angezeigt wird.
    9. Klicken Sie auf **OK** > **OK**.

### 4. AdGuard, DNS, VPN und andere Funktionen einrichten

Befolgen Sie diese Anleitungen, um die gewünschten Funktionen auf Ihrem GL.iNet-Router zu aktivieren.

* [AdGuard Home](../interface_guide/adguardhome.md){target="_blank"}
* [Encrypted DNS](../interface_guide/dns.md){target="_blank"}
* [Parental Control](../interface_guide/parental_control.md){target="_blank"}
* [WireGuard Client](../interface_guide/wireguard_client.md){target="_blank"}
* [OpenVPN Client](../interface_guide/openvpn_client.md){target="_blank"}

---

Verwandter Artikel:

- [Drop-in Gateway](../interface_guide/drop-in_gateway.md)

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
