# VPN Dashboard (Firmware v4.9)

**Hinweis**: Diese Anleitung basiert auf Firmware v4.9. Für frühere Versionen siehe [hier](vpn_dashboard.md).

---

Gehen Sie auf der linken Seite des web Admin Panel zu **VPN** -> **VPN Dashboard**. 

Das VPN Dashboard zeigt Details zu VPN-Verbindungen an, darunter Routing-Regeln, den verbundenen Server, Verkehrsstatistiken, die virtuelle Client-IP und das Verbindungsprotokoll. Außerdem können Benutzer erweiterte Einstellungen wie den VPN Kill Switch, die IP-Maskierung und die MTU konfigurieren.

Im Vergleich zu Firmware v4.8 enthält v4.9 die folgenden Verbesserungen im VPN Dashboard:

1. **Benutzer können mehrere Profile innerhalb einer Tunnelgruppe auswählen und deren Priorität festlegen**. Der Tunnel versucht, die Verbindung mit jedem Profil in Prioritätsreihenfolge herzustellen, bis eine Verbindung erfolgreich aufgebaut wurde.

2. **Jede Tunnelgruppe arbeitet unabhängig und führt kein Failover zwischen Gruppen durch**. Wenn alle Profile in einem einzelnen Tunnel keine Verbindung herstellen können, entscheidet das System anhand des Status des Kill Switches des Tunnels und des Tunnels **All Other Traffic**, ob auf das lokale WAN umgeschaltet wird.

## Erste Schritte

Wenn Sie diese Seite zum ersten Mal öffnen und noch keine Tunnel erstellt wurden, wird die Seite wie unten dargestellt angezeigt. Klicken Sie auf **Add VPN Tunnel**, um zu beginnen.

![getting started](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/getting_started.png){class="glboxshadow"}

**Wählen Sie einen VPN-Anbieter aus**. Die aufgeführten VPN-Anbieter sind in das web Admin Panel des GL.iNet-Routers integriert. Mit einem aktiven Abonnement geben Benutzer einfach ihre Zugangsdaten ein, melden sich sofort an und erhalten die Konfigurationsdateien für VPN-Verbindungen.

![select vpn provider](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_client.png){class="glboxshadow"}

Wenn Sie andere VPN-Anbieter abonniert haben oder Ihre persönlichen VPN-Konfigurationen hochladen möchten, wechseln Sie zu **VPN Client Profile**, um die Konfiguration manuell vorzunehmen.

Hier ein Beispiel mit **Hide.me**. Melden Sie sich mit Ihren Hide.me-Zugangsdaten an.

![hide.me login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/vpn_login.png){class="glboxshadow"}

**Wählen Sie einen VPN-Server aus**. Mit diesem Server verbindet sich Ihr Gerät über diesen VPN-Tunnel, und Ihre öffentliche IP-Adresse erscheint so, als stamme sie vom Standort des ausgewählten Servers. Klicken Sie auf **Apply**.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_vpn_server.png){class="glboxshadow"}

Die Verbindung wird automatisch hergestellt. Klicken Sie auf **Done**.

![successful networking](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/successful_networking.png){class="glboxshadow"}

Sie werden zum VPN Dashboard weitergeleitet, in dem VPN Tunnel 1 aktiviert und verbunden wurde. 

![tunnel 1 global policy](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel1_global_policy.png){class="glboxshadow"}

**In diesem Beispiel greifen alle mit diesem Router verbundenen Clients über diesen VPN-Tunnel auf das Internet zu.**

