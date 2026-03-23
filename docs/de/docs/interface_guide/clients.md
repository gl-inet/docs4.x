# Clients

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **CLIENTS**.

Auf der Seite Clients werden Informationen über verbundene Geräte angezeigt, darunter Gerätename, Verbindungstyp, IP-Adresse, MAC-Adresse, Geschwindigkeit und Datenverkehr, von links nach rechts angeordnet.

## Gerätename

In der ersten Spalte werden der Gerätename und der Gerätetyp angezeigt. Diese hängen vom Hostnamen des Geräts ab.

![device name](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/device_name.png){class="glboxshadow"}

Um den Gerätenamen und den Gerätetyp zu ändern, klicken Sie in der Spalte Action auf das Drei-Punkte-Symbol und im Dropdown-Menü auf **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

## Verbindungstyp

Das blaue Symbol rechts neben dem Gerätenamen steht für den Verbindungstyp bzw. die Verbindungsmethode des Geräts.

Es zeigt an, wie das Gerät mit dem Netzwerk verbunden ist – entweder über Wi-Fi oder über ein Ethernet-Kabel.

![connection type](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/connection_type.png){class="glboxshadow"}

## IP- und MAC-Adresse

In der zweiten Spalte werden die IP- und MAC-Adressen des verbundenen Geräts aufgeführt.

![ip and mac](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/ip_mac.png){class="glboxshadow"}

Viele Geräte verwenden zufällig generierte MAC-Adressen. Wenn verbundene Geräte zufällige MAC-Adressen verwenden, erscheint der folgende Hinweis.

![random mac prompt](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/randomized_mac.png){class="glboxshadow"}

**Hinweis**: Hier gilt die Regel, dass eine MAC-Adresse als zufällig generiert betrachtet wird, wenn das zweite Zeichen 2, 6, A oder E ist (Groß-/Kleinschreibung wird ignoriert). Manche Geräte verwenden jedoch andere Regeln zur Generierung zufälliger MAC-Adressen, daher ist diese Erkennungsmethode möglicherweise nicht immer genau.

## Geschwindigkeit

In der dritten Spalte wird die Internetgeschwindigkeit des verbundenen Geräts angezeigt.

![speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/speed.png){class="glboxshadow"}

Die hier angezeigte Geschwindigkeit ist die Durchschnittsgeschwindigkeit über 3 Minuten.

- Wenn Sie die aktuelle Seite 10 Sekunden lang geöffnet haben, wird der Durchschnitt der letzten 10 Sekunden angezeigt.
- Wenn Sie die aktuelle Seite 30 Sekunden lang geöffnet haben, wird der Durchschnitt der letzten 30 Sekunden angezeigt.
- Wenn Sie die aktuelle Seite 60 Sekunden lang geöffnet haben, wird der Durchschnitt der letzten 60 Sekunden angezeigt.
- Wenn Sie die aktuelle Seite 3 Minuten lang geöffnet haben, wird die Durchschnittsrate der letzten 3 Minuten angezeigt.
- Wenn Sie die aktuelle Seite 10 Minuten lang geöffnet haben, wird ebenfalls die Durchschnittsrate der letzten 3 Minuten angezeigt.

## Datenverkehr

In der vierten Spalte wird der Internetdatenverkehr des verbundenen Geräts angezeigt.

![traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/traffic.png){class="glboxshadow"}

## Reservierte IP

In der fünften Spalte können Sie mit nur einem Klick eine IP-Adresse für ein bestimmtes verbundenes Gerät reservieren. 

Diese Funktion ist ab v4.8 verfügbar.

Wenn Sie einem Client im LAN eine reservierte IP-Adresse zuweisen, erhält dieser jedes Mal dieselbe IP-Adresse, wenn er den DHCP-Server des Routers verwendet. 

Sie können reservierte IP-Adressen für Computer oder Server vergeben, die dauerhaft feste IP-Einstellungen benötigen.

![reserved ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/reserved_ip.png){class="glboxshadow"}

## Sperrliste

In der sechsten Spalte können Sie bestimmte verbundene Geräte mit nur einem Klick blockieren. 

Standardmäßig ist die Zugriffskontrollregel auf Blocklist eingestellt. Bei Bedarf können Sie sie oben auf Allowlist umstellen.

![blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist.jpg){class="glboxshadow"}

![access control](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/blocklist_allowlist.jpg){class="glboxshadow"}

- **Blocklist**: Geräte mit MAC-Adressen auf der Sperrliste dürfen sich nicht mit diesem Router verbinden.

- **Allowlist**: Nur Geräte mit bestimmten MAC-Adressen dürfen sich verbinden. Das eignet sich für IoT-Geräte und das Management von Unternehmensnetzwerken.

