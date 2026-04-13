# So richten Sie VPN-Verschleierung auf GL.iNet-Routern ein



## Was ist VPN-Verschleierung?



VPN-Verschleierung ist eine Technik, mit der VPN-Datenverkehr so getarnt wird, dass er wie normaler Internetverkehr aussieht. Das hilft Benutzern, Netzwerkeinschränkungen und Zensur zu umgehen, insbesondere in Regionen mit strengen Internetvorgaben.



- Sie verschleiert die Merkmale von VPN-Datenverkehr, damit dieser von ISPs, Firewalls oder Deep Packet Inspection (DPI) nicht erkannt wird.



- Sie lässt Ihre VPN-Verbindung wie normalen Webverkehr aussehen und verbessert dadurch die Verbindungsstabilität und Erfolgsrate in eingeschränkten Netzwerken.



## Was ist AmneziaWG?



AmneziaWG ist ein auf WireGuard basierendes VPN-Protokoll mit integrierter Datenverkehrsverschleierung. Es behält die zentralen Vorteile von WireGuard bei, etwa hohe Geschwindigkeit, schlankes Design und geringe Latenz, und ergänzt diese um ein spezielles Verschleierungsmodul. Dieses Modul verbirgt VPN-Verkehrsmuster effektiv und hilft sowohl Privat- als auch Geschäftsanwendern dabei, ihre Online-Privatsphäre zu schützen, regionale Einschränkungen zu umgehen und Verbindungsabbrüche durch strenge Netzwerkkontrollen zu vermeiden.



AmneziaWG ist mit einer Vielzahl von Geräten kompatibel, darunter Windows, macOS, iOS, Android, Linux und Router, und bietet in allen Einsatzszenarien zuverlässige verschleierte VPN-Verbindungen.



Derzeit unterstützen mehrere GL.iNet-Router (z. B. **Brume 3**, **Flint 3**, **Flint 2** und **Beryl AX**) das AmneziaWG-Protokoll in ausgewählten Firmware-Versionen. Die vollständige offizielle Unterstützung wird mit Firmware-Version 4.9 verfügbar sein und anschließend schrittweise für weitere Modelle eingeführt.



## Schnelleinrichtung



Im Folgenden finden Sie zwei typische Szenarien zum Einrichten der AmneziaWG-VPN-Verschleierung auf GL.iNet-Routern.



### Szenario 1. Verwendung von zwei GL.iNet-Routern



In diesem Szenario werden zwei GL.iNet-Router verwendet, um über das AmneziaWG-Protokoll eine VPN-Verschleierungsverbindung herzustellen.



- **Brume 3 (GL-MT5000)**: Fungiert als VPN-Server für zu Hause.

- **Beryl AX (GL-MT3000)**: Fungiert als tragbarer VPN-Client für unterwegs.



#### VPN-Server einrichten



1. Melden Sie sich am Web-Admin-Panel des Brume 3 an.



    Verbinden Sie ein Gerät (z. B. Ihren Laptop oder PC) per Ethernet-Kabel mit dem LAN-Port des Brume 3. Öffnen Sie einen Browser und geben Sie die Standard-Admin-Adresse ein (in der Regel `192.168.8.1`). Melden Sie sich anschließend mit Ihrem Admin-Passwort an.



2. Schließen Sie die Ersteinrichtung des Brume 3 für den Internetzugang ab.



    Wenn der Brume 3 als primärer Router verwendet wird, verbinden Sie seinen WAN-Port mit dem vorgelagerten Netzwerk, z. B. einem ISP-Modem.



    Wenn er nicht als primärer Router verwendet wird (d. h. wenn ein anderes vorgeschaltetes Gerät, z. B. ein ISP-Router, als primärer Router fungiert), ist auf Ihrem primären Router eine **Portweiterleitung** erforderlich. Weitere Informationen finden Sie unter [diesem Link](how_to_set_up_port_forwarding.md).



3. DDNS aktivieren (optional).



    Aktivieren Sie die DDNS-Funktion, wenn Ihre öffentliche IP nicht statisch, sondern dynamisch ist.



    Navigieren Sie in der linken Seitenleiste zu **APPLICATIONS** -> **Dynamic DNS**. Aktivieren Sie **Enable DDNS**, stimmen Sie den **Terms of Service & Privacy Policy** zu und klicken Sie dann auf **Apply**.



    ![enable ddns](https://static.gl-inet.com/docs/router/en/4/interface_guide/ddns/enable_ddns.png){class="glboxshadow"}



4. VPN-Verschleierung aktivieren.



    Navigieren Sie in der linken Seitenleiste zu **VPN** > **WireGuard Server** -> Registerkarte **Configurations**, aktivieren Sie **Enable Obfuscation** und klicken Sie dann auf **Apply**.



    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation1.png){class="glboxshadow"}



    Sie können die Verschleierungsparameter bei Bedarf anpassen. Wir empfehlen, die Standardeinstellungen beizubehalten.



    ![enable obfuscation](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_obfuscation2.png){class="glboxshadow"}



