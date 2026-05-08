# Inhaltsfilter

Der Inhaltsfilter ist eine intelligente Online-Sicherheitsfunktion auf Basis der DPI-Klassifizierung. Er blockiert automatisch schädliche und bösartige Websites, hält Ihr Netzwerk sauber und sicher und unterstützt außerdem benutzerdefinierte Regeln zum Blockieren bestimmter Apps, Domains oder IP-Adressen.

**Hinweis**:

1. Der Inhaltsfilter wirkt nicht, wenn sich der Router im Drop-in Gateway-Modus befindet.
2. Der Inhaltsfilter kann nicht zusammen mit der Netzwerkbeschleunigung verwendet werden. Beim Aktivieren des Inhaltsfilters wird die Netzwerkbeschleunigung automatisch deaktiviert, um eine stabile Leistung sicherzustellen.

## Unterstützte Modelle

!!! note "Unterstützte Modelle"

    - GL-BE10000 (Slate 7 Pro)
    - GL-MT5000 (Brume 3)
    - ※GL-BE9300 (Flint 3)
    - ※GL-BE3600 (Slate 7)
    - ※GL-MT6000 (Flint 2)
    - ※GL-MT3000 (Beryl AX)

    Hinweis: Mit ※ gekennzeichnete Modelle unterstützen den Inhaltsfilter ab Firmware v4.9.

## Schnelleinrichtung

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **Content Filter**.

Schalten Sie den Schalter oben rechts ein, passen Sie die blockierten Inhalte an (z. B. Apps, Domains oder IP-Adressen) und klicken Sie dann auf **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Diese Seite besteht aus zwei Bereichen:

- **Blocked Apps List**: Dieser Abschnitt enthält drei vorab ausgewählte Kategorien: Gambling, Adult und Malware. Wenn sie aktiviert sind, werden alle Websites, Dienste oder Apps blockiert, die zu diesen drei Kategorien gehören.

    Sie können auch auf **Edit App** klicken, um bei Bedarf weitere Kategorien hinzuzufügen, z. B. Game oder Social Media.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    Wählen Sie im Pop-up-Fenster die Kategorien aus, die Sie blockieren möchten. Die drei Standardkategorien sind leer; alle anderen Kategorien enthalten eine App-Liste.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Klicken Sie auf eine beliebige Kategorie, um die Apps anzuzeigen und auszuwählen, die Sie blockieren möchten. Alternativ können Sie oben rechts auf **Select All** klicken, um alle Apps dieser Kategorie gleichzeitig zu blockieren. Klicken Sie anschließend auf **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    Danach sehen Sie die ausgewählten Apps in der Blocked Apps List.

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: In diesem Abschnitt können Sie bestimmte Domains (z. B. google.com), CIDR-Bereiche (z. B. 192.168.8.0/24) oder IP-Adressen (z. B. 192.168.10.10) manuell eingeben, um den Zugriff darauf zu blockieren. Die Liste unterstützt bis zu 10000 Einträge.

    Geben Sie die Domains oder IP-Adressen ein, die Sie blockieren möchten, und klicken Sie dann auf **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Inhaltsfilter testen

In diesem Beispiel haben wir die Kategorie **Game** ausgewählt, die Nintendo enthält.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

Auf einem Laptop, der mit Ihrem Router verbunden ist, kann die Website `nintendo.com` nicht mehr aufgerufen werden, obwohl sie vor der Aktivierung des Inhaltsfilters erreichbar war.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

Im Web-Admin-Panel des Routers können Sie sehen, wie viele Zugriffsanfragen blockiert wurden.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
