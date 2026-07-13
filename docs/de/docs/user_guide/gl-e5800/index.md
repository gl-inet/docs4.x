# Mudi 7 (GL-E5800) Benutzerhandbuch

## Produktübersicht

Mudi 7 ist ein tragbarer 5G-NR-Wi-Fi-7-Reiserouter für Vielreisende und Geschäftsanwender, der zuverlässige private Netzwerke bereitstellt, um Daten vor Cyberbedrohungen zu schützen. Er bietet 5G-Hochgeschwindigkeit, automatisches Umschalten zwischen zwei SIM-Karten (Failover) sowie Wi-Fi 7 mit 320-MHz-Kanälen und 4K QAM für stabile und schnelle Verbindungen. So werden schnelle Downloads, 4K-Streaming und verzögerungsfreie Videokonferenzen auch in stark frequentierten Bereichen unterstützt.

Dank des Touchscreens können Sie mit dem Mudi 7 die Datennutzung in Echtzeit, die Signalstärke, verbundene Geräte und Client-Geschwindigkeiten überwachen und Einstellungen per Fingertipp anpassen, für eine intuitive und unkomplizierte Bedienung.

![gl-e5800 overview](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/gl-e5800_overview.png){class="glboxshadow"}

## Lieferumfang

- 1 x Mudi 7 (GL-E5800)
- 1 x Akkupack
- 1 x 10-Gbit/s-USB-C-Kabel
- 1 x Reisetasche
- 1 x Benutzerhandbuch

![package contents](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/unboxing.png){class="glboxshadow"}

Sehen Sie sich unten das Unboxing-Video von Mudi 7 an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sCEIReC70Fw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## So richten Sie Mudi 7 ein

Sehen Sie sich dieses Einrichtungsvideo an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/6xg8I0ohAMM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### 1. SIM-Karte einsetzen

Setzen Sie Nano-SIM-Karte(n) in Ihren Mudi 7 ein. Wenn Sie lieber eSIM verwenden möchten, überspringen Sie diesen Schritt und fahren Sie mit Schritt 2 fort.

Nutzen Sie zuerst die kleine Kerbe unten rechts an der Rückabdeckung als Hebelpunkt. Hebeln Sie entlang der Fuge, um einen Spalt zu schaffen, öffnen Sie dann die Rückabdeckung und nehmen Sie den Akku des Mudi 7 heraus.

![small notch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/notch.png){class="glboxshadow"}

![remove battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery1.png){class="glboxshadow"}

Setzen Sie als Nächstes die Nano-SIM-Karte(n) ein. Wenn Sie nur eine Karte verwenden, nutzen Sie bevorzugt SIM 1.

![sim slots](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/sim-slots.png){class="glboxshadow"}

Setzen Sie abschließend den Akku wieder ein und bringen Sie die Abdeckung wieder an.

![restore battery](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/battery2.png){class="glboxshadow"}

### 2. Einschalten

Halten Sie die Ein-/Aus-Taste **3 Sekunden** lang gedrückt oder schließen Sie ein Netzteil an.

![power on](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/first_time_setup/power-button.png){class="glboxshadow"}

### 3. Grundeinstellungen

Folgen Sie den Anweisungen auf dem Bildschirm, um die Grundeinstellungen zu konfigurieren, darunter **Bildschirm-Passcode**, **Admin-Passwort**, **Wi-Fi-Name**, **Wi-Fi-Passwort** und **Frequenzbänder**.

**Tipp:** Das Standard-Admin-Passwort besteht aus den letzten 9 Zeichen der S/N des Geräts, gefolgt von einem `#`. Sie können dieses Standard-Passwort verwenden oder ein eigenes festlegen.

### 4. Internet einrichten

Richten Sie Mudi 7 mit einer der unterstützten Internetverbindungsmethoden ein: Cellular, Ethernet, Repeater, Tethering und USB Ethernet. Wenn Sie die Funktion [Multi-WAN](../../interface_guide/multi-wan.md) verwenden möchten, richten Sie bitte mehr als eine Internetverbindung ein.

