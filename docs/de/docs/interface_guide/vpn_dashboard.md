# VPN Dashboard {#vpn-dashboard}

Der Inhalt dieser Seite basiert auf Firmwareversion v4.9.x und höher. Wenn auf Ihrem Gerät eine andere Firmwareversion ausgeführt wird, verwenden Sie die folgende Auswahl, um zur entsprechenden Anleitung zu wechseln.

<div class="gl-link-select" data-label="Firmwareversion" data-placeholder="Firmware v4.9 und höher" markdown="1">

- [Firmware v4.7 und früher](vpn_dashboard_v4.7.md)
- [Firmware v4.8](vpn_dashboard_v4.8.md)

</div>

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **VPN** -> **VPN Dashboard**.

Das VPN Dashboard zeigt VPN-Verbindungsdetails wie Routing-Regeln, verbundenen Server, Datenverkehrsstatistiken, virtuelle Client-IP und Verbindungsprotokoll an und ermöglicht es Benutzern, erweiterte Einstellungen wie VPN Kill Switch, IP-Maskierung und MTU zu konfigurieren.

Im Vergleich zu Firmware v4.8 enthält v4.9 die folgenden Verbesserungen am VPN Dashboard:

1. **Benutzer können mehrere Profile innerhalb einer Tunnel-Gruppe auswählen und ihre Priorität festlegen**. Der Tunnel versucht, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde.

2. **Jede Tunnel-Gruppe arbeitet unabhängig und führt kein Failover zwischen Gruppen durch**. Wenn alle Profile in einem einzelnen Tunnel keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und des All Other Traffic Tunnels, ob auf das lokale WAN umgeschaltet werden soll.

## VPN-Profil hochladen {#upload-vpn-profile}

Wenn Sie diese Seite zum ersten Mal aufrufen und noch keine Tunnel erstellt wurden, wird die Seite wie unten gezeigt angezeigt. Klicken Sie auf **Add VPN Tunnel**, um zu beginnen.

