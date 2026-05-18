# FAQ zur Fehlerbehebung bei der Internetverbindung

## Q1. Was soll ich tun, wenn ich nicht auf das Internet zugreifen kann?

Führen Sie die folgenden Schritte zur grundlegenden Fehlerbehebung aus.

1. Prüfen Sie die physische Verbindung.

    Stellen Sie sicher, dass das Ethernet-Kabel fest zwischen dem WAN-Port Ihres Routers und dem vorgeschalteten Gerät (z. B. Modem, ONT oder Ethernet-Buchse) angeschlossen ist. Prüfen Sie die LEDs am vorgeschalteten Gerät und stellen Sie sicher, dass eine aktive Übertragung stattfindet.

2. Starten Sie die Geräte neu.

    Schalten Sie das vorgeschaltete Gerät (z. B. das Modem) und Ihren Router aus. Warten Sie 1 bis 2 Minuten. Schalten Sie dann zuerst das Modem wieder ein, warten Sie, bis es vollständig online ist, und schalten Sie anschließend den Router ein.

3. Prüfen Sie die WAN-IP-Adresse.

    Melden Sie sich im Web-Admin-Panel Ihres Routers an und gehen Sie zu **INTERNET** -> **Ethernet**. Wenn der Status wie unten gezeigt bei „connecting“ hängen bleibt, kann dies an DHCP, MAC-Bindung oder einer erforderlichen VLAN-ID liegen.

    ![connecting](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/connecting.png){class="glboxshadow"}

    Erkundigen Sie sich bei Ihrem ISP, ob Sie für den Internetzugang einen **PPPoE username**, ein **PPPoE password** und eine **VLAN ID** benötigen.

    Prüfen Sie außerdem, ob Ihr ISP zuvor eine **MAC binding** auf Ihrem Modem/ONT eingerichtet hat.

## Q2. Wann sollte ich eine MAC-Adresse klonen?

Einige ISPs binden Ihren Breitbandanschluss an die MAC-Adresse des zuerst verbundenen Geräts, in der Regel Ihres alten Routers oder Computers. Wenn Sie den Router austauschen, müssen Sie die MAC-Adresse klonen, um den Internetzugang wiederherzustellen.

Führen Sie die folgenden Schritte aus, um eine MAC-Adresse auf Ihren GL.iNet-Router zu klonen.

1. Notieren Sie sich die MAC-Adresse Ihres alten Routers (oder des Computers, der zuvor mit Ihrem Breitbandanschluss verknüpft war).

2. Melden Sie sich im Web-Admin-Panel Ihres Routers an und gehen Sie zu **NETWORK** -> **Ethernet Port** (in manchen Firmware-Versionen **Port Management** genannt). Stellen Sie **MAC Mode** auf **Clone** oder **Manual**, geben Sie die MAC-Adresse manuell ein und klicken Sie dann auf **Apply**.

    ![mac clone](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/mac_clone.png){class="glboxshadow"}

3. Starten Sie Ihr Modem (also das vorgeschaltete Gerät) neu.

## Q3. Wann muss ich eine VLAN-ID konfigurieren?

Einige ISPs verlangen VLAN-Tagging für die Internetauthentifizierung oder die Trennung des Datenverkehrs, insbesondere bei Glasfaser- und IPTV-Anschlüssen. Fragen Sie bei Ihrem ISP nach, ob eine VLAN-ID erforderlich ist.

Führen Sie die folgenden Schritte aus, um die VLAN-ID zu konfigurieren.

1. Melden Sie sich an Ihrem Router an und gehen Sie zu **INTERNET** -> **Ethernet**. Klicken Sie auf **Modify**.