=== "Cellular"

    ![cellular connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_cellular.jpg){class="glboxshadow"}

    Mudi 7 verfügt über eine **integrierte eSIM** und **zwei Nano-SIM-Steckplätze**. Sie können eine Internetverbindung herstellen, indem Sie ein eSIM-Paket kaufen (ohne physische SIM-Karte) oder Ihre Nano-SIM-Karten einsetzen, um das 5G-Mobilfunknetz zu nutzen.

    **eSIM einrichten**:

    1. Gehen Sie auf dem Touchscreen zu **Cellular** -> **SIM Card Switch** und aktivieren Sie den Schalter, um die **eSIM** zu aktivieren.

        ![enable esim](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/lcd_enable_esim.png){class="glboxshadow" width="590"}

    2. Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **INTERNET** -> **Cellular** -> **eSIM Management**.

        ![esim management](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/esim_management.png){class="glboxshadow" width="590"}

    3. Klicken Sie im Pop-up-Fenster unten auf **Add eSIM Profile**.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile1.png){class="glboxshadow" width="590"}

        Laden Sie Ihr eSIM-Profil per QR-Code oder Aktivierungscode hoch und klicken Sie auf **Install**. Beachten Sie, dass die meisten eSIM-Profile nur einmal heruntergeladen und hinzugefügt werden können.

        ![add esim profile](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/add_esim_profile2.png){class="glboxshadow"}

        **Tipp**: Wenn Sie noch kein eSIM-Profil gekauft haben, können Sie eines im **eSIM Profile Recommended Store** erwerben.

        ![recommended store](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/recommended_store.png){class="glboxshadow" width="590"}

    4. Wechseln Sie nach dem Hochladen zu **Cellular** und klicken Sie auf **SIM Card Switch**.

        ![sim card switch](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/sim_card_switch.png){class="glboxshadow" width="590"}

        Wählen Sie im Pop-up-Fenster **eSIM** als aktive SIM-Karte aus und klicken Sie dann auf **Apply**.

        ![active sim card](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/esim/active_sim_card.png){class="glboxshadow"}

    5. Der Router beginnt, sich über dieses eSIM-Profil zu verbinden. Bitte warten Sie und prüfen Sie, ob die Verbindung erfolgreich hergestellt wird.

    **Nano-SIM einrichten**:

    1. Entfernen Sie die Rückabdeckung, nehmen Sie den Akku heraus, setzen Sie Ihre Nano-SIM-Karte in den Steckplatz ein und installieren Sie anschließend den Akku wieder.

    2. Der Router beginnt automatisch, sich über diese Nano-SIM-Karte zu verbinden. Bitte warten Sie und prüfen Sie, ob die Verbindung erfolgreich hergestellt wird.

    Sobald die Internetverbindung erfolgreich hergestellt wurde, werden die Signalbalken und der Mobilfunkstatus oben rechts auf dem Touchscreen angezeigt. Sie können die Verbindungsdetails auch im Web-Admin-Panel prüfen.

    Weitere Informationen finden Sie unter [Connect to the Internet via cellular](../../interface_guide/internet_cellular.md).

    !!! note

        1. Die integrierte eSIM und SIM 2 schließen sich gegenseitig aus und können nicht gleichzeitig aktiviert werden. Die eSIM ist standardmäßig deaktiviert. Wenn Sie die eSIM aktivieren, funktioniert SIM 2 nicht, selbst wenn eine SIM-Karte eingesetzt ist.
        2. Da Mudi 7 über eine integrierte eSIM verfügt, wird eine SIMPoYo eSIM-Physikkarte auf dem Mudi 7 als normale SIM-Karte ohne eSIM-Funktion erkannt.

=== "Ethernet"

    ![ethernet connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_ethernet.jpg){class="glboxshadow"}

    1. Verbinden Sie den Ethernet-Port Ihres Mudi 7 per Ethernet-Kabel mit einer vorgelagerten Netzwerkquelle, z. B. einem ISP-Modem, Netzwerkswitch oder einer Ethernet-Wanddose.
    2. Gehen Sie auf dem Touchscreen oder im Web-Admin-Panel zu **Network** -> **Ethernet Ports**, setzen Sie die Portrolle auf **WAN** und klicken Sie auf **Apply**.

        ![touchscreen ethernet wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-ethernet-wan.png){class="glboxshadow"}

    3. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint oben rechts auf dem Touchscreen ein Ethernet-Port-Symbol. Die Verbindungsdetails können Sie auch im Web-Admin-Panel prüfen.

    Detaillierte Anweisungen finden Sie unter [Über ein Ethernet-Kabel eine Verbindung zum Internet herstellen](../../interface_guide/internet_ethernet.md).

=== "Repeater"

    ![repeater connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_repeater.jpg){class="glboxshadow"}

    1. Gehen Sie auf dem Touchscreen oder im Web-Admin-Panel zu **Internet** -> **Repeater** und klicken Sie auf **Connect**. Mudi 7 beginnt dann mit der Suche nach verfügbaren Wi-Fi-Netzwerken.
    2. Wählen Sie das Wi-Fi-Netzwerk aus, das Mudi 7 erweitern soll.
    3. Geben Sie das Passwort ein und klicken Sie auf **Apply**.
    4. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint oben rechts auf dem Touchscreen ein Wi-Fi-Symbol. Die Verbindungsdetails können Sie auch im Web-Admin-Panel prüfen.

    Detaillierte Anweisungen finden Sie unter [Über ein vorhandenes Wi-Fi-Netzwerk eine Verbindung zum Internet herstellen](../../interface_guide/internet_repeater.md).

=== "Tethering"

    ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_tethering.jpg){class="glboxshadow"}

    1. Verbinden Sie Ihr Mobilgerät, z. B. ein Smartphone oder USB-Dongle, per USB-Kabel mit dem USB-C-Port des Mudi 7.
    2. Öffnen Sie auf Ihrem Mobilgerät die Einstellungen und aktivieren Sie **USB Tethering**. Wenn Sie ein iPhone verwenden, tippen Sie bei entsprechender Aufforderung auf **Trust This Device**.
    3. Mudi 7 verbindet sich anschließend automatisch mit Ihrem Gerät. Falls keine Verbindung hergestellt wird, wiederholen Sie die obigen Schritte oder melden Sie sich im Web-Admin-Panel an und prüfen Sie die Tethering-Verbindung auf der Seite INTERNET.
    4. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheint oben rechts auf dem Touchscreen ein Kettensymbol. Die Verbindungsdetails können Sie auch im Web-Admin-Panel prüfen.

    Detaillierte Anweisungen finden Sie unter [Über USB-Tethering eine Verbindung zum Internet herstellen](../../interface_guide/internet_tethering.md).

