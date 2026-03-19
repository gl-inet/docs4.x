# GoodCloud Site-to-Site

## Einführung

GoodCloud Site-to-Site ermöglicht es Büros an mehreren Standorten, sichere Verbindungen über das Internet miteinander aufzubauen. Dadurch wird das Unternehmensnetzwerk erweitert, sodass Computerressourcen eines Standorts für Mitarbeiter an anderen Standorten im Netzwerk verfügbar sind.

![site to site](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/s2s-main.png){class="glboxshadow"}

**Szenario 1**: Dutzende Zweigstellen desselben Unternehmens müssen in ein einheitliches privates Netzwerk integriert werden, damit Ressourcen standortübergreifend nahtlos gemeinsam genutzt werden können.

**Szenario 2**: Wenn zwei eng zusammenarbeitende Unternehmen geschäftlich kooperieren müssen, erleichtert Site-to-Site die Zusammenarbeit in einer gemeinsamen und sicheren Netzwerkumgebung.

**Szenario 3**: Für Familien mit IP-Kameras ermöglicht Site-to-Site den Fernzugriff auf die Geräte, wenn Familienmitglieder nicht zu Hause sind, und sorgt so für eine einfache Überwachung von überall.

## Voraussetzungen

1. Zum Aufbau eines Site-to-Site-Netzwerks werden mindestens zwei GL.iNet-Router benötigt.

2. Mindestens ein Router sollte über eine öffentliche IP-Adresse verfügen, damit er als Hauptknoten festgelegt werden kann. [Prüfen Sie, ob Ihr ISP Ihnen eine öffentliche IP-Adresse zuweist](how_to_check_if_isp_assigns_you_a_public_ip_address.md).

    Als Hauptknoten wird ein Router mit hoher Leistung und der besten Netzwerkgeschwindigkeit empfohlen.

3. Es wird **NICHT** empfohlen, Site-to-Site zu betreiben, während die Unterknoten gleichzeitig einen VPN-Client / Tailscale / ZeroTier / AstroWarp verwenden, da dies die Netzwerkkonfiguration besonders komplex machen kann.

## Ein Site-to-Site-Netzwerk aufbauen

1. Verbinden Sie Ihre Router mit Ihrem GoodCloud-Konto. [Wie](../interface_guide/cloud.md/#setup-your-goodcloud-account)?

2. Melden Sie sich bei [GoodCloud](https://www.goodcloud.xyz/#/login) an, navigieren Sie in der linken Seitenleiste zu **Site to Site** und klicken Sie oben rechts auf **Create Network**.

    ![create network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/create-network.png){class="glboxshadow"}

3. Aktivieren Sie das Kontrollkästchen auf der linken Seite, um mindestens zwei Geräte auszuwählen.

    ![select devices](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/select-devices.png){class="glboxshadow"}
    
    Die ausgewählten Geräte werden im unteren Bereich der Seite angezeigt.

    Der Standardport für Site-to-Site ist **51830**. Wenn Sie einen anderen Port verwenden möchten, klicken Sie unten links auf **Advanced**, um ihn zu ändern. Klicken Sie anschließend auf **Next**.

    ![two devices selected](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/two-devices-selected.png){class="glboxshadow"}

    Ein Site-to-Site-Netzwerk kann zur Gewährleistung einer stabilen Leistung bis zu 10 Geräte enthalten.

4. Benennen Sie Ihr Netzwerk und klicken Sie auf **Next**.

    ![name network](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/name-network.png){class="glboxshadow"}

5. Der Test **Node Usability Testing** startet und prüft, ob ein Gerät als Hauptknoten festgelegt werden kann.

    ![node testing](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/node-testing.png){class="glboxshadow"}

    Wenn keines Ihrer Geräte als Hauptknoten verwendet werden kann, stellen Sie bitte Folgendes sicher:

    - Mindestens ein Router hat eine öffentliche IP, entweder eine statische oder dynamische öffentliche IP.
    - Der Port ist geöffnet. Der Standardport für Site-to-Site ist 51830. Sie können auch den Port ändern und es erneut versuchen.
    - Wenn sich der Router, den Sie als Hauptknoten festlegen möchten, hinter NAT befindet, müssen Sie möglicherweise eine Portweiterleitung einrichten.

    ![testing failed](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-failed.png){class="glboxshadow"}

    Wenn mehr als ein Gerät als Hauptknoten festgelegt werden kann, wählen Sie bitte eines aus, um fortzufahren. Wir empfehlen, den Router mit hoher Leistung und der besten Netzwerkgeschwindigkeit als Hauptknoten auszuwählen.

    ![testing success](https://static.gl-inet.com/goodcloud/docs/tutorials/site_to_site/testing-success.jpg){class="glboxshadow"}

    Wenn nur ein Gerät als Hauptknoten festgelegt werden kann, gelangen Sie direkt zur Detailseite von Site-to-Site.

6. Das Netzwerk ist standardmäßig deaktiviert. Stellen Sie sicher, dass sich die LAN-IP-Adressen aller Knoten nicht überschneiden. Klicken Sie bei Bedarf auf das Zahnradsymbol, um die LAN-IP zu ändern, und klicken Sie dann auf **Start**.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-00.png){class="glboxshadow"}

7. Warten Sie einige Minuten. Sobald die gestrichelte Linie durchgezogen angezeigt wird, wurde das Site-to-Site-Netzwerk erfolgreich aufgebaut.

    ![detail s2s](https://static.gl-inet.com/goodcloud/docs/detail-s2s-01.png){class="glboxshadow"}

## Die Site-to-Site-Verbindung testen

1. Verbinden Sie Ihren PC oder Ihr Smartphone mit einem der Knoten in diesem Site-to-Site-Netzwerk.

2. Öffnen Sie einen Webbrowser und greifen Sie auf die LAN-IP eines anderen Knotens zu. Wenn Sie die Anmeldeseite aufrufen können, funktioniert die Verbindung zwischen diesen beiden Knoten.

## Routen und weitere Optionen

Standardmäßig kann jeder Knoten auf das LAN anderer Knoten zugreifen. Aus Sicherheitsgründen empfehlen wir, nur die IP-Adressen bestimmter Dienste freizugeben.

Beispielsweise befindet sich in dem Subnetz von Knoten 1 ein Server A (172.30.97.100). Wenn andere Knoten nur auf Dienst A von Knoten 1 zugreifen sollen, können Sie dies wie folgt einrichten:

![LAN IP and routes](https://static.gl-inet.com/goodcloud/docs/lanip-routes-s2s-02.png){class="glboxshadow"}

Sie können auch übergeordnete Routen eines Knotens hinzufügen.

Jeder Unterknoten baut ein verschlüsseltes Tunnelnetzwerk zum Hauptknoten auf. Wenn Sie die IP des Tunnel-Subnetzes ändern möchten, klicken Sie auf **IP Address Range**.

Das Anwenden einer Änderung des IP-Adressbereichs führt für einige Minuten zu einer Netzwerkunterbrechung.

![Tunnel IP Address Range](https://static.gl-inet.com/goodcloud/docs/tunnel-ip-address-range-s2s.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
