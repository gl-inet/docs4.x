# Wie leitet man DNS-Anfragen eines VPN-Clients an den Upstream-DNS des VPN-Servers weiter?

Dieses Tutorial beschreibt die Schritte, um alle DNS-Anfragen von VPN-Clients an Ihren selbst gehosteten DNS-Server im LAN Ihres primären Routers weiterzuleiten, der sich vorgelagert zum VPN-Server befindet.

## Topologie

In diesem Tutorial verwenden wir **Flint 3 (GL-BE9300)** und **Slate 7 (GL-BE3600)** als Beispiele.

Flint 3 ist der VPN-Server, dessen Upstream-Netzwerk über einen primären Router verfügt, und Slate 7 ist der VPN-Client, der sich mit Flint 3 verbindet.

Wenn zwischen VPN-Server und Client ein VPN-Tunnel aufgebaut wird, werden die DNS-Anfragen des VPN-Clients standardmäßig zunächst an den VPN-Server gesendet, dann an den primären Router weitergeleitet und schließlich von den vom ISP zugewiesenen DNS-Servern aufgelöst, die auf dem WAN des primären Routers konfiguriert sind.

![topology 1](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-1.jpg){class="glboxshadow"}

Wenn Sie jedoch auf dem primären Router einen selbst gehosteten DNS-Server (IP-Adresse `192.168.1.13`) eingerichtet haben, sind zusätzliche Konfigurationen erforderlich, damit DNS-Anfragen an diesen DNS-Server weitergeleitet werden.

![topology 2](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/topology-2.jpg){class="glboxshadow"}

## Einrichtung

1. Melden Sie sich am webbasierten Admin Panel von Flint 3 an und navigieren Sie zu **NETWORK** -> **DNS**. Stellen Sie den DNS Server Mode auf **Manual DNS** und geben Sie die IP-Adresse Ihres DNS-Servers ein.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/manual_dns.png){class="glboxshadow"}

2. Navigieren Sie zu **VPN** -> **WireGuard Server** -> Registerkarte **Configuration** und notieren Sie sich die IPv4-Adresse. Diese ist je nach Modell und Firmware-Version in der Regel `10.0.0.1/24` oder `10.1.0.1/24`.

    ![server ip](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_ip.png){class="glboxshadow"}

3. Wechseln Sie zur Registerkarte **Profiles**, fügen Sie eine Client-Konfiguration hinzu und exportieren Sie ein Profil für Slate 7.

    ![add profile](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/add_profile.png){class="glboxshadow"}

4. Öffnen Sie das Profil und stellen Sie sicher, dass als DNS die in Schritt 2 ermittelte IP-Adresse des VPN-Servers eingetragen ist.

    Um DNS-Auflösungsfehler zu vermeiden, löschen Sie gegebenenfalls `64.6.64.6` und speichern Sie die Änderungen.

    ![edit config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/edit_config.png){class="glboxshadow"}

5. Klicken Sie im webbasierten Admin Panel von Flint 3 oben auf der Seite **WireGuard Server** auf die Schaltfläche **Start**, um den Server zu starten.

    ![start server](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_server.png){class="glboxshadow"}

6. Melden Sie sich am webbasierten Admin Panel von Slate 7 an und navigieren Sie zu **VPN** -> **WireGuard Client**.

    Klicken Sie auf **Add Manually** und laden Sie das bearbeitete Profil hoch.

    ![upload config](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/upload_config.png){class="glboxshadow"}

7. Klicken Sie auf das Drei-Punkte-Symbol, um die VPN-Verbindung zu starten. Wenn die Statusanzeige grün wird, wurde die VPN-Verbindung erfolgreich aufgebaut.

    ![start client](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/start_client.png){class="glboxshadow"}

## DNS-Auflösung überprüfen

Führen Sie den folgenden Befehl aus, um den DNS-Datenverkehr auf dem VPN-Client mitzuschneiden. Dadurch wird angezeigt, dass der gesamte DNS-Datenverkehr des VPN-Clients an den VPN-Server geht (in diesem Beispiel `10.0.0.1`).

![client dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/client_dns_traffic.png){class="glboxshadow"}

Führen Sie den folgenden Befehl aus, um den DNS-Datenverkehr auf dem VPN-Server mitzuschneiden. Dadurch wird angezeigt, dass der gesamte DNS-Datenverkehr des VPN-Clients letztlich an den selbst gehosteten DNS-Server geht (in diesem Beispiel `192.168.1.13`).

![server dns traffic](https://static.gl-inet.com/docs/router/en/4/tutorials/route_vpn_dns_to_server_upstream_dns/server_dns_traffic.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.











