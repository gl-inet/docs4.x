# Mesh

**Hinweis**: Diese Funktion wurde mit Firmware v4.10 eingeführt.

---

Navigieren Sie auf der linken Seite des webbasierten Admin Panels zu **MESH**.

Mesh ist eine auf dem Wi-Fi EasyMesh™-Standard basierende Funktion, die die WLAN-Abdeckung im gesamten Zuhause erweitert und nahtloses Roaming ermöglicht. Wenn Sie mehrere GL.iNet-Router besitzen, legen Sie einen davon als Hauptrouter und die übrigen als Mesh-Knoten fest. Dadurch können Sie sich in Ihrem Zuhause bewegen, ohne die WLAN-Verbindung wechseln zu müssen.

Im folgenden Beispiel wird mit Flint 3 (GL‑BE9300) und Slate 7 (GL‑BE3600) ein Mesh-Netzwerk eingerichtet.

- **Flint 3** ist der Hauptrouter, der die Verbindung zum Internet herstellt und alle Mesh-Knoten verwaltet.

- **Slate 7** ist der Mesh-Knoten, der die WLAN-Abdeckung des Hauptrouters erweitert.

## Schnelleinrichtung

1. Schalten Sie den Mesh-Knoten ein und stellen Sie ihn in der Nähe des Hauptrouters auf.

    Stellen Sie den Mesh-Knoten bei der Ersteinrichtung direkt neben den Hauptrouter, damit er schnell erkannt wird. Nach Abschluss der Einrichtung können Sie ihn etwa auf halber Strecke zwischen dem Hauptrouter und einem Bereich ohne WLAN-Empfang aufstellen, um die WLAN-Abdeckung zu erweitern.

2. Melden Sie sich am webbasierten Admin Panel des Mesh-Knotens an, navigieren Sie zu **MESH** und klicken Sie auf **Mesh Node**.

    ![mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node.png){class="glboxshadow"}

    Der Mesh-Knoten kann nun erkannt werden und verfügt noch über keine Netzwerkverbindung, bis er dem Mesh-Netzwerk hinzugefügt wurde.

3. Melden Sie sich am webbasierten Admin Panel des Hauptrouters an und navigieren Sie zu **INTERNET**. Stellen Sie über einen beliebigen unterstützten Verbindungstyp eine Internetverbindung her: Ethernet, Repeater, Tethering oder Cellular.

4. Navigieren Sie nach dem Einrichten der Internetverbindung zu **MESH** und klicken Sie auf **Main Router**.

    ![main router](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_router.png){class="glboxshadow"}

5. Auf der Seite werden zwei Methoden zum Hinzufügen von Mesh-Knoten angezeigt: Wi-Fi Scan und Ethernet Backhaul.

    ![add mesh node](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_mesh_node.jpg){class="glboxshadow"}

    Wählen Sie nachfolgend die entsprechende Anleitung aus, um Ihre Mesh-Knoten hinzuzufügen.

    ??? note "Wi-Fi Scan"

        Klicken Sie auf **Start Scanning**.

        ![start scanning](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/start_scanning.png){class="glboxshadow"}

        Der Router sucht nun über WLAN nach Mesh-Knoten in der Nähe. Wählen Sie die Geräte aus, die Sie hinzufügen möchten, und klicken Sie auf **Add**.

        ![wifi scan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan1.png){class="glboxshadow"}

        Der Mesh-Knoten wird daraufhin Ihrem Mesh-Netzwerk hinzugefügt. Klicken Sie auf **Finish**.

        ![wifi scan2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/wifiscan2.png){class="glboxshadow"}

    ??? note "Ethernet Backhaul"

        Verbinden Sie den WAN-Port des Mesh-Knotens über ein Ethernet-Kabel mit dem LAN-Port des Hauptrouters. Ein Ethernet-Backhaul-Netzwerk wird daraufhin automatisch eingerichtet.

        ![ethernet backhaul](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/ethernet_backhaul.png){class="glboxshadow"}

6. Nachdem der Mesh-Knoten hinzugefügt wurde, wird die Topologie im Admin Panel des Hauptrouters angezeigt.

    ![main topology](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_topology_wifi.png){class="glboxshadow"}

## Knoten verwalten

Nach Abschluss der Einrichtung ist der Mesh-Knoten nicht mehr unter seiner ursprünglichen IP-Adresse erreichbar. Sie können den Hauptrouter und alle Mesh-Knoten über das Admin Panel des Hauptrouters verwalten.

### Details eines Knotens anzeigen

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Main Router**.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Sie können Details zum Hauptrouter anzeigen, darunter Modell, IP- und MAC-Adresse, Betriebszeit und verbundene Clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Sie können Details zum Mesh-Knoten anzeigen, darunter Modell, IP- und MAC-Adresse, Firmwareversion, Betriebszeit und verbundene Clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh-Knoten bearbeiten

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Jeder Mesh-Knoten wird standardmäßig als „Node“ gefolgt von den letzten vier Stellen seiner MAC-Adresse benannt. Klicken Sie auf das Bearbeitungssymbol, um Ihren Mesh-Knoten umzubenennen.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Auf Mesh-Knoten zugreifen

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Klicken Sie oben rechts auf das Zahnradsymbol und wählen Sie **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Sie werden zur Anmeldeseite des Mesh-Knotens unter der vom Hauptrouter zugewiesenen IP-Adresse weitergeleitet. Sie können sich nun am Mesh-Knoten anmelden.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Weitere Knoten hinzufügen

Klicken Sie bei Bedarf oben rechts in der Topologie auf **Add**, um weitere Knoten hinzuzufügen.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