Um eine Blocklist zu erstellen, können Sie bei **(1)** eine Sperrliste im Excel-Format hochladen oder bei **(2)** MAC-Adressen manuell eingeben.

![create blocklist](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/create_blocklist.png){class="glboxshadow"}

**Methode 1. Clients importieren**

Klicken Sie auf der Seite Access Control auf **Import Clients**.

![import clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/import_clients.png){class="glboxshadow"}

Klicken Sie auf **Download Import Template**. Dadurch laden Sie ein XLS-Arbeitsblatt mit dem Namen "mac-template.csv" herunter.

![download template](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/download_template.png){class="glboxshadow"}

Öffnen Sie die Datei, tragen Sie die MAC-Adressen ein und speichern Sie sie.

![import csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/importcsv.jpg){class="glboxshadow gl-80-desktop"}

Wählen Sie die gespeicherte Datei aus oder ziehen Sie sie in den Upload-Bereich.

![upload csv](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/dragcsv.jpg){class="glboxshadow  gl-80-desktop"}

Sobald der Upload erfolgreich war, klicken Sie auf **Import**, um den Massenimport der MAC-Adressen abzuschließen.

![upload successful](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/upload_successful.png){class="glboxshadow"}

**Methode 2. Manuell eingeben**

Geben Sie auf der Seite Access Control die MAC-Adresse der Geräte, die Sie blockieren möchten, manuell ein und klicken Sie auf **Apply**.

![input mac manually](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/input_mac_manually.png){class="glboxshadow"}

**Hinweis**: Das Blockieren eines Clients basiert auf der MAC-Adresse des Geräts. Wenn das blockierte Gerät beim nächsten Mal eine andere MAC-Adresse verwendet, kann es sich weiterhin mit dem Router verbinden.

## Sortierung

Der aktuelle Sortiertyp wird oben rechts angezeigt, und Sie können zu anderen Sortiertypen wechseln.

Der Standardsortiertyp ist wie folgt:

- Das aktuelle Gerät steht immer ganz oben.
- Im Abschnitt der Online-Clients gilt: Je später sich ein Gerät verbindet, desto weiter oben erscheint es in der Liste.

![sort](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/sort.png){class="glboxshadow"}

## Aktion

### Client-Details

Wenn Sie die Details eines Client-Geräts anzeigen möchten, klicken Sie in der rechten Spalte Action auf das Drei-Punkte-Symbol und anschließend im Dropdown-Menü auf **View Details**.

![view details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/details.png){class="glboxshadow"}

Auf der geöffneten Unterseite sehen Sie alle Informationen zum Client-Gerät, einschließlich aller IPv6-Adressen des Geräts, sofern vorhanden.

![client details](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/client_detail.png){class="glboxshadow"}

### Modify

Klicken Sie in der Spalte Action auf das Drei-Punkte-Symbol und im Dropdown-Menü auf **Modify**.

![modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify.png){class="glboxshadow"}

![modify client device](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/modify_client_device.png){class="glboxshadow"}

### Geschwindigkeit begrenzen

Klicken Sie in der Spalte Action auf das Drei-Punkte-Symbol und im Dropdown-Menü auf **Limit Speed**.

![limit speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.png){class="glboxshadow"}

![limit speed settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/clients_limit_speed_settings.png){class="glboxshadow"}

Wenn für einen Client eine Geschwindigkeitsbegrenzung angewendet wurde, werden die Aufwärts- und Abwärtspfeile bei der Geschwindigkeit gelb dargestellt.

![limited speed](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/limit_speed.jpg){class="glboxshadow"}

Klicken Sie in der Spalte Action auf das Drei-Punkte-Symbol, um die Geschwindigkeitsbegrenzung zu deaktivieren.

### VPN-Tunnel verwenden

**Hinweis**: Diese Option ist ab Firmware v4.8 verfügbar und erscheint nur im Action-Menü, wenn eine MAC-basierte Richtlinie konfiguriert ist.

Fügen Sie einen Client mit einer MAC-basierten Richtlinie zur Liste der VPN-Tunnel hinzu. Wenn Sie detaillierte Anpassungen an den Tunneln vornehmen müssen, gehen Sie zum VPN Dashboard, um sie dort zu verwalten.

![use vpn tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/use-vpn-tunnel.png){class="glboxshadow"}

## Offline-Clients entfernen

Im Abschnitt der Offline-Clients können Sie oben rechts auf **Delete All** klicken, um alle Offline-Clients zu löschen. 

Wenn Sie einen bestimmten Client entfernen möchten, klicken Sie in der Spalte Action auf das Drei-Punkte-Symbol und anschließend im Dropdown-Menü auf **Remove Client**.

![remove offline clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/clients/remove_offline.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
