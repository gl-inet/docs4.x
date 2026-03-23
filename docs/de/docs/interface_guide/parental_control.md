# Parental Control

Parental Control hilft dabei, Kinder online zu schützen, indem ungeeignete Websites blockiert und die Nutzungsdauer von Geräten begrenzt wird. So lässt sich der Zugriff auf schädliche Inhalte verhindern, die Bildschirmzeit steuern und eine verantwortungsvolle Internetnutzung fördern.

Diese Funktion ist seit Firmware v4.2 verfügbar.

Sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten, um mehr über Parental Control auf GL.iNet-Routern zu erfahren.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Lokale Version

Die lokale Version wird von GL.iNet bereitgestellt. Sie befindet sich derzeit in der Beta-Phase und verursacht keine zusätzlichen Kosten. Wenn Sie in dieser Version Anfragen nach Anwendungen filtern möchten, müssen Sie die Domain manuell eingeben.

### Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Nicht unterstützte Modelle"
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und gehen Sie zu **APPLICATIONS** -> **Parental Control**.

Bei Firmware v4.8.4 und neuer navigieren Sie zu **Flow Control** -> **Parental Control**.

Stellen Sie sicher, dass die Routerzeit korrekt ist. Falls nicht, gehen Sie zunächst zu **SYSTEM** -> **Time Zone**, um sie zu synchronisieren.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Aktivieren Sie Parental Control und klicken Sie auf **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Diese Option wird verwendet, um nicht verwalteten Geräten den Internetzugang zu sperren.

Folgen Sie anschließend dem Einrichtungsassistenten, um Parental Control einzurichten.

Hier sind zwei Anwendungsfälle als Referenz, die Sie an Ihre eigene Situation anpassen können.

**Fall 1**

**Szenario**: Geräte in diesem Profil dürfen werktags nur von 8:00 bis 11:00 Uhr für Lernzwecke und am Wochenende von 18:00 bis 20:00 Uhr für Spiele auf das Internet zugreifen. Zu allen anderen Zeiten ist der Internetzugang standardmäßig blockiert.

Gehen Sie wie folgt vor.

1. Erstellen Sie ein Profil und vergeben Sie einen Namen.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_1.png){class="glboxshadow"}

2. Wählen Sie die Geräte aus, die Sie verwalten möchten. Wenn sie noch nicht mit dem Router verbunden wurden, fügen Sie sie manuell über ihre MAC-Adressen hinzu.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_2.png){class="glboxshadow"}

3. Legen Sie die Zugriffsbegrenzung fest.

    Es gibt zwei Standard-Regelsätze: **Block Internet Access** und **No Limit**. Erstellen Sie hier zwei weitere Regelsätze für die spätere Verwendung: **Learning** und **Play**.

    Klicken Sie auf **Add a New Ruleset**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_3.png){class="glboxshadow"}

4. Legen Sie den Namen des Regelsatzes fest (z. B. Learning), wählen Sie eine Farbe und tragen Sie die Liste der zu blockierenden Websites ein. Klicken Sie dann auf **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_4.png){class="glboxshadow"}

    **Hinweis**: Die in die Blockliste eingetragenen Domainnamen sollten ihre Subdomains mit einschließen. Wenn Sie zum Beispiel `example.com` eintragen, werden auch Subdomains wie `subdomain.example.com` erfasst.

    Erstellen Sie auf dieselbe Weise einen weiteren Regelsatz mit dem Namen Play. Legen Sie eine Farbe und die zu blockierenden Websites fest und klicken Sie auf **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_ruleset_5.png){class="glboxshadow"}

5. Nach dem Anwenden gibt es insgesamt vier Regelsätze, wie unten dargestellt.

    Stellen Sie sicher, dass **Block Internet Access** als **Default Ruleset** ausgewählt ist, und klicken Sie auf **Finish**.

    ![create a profile guide](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_create_profile_6.png){class="glboxshadow"}

6. Gehen Sie anschließend zu Set Schedule. Klicken Sie auf **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_7.png){class="glboxshadow"}

7. Fügen Sie den Regelsatz **Learning** dem Zeitplan hinzu. Setzen Sie **Execution Time** werktags auf 8:00 bis 11:00 Uhr. Klicken Sie auf **Apply**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_schedule_8.png){class="glboxshadow"}

8. Sie werden zur Bearbeitungsseite des neu erstellten Profils weitergeleitet.

    ![modify profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/modify_profile.png){class="glboxshadow"}

    Sie sehen nun, dass ein Zeitplan erstellt wurde. Klicken Sie oben rechts auf **Add Schedule**.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/add_schedule.png){class="glboxshadow"}

9. Fügen Sie dem Zeitplan einen weiteren Regelsatz **Play** hinzu. Setzen Sie **Execution Time** am Wochenende auf 18:00 bis 20:00 Uhr. Klicken Sie auf **Apply**.

    ![add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/create_schedule_2.png){class="glboxshadow"}

10. Danach sehen Sie, dass auch der Regelsatz Play in den Zeitplan aufgenommen wurde.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedules_2.png){class="glboxshadow"}

    **Hinweis**: Die rote gestrichelte Linie zeigt die aktuelle Uhrzeit an.

    Sie können den Zeitplan-Regelsatz auch ändern, indem Sie auf einen bestimmten Bereich im Zeitplan klicken.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/schedule_edit.jpg){class="glboxshadow"}

