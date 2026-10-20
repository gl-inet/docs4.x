# Mesh {#mesh}

**Hinweis**: Diese Funktion wurde mit Firmware v4.10 eingeführt.

Mango 2 (GL-MG1300) und Mudi 7 (GL-E5800) unterstützen Mesh auch mit Firmware v4.10 oder höher nicht. Weitere Informationen finden Sie unter [Unterstützte Modelle](#supported-models).

---

Navigieren Sie auf der linken Seite des webbasierten Admin Panels zu **MESH**.

Mesh ist eine auf dem Wi-Fi EasyMesh™-Standard basierende Funktion, die die WLAN-Abdeckung im gesamten Zuhause erweitert und nahtloses Roaming ermöglicht. Wenn Sie mehrere GL.iNet-Router besitzen, legen Sie einen davon als Hauptrouter und die übrigen als Mesh-Knoten fest. Dadurch können Sie sich in Ihrem Zuhause bewegen, ohne die WLAN-Verbindung wechseln zu müssen.

## Mesh, Extender und Access-Point-Modus im Vergleich {#mesh-vs-extender-vs-access-point-mode}

Alle drei Modi können die Wi-Fi-Abdeckung erweitern. Die wesentlichen Unterschiede betreffen die Verbindung zum Hauptrouter sowie die Konfiguration und Verwaltung der Geräte. **Backhaul** bezeichnet die Verbindung zwischen dem Hauptrouter und einem Extender, Access Point oder Mesh-Knoten.

Die folgende Tabelle vergleicht die eigenständigen Modi Extender und Access Point von GL.iNet mit der Mesh-Implementierung.

| Funktion | Extender-Modus | Access-Point-Modus | Mesh-Modus |
|---|---|---|---|
| **Drahtloser Backhaul** | ✅ Unterstützt | ❌ Nicht verwendet | ✅ Unterstützt |
| **Ethernet-Backhaul** | ❌ In diesem Modus nicht verwendet | ✅ Unterstützt | ✅ Unterstützt |
| **Vollduplex-Backhaul** | ❌ Wi-Fi arbeitet im Halbduplexbetrieb | ✅ Ethernet | ✅ Nur Ethernet; drahtloser Backhaul bleibt Halbduplex |
| **Drahtloser Backhaul über 2.4/5 GHz** | ⚠️ Verfügbare Bänder hängen von Modell und Firmware ab | ❌ Nicht zutreffend | ⚠️ Verfügbare Bänder hängen von Modell und Firmware ab |
| **Drahtloser Backhaul über 6 GHz** | ⚠️ Abhängig von Modell und Firmware | ❌ Nicht zutreffend | 🔜 Demnächst verfügbar |
| **Wi-Fi-Roaming** | ✅ Vom Client gesteuert | ✅ Vom Client gesteuert | ✅ Vom Client gesteuert, mit Unterstützung durch 802.11k/v |
| **Automatische Synchronisierung der Wi-Fi-Einstellungen** | ❌ Separat konfigurieren | ❌ Separat konfigurieren | ✅ Vom Hauptrouter aus |
| **Zentrale Knotenverwaltung** | ❌ Separat konfigurieren | ❌ Separat konfigurieren | ✅ Über den Hauptrouter |
| **Netzwerktopologie und Client-Übersicht** | ❌ Keine Mesh-weite Übersicht | ❌ Keine Mesh-weite Übersicht | ✅ Auf dem Hauptrouter verfügbar |
| **Zentral verwaltete Erweiterung** | ❌ Unabhängige Extender | ❌ Unabhängige Access Points | ✅ Ein Hauptrouter und bis zu acht Knoten |
| **Zentral verwaltete drahtlose Hops** | ❌ Nicht durch Mesh verwaltet | ❌ Nicht zutreffend | ✅ Bis zu drei drahtlose Hops |
| **Automatischer Wechsel zwischen kabelgebundenem und drahtlosem Backhaul** | ❌ Kein durch Mesh verwalteter Wechsel | ❌ Kein durch Mesh verwalteter Wechsel | ✅ Bevorzugt Ethernet |
| **Besonders geeignet für** | Einfache drahtlose Erweiterung der Abdeckung | Erweiterung der Abdeckung bei verfügbarem Ethernet | Abgestimmte Abdeckung mit kabelgebundenen, drahtlosen oder gemischten Verbindungen |

✅ Unterstützt · ❌ In diesem Modus nicht unterstützt oder nicht zutreffend · ⚠️ Abhängig von Hardware, Firmware oder Konfiguration · 🔜 Geplante Funktion

Mesh synchronisiert unterstützte Wi-Fi-Einstellungen für Haupt-, Gast-, IoT- und MLO-Netzwerke. Es bietet außerdem eine zentrale Knotenverwaltung, einschließlich Neustart, Entfernen und Aktualisieren unterstützter GL.iNet-Knoten. Knoten lassen sich per Wi-Fi-Suche, Ethernet-Verbindung oder, sofern unterstützt, über eine Mesh/WPS-Taste hinzufügen. Die Backhaul-Verwaltung umfasst Ethernet-Priorität, den Wechsel zwischen kabelgebundenen und drahtlosen Verbindungen sowie die Vermeidung von Schleifen.

### Leistungsunterschiede verstehen {#understanding-performance-differences}

#### Extender-Modus {#extender-mode}

Das Gerät verbindet sich mit einem bestehenden Wi-Fi-Netzwerk. Das für diese Upstream-Verbindung verwendete Funkmodul folgt dem Kanal des Hauptrouters. Clients, die dasselbe Funkmodul nutzen, verwenden ebenfalls diesen Kanal. Upstream- und Client-Datenverkehr teilen sich daher die verfügbare Sendezeit.

Bei unterstützten Mehrbandmodellen können separate Funkmodule weiterhin Clients auf anderen Bändern versorgen. Ein Extender kann sich beispielsweise über 2.4 GHz mit dem Hauptrouter verbinden und gleichzeitig Clients über sein separates 5-GHz-Funkmodul bedienen. Diese beiden Verbindungen konkurrieren nicht um die Sendezeit desselben Kanals. Die verfügbaren Kombinationen hängen von Modell und Firmware ab; der Extender-Modus ist grundsätzlich nicht auf ein einzelnes Band beschränkt.

Dieselbe Vorgabe für den Upstream-Kanal gilt für die Repeater-Verbindungsfunktion von GL.iNet, obwohl sich der Repeater-Betrieb und der eigenständige Extender-Netzwerkmodus in anderen Punkten unterscheiden.

#### Drahtloses Mesh {#wireless-mesh}

In der getesteten Tri-Band-Mesh-Konfiguration nutzt der Knoten **5 GHz für den drahtlosen Backhaul**. Sein 5-GHz-Kanal folgt dem Hauptrouter und kann nicht unabhängig geändert werden. Die separaten **Kanaleinstellungen für 2.4 GHz und 6 GHz bleiben dagegen unabhängig konfigurierbar**. Diese Aussage bezieht sich auf Kanaleinstellungen und nicht darauf, mit welchen Bändern sich Client-Geräte verbinden können. Eine Änderung des clientseitigen Kanals ändert das Backhaul-Band nicht.

Die Auswirkungen auf die Leistung hängen daher von der Client-Verbindung ab:

- **Über 5 GHz verbundene Geräte:** Wenn sich ein Smartphone, Laptop oder anderes Gerät mit dem 5-GHz-Wi-Fi des Mesh-Knotens verbindet und dasselbe Funkmodul den drahtlosen Backhaul überträgt, teilen sich die Verbindungen die verfügbare Sendezeit. Ein festgelegter 5-GHz-Kanal des Knotens verhindert nicht zwangsläufig, dass sich Clients auf diesem Band verbinden.
- **Über 2.4 GHz oder 6 GHz verbundene Geräte:** Wenn diese Clients ein separates Funkmodul gegenüber dem drahtlosen 5-GHz-Backhaul verwenden, entfällt bei diesen beiden Verbindungen der Nachteil der Weiterleitung auf demselben Kanal.

Dies beschreibt die getestete Konfiguration, nicht jedes unterstützte Mesh-Modell. Die Weiterleitung über separate Funkmodule ist keine exklusive Mesh-Funktion. Ein Wechsel von Extender zu Mesh verbessert den Durchsatz nicht automatisch.

#### Access-Point-Modus und kabelgebundenes Mesh {#access-point-mode-and-wired-mesh}

Beide nutzen Ethernet für die Verbindung zum Hauptrouter. Ethernet-Backhaul arbeitet im Vollduplexbetrieb und vermeidet die Übertragung des Backhaul-Datenverkehrs über Wi-Fi. Wi-Fi-Verbindungen der Clients bleiben Halbduplex. Bei ansonsten vergleichbarer Hardware und vergleichbaren Bedingungen können Access-Point-Modus und kabelgebundenes Mesh einen ähnlichen Durchsatz bieten; Mesh ergänzt eine abgestimmte Konfiguration und Verwaltung.

Mesh bevorzugt Ethernet-Backhaul und unterstützt den Wechsel zu einer drahtlosen Verbindung, wenn eine geeignete Verbindung verfügbar ist. In der getesteten Konfiguration bleibt der 5-GHz-Kanal des Knotens auch bei aktivem Ethernet-Backhaul mit dem Hauptrouter abgestimmt. Dies bedeutet nicht, dass der Datenverkehr über den drahtlosen Backhaul läuft. Ethernet beseitigt den drahtlosen Hop für den Daten-Backhaul, doch benachbarte Knoten und Clients auf demselben Wi-Fi-Kanal können weiterhin um Sendezeit konkurrieren.

!!! note "6-GHz-Mesh-Backhaul — Demnächst verfügbar"

    Für 6-GHz-Mesh-Backhaul werden sowohl am Hauptrouter als auch am Mesh-Knoten kompatible 6-GHz-Hardware und unterstützende Firmware benötigt. Gehen Sie nicht davon aus, dass alle Mesh-fähigen Modelle diese Funktion unterstützen werden.

    Dies unterscheidet sich davon, einen Client mit dem bestehenden 6-GHz-Wi-Fi-Netzwerk eines Knotens zu verbinden. Mit 6-GHz-Backhaul könnte ein separates 5-GHz-Funkmodul Clients bedienen, ohne die Sendezeit des Backhaul-Kanals zu teilen. Ein Funkmodul ist nur dann ausschließlich für Backhaul vorgesehen, wenn es für diesen Zweck reserviert ist und nicht zusätzlich Clients bedient.

!!! important "Separate Funkmodule machen Wi-Fi nicht zu Vollduplex"

    Jede Wi-Fi-Verbindung bleibt Halbduplex. Die Weiterleitung über separate Funkmodule vermeidet die gemeinsame Nutzung eines Kanals für Backhaul- und Client-Verbindungen, beseitigt aber keine anderen Störungen, Kanalbelegungskonflikte oder Mehrfach-Hop-Einschränkungen. Der Ende-zu-Ende-Durchsatz wird weiterhin durch die langsamere Verbindung und die Netzwerkbedingungen begrenzt.

## Unterstützte Modelle {#supported-models}

??? "Unterstützte Modelle"
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Nicht unterstützte Modelle"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)


## Schnelleinrichtung {#quick-setup}

Im folgenden Beispiel wird mit Flint 3 (GL‑BE9300) und Slate 7 (GL‑BE3600) ein Mesh-Netzwerk eingerichtet.

**Flint 3** ist der Hauptrouter, der die Verbindung zum Internet herstellt und alle Mesh-Knoten verwaltet.

**Slate 7** ist der Mesh-Knoten, der die WLAN-Abdeckung des Hauptrouters erweitert.

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

## Knoten verwalten {#manage-nodes}

Nach Abschluss der Einrichtung ist der Mesh-Knoten nicht mehr unter seiner ursprünglichen IP-Adresse erreichbar. Sie können den Hauptrouter und alle Mesh-Knoten über das Admin Panel des Hauptrouters verwalten.

### Details eines Knotens anzeigen {#view-node-details}

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Main Router**.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info1.png){class="glboxshadow"}

