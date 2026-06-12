# Kindersicherung (Firmware v4.9)

> Diese Anleitung gilt für Firmware v4.9 und höher. Für frühere Versionen klicken Sie bitte [hier](parental_control.md).

Gehen Sie auf der linken Seite des Web-Admin-Panels zu **FLOW CONTROL** -> **Parental Control**.

Die Kindersicherung schützt Kinder online, indem ungeeignete Websites blockiert und Bildschirmzeiten begrenzt werden. Sie filtert schädliche Inhalte und fördert eine verantwortungsvolle Internetnutzung.

GL.iNet Parental Control bietet flexible Zeitpläne, um den Internetzugang auf häufig genutzten Geräten Ihrer Kinder einzuschränken. Ungeeignete Apps und Websites lassen sich mit einem Klick blockieren. Zusätzlich können Sie bei Bedarf Domains manuell eingeben, um einen umfassenden Online-Schutz zu erreichen.

Das Seitenlayout und der Ablauf von Parental Control wurden in Firmware v4.9 verbessert, was die Einrichtung vereinfacht und eine intuitivere Übersicht über die Regeln bietet.

---

Folgen Sie den nachstehenden Schritten, um Ihre Kindersicherung einzurichten.

1. Melden Sie sich im Web-Admin-Panel des Routers an und gehen Sie zu **FLOW CONTROL** -> **Parental Control**. Stellen Sie sicher, dass die Routerzeit korrekt ist.

    ![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/router_time.png){class="glboxshadow"}

    Falls nicht, gehen Sie zuerst zu **SYSTEM** -> **Time Zone**, um die Zeit zu synchronisieren.

2. Aktivieren Sie Parental Control und klicken Sie auf **Apply**.

    ![enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/enable.png){class="glboxshadow"}

3. Daraufhin wird eine Regelliste wie unten gezeigt angezeigt. Klicken Sie auf **Add a New Rule**.

    ![add a new rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/add_rules.png){class="glboxshadow"}

4. Erstellen Sie im Pop-up-Fenster eine Regel, vergeben Sie einen benutzerdefinierten Namen und klicken Sie dann auf **Next**.

    ![create a rule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/create_rule.png){class="glboxshadow gl-90-desktop"}

5. Wählen Sie das Gerät Ihres Kindes aus und klicken Sie dann auf **Next**.

    Ein Gerät erscheint auf dieser Seite nur, wenn es per Wi-Fi oder Ethernet mit dem Router verbunden ist. Cyan zeigt an, dass das Gerät online ist, Grau bedeutet offline.

    ![select device](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/select_device.png){class="glboxshadow gl-90-desktop"}

    **Tipp**: Wenn Sie verbundene Geräte besser unterscheiden möchten, gehen Sie zur Seite **CLIENTS** und passen Sie die Gerätenamen an.

6. Legen Sie eine Schlafenszeit für das Gerät Ihres Kindes fest und klicken Sie dann auf **Next**.

    Während dieses Zeitraums ist das Internet auf den ausgewählten Geräten nicht verfügbar. Standardmäßig gilt dieselbe Schlafenszeit für jeden Tag.

    ![bedtime1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime1.png){class="glboxshadow gl-90-desktop"}

    Wenn Sie für jeden Wochentag unterschiedliche Schlafenszeiten festlegen möchten, wählen Sie **Customize Days**, legen die Zeiten fest und klicken dann auf **Next**.

    ![bedtime2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/bedtime2.png){class="glboxshadow gl-90-desktop"}

7. Wählen Sie den Inhaltsfilter aus.

    Standardmäßig sind drei Kategorien ausgewählt: **Gambling**, **Malicious Content** und **Sexual Content**.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Bei Bedarf können Sie weitere Kategorien auswählen, zum Beispiel **Games**, **Shopping**, **Social Media**, **Entertainment** usw.

    ![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/filter.png){class="glboxshadow gl-90-desktop"}

    Wenn Sie eine bestimmte App blockieren möchten und sie schwer zu finden ist, verwenden Sie die Suche oben, um sie schnell zu finden.

    ![search app](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/search_app.png){class="glboxshadow gl-90-desktop"}

8. Wenn Sie bestimmte Domains blockieren müssen, klicken Sie unten rechts auf **Advanced Settings**.

    ![block domain1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain1.png){class="glboxshadow gl-90-desktop"}

    Geben Sie die Domains manuell ein und klicken Sie dann auf **Finish**.

    ![block domain2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/block_domain2.png){class="glboxshadow gl-90-desktop"}

9. Die Regel ist nun hinzugefügt. Die Liste zeigt den Regelnamen, die Anzahl verbundener Geräte, den Schlafenszeitplan, die gefilterten Inhalte und den Regelstatus (aktiviert/deaktiviert).

    ![rules added](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/rules_added.png){class="glboxshadow"}

    Für vorhandene Regeln stehen grundlegende Aktionen zur Verfügung: Modify, Copy und Delete.

    ![action](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action.png){class="glboxshadow"}

    - **Modify**: Ändert die ausgewählten Geräte, Schlafenszeiten und Inhaltsfilterregeln.

        ![action modify](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_modify.png){class="glboxshadow"}

    - **Copy**: Erstellt eine Kopie einer vorhandenen Regel, damit Sie sie nicht manuell neu konfigurieren müssen.

        ![action copy](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control_v4.9/action_copy.png){class="glboxshadow"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
