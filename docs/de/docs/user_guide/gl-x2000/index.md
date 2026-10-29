# Spitz Plus (GL-X2000) Benutzerhandbuch {#spitz-plus-gl-x2000-user-guide}

## Sicherheitshinweise {#safety-information}

Lesen Sie vor der Verwendung des Geräts alle nachstehenden Sicherheitsinformationen sorgfältig durch. Die nachfolgenden Sicherheitsempfehlungen können nicht sämtliche möglicherweise auftretenden Gefahrensituationen abdecken.

Installieren oder verwenden Sie das Gerät nicht in Umgebungen mit hohen Temperaturen, starker Staubentwicklung, schädlichen Gasen, Brandgefahr, Explosionsgefahr, starken elektromagnetischen Störungen, instabiler Netzspannung, starken Vibrationen oder starker Lärmeinwirkung.

Installieren oder verwenden Sie das Gerät nicht in feuchten Umgebungen, in denen Wasseransammlungen, eindringendes Wasser, Tropfwasser oder Kondensat auftreten können, da dies einen Stromschlag verursachen kann.

Elektromagnetische Störungen können von jedem Gerät ausgehen, das elektromagnetische Signale aussendet. Um Störungen medizinischer Geräte zu vermeiden, befolgen Sie beim Betrieb dieses Geräts insbesondere in Krankenhäusern, ambulanten Gesundheitszentren, Arztpraxen und sonstigen medizinischen Einrichtungen die Anweisungen und Vorgaben des autorisierten Personals, um eine Beeinflussung empfindlicher medizinischer Geräte auszuschließen.

Sofern das Gerät mit einem Netzteil ausgeliefert wird, verwenden Sie zur Stromversorgung ausschließlich das mitgelieferte Netzteil.

Sofern das Gerät mit einem Bildschirm ausgestattet ist und dieser Risse oder Beschädigungen aufweist, verwenden Sie das Gerät nicht weiter. Gebrochenes Glas oder gebrochener Kunststoff kann zu Verletzungen an Händen oder im Gesicht führen.

Sofern das Gerät mit einer Batterie ausgestattet ist, verwenden Sie ausschließlich Batterien, die den Anforderungen der Spezifikation entsprechen. Weist die Batterie sichtbare Beschädigungen auf, tauschen Sie sie aus, da es andernfalls zu Personenschäden kommen kann. Funkendgeräte dürfen nur bei geschlossener Batterieabdeckung betrieben werden.

Bewahren Sie kleine Batterien und Kleinteile, die verschluckt werden könnten, für Kinder unzugänglich auf. Das Verschlucken einer Batterie kann schwere Verletzungen verursachen; nehmen Sie in diesem Fall unverzüglich ärztliche Hilfe in Anspruch.

Vermeiden Sie ein häufiges Umstellen des Geräts. Schalten Sie vor jedem Bewegen oder Transportieren sämtliche Stromversorgungen aus und ziehen Sie alle Netz- und Anschlusskabel ab.

Überlastete Steckdosen, Verlängerungskabel und Steckdosenleisten können Brände und Stromschläge verursachen.

Durch Wärmestau kann sich das Gerät übermäßig erhitzen. Stellen Sie das Gerät daher nicht auf Teppiche oder weiche Unterlagen und sorgen Sie für eine ausreichende Luftzirkulation im Umfeld des Geräts. Stellen Sie das Gerät nicht auf Oberflächen von Gegenständen, die empfindlich auf Wärme reagieren.

Um den einwandfreien Betrieb des Geräts zu gewährleisten, beachten Sie die in den technischen Daten angegebene zulässige Betriebsumgebungstemperatur des Geräts.

Unsachgemäßes Öffnen oder unsachgemäße Instandsetzung kann den Benutzer des Geräts gefährden.

Schalten Sie bei einem Störfall zuerst den Netzschalter aus.

## Produktübersicht {#product-overview}