=== "USB Ethernet"

    ![usb ethernet](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/e5800_usb_ethernet.png){class="glboxshadow"}

    Mudi 7 ist mit einem **OTG-fähigen** USB-C-Port ausgestattet, sodass Sie für Dual-Ethernet-WAN einen zweiten Ethernet-Port hinzufügen können. Dafür wird ein **separat erhältlicher USB-C-auf-Ethernet-Adapter** benötigt.

    <small>*USB OTG (On-The-Go) ist ein USB-Standard, der kompatiblen Geräten wie Routern erlaubt, zwischen Host- und Peripherierolle zu wechseln, sodass direkte Datenübertragung und Stromversorgung ohne separates Host-Gerät möglich sind.</small>

    1. Verbinden Sie eine vorgelagerte Netzwerkquelle, z. B. ein ISP-Modem, einen Netzwerkswitch oder eine Ethernet-Wanddose, über einen USB-C-auf-Ethernet-Adapter mit dem USB-C-Port des Mudi 7.
    2. Gehen Sie auf dem Touchscreen oder im Web-Admin-Panel zu **Network** -> **Ethernet Ports** -> **USB Ethernet Port**, setzen Sie die Portrolle auf **WAN** und klicken Sie auf **Apply**.

        ![touchscreen usb eth wan](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/ts-usb-eth-wan.png){class="glboxshadow"}

    3. Mudi 7 verbindet sich anschließend automatisch mit Ihrem Gerät. Falls keine Verbindung hergestellt wird, wiederholen Sie die obigen Schritte oder melden Sie sich im Web-Admin-Panel an und prüfen Sie die USB-Ethernet-Verbindung auf der Seite INTERNET.
    4. Sobald die Internetverbindung erfolgreich hergestellt wurde, erscheinen oben rechts auf dem Touchscreen ein USB-Symbol und ein Ethernet-Port-Symbol. Die Verbindungsdetails können Sie auch im Web-Admin-Panel prüfen.

## Firmware-Upgrade

!!! note "Vor dem Upgrade bitte beachten:"

    1. Um Ihre Mudi-7-Konfigurationen zu behalten, wählen Sie auf der Upgrade-Seite **Keep Settings**.
    2. Wählen Sie **Keep Settings** nicht beim Downgrade, da es zu Kompatibilitätsproblemen kommen kann.
    3. Für ein Firmware-Upgrade wird eine gewisse Datenmenge verbraucht. Wenn Ihr SIM-Kartentarif ein begrenztes Datenvolumen hat, empfehlen wir, den Router über andere Methoden mit dem Internet zu verbinden (z. B. Repeater, USB Tethering usw.), um zusätzlichen Datenverbrauch zu vermeiden.

Sie können die Firmware von Mudi 7 über den Touchscreen oder das Web-Admin-Panel aktualisieren.

### Upgrade über den Touchscreen

1. Verbinden Sie Ihren Mudi 7 mit dem Internet.

2. Sobald die Verbindung hergestellt ist, sucht das System automatisch nach verfügbaren Firmware-Updates. Wenn eine neue Firmware verfügbar ist, erscheint eine Meldung auf dem Bildschirm. Klicken Sie im Pop-up-Fenster auf **Go to Upgrade**, um fortzufahren.

   ![go to upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade1.png){class="glboxshadow" width="300"}

3. Wenn das Pop-up-Fenster nicht erscheint, tippen Sie auf dem Startbildschirm auf **More** -> **About Device** -> **Version & Upgrade** -> **Download & Upgrade** und folgen Sie dann den Anweisungen auf dem Bildschirm, um die Firmware zu aktualisieren.

   ![download & upgrade](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/internet/screen_upgrade2.png){class="glboxshadow" width="300"}

### Upgrade über das Web

1. Online-Upgrade

   Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **SYSTEM** -> **Upgrade** -> **Firmware Online Upgrade**, um die Firmware Ihres Routers zu aktualisieren.

   Weitere Informationen finden Sie [hier](../../interface_guide/upgrade.md#online-upgrade).

2. Lokales Upgrade

   Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **SYSTEM** -> **Upgrade** -> **Firmware Local Upgrade**, um die Firmware Ihres Routers zu aktualisieren.

   Weitere Informationen finden Sie [hier](../../interface_guide/upgrade.md#local-upgrade).

## Werkseinstellungen wiederherstellen

Es gibt drei Möglichkeiten, Ihren Mudi 7 zurückzusetzen: direkt über den Touchscreen, mit der Reset-Taste und über das Web-Admin-Panel.

**Hinweis**: Bevor Sie den Reset durchführen, stellen Sie sicher, dass Mudi 7 vollständig hochgefahren ist. Drücken Sie die Reset-Taste NICHT direkt nach dem Einschalten, da sonst der U-Boot-Failsafe-Modus ausgelöst werden kann.

Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3Kx_StIFLqo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Über den Touchscreen zurücksetzen

1. Tippen Sie auf der Startseite auf **More**.

   ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset1.png){class="glboxshadow" width="300"}

2. Scrollen Sie auf der Seite **More** ganz nach unten und tippen Sie auf **Reset**.

   ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset2.png){class="glboxshadow" width="300"}

3. Tippen Sie zur Bestätigung erneut auf **Reset**. Der Router beginnt mit dem Zurücksetzen und startet anschließend neu.

   ![LCD reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/lcd_reset3.png){class="glboxshadow" width="300"}