Wenn Sie die VPN-Richtlinie konfigurieren möchten, lesen Sie bitte [VPN-Richtlinie](#vpn-richtlinie).

**All Other Traffic** ist ein voraktivierter Tunnel, der unten im VPN Dashboard angezeigt wird. Klicken Sie [hier](#all-other-traffic) für Details.

## Tunneldetails

Im VPN Dashboard wird jeder einzelne VPN-Tunnel wie unten dargestellt angezeigt. Dort sehen Sie detaillierte VPN-Tunnelinformationen wie Routing-Regeln, verbundenen Server, Verkehrsstatistiken, Serveradresse, Listening-Port, virtuelle Client-IP und Verbindungsprotokoll. Sie können den VPN-Tunnel aktivieren oder deaktivieren und die Tunneleinstellungen oben in der Tunnelgruppe konfigurieren.

![tunnel details](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_details.png){class="glboxshadow"}

## VPN-Richtlinie

Eine VPN-Richtlinie definiert, wie Netzwerkverkehr über VPN-Tunnel geleitet wird. Sie legt fest, welcher Datenverkehr über VPN zu den Zielzielen geleitet wird und welcher direkt über das lokale WAN auf das Internet zugreift.

Damit können alle Clients oder bestimmte Geräte über eine VPN-Verbindung auf festgelegte Websites oder auf das gesamte Internet zugreifen, was eine flexible und sichere Netzwerkverwaltung ermöglicht.

### Schnelleinrichtung

Klicken Sie im VPN Dashboard auf **Add New Tunnel** oder auf den mittleren Bereich eines vorhandenen VPN-Tunnels. 

![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/add_new_tunnel.png){class="glboxshadow"}

Folgen Sie dann dem Einrichtungsassistenten, um Ihre VPN-Richtlinie zu konfigurieren, einschließlich der Auswahl von VPN-Profil, Datenverkehrsquelle und Datenverkehrsziel.

1. **VPN-Profil auswählen.** 

    Wenn Sie sich bereits mit Zugangsdaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls wechseln Sie zu **VPN Client Profile**, um sich mit Ihren Zugangsdaten anzumelden oder manuell eine Konfigurationsdatei hochzuladen.

    Nehmen wir [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} als Beispiel. Melden Sie sich mit Ihren Dienst-Zugangsdaten an, und Sie sehen eine Liste von VPN-Profilen. Wählen Sie ein oder mehrere Profile aus und passen Sie rechts bei Bedarf deren Priorität an.

    ![select profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/select_profile.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt sind, versucht der Tunnel, die Verbindung mit jedem Profil in Prioritätsreihenfolge herzustellen, bis eine Verbindung erfolgreich aufgebaut wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, entscheidet das System anhand des Status des Kill Switches des Tunnels und des Tunnels [All Other Traffic](#all-other-traffic), ob auf das lokale WAN umgeschaltet wird.

2. **Client-Quelle auswählen.** 

    Es gibt vier Optionen:

    - **All Clients**: Wenn diese Option ausgewählt ist, entspricht der Datenverkehr aller Geräte dieser Regel.
    ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_clients.png){class="glboxshadow"}

    - **Specified Connection Types**: Wenn diese Option ausgewählt ist, entspricht der Datenverkehr der angegebenen Verbindungstypen (z. B. LAN subnet, Drop-in Gateway, Guest Network) dieser Regel.
    ![specified connection types](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_connection.png){class="glboxshadow"}

    - **Specified Devices**: Wenn diese Option ausgewählt ist, entspricht der Datenverkehr angegebener Geräte (identifiziert über die MAC-Adresse) dieser Regel.
    ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_devices.png){class="glboxshadow"}

    - **Exclude Specified Devices**: Wenn diese Option ausgewählt ist, entspricht der Datenverkehr angegebener Geräte (identifiziert über die MAC-Adresse) dieser Regel nicht.
    ![exclude specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_devices.png){class="glboxshadow"}

3. **Datenverkehrsziel auswählen**. 

    Es gibt drei Optionen:

    - **All Targets**: Wenn diese Option ausgewählt ist, wird der Datenverkehr, der dieser Regel entspricht, zu allen Zielen geleitet.
    ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_targets.png){class="glboxshadow"}

    - **Specified Domain / IP List**: Wenn diese Option ausgewählt ist, wird der Datenverkehr, der dieser Regel entspricht, zu den angegebenen Domains oder IP-Adressen geleitet. Diese müssen manuell eingegeben werden.
    ![specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/specified_domain_ip.png){class="glboxshadow"}

    - **Exclude specified Domain / IP List**: Wenn diese Option ausgewählt ist, wird der Datenverkehr, der dieser Regel entspricht, nicht zu den angegebenen Domains oder IP-Adressen geleitet. Diese müssen manuell eingegeben werden.
    ![exclude specified domain ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/exclude_specified_domain_ip.png){class="glboxshadow"}

### Anwendungsszenarien

Nachfolgend finden Sie zwei Szenarien mit Schritt-für-Schritt-Anleitungen als Referenz.

**Szenario 1** 

**Ziele**:

1. Nur bestimmte mit diesem Router verbundene Geräte greifen über das VPN auf das Internet zu. Alle anderen Geräte greifen über das lokale WAN auf das Internet zu.

2. Die ausgewählten Geräte dürfen nur die VPN-Verbindung verwenden. Wenn die VPN-Verbindung unerwartet getrennt wird, wird der Internetzugang für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

**Führen Sie die folgenden Schritte aus, um die VPN-Richtlinie zu konfigurieren.**

1. Wählen Sie das VPN-Profil aus. 

    Wenn Sie sich bereits mit Zugangsdaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls wechseln Sie zu **VPN Client Profile**, um sich mit Ihren Zugangsdaten anzumelden oder manuell eine Konfigurationsdatei hochzuladen.

    Nehmen wir [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} als Beispiel. Melden Sie sich mit Ihren Dienst-Zugangsdaten an, und Sie sehen eine Liste von VPN-Profilen.

    ![select profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile1.png){class="glboxshadow"}

    Wählen Sie ein oder mehrere Profile aus und passen Sie rechts bei Bedarf deren Priorität an.

    ![select profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_profile2.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt sind, versucht der Tunnel, die Verbindung mit jedem Profil in Prioritätsreihenfolge herzustellen, bis eine Verbindung erfolgreich aufgebaut wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, entscheidet das System anhand des Status des Kill Switches des Tunnels und des Tunnels [All Other Traffic](#all-other-traffic), ob auf das lokale WAN umgeschaltet wird.

2. Wählen Sie **Specified Devices** als Datenverkehrsquelle aus, markieren Sie dann die Geräte, die das VPN verwenden sollen, und klicken Sie auf **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_source.png){class="glboxshadow"}

3. Wählen Sie **All Targets** als Datenverkehrsziel aus und klicken Sie dann auf **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_target.png){class="glboxshadow"}

4. Sie werden zum VPN Dashboard weitergeleitet, wo ein VPN-Tunnel hinzugefügt wurde. 

    ![policy apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_apply.jpg){class="glboxshadow"}

5. Stellen Sie sicher, dass der **Kill Switch** für diesen Tunnel aktiviert ist. Wenn die VPN-Verbindung unerwartet getrennt wird, wird der Internetzugang für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch1.png){class="glboxshadow"}

    ![kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_killswitch2.png){class="glboxshadow"}
    
