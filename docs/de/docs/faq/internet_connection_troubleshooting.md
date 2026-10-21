# FAQ zur Fehlerbehebung bei der Internetverbindung {#internet-connection-troubleshooting-faq}

## Q1. Was soll ich tun, wenn ich nicht auf das Internet zugreifen kann? {#q1-what-should-i-do-if-i-cannot-access-the-internet}

Führen Sie die folgenden Schritte zur grundlegenden Fehlerbehebung aus.

1. Prüfen Sie die physische Verbindung.

    Stellen Sie sicher, dass das Ethernet-Kabel fest zwischen dem WAN-Port Ihres Routers und dem vorgeschalteten Gerät (z. B. Modem, ONT oder Ethernet-Buchse) angeschlossen ist. Prüfen Sie die LEDs am vorgeschalteten Gerät und stellen Sie sicher, dass eine aktive Übertragung stattfindet.

2. Starten Sie die Geräte neu.

    Schalten Sie das vorgeschaltete Gerät (z. B. das Modem) und Ihren Router aus. Warten Sie 1 bis 2 Minuten. Schalten Sie dann zuerst das Modem wieder ein, warten Sie, bis es vollständig online ist, und schalten Sie anschließend den Router ein.

3. Prüfen Sie die WAN-IP-Adresse.

    Melden Sie sich im Web-Admin-Panel Ihres Routers an und gehen Sie zu **INTERNET** -> **Ethernet**. Wenn der Status wie unten gezeigt bei „connecting“ hängen bleibt, kann dies an einem DHCP-Problem, einer MAC-Bindung oder einer erforderlichen VLAN-ID liegen.

    ![connecting](https://static.gl-inet.com/docs/router/de/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Erkundigen Sie sich bei Ihrem ISP, ob Sie für den Internetzugang einen **PPPoE username**, ein **PPPoE password** und eine **VLAN ID** benötigen.

    Prüfen Sie außerdem, ob Ihr ISP zuvor eine **MAC binding** auf Ihrem Modem/ONT eingerichtet hat.

## Q2. Wann sollte ich eine MAC-Adresse klonen? {#q2-when-should-i-clone-a-mac-address}

Einige ISPs binden Ihren Breitbandanschluss an die MAC-Adresse des zuerst verbundenen Geräts, in der Regel Ihres alten Routers oder Computers. Wenn Sie den Router austauschen, müssen Sie die MAC-Adresse klonen, um den Internetzugang wiederherzustellen.

Führen Sie die folgenden Schritte aus, um eine MAC-Adresse auf Ihren GL.iNet-Router zu klonen.

1. Notieren Sie sich die MAC-Adresse Ihres alten Routers (oder des Computers, der zuvor mit Ihrem Breitbandanschluss verknüpft war).

2. Melden Sie sich im Web-Admin-Panel Ihres Routers an und gehen Sie zu **NETWORK** -> **Ethernet Port** (in manchen Firmware-Versionen **Port Management** genannt). Stellen Sie **MAC Mode** auf **Clone** oder **Manual**, geben Sie die MAC-Adresse manuell ein und klicken Sie dann auf **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/de/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Starten Sie Ihr Modem (also das vorgeschaltete Gerät) neu.

## Q3. Wann muss ich eine VLAN-ID konfigurieren? {#q3-when-do-i-need-to-configure-a-vlan-id}

Einige ISPs verlangen VLAN-Tagging für die Internetauthentifizierung oder die Trennung des Datenverkehrs, insbesondere bei Glasfaser- und IPTV-Anschlüssen. Fragen Sie bei Ihrem ISP nach, ob eine VLAN-ID erforderlich ist.

Führen Sie die folgenden Schritte aus, um die VLAN-ID zu konfigurieren.

1. Melden Sie sich an Ihrem Router an und gehen Sie zu **INTERNET** -> **Ethernet**. Klicken Sie auf **Modify**.

2. Geben Sie die von Ihrem ISP bereitgestellte VLAN-ID ein und klicken Sie dann auf **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/de/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. Was ist, wenn es weiterhin nicht funktioniert? {#q4-what-if-it-still-doesnt-work}

Wenn das Problem weiterhin besteht, verbinden Sie versuchsweise einen PC oder Laptop direkt mit Ihrem Modem und prüfen Sie, ob Sie Internetzugang haben.

Wenn Sie keinen Internetzugang haben, liegt das Problem möglicherweise bei Ihrem ISP. Wenden Sie sich für weitere Unterstützung an Ihren ISP.

Wenn Sie Internetzugang haben, hängt das Problem möglicherweise mit der Konfiguration Ihres Routers zusammen. Kontaktieren Sie unseren technischen Support unter [support@gl-inet.com](mailto:support@gl-inet.com) und senden Sie die folgenden Informationen mit:

- Routermodell
- Bereits durchgeführte Schritte zur Fehlerbehebung
- Name Ihres ISP
- Alle weiteren Informationen, die uns bei der Unterstützung helfen könnten

## ISP-Informationen {#isp-information}

Nachfolgend finden Sie regionsspezifische ISP-Informationen, die GL.iNet aus Kundenfeedback, Foren und OpenWRT-Ressourcen zusammengestellt hat. Diese dienen nur als Referenz.

| Land/Region   | ISP   | Verbindungstyp | VLAN-ID | MAC-Klonen erforderlich | Zusätzliche Anforderungen |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| Vereinigte Staaten | AT&T Fiber | DHCP (IP Passthrough) | N/A | Nein | IP Passthrough muss aktiviert werden; EAP-Authentifizierung muss umgangen werden |
| Vereinigte Staaten | Spectrum | DHCP | N/A | Ja (in einigen Regionen) | Strenge MAC-Bindung (Neustart des Modems erforderlich) |
| Vereinigte Staaten | Verizon Fios | DHCP | N/A | Nein | |
| Vereinigte Staaten | Comcast Xfinity | DHCP | N/A | Ja (häufig) | Modem muss beim Routerwechsel neu gestartet werden (MAC-Freigabe) |
| Vereinigte Staaten | Cox Communications | DHCP | N/A | Ja | Modem muss beim Routerwechsel neu gestartet werden (MAC-Freigabe) |
| Vereinigte Staaten | Frontier Fiber | DHCP | N/A | Nein | |
| Vereinigte Staaten | CenturyLink / Lumen | PPPoE | 201 | Nein | In bestimmten Regionen sind VLANs erforderlich. |
| Kanada | Bell Canada Fibe | PPPoE | 35 | Nein | |
| Deutschland | Deutsche Telekom | PPPoE | 7 | Nein | VLAN 7 für den Internetzugang zwingend erforderlich; PPPoE-Zugangsdaten erforderlich |
| Deutschland | Vodafone (Kabel) | DHCP | N/A | Ja (manchmal) | MAC-Bindung möglich; Modem nach einem Routerwechsel neu starten |
| Deutschland | 1&1 / O2 (Telekom line) | PPPoE | 7 | Nein | VLAN 7 für den Internetzugang zwingend erforderlich |
| Deutschland | DNS:NET | PPPoE | 37 | Nein | |
| Deutschland | o2(UGG) | PPPoE | 7 | Nein | |
| Vereinigtes Königreich | BT Broadband | PPPoE | 101 | Nein | VLAN 101 erforderlich; PPPoE-Anmeldung erforderlich |
| Vereinigtes Königreich | Sky Broadband | DHCP (Option 61) | 101 | Nein | Erfordert DHCP Option 61 (Client-Kennung) |
| Vereinigtes Königreich | Virgin | DHCP | N/A | Ja | Das Modem befindet sich im Bridge-Modus und erfordert MAC-Klonen. |
| Frankreich | Orange | DHCP / PPPoE | 832 | Nein | VLAN 832 erforderlich; ggf. Authentifizierung über Option 90 erforderlich |
| Frankreich | Free (Freebox) | DHCP | N/A | Nein | |
| Frankreich | Bouygues Telecom | DHCP | 100 | Ja | MAC-Adresse der Bbox klonen |
| Spanien | Movistar | PPPoE | 6 | Nein | VLAN 6 (Internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spanien | DIGI | PPPoE | 20 | Nein | |
| Spanien | Orange | DHCP | 832/835 | Nein | VLANs können je nach Region variieren |
| Italien | TIM | PPPoE | 835 | Nein | VLAN 835 erforderlich |
| Italien | Aruba | PPPoE | 835 | Nein | |
| Niederlande | KPN | DHCP | 6 | Nein | VLAN 6 für den Internetzugang erforderlich |
| Niederlande | Tweak | DHCP | 34 | Ja | MAC-Adresse der Experia Box klonen |
| Niederlande | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | Nein | |
| Niederlande | Odido | DHCP | 300 | Nein | |
| Belgien | EDPnet | PPPoE | 10 | Nein | |
| Bosnien und Herzegowina | BH Telecom | PPPoE | 100 | Nein | |
| Kroatien | Terrakom | PPPoE | 905 | Nein | |
| Tschechien | O2 | PPPoE | 848 | Nein | |
| Zypern | Epic | PPPoE | 35 | Nein | |
| Zypern | Cyta | PPPoE | 42 | Nein | |
| Zypern | Cablenet | PPPoE | 42 | Nein | |
| Zypern | Primetel | PPPoE | 42 | Nein | |
| Polen | Orange Polska | PPPoE | 35 | Nein | VLAN 35 erforderlich |
| Polen | T-mobile | PPPoE | 35 | Nein | |
| Irland | Vodafone SIRO | PPPoE | 10 | Nein | |
| Irland | Pure Telecom | PPPoE | 10 | Nein | |
| Österreich | A1 Telekom | PPPoE | 2 | Nein | |
| Österreich | Fonira | PPPoE | 31 | Nein | |
| Türkei | Turknet | PPPoE | 35 | Nein | |
| Türkei | Turk Telekom | PPPoE | 35 | Nein | |
| Türkei | Turkcell Superonline | PPPoE | N/A | Ja | |
| Türkei | Turksat Kablonet | DHCP/PPPoE | N/A | Nein | |
| Griechenland | Cosmote | PPPoE | 835 | Nein | |
| Griechenland | Nova | PPPoE | 835 | Ja | |
| Griechenland | DEI/PPC | DHCP | 835 | Nein | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | Nein | IPoE erfordert einen Router mit MAP-E/DS-Lite-Unterstützung |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | Nein | Häufig wird der IPoE-Dienst von BBIX verwendet |
| Indien | Airtel | PPPoE / DHCP | N/A | Nein | In einigen Regionen ist PPPoE erforderlich |
| Indien | JioFiber | DHCP | N/A | Nein | ONT in vielen Fällen gesperrt |
| Singapur | Singtel | PPPoE | 10 | Nein | VLAN 10 erforderlich; IPTV über separates VLAN |
| Singapur | StarHub | DHCP | N/A | Nein | DHCP-basierte Verbindung |
| Australien | NBN (verschiedene ISPs) | PPPoE / DHCP | 2 (häufig) | Ja | VLAN 2 üblich, aber ISP-abhängig |
