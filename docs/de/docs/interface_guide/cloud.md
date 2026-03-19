# GL.iNet GoodCloud

## Inhalt

- [Einführung](#einführung)
- [Geräte mit GoodCloud verknüpfen](#geräte-mit-goodcloud-verknüpfen)
    - [Für Firmware v4.6 oder älter](#für-firmware-v46-oder-älter)
        - [GoodCloud aktivieren](#goodcloud-aktivieren)
        - [Ein Konto registrieren](#ein-konto-registrieren)
        - [Geräte hinzufügen](#geräte-hinzufügen)
        - [Details zur Verknüpfung](#details-zur-verknüpfung)
        - [Geräteverknüpfung aufheben](#geräteverknüpfung-aufheben)
    - [Für Firmware v4.7 oder neuer](#für-firmware-v47-oder-neuer)
        - [Cloud Service aktivieren](#cloud-service-aktivieren)
        - [Details zur Verknüpfung](#details-zur-verknüpfung_1)
        - [Geräteverknüpfung aufheben](#geräteverknüpfung-aufheben_1) 
- [Geräte verwalten](#geräte-verwalten)
    - [Systeminformationen und Aktionen](#systeminformationen-und-aktionen)
    - [Gerätedetails](#gerätedetails)  
        - [Basisinformationen](#basisinformationen)
        - [Statistiken](#statistiken)
        - [Netzwerkeinstellungen](#netzwerkeinstellungen)
        - [Client-Liste](#client-liste)
- [Fernzugriff](#fernzugriff)
    - [Remote GUI](#remote-gui)
    - [Remote SSH](#remote-ssh)
- [Einstellungen ändern](#einstellungen-ändern)
- [E-Mail-Benachrichtigungen](#e-mail-benachrichtigungen)
- [Site to Site](#site-to-site)
- [GoodCloud und VPN](#goodcloud-und-vpn)
- [Protokolle anzeigen](#protokolle-anzeigen)
- [Cloud deaktivieren](#cloud-deaktivieren)
- [Konto löschen](#konto-löschen)

## Einführung

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} ist eine Plattform, die die Bereitstellung und Verwaltung verbundener Geräte aus der Ferne vereinfacht. Sie bietet eine komfortable Möglichkeit, GL.iNet-Router zentral zu verwalten und auf sie zuzugreifen. Durch die Zentralisierung der Netzwerkgeräte in der Cloud können Benutzer Verwaltungsaufgaben für mehrere Geräte effizient durchführen, etwa Netzwerkkonfigurationen ausrollen oder Software-Upgrades ausführen. Außerdem können sie aus der Ferne auf das webbasierte Admin Panel des Routers zugreifen oder sich per SSH mit dem Terminal des Routers verbinden und so ein regionsübergreifendes End-to-End-Management von Netzwerkgeräten umsetzen.

Mit GoodCloud können Sie:

1. Den Echtzeitstatus des Routers prüfen
    - Online-/Offline-Status überwachen
    - RAM-Auslastung und Load Average in Echtzeit anzeigen
    - E-Mail-Benachrichtigungen bei Änderungen des Online-/Offline-Status erhalten

2. Router aus der Ferne verwalten und einrichten
    - Routereinstellungen konfigurieren (z. B. SSID und Passwort)
    - Fernzugriff per SSH
    - Fernzugriff auf das WebUI
    - Routerzugriff mit anderen teilen

3. Verbundene Clients aus der Ferne verwalten und überwachen
    - Geräte anzeigen, die mit Ihrem Netzwerk verbunden sind
    - Datenverkehr in Echtzeit überwachen und Clients blockieren
    - E-Mail-Benachrichtigungen bei neuen Verbindungen und Blockierungsereignissen erhalten

4. Batch-Operationen durchführen
    - Batch-Neustart
    - Batch-Firmware-Upgrade

5. Site-to-Site-Konnektivität aufbauen
    - Virtuelles Büro: Erweitern Sie Ihr Büronetzwerk auf weitere Niederlassungen
    - Geschäftsreisen: Greifen Sie remote auf Bürosysteme zu (z. B. OA, CRM, MySQL)
    - Smart Home: Greifen Sie remote auf Heimgeräte zu (z. B. IP-Kameras, NAS)

Wenn Sie mehrere Geräte verwalten und erweiterte Funktionen wie Batch-Operationen, Multi-Account-Verwaltung und maßgeschneiderte Lösungen nutzen möchten, wählen Sie unsere kostenpflichtigen Mehrwertpläne. Klicken Sie [hier](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} für Details oder kontaktieren Sie [support@glinet.biz](mailto:support@glinet.biz).

## Geräte mit GoodCloud verknüpfen

Damit Geräte erfolgreich mit der Cloud-Plattform verbunden werden können, befolgen Sie bitte die Verknüpfungsschritte entsprechend Ihrer Firmware-Version.

### Für Firmware v4.6 oder älter

#### GoodCloud aktivieren

Melden Sie sich am webbasierten Admin Panel Ihres Routers an und navigieren Sie zu **APPLICATIONS** -> **GoodCloud**. Aktivieren Sie den Schalter, um GoodCloud einzuschalten.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

Aktivieren Sie **Remote SSH** und **Remote Web Access** nach Bedarf, wählen Sie den nächstgelegenen Server, lesen und akzeptieren Sie die **Terms of Service & Privacy Policy**, und klicken Sie dann auf **Apply**.

![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

- **Remote SSH**: Für den Fernzugriff auf das Terminal des Routers über GoodCloud.

- **Remote Web Access**: Für den Fernzugriff auf das webbasierte Admin Panel des Routers über GoodCloud.

- **Data Server**: Wählen Sie den Server, der dem Standort Ihres Geräts am nächsten ist. Es stehen drei Optionen zur Verfügung: Asia Pacific (Japan), America (Oregon) und Europe (Ireland).

#### Ein Konto registrieren

Besuchen Sie die [GoodCloud-Website](https://www.goodcloud.xyz){target="_blank"}, registrieren Sie ein Konto und melden Sie sich an.

Wenn Sie keine Bestätigungs-E-Mail erhalten, prüfen Sie bitte Ihren Spam-Ordner oder warten Sie einige Minuten und versuchen Sie es erneut. Bei Problemen bei der Registrierung wenden Sie sich bitte an [support@glinet.biz](mailto:support@glinet.biz).

#### Geräte hinzufügen

Navigieren Sie auf der Cloud-Plattform zu **Devices** -> **Bound Devices** -> **Add Devices**.

![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

Es gibt drei Möglichkeiten, ein Gerät mit Ihrem GoodCloud-Konto zu verknüpfen: Auto Discover, Manually Add und Bulk Import.

??? "Auto Discover"

    Sie können **Auto discover** verwenden, wenn sich Ihr Router und das Gerät, mit dem Sie auf die GoodCloud-Website zugreifen, im selben Netzwerk befinden.

    Wählen Sie Ihr Gerät aus der Dropdown-Liste aus und geben Sie **DDNS / Device ID** ein. Diese Angaben finden Sie auf der Unterseite Ihres Routers oder auf der GoodCloud-Seite im webbasierten Admin Panel.

    ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

    Unter [diesem Link](../faq/where_to_find_the_device_id_mac_sn.md) finden Sie Informationen dazu, wo die Device ID zu finden ist.

??? "Manually Add"

    Wenn Ihr Gerät nicht in der Liste erscheint, klicken Sie auf **Manually add** und geben Sie die Details Ihres Routers ein. Alle erforderlichen Informationen finden Sie auf der Unterseite des Routers oder auf der GoodCloud-Seite im webbasierten Admin Panel.

    ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

??? "Bulk Import"

    **Bulk Import** ist für Benutzer gedacht, die eine große Anzahl von Geräten verwalten. Sie können mehrere Geräte über eine Microsoft-Excel-Datei importieren.

    ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

#### Details zur Verknüpfung

Nachdem die Verknüpfung erfolgreich abgeschlossen wurde, melden Sie sich erneut am webbasierten Admin Panel des Routers an und navigieren zu **APPLICATIONS** -> **GoodCloud**. Aktualisieren Sie diese Seite; anschließend werden der verknüpfte GoodCloud-Benutzername und das Datum angezeigt.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_1.png){class="glboxshadow"}

#### Geräteverknüpfung aufheben

Wenn Sie die Verknüpfung Ihres Routers aufheben möchten, melden Sie sich am webbasierten Admin Panel des Routers an, navigieren zu **APPLICATION** -> **GoodCloud** und klicken auf **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

Alternativ können Sie das entsprechende Gerät in der Liste der gebundenen Geräte auf der GoodCloud-Plattform entfernen. Das webbasierte Admin Panel des Routers synchronisiert sich dann automatisch und zeigt den aktuellen Verknüpfungsstatus an.

Wenn Sie Hilfe benötigen, kontaktieren Sie bitte [support@glinet.biz](mailto:support@glinet.biz).

### Für Firmware v4.7 oder neuer

#### Cloud Service aktivieren

Melden Sie sich am webbasierten Admin Panel Ihres Routers an und navigieren Sie zu **CLOUD SERVICE** -> **GoodCloud**.

Klicken Sie auf die Schaltfläche **Get Started**. Daraufhin erscheint oben rechts ein Cloud-Service-Popup. Klicken Sie auf **Enable**, um Cloud Service zu verwenden.

![enable cloud service](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.jpg){class="glboxshadow"}

Melden Sie sich mit Ihrem GoodCloud-Konto an.

![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

Wenn Sie noch kein Konto haben, registrieren Sie eines und melden Sie sich an. Nach Abschluss der Registrierung wird der Router automatisch mit diesem Konto verknüpft.

![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

Wenn Sie keine Bestätigungs-E-Mail erhalten, prüfen Sie bitte Ihren Spam-Ordner oder warten Sie einige Minuten und versuchen Sie es erneut. Bei Problemen bei der Registrierung wenden Sie sich bitte an [support@glinet.biz](mailto:support@glinet.biz).

#### Details zur Verknüpfung

Nach erfolgreicher Verknüpfung melden Sie sich erneut am webbasierten Admin Panel des Routers an, klicken oben rechts auf das Cloud-Symbol und sehen die Verknüpfungsdetails, darunter GoodCloud-Benutzername und Datum, Device ID, Device MAC und Device S/N.

![cloud info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/cloud_info.png){class="glboxshadow"}

Navigieren Sie im webbasierten Admin Panel zu **CLOUD SERVICES** -> **GoodCloud**. Dort können Sie den Fernzugriff für Ihren Router aktivieren oder deaktivieren.

![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info_2.png){class="glboxshadow"}

- **Remote SSH**: Für den Fernzugriff auf das Terminal des Routers über GoodCloud.

- **Remote Web Access**: Für den Fernzugriff auf das webbasierte Admin Panel des Routers über GoodCloud.

- **View Logs**: Zeigt API-Aufrufprotokolle von GoodCloud an.

#### Geräteverknüpfung aufheben

Wenn Sie die Verknüpfung Ihres Routers aufheben möchten, melden Sie sich am webbasierten Admin Panel des Routers an. Klicken Sie oben rechts auf das Cloud-Symbol und anschließend auf **Unbind**.

![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

Alternativ können Sie das entsprechende Gerät in der Liste der gebundenen Geräte auf der GoodCloud-Plattform entfernen. Das webbasierte Admin Panel des Routers synchronisiert sich dann automatisch und zeigt den aktuellen Verknüpfungsstatus an.

Wenn Sie Hilfe benötigen, kontaktieren Sie bitte [support@glinet.biz](mailto:support@glinet.biz).

## Geräte verwalten

### Systeminformationen und Aktionen

Unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** können Sie die Systeminformationen (z. B. Modell, Version, MAC-Adresse, IP-Adresse) und den Status (z. B. online, offline) aller Geräte anzeigen, die mit Ihrem Konto verknüpft sind.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Wählen Sie ein Gerät aus. Anschließend können Sie oben rechts Aktionen ausführen, z. B. Einstellungen ändern, Firmware aktualisieren, aus der Ferne auf das Gerät zugreifen, es neu starten oder zurücksetzen.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Klicken Sie auf das Zahnradsymbol ganz rechts in der Listenüberschrift. Dort können Sie die angezeigten Spalten und deren Reihenfolge anpassen, damit genau die Geräteinformationen angezeigt werden, die für Sie wichtig sind.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Gerätedetails

Klicken Sie unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** auf einen Gerätenamen. Sie werden dann zur Detailseite des Geräts weitergeleitet. Dort werden unter anderem die Basisinformationen des Routers, statistische Daten, Netzwerkeinstellungen und die Client-Liste angezeigt.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Basisinformationen

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistiken

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Netzwerkeinstellungen

Auf dieser Seite werden die Netzwerkkonfigurationen und Wi-Fi-Einstellungen Ihres Routers angezeigt.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Client-Liste

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Fernzugriff

Unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** klicken Sie auf den Namen des Geräts, auf das Sie zugreifen möchten, um die Detailseite zu öffnen. Dort finden Sie oben rechts die Remote-Aktionen.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI

Klicken Sie auf **Remote GUI**, um remote auf das webbasierte Admin Panel Ihres Routers zuzugreifen.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Wenn diese Option ausgegraut oder nicht verfügbar ist, ist die Funktion wahrscheinlich deaktiviert. Aktivieren Sie sie zuerst im webbasierten Admin Panel des Routers, bevor Sie über GoodCloud darauf zugreifen.

Wenn diese Option anklickbar ist, aber nicht reagiert, versuchen Sie es im Inkognito-/InPrivate-Modus Ihres Browsers.

### Remote SSH

Klicken Sie auf **Remote SSH**, um per SSH remote auf das Terminal Ihres Routers zuzugreifen.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Wenn diese Option ausgegraut oder nicht verfügbar ist, ist die Funktion wahrscheinlich deaktiviert. Aktivieren Sie sie zuerst im webbasierten Admin Panel des Routers, bevor Sie über GoodCloud darauf zugreifen.

Wenn diese Option anklickbar ist, aber nicht reagiert, versuchen Sie es im Inkognito-/InPrivate-Modus Ihres Browsers.

## Einstellungen ändern

Sie können mehrere Parameter für ein einzelnes Gerät oder für mehrere Geräte konfigurieren.

Navigieren Sie unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** zu dem Gerät, das Sie konfigurieren möchten, und klicken Sie oben rechts auf **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Hier können Sie die Netzwerkeinstellungen des Routers prüfen und ändern, darunter Einstellungen für Wireless, Ethernet, Sicherheit, Port Forwarding, LAN und das System.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## E-Mail-Benachrichtigungen

Sie können E-Mail-Benachrichtigungen einrichten, wenn sich der Gerätestatus ändert (online/offline) oder wenn neue Clients verbunden werden.

Navigieren Sie unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** und klicken Sie oben rechts auf die Schaltfläche **Add Rule**.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Wählen Sie das Gerät aus, das Sie überwachen möchten, und klicken Sie auf **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Wählen Sie das auslösende Ereignis, z. B. den Online-/Offline-Status des Geräts, und klicken Sie auf **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Prüfen Sie die Regeleinstellungen und klicken Sie auf **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

In der Benachrichtigungsliste können Sie die von Ihnen erstellten Alarmregeln anzeigen. Einzelne Benutzer können derzeit nur eine Alarmregel erstellen. Wenn Sie Geräte in größerem Umfang verwalten möchten, kontaktieren Sie uns gerne, um Ihren Plan zu erweitern.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site

Bitte lesen Sie [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud und VPN

Wenn Sie auf Ihrem Router gleichzeitig **GoodCloud** und den **VPN client** aktivieren, wird die Verbindung zwischen dem Router und dem GoodCloud-Server standardmäßig nicht über das VPN geleitet. Dadurch bleibt die Verbindung zu den GoodCloud-Diensten stabiler.

Wenn Sie möchten, dass die GoodCloud-Verbindung über das VPN läuft, können Sie diese Einstellung jedoch im webbasierten Admin Panel des Routers ändern. Navigieren Sie zu VPN -> VPN Dashboard -> VPN Client -> Options und aktivieren Sie die Option **Services from GL.iNet Use VPN**.

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Beachten Sie, dass das Routing von GoodCloud über ein VPN die Stabilität der Cloud-Verbindung beeinträchtigen kann, insbesondere wenn:

* die VPN-Verbindung instabil ist
* der VPN-Anbieter GoodCloud-Datenverkehr filtert oder blockiert
* das VPN der Verbindung eine hohe Latenz hinzufügt

Im Allgemeinen wird empfohlen, die Standardeinstellung beizubehalten, bei der GoodCloud das VPN umgeht, um optimale Leistung und Zuverlässigkeit zu gewährleisten.

## Protokolle anzeigen

Sie können GoodCloud-Protokolle nach Bedarf anzeigen, darunter Activity Logs, Device Logs, Upgrade Logs, Alert Logs und Device Settings Logs.

Navigieren Sie unter [GoodCloud](https://www.goodcloud.xyz){target="_blank"} zu **Logs** und wählen Sie in der Dropdown-Liste die Protokolle aus, die Sie anzeigen möchten.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Cloud deaktivieren

Wenn Sie nicht mehr möchten, dass Ihr Gerät mit der Cloud-Plattform verbunden ist, können Sie den Cloud Service im webbasierten Admin Panel des Routers deaktivieren.

??? "Für Firmware v4.6 oder älter"

    Melden Sie sich am webbasierten Admin Panel Ihres Routers an, navigieren Sie zu **APPLICATIONS** -> **GoodCloud**, deaktivieren Sie GoodCloud per Schalter und klicken Sie auf **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Nach der Deaktivierung wird die Oberfläche wie folgt angezeigt.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Für Firmware v4.7 oder neuer"

    Melden Sie sich am webbasierten Admin Panel Ihres Routers an und klicken Sie oben rechts auf das Cloud-Symbol.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Nach der Deaktivierung wird die Oberfläche wie folgt angezeigt.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Konto löschen

Aus Sicherheitsgründen können Sie Ihr Konto löschen, wenn Sie es nicht mehr nutzen.

Klicken Sie auf der [GoodCloud](https://www.goodcloud.xyz){target="_blank"}-Plattform oben rechts auf den Benutzernamen und wählen Sie **Personal Center**. Scrollen Sie bis zum Ende der Seite und klicken Sie auf **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Durch das Löschen werden alle zugehörigen Dienste, Daten und persönlichen Informationen dauerhaft entfernt. Eine Wiederherstellung ist nicht möglich.

    Wenn Ihr Konto zu einer Organisation gehört, verlassen Sie bitte zuerst alle Organisationen, bevor Sie Ihr Konto löschen.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