### Über die Taste zurücksetzen

1. Entfernen Sie die Rückabdeckung. Dort finden Sie die Reset-Taste wie unten gezeigt.

   ![tethering connection](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/reset-button.png){class="glboxshadow"}

2. Führen Sie je nach Bedarf einen Soft Reset oder einen Werksreset durch.

   - **Soft Reset**: Wenn Sie die Netzwerkverbindung neu starten möchten, ohne Daten zu löschen, halten Sie die Reset-Taste **4 Sekunden** lang gedrückt und lassen Sie sie dann los, um Ihr Netzwerk zu reparieren. Achten Sie währenddessen auf die Hinweise auf dem Bildschirm und folgen Sie den Anweisungen. Dadurch wird die Netzwerkschnittstelle neu gestartet, während Wi-Fi-Einstellungen, VPN-Konfigurationen (deaktiviert), Systemeinstellungen usw. erhalten bleiben. Wenn Wi-Fi deaktiviert wurde, stellt ein Soft Reset Wi-Fi wieder auf den standardmäßig aktivierten Zustand zurück. Ein Soft Reset kann auch verwendet werden, um das Gerät schnell vom Nicht-Router-Modus in den Router-Modus zu wechseln.

   - **Werksreset**: Halten Sie die Reset-Taste **10 Sekunden** lang gedrückt und lassen Sie sie dann los, um einen Hard Reset durchzuführen. Achten Sie währenddessen auf die Hinweise auf dem Bildschirm und folgen Sie den Anweisungen. Dadurch werden alle Ihre Einstellungen gelöscht. Bitte gehen Sie vorsichtig vor.

### Über das Web zurücksetzen

1. Melden Sie sich im Web-Admin-Panel an und gehen Sie zu **SYSTEM** -> **Reset Firmware**.

2. Klicken Sie auf **Delete All and Reboot**. Der Router beginnt mit dem Zurücksetzen und startet anschließend neu.

   ![web reset](https://static.gl-inet.com/docs/router/en/4/user_guide/gl-e5800/hardware_info/web_reset.png){class="glboxshadow"}

## Anmeldung im Web-Admin-Panel

Sie können sich im Web-Admin-Panel des Mudi 7 anmelden, um weitere Einstellungen zu konfigurieren oder zu prüfen.

Verbinden Sie zunächst ein Gerät, z. B. einen Computer, Laptop oder ein Smartphone, per Wi-Fi, Ethernet-Kabel oder USB-Kabel mit dem Mudi 7.

- **Wi-Fi**
  - <u>QR-Code</u>: Scannen Sie mit Ihrem Gerät den QR-Code auf dem Bildschirm des Mudi 7. Klicken Sie anschließend auf Ihrem Gerät auf „Join“, um die Verbindung herzustellen.
  - <u>Manuell verbinden</u>: Öffnen Sie auf Ihrem Gerät Einstellungen -> WLAN, suchen Sie den Wi-Fi-Netzwerknamen des Mudi 7 in der Liste der verfügbaren Netzwerke und geben Sie das Passwort ein, um sich zu verbinden. Den Standard-Netzwerknamen und das Standard-Passwort finden Sie auf dem Etikett.

- **Ethernet**

  Verbinden Sie Ihr Gerät per Ethernet-Kabel mit dem Ethernet-Port des Mudi 7 (standardmäßig LAN).

- **USB**

  Verbinden Sie Ihr Gerät per USB-Kabel mit dem USB-C-Port des Mudi 7. Über den OTG-fähigen USB-C-Port können Sie im nächsten Schritt auf die WebGUI des Mudi 7 zugreifen.

Öffnen Sie dann einen Webbrowser und geben Sie `192.168.8.1` in die Adressleiste ein, um die Anmeldeseite aufzurufen. Wählen Sie Ihre Sprache aus, legen Sie Ihr Admin-Passwort fest und klicken Sie auf **Apply**.

Anschließend sind Sie im Web-Admin-Panel des Mudi 7 angemeldet.

Im Folgenden finden Sie einen Überblick über die Funktionen im Web-Admin-Panel des Mudi 7.

## WLAN

Auf der Seite Wireless können Sie Einstellungen für die 6-GHz-, 5-GHz- und 2.4-GHz-Wi-Fi-Netzwerke konfigurieren, darunter das Aktivieren von Wi-Fi, das Festlegen der TX-Leistung, das Definieren des Wi-Fi-Namens (SSID), das Aktivieren randomisierter BSSID, die Auswahl des Wi-Fi-Sicherheitsmodus und Passworts sowie die Konfiguration von SSID-Sichtbarkeit, Wi-Fi-Modus, Bandbreite und Kanal.

Informationen zur Einrichtung von Wireless finden Sie unter [Wireless](../../interface_guide/wireless.md).

**Hinweis:** Bei den Wireless-Einstellungen des Mudi 7 gibt es einige Unterschiede im Vergleich zu anderen GL.iNet-Wi-Fi-7-Routern.

1. Aufgrund von Hardware-Beschränkungen des Chipsatzes können 5-GHz- und 6-GHz-Wi-Fi nicht gleichzeitig aktiviert werden.
2. Wenn Repeater aktiviert ist, wird das Gastnetzwerk automatisch deaktiviert.
3. Wie gesetzlich vorgeschrieben, sollten Sie Wi-Fi bei Verwendung im Außenbereich auf den Outdoor-Modus umstellen. Dadurch kann sich die Reichweite verringern. Die Nutzungsumgebung (Indoor oder Outdoor) können Sie oben auf der Seite Wireless umschalten.

## Clients

Auf der Seite Clients werden Informationen zu verbundenen Geräten angezeigt. Für jeden Client werden Name, IP- und MAC-Adressen, Download- und Upload-Geschwindigkeiten sowie das gesamte Datenvolumen angezeigt. Außerdem können Sie den Client blockieren oder weitere Aktionen ausführen.

Informationen zur Einrichtung von Clients finden Sie unter [Clients](../../interface_guide/clients.md).

## Cloud-Dienste

=== "GoodCloud"

    Der Cloud-Management-Dienst GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} bietet eine einfache Möglichkeit, per Fernzugriff auf GL.iNet-Router zuzugreifen und sie zu verwalten.

    Zum Einrichten von GoodCloud lesen Sie bitte [GoodCloud](../../interface_guide/cloud.md).