6. Stellen Sie sicher, dass **All Other Traffic** aktiviert ist und der Modus auf **Allow Non-VPN Traffic** gesetzt ist. Dadurch wird sichergestellt, dass Datenverkehr, der den oben genannten VPN-Tunneln nicht entspricht, weiterhin über das lokale WAN auf das Internet zugreifen kann.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_all_other_traffic.png){class="glboxshadow"}

7. Betätigen Sie den Schalter, um diesen Tunnel zu aktivieren.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_start.png){class="glboxshadow"}

8. Nach erfolgreicher Verbindung zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Verkehrsstatistiken, Serveradresse, Listening-Port und virtueller IP-Adresse.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case1_connected.png){class="glboxshadow"}

    Jetzt greifen nur die zwei angegebenen Geräte über VPN auf das Internet zu. Wenn die VPN-Verbindung unerwartet getrennt wird, wird der Internetzugang für diese Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern. Alle anderen Geräte greifen stattdessen über das lokale WAN auf das Internet zu.

**Szenario 2**

**Ziele:** 

1. Alle Geräte verwenden beim Zugriff auf Domains bestimmter Social-Media- und Streaming-Dienste **VPN Tunnel 1** und für jeden anderen Internetzugriff **VPN Tunnel 2**.

2. Wenn die VPN-Tunnel unerwartet getrennt werden, wird der Internetzugang für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

