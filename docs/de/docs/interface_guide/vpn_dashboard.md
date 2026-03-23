# VPN Dashboard

**Hinweis**: Diese Anleitung basiert auf Firmware v4.8. Für frühere Versionen lesen Sie bitte [hier](vpn_dashboard_v4.7.md) weiter.

---

Gehen Sie auf der linken Seite des webbasierten Admin Panels zu **VPN** -> **VPN Dashboard**.

Das VPN Dashboard zeigt Verbindungsdetails wie Tunnel-Regeln, Serveradresse, Datenverkehrsstatistiken, virtuelle Client-IP und Verbindungsprotokoll an. Außerdem können hier erweiterte Einstellungen wie VPN Kill Switch, IP-Maskierung und MTU konfiguriert werden.

Sie können außerdem mehrere VPN-Verbindungen für Multi-Tunnel-Szenarien aktivieren.

## Einrichtungsassistent

Klicken Sie oben links auf das Buchsymbol und folgen Sie dem VPN Setup Wizard, um die VPN-Konfiguration schnell abzuschließen.

![vpn wizard 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_1.png){class="glboxshadow"}

![vpn wizard 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_wizard_2.png){class="glboxshadow"}

**Hinweis**: Der VPN Setup Wizard ist nur für die integrierten VPN-Dienste vorgesehen, darunter AzireVPN, Hide.me, IPVanish, Mullvad, NordVPN, PIA und Surfshark. Für andere VPN-Dienste überspringen Sie den Assistenten und richten das VPN manuell unter [OpenVPN Client](openvpn_client.md){target="_blank"} oder [WireGuard Client](wireguard_client.md){target="_blank"} ein.

Hier ein Beispiel mit **Hide.me**. Melden Sie sich mit Ihren Hide.me-Zugangsdaten an.

![vpn login](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_login.png){class="glboxshadow"}

Wählen Sie einen VPN-Server aus und klicken Sie auf **Apply**. Dies ist der Server, mit dem sich dieser VPN-Tunnel verbindet. Ihre öffentliche IP-Adresse erscheint dann so, als stamme sie vom Standort des ausgewählten Servers.

![select server](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/select_server.png){class="glboxshadow"}

Die Verbindung wird automatisch aufgebaut. Nach erfolgreicher Verbindung sehen Sie im VPN Dashboard, dass ein VPN-Tunnel aktiviert wurde.

![vpn connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected.png){class="glboxshadow"}

Angezeigt werden das aktuell verwendete VPN-Protokoll (z. B. WireGuard), die Konfigurationsdatei, Serveradresse, Listening-Port des Servers, Datenverkehrsstatistiken und die virtuelle Client-IP. Unten rechts können Benutzer das Verbindungsprotokoll einsehen.

Alle verbundenen Clients greifen über diesen VPN-Tunnel auf das Internet zu.

Wenn Sie VPN-Richtlinien konfigurieren möchten, lesen Sie bitte [Policy Mode](#policy-mode).

## VPN Mode

Klicken Sie im VPN Dashboard oben rechts auf die Schaltfläche, um zwischen den VPN-Modi zu wechseln.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/vpn_mode.png){class="glboxshadow"}

Es stehen zwei Modi zur Verfügung: **Global Mode** und **Policy Mode**.

![vpn mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/global_mode.png){class="glboxshadow"}

### Global Mode

In diesem Modus wird der gesamte Datenverkehr durch den VPN-Tunnel geleitet, und es kann nur eine VPN-Client-Instanz aktiviert werden.

Er eignet sich ideal für Szenarien, in denen der gesamte Client-Datenverkehr über einen einzelnen VPN-Server geleitet wird, etwa für einheitliche Netzwerksicherheit oder regionalspezifischen Inhaltszugriff.

Im folgenden Beispiel verbindet sich der Router per WireGuard mit einem australischen Server. Der gesamte Datenverkehr verbundener Clients wird durch diesen VPN-Tunnel geleitet.

![connected global mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-global-mode.png){class="glboxshadow"}

### Policy Mode

In diesem Modus kann sich der Router mit mehreren VPN-Servern verbinden, und Sie können benutzerdefinierte Routing-Regeln für verschiedene Clients oder Datenverkehrsziele festlegen.

Er eignet sich für Anwendungsfälle, die ein flexibles Datenverkehrsmanagement erfordern, z. B. wenn unterschiedlicher Datenverkehr über mehrere VPN-Server an verschiedene Ziele geleitet werden soll.

Wechseln Sie den VPN Mode zu Policy Mode und klicken Sie auf **Apply**.

![policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_mode.png){class="glboxshadow"}

