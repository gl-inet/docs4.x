# Wie greife ich aus der Ferne auf das Web-Admin-Panel eines GL.iNet-Routers zu?

Die folgende Methode erfordert eine Vorkonfiguration, während Sie sich noch physisch in der Nähe des Routers befinden.

## Methode 1. GoodCloud

[GL.iNet GoodCloud](https://www.goodcloud.xyz){target="_blank"} ist eine Plattform, die die Remote-Bereitstellung und Verwaltung verbundener Geräte vereinfacht. Sie bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten. Binden Sie Ihren GL.iNet-Router einfach an GoodCloud. Danach können Sie jederzeit und überall aus der Ferne auf das Web-Admin-Panel des Routers zugreifen.

Weitere Informationen finden Sie in [dieser Anleitung](../interface_guide/cloud.md){target="_blank"}.

## Methode 2. VPN

Wenn Ihr Router eine **öffentliche IP-Adresse** hat, können Sie über einen VPN-Tunnel aus der Ferne auf sein Web-Admin-Panel zugreifen. Beachten Sie, dass diese Methode erweiterte Konfigurationen erfordert und zusätzliche Einrichtungszeit benötigt.

1. Stellen Sie sicher, dass Ihr Router eine öffentliche IP-Adresse hat. [Wie kann ich prüfen, ob ich eine öffentliche IP-Adresse habe?](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md){target="_blank"}

2. Richten Sie Ihren Router als WireGuard Server ein. Details finden Sie [hier](../interface_guide/wireguard_server.md){target="_blank"}.

3. Exportieren Sie eine Konfigurationsdatei von Ihrem WireGuard Server zur späteren Verwendung.

4. Öffnen Sie im Web-Admin-Panel des Routers **VPN** -> **WireGuard Server** und klicken Sie oben rechts auf **Options**. Aktivieren Sie **Allow Remote Access to the LAN Subnet** und klicken Sie dann auf **Apply**.

5. Richten Sie das Gerät, von dem aus Sie per Fernzugriff auf Ihren Router zugreifen möchten, als WireGuard Client ein, indem Sie die Konfigurationsdatei manuell importieren.

    - Wenn Ihr WireGuard Client ein Endgerät wie ein Smartphone oder Laptop ist, [installieren Sie die WireGuard App](https://www.wireguard.com/install){target="_blank"} und importieren Sie anschließend die Datei, um eine Verbindung zu starten.

    - Wenn Ihr WireGuard Client ein anderer GL.iNet-Router ist, z. B. ein GL.iNet-Reiserouter, lesen Sie [diese Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers){target="_blank"}, um die Konfigurationsdatei zu importieren und eine Verbindung zu starten.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
