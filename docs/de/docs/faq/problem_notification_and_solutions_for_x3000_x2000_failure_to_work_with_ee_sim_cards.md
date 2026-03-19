# Problemmitteilung und Lösungen für GL-X3000/GL-XE3000/GL-X2000 bei Problemen mit EE-SIM-Karten

Liebe GL.iNet-Kunden,

Vor Kurzem haben wir festgestellt, dass bei einigen Kunden mit GL-X3000/GL-XE3000/GL-X2000 Verbindungsprobleme auftreten, wenn EE-SIM-Karten verwendet werden. Nach weiterer Fehleranalyse haben wir herausgefunden, dass bestimmte EE-SIM-Karten nur das IPv4-Protokoll unterstützen. In den Standardeinstellungen der Mobilfunkrouter von GL.iNet sind jedoch gleichzeitig IPv4 und IPv6 aktiviert, wodurch dieses Problem entsteht.

## Lösungen und Workarounds

1. **Firmware-Aktualisierung**

    Wir haben neue Firmware-Versionen veröffentlicht, bei denen das Standardprotokoll zur Behebung dieses Problems auf IPv4 geändert wurde. Kunden, die IPv6 benötigen, können die Einstellung im Admin Panel weiterhin auf IPv4 & IPv6 ändern.

    | Routermodell                  |                       |
    | :---------------------------- | :-------------------: |
    | GL-X3000 (Spitz AX)           | [Firmware herunterladen](https://dl.gl-inet.com/router/x3000/stable)     |
    | GL-XE3000 (Puli AX)           | [Firmware herunterladen](https://dl.gl-inet.com/router/xe3000/stable)    |
    | GL-X2000 (Spitz Plus)         | [Firmware herunterladen](https://dl.gl-inet.com/router/x2000/stable)   |

2. **Workaround für andere Modelle**

    Wenn Sie andere Modelle verwenden oder die oben genannte Firmware nicht nutzen möchten, führen Sie bitte nach dem Start der Mobilfunkverbindung nacheinander die AT-Befehle aus.

    ```
    AT+CGDCONT=1,"IP","User_APN"
    AT+CFUN=0
    AT+CFUN=1
    ```

    **Hinweis**: "User_APN" ist bei EE-SIM-Karten in der Regel "everywhere". Wiederholen Sie diesen Vorgang nach jedem Neustart des Routers.

    ??? note "Wie führe ich einen AT-Befehl aus?"

        1. Navigieren Sie im Web-Admin-Panel zum Abschnitt INTERNET -> Cellular, klicken Sie oben rechts auf das Drei-Punkte-Symbol und wählen Sie **Modem AT Command**.
        
            ![modem AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_0.jpg){class="glboxshadow"}
        
            Bei älterer Firmware klicken Sie oben rechts auf die Werkzeugschaltfläche, um die Modemverwaltungsseite zu öffnen.

            ![modem management](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/modem_management_button.png){class="glboxshadow"}
        
        2. Suchen Sie den Bereich für AT-Befehle wie unten dargestellt.

            ![AT command](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_cellular/4.8/at_command_1.png){class="glboxshadow"}

Wenn Sie weitere Probleme haben, kontaktieren Sie bitte unser Support-Team unter [support@gl-inet.com](mailto:support@gl-inet.com).

<br>

Mit freundlichen Grüßen

GL.iNet Technischer Support

17. Juni 2025

