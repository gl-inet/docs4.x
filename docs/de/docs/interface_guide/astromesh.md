# AstroMesh

> Diese Funktion wurde mit Firmware v4.10 eingeführt.

AstroMesh ist GL.iNets proprietäre globale Mesh-Technologie und kombiniert EasyMesh mit AstroWarp. Im Gegensatz zu herkömmlichen WLAN-Mesh-Systemen, die nur in einem lokalen Netzwerk funktionieren, kann AstroMesh geografische Grenzen überbrücken und Sie auch unterwegs mit Ihrem Heimnetzwerk verbinden.

Zu Hause arbeitet Ihr Reiserouter als normaler Mesh Node und erweitert die WLAN-Abdeckung mit nahtlosem Roaming. Unterwegs kann er automatisch in den Astro Node-Modus wechseln und die WLAN-Einstellungen Ihres Heimnetzwerks über die Cloud synchronisieren. So können Sie aus der Ferne auf Geräte im Heim-LAN zugreifen und den Datenverkehr über den Heimnetzwerk-Ausgang leiten. Plug-and-play ohne komplizierte Konfiguration: AstroMesh bietet ein nahtloses Interneterlebnis, egal ob Sie zu Hause entspannen oder unterwegs sind.

## Schnelle Einrichtung

Im folgenden Beispiel verwenden wir Flint 3 (GL-BE9300) und Slate 7 (GL-BE3600), um ein AstroMesh-Netzwerk aufzubauen.

- **Flint 3**: dient als Main Node, verbindet sich mit dem Internet, verwaltet alle Mesh Nodes und stellt den Netzwerk-Ausgang für entfernte Astro Nodes bereit.
- **Slate 7**: dient als Mesh Node, der die WLAN-Abdeckung des Main Node lokal per EasyMesh erweitert oder das Heimnetzwerk über AstroWarp an entfernte Standorte bringt.

Führen Sie die folgenden Schritte aus.

1. Melden Sie sich am Web Admin Panel von Flint 3 an und gehen Sie zu **INTERNET**. Verbinden Sie ihn über eine unterstützte Verbindungsart mit dem Internet: Ethernet, Repeater, Tethering oder Cellular.

2. Gehen Sie zu **ASTROMESH** und klicken Sie auf **Main Node**.

    ![main node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node.png){class="glboxshadow"}

3. Fügen Sie Nodes über **Wi-Fi Scan** oder **Pairing Code** hinzu.

    ![main add node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_add_nodes.png){class="glboxshadow"}

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

        **Hinweis**: Sobald dieser Mesh Node verbunden ist, ist er nicht mehr über seine ursprüngliche IP-Adresse erreichbar. Verwenden Sie danach die neue IP-Adresse, die er vom Main Node erhält. Verwalten Sie alle Nodes im Admin Panel des Main Node. Details finden Sie [hier](#manage-nodes).

    ??? note "Pairing Code"

        Klicken Sie auf **Add nodes via Pairing Code**.

        ![add nodes pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/add_nodes_pairing.png){class="glboxshadow"}

        Der Main Node erzeugt einen Pairing Code. Kopieren Sie diesen Code.

        ![pairing code mesh mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/pairing_code_mesh.png){class="glboxshadow"}

        Melden Sie sich am Web Admin Panel von Slate 7 an, gehen Sie zu **AstroMesh** und klicken Sie auf **Mesh/Astro Node**.

        ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/sub_node.png){class="glboxshadow"}

        Geben Sie den kopierten Pairing Code ein und klicken Sie auf **Apply**.

        ![enter pairing code](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/enter_pairing_code.png){class="glboxshadow"}

        Der Mesh Node beginnt, sich mit dem Main Node zu verbinden. Klicken Sie auf **Done**.

        ![mesh node pairing](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_pairing.png){class="glboxshadow"}

        **Hinweis**: Sobald dieser Mesh Node verbunden ist, ist er nicht mehr über seine ursprüngliche IP-Adresse erreichbar. Verwenden Sie danach die neue IP-Adresse, die er vom Main Node erhält. Verwalten Sie alle Nodes im Admin Panel des Main Node. Details finden Sie [hier](#manage-nodes).

4. Nachdem der Node dem AstroMesh-Netzwerk hinzugefügt wurde, zeigt das Admin Panel des Main Node die Netzwerktopologie an.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_topology.png){class="glboxshadow"}

    Auch das Admin Panel des Mesh Node zeigt den Verbindungsstatus an.

    ![mesh node status](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_status.png){class="glboxshadow"}

    **Hinweis**: Nach dem Hinzufügen zum AstroMesh-Netzwerk ist der Mesh Node nicht mehr über seine ursprüngliche IP-Adresse erreichbar. Verwenden Sie die neue IP-Adresse vom Main Node und verwalten Sie alle Nodes im Admin Panel des Main Node. Details finden Sie [hier](#manage-nodes).

5. Wenn Sie den Mesh Node von zu Hause mitnehmen, wechselt er automatisch in den Astro Node-Modus.

## Nodes verwalten {#manage-nodes}

Verwalten Sie Ihr AstroMesh-Netzwerk im Admin Panel des Main Node.

### Node-Informationen anzeigen

Klicken Sie in der AstroMesh-Topologie auf **Main Node**.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info1.png){class="glboxshadow"}

Sie können Details zum Main Node anzeigen, einschließlich Modell, IP- und MAC-Adresse, Betriebszeit und verbundenen Clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/main_node_info2.png){class="glboxshadow"}

Klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Sie können Details zum Mesh Node anzeigen, einschließlich Modell, IP- und MAC-Adresse, Firmware-Version, Betriebszeit und verbundenen Clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh Node bearbeiten

Klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Jeder Mesh Node wird standardmäßig als "Node" plus die letzten vier Stellen seiner MAC-Adresse benannt. Klicken Sie auf das Bearbeiten-Symbol, um den Mesh Node umzubenennen.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node2.png){class="glboxshadow"}

### Auf Mesh Node zugreifen

Klicken Sie in der AstroMesh-Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_info1.png){class="glboxshadow"}

Klicken Sie oben rechts auf das Zahnrad-Symbol und wählen Sie **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/node_actions.png){class="glboxshadow"}

Sie werden zur Anmeldeseite des Mesh Node weitergeleitet. Geben Sie das Admin-Passwort ein, um über die vom Main Node zugewiesene IP-Adresse auf das Admin Panel zuzugreifen.

![mesh admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/mesh_node_admin.png){class="glboxshadow"}

---

Sie haben noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