Spitz Plus (GL-X2000) ist ein Dual-SIM-4G-LTE-Wi-Fi-6-Cellular-Gateway, das besonders in abgelegenen Gebieten und auf Reisen schnelle und zuverlässige Verbindungen bietet. Mit Drei-Träger-Aggregation (3CA) kann der Router bis zum Dreifachen der theoretischen Kanalbandbreite einer Cat 4-Verbindung mit einem einzelnen Träger bereitstellen. Dies hängt von den Bandbreiten der aggregierten Träger sowie der Unterstützung für LTE 3CA durch Ihren Mobilfunkanbieter und die lokalen Basisstationen ab. Er unterstützt vier Methoden für den Internetzugang: Cellular (SIM-Karten), Ethernet, Repeater und Tethering. Darüber hinaus werden Multi-WAN (Failover und Lastverteilung), VPN (OpenVPN und WireGuard), Parental Control, AdGuard Home, Portweiterleitung, Tailscale und weitere Funktionen unterstützt.

![gl-x2000 interface](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/hardware_info/x2000_interface.jpg){class="glboxshadow"}

## Lieferumfang {#package-contents}

- 1 x Spitz Plus (GL-X2000)
- 1 x Benutzerhandbuch
- 4 x Externe Antennen
- 1 x Dankeskarte
- 1 x RJ45-Ethernet-Kabel
- 1 x Wandmontageset
- 1 x Klebepad
- 1 x Netzadapter
- 1 x Adapter (je nach Versandland)

![package contents](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/first_time_setup/x2000_package.png){class="glboxshadow"}

## LED-Anzeigen {#led-indicators}

