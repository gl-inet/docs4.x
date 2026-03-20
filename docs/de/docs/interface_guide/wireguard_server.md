# WireGuard-Server auf GL.iNet-Routern einrichten

WireGuard® ist ein äußerst einfaches und dennoch schnelles, modernes VPN, das modernste Kryptografie verwendet. Es wurde entwickelt, um schneller, einfacher, schlanker und nützlicher als IPSec zu sein, ohne den üblichen großen Aufwand zu verursachen. Zudem bietet es eine deutlich höhere Leistung als OpenVPN.

Um den WireGuard-Server auf einem GL.iNet-Router einzurichten, sehen Sie sich dieses Video an oder folgen Sie den nachstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jvc-CNmXfuM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Öffentliche IP-Adresse prüfen

Klicken Sie bitte [hier](../tutorials/how_to_check_if_isp_assigns_you_a_public_ip_address.md), um zu prüfen, ob Ihr Internetdienstanbieter Ihnen eine öffentliche IP-Adresse zuweist.

**Falls nicht, kann Ihr Router nicht als WireGuard-Server eingerichtet werden.**

Alternative Methoden:

1. Wenn Sie einen Hauptrouter haben, melden Sie sich dort an und prüfen Sie, ob er von Ihrem ISP eine öffentliche IP erhält.
2. Fragen Sie Ihren ISP nach einer öffentlichen IP-Adresse. Dafür können zusätzliche Gebühren anfallen.
3. Falls die beiden oben genannten Methoden nicht funktionieren (z. B. wenn sich Ihr Netzwerk hinter CGNAT befindet), können Sie unsere SD-WAN-Lösung [AstroWarp](https://www.astrowarp.net/){target="_blank"} ausprobieren. 

## Portweiterleitung prüfen

**Netzwerktopologie**

??? "GL.iNet ist der Hauptrouter"
    
    * Wenn der GL.iNet-Router der Hauptrouter in Ihrem Netzwerk ist, ist keine Portweiterleitung erforderlich. Bitte fahren Sie mit dem [nächsten Schritt](#wireguard-server-einrichten) fort.

??? "GL.iNet ist der Unterrouter"

    * Wenn bereits ein Hauptrouter verwendet wird und der GL.iNet-Router als sekundärer Router konfiguriert ist, müssen Sie auf dem Hauptrouter eine [Portweiterleitung](../tutorials/how_to_set_up_port_forwarding.md) einrichten.
    
    * Wenn bereits ein Hauptrouter verwendet wird und sich der GL.iNet-Router mehrere Ebenen darunter befindet, richten Sie die [Portweiterleitung](../tutorials/how_to_set_up_port_forwarding.md) auf jeder dazwischenliegenden Ebene ein.

## WireGuard-Server einrichten

Melden Sie sich im web Admin Panel an und wechseln Sie zu **VPN** -> **WireGuard Server**.

1. Klicken Sie auf **Generate Configuration** (nur für die Ersteinrichtung des VPN-Servers).

    ![generate configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/generate_configuration.png){class="glboxshadow"}

2. Prüfen Sie die Konfiguration.

    Die Standardkonfiguration funktioniert in den meisten Fällen, wie unten gezeigt. Sie müssen die IPv4-Adresse nicht ändern, sofern sie nicht mit dem Gateway Ihres Upstream-Routers in Konflikt steht.

    ![check configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/check_configuration.png){class="glboxshadow"}

    (IPv6 ist auf GL.iNet standardmäßig deaktiviert. Wenn Sie IPv6-Adressen verwenden möchten, aktivieren Sie bitte IPv6 auf Ihrem Router.)
    
    Wenn Sie feststellen, dass die IPv4-Adresse mit dem Gateway Ihres Upstream-Routers in Konflikt steht, ändern Sie die Adresse auf eine andere, z. B. **10.1.0.1/24**, und klicken Sie auf **Apply**. Achten Sie darauf, dass die CIDR-Notation "/24" enthalten ist, um Verbindungsprobleme zu vermeiden.

    ![modify configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/modify_configuration.png){class="glboxshadow"}

    Wenn sich beispielsweise upstream von einem GL.iNet-Router ein Xfinity-Router befindet, könnte dessen IP-Adresse 10.0.0.1 sein. Diese würde mit der Tunnel-IP des WireGuard-Servers kollidieren, wenn der GL.iNet-Router als WireGuard-Server eingerichtet ist. In diesem Fall müssen Sie die oben genannten Änderungen vornehmen.
    
    ![xfinity gateway](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/xfinitygateway.jpg){class="glboxshadow"}

3. Fügen Sie ein Profil hinzu.

    Wechseln Sie zur Registerkarte **Profiles** und klicken Sie auf **Add**, um ein Profil für Ihr Gerät zu erstellen.

    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles.png){class="glboxshadow"}

    Legen Sie einen aussagekräftigen Namen fest und klicken Sie auf **Apply**, um fortzufahren.

    ![profile name](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_name.png){class="glboxshadow"}
    
    Wenn Sie erweiterte Einstellungen festlegen möchten, klicken Sie auf **Set More**. Klicken Sie anschließend auf **Apply**, um fortzufahren.

    ![profile settings](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/add_profiles_set_more.png){class="glboxshadow"}

    ??? "Bei Bedarf Routing-Regeln hinzufügen"

        In den meisten Fällen ist es nicht erforderlich, Routing-Regeln hinzuzufügen.
        
        Wenn Sie vom Server aus auf LAN-Geräte des WireGuard-Clients zugreifen möchten, wechseln Sie auf der Seite **WireGuard Server** zur Registerkarte **Route Rules**, um die Routing-Regeln einzurichten. Klicken Sie [hier](../tutorials/wireguard_server_access_to_client_lan_side.md) für weitere Anweisungen.

        ![route rules](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/route_rules.png){class="glboxshadow"}

        Andernfalls fahren Sie mit Schritt 4 fort, um eine Client-Konfiguration herunterzuladen.

4. Konfiguration herunterladen.

    Nachdem Sie ein Profil hinzugefügt und auf **Apply** geklickt haben, wird eine Konfigurationsdatei in drei Formaten erstellt: QR-Code, Klartext und `.conf`-Datei. Wählen Sie die gewünschte Methode aus, um die Konfigurationsdatei zu erhalten.

    - **QR code**: Geeignet für Endgeräte (z. B. Smartphone, Tablet, Laptop), auf denen die WireGuard App installiert ist. Wenn Sie ein bestimmtes Gerät als WireGuard-Client einrichten möchten, öffnen Sie einfach die WireGuard App, scannen den QR-Code und die Konfiguration wird automatisch importiert.
    
        ![client configuration qrcode](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_qrcode.png){class="glboxshadow"}

    - **Plain text**: Im Klartextformat können Sie die Konfigurationsdetails prüfen und sie bequem an anderer Stelle für die manuelle Konfiguration einfügen, etwa in die WireGuard App oder auf einen GL.iNet-Router.

        ![client configuration plain text](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_text.png){class="glboxshadow"}

    - **.conf file**: Klicken Sie auf **Download**, um die `.conf`-Datei auf Ihrem lokalen Gerät zu speichern. Auch dieses Format ist praktisch und kann direkt in die WireGuard App oder auf einen GL.iNet-Router hochgeladen werden.

        ![client configuration file](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/download_config_file.png){class="glboxshadow"}

    Bei Bedarf können Sie die Serveradresse aus öffentlicher IP, DDNS-Domäne und aktueller WAN-IP auswählen. Diese Funktion ist seit Firmware v4.8 verfügbar. Nach einer Änderung wird die Serveradresse in der Konfigurationsdatei gleichzeitig aktualisiert.
    
    Wenn sich die öffentliche IP Ihres Netzwerks häufig ändert, wird zum Beispiel empfohlen, [DDNS](ddns.md) zu aktivieren und die DDNS-Domäne als Serveradresse zu verwenden. 
    
    ![change server address](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/change_server_address.png){class="glboxshadow"}

5. Starten Sie den WireGuard-Server.

    Klicken Sie oben rechts auf **Start**, um den WireGuard-Server zu starten.

    ![start wireguard server](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/start_wgserver.png){class="glboxshadow"}

    Der Verbindungsstatus wird auf derselben Seite angezeigt.

    ![wireguard server status](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

## Prüfen, ob der WireGuard-Server ordnungsgemäß funktioniert

### Serverstatus prüfen

Seit Firmware v4.8 können Sie den Server-Verbindungsstatus auf der Seite **WireGuard Server** prüfen. 

Wenn Upload-/Download-Verkehrsstatistiken und online verbundene Geräte angezeigt werden, bedeutet dies, dass der WireGuard-Server läuft und WireGuard-Clients damit verbunden sind.

![wireguard server connected](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status.png){class="glboxshadow"}

Wenn 0 Datenverkehr und 0 Clients angezeigt werden, bedeutet das, dass kein WireGuard-Client verbunden ist.

![wireguard server no client](https://static.gl-inet.com/docs/router/en/4/tutorials/wireguard_server/wgserver_status_no_client.png){class="glboxshadow"}

Bei Firmware v4.7 und früher prüfen Sie den Server-Verbindungsstatus bitte auf der Seite **VPN Dashboard**.

### IP-Adresse des Clients prüfen

So prüfen Sie, ob die Verbindung zum Server erfolgreich ist: Importieren Sie die zuvor exportierte WireGuard-Konfiguration auf ein Gerät in einem anderen Netzwerk (nicht im selben lokalen Netzwerk wie der Server). Öffnen Sie dann einen Webbrowser und suchen Sie nach Ihrer IP-Adresse und Ihrem Standort. Wenn diese mit der IP-Adresse und dem Standort des VPN-Servers übereinstimmen (anstelle der IP-Adresse und des Standorts Ihres Internetdienstanbieters), ist die VPN-Verbindung erfolgreich.

Am einfachsten geht das mit einem Smartphone, auf dem die offizielle [WireGuard App](https://www.wireguard.com/install){target="_blank"} installiert ist. Deaktivieren Sie zunächst das WLAN des Smartphones und verbinden Sie es ausschließlich über mobile Daten (4G/5G) mit dem Internet. Öffnen Sie dann die WireGuard App, importieren Sie die Konfigurationsdatei und starten Sie die Verbindung. Prüfen Sie anschließend, ob das Smartphone auf das Internet zugreifen kann und ob seine IP-Adresse mit der IP-Adresse des WireGuard-Servers übereinstimmt.

Wenn die Verbindung fehlschlägt, gibt es mehrere häufige Ursachen:

* Ihr Internetdienstanbieter weist Ihnen keine öffentliche IP-Adresse zu. Bitte prüfen Sie [hier](#offentliche-ip-adresse-prufen).
* Möglicherweise müssen Sie eine Portweiterleitung einrichten. Bitte prüfen Sie [hier](#portweiterleitung-prufen).
* Der für den WireGuard-Server verwendete Port wird von Ihrem Internetdienstanbieter blockiert. Wechseln Sie auf einen anderen Port oder wenden Sie sich für weitere Unterstützung an den Internetdienstanbieter.
* In einigen Ländern/Regionen kann die VPN-Verbindung blockiert werden.

## WireGuard App installieren

Bitte laden Sie die WireGuard App von der [offiziellen WireGuard-Website](https://www.wireguard.com/install){target="_blank"} herunter.

---

WireGuard® ist eine eingetragene Marke von Jason A.Donenfeld.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
