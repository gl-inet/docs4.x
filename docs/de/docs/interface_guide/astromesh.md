# AstroMesh

> Diese Funktion wurde mit Firmware v4.10 eingeführt.

AstroMesh ist GL.iNets proprietäre globale Mesh-Technologie und kombiniert EasyMesh mit AstroWarp. Im Gegensatz zu herkömmlichen WLAN-Mesh-Systemen, die nur in einem lokalen Netzwerk funktionieren, kann AstroMesh geografische Grenzen überbrücken und Sie auch unterwegs mit Ihrem Heimnetzwerk verbinden.

Zu Hause arbeitet Ihr Reiserouter als normaler Mesh Node und erweitert die WLAN-Abdeckung mit nahtlosem Roaming. Unterwegs kann er automatisch in den Astro Node-Modus wechseln und die WLAN-Einstellungen Ihres Heimnetzwerks über die Cloud synchronisieren. So können Sie aus der Ferne auf Geräte im Heim-LAN zugreifen und den Datenverkehr über den Heimnetzwerk-Ausgang leiten. Plug-and-play ohne komplizierte Konfiguration: AstroMesh bietet ein nahtloses Interneterlebnis, egal ob Sie zu Hause entspannen oder unterwegs sind.

## Schnelle Einrichtung

Im folgenden Beispiel verwenden wir Flint 3 (GL-BE9300) und Slate 7 (GL-BE3600), um ein AstroMesh-Netzwerk aufzubauen.

- **Flint 3**: dient als Main Router, verbindet sich mit dem Internet, verwaltet alle Mesh Nodes und stellt den Netzwerk-Ausgang für alle entfernten Astro Nodes bereit.
- **Slate 7**: dient als Mesh Node, der die WLAN-Abdeckung des Main Routers lokal per EasyMesh erweitert oder das Heimnetzwerk über AstroWarp an entfernte Standorte bringt.

Führen Sie die folgenden Schritte aus.

1. Melden Sie sich am Web Admin Panel von Flint 3 an und gehen Sie zu **INTERNET**. Verbinden Sie ihn über eine unterstützte Verbindungsart mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