Die folgenden Angaben beschreiben die LED-Zustände bei verschiedenen Ereignissen. Alle Zustände der einzelnen LEDs finden Sie unter [GL-X2000: LED-Status](../../faq/led.md#gl-x2000){target="_blank"}.

| Gerätestatus | Stromversorgung | Internet | 2.4GHz | 5GHz | Cellular |
| --- | --- | --- | --- | --- | --- |
| Mit dem Internet verbunden | Grün | Grün | Grün | Grün | Grün |
| Keine Internetverbindung | Grün | Aus | Grün | Grün | Grün |
| Firmware wird aktualisiert | Grün | Blinkt alle 0,5 s | Blinkt alle 0,5 s | Blinkt alle 0,5 s | Grün |
| Netzwerk zurücksetzen (Reset 5 s gedrückt halten) | Blinkt alle 1 s | Grün | Grün | Grün | Grün |
| Auf Werkseinstellungen zurücksetzen (Reset 10 s gedrückt halten) | Blinkt schnell alle 0,25 s | Grün | Grün | Grün | Grün |

## So richten Sie Spitz Plus ein {#how-to-set-up-spitz-plus}

Zum Einrichten von Spitz Plus verwenden Sie eine der vier unterstützten Internetverbindungsmethoden: Cellular (SIM erforderlich), Ethernet, Repeater und Tethering. Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/-_K3xuAj4UA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<small>(Dieses Video zeigt die Einrichtung von Spitz Plus über Cellular. Wenn Sie Spitz Plus mit einer anderen Internetverbindungsmethode konfigurieren möchten, beachten Sie bitte die untenstehenden Schritte.)</small>

!!! note "Bevor Sie beginnen, führen Sie diese Schritte aus (bei Verbindung über Cellular):"

    Für die Verbindung mit dem Internet über Cellular wird mindestens eine Nano-SIM-Karte benötigt. Wenn Sie die Nano-SIM-Karte(n) bereit haben, führen Sie bitte die folgenden Schritte aus:

    1. Aktivieren Sie Ihre SIM-Karte(n), falls dies vom Mobilfunkanbieter verlangt wird.
    2. Schalten Sie Ihren Router aus.
    3. Setzen Sie die SIM-Karte(n) in die SIM-Kartensteckplätze ein. (**Hinweis:** Es ist jeweils nur eine SIM-Karte aktiv. Die andere SIM-Karte dient ausschließlich als Backup.)

### 1. Einschalten {#1-power-on}

Setzen Sie den zweiteiligen Netzadapter zusammen. Schließen Sie ihn an Ihren Router an und stecken Sie ihn in eine Steckdose. Das Gerät startet automatisch.

### 2. Gerät verbinden {#2-connect-device}

Verbinden Sie ein Gerät (z. B. Computer, Laptop oder Smartphone) per Wi-Fi oder Ethernet mit dem Router.

- Ethernet

    Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem LAN-Port des Routers.

- Wi-Fi

    Öffnen Sie auf Ihrem Gerät Settings -> WLAN, suchen Sie in der Liste der verfügbaren Netzwerke den Wi-Fi-Netzwerknamen Ihres Routers und geben Sie das Passwort ein. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett Ihres Routers.

### 3. Im Web-Admin-Panel anmelden {#3-log-in-to-web-admin-panel}

Öffnen Sie einen Webbrowser, geben Sie `192.168.8.1` in die Adressleiste ein und melden Sie sich an. Wählen Sie eine Sprache aus, legen Sie Ihr Admin-Passwort fest und klicken Sie anschließend auf **Apply**.

### 4. Internet einrichten {#4-internet-setup}

**Hinweis:** Die folgenden Anweisungen gelten für Benutzer, die den Router über das GL.iNet Web-Admin-Panel konfigurieren. Wenn Sie lieber die GL.iNet-App verwenden möchten, [laden Sie die App herunter](https://www.gl-inet.com/app/){target="_blank"} und folgen Sie den Anweisungen auf dem Bildschirm.

Richten Sie Spitz Plus mit einer der unterstützten Internetverbindungsmethoden ein: Cellular, Ethernet, Repeater und Tethering. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Cellular"

    ![cellular](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/internet/x2000_cellular.jpg){class="glboxshadow"}

    Wenn Sie die SIM-Karte in Ihren Router eingesetzt haben, sollte die Internetverbindung automatisch hergestellt werden. Im Cellular-Bereich sollten der Name Ihres Mobilfunkanbieters und ein grüner Punkt angezeigt werden.

    Falls nicht, schalten Sie den Router aus, setzen Sie die SIM-Karte erneut ein und schalten Sie das Gerät wieder ein.

    Detaillierte Anweisungen finden Sie unter [Über Cellular eine Verbindung zum Internet herstellen](../../interface_guide/internet_cellular.md#setup-for-dual-sim-models).

    **Hinweis:** Die eSIM-Funktion von Spitz Plus ist ab Firmware v4.7 verfügbar. Wie Sie die physische eSIM-Karte auf einem GL.iNet-Router verwenden, erfahren Sie [hier](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    Wenn Probleme auftreten, lesen Sie bitte den [Leitfaden zur Fehlerbehebung bei Cellular-Netzwerken](../../faq/cellular_network_troubleshooting_guide.md).

=== "Ethernet"

    ![ethernet](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/internet/x2000_ethernet.jpg){class="glboxshadow"}

    Verbinden Sie den WAN-Port von Spitz Plus per Ethernet-Kabel mit einem vorgelagerten Gerät, z. B. einem Modem.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Ethernet-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/internet/x2000_repeater.jpg){class="glboxshadow"}

    1. Suchen Sie auf der Seite INTERNET des Admin-Panels den Bereich Repeater und klicken Sie auf **Connect**.
    2. Wählen Sie ein Wi-Fi-Netzwerk aus den verfügbaren Netzwerken aus.
    3. Geben Sie das Passwort ein und klicken Sie dann auf **Apply**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Repeater-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

     ![tethering](https://static.gl-inet.com/docs/router/de/4/user_guide/gl-x2000/internet/x2000_tethering.jpg){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder USB-Dongle, per USB-Kabel mit dem USB-Port des Routers.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie USB Tethering.
    3. Klicken Sie auf der Seite INTERNET des Web-Admin-Panels im Bereich Tethering auf **Connect**.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint im Tethering-Bereich auf der Seite INTERNET ein grüner Punkt.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

---

Im Folgenden finden Sie einen Überblick über die Funktionen im Web-Admin-Panel von Spitz Plus.

## WLAN {#wireless}

Auf der Seite Wireless können Sie Einstellungen für 5-GHz- und 2,4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren/Deaktivieren von Wi-Fi, die TX-Leistung, den Wi-Fi-Namen (SSID), das Aktivieren/Deaktivieren der randomisierten BSSID, den Wi-Fi-Sicherheitsmodus, das Wi-Fi-Passwort, die Sichtbarkeit der SSID sowie Wi-Fi-Modus, Bandbreite und Kanal.

Weitere Informationen finden Sie unter [Wireless](../../interface_guide/wireless_v4.8.md).

## Clients {#clients}

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Gerätename, Verbindungstyp (d. h. über Ethernet oder Wi-Fi), IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie eine IP reservieren, den Client blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste {#cloud-services}

=== "GoodCloud"

    Der Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, aus der Ferne auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Remote-Vernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt ein umfassendes Gerätemanagement über ganze Netzwerke hinweg, einschließlich der Verwaltung über- und untergeordneter Geräte. Mit seinem Fokus auf netzwerkweites Management und zukünftiger Unterstützung für Hardware-Steuerung bietet AstroWarp eine robuste und verlässliche Lösung für die Geräteverwaltung sowie für sichere und stabile Netzwerke.

    Zum Einrichten von AstroWarp lesen Sie bitte [AstroWarp](../../interface_guide/astrowarp.md).

    **Hinweis:** Bitte aktualisieren Sie Spitz Plus auf Firmware v4.8 oder höher, um AstroWarp zu verwenden.

## VPN {#vpn}

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Spitz Plus unterstützt OpenVPN und WireGuard.

=== "OpenVPN"

    Spitz Plus und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Spitz Plus und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

## Anwendungen {#applications}

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen hinzufügt und so dessen Anpassung und Erweiterung ermöglicht.

    Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dabei wird ein Domainname der dynamischen öffentlichen IP-Adresse Ihres Routers zugeordnet, sodass Sie ohne statische IP-Adresse aus der Ferne auf Ihr Netzwerk zugreifen können.

    Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, die es mehreren Benutzern und Geräten ermöglicht, über ein Netzwerk auf Dateien zuzugreifen und sie gemeinsam zu nutzen.

    Zum Einrichten von Network Storage lesen Sie bitte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist ein Drittanbieter-Tool, das Werbung und Tracking blockiert, um Sie zu schützen. Wie Sie AdGuard Home aktivieren, erfahren Sie unter [AdGuard Home](../../interface_guide/adguardhome.md).

=== "Parental Control"

    Parental Control ist eine Gruppe von Einstellungen, die Ihnen dabei hilft, die Geräte Ihrer Kinder zu verwalten und zu steuern. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Zum Einrichten von Parental Control lesen Sie bitte [Parental controls](../../interface_guide/parental_control.md).

=== "Tailscale"

    Spitz Plus unterstützt Tailscale ab Firmware v4.7.

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können.

    Zum Einrichten von Tailscale lesen Sie bitte [Tailscale](../../interface_guide/tailscale.md).

=== "eSIM"

    Spitz Plus unterstützt die eSIM-Funktion ab Firmware v4.7.

    Wie Sie eSIM auf Ihrem Gerät einrichten und verwalten, erfahren Sie in [dieser Anleitung](../../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md).

    <iframe width="560" height="315" src="https://www.youtube.com/embed/hyHh8pAxgVw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Netzwerk {#network}

=== "Portweiterleitung"

    Port forwarding ermöglicht es entfernten Servern und Geräten im Internet, auf Geräte in einem privaten Netzwerk zuzugreifen. Zum Einrichten der Portweiterleitung lesen Sie bitte [Port Forwards](../../interface_guide/port_forwarding.md).

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen einrichten können, z. B. Cellular, Repeater und Ethernet. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, kurz für Local Area Network, ist ein Netzwerk, das Computer und Geräte in einem begrenzten geografischen Bereich wie einem Zuhause oder Büro verbindet. Es ermöglicht schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Zum Einrichten von LAN lesen Sie bitte [Lan Tutorial](../../interface_guide/lan.md).

=== "Gastnetzwerk"

    Hier können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, Gateway- und Netmasken-IP-Adressen angeben und Sicherheitseinstellungen wie AP Isolation für das Gastnetzwerk konfigurieren.

    Zum Einrichten des Gastnetzwerks lesen Sie bitte [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    Auf der Seite DNS können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren, die DNS-Einstellungen aller Clients überschreiben und zulassen, dass benutzerdefiniertes DNS VPN-DNS überschreibt. Sie können automatisch von vorgeschalteten Geräten bezogene DNS-Server verwenden oder benutzerdefinierte DNS-Server manuell angeben.

    Zum Einrichten von DNS lesen Sie bitte [DNS](../../interface_guide/dns.md).

=== "Portverwaltung"

    Auf der Seite Port Management können Sie die WAN- und LAN-Ports konfigurieren, die WAN/LAN-Schnittstelle auf Ethernet setzen, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle festlegen und die ausgehandelte Portgeschwindigkeit anzeigen.

    Zum Verwalten der Ethernet-Ports lesen Sie bitte [Port Management](../../interface_guide/ethernet_port.md).


=== "Network Mode"

    Der Netzwerkmodus bezeichnet die Konfigurationseinstellungen, die festlegen, wie sich ein Gerät mit einem Netzwerk verbindet und mit anderen Geräten kommuniziert.

    Zum Einrichten des Netzwerkmodus lesen Sie bitte [Network Mode](../../interface_guide/network_mode.md).

=== "IPv6"

    IPv6, kurz für Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen wesentlich größeren Adressraum und damit nahezu unbegrenzt viele eindeutige IP-Adressen, was für die stetig wachsende Zahl internetfähiger Geräte entscheidend ist.

    Zum Einrichten von IPv6 lesen Sie bitte [IPv6](../../interface_guide/ipv6.md).

---

=== "Drop-in Gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen, die er möglicherweise nicht bietet, darunter AdGuard Home, verschlüsseltes DNS und VPN. Zum Einrichten von Drop-in Gateway lesen Sie bitte [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md).

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches eingesetzt wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Zum Einrichten von IGMP Snooping lesen Sie bitte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Netzwerkbeschleunigung"

    Hardware-Beschleunigung bezeichnet den Einsatz spezialisierter Hardwarekomponenten, um bestimmte Aufgaben effizienter auszuführen als mit allgemeinen CPUs.

    Zum Einrichten der Netzwerkbeschleunigung lesen Sie bitte die Anleitung [Network Acceleration](../../interface_guide/network_acceleration.md).

=== "NAT-Einstellungen"

    Auf der Seite NAT Settings können Sie die Funktionen Full Cone NAT und SIP ALG (Application Layer Gateway) aktivieren oder deaktivieren.

    Zum Einrichten der NAT-Einstellungen lesen Sie bitte [NAT Settings](../../interface_guide/nat_settings.md).

## System {#system}

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der Router-CPU, um die Leistung zu bewerten und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers aktuell genutzt wird, um Ressourcen besser zu verwalten.
    * LED Control: Schalten Sie die LED-Anzeigen des Routers ein oder aus, um die optischen Signale des Geräts anzupassen.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten verfügbar bleibt.
    * Device Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, darunter Uptime, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Geräte-S/N.
    * External Storage: Prüfen Sie den Status externer Speichergeräte, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md){target="_blank"}.

=== "Upgrade"

    Auf der Seite Upgrade können Sie die Firmware Ihres Routers auf die neueste Version aktualisieren, um bessere Leistung, mehr Sicherheit und neue Funktionen zu erhalten. Diese Seite bietet vier Upgrade-Optionen:

    * Firmware Online Upgrade: Prüft automatisch auf dem Server des Herstellers, ob die neueste Firmware-Version verfügbar ist. Wenn eine neuere Version online verfügbar ist, können Sie sie installieren.
    * Firmware Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren, und behalten Sie dabei die Kontrolle über Version und Zeitpunkt des Upgrades.
    * Module Online Upgrade: Prüft automatisch auf dem Server des Herstellers, ob die neueste 4G/5G-Modulversion verfügbar ist. Wenn eine neuere Version online verfügbar ist, können Sie sie installieren.
    * Module Local Upgrade: Laden Sie manuell eine Moduldatei von Ihrem Computer hoch, um das 4G/5G-Modul zu aktualisieren.

    Mit diesen Optionen halten Sie Ihren Router auf dem neuesten Stand und profitieren von aktuellen Verbesserungen und Fehlerbehebungen.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md){target="_blank"}.

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie verschiedene Routerfunktionen anhand eines festgelegten Zeitplans automatisieren und so Komfort und Effizienz erhöhen. Zu den wichtigsten Funktionen auf dieser Seite gehören:

    * LED Display Schedule: Legen Sie einen Zeitplan fest, um die LED-Anzeigen des Routers automatisch ein- oder auszuschalten und so die Lichtemission zu bestimmten Zeiten zu reduzieren.
    * Schedule Reboot: Konfigurieren Sie Ihren Router so, dass er in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität aufrechtzuerhalten.
    * Wi-Fi Status Schedule: Legen Sie einen Zeitplan fest, um das 5GHz-/2.4GHz-Wi-Fi-Band zu steuern und Verfügbarkeit sowie Stromverbrauch besser zu verwalten.

    Diese Zeitplanoptionen geben Ihnen mehr Kontrolle über den Betrieb Ihres Routers und helfen dabei, ihn an Ihre Anforderungen und Vorlieben anzupassen.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md){target="_blank"}.

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle Zeitpläne, Protokolle und Systemereignisse präzise mit Ihrer Ortszeit versehen werden. Diese Einstellung ist wichtig für genaue Aufzeichnungen und die korrekte Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md){target="_blank"}.

---

=== "Log"

    Auf der Seite Log erhalten Sie Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und so die Fehlerbehebung sowie Leistungsüberwachung unterstützen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle von Systemereignissen und -aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, die bei der Diagnose kritischer Probleme helfen.
    * Cloud Log: Protokolle zu Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern dieser vom Router genutzt wird, mit Informationen zu Webverkehr und Serverbetrieb.

    Zusätzlich verfügt die Seite über die Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders hilfreich bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md){target="_blank"}.

=== "Security"

    Auf der Seite Security können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite enthält Optionen für:

    * Admin Password: Legen Sie das Passwort für die Administrationsoberfläche des Routers fest oder ändern Sie es, damit nur autorisierte Benutzer Einstellungen ändern können.
    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten in Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche aus entfernten Standorten über das Internet, um die Sicherheit vor externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports am Router geöffnet sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch verbundene Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen, wodurch alle benutzerdefinierten Konfigurationen gelöscht werden. Dabei wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Das ist hilfreich, um hartnäckige Probleme zu beheben oder mit der Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md){target="_blank"}.

=== "Advanced Settings"

    Auf der Seite Advanced Settings erhalten erfahrene Benutzer über die OpenWrt-LuCI-Oberfläche Zugriff auf erweiterte Konfigurationsoptionen, um Routereinstellungen und Funktionen über die grundlegenden Oberflächenoptionen hinaus fein abzustimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen und weitere Informationen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md){target="_blank"}.