=== "AstroWarp"

    AstroWarp ist eine fortschrittliche Netzwerkplattform für nahtlose Remote-Vernetzung und Fernverwaltung von Geräten. AstroWarp wurde speziell für die Integration mit GL.iNet-Routern entwickelt und unterstützt ein umfassendes Gerätemanagement über ganze Netzwerke hinweg, einschließlich der Verwaltung über- und untergeordneter Geräte. Mit seinem Fokus auf netzwerkweites Management und zukünftiger Unterstützung für Hardware-Steuerung bietet AstroWarp eine robuste und verlässliche Lösung für die Geräteverwaltung sowie für sichere und stabile Netzwerke.

    Zum Einrichten von AstroWarp lesen Sie bitte [AstroWarp](../../interface_guide/astrowarp.md).

## VPN

Ein VPN (virtuelles privates Netzwerk) erstellt einen sicheren, verschlüsselten Datenverkehr zwischen Ihrem Gerät und dem VPN-Server. Es bietet eine zusätzliche Ebene für Datenschutz und Sicherheit (VPN-Client) und ermöglicht Ihnen den Zugriff auf ein entferntes Netzwerk (VPN-Server). Mudi 7 unterstützt OpenVPN und WireGuard.

=== "OpenVPN"

    Mudi 7 und andere GL.iNet-Router unterstützen das OpenVPN-Protokoll, das hohe Sicherheit bietet. Folgen Sie zum Einrichten von OpenVPN diesen Anleitungen:

    * [So richten Sie einen OpenVPN-Client ein](../../interface_guide/openvpn_client.md)
    * [So richten Sie einen OpenVPN-Server ein](../../interface_guide/openvpn_server.md)

=== "WireGuard"

    Mudi 7 und andere GL.iNet-Router unterstützen das WireGuard-Protokoll, das hohe Geschwindigkeiten und eine komfortable Nutzung bietet. Folgen Sie zum Einrichten von WireGuard diesen Anleitungen:

    * [So richten Sie einen WireGuard-Client ein](../../interface_guide/wireguard_client.md)
    * [So richten Sie einen WireGuard-Server ein](../../interface_guide/wireguard_server.md)

## Netzwerk

=== "Multi-WAN"

    Multi-WAN ist eine Netzwerkfunktion, mit der Sie Ihren Router gleichzeitig mit mehreren Internetverbindungen einrichten können, z. B. Ethernet, Repeater, Tethering, Cellular und USB Ethernet. Wenn Ihre aktuelle Internetverbindung ausfällt, wechselt der Router automatisch zu einer anderen Internetverbindung. So bleibt der Internetzugang stabil und unterbrechungsfrei.

    Zum Einrichten von Multi-WAN lesen Sie bitte [Multi-WAN](../../interface_guide/multi-wan.md).

=== "LAN"

    LAN, kurz für Local Area Network, ist ein Netzwerk, das Computer und Geräte in einem begrenzten geografischen Bereich wie einem Zuhause oder Büro verbindet. Es ermöglicht schnelle Datenübertragung und gemeinsame Ressourcennutzung, sodass Geräte effizient miteinander kommunizieren können.

    Zum Einrichten von LAN lesen Sie bitte [Lan](../../interface_guide/lan.md).

=== "Gastnetzwerk"

    Hier können Sie ein Subnetz innerhalb der privaten IPv4-Adressbereiche 192.168.0.0/16, 172.16.0.0/12 oder 10.0.0.0/8 festlegen, Gateway- und Netmasken-IP-Adressen angeben und Sicherheitseinstellungen wie AP Isolation für das Gastnetzwerk konfigurieren.

    Zum Einrichten des Gastnetzwerks lesen Sie bitte [Guest Network](../../interface_guide/guest_network.md).

---

=== "DNS"

    Auf der Seite DNS können Sie benutzerdefinierte DNS-Server festlegen, den Schutz vor DNS-Rebinding-Angriffen aktivieren und die DNS-Einstellungen aller Clients überschreiben. Außerdem können Sie erlauben, dass benutzerdefiniertes DNS VPN-DNS überschreibt, und den DNS-Servermodus auf automatisch setzen oder DNS-Server der Ethernet-Verbindung manuell angeben.

    Zum Einrichten von DNS lesen Sie bitte [DNS](../../interface_guide/dns.md).

