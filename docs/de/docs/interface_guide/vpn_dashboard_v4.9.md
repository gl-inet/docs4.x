# VPN Dashboard (Firmware v4.9)

**Hinweis**: Diese Anleitung basiert auf Firmware v4.9. Für frühere Versionen siehe [hier](vpn_dashboard.md).

---

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **VPN** -> **VPN Dashboard**.

Das VPN Dashboard zeigt VPN-Verbindungsdetails wie Routing-Regeln, verbundenen Server, Datenverkehrsstatistiken, virtuelle Client-IP und Verbindungsprotokoll an und ermöglicht es Benutzern, erweiterte Einstellungen wie Kill Switch, IP-Maskierung und MTU zu konfigurieren.

Im Vergleich zu Firmware v4.8 enthält v4.9 die folgenden Verbesserungen am VPN Dashboard:

1. **Benutzer können mehrere Profile innerhalb einer Tunnel-Gruppe auswählen und ihre Priorität festlegen**. Der Tunnel versucht, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde.

2. **Jede Tunnel-Gruppe arbeitet unabhängig und führt kein Failover zwischen Gruppen durch**. Wenn alle Profile in einem einzelnen Tunnel keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und des All Other Traffic Tunnels, ob auf das lokale WAN umgeschaltet werden soll.

## Erste Schritte

Wenn Sie diese Seite zum ersten Mal aufrufen und noch keine Tunnel erstellt wurden, wird die Seite wie unten gezeigt angezeigt. Klicken Sie auf **Add VPN Tunnel**, um zu beginnen.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

Sie werden zur Seite **VPN Client Profile** weitergeleitet. Wählen Sie einen VPN-Anbieter aus und melden Sie sich an.

Die aufgelisteten VPN-Anbieter sind in das GL.iNet Router Web-Admin-Panel integriert. Mit einem aktiven Abonnement geben Benutzer einfach ihre Anmeldedaten ein, um sich sofort anzumelden und Konfigurationsdateien für VPN-Verbindungen zu erhalten.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_client_profile.png){class="glboxshadow"}

Wenn Sie andere VPN-Anbieter abonniert haben oder Ihre persönlichen VPN-Konfigurationen hochladen möchten, klicken Sie auf **Add Manually** und laden Sie Ihre Konfigurationen hoch.

Nehmen wir **PureVPN** als Beispiel. Klicken Sie auf PureVPN und melden Sie sich mit gültigen Anmeldedaten an.

![PureVPN1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn1.png){class="glboxshadow"}

![PureVPN2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn2.png){class="glboxshadow"}

Sie erhalten eine Liste von VPN-Profilen. Bei einigen VPN-Dienstanbietern müssen Sie möglicherweise ein VPN-Protokoll oder bevorzugte Server/Städte auswählen, bevor die Liste der Profile erscheint.

Klicken Sie dann unten auf **Go to Dashboard**. Sie werden zum VPN Dashboard weitergeleitet, um Ihren VPN-Tunnel hinzuzufügen und die VPN-Richtlinie einzurichten.

![PureVPN3](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/purevpn3.png){class="glboxshadow"}

??? "Was ist eine VPN-Richtlinie?"

    Eine VPN-Richtlinie definiert, wie Netzwerkverkehr durch VPN-Tunnel geleitet wird, und bestimmt, welcher Datenverkehr über VPN zu Zielzielen geht und welcher direkt über das lokale WAN auf das Internet zugreift.

    Sie ermöglicht es allen Clients oder bestimmten Geräten, auf bestimmte Websites oder das gesamte Internet über eine VPN-Verbindung zuzugreifen, was eine flexible und sichere Netzwerkverwaltung ermöglicht.

Folgen Sie im VPN Dashboard dem Einrichtungsassistenten, um Ihre VPN-Richtlinie zu konfigurieren, einschließlich der Auswahl von VPN-Profil, Datenverkehrsquelle und Datenverkehrsziel.

1. **Wählen Sie das VPN-Profil.**

    Wenn Sie sich zuvor mit Anmeldedaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls gehen Sie zu **VPN Client Profile**, um sich mit Ihren Anmeldedaten anzumelden oder eine Konfigurationsdatei manuell hochzuladen.

    Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt werden, versucht der Tunnel, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und der [All Other Traffic](#all-other-traffic)-Richtlinie, ob auf das lokale WAN umgeschaltet werden soll.

2. **Wählen Sie die Client-Quelle.**

    Es gibt vier Optionen:

    - **All Clients**: Falls ausgewählt, wird der Datenverkehr von allen Geräten dieser Regel entsprechen.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: Falls ausgewählt, wird der Datenverkehr von bestimmten Verbindungstypen (z.B. LAN-Subnetz, Drop-in Gateway, Gastnetzwerk) dieser Regel entsprechen.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: Falls ausgewählt, wird der Datenverkehr von bestimmten Geräten (identifiziert durch MAC-Adresse) dieser Regel entsprechen.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_device.png){class="glboxshadow"}

    - **Exclude Specified Devices**: Falls ausgewählt, wird der Datenverkehr von bestimmten Geräten (identifiziert durch MAC-Adresse) dieser Regel nicht entsprechen.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_device.png){class="glboxshadow"}