11. Klicken Sie oben auf **Parental Control**, um zur Seite Parental Control zurückzukehren.

    ![back to parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/back_to_parental_control_page.png){class="glboxshadow"}

    Dort sehen Sie die endgültige Konfiguration. Sie können bestehende Profile und Regelsätze ändern oder neue hinzufügen.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/final_configuration.png){class="glboxshadow"}

**Fall 2**

**Szenario**: Geräte in diesem Profil dürfen am Wochenende abends nur von 18:00 bis 20:00 Uhr für Spiele und kurze Videos auf das Internet zugreifen. Zu allen anderen Zeiten, einschließlich der Schlafenszeit von 21:00 bis 7:00 Uhr am nächsten Morgen, ist der Internetzugang standardmäßig blockiert.

Sehen Sie sich das folgende Video-Tutorial an.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5-EOWZ3WkeE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Fehlerbehebung

Wenn Ihre konfigurierten Einstellungen nicht wirksam werden, prüfen Sie bitte die folgenden möglichen Ursachen.

1. DNS-Cache.
  
    Browser und Betriebssysteme verwenden DNS-Caches, daher können Änderungen etwas Zeit benötigen, bis sie wirksam werden. Sie können den Cache leeren, damit Änderungen sofort greifen.
  
      * [Clear the cache in desktop Chrome](https://support.google.com/accounts/answer/32050){target="_blank"}
      
      * [Clear the cache in desktop Edge](https://www.microsoft.com/en-us/edge/learning-center/how-to-manage-and-clear-your-cache-and-cookies?form=MA13I2){target="_blank"}

2. Der Profil-Zeitplan wurde noch nicht gestartet.

3. Der von Ihnen eingegebene Domainname ist möglicherweise falsch.

    Die Domain einer Website ist öffentlich, die von einer App verwendete API-Domain jedoch oft nicht. Um das zu lösen, verwenden Sie ein Werkzeug wie Wireshark, um Pakete mitzuschneiden, oder recherchieren Sie nach der betreffenden Domain.

    Um zum Beispiel `www.google.com` zu blockieren, ist `google.com` in der Regel wirksamer als `www.google.com`.

4. Das Zielgerät verwendet für jede Verbindung eine zufällige MAC-Adresse, wodurch die Regeln nicht wirksam werden.

## Bark-Version

Die [Bark](https://www.bark.us/){target="_blank"}-Version, die von Bark auf ihrer eigenen Plattform bereitgestellt und verwaltet wird, bietet die Möglichkeit, Anwendungen und Websites mit einem Klick zu filtern und die Historie der Anfragen zu überwachen.

Sie bietet Überwachungsfunktionen für mehr als 24 beliebte Apps und Social-Media-Plattformen, die in der voreingestellten Liste unserer lokalen Parental-Control-Funktion enthalten sind.

Mit der Protokollfunktion wird aufgezeichnet, welcher Client wann auf welche Website zugegriffen hat. So können Eltern die Protokolle einfach prüfen, nicht blockierte Websites erkennen und sie schnell in den Verwaltungsbereich aufnehmen.

Die Bark-Parental-Control-Funktion ist seit Firmware v4.5 verfügbar und wird nur von ausgewählten GL.iNet-Routern unterstützt.

**Hinweis**:

1. Der Bark-Dienst ist **nur in den Vereinigten Staaten, Australien und Südafrika** verfügbar. Details finden Sie [hier](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"}.

2. Der Bark-Dienst erfordert in der Regel ein kostenpflichtiges Abonnement. Im Rahmen unserer Partnerschaft mit Bark bietet GL.iNet jedoch den Bark-Home-Plan auf ausgewählten Routermodellen kostenlos an, einschließlich erweiterter Überwachung und Benachrichtigungen ohne Zusatzkosten.

3. Die beiden Parental-Control-Versionen können nicht gleichzeitig aktiviert werden. Beim Wechsel zwischen den Versionen wird die jeweils andere automatisch deaktiviert.

### Unterstützte Modelle

??? "Unterstützte Modelle"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint2)

??? "Nicht unterstützte Modelle"
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-X300B (Collie)

### Einrichtung

Melden Sie sich am webbasierten Admin Panel des Routers an und navigieren Sie zu **APPLICATIONS** -> **Parental Control**.

Wählen Sie die Bark-Version aus, schalten Sie den Schalter ein und klicken Sie auf **Apply**.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

**Hinweis:** Der Bark-Dienst ist möglicherweise in bestimmten Ländern nicht verfügbar. Da GL.iNet nicht der Anbieter dieses Dienstes ist, wenden Sie sich bei Problemen mit Bark bitte direkt an den [technischen Support von Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet).

Der Bark-Dienst ist aktiviert, aber dieses Gerät ist noch keinem Konto zugeordnet. Verwenden Sie bitte den [Device Pairing Link](https://www.bark.us/app/signup/?ref=glinet&home=glinet), um dieses Gerät mit Ihrem Bark-Konto zu koppeln.

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Nach der Kopplung wird die Seite wie folgt angezeigt.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Ihr Gerät ist jetzt mit den Bark Cloud Services verbunden und mit Ihrem Konto gekoppelt. Bitte [gehen Sie zu Bark](https://www.bark.us/app/children/?ref=glinet&home=glinet) und melden Sie sich dort an, um ein Profil für die Netzwerksteuerung zu erstellen.

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow gl-90-desktop"}

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
