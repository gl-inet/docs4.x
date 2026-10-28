# RDP aus einem externen Netzwerk mit WireGuard absichern {#securing-rdp-from-an-external-network-with-wireguard}

Möglicherweise möchten Sie von außerhalb Ihres Netzwerks auf Ihren PC zugreifen oder umgekehrt. Ein sicherer Ansatz ist der Zugriff über Ihren eigenen WireGuard-Tunnel. Das bietet mehr Sicherheit, als Portweiterleitung zu verwenden und über Ihre öffentliche IP-Adresse direkt auf den PC zuzugreifen. Nach dem Einrichten des Tunnels können Sie **Windows Remote Desktop** verwenden, um von überall auf Ihren PC zuzugreifen.

Dieses Tutorial zeigt am Beispiel von zwei GL.iNet-Routern, wie Sie Windows RDP über ein WireGuard-Netzwerk absichern.

## Topologie {#topology}

![wgrdp](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Einrichtungsschritte {#setup-steps}

1. Richten Sie Ihr WireGuard-Netzwerk ein.

    Richten Sie zunächst Ihren eigenen WireGuard-Server und WireGuard-Client mit zwei GL.iNet-Routern ein. Siehe [Eigenen WireGuard-Server mit zwei GL.iNet-Routern aufbauen](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

2. Erlauben Sie Ihrem WireGuard-Server den Zugriff auf das Client-LAN.

    Um gegenseitigen Zugriff zwischen Server und Client zu ermöglichen, erlauben Sie zunächst dem Server den Zugriff auf das Client-LAN. Siehe [Zugriff auf das WireGuard-Client-LAN vom Server aus](wireguard_server_access_to_client_lan_side.md).

    Die Schritte können je nach Firmware-Version abweichen.

3. Erlauben Sie Ihrem WireGuard-Client den Zugriff auf das Server-LAN.

    Dieser Schritt kann je nach Firmware-Version abweichen. Wählen Sie unten die Firmware-Version des Routers aus, den Sie als WireGuard-Client eingerichtet haben.

    ??? note "Für Firmware v4.7 und früher"

        Melden Sie sich bei Ihrem WireGuard-Client an und gehen Sie zu **VPN** -> **VPN Dashboard**. Suchen Sie **VPN Server** und klicken Sie rechts auf das Zahnradsymbol.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1.png){class="glboxshadow"}

        Aktivieren Sie im Pop-up-Fenster **Remote Access LAN** und klicken Sie auf **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2.png){class="glboxshadow"}

    ??? note "Für Firmware v4.8 und höher"

        Melden Sie sich bei Ihrem WireGuard-Client an und gehen Sie zu **VPN** -> **WireGuard Server**. Klicken Sie oben rechts auf **Options**.

        ![wgserver options1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options1_v4.8.png){class="glboxshadow"}

        Aktivieren Sie im Pop-up-Fenster **Allow Remote Access to the LAN Subnet** und klicken Sie auf **Apply**.

        ![wgserver options2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgserver_options2_v4.8.png){class="glboxshadow"}

4. Verbinden Sie den Computer, auf den zugegriffen werden soll, mit dem VPN-Server und ermitteln Sie seine LAN-IP-Adresse.

    Im folgenden Beispiel lautet die IP-Adresse des PCs auf der Serverseite **192.168.29.123**.

5. Machen Sie den PC auf der Serverseite erreichbar.

    Öffnen Sie auf dem PC auf der Serverseite **System Settings** und klicken Sie auf **Remote Desktop**.

    ![rdp1](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

    Aktivieren Sie **Remote Desktop** und klicken Sie auf **Confirm**.

    ![rdp2](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

    ![rdp3](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

6. Greifen Sie vom Laptop auf der Client-Seite aus zu.

    Suchen Sie in der Suchleiste nach **Remote Desktop Connection**.

    ![rdp4](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

    Starten Sie die App und geben Sie die IP-Adresse des PCs auf der Serverseite ein, z. B. **192.168.29.123**.

    ![rdp5](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

    Geben Sie die Anmeldedaten des PCs auf der Serverseite ein, um die Verbindung herzustellen.

    ![rdp6](https://static.gl-inet.com/docs/router/de/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

    Sie können den PC auf der Serverseite nun per Fernzugriff steuern.

    Wenn Sie den Vorgang in die andere Richtung durchführen möchten, tauschen Sie einfach die Schritte für Server-PC und Client-Laptop aus.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
