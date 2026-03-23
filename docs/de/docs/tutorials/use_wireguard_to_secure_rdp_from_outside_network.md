# WireGuard verwenden, um RDP aus einem externen Netzwerk abzusichern

Möglicherweise möchten Sie von außerhalb Ihres Netzwerks auf Ihren PC zugreifen oder umgekehrt. Am sichersten ist der Zugriff über Ihren eigenen WireGuard-Tunnel. Das bietet mehr Sicherheit, als Portweiterleitung zu verwenden und über Ihre öffentliche IP-Adresse zuzugreifen. Nach dem Einrichten des Tunnels können Sie die **Remote Desktop App** von Windows verwenden, um von überall auf Ihren PC zuzugreifen.

## Topologie

![wgrdp](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/wgrdp.jpg){class="glboxshadow"}

## Eigenes WireGuard-Netzwerk einrichten

Sie müssen zunächst Ihren eigenen WireGuard-Server und WireGuard-Client einrichten, bevor Sie den WireGuard-Tunnel für RDP verwenden können. Sie können den Tunnel mit zwei GL.iNet-Routern einrichten. [Eigenen WireGuard-Heimserver mit zwei GL.iNet-Routern aufbauen](build_your_own_wireguard_home_server_with_two_glinet_routers.md).

## Dem Server Zugriff auf die Client-LAN-Seite erlauben

Wenn Sie einen gegenseitigen Zugriff von Server und Client möchten, müssen Sie Ihrem Server zunächst den Zugriff auf die Client-LAN-Seite erlauben. [Zugriff auf das Client-LAN vom Server aus](wireguard_server_access_to_client_lan_side.md).

## Dem Client Zugriff auf die Server-LAN-Seite erlauben
Aktivieren Sie danach auf den VPN Dashboards sowohl des Servers als auch des Clients die Option „Allow Remote LAN Access“. Details finden Sie hier für die Client-Seite [hier](../interface_guide/vpn_dashboard_v4.7.md/#vpn-clinet-options) und für die Server-Seite [hier](../interface_guide/vpn_dashboard_v4.7.md/#wireguard-server-options).

## Den PC auf der Serverseite erreichbar machen

### PC auf der Serverseite

Wenn Sie auf den PC zugreifen möchten, der mit der Server-LAN-Seite verbunden ist und die IP **192.168.29.123** hat, öffnen Sie bitte die Windows-Einstellungen dieses PCs und klicken Sie auf **Remote Desktop**.

![rdp1](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp1.jpg){class="glboxshadow"}

Aktivieren Sie die Funktion.

![rdp2](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp2.jpg){class="glboxshadow"}

Klicken Sie auf **Confirm**.

![rdp3](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp3.jpg){class="glboxshadow"}

## Remote-App auf dem Client-Laptop starten

### Laptop auf der Client-Seite

Suchen Sie die **Remote Desktop Connection App**.

![rdp4](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp4.jpg){class="glboxshadow"}

Starten Sie sie und geben Sie die IP des PCs auf der Serverseite **192.168.29.123** in das Feld ein.

![rdp5](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp5.jpg){class="glboxshadow"}

Geben Sie die Anmeldedaten Ihres PCs auf der Serverseite ein.

![rdp6](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_rdp/rdp6.jpg){class="glboxshadow"}

Sie steuern dann sofort Ihren PC auf der Serverseite per Fernzugriff.

Wenn Sie den Vorgang in die andere Richtung durchführen möchten, tauschen Sie einfach die Schritte für Server-PC und Client-Laptop aus.