=== "Ethernet Port"

    Auf der Seite Ethernet Port können Sie die Portrolle des Ethernet-Ports festlegen, also ihn als WAN oder LAN verwenden, den MAC-Modus und die MAC-Adresse für die WAN-Schnittstelle ändern und die ausgehandelte Portgeschwindigkeit anzeigen.

    Mudi 7 verfügt über einen einzelnen Ethernet-Port, der standardmäßig als LAN konfiguriert ist. Bei Bedarf können Sie ihn über den Touchscreen oder das Web-Admin-Panel auf WAN umstellen.

    Zum Verwalten der Ethernet-Ports lesen Sie bitte [Ethernet Port](../../interface_guide/ethernet_port.md).

=== "IPv6"

    IPv6, kurz für Internet Protocol Version 6, ist die neueste Version des Internetprotokolls und wurde als Nachfolger von IPv4 entwickelt. Es bietet einen wesentlich größeren Adressraum und damit nahezu unbegrenzt viele eindeutige IP-Adressen, was für die stetig wachsende Zahl internetfähiger Geräte entscheidend ist.

    Zum Einrichten von IPv6 lesen Sie bitte [IPV6](../../interface_guide/network_mode.md).

---

=== "IGMP Snooping"

    IGMP Snooping ist eine Netzwerkoptimierungstechnik, die in Ethernet-Switches eingesetzt wird, um Multicast-Datenverkehr zu verwalten und zu steuern.

    Zum Einrichten von IGMP Snooping lesen Sie bitte [IGMP Snooping](../../interface_guide/igmp_snooping.md).

=== "Network Mode"

    Der Netzwerkmodus bezeichnet die Konfiguration, die festlegt, wie sich ein Gerät mit einem Netzwerk verbindet und mit anderen Geräten kommuniziert.

    Zum Einrichten des Netzwerkmodus lesen Sie bitte [Network Mode](../../interface_guide/network_mode.md).

    **Hinweis:** Mudi 7 unterstützt Router-, Access-Point- und Extender-Modus. Der WDS-Modus wird nicht unterstützt.

=== "Drop-in gateway"

    Drop-in Gateway erweitert die Funktionalität Ihres Hauptrouters um Funktionen wie AdGuard Home, verschlüsseltes DNS und VPN-Client.

    Zum Einrichten von Drop-in Gateway lesen Sie bitte diese Links:

    - [Drop-in Gateway](../../interface_guide/drop-in_gateway.md)
    - [So richten Sie Drop-in Gateway ein](../../tutorials/how_to_set_up_drop_in_gateway.md)

=== "Netzwerkbeschleunigung"

    Netzwerkbeschleunigung kann die CPU-Last reduzieren und die Weiterleitung von Datenpaketen beschleunigen.

    Zum Einrichten der Netzwerkbeschleunigung lesen Sie bitte [Network Acceleration](../../interface_guide/network_acceleration.md).

## Durchflusskontrolle

=== "Parental Control"

    Parental Control hilft Ihnen dabei, die Geräte Ihrer Kinder zu verwalten und zu steuern. Dazu gehören die Begrenzung der Bildschirmzeit und die Einschränkung des Zugriffs auf bestimmte Inhalte.

    Zum Einrichten von Parental Control lesen Sie bitte [Parental Control](../../interface_guide/parental_control.md).

## Sicherheit

=== "Port Forwarding"

    Port forwarding ermöglicht es entfernten Servern und Geräten im Internet, auf Geräte in einem privaten Netzwerk zuzugreifen.

    Zum Einrichten der Portweiterleitung lesen Sie bitte [Port Forwarding](../../interface_guide/port_forwarding.md).

=== "Management Control"

    Mit Management Control können Sie verschiedene Sicherheitseinstellungen konfigurieren, um Ihr Netzwerk und Ihren Router vor unbefugtem Zugriff zu schützen. Diese Seite enthält die folgenden Optionen:

    * Local Access Control: Verwalten und beschränken Sie den Zugriff auf die Routeroberfläche von Geräten in Ihrem lokalen Netzwerk.
    * Remote Access Control: Konfigurieren und beschränken Sie den Zugriff auf die Routeroberfläche aus entfernten Standorten über das Internet, um die Sicherheit vor externen Bedrohungen zu erhöhen.
    * Open Ports on Router: Steuern Sie, welche Ports am Router geöffnet sind, um potenzielle Schwachstellen und unbefugten Zugriff zu begrenzen.

    Diese Einstellungen helfen Ihnen, eine sichere Netzwerkumgebung aufrechtzuerhalten und sowohl Ihren Router als auch verbundene Geräte zu schützen.

    Detaillierte Anweisungen finden Sie unter [Security](../../interface_guide/security.md).

=== "NAT Mode"

    Auf der Seite NAT Mode können Sie die Funktionen Full Cone NAT und SIP ALG aktivieren oder deaktivieren.

    Zum Einrichten der NAT-Einstellungen lesen Sie bitte [NAT Mode](../../interface_guide/nat_settings.md).

## Anwendungen

=== "Plug-ins"

    Ein Plug-in ist eine Softwarekomponente, die einem bestehenden Computerprogramm bestimmte Funktionen oder Erweiterungen hinzufügt und so dessen Anpassung und Erweiterung ermöglicht.

    Zum Einrichten von Plug-ins lesen Sie bitte [Plug-ins](../../interface_guide/plugins.md).