Nach dem Umschalten wird, falls das VPN noch nicht aktiviert ist, die Seite wie unten dargestellt angezeigt. Sie enthält die drei Bereiche Primary Tunnel, Add Tunnel und All Other Traffic.

![policy mode no vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/policy_no_vpn_file.png){class="glboxshadow"}

Klicken Sie auf den entsprechenden Bereich, um mehr zu erfahren.

- [Primary Tunnel](#primary-tunnel)
- [Add Tunnel](#add-tunnel)
- [All Other Traffic](#all-other-traffic)

#### Primary Tunnel

Der Primary Tunnel ist ein <u>voreingestellter</u> Tunnel im Policy Mode. Er hat die höchste Priorität. Wenn es mehr als einen Tunnel gibt, können Sie die [Tunnel-Priorität](#tunnel-priority) ändern.

In diesem Tunnel können Sie die Tunnel-Regel über drei Faktoren anpassen:

1. **From**: Bezieht sich auf die Datenverkehrsquelle, also den Datenverkehr, der über diesen Tunnel geleitet werden soll.

    Klicken Sie auf das ausgegraute Feld, um die Datenverkehrsquelle auszuwählen.

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_1.png){class="glboxshadow"}

    ![traffic source](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_from_2.jpg){class="glboxshadow"}
        
    - **All Clients**: Wenn ausgewählt, entspricht der Datenverkehr aller Geräte dieser Regel.
        
        ![all clients](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_clients.jpg){class="glboxshadow"}

    - **Specified Connection Types**: Wenn ausgewählt, entspricht Datenverkehr bestimmter Verbindungstypen (z. B. LAN-Subnetz, Drop-in Gateway, Guest Network) dieser Regel.
        
        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_1.jpg){class="glboxshadow"}

        Wenn Sie auf diesem Router den OpenVPN-Server oder WireGuard-Server aktiviert haben, erscheinen unter Specified Connection Types zusätzliche Optionen. Das ist nützlich für [VPN Cascading](../tutorials/how_to_use_vpn_cascading_on_glinet_routers.md).

        ![specified connection](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_connection_types_2.png){class="glboxshadow"}

    - **Specified Devices**: Wenn ausgewählt, entspricht der Datenverkehr bestimmter Geräte (identifiziert über die MAC-Adresse) dieser Regel.

        ![specified devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_devices.jpg){class="glboxshadow"}

    - **Exclude Specified Devices**: Wenn ausgewählt, entspricht der Datenverkehr bestimmter Geräte (identifiziert über die MAC-Adresse) dieser Regel **NICHT**.

        ![exclude devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_devices.jpg){class="glboxshadow"}

2. **To**: Bezieht sich auf die Datenverkehrsziele.

    Klicken Sie auf das ausgegraute Feld, um die Datenverkehrsziele auszuwählen.

    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_1.png){class="glboxshadow"}
    
    ![traffic destination](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_to_2.png){class="glboxshadow"}

    - **All Targets**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, zu allen Zielen geleitet.

        ![all targets](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_targets.png){class="glboxshadow"}
    
    - **Specified Domain / IP List**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, zu den angegebenen Domains oder IP-Adressen geleitet. Diese müssen manuell eingegeben werden.

        ![specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_manual.png){class="glboxshadow"}

        Oder wechseln Sie den **Input Mode** von Manual zu Subscription URL und geben Sie einen URL-Link ein.

        ![specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/specified_domain_ip_subscription.png){class="glboxshadow"}

        !!! Note
        
            - Wenn Sie Subscribe URL auswählen, werden die Domainnamen oder IPs unter dieser URL täglich automatisch aktualisiert.

            - Stellen Sie sicher, dass Sie die richtige URL eingeben. Die URL-Prüfung verifiziert die Gültigkeit der Domainnamen oder IP-Adressen. [Mehr erfahren](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

    - **Exclude Specified Domain / IP List**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, **NICHT** zu den angegebenen Domains oder IP-Adressen geleitet. Diese müssen manuell eingegeben werden.

        ![exclude specified domain/IP manual](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_manual.png){class="glboxshadow"}

        Oder wechseln Sie den **Input Mode** von Manual zu Subscription URL und geben Sie einen URL-Link ein.

        ![exclude specified domain/IP subscription](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/exclude_domain_ip_subscription.png){class="glboxshadow"} 

        !!! Note
        
            - Wenn Sie Subscribe URL auswählen, werden die Domainnamen oder IPs unter dieser URL täglich automatisch aktualisiert.

            - Stellen Sie sicher, dass Sie die richtige URL eingeben. Die URL-Prüfung verifiziert die Gültigkeit der Domainnamen oder IP-Adressen. [Mehr erfahren](../tutorials/how_to_configure_domain_and_ip_filtering_rules_for_glinet_routers_via_an_online_text_file.md){target="_blank"}

3. **Via**: Bezieht sich auf die Routing-Methode des Datenverkehrs, also darauf, ob das VPN verwendet wird.

    Klicken Sie auf das ausgegraute Feld, um die Routing-Methode auszuwählen.

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_1.png){class="glboxshadow"}

    ![via](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/traffic_via_2.png){class="glboxshadow"}

    - **Use VPN**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, über das VPN zu den ausgewählten Zielen geleitet.
        
        Zunächst müssen Sie Ihren Router als VPN-Client konfigurieren. Verwenden Sie den [VPN Setup Wizard](#setup-wizard), um die Konfiguration schnell abzuschließen, oder gehen Sie in der linken Seitenleiste zu OpenVPN Client bzw. WireGuard Client, um die Konfiguration manuell vorzunehmen.

        Sobald der Router als VPN-Client eingerichtet ist, wählen Sie eine VPN-Konfigurationsdatei für diesen Tunnel aus und klicken Sie auf **Apply**.

        ![use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/use_vpn_2.png){class="glboxshadow"}

    - **Not Use VPN**: Wenn ausgewählt, wird Datenverkehr, der dieser Regel entspricht, über das lokale WAN statt über das VPN zu den ausgewählten Zielen geleitet.

        ![not use vpn](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/not_use_vpn.png){class="glboxshadow"}

4. Nachdem Datenverkehrsquelle, Ziel und Routing-Methode ausgewählt wurden, ist die Einrichtung der Primary-Tunnel-Regel abgeschlossen.

Im folgenden Beispiel lautet die Primary-Tunnel-Regel: Alle Clients verwenden das VPN, um auf angegebene Domains zuzugreifen. Ihr Datenverkehr wird über den australischen Server geleitet und verlässt über diesen Tunnel das Internet zu den ausgewählten Domains.

![connected policy mode](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/connected-policy-mode.jpg){class="glboxshadow"}

**Hinweis**: Prüfen Sie aus Sicherheitsgründen vor dem Aktivieren der Tunnel bitte die Einstellungen unter [All Other Traffic](#all-other-traffic) und [Tunnel Options](#tunnel-options).

#### Add Tunnel

Um zusätzliche Tunnel für mehrere VPN-Instanzen zu erstellen, klicken Sie unter dem Primary Tunnel auf **Add Tunnel** und konfigurieren benutzerdefinierte Regeln.

![add tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/add_tunnel.jpg){class="glboxshadow"}

Geben Sie dem Tunnel einen Namen.

![name tunnel](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/name_tunnel.png){class="glboxshadow"}

Im VPN Dashboard erscheint ein weiterer Tunnel.

![two tunnels](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/two_tunnels.png){class="glboxshadow"}

Bei Bedarf können Sie weitere Tunnel hinzufügen. Es können bis zu 5 Tunnel erstellt werden (einschließlich des voreingestellten Primary Tunnel).

Passen Sie die Tunnel-Regeln an, indem Sie Datenverkehrsquelle, Ziele und Routing-Methode festlegen. Lesen Sie dazu den Abschnitt [Primary Tunnel](#primary-tunnel).

**Hinweis**: Prüfen Sie aus Sicherheitsgründen vor dem Aktivieren der Tunnel bitte die Einstellungen unter [All Other Traffic](#all-other-traffic) und [Tunnel Options](#tunnel-options).

#### All Other Traffic

Im Policy Mode wird am unteren Rand des VPN Dashboard ein <u>voraktivierter</u> Tunnel angezeigt.

![all other traffic](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/all_other_traffic.png){class="glboxshadow"}

Dieser Tunnel steuert, ob Datenverkehr, der keiner der oben genannten VPN-Tunnelgruppen entspricht, auf das Internet zugreifen kann. Er ist standardmäßig aktiviert, um normalen Internetzugang für Datenverkehr sicherzustellen, der nicht über ein VPN geleitet wird.

- Wenn aktiviert, kann nicht zugeordneter Datenverkehr weiterhin auf das Internet zugreifen.

    ![all other traffic on](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_on.png){class="glboxshadow"}

- Wenn deaktiviert, darf nur über VPN geleiteter Datenverkehr auf das Internet zugreifen. Jeglicher Nicht-VPN-Datenverkehr sowie Datenverkehr, der von VPN-Verbindungen per Failover übernommen wird, wird blockiert. Diese Option überschreibt nicht den individuellen Kill Switch jedes VPN-Tunnels.

    ![all other traffic off](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.9/all_other_traffic_off.png){class="glboxshadow"}

#### Tunnel Priority

Standardmäßig hat der voreingestellte Primary Tunnel die höchste Priorität, gefolgt von manuell hinzugefügten Tunneln (falls vorhanden) und danach dem Tunnel All Other Traffic, um die lokale Netzwerkverbindung über das lokale WAN sicherzustellen.

Um die Tunnel-Priorität zu ändern, klicken Sie in der oberen Infoleiste auf **Modify Priority** oder auf das **Prioritäts-Label** oben links an einem beliebigen Tunnel (z. B. Priority 1 / Priority 2).

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_1.png){class="glboxshadow"}

Klicken Sie rechts auf das Symbol mit den drei Linien und halten Sie es gedrückt, um die Tunnel neu anzuordnen. Klicken Sie anschließend auf **Apply**.

![modify priority](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/modify_priority_2.png){class="glboxshadow"}

**Wenn mehrere Tunnel aktiviert sind, leitet der Router den Datenverkehr in der folgenden Reihenfolge weiter**:

1. Der Datenverkehr versucht zuerst, mit der Tunnel-Regel der höchsten Priorität übereinzustimmen. Wenn es eine Übereinstimmung gibt, wird er über diesen Tunnel geleitet; andernfalls wird der Tunnel mit der nächstniedrigeren Priorität geprüft usw., bis er mit dem Tunnel „All Other Traffic“ übereinstimmt.

2. Wenn ein VPN-Tunnel unerwartet die Verbindung verliert, entscheidet das System abhängig davon, ob der **Kill Switch** dieses Tunnels aktiviert ist, ob der Datenverkehr per Failover an den Tunnel mit der nächstniedrigeren Priorität weitergegeben wird.

    - Wenn der Kill Switch aktiviert ist, wird der Datenverkehr blockiert und nicht an den nächsten Prioritätstunnel per Failover übergeben.
    - Wenn der Kill Switch deaktiviert ist, wird der Datenverkehr an den nächsten Prioritätstunnel per Failover übergeben und versucht, dessen Tunnel-Regeln zu erfüllen.

3. Der Tunnel **All Other Traffic** ist standardmäßig aktiviert, damit Datenverkehr, der nicht zu den VPN-Tunneln passt, weiterhin auf das Internet zugreifen kann.

    - Wenn aktiviert, leitet er nicht zugeordneten oder per Failover übernommenen Datenverkehr über das lokale WAN.
    - Wenn deaktiviert, verstärkt er die Wirkung des Kill Switch und blockiert den normalen Internetzugang, um IP-Lecks zu verhindern.

#### Tunnel Options

Sie können für jeden VPN-Tunnel erweiterte Einstellungen wie VPN Kill Switch, IP-Maskierung und MTU konfigurieren.

Klicken Sie auf das Zahnradsymbol neben einem Tunnelnamen und wählen Sie **Options**.

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_1.png){class="glboxshadow"}

![tunnel options](https://static.gl-inet.com/docs/router/en/4/interface_guide/vpn_dashboard/4.8/tunnel_options_2.png){class="glboxshadow"}

- **Kill Switch**: Wenn aktiviert, wird Datenverkehr, der diesem VPN-Tunnel entspricht, blockiert, falls die VPN-Verbindung unerwartet ausfällt. Wenn deaktiviert, wird dieser Datenverkehr per Failover an den nächsten Prioritätstunnel oder das lokale WAN weitergegeben.

- **Services from GL.iNet Use VPN**: Wenn aktiviert, übertragen GoodCloud, DDNS und rtty ihre Pakete über VPN-Tunnel. Diese Option ist standardmäßig deaktiviert, da diese Dienste normalerweise die echte IP-Adresse des Geräts benötigen, um ordnungsgemäß zu funktionieren.

- **Allow Remote Access the LAN Subnet**: Wenn aktiviert, ist der Fernzugriff auf diesen Router und seine LAN-Geräte über das VPN erlaubt. Dafür muss der VPN-Server eine Rückroute zu seinem LAN-Subnetz bekanntgeben.

- **IP Masquerading**: Wenn aktiviert, werden die Quell-IP-Adressen von LAN-Clients auf die VPN-Tunnel-IP des Routers umgeschrieben. Deaktivieren Sie dies nur bei Site-to-Site-Setups, in denen der entfernte Peer Ihre LAN-Subnetze kennt.

- **MTU**: Der MTU-Wert, den Sie für den Tunnel festlegen, überschreibt die MTU-Einstellungen in der Konfigurationsdatei.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