2. Gehen Sie zu **ASTROMESH** und klicken Sie auf **Main Router**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Fügen Sie Nodes über **Wi-Fi Scan** oder **Pairing Code** hinzu.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

    Befolgen Sie die passenden Anweisungen unten.

    ??? note "Wi-Fi Scan"

        Stellen Sie vor dem Scan sicher, dass:

        1. Der hinzuzufügende Router eingeschaltet ist und sich in der Nähe des Main Routers befindet.
        2. AstroMesh auf dem hinzuzufügenden Router aktiviert ist und dieser im Modus **Mesh Node** arbeitet.
        ---

        Klicken Sie auf **Add nodes via Wi-Fi Scan**.

        ![add nodes wifi scan](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_wifiscan.png){class="glboxshadow"}

        Klicken Sie im Pop-up-Fenster auf **Scan**.

        ![wifi scan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan1.png){class="glboxshadow"}

        Der Scan nach nahegelegenen Mesh Nodes über WLAN beginnt.

        ![wifi scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scanning.png){class="glboxshadow"}

        Wählen Sie einen Node aus und klicken Sie auf **Add**.

        ![wifi scan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan2.jpg){class="glboxshadow"}

        Der Mesh Node wird dem AstroMesh-Netzwerk hinzugefügt. Klicken Sie auf **Finish**.

        ![wifi scan added](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/wifi_scan_added.png){class="glboxshadow"}

        **Hinweis**: Sobald ein Node dem AstroMesh-Netzwerk beitritt, ist er nicht mehr über seine ursprüngliche IP-Adresse erreichbar. Alle Nodes können über das Admin Panel des Main Routers verwaltet werden. Details finden Sie unter [Mesh Nodes verwalten](#manage-mesh-nodes).

    ??? note "Pairing Code"

        Klicken Sie auf **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Der Main Router erzeugt einen Pairing Code. Kopieren Sie diesen Code.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Melden Sie sich am Web Admin Panel von Slate 7 an, gehen Sie zu **ASTROMESH** und klicken Sie auf **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Geben Sie den kopierten Pairing Code ein und klicken Sie auf **Apply**. *Der Pairing Code ist zeitlich begrenzt. Geben Sie ihn ein, bevor er abläuft.*

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Der Mesh Node beginnt, sich mit dem Main Router zu verbinden. Klicken Sie auf **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Hinweis**: Sobald ein Node dem AstroMesh-Netzwerk beitritt, ist er nicht mehr über seine ursprüngliche IP-Adresse erreichbar. Alle Nodes können über das Admin Panel des Main Routers verwaltet werden. Details finden Sie unter [Mesh Nodes verwalten](#manage-mesh-nodes).

4. Nachdem Nodes erfolgreich zu AstroMesh hinzugefügt wurden, erscheint im Admin Panel des Main Routers die folgende Topologie.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

## Mesh Nodes verwalten {#manage-mesh-nodes}

Verwalten Sie Ihre Mesh Nodes im Admin Panel des Main Routers.

### Node-Informationen anzeigen

Gehen Sie im Admin Panel des Main Routers zu **ASTROMESH** und klicken Sie in der AstroMesh-Topologie auf **Main Router**.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Sie können Details zum Main Router anzeigen, einschließlich Modell, IP- und MAC-Adresse, Betriebszeit und verbundenen Clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Sie können Details zum Mesh Node anzeigen, einschließlich Modell, IP- und MAC-Adresse, Firmware-Version, Betriebszeit und verbundenen Clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh Node bearbeiten

Gehen Sie im Admin Panel des Main Routers zu **ASTROMESH** und klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Jeder Mesh Node wird standardmäßig als "Node" plus die letzten vier Stellen seiner MAC-Adresse benannt. Klicken Sie auf das Bearbeiten-Symbol, um den Mesh Node umzubenennen.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Auf Mesh Node zugreifen

Gehen Sie im Admin Panel des Main Routers zu **ASTROMESH** und klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Klicken Sie oben rechts auf das Zahnrad-Symbol und wählen Sie **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Sie werden zur Anmeldeseite des Mesh Node unter der vom Main Router zugewiesenen IP-Adresse weitergeleitet. Geben Sie Ihr Admin-Passwort ein, um sich anzumelden.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

Gehen Sie nach der Anmeldung zu **ASTROMESH**, um den Verbindungsstatus anzuzeigen.

![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

### Weitere Nodes hinzufügen

Um weitere Nodes hinzuzufügen, klicken Sie oben rechts in der AstroMesh-Topologie auf **Add**.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_more_nodes.png){class="glboxshadow"}

## Astro Nodes verwalten

Wenn Sie einen Mesh Node aus Ihrem Heimnetzwerk entfernen, wechselt er automatisch in den Modus **Astro Node**.

Nehmen Sie zum Beispiel den Slate 7 an einen anderen Standort mit. Schalten Sie ihn ein und wählen Sie auf dem Touchscreen den Modus **Mesh Node** aus.

![select mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/select_mode.png){class="glboxshadow" width="360"}

Er erkennt die aktuelle Netzwerkumgebung, wechselt automatisch in den Modus **Astro Node** und startet die Verbindung.

![astro node connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connecting.png){class="glboxshadow" width="360"}

Nach erfolgreicher Verbindung zeigt er seine ursprüngliche IP-Adresse an. Diese kann für den Zugriff auf sein Web Admin Panel verwendet werden.

![astro node connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/be3600/astro_node_connected.png){class="glboxshadow" width="360"}

Verwenden Sie diese IP-Adresse, um sich bei Ihrem Astro Node anzumelden.

![astro node admin](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_admin.png){class="glboxshadow"}

Gehen Sie nach der Anmeldung zu **ASTROMESH**, um den Verbindungsstatus anzuzeigen. Der Standard-Verbindungsmodus ist **Exit Node Mode**. Sie können bei Bedarf zu **Traffic Split Mode** wechseln.

![astro node exit](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/astro_node_exit.png){class="glboxshadow"}

- **Exit Node Mode**: In diesem Modus wird der gesamte Datenverkehr des Astro Node über Ihr Heimnetzwerk ins Internet geleitet. Die öffentliche IP-Adresse des Astro Node entspricht der öffentlichen IP-Adresse Ihres Heimnetzwerks.

- **Traffic Split Mode**: In diesem Modus wird nur Datenverkehr zu Ihrem Heimnetzwerk zurück an den Main Router weitergeleitet, während anderer Internetverkehr direkt über das lokale WAN des Astro Node läuft. Stellen Sie sicher, dass der Astro Node mit einem lokalen Internetnetzwerk verbunden ist.

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