=== "Dynamic DNS"

    Dynamic DNS (DDNS) erkennt und aktualisiert automatisch die mit einer Domain verknüpfte IP-Adresse in Echtzeit. Dies ist besonders nützlich für Benutzer, die für den Zugriff auf ein entferntes Netzwerk eine statische IP-Adresse benötigen.

    Zum Einrichten von Dynamic DNS lesen Sie bitte [Dynamic DNS](../../interface_guide/ddns.md).

=== "Network Storage"

    Network Storage bezeichnet eine zentrale Datenspeicherlösung, die es mehreren Benutzern und Geräten ermöglicht, über ein Netzwerk auf Dateien zuzugreifen und sie gemeinsam zu nutzen.

    Zum Einrichten von Network Storage lesen Sie bitte [Network Storage](../../interface_guide/network_storage.md).

---

=== "AdGuard Home"

    AdGuard Home ist eine netzwerkweite Lösung zum Blockieren von Werbung und Trackern, die als DNS-Server fungiert, um unerwünschte Inhalte auf allen Geräten eines Heimnetzwerks zu filtern.

    Zum Einrichten von AdGuard Home lesen Sie bitte [AdGuard Home](../../interface_guide/adguardhome.md).

=== "ZeroTier"

    ZeroTier ist eine Software-defined-Networking-Lösung, mit der Benutzer sichere virtuelle Netzwerke über das Internet erstellen können, sodass Geräte miteinander verbunden werden, als befänden sie sich im selben lokalen Netzwerk.

    Zum Einrichten von ZeroTier lesen Sie bitte [ZeroTier](../../interface_guide/zerotier.md).

=== "Tailscale"

    Tailscale ist ein VPN-Dienst, mit dem Sie von überall auf Ihre Geräte und Anwendungen zugreifen können.

    Zum Einrichten von Tailscale lesen Sie bitte [Tailscale](../../interface_guide/tailscale.md).

=== "Tor"

    Tor, kurz für The Onion Router, ist ein auf Privatsphäre ausgerichtetes Netzwerk, das anonyme Kommunikation über das Internet ermöglicht. Es leitet den Internetverkehr über eine Reihe von freiwillig betriebenen Servern (Nodes), um den Standort und die Nutzung des Benutzers zu verschleiern und Online-Aktivitäten nur schwer nachvollziehbar zu machen.

    Zum Einrichten von Tor lesen Sie bitte [Tor](../../interface_guide/tor.md).

## System

=== "Overview"

    Die Seite Overview bietet einen umfassenden Überblick über den aktuellen Status und die Leistungsdaten Ihres Routers. Auf dieser Seite können Sie Folgendes anzeigen:

    * CPU Average Load: Überwachen Sie die durchschnittliche Auslastung der Router-CPU, um die Leistung zu bewerten und mögliche Engpässe zu erkennen.
    * Memory Usage: Prüfen Sie, wie viel Arbeitsspeicher Ihres Routers aktuell genutzt wird, um Ressourcen besser zu verwalten.
    * LED Control: Schalten Sie die LED-Anzeigen des Routers ein oder aus, um die optischen Signale des Geräts anzupassen.
    * Flash Usage: Sehen Sie die Auslastung des Flash-Speichers Ihres Routers ein, damit ausreichend Platz für Firmware- und Konfigurationsdaten verfügbar bleibt.
    * Device Info: Greifen Sie auf detaillierte Systeminformationen Ihres Routers zu, darunter Uptime, Hostname, Modell, Architektur, OpenWrt-Version, Kernel-Version, Geräte-ID, Geräte-MAC und Geräte-S/N.
    * External Storage: Prüfen Sie den Status externer Speichergeräte, die mit dem Router verbunden sind, z. B. USB-Laufwerke oder TF-Karten.

    Diese Funktionen liefern wichtige Einblicke und Steuerungsmöglichkeiten, damit Sie den Betrieb Ihres Routers effektiv verwalten und überwachen können.

    Detaillierte Anweisungen finden Sie unter [Overview](../../interface_guide/system_overview.md).

=== "Admin Password"

    Auf der Seite Admin Password können Sie das Passwort für die Administrationsoberfläche des Routers festlegen oder ändern.

    Das Admin-Passwort muss die folgenden Anforderungen erfüllen:

    * Mindestens 10 und höchstens 63 Zeichen.
    * Buchstaben (Groß- und Kleinschreibung wird unterschieden), Zahlen und Symbole ``! @ # $ % ^ & * ( ) _ + - = , . > < | ? / \ [ ] { } : ; " ' ` ~`` sind zulässig.
    * Mindestens zwei der folgenden Kategorien sind erforderlich: Großbuchstaben, Kleinbuchstaben, Zahlen und Symbole.

=== "Upgrade"

    Auf der Seite Upgrade können Sie die Firmware Ihres Routers auf die neueste Version aktualisieren, um bessere Leistung, mehr Sicherheit und neue Funktionen zu erhalten. Diese Seite bietet zwei Upgrade-Optionen:

    * Firmware Online Upgrade: Prüfen Sie automatisch auf die neueste Firmware-Version und installieren Sie sie direkt vom Server des Herstellers, um den Aktualisierungsprozess zu vereinfachen.
    * Firmware Local Upgrade: Laden Sie manuell eine Firmware-Datei von Ihrem Computer hoch, um den Router zu aktualisieren, und behalten Sie dabei die Kontrolle über Version und Zeitpunkt des Upgrades.

    Mit diesen Optionen halten Sie Ihren Router auf dem neuesten Stand und profitieren von aktuellen Verbesserungen und Fehlerbehebungen.

    Detaillierte Anweisungen finden Sie unter [Upgrade](../../interface_guide/upgrade.md).