![add vpn tunnel](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

Sie werden zur Seite **VPN Client Profile** weitergeleitet. Wählen Sie einen VPN-Anbieter aus und melden Sie sich an.

![select vpn provider](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

!!! Tip

    1. Die in der Abbildung oben aufgeführten VPN-Anbieter sind in das Web-Admin-Panel des GL.iNet-Routers integriert. Mit einem aktiven Abonnement geben Benutzer einfach ihre Anmeldedaten ein, um sich sofort anzumelden und Konfigurationsdateien für VPN-Verbindungen zu erhalten.

    2. Wenn Sie andere VPN-Anbieter abonniert haben oder Ihre persönlichen VPN-Konfigurationen hochladen möchten, klicken Sie auf **Add Manually** und laden Sie Ihre Konfigurationen hoch.

Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Klicken Sie auf PureVPN und melden Sie sich mit gültigen Anmeldedaten an.

![PureVPN1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Sie erhalten eine Liste von VPN-Profilen. Bei einigen VPN-Dienstanbietern müssen Sie möglicherweise ein VPN-Protokoll oder bevorzugte Server/Städte auswählen, bevor die Liste der Profile erscheint.

![PureVPN3](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

Klicken Sie unten auf **Go to Dashboard**. Sie werden zum VPN Dashboard weitergeleitet, um Ihren VPN-Tunnel hinzuzufügen und VPN-Richtlinien zu konfigurieren.

## VPN-Tunnel hinzufügen {#add-vpn-tunnel}

### Allgemeine Schritte {#general-steps}

Folgen Sie den nachstehenden Schritten, um Ihren VPN-Tunnel hinzuzufügen und VPN-Richtlinien zu konfigurieren. Siehe bei Bedarf [Fallbeispiele](#case-reference).

1. Klicken Sie im VPN Dashboard auf **Add VPN Tunnel**. Rechts wird ein VPN-Einrichtungsassistent eingeblendet.

    ![add vpn tunnel](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/add_vpn_tunnel.png){class="glboxshadow"}

2. Wählen Sie das VPN-Profil.

    Wählen Sie ein oder mehrere Profile aus, passen Sie deren Priorität rechts nach Bedarf an und klicken Sie dann auf **Next**.

    ![select profile](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt werden, versucht der Tunnel, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Kill Switch in den Einstellungen unter [Tunnel-Optionen](#tunnel-options) und [All Other Traffic](#all-other-traffic), ob auf das lokale WAN des Routers umgeschaltet werden soll.

3. Wählen Sie die Client-Quelle und klicken Sie dann auf **Next**.

    Es gibt vier Optionen:

    - **All Clients**: Wenn ausgewählt, entspricht der Datenverkehr aller Geräte dieser Regel.
    ![all clients](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: Wenn ausgewählt, entspricht der Datenverkehr bestimmter Verbindungstypen (z. B. LAN-Subnetz, Drop-in Gateway, Gastnetzwerk) dieser Regel.
    ![specified connection types](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: Wenn ausgewählt, entspricht der Datenverkehr bestimmter Geräte (identifiziert über die MAC-Adresse) dieser Regel.
    ![specified devices](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: Wenn ausgewählt, entspricht der Datenverkehr bestimmter Geräte (identifiziert über die MAC-Adresse) dieser Regel nicht.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

4. Wählen Sie das Datenverkehrsziel und klicken Sie dann auf **Apply**.

    Es gibt drei Optionen:

    - **All Targets**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, zu allen Zielen geleitet.
    ![all targets](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, zu bestimmten Domains oder IP-Adressen geleitet. Sie müssen diese manuell eingeben.
    ![specified domain ip](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, nicht zu bestimmten Domains oder IP-Adressen geleitet. Sie müssen diese manuell eingeben.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

5. Der VPN-Tunnel wurde erfolgreich hinzugefügt. Sie werden zum **VPN Dashboard** weitergeleitet. Fügen Sie bei Bedarf weitere VPN-Tunnel hinzu.

    Prüfen Sie aus Sicherheitsgründen unter [All Other Traffic](#all-other-traffic) und [Tunnel-Optionen](#tunnel-options) den Status des **Kill Switch**, bevor Sie Ihren VPN-Tunnel aktivieren.

### Fallbeispiele {#case-reference}

Im Folgenden finden Sie zwei typische Konfigurationsbeispiele für VPN-Richtlinien mit schrittweisen Einrichtungsanweisungen zur Orientierung.

??? note "Fall 1: Nur bestimmte Geräte über VPN leiten."

    **Anforderungen:**

    1. Nur bestimmte Geräte, die mit diesem Router verbunden sind, greifen über VPN auf das Internet zu. Alle anderen Geräte greifen über das lokale WAN auf das Internet zu.

    2. Die ausgewählten Geräte müssen ausschließlich die VPN-Verbindung verwenden. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    **Konfigurationsschritte:**

    1. Wählen Sie das VPN-Profil.

        Wenn Sie sich mit Anmeldedaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls gehen Sie zu **VPN Client Profile**, um sich mit Ihren Anmeldedaten anzumelden oder eine Konfigurationsdatei manuell hochzuladen.

        Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

        ![case 1 profile](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    2. Wählen Sie die Client-Quelle.

        Klicken Sie auf die Registerkarte **Specified Devices**, wählen Sie die Geräte aus, die das VPN verwenden sollen, und klicken Sie dann auf **Next**.

        ![case 1 source](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

    3. Wählen Sie das Datenverkehrsziel.

        Klicken Sie auf die Registerkarte **All Targets**, legen Sie sie als Datenverkehrsziel fest und klicken Sie dann auf **Apply**.

        ![case 1 target](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_all_targets.png){class="glboxshadow"}

    4. Sie werden zum VPN Dashboard weitergeleitet. Der VPN-Tunnel wurde nun erfolgreich hinzugefügt, wie unten gezeigt.

        ![case 1 dashboard](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

    5. Stellen Sie sicher, dass der **Kill Switch** für diesen Tunnel aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

        ![case 1 kill switch1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

        ![case 1 kill switch2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

    6. Stellen Sie sicher, dass **Allow Non-VPN Traffic** aktiviert ist. Diese Option ist standardmäßig aktiviert, damit Datenverkehr, der nicht dem VPN-Tunnel entspricht, weiterhin über das lokale WAN auf das Internet zugreifen kann.

        ![case 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

    7. Klicken Sie auf die mittlere Schaltfläche, um diesen Tunnel zu aktivieren.

        ![case 1 connect](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

    8. Sobald die Verbindung hergestellt ist, zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Datenverkehrsstatistiken, Serveradresse, Listening-Port und virtueller IP-Adresse.

        ![case 1 connected](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

        Jetzt greifen nur zwei bestimmte Geräte über VPN auf das Internet zu. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern. Alle anderen Geräte greifen stattdessen über das lokale WAN auf das Internet zu.

??? note "Fall 2: Alle Geräte für bestimmte Websites über VPN 1 und den gesamten übrigen Datenverkehr über VPN 2 leiten."

    **Anforderungen:**

    1. Alle Geräte verwenden **VPN Tunnel 1** beim Zugriff auf Domains bestimmter Social-Media- und Streaming-Dienste und **VPN Tunnel 2** für den gesamten übrigen Internetzugriff.

    2. Wenn die VPN-Tunnel unerwartet unterbrochen werden, wird der Internetzugriff für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    **Konfigurationsschritte:**

    1. Wählen Sie das VPN-Profil für Tunnel 1.

        Wenn Sie sich mit Anmeldedaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls gehen Sie zu **VPN Client Profile**, um sich mit Ihren Anmeldedaten anzumelden oder eine Konfigurationsdatei manuell hochzuladen.

        Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus, passen Sie deren Priorität rechts nach Bedarf an und klicken Sie dann auf **Next**.

        ![case 2 profile1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    2. Wählen Sie die Client-Quelle.

        Klicken Sie auf die Registerkarte **All Clients**, legen Sie sie als Client-Quelle für Tunnel 1 fest und klicken Sie dann auf **Next**.

        ![case 2 source1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    3. Wählen Sie das Datenverkehrsziel.

        Klicken Sie auf die Registerkarte **Specified Domain / IP List**, geben Sie wie unten gezeigt Domains einiger gängiger Social-Media- und Streaming-Dienste ein und klicken Sie dann auf **Apply**.

        ![case 2 target1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

    4. Sie werden zum VPN Dashboard weitergeleitet. VPN-Tunnel 1 wurde nun erfolgreich hinzugefügt.

        ![case 2 tunnel 1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

    5. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 1 aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

        ![tunnel 1 kill switch](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

    6. Klicken Sie auf **Add New Tunnel**, um Tunnel 2 hinzuzufügen.

        ![case 2 add tunnel](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

    7. Wählen Sie das VPN-Profil für Tunnel 2.

        Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

        ![case 2 profile2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    8. Wählen Sie die Client-Quelle.

        Klicken Sie auf die Registerkarte **All Clients**, legen Sie sie als Client-Quelle für Tunnel 2 fest und klicken Sie dann auf **Next**.

        ![case 2 source2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

    9. Wählen Sie das Datenverkehrsziel.

        Klicken Sie auf die Registerkarte **All Targets**, legen Sie sie als Datenverkehrsziel für Tunnel 2 fest und klicken Sie dann auf **Apply**.

        ![case 2 target2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

    10. Sie werden zum VPN Dashboard weitergeleitet. VPN-Tunnel 2 wurde nun erfolgreich hinzugefügt.

        ![case 2 tunnel 2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

    11. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 2 aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

        ![tunnel 2 kill switch](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

    12. Klicken Sie auf das Zahnrad-Symbol oben rechts und aktivieren Sie **Enhanced Kill Switch**. Dies stellt sicher, dass der gesamte Datenverkehr über VPN auf das Internet zugreifen muss.

        ![enhanced killswitch1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

        ![enhanced killswitch2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

    13. Klicken Sie auf die mittlere Schaltfläche, um Tunnel 1 und Tunnel 2 zu aktivieren.

        ![case 2 connect](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

    14. Sobald die Verbindung hergestellt ist, zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Datenverkehrsstatistiken, Serveradresse, Listening-Port und virtueller IP-Adresse.

        ![case 2 connected](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

        Jetzt verwenden alle Geräte **VPN Tunnel 1** beim Zugriff auf die angegebenen Domains und **VPN Tunnel 2** für den gesamten übrigen Internetzugriff. Wenn die VPN-Tunnel unerwartet unterbrochen werden, wird der Internetzugriff für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

## Kill Switch {#kill-switch}

!!! Tip "Was ist Kill Switch?"

    Ein VPN Kill Switch hilft zu verhindern, dass Datenverkehr bei einem Ausfall der VPN-Verbindung auf eine unverschlüsselte Internetverbindung ausweicht.

    Wenn **Kill Switch** für einen einzelnen Tunnel aktiviert ist, wird bei einem Verbindungsausfall der Internetzugang für den diesem Tunnel zugewiesenen Datenverkehr blockiert. Für anderen Datenverkehr gelten die Einstellungen unter **All Other Traffic**.

    **Enhanced Kill Switch** blockiert Internetdatenverkehr, der keinem VPN-Tunnel entspricht. Die **Kill Switch**-Einstellung der einzelnen Tunnel wird dadurch nicht außer Kraft gesetzt.

Seit Firmware v4.8 unterstützen GL.iNet-Router die Kill-Switch-Konfiguration sowohl für die globale VPN-Verbindung als auch für jeden einzelnen VPN-Tunnel.

- Informationen zum Einrichten des Kill Switch für die globale VPN-Verbindung (d. h. Enhanced Kill Switch) finden Sie unter [All Other Traffic](#all-other-traffic).

- Informationen zum Einrichten des Kill Switch für jeden einzelnen VPN-Tunnel finden Sie unter [Tunnel-Optionen](#tunnel-options).

## All Other Traffic {#all-other-traffic}

Klicken Sie auf das Zahnrad-Symbol oben rechts, um die Richtlinie für den Datenverkehr einzurichten, der keinem VPN-Tunnel entspricht.

![all other traffic](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Diese Richtlinie steuert, ob Datenverkehr, der keiner Ihrer VPN-Tunnel-Gruppen entspricht, auf das Internet zugreifen kann oder nicht. Sie hat zwei Optionen: **Allow Non-VPN Traffic** und **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Standardmäßig aktiviert, um normalen Internetzugriff für Nicht-VPN-Datenverkehr sicherzustellen.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Zwingt alle Geräte, über ein VPN auf das Internet zuzugreifen. Jeder Datenverkehr, der keinem VPN-Tunnel entspricht, wird blockiert. Diese globale Einstellung setzt den für einzelne VPN-Tunnel konfigurierten Kill Switch nicht außer Kraft.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel-Optionen {#tunnel-options}

Sie können für jeden VPN-Tunnel erweiterte Einstellungen konfigurieren, z. B. VPN Kill Switch, IP-Maskierung und MTU.

Klicken Sie auf das Zahnrad-Symbol in einer Tunnel-Gruppe und wählen Sie **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: Falls aktiviert, wird Datenverkehr, der diesem VPN-Tunnel entspricht, blockiert, wenn die VPN-Verbindung unerwartet ausfällt. Falls deaktiviert, erfolgt für diesen Datenverkehr ein Failover auf den **All Other Traffic** Tunnel.

- **Services from GL.iNet Use VPN**: Falls aktiviert, übertragen die Dienste GoodCloud, DDNS und rtty Pakete über VPN-Tunnel. Diese Option ist standardmäßig deaktiviert, da diese Dienste normalerweise die echte IP-Adresse des Geräts benötigen, um ordnungsgemäß zu funktionieren.

- **Allow Remote Access to the LAN Subnet**: Falls aktiviert, wird der Fernzugriff auf diesen Router und seine LAN-Geräte über das VPN erlaubt. Dazu muss der VPN-Server eine Route zurück zu seinem LAN-Subnetz bekannt geben.

- **IP Masquerading**: Falls aktiviert, werden die Quell-IP-Adressen von LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie diese Option nur bei Site-to-Site-Setups, bei denen die Gegenstelle Ihre LAN-Subnetze kennt.

    Wie unten dargestellt: Wenn IP-Maskierung aktiviert ist und der Laptop (192.168.10.200) im Reise-LAN Datenverkehr über den Tunnel an das NAS (192.168.8.100) im Heim-LAN sendet, schreibt der Reiserouter die Quell-IP von `192.168.10.200` in die Tunneladresse des VPN-Clients `10.1.0.2` um. Die Serverseite sieht dadurch, dass der Datenverkehr vom Client stammt und nicht aus dessen lokalem LAN.

    ![ip masquerading](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/ip_masquerading.png){class="glboxshadow"}

- **MTU**: Der MTU-Wert, den Sie für den Tunnel festlegen, überschreibt die MTU-Einstellungen in der Konfigurationsdatei.

## Tunnel-Priorität {#tunnel-priority}

Um die Tunnel-Priorität anzupassen, klicken Sie auf das Zahnrad-Symbol in einer Tunnel-Gruppe und wählen Sie **Priority**.

![priority1](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Klicken Sie auf das Drei-Linien-Symbol rechts und halten Sie es gedrückt, um die Tunnel neu anzuordnen, und klicken Sie dann auf **Apply**.

![priority2](https://static.gl-inet.com/docs/router/de/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Wenn mehrere Tunnel aktiviert sind, leitet der Router den Datenverkehr nach folgenden Regeln**:

1. Der Datenverkehr wird zuerst mit der Regel des Tunnels mit der höchsten Priorität abgeglichen. Bei einer Übereinstimmung wird er durch diesen Tunnel geleitet; andernfalls wird der Tunnel mit der nächsthöheren Priorität geprüft, und so weiter.

2. Jede Tunnel-Gruppe arbeitet unabhängig. Sobald Datenverkehr einer Tunnel-Regel entspricht, wird er durch diesen Tunnel geleitet, und es erfolgt kein Failover zwischen Tunnel-Gruppen.

3. Innerhalb jeder Tunnel-Gruppe können mehrere Profile ausgewählt werden, um ein Failover innerhalb des Tunnels zu ermöglichen. Wenn das Profil mit der höchsten Priorität in einer Tunnel-Gruppe ausfällt, stellt der Tunnel automatisch eine Verbindung mit dem Profil mit der zweithöchsten Priorität her, und so weiter.

4. Wenn ein VPN-Tunnel unerwartet unterbrochen wird, bestimmt das System anhand des Status des **Kill Switch** dieses Tunnels, ob ein Failover des Datenverkehrs auf den All Other Traffic Tunnel erfolgt.

    - Wenn der Kill Switch aktiviert ist, wird der Datenverkehr blockiert und es erfolgt kein Failover auf den All Other Traffic Tunnel.
    - Wenn der Kill Switch deaktiviert ist, erfolgt ein Failover des Datenverkehrs auf den All Other Traffic Tunnel.

5. Im **All Other Traffic** Tunnel bestimmen verschiedene Modi, ob der Datenverkehr, der nicht dem VPN-Tunnel entspricht, auf das Internet zugreifen kann.

    - **Allow Non-VPN Traffic**: Diese Option ist standardmäßig aktiviert, damit Datenverkehr, der nicht den VPN-Tunneln entspricht, weiterhin über das lokale WAN auf das Internet zugreifen kann.

    - **Enhanced Kill Switch**: Diese Option zwingt alle Geräte, über ein VPN auf das Internet zuzugreifen. Jeder Datenverkehr, der keinem VPN-Tunnel entspricht, wird blockiert. Diese globale Einstellung setzt den für einzelne VPN-Tunnel konfigurierten Kill Switch nicht außer Kraft. Kurz gesagt: Sie verstärkt den Kill Switch und blockiert den regulären Internetzugriff, um IP-Lecks zu verhindern.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