3. **Wählen Sie das Zielziel.**

    Es gibt drei Optionen:

    - **All Targets**: Falls ausgewählt, wird der Datenverkehr, der dieser Regel entspricht, zu allen Zielen geleitet.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Falls ausgewählt, wird der Datenverkehr, der dieser Regel entspricht, zu bestimmten Domains oder IP-Adressen geleitet. Sie müssen diese manuell eingeben.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Falls ausgewählt, wird der Datenverkehr, der dieser Regel entspricht, nicht zu bestimmten Domains oder IP-Adressen geleitet. Sie müssen diese manuell eingeben.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

## Verwendungsszenarien

Hier sind zwei Szenarien mit schrittweisen Einrichtungsanweisungen zur Orientierung.

### Szenario 1

**Ziele**:

1. Nur bestimmte Geräte, die mit diesem Router verbunden sind, greifen über VPN auf das Internet zu. Alle anderen Geräte greifen über das lokale WAN auf das Internet zu.

2. Die ausgewählten Geräte müssen ausschließlich die VPN-Verbindung verwenden. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

**Folgen Sie den nachstehenden Schritten, um die VPN-Richtlinie zu konfigurieren.**

1. Wählen Sie das VPN-Profil.

    Wenn Sie sich mit Anmeldedaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls gehen Sie zu **VPN Client Profile**, um sich mit Ihren Anmeldedaten anzumelden oder eine Konfigurationsdatei manuell hochzuladen.

    Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

    ![scenario 1 select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_profiles.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt werden, versucht der Tunnel, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und der [All Other Traffic](#all-other-traffic)-Richtlinie, ob auf das lokale WAN umgeschaltet werden soll.

2. Wählen Sie Client Source.

    Klicken Sie auf die Registerkarte **Specified Devices**, wählen Sie die Geräte aus, die das VPN verwenden werden, und klicken Sie dann auf **Apply**.

    ![scenario 1 select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_specified_devices.png){class="glboxshadow"}

3. Wählen Sie Target Destination.

    Klicken Sie auf die Registerkarte **All Targets**, legen Sie sie als Datenverkehrsziel fest und klicken Sie dann auf **Apply**.

    ![scenario 1 select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Sie werden zum VPN Dashboard weitergeleitet, wo ein VPN-Tunnel hinzugefügt wurde.

    ![scenario 1 dashboard](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_dashboard.png){class="glboxshadow"}

5. Stellen Sie sicher, dass der **Kill Switch** für diesen Tunnel aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![scenario 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch1.png){class="glboxshadow"}

    ![scenario 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_killswitch2.png){class="glboxshadow"}

6. Stellen Sie sicher, dass **Allow Non-VPN Traffic** aktiviert ist. Dies ist standardmäßig aktiviert, um sicherzustellen, dass Datenverkehr, der nicht mit dem VPN-Tunnel übereinstimmt, weiterhin über das lokale WAN auf das Internet zugreifen kann.

    ![scenario 1 allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_allow_nonvpn.png){class="glboxshadow"}

7. Klicken Sie auf die mittlere Schaltfläche, um diesen Tunnel zu aktivieren.

    ![scenario 1 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connect.png){class="glboxshadow"}

8. Sobald verbunden, zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Datenverkehrsstatistiken, Serveradresse, Listening-Port und virtuelle IP-Adresse.

    ![scenario 1 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/1_connected.png){class="glboxshadow"}

    Jetzt greifen nur zwei bestimmte Geräte über VPN auf das Internet zu. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern. Alle anderen Geräte greifen stattdessen über das lokale WAN auf das Internet zu.

### Szenario 2

**Ziele:**

1. Alle Geräte verwenden **VPN Tunnel 1** beim Zugriff auf Domains bestimmter sozialer Medien und Streaming-Dienste und verwenden **VPN Tunnel 2** für den gesamten anderen Internetzugriff.

2. Wenn die VPN-Tunnel unerwartet unterbrochen werden, wird der Internetzugriff für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

**Folgen Sie den nachstehenden Schritten, um die VPN-Richtlinie zu konfigurieren.**

1. Wählen Sie das VPN-Profil für Tunnel 1.

    Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

    ![scenario 2 select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles1.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt werden, versucht der Tunnel, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und der [All Other Traffic](#all-other-traffic)-Richtlinie, ob auf das lokale WAN umgeschaltet werden soll.

2. Wählen Sie Client Source.

    Klicken Sie auf die Registerkarte **All Clients**, legen Sie sie als Client-Quelle für Tunnel 1 fest und klicken Sie dann auf **Apply**.

    ![scenario 2 select source1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Wählen Sie Target Destination.

    Klicken Sie auf die Registerkarte **Specified Domain / IP List**, geben Sie Domains einiger gängiger sozialer Medien und Streaming-Dienste ein, wie unten gezeigt, und klicken Sie dann auf **Apply**.

    ![scenario 2 select target1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_specified_targets.png){class="glboxshadow"}

4. Sie werden zum VPN Dashboard weitergeleitet, wo Tunnel 1 hinzugefügt wurde.

    ![scenario 2 tunnel 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel1.png){class="glboxshadow"}

5. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 1 aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch2.png){class="glboxshadow"}

6. Klicken Sie auf **Add New Tunnel**, um Tunnel 2 hinzuzufügen.

    ![scenario 2 add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_add_tunnel.png){class="glboxshadow"}

7. Wählen Sie das VPN-Profil für Tunnel 2.

    Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Wählen Sie ein oder mehrere Profile aus und passen Sie deren Priorität rechts nach Bedarf an.

    ![scenario 2 select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_profiles2.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt werden, versucht der Tunnel, sich mit jedem Profil in Prioritätsreihenfolge zu verbinden, bis eine Verbindung erfolgreich hergestellt wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, bestimmt das System basierend auf dem Status des Tunnel Kill Switch und der [All Other Traffic](#all-other-traffic)-Richtlinie, ob auf das lokale WAN umgeschaltet werden soll.

8. Wählen Sie Click Source.

    Klicken Sie auf die Registerkarte **All Clients**, legen Sie sie als Client-Quelle für Tunnel 2 fest und klicken Sie dann auf **Apply**.

    ![scenario 2 select source2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_clients.png){class="glboxshadow"}

9. Wählen Sie Target Destination.

    Klicken Sie auf die Registerkarte **All Targets**, legen Sie sie als Datenverkehrsziel für Tunnel 2 fest und klicken Sie dann auf **Apply**.

    ![scenario 2 select target2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_all_targets.png){class="glboxshadow"}

10. Sie werden zum VPN Dashboard weitergeleitet, wo Tunnel 2 hinzugefügt wurde.

    ![scenario 2 tunnel 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_tunnel2.png){class="glboxshadow"}

11. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 2 aktiviert ist. Wenn die VPN-Verbindung unerwartet unterbrochen wird, wird der Internetzugriff für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch3.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_killswitch4.png){class="glboxshadow"}

12. Klicken Sie auf das Zahnrad-Symbol oben rechts und aktivieren Sie **Enhanced Kill Switch**. Dies stellt sicher, dass der gesamte Datenverkehr über VPN auf das Internet zugreifen muss.

    ![enhanced killswitch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch1.png){class="glboxshadow"}

    ![enhanced killswitch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_enhanced_killswitch2.png){class="glboxshadow"}

13. Klicken Sie auf die mittlere Schaltfläche, um Tunnel 1 und Tunnel 2 zu aktivieren.

    ![scenario 2 connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connect.png){class="glboxshadow"}

14. Sobald verbunden, zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Datenverkehrsstatistiken, Serveradresse, Listening-Port und virtuelle IP-Adresse.

    ![scenario 2 connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/2_connected.png){class="glboxshadow"}

    Jetzt verwenden alle Geräte **VPN Tunnel 1** beim Zugriff auf bestimmte Domains und verwenden **VPN Tunnel 2** für den gesamten anderen Internetzugriff. Wenn die VPN-Tunnel unerwartet unterbrochen werden, wird der Internetzugriff für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

## All Other Traffic

Klicken Sie auf das Zahnrad-Symbol oben rechts, um die Richtlinie für den Datenverkehr einzurichten, der nicht mit einem VPN-Tunnel übereinstimmt.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic.png){class="glboxshadow"}

Diese Richtlinie steuert, ob Datenverkehr, der mit keiner Ihrer VPN-Tunnel-Gruppen übereinstimmt, auf das Internet zugreifen kann oder nicht. Sie hat zwei Optionen: **Allow Non-VPN Traffic** und **Enhanced Kill Switch**.

- **Allow Non-VPN Traffic**: Standardmäßig aktiviert, um normalen Internetzugriff für Nicht-VPN-Datenverkehr sicherzustellen.

    ![allow non-vpn traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/allow_non-vpn_traffic.png){class="glboxshadow"}

- **Enhanced Kill Switch**: Zwingt alle Geräte, über VPN auf das Internet zuzugreifen. Jeder Datenverkehr, der nicht mit einem VPN-Tunnel übereinstimmt, wird blockiert. Diese globale Einstellung überschreibt nicht den für einzelne VPN-Tunnel konfigurierten Kill Switch.

    ![enhanced killswitch](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/enhanced_killswitch.png){class="glboxshadow"}

## Tunnel-Priorität

Um die Tunnel-Priorität anzupassen, klicken Sie auf das Zahnrad-Symbol in einer Tunnel-Gruppe und wählen Sie **Priority**.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Klicken Sie auf das Drei-Linien-Symbol rechts und halten Sie es, um die Tunnel neu zu ordnen, und klicken Sie dann auf **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Wenn mehrere Tunnel aktiviert sind, leitet der Router den Datenverkehr nach folgenden Regeln**:

1. Der Datenverkehr versucht zuerst, mit der Regel des Tunnels mit der höchsten Priorität übereinzustimmen. Wenn eine Übereinstimmung vorliegt, wird er durch diesen Tunnel geleitet; andernfalls wird der nächste Prioritäts-Tunnel versucht, und so weiter.

2. Jede Tunnel-Gruppe arbeitet unabhängig. Sobald Datenverkehr mit einer Tunnel-Regel übereinstimmt, wird er durch diesen Tunnel geleitet und es erfolgt kein Failover zwischen Tunnel-Gruppen.

3. Innerhalb jeder Tunnel-Gruppe können mehrere Profile ausgewählt werden, um Intra-Tunnel-Failover zu ermöglichen. Wenn das Profil mit der höchsten Priorität in einer Tunnel-Gruppe ausfällt, stellt der Tunnel automatisch eine Verbindung mit dem Profil mit der zweithöchsten Priorität her, und so weiter.

4. Wenn ein VPN-Tunnel unerwartet unterbrochen wird, bestimmt das System basierend darauf, ob der **Kill Switch** dieses Tunnels aktiviert ist, ob der Datenverkehr auf den All Other Traffic Tunnel umgeleitet wird.

    - Wenn der Kill Switch aktiviert ist, wird der Datenverkehr blockiert und nicht auf den All Other Traffic Tunnel umgeleitet.
    - Wenn der Kill Switch deaktiviert ist, wird der Datenverkehr auf den All Other Traffic Tunnel umgeleitet.

5. Im **All Other Traffic** Tunnel bestimmen verschiedene Modi, ob der Datenverkehr, der nicht mit dem VPN-Tunnel übereinstimmt, auf das Internet zugreifen kann.

    - **Allow Non-VPN Traffic**: Dies ist standardmäßig aktiviert, um sicherzustellen, dass Datenverkehr, der nicht mit den VPN-Tunneln übereinstimmt, weiterhin über das lokale WAN auf das Internet zugreifen kann.

    - **Enhanced Kill Switch**: Dies zwingt alle Geräte, über VPN auf das Internet zuzugreifen. Jeder Datenverkehr, der nicht mit einem VPN-Tunnel übereinstimmt, wird blockiert. Diese globale Einstellung überschreibt nicht den für einzelne VPN-Tunnel konfigurierten Kill Switch. Kurz gesagt, es verstärkt den Kill Switch und blockiert den regulären Internetzugriff, um IP-Lecks zu verhindern.

## Tunnel-Optionen

Sie können erweiterte Einstellungen für jeden VPN-Tunnel konfigurieren, wie Kill Switch, IP-Maskierung und MTU.

Klicken Sie auf das Zahnrad-Symbol in einer Tunnel-Gruppe und wählen Sie **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: Falls aktiviert, wird Datenverkehr, der diesem VPN-Tunnel entspricht, blockiert, wenn die VPN-Verbindung unerwartet fehlschlägt. Falls deaktiviert, wird dieser Datenverkehr auf den **All Other Traffic** Tunnel umgeleitet.

- **Services from GL.iNet Use VPN**: Falls aktiviert, übertragen GoodCloud, DDNS und rtty-Dienste Pakete durch VPN-Tunnel. Diese Option ist standardmäßig deaktiviert, da diese Dienste normalerweise die echte IP-Adresse des Geräts benötigen, um ordnungsgemäß zu funktionieren.

- **Allow Remote Access to the LAN Subnet**: Falls aktiviert, wird der Fernzugriff auf diesen Router und seine LAN-Geräte über VPN erlaubt. Es erfordert, dass der VPN-Server eine Route zurück zu seinem LAN-Subnetz bewirbt.

- **IP Masquerading**: Falls aktiviert, werden die Quell-IP-Adressen von LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie dies nur für Site-to-Site-Setups, bei denen der Remote-Peer Ihre LAN-Subnetze kennt.

- **MTU**: Der MTU-Wert, den Sie für den Tunnel festlegen, überschreibt die MTU-Einstellungen in der Konfigurationsdatei.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