5. Konfigurationsdatei exportieren.



    Wechseln Sie auf der Seite **WireGuard Server** zur Registerkarte **Profiles** und klicken Sie auf **Add**, um eine Konfigurationsdatei zu erstellen, mit der sich Beryl AX verbinden kann.



    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles1.png){class="glboxshadow"}



    Legen Sie einen aussagekräftigen Namen fest (z. B. Reiserouter) und klicken Sie dann auf **Apply**.



    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/add_profiles2.png){class="glboxshadow"}



    Klicken Sie im Pop-up-Fenster auf **Export**, um die Konfiguration lokal herunterzuladen. Sie wird später verwendet.



    ![add profiles](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/wg_config_qrcode.png){class="glboxshadow"}



6. VPN-Server starten.



    Klicken Sie oben auf der Seite **WireGuard Server** auf die Schaltfläche **Start**, um den Server zu starten.



    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start1.png){class="glboxshadow"}



    Damit ist Ihr VPN-Server mit aktivierter AmneziaWG-Verschleierung eingerichtet. Sie können sich jetzt über die AmneziaWG-App oder einen GL.iNet-Router mit Firmware-Unterstützung für AmneziaWG-Verschleierung mit diesem VPN-Server auf dem Brume 3 verbinden.



    **Hinweis: Clients, die AmneziaWG-Verschleierung nicht unterstützen, können keine Verbindung herstellen.**



    ![server start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_start2.png){class="glboxshadow"}



#### VPN-Client einrichten



1. Melden Sie sich am Web-Admin-Panel des Beryl AX an.



    Verbinden Sie ein Gerät (z. B. Ihren Laptop oder PC) per Ethernet-Kabel mit dem WLAN oder LAN-Port des Beryl AX. Öffnen Sie einen Browser und geben Sie die Standard-Admin-Adresse ein (in der Regel `192.168.8.1`). Melden Sie sich anschließend mit Ihrem Admin-Passwort an.



2. Schließen Sie die Ersteinrichtung des Beryl AX für den Internetzugang ab.



    **Tipp**: Verbinden Sie den Beryl AX bitte mit einem anderen Netzwerk als dem Brume 3. Sie können beispielsweise einen mobilen Hotspot aktivieren, damit sich der Beryl AX damit verbindet.



3. Konfigurationsdatei hochladen.



    Navigieren Sie in der linken Seitenleiste zu **VPN** > **WireGuard Client**. Fügen Sie eine neue Gruppe hinzu und vergeben Sie einen aussagekräftigen Namen (z. B. Heimrouter).



    ![client add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_add_group.png){class="glboxshadow"}



    Laden Sie auf der rechten Seite die zuvor exportierte Konfigurationsdatei hoch.



    ![client upload file](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_upload_file.png){class="glboxshadow"}



    Klicken Sie nach dem Hochladen und der erfolgreichen Überprüfung der Konfigurationsdatei auf **Apply**.



    ![client uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_uploaded.png){class="glboxshadow"}



    Die Seite wird aktualisiert und zeigt dann eine Konfigurationsdatei in der Liste an.



4. VPN-Verbindung starten.



    Klicken Sie auf das Symbol mit den drei Punkten und wählen Sie dann **Start**.



    ![client start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_start.png){class="glboxshadow"}



    Warten Sie etwa 1 Minute. Wenn die Statusanzeige grün wird, wurde die VPN-Verbindung erfolgreich hergestellt.



    ![client connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_connected.png){class="glboxshadow"}



    Wechseln Sie zum **VPN Dashboard**. Dort sehen Sie, dass der Beryl AX mit dem Heimrouter Brume 3 verbunden ist.



    ![client dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_home.png){class="glboxshadow"}



5. Gegenprüfung (optional).



    Melden Sie sich am Web-Admin-Panel des Brume 3 an und navigieren Sie zu **VPN** -> **WireGuard Server**. Dort sehen Sie ebenfalls einen Online-Client, nämlich den Beryl AX, der aktuell mit diesem VPN-Server auf dem Brume 3 verbunden ist.



    ![server online client](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/server_online_client.png){class="glboxshadow"}



    Die VPN-Verbindung ist damit abgeschlossen. Alle Geräte am Beryl AX greifen jetzt über das Gateway des Brume 3 auf das Internet zu, wodurch eine VPN-Verschleierungsverbindung ermöglicht wird.



### Szenario 2. Verwendung eines einzelnen GL.iNet-Routers



In diesem Szenario wird ein einzelner GL.iNet-Router **Brume 3 (GL-MT5000)** als VPN-Client verwendet, um sich mit einem AmneziaVPN-Server zu verbinden.