---

=== "Scheduled Tasks"

    Auf der Seite Scheduled Tasks können Sie Ihren Router so konfigurieren, dass er in festgelegten Intervallen automatisch neu startet, um Leistung und Stabilität aufrechtzuerhalten.

    Detaillierte Anweisungen finden Sie unter [Scheduled Tasks](../../interface_guide/scheduled_tasks.md).

    **Hinweis:** Mudi 7 unterstützt weder einen Zeitplan für die LED-Anzeige noch einen Zeitplan für den Wi-Fi-Status.

=== "Display Management"

    Auf der Seite Display Management können Sie das Touchscreen-Display und die zugehörigen Einstellungen verwalten.

    - Wallpaper: Passen Sie Hintergrundbild und Stil des Wake-Displays an.
    - Brightness: Stellen Sie die Helligkeit des Touchscreens ein. Verwenden Sie den Schieberegler oder geben Sie einen Prozentwert ein, um sie an unterschiedliche Lichtverhältnisse anzupassen.
    - Personalised Signature: Fügen Sie dem Touchscreen einen benutzerdefinierten Text hinzu, um Ihren eigenen Stil zu zeigen oder das Gerät schnell zu identifizieren.
    - Auto Lock: Legen Sie die Verzögerung fest, nach der sich der Bildschirm bei Inaktivität automatisch sperrt. Der Bereich reicht von 15 Sekunden bis 5 Minuten.
    - Passcode: Legen Sie einen Passcode für den Touchscreen fest, um eine zusätzliche Sicherheitsebene hinzuzufügen.

    Detaillierte Anweisungen finden Sie unter [Display Management](../../interface_guide/display_management.md).

=== "USB & Power"

    Auf der Seite USB & Power können Sie USB-bezogene Einstellungen und die Energieverwaltung Ihres Routers konfigurieren, z. B. USB-Protokoll, Stromrichtung, Leerlauf-Timeouts und Standby-Verhalten.

    Detaillierte Anweisungen finden Sie unter [USB & Power](../../interface_guide/usb_power.md).

---

=== "Time Zone"

    Auf der Seite Time Zone können Sie die korrekte Zeitzone für Ihren Router festlegen, damit alle Zeitpläne, Protokolle und Systemereignisse präzise mit Ihrer Ortszeit versehen werden. Diese Einstellung ist wichtig für genaue Aufzeichnungen und die korrekte Ausführung zeitbasierter Konfigurationen.

    Detaillierte Anweisungen finden Sie unter [Time Zone](../../interface_guide/time_zone.md).

=== "Reset Firmware"

    Auf der Seite Reset Firmware können Sie die aktuell installierte Firmware-Version Ihres Routers auf ihre Standardeinstellungen zurücksetzen, wodurch alle benutzerdefinierten Konfigurationen gelöscht werden. Dabei wird der Router auf die Standardeinstellungen der derzeit installierten Firmware-Version zurückgesetzt. Das ist hilfreich, um hartnäckige Probleme zu beheben oder mit der Standardkonfiguration der aktuellen Firmware neu zu beginnen.

    Detaillierte Anweisungen finden Sie unter [Reset Firmware](../../interface_guide/reset_firmware.md).

=== "Log"

    Auf der Seite Log erhalten Sie Zugriff auf verschiedene Protokolle, die die Aktivitäten und Ereignisse des Routers aufzeichnen und so die Fehlerbehebung sowie Leistungsüberwachung unterstützen. Diese Seite umfasst:

    * System Log: Detaillierte Protokolle von Systemereignissen und -aktivitäten.
    * Kernel Log: Protokolle zu Vorgängen und Ereignissen des Kernels.
    * Crash Log: Aufzeichnungen von Systemabstürzen und Fehlern, die bei der Diagnose kritischer Probleme helfen.
    * Cloud Log: Protokolle zu Interaktionen und Aktivitäten im Zusammenhang mit den in den Router integrierten GoodCloud-Diensten.
    * Nginx Log: Protokolle des Nginx-Webservers, sofern dieser vom Router genutzt wird, mit Informationen zu Webverkehr und Serverbetrieb.

    Zusätzlich verfügt die Seite über die Schaltfläche Export Log, mit der Sie alle gesammelten Protokolle zur Analyse durch den technischen Support exportieren können. Diese Funktion ist besonders hilfreich bei der Diagnose komplexer Probleme und beim Einholen professioneller Unterstützung.

    Detaillierte Anweisungen finden Sie unter [Log](../../interface_guide/log.md).

=== "Advanced Settings"

    Auf der Seite Advanced Settings erhalten erfahrene Benutzer über die OpenWrt-LuCI-Oberfläche Zugriff auf erweiterte Konfigurationsoptionen, um Routereinstellungen und Funktionen über die grundlegenden Oberflächenoptionen hinaus fein abzustimmen. Dazu gehören detaillierte Netzwerkkonfigurationen, Firewall-Einstellungen und weitere erweiterte Systemanpassungen.

    Detaillierte Anweisungen finden Sie unter [Advanced Settings](../../interface_guide/advanced_settings.md).