2. Geben Sie die von Ihrem ISP bereitgestellte VLAN-ID ein und klicken Sie dann auf **Apply**.

    ![vlan id](https://static.gl-inet.com/docs/router/en/4/faq/internet_connection_troubleshooting_faq/vlan_id.png){class="glboxshadow"}

## Q4. Was ist, wenn es weiterhin nicht funktioniert?

Wenn das Problem weiterhin besteht, verbinden Sie versuchsweise einen PC oder Laptop direkt mit Ihrem Modem und prüfen Sie, ob Sie Internetzugang haben.

Wenn Sie keinen Internetzugang haben, liegt das Problem möglicherweise bei Ihrem ISP. Wenden Sie sich für weitere Unterstützung an Ihren ISP.

Wenn Sie Internetzugang haben, hängt das Problem möglicherweise mit der Konfiguration Ihres Routers zusammen. Kontaktieren Sie unseren technischen Support unter [support@gl-inet.com](mailto:support@gl-inet.com) und senden Sie die folgenden Informationen mit:

- Routermodell
- Bereits durchgeführte Schritte zur Fehlerbehebung
- Name Ihres ISP
- Alle weiteren Informationen, die uns bei der Unterstützung helfen könnten

## ISP information

Nachfolgend finden Sie regionsspezifische ISP-Informationen, die GL.iNet aus Kundenfeedback, Foren und OpenWRT-Ressourcen zusammengestellt hat. Diese dienen nur als Referenz.

| Country/Region   | ISP   | Connection Type | VLAN ID | MAC Clone Required | Additional Requirements |
| :--------------- | :---- | :-------------- | :------ | :-------- | :---------------------- |
| United States    | AT&T Fiber | DHCP (IP Passthrough) | N/A | No | Must enable IP Passthrough; EAP authentication bypass needed |
| United States | Spectrum | DHCP | N/A | Yes (in some areas) | Strong MAC binding (modem reboot required) |
| United States | Verizon Fios | DHCP | N/A | No | |
| United States | Comcast Xfinity | DHCP | N/A | Yes (common) | Must reboot modem when changing router (MAC release) |
| United States | Cox Communications | DHCP | N/A | Yes | Must reboot modem when changing router (MAC release) |
| United States | Frontier Fiber | DHCP | N/A | No | |
| United States | CenturyLink / Lumen | PPPoE | 201 | No | VLANs are required in certain areas. |
| Canada | Bell Canada Fibe | PPPoE | 35 | No | |
| Germany | Deutsche Telekom | PPPoE | 7 | No | VLAN 7 mandatory for internet; PPPoE credentials required |
| Germany | Vodafone (Kabel) | DHCP | N/A | Yes (sometimes) | MAC binding may apply; reboot modem after router change |
| Germany | 1&1 / O2 (Telekom line) | PPPoE | 7 | No | VLAN 7 mandatory for internet |
| Germany | DNS:NET | PPPoE | 37 | No | |
| Germany | o2(UGG) | PPPoE | 7 | No | |
| United Kingdom | BT Broadband | PPPoE | 101 | No | VLAN 101 required; PPPoE login needed |
| United Kingdom | Sky Broadband | DHCP (Option 61) | 101 | No | Requires DHCP Option 61 (client identifier) |
| United Kingdom | Virgin | DHCP | N/A | Yes | The modem is in bridged mode and requires MAC cloning. |
| France | Orange | DHCP / PPPoE | 832 | No | VLAN 832 required; may require Option 90 authentication |
| France | Free (Freebox) | DHCP | N/A | No | |
| France | Bouygues Telecom | DHCP | 100 | Yes | Clone Bbox MAC |
| Spain | Movistar | PPPoE | 6 | No | VLAN 6 (internet), VLAN 2 (IPTV), VLAN 3 (VoIP) |
| Spain | DIGI | PPPoE | 20 | No | |
| Spain | Orange | DHCP | 832/835 | No | VLANs may vary by region |
| Italy | TIM | PPPoE | 835 | No | VLAN 835 required |
| Italy | Aruba | PPPoE | 835 | No | |
| Netherlands | KPN | DHCP | 6 | No | VLAN 6 required for internet |
| Netherlands | Tweak | DHCP | 34 | Yes | Cloning Experia Box MAC |
| Netherlands | Telfort / Oxxio / Tweak | DHCP (IPoE) | 34 | No | |
| Netherlands | Odido | DHCP | 300 | No | |
| Belgium | EDPnet | PPPoE | 10 | No | |
| Bosnia and Herzegovina | BH Telecom | PPPoE | 100 | No | |
| Croatia | Terrakom | PPPoE | 905 | No | |
| Czech Republic | O2 | PPPoE | 848 | No | |
| Cyprus | Epic | PPPoE | 35 | No | |
| Cyprus | Cyta | PPPoE | 42 | No | |
| Cyprus | Cablenet | PPPoE | 42 | No | |
| Cyprus | Primetel | PPPoE | 42 | No | |
| Poland | Orange Polska | PPPoE | 35 | No | VLAN 35 required |
| Poland | T-mobile | PPPoE | 35 | No | |
| Ireland | Vodafone SIRO | PPPoE | 10 | No | |
| Ireland | Pure Telecom | PPPoE | 10 | No | |
| Austria | A1 Telekom | PPPoE | 2 | No | |
| Austria | Fonira | PPPoE | 31 | No | |
| Türkiye | Turknet | PPPoE | 35 | No | |
| Türkiye | Turk Telekom | PPPoE | 35 | No | |
| Türkiye | Turkcell Superonline | PPPoE | N/A | Yes | |
| Türkiye | Turksat Kablonet | DHCP/PPPoE | N/A | No | |
| Greece | Cosmote | PPPoE | 835 | No | |
| Greece | Nova | PPPoE | 835 | Yes | |
| Greece | DEI/PPC | DHCP | 835 | No | |
| Japan | NTT (FLET'S) | PPPoE / IPoE (MAP-E) | N/A | No | IPoE requires MAP-E/DS-Lite compatible router |
| Japan | SoftBank Hikari | PPPoE / IPoE | N/A | No | BBIX IPoE service commonly used |
| India | Airtel | PPPoE / DHCP | N/A | No | Some regions require PPPoE |
| India | JioFiber | DHCP | N/A | No | Locked ONT in many cases |
| Singapore | Singtel | PPPoE | 10 | No | VLAN 10 required; IPTV separate VLAN |
| Singapore | StarHub | DHCP | N/A | No | DHCP-based connection |
| Australia | NBN (various ISPs) | PPPoE / DHCP | 2 (common) | Yes | VLAN 2 common but ISP-dependent |