**Führen Sie die folgenden Schritte aus, um die VPN-Richtlinie zu konfigurieren.**

1. Wählen Sie das VPN-Profil für Tunnel 1 aus. 

    Wenn Sie sich bereits mit Zugangsdaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls wechseln Sie zu **VPN Client Profile**, um sich mit Ihren Zugangsdaten anzumelden oder manuell eine Konfigurationsdatei hochzuladen.

    Nehmen wir [Hide.me](https://hide.me/en/?friend=glinet){target="_blank"} als Beispiel. Melden Sie sich mit Ihren Dienst-Zugangsdaten an, und Sie sehen eine Liste von VPN-Profilen. 

    ![hide.me profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme1.png){class="glboxshadow"}
    
    Wählen Sie ein oder mehrere Profile aus und passen Sie rechts bei Bedarf deren Priorität an.

    ![hide.me profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_hideme2.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt sind, versucht der Tunnel, die Verbindung mit jedem Profil in Prioritätsreihenfolge herzustellen, bis eine Verbindung erfolgreich aufgebaut wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, entscheidet das System anhand des Status des Kill Switches des Tunnels und des Tunnels [All Other Traffic](#all-other-traffic), ob auf das lokale WAN umgeschaltet wird.

2. Wählen Sie **All Clients** als Datenverkehrsquelle für Tunnel 1 aus und klicken Sie dann auf **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

3. Wählen Sie **Specified Domain / IP List** als Datenverkehrsziel für Tunnel 1 aus. Geben Sie wie unten gezeigt die Domains einiger gängiger Social-Media- und Streaming-Dienste ein und klicken Sie dann auf **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target1.png){class="glboxshadow"}

4. Sie werden zum VPN Dashboard weitergeleitet, wo Tunnel 1 hinzugefügt wurde. 

    ![tunnel 1 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_apply.png){class="glboxshadow"}

5. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 1 aktiviert ist. Wenn die VPN-Verbindung unerwartet getrennt wird, wird der Internetzugang für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![tunnel 1 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch1.png){class="glboxshadow"}

    ![tunnel 1 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel1_killswitch2.png){class="glboxshadow"}
    
6. Klicken Sie auf **Add New Tunnel**, um Tunnel 2 hinzuzufügen.

    ![add new tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_add_tunnel2.png){class="glboxshadow"}

7. Wählen Sie das VPN-Profil für Tunnel 2 aus. 

    Wenn Sie sich bereits mit Zugangsdaten eines integrierten VPN-Dienstes angemeldet oder eine Konfigurationsdatei hochgeladen haben, werden die verfügbaren Profile hier aufgelistet. Andernfalls wechseln Sie zu **VPN Client Profile**, um sich mit Ihren Zugangsdaten anzumelden oder manuell eine Konfigurationsdatei hochzuladen.

    Nehmen wir [PureVPN](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"} als Beispiel. Melden Sie sich mit Ihren Dienst-Zugangsdaten an, und Sie sehen eine Liste von VPN-Profilen. 
    
    ![purevpn profile1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn1.png){class="glboxshadow"}
    
    Wählen Sie ein oder mehrere Profile aus und passen Sie rechts bei Bedarf deren Priorität an.

    ![purevpn profile2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_purevpn2.png){class="glboxshadow"}

    **Hinweis**: Wenn mehrere Profile ausgewählt sind, versucht der Tunnel, die Verbindung mit jedem Profil in Prioritätsreihenfolge herzustellen, bis eine Verbindung erfolgreich aufgebaut wurde. Wenn alle Profile innerhalb eines einzelnen Tunnels keine Verbindung herstellen können, entscheidet das System anhand des Status des Kill Switches des Tunnels und des Tunnels [All Other Traffic](#all-other-traffic), ob auf das lokale WAN umgeschaltet wird.

8. Wählen Sie **All Clients** als Datenverkehrsquelle für Tunnel 2 aus und klicken Sie dann auf **Apply**.

    ![select source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_source.png){class="glboxshadow"}

9. Wählen Sie **All Targets** als Datenverkehrsziel für Tunnel 2 aus und klicken Sie dann auf **Apply**.

    ![select target](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_target2.png){class="glboxshadow"}

10. Sie werden zum VPN Dashboard weitergeleitet, wo Tunnel 2 hinzugefügt wurde. 

    ![tunnel 2 apply](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_apply.png){class="glboxshadow"}

11. Stellen Sie sicher, dass der **Kill Switch** für Tunnel 2 aktiviert ist. Wenn die VPN-Verbindung unerwartet getrennt wird, wird der Internetzugang für Datenverkehr, der diesem Tunnel entspricht, blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

    ![tunnel 2 kill switch1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch1.png){class="glboxshadow"}

    ![tunnel 2 kill switch2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_tunnel2_killswitch2.png){class="glboxshadow"}

12. Deaktivieren Sie **All Other Traffic**. Stellen Sie sicher, dass der Modus auf **Enhanced Kill Switch** gesetzt ist. Dadurch wird sichergestellt, dass sämtlicher Datenverkehr nur über das VPN auf das Internet zugreifen muss.

    ![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_all_other_traffic.png){class="glboxshadow"}

13. Betätigen Sie den Schalter, um Tunnel 1 und Tunnel 2 zu aktivieren.

    ![start connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_start.png){class="glboxshadow"}

14. Nach erfolgreicher Verbindung zeigt die Seite die VPN-Verbindungsdetails an, einschließlich VPN-Richtlinie, Verkehrsstatistiken, Serveradresse, Listening-Port und virtueller IP-Adresse.

    ![connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/case2_connected.png){class="glboxshadow"}

    Jetzt verwenden alle Geräte beim Zugriff auf die angegebenen Domains **VPN Tunnel 1** und für allen anderen Internetzugriff **VPN Tunnel 2**. Wenn die VPN-Tunnel unerwartet getrennt werden, wird der Internetzugang für alle Geräte blockiert, um DNS-Lecks und IP-Tracking zu verhindern.

## All Other Traffic

Diese Option steuert, ob Datenverkehr, der keiner der oben genannten VPN-Tunnelgruppen entspricht, auf das Internet zugreifen kann. Sie ist standardmäßig aktiviert, damit Datenverkehr, der nicht über VPN geleitet wird, normal auf das Internet zugreifen kann.

Wenn die Option aktiviert ist, kann nicht zugeordneter Datenverkehr weiterhin auf das Internet zugreifen.

![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

Wenn die Option deaktiviert ist, darf nur Datenverkehr, der über VPN geleitet wird, auf das Internet zugreifen. Sämtlicher Nicht-VPN-Datenverkehr sowie Datenverkehr, der per Failover von VPN-Verbindungen kommt, werden blockiert. Diese Option überschreibt nicht den individuellen Kill Switch jedes VPN-Tunnels.

![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

## Tunnel-Priorität

Um die Tunnel-Priorität anzupassen, klicken Sie auf das Zahnradsymbol in einer Tunnelgruppe und wählen **Sort** aus.

![priority1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority1.png){class="glboxshadow"}

Klicken und halten Sie rechts das Symbol mit den drei Linien, um die Tunnel neu anzuordnen, und klicken Sie dann auf **Apply**.

![priority2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/priority2.png){class="glboxshadow"}

**Wenn mehrere Tunnel aktiviert sind, leitet der Router den Datenverkehr gemäß den folgenden Regeln weiter**:

1. Der Datenverkehr versucht zuerst, der Regel des Tunnels mit der höchsten Priorität zu entsprechen. Wenn er übereinstimmt, wird er über diesen Tunnel geleitet. Andernfalls wird der Tunnel mit der nächsthöheren Priorität geprüft und so weiter.

2. Jede Tunnelgruppe arbeitet unabhängig. Sobald Datenverkehr einer Tunnelregel entspricht, wird er über diesen Tunnel geleitet und führt kein Failover zwischen Tunnelgruppen durch.

3. Innerhalb jeder Tunnelgruppe können mehrere Profile ausgewählt werden, um ein internes Failover im Tunnel zu ermöglichen. Wenn das Profil mit der höchsten Priorität innerhalb einer Tunnelgruppe ausfällt, verbindet sich der Tunnel automatisch mit dem Profil mit der zweithöchsten Priorität usw.

4. Wenn ein VPN-Tunnel unerwartet getrennt wird, entscheidet das System anhand des Status des **Kill Switches** dieses Tunnels, ob der Datenverkehr per Failover zum Tunnel **All Other Traffic** geleitet wird. 

    - Wenn der Kill Switch aktiviert ist, wird der Datenverkehr blockiert und nicht per Failover zum Tunnel **All Other Traffic** geleitet.
    - Wenn der Kill Switch deaktiviert ist, wird der Datenverkehr per Failover zum Tunnel **All Other Traffic** geleitet.

5. Der Tunnel **All Other Traffic** ist standardmäßig aktiviert, damit Datenverkehr, der den VPN-Tunneln nicht entspricht, weiterhin auf das Internet zugreifen kann.

    - Wenn er aktiviert ist, wird nicht zugeordneter Datenverkehr oder Failover-Datenverkehr über das lokale WAN geleitet.
    - Wenn er deaktiviert ist, verstärkt er den Kill Switch und blockiert den regulären Internetzugang, um IP-Lecks zu verhindern.

## Tunnel-Optionen

Sie können für jeden VPN-Tunnel erweiterte Einstellungen wie den VPN Kill Switch, die IP-Maskierung und die MTU konfigurieren.

Klicken Sie auf das Zahnradsymbol in einer Tunnelgruppe und wählen Sie **Options**.

![tunnel options1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options1.png){class="glboxshadow"}

![tunnel options2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/tunnel_options2.png){class="glboxshadow"}

- **Kill Switch**: Wenn aktiviert, wird Datenverkehr, der diesem VPN-Tunnel entspricht, blockiert, falls die VPN-Verbindung unerwartet ausfällt. Wenn deaktiviert, wird dieser Datenverkehr per Failover zum Tunnel **All Other Traffic** geleitet.

- **Services from GL.iNet Use VPN**: Wenn aktiviert, übertragen GoodCloud-, DDNS- und rtty-Dienste ihre Pakete über VPN-Tunnel. Diese Option ist standardmäßig deaktiviert, da diese Dienste normalerweise die echte IP-Adresse des Geräts benötigen, um ordnungsgemäß zu funktionieren.

- **Allow Remote Access to the LAN Subnet**: Wenn aktiviert, ist der Fernzugriff auf diesen Router und seine LAN-Geräte über das VPN erlaubt. Dafür muss der VPN-Server eine Route zurück zu seinem LAN-Subnetz ankündigen.

- **IP Masquerading**: Wenn aktiviert, werden die Quell-IP-Adressen der LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie dies nur für Site-to-Site-Einrichtungen, bei denen der entfernte Kommunikationspartner Ihre LAN-Subnetze kennt.

- **MTU**: Der MTU-Wert, den Sie für den Tunnel festlegen, überschreibt die MTU-Einstellungen in der Konfigurationsdatei.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
