# So verwenden Sie VPN Cascading auf GL.iNet-Routern

## Einführung

VPN Cascading wird in manchen Zusammenhängen auch als „Double VPN“ bezeichnet, kann sich auf GL.iNet-Routern jedoch leicht unterscheiden. Das Grundprinzip ist unten dargestellt.

![gl.inet vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/mt2500_vpn-cascading.jpg){class="glboxshadow"}

**VPN 1 (Router als VPN-Server)**: Wenn der Router als VPN-Server fungiert, greifen Clients, die mit diesem Server verbunden sind, standardmäßig über das ISP-Netzwerk des Routers auf das Internet zu.

**VPN 2 (Router als VPN-Client)**: Der Router fungiert außerdem als VPN-Client und verbindet sich mit einem VPN-Dienst eines Drittanbieters.

**VPN Cascading**: Der Router leitet den Datenverkehr aus dem Tunnel von VPN 1 in den Tunnel von VPN 2 weiter. Dadurch greifen Geräte, die per VPN 1 mit dem Router verbunden sind, über den VPN-Dienst des Drittanbieters (VPN 2) statt über das ISP-Netzwerk des Routers auf das Internet zu.

## So aktivieren Sie VPN Cascading

### Für Firmware v4.7 und früher

1. Richten Sie Ihren Router zunächst als VPN-Server ein. Für höhere Geschwindigkeiten wird das WireGuard-Protokoll empfohlen. Weitere Informationen finden Sie unter [diesem Link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exportieren Sie eine Konfigurationsdatei von Ihrem Router und laden Sie sie auf ein Client-Gerät hoch, das sich per VPN mit dem Router verbinden soll.

3. Richten Sie Ihren Router als VPN-Client ein und verbinden Sie ihn mit einem VPN-Dienst eines Drittanbieters. Für höhere Geschwindigkeiten wird das WireGuard-Protokoll empfohlen. Weitere Informationen finden Sie unter [diesem Link](../interface_guide/wireguard_client.md){target="_blank"}.

4. Nach der Verbindung wird die Seite **VPN Dashboard** wie unten dargestellt angezeigt. Der Router ist dann gleichzeitig als VPN-Server und als VPN-Client eingerichtet.

    ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-vpn-dashboard.png){class="glboxshadow"}

    Wechseln Sie auf derselben Seite zum Abschnitt VPN Server und klicken Sie auf **Global Options**.

    ![global options](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.7-global-options.png){class="glboxshadow"}

    Aktivieren Sie **VPN Cascading** und klicken Sie auf **Apply**.

    ![enable vpn cascading](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/enable_vpn_cascading.png){class="glboxshadow gl-80-desktop"}

5. VPN Cascading ist nun aktiviert. Geräte, die per VPN mit Ihrem Router verbunden sind, greifen jetzt über den VPN-Dienst des Drittanbieters auf das Internet zu, statt über das ISP-Netzwerk des Routers.

### Für Firmware v4.8 und höher

1. Richten Sie Ihren Router zunächst als VPN-Server ein. Für höhere Geschwindigkeiten wird das WireGuard-Protokoll empfohlen. Weitere Informationen finden Sie unter [diesem Link](../interface_guide/wireguard_server.md){target="_blank"}.

2. Exportieren Sie eine Konfigurationsdatei von Ihrem Router und laden Sie sie auf ein Client-Gerät hoch, das sich per VPN mit dem Router verbinden soll.

3. Richten Sie Ihren Router als VPN-Client ein und verbinden Sie ihn mit einem VPN-Dienst eines Drittanbieters. Für höhere Geschwindigkeiten wird das WireGuard-Protokoll empfohlen. Weitere Informationen finden Sie unter [diesem Link](../interface_guide/wireguard_client.md){target="_blank"}.

4. Navigieren Sie im Web-Admin-Panel zu **VPN Dashboard**. Wählen Sie unten die Anweisungen aus, die zu Ihrem VPN-Modus passen.

    ??? "Global Mode"
    
        Wenn Ihr VPN-Modus **Global Mode** ist, wird VPN Cascading automatisch aktiviert, sobald der VPN-Client aktiviert ist (wie unten gezeigt).
        
        Geräte, die per VPN mit Ihrem Router verbunden sind, greifen dann über den VPN-Dienst des Drittanbieters auf das Internet zu, statt über das ISP-Netzwerk des Routers.

        ![vpn connected global mode](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-global-mode.png){class="glboxshadow"}

    ??? "Policy Mode"
    
        Wenn Ihr VPN-Modus **Policy Mode** ist, müssen Sie eine Regel für den VPN-Tunnel einrichten.
        
        Klicken Sie auf das ausgegraute Feld links.

        ![traffic from](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

        Wählen Sie die Datenverkehrsquelle aus, auf die diese Regel angewendet werden soll. Um VPN Cascading zu aktivieren, wählen Sie **All Clients**, oder wählen Sie **Specified Connection Types** und anschließend **WireGuard/OpenVPN Server**.

        ![select traffic source](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/select_traffic.jpg){class="glboxshadow"}

        - **All Clients**: Dazu gehören alle LAN-Geräte, Geräte von Drop-in Gateway, Geräte aus dem Gastnetzwerk und Geräte, die per VPN mit Ihrem Router verbunden sind.
        
            Wenn der Datenverkehr aller Geräte derselben Tunnelregel folgen soll, wählen Sie **All Clients** und klicken Sie auf **Apply**.

            ![all clients](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/all_clients.png){class="glboxshadow"}

        - **Specified Connection Types**: Damit können Sie festlegen, dass Geräte, die über eine bestimmte Methode mit dem Router verbunden sind (z. B. per VPN), dieser Tunnelregel folgen.

            Wenn die VPN-Clients Ihres Routers einer anderen Regel als andere Geräte folgen sollen, wählen Sie **WireGuard/OpenVPN Server** und klicken Sie auf **Apply**.
        
            ![specified connection](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/specified_connection_types.png){class="glboxshadow"}
            
            Dies ist ein Beispiel für VPN-Tunnelregeln im Policy Mode.
            
            ![vpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-vpn-dashboard.png){class="glboxshadow"}

5. VPN Cascading ist nun aktiviert. Geräte, die per VPN mit Ihrem Router verbunden sind, greifen jetzt über den VPN-Dienst des Drittanbieters auf das Internet zu, statt über das ISP-Netzwerk des Routers.

6. **Verbindungstest**: Öffnen Sie auf einem Laptop, der per VPN mit dem Router verbunden ist, einen Browser und rufen Sie [What Is My IP](https://whatismyipaddress.com/){target="_blank"} auf, um die öffentliche IP-Adresse zu prüfen.

    Wenn dort angezeigt wird, dass sich die IP-Adresse des Laptops in der Region des VPN-Servers des Drittanbieters befindet (in dieser Anleitung Buenos Aires), zeigt dies, dass VPN Cascading wirksam ist.

    ![vpn test](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_cascading/4.8-ipcheck.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