In diesem Fall müssen Sie keinen eigenen Server einrichten. Laden Sie einfach eine AmneziaWG-Konfigurationsdatei von der [offiziellen Amnezia-Website](https://amnezia.org/){target="_blank"} oder von einem VPN-Dienstanbieter herunter, der AmneziaWG integriert, und laden Sie die Datei dann auf Ihren GL.iNet-Router hoch. Danach können Sie eine VPN-Verbindung mit aktivierter Verschleierung herstellen.


#### Konfiguration herunterladen



<u>Option 1</u>: Laden Sie eine Konfiguration von Amnezia Official herunter (Premium-Abonnement erforderlich).

1. Melden Sie sich mit Ihrem Subscription Key beim [Amnezia Premium Dashboard](https://cp.amnezia.org/en/login){target="_blank"} an.


    ![amnezia login](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_login.png){class="glboxshadow"}



2. Wechseln Sie im Amnezia Dashboard zu **Connection Assets** -> **Configuration Files**, wählen Sie ein Land aus und laden Sie eine Konfigurationsdatei lokal herunter, damit Sie sie später verwenden können.



    ![amnezia config](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/amnezia_config.png){class="glboxshadow"}

<u>Option 2</u>: Laden Sie eine Konfiguration von einem anderen VPN-Anbieter herunter, der AmneziaWG integriert.

Nehmen Sie StarVPN als Beispiel.

1. Rufen Sie die Optionen des [Tarifplans](https://www.starvpn.com/#pricing){target="_blank"} von StarVPN auf und wählen Sie einen VPN-Tarif, der zu Ihren Anforderungen passt. Sie können sich beim Checkout oder direkt [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"} für ein StarVPN-Konto registrieren.

2. Melden Sie sich im [StarVPN Dashboard](https://www.starvpn.com/dashboard){target="_blank"} an, suchen Sie **VPN Configuration** und klicken Sie auf **AmneziaWG Config**, um die Konfigurationsdatei herunterzuladen.

    ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_starvpn.png){class="glboxshadow"}

3. Die Konfiguration kann eine IPv6-Adresse enthalten. Um Kompatibilitäts- und Verbindungsprobleme zu vermeiden, öffnen Sie die `.conf`-Datei und entfernen Sie die IPv6-Adresse wie unten gezeigt.

    ![starvpn remove ipv6](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/awg_remove_ipv6.png){class="glboxshadow"}

    Folgen Sie anschließend den nachstehenden Schritten, um den VPN-Client einzurichten.


#### VPN-Client einrichten



1. Melden Sie sich am Web-Admin-Panel des Brume 3 an.



    Verbinden Sie ein Gerät (z. B. Ihren Laptop oder PC) per Ethernet-Kabel mit dem LAN-Port des Brume 3. Öffnen Sie einen Browser und geben Sie die Standard-Admin-Adresse ein (in der Regel `192.168.8.1`). Melden Sie sich anschließend mit Ihrem Admin-Passwort an.



2. Schließen Sie die Ersteinrichtung des Brume 3 für den Internetzugang ab.



3. Konfigurationsdatei hochladen.



    Navigieren Sie in der linken Seitenleiste zu **VPN** > **WireGuard Client**. Fügen Sie eine neue Gruppe hinzu und vergeben Sie einen aussagekräftigen Namen (z. B. AmneziaVPN).



    ![client amnezia add a group](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_add_group.png){class="glboxshadow"}



    Laden Sie auf der rechten Seite die zuvor exportierte AmneziaVPN-Konfigurationsdatei hoch.



    ![client amnezia upload](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_upload.png){class="glboxshadow"}



    Klicken Sie nach dem Hochladen und der erfolgreichen Überprüfung der Konfigurationsdatei auf **Apply**.



    ![client amnezia uploaded](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_uploaded.png){class="glboxshadow"}



    Die Seite wird aktualisiert und zeigt dann eine Konfigurationsdatei in der Liste an.



4. VPN-Verbindung starten.



    Klicken Sie auf das Symbol mit den drei Punkten und wählen Sie dann **Start**.



    ![client amnezia start](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_start.png){class="glboxshadow"}



    Warten Sie etwa 1 Minute. Wenn die Statusanzeige grün wird, wurde die VPN-Verbindung erfolgreich hergestellt.



    ![client amnezia connected](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_amnezia_connected.png){class="glboxshadow"}



    Wechseln Sie zum **VPN Dashboard**. Dort sehen Sie, dass der Brume 3 mit einem AmneziaVPN-Server verbunden ist.



    ![client amnezia dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/vpn_obfuscation/client_dashboard_amnezia.png){class="glboxshadow"}



Die VPN-Verbindung ist damit abgeschlossen. Alle Geräte am Brume 3 greifen jetzt über den AmneziaVPN-Server auf das Internet zu, wodurch eine VPN-Verschleierungsverbindung ermöglicht wird.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