Sie können Details zum Hauptrouter anzeigen, darunter Modell, IP- und MAC-Adresse, Betriebszeit und verbundene Clients.

![main node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/main_node_info2.png){class="glboxshadow"}

Klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Sie können Details zum Mesh-Knoten anzeigen, darunter Modell, IP- und MAC-Adresse, Firmwareversion, Betriebszeit und verbundene Clients.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info2.png){class="glboxshadow"}

### Mesh-Knoten bearbeiten {#edit-mesh-node}

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Jeder Mesh-Knoten wird standardmäßig als „Node“ gefolgt von den letzten vier Stellen seiner MAC-Adresse benannt. Klicken Sie auf das Bearbeitungssymbol, um Ihren Mesh-Knoten umzubenennen.

![edit node 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/astromesh/edit_node1.png){class="glboxshadow"}

![edit node 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/edit_node2.png){class="glboxshadow"}

### Auf Mesh-Knoten zugreifen {#access-mesh-node}

Navigieren Sie im Admin Panel des Hauptrouters zu **MESH** und klicken Sie in der Topologie auf **Mesh Node**.

![mesh node info](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/mesh_node_info1.png){class="glboxshadow"}

Klicken Sie oben rechts auf das Zahnradsymbol und wählen Sie **Open Admin Panel**.

![mesh node actions](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node1.png){class="glboxshadow"}

Sie werden zur Anmeldeseite des Mesh-Knotens unter der vom Hauptrouter zugewiesenen IP-Adresse weitergeleitet. Sie können sich nun am Mesh-Knoten anmelden.

![mesh admin login](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/access_mesh_node2.png){class="glboxshadow"}

### Weitere Knoten hinzufügen {#add-more-nodes}

Klicken Sie bei Bedarf oben rechts in der Topologie auf **Add**, um weitere Knoten hinzuzufügen.

![add more nodes](https://static.gl-inet.com/docs/router/en/4/interface_guide/mesh/add_node.png){class="glboxshadow"}

---

Noch Fragen? Besuchen Sie unser [Community-Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
