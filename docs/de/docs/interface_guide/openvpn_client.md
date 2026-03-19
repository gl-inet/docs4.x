# OpenVPN-Client auf GL.iNet-Routern einrichten

OpenVPN ist ein Open-Source-VPN-Protokoll, das mithilfe von Techniken für virtuelle private Netzwerke sichere Site-to-Site- oder Point-to-Point-Verbindungen aufbaut.

Um einen OpenVPN-Client auf einem GL.iNet-Router einzurichten, sehen Sie sich dieses Video an oder folgen Sie den untenstehenden Schritten.

<iframe width="560" height="315" src="https://www.youtube.com/embed/04sW3l6_rDM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

---

Bevor Sie beginnen, stellen Sie sicher, dass Sie ein aktives Abonnement bei einem VPN-Anbieter haben, der die manuelle OpenVPN-Konfiguration unterstützt. Klicken Sie [hier](https://www.gl-inet.com/solutions/vpn/){target="_blank"}, um die mit GL.iNet kompatiblen OpenVPN-Anbieter zu prüfen.

In der Regel müssen Sie zuerst die offizielle Website Ihres VPN-Anbieters besuchen, die Konfigurationsdatei abrufen und sie auf den Router hochladen, um ihn als OpenVPN-Client einzurichten. Wenn Sie nicht wissen, wie Sie die Konfigurationsdatei erhalten, lesen Sie [diesen Abschnitt](#konfigurationsdateien-von-openvpn-anbietern-abrufen) oder wenden Sie sich an den Support Ihres Anbieters.

Sie können einen OpenVPN-Client über das webbasierte Admin Panel oder die [GL.iNet App](../faq/mobile_app.md) einrichten. Nachfolgend finden Sie die Schritte für die Einrichtung über das webbasierte Admin Panel.

---

Navigieren Sie im webbasierten Admin Panel zu **VPN** -> **OpenVPN Client**.

Wenn Sie ein NordVPN-Abonnement haben, klicken Sie auf **NordVPN**, um sich anzumelden. Andernfalls klicken Sie auf **Add Manually**, um die OpenVPN-Konfigurationsdateien hochzuladen.

![openvpn client](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/openvpn_client_initial.png){class="glboxshadow"}

## NordVPN einrichten

[NordVPN](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} ist ein beliebter Online-VPN-Dienst für Geschwindigkeit und Sicherheit.

Die NordVPN-Schnelleinrichtung ist in das Admin Panel der GL.iNet-Router integriert. Sie können Konfigurationsdateien für alle NordVPN-Server online abrufen, indem Sie Ihre Kontodaten aus dem NordVPN-Dashboard im webbasierten Admin Panel oder in der GL.iNet App des Routers eingeben. So entfällt das manuelle Hochladen von Dateien.

1. Melden Sie sich [hier](https://my.nordaccount.com/){target="_blank"} bei Ihrem NordVPN-Webkonto an.

    ![nord login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

    Klicken Sie nach der Anmeldung im Nord-Dashboard auf **NordVPN** und anschließend auf **Set up NordVPN manually**.

    ![nord dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

    ![nord setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

    Dort finden Sie die **Service-Zugangsdaten**. Kopieren Sie diese für die spätere Verwendung.

    ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

2. Melden Sie sich am webbasierten Admin Panel Ihres Routers an, navigieren Sie zu VPN -> OpenVPN Client -> NordVPN. Geben Sie die in Schritt 1 erhaltenen **Service-Zugangsdaten** ein (Hinweis: Dies ist **NICHT** Ihre E-Mail-/Passwort-Kombination für die Kontoanmeldung) und klicken Sie dann auf **Save and Continue**.

    ![input nordvpn service credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn1.png){class="glboxshadow"}

3. Wählen Sie Protokoll, maximale Serveranzahl pro Standort und die gewünschten Standorte aus und klicken Sie dann auf **Apply**.

    ![select nordvpn servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn2.png){class="glboxshadow"}

    Daraufhin werden die Konfigurationsdateien heruntergeladen.

    ![nordvpn configuration files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn3.png){class="glboxshadow"}

4. Starten Sie eine Verbindung.

    Wählen Sie einen bevorzugten Server aus und klicken Sie rechts auf das Symbol mit den drei Punkten, um die Verbindung zu starten.

    ![nordvpn start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn4.png){class="glboxshadow"}

5. Nach erfolgreicher Verbindung erscheint ein grüner Punkt neben der Konfigurationsdatei.

    ![nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn5.png){class="glboxshadow"}

    Außerdem werden die Details der VPN-Verbindung im **VPN Dashboard** angezeigt.

    ![vpn dashboard nordvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn6.png){class="glboxshadow"}

6. Server aktualisieren.

    Sie können auf **Update Servers** klicken, um die neueste verfügbare Serverliste abzurufen. Dadurch lassen sich Verbindungsfehler vermeiden, die durch Serverwartung oder Abschaltungen verursacht werden.

    ![nordvpn update servers](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn7.png){class="glboxshadow"}

7. Zugangsdaten bearbeiten.

    Klicken Sie auf das Zahnradsymbol, um Ihre Zugangsdaten zu ändern.

    ![nordvpn edit credentials](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn8.png){class="glboxshadow"}

8. Alle Dateien löschen.

    Sie können auf **Delete All** klicken, um alle Konfigurationsdateien mit einem Klick zu löschen.

    ![nordvpn delete all](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nordvpn9.png){class="glboxshadow"}

## OpenVPN-Client manuell einrichten (für andere Anbieter)

Wenn Ihr OpenVPN-Anbieter nicht in unser Admin Panel integriert ist, besuchen Sie bitte zuerst die offizielle Website Ihres Anbieters, um die Konfigurationsdatei zu erhalten. Laden Sie diese anschließend auf den Router hoch, um einen OpenVPN-Client einzurichten.

In den folgenden Schritten verwenden wir [PIA (Private Internet Access)](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"} als Beispiel.

1. Laden Sie eine Konfigurationsdatei von der offiziellen Website von Private Internet Access herunter.

2. Melden Sie sich am webbasierten Admin Panel Ihres Routers an, navigieren Sie zu VPN -> OpenVPN Client und klicken Sie auf **Add Manually**.

    ![add manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual1.png){class="glboxshadow"}

3. Daraufhin wird in der linken Seitenleiste eine Gruppe erstellt.

    ![add a new group](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual2.png){class="glboxshadow"}

4. Geben Sie der Gruppe einen aussagekräftigen Namen (z. B. private internet access).

    ![set the new group name](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual3.png){class="glboxshadow"}

5. Laden Sie Ihre OpenVPN-Konfigurationsdatei hoch. Geben Sie bei Bedarf die Zugangsdaten ein und klicken Sie dann auf **Apply**.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual4.png){class="glboxshadow"}

    - Es gibt 4 Arten von Zugangsdaten für die Authentifizierung:

        1. Keine Authentifizierung.

        2. Nur Benutzername und Passwort.

        3. Nur Passphrase.

        4. Benutzername, Passwort und Passphrase.

    Anschließend wird die hochgeladene Konfigurationsdatei angezeigt.

    ![manual upload files](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual5.png){class="glboxshadow"}

6. Klicken Sie rechts auf das Symbol mit den drei Punkten, um eine Verbindung zu starten.

    ![start connect](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual6.png){class="glboxshadow"}

7. Nach erfolgreicher Verbindung erscheint ein grüner Punkt neben der Konfigurationsdatei.

    ![openvpn connected](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual7.png){class="glboxshadow"}

    Außerdem werden die Details der VPN-Verbindung im **VPN Dashboard** angezeigt.

    ![vpn dashboard openvpn status](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/manual8.png){class="glboxshadow"}

## OpenVPN-Server auf dem GL.iNet-Router einrichten

Wenn Sie zwei GL.iNet-Router besitzen, können Sie einen als OpenVPN-Server (eine öffentliche IP ist erforderlich) und den anderen als OpenVPN-Client verwenden. Auf diese Weise können Sie Ihre eigene VPN-Verbindung aufbauen, ohne einen VPN-Dienst eines Drittanbieters abonnieren zu müssen.

Für die Einrichtung eines OpenVPN-Servers lesen Sie bitte [hier](openvpn_server.md).

## Konfigurationsdateien von OpenVPN-Anbietern abrufen

Wir haben über 30 OpenVPN-Anbieter getestet und die Schritte zum Abrufen der Konfigurationsdateien dokumentiert. Wenn Sie nicht sicher sind, wie Sie die Konfigurationsdatei erhalten, folgen Sie bitte den untenstehenden Schritten.

Wenn Ihr abonnierter Anbieter unten nicht aufgeführt ist, wenden Sie sich bitte an dessen Support.

??? "NordVPN"
    ### NordVPN

    [Offizielle Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"}

    1. **Bei Ihrem NordVPN-Konto anmelden**

        Melden Sie sich auf der [offiziellen Website](https://go.nordvpn.net/aff_c?offer_id=15&amp;aff_id=12016&amp;url_id=902){target="_blank"} an und öffnen Sie das Nord-Account-Dashboard. Dort finden Sie die Service-Zugangsdaten.

        ![nordvpn login](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_login.png){class="glboxshadow"}

        Klicken Sie nach der Anmeldung im Nord-Dashboard links auf NordVPN und dann auf **Set up NordVPN manually**.

        ![nordvpn dashboard](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_dashboard.png){class="glboxshadow"}

        ![nordvpn setup manually](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_setup_manually.png){class="glboxshadow"}

        Suchen Sie die **Service-Zugangsdaten**. Kopieren Sie diese, falls Sie sie für den Upload der Konfiguration benötigen.

        ![nordvpn service credential](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_service_credentials.jpg){class="glboxshadow"}

    2. **Einen NordVPN-Server auswählen und die Konfigurationsdatei herunterladen**

        Gehen Sie zur Registerkarte **Server recommendation**. Dort wird Ihnen auf Basis Ihres Netzwerks ein Server empfohlen und die verfügbaren Protokolle zum Download angezeigt. Klicken Sie auf **Get setup configuration**, um fortzufahren.

        ![nordvpn config download](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_config_download.png){class="glboxshadow"}

        Wählen Sie im Popup-Fenster das Protokoll **OpenVPN** und laden Sie die UDP- oder TCP-Konfiguration herunter.

        ![nordvpn select protocol](https://static.gl-inet.com/docs/router/en/4/tutorials/openvpn_client/nord_select_protocol.png){class="glboxshadow"}

    Sie können die Konfigurationen aller Server [hier](https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip) herunterladen.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien aus der ZIP-Datei löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

    [Referenzlink](https://support.nordvpn.com/Connectivity/Router/1047409122/GL-iNet-setup-with-NordVPN.htm){target="_blank"}

    Sie können NordVPN auch mit der [GL.iNet App](../faq/mobile_app.md) einrichten.

??? "AirVPN"
    ### AirVPN

    [Offizielle Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Melden Sie sich bei Ihrem AirVPN-Konto an.

        ![airvpn client detail](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn1.png){class="glboxshadow"}

    2. Wählen Sie links **Config Generator** und anschließend **Linux** als Betriebssystem. Danach wählen Sie Ihren bevorzugten Server aus.

        ![openvpn config generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn2.png){class="glboxshadow"}

    3. Danach gelangen Sie zur Download-Seite der Konfigurationsdatei.

        ![download config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/airvpn/airvpn3.png){class="glboxshadow"}

??? "Astrill"
    ### Astrill

    [Offizielle Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Informationen zitiert aus der [Astrill official instruction](https://wiki.astrill.com/Astrill_Setup_Manual:How_to_configure_OpenVPN_with_OpenVPN_application_on_Windows){target="_blank"}

    1. Erzeugen und laden Sie die Astrill-OpenVPN-Konfigurations-ZIP herunter.

        ![astrill vpn tools](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill1.png){class="glboxshadow"}

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill2.png){class="glboxshadow"}

    2. Geben Sie eine Beschreibung wie OPENVPN_GUI ein.

    3. Klicken Sie auf die Schaltfläche **ADD to my certificates**.

        ![create new certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill3.png){class="glboxshadow"}

    4. Nachdem das OpenVPN-Zertifikat hinzugefügt wurde, klicken Sie auf **Download**.

        ![download certificate](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/astrillvpn/astrill4.png){class="glboxshadow"}

??? "BolehVPN"
    ### BolehVPN

    [Offizielle Website](https://www.bolehvpn.net/){target="_blank"}

    Melden Sie sich im [Dashboard](https://users.bolehvpn.net/){target="_blank"} an, laden Sie Ihre Konfigurationsdateien herunter und wählen Sie das Format [Linux_iOS inline](https://users.bolehvpn.net/download/inline/6){target="_blank"}. Entpacken Sie die ZIP-Dateien nach dem Download.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

    [Referenzlink](https://www.bolehvpn.net/clients-installations/#1487691248224-0c435dba-d612){target="_blank"}

??? "CactusVPN"
    ### CactusVPN

    [Offizielle Website](https://billing.cactusvpn.com/aff.php?aff=2310){target="_blank"}

    [Download](https://www.cactusvpn.com/downloads/){target="_blank"} direkt.

    ![download cactusvpn openvpn profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cactusvpn/cactusvpn1.jpg){class="glboxshadow"}

??? "Cryptostorm"
    ### Cryptostorm

    [Offizielle Website](https://cryptostorm.is/){target="_blank"}

    [Download](https://cryptostorm.is/configs/ecc/){target="_blank"} direkt.

??? "CyberGhost"
    ### CyberGhost

    [Offizielle Website](https://www.cyberghostvpn.com/offer/GLiNet_rem6fdij){target="_blank"}

    Informationen zitiert aus der [CyberGhost official instruction](https://support.cyberghostvpn.com/hc/en-us/articles/213811885-Router-How-to-configure-OpenVPN-for-flashed-DD-WRT-routers){target="_blank"}

    1. Melden Sie sich bei Ihrem CyberGhost-VPN-Onlinekonto an.

        ![login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost1.png){class="glboxshadow"}

    2. Wählen Sie im linken Menü "**VPN**" und klicken Sie dann auf "**Configure Device**". Erstellen Sie anschließend Ihre Serverkonfiguration wie unten beschrieben:

        ![config device](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost2.jpg){class="glboxshadow"}

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost3.jpg){class="glboxshadow"}

    3. Erstellen Sie nun Ihre Serverkonfiguration wie folgt:

        * **Protocol** : **OpenVPN**
        * **Country** : Da native Protokollverbindungen jeweils nur mit genau einem Server verwendet werden können, wählen Sie nun das Land aus, über das Sie surfen möchten. Der tatsächlich verwendete Server in diesem Land wird automatisch von CyberGhost ausgewählt.
        * **Server group** : Wählen Sie die Servergruppe und das OpenVPN-Protokoll (UDP oder TCP), das Sie verwenden möchten.

        **OpenVPN UDP** ermöglicht höhere Geschwindigkeiten als die TCP-Version, kann in manchen Fällen jedoch zu fehlerhaften Downloads führen. Dies ist die Standardeinstellung.

        **OpenVPN TCP** ermöglicht stabilere Verbindungen als die UDP-Version, ist jedoch etwas langsamer. Wählen Sie diese Version, wenn wiederholt Verbindungsprobleme wie plötzliche Trennungen auftreten.

        Sobald die gewünschten Parameter ausgewählt sind, speichern Sie sie mit **Save Configuration**.

    4. Um die für Sie generierten **OpenVPN**-Zugangsdaten auf dem Konfigurations-Dashboard anzuzeigen, klicken Sie auf **View Configuration**.

        ![view configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost4.png){class="glboxshadow"}

    5. Nachdem Sie Ihre Verbindungseinstellungen festgelegt haben, beachten Sie bitte Folgendes:

        * **Server Group** : Dies ist die Adresse des Landes bzw. Servers, mit dem Sie verbunden werden möchten, z. B. `12345-1-ca.cg-dialup.net`. Diese Adresse ändert sich je nach in Schritt zuvor ausgewähltem Land. Der tatsächlich verwendete einzelne Server wird automatisch von CyberGhost ausgewählt.
        * **Username** : Ein nur für dieses Protokoll generierter Benutzername. Dies ist **NICHT** Ihr normaler CyberGhost-Kontobenutzername, sondern wird ausschließlich zur Authentifizierung an CyberGhost-Servern bei manueller Konfiguration verwendet. Sie benötigen ihn für die Einrichtung von OpenVPN auf GL.iNet-Routern.
        * **Password** : Ein nur für dieses Protokoll generiertes Passwort. Dies ist **NICHT** Ihr normales CyberGhost-Kontopasswort, sondern wird ausschließlich zur Authentifizierung an CyberGhost-Servern bei manueller Konfiguration verwendet. Sie benötigen es für die Einrichtung von OpenVPN auf GL.iNet-Routern.

        Laden Sie anschließend die Konfigurationsdatei herunter. Klicken Sie dazu auf *Download Configuration* und speichern Sie die Datei auf Ihrem Computer.

        ![save config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/cyberghost/cyberghost5.png){class="glboxshadow"}

??? "ExpressVPN"
    ### ExpressVPN

    [Offizielle Website](https://go.expressvpn.com/c/4130682/1645813/16063){target="_blank"}

    Informationen zitiert aus der [offiziellen ExpressVPN-Anleitung](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

    1. Besuchen Sie die [ExpressVPN](https://go.expressvpn.com/c/4130682/1645813/16063){rel="sponsored" target="_blank"}-Website und melden Sie sich mit Ihren ExpressVPN-Zugangsdaten an.

        ![expressvpn account click sign in](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/expressvpn-account-click-sign-in.jpg){target="_blank"}

        Geben Sie den **Bestätigungscode** ein, der an Ihre E-Mail-Adresse gesendet wurde.

    2. Klicken Sie im Abschnitt „Set up your devices“ auf **More**.

        ![expressvpn, set up your devices, more](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_more.png){class="glboxshadow"}

    3. Klicken Sie auf **Manual Configuration**.

        ![expressvpn, set up your devices, manual configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/set_up_your_devices_manual_configuration.png){class="glboxshadow"}

    4. Dort sehen Sie Ihren **username**, Ihr **password** und eine Liste mit **OpenVPN configuration files**.

        ![expressvpn, setup info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/expressvpn/setup_info.png){class="glboxshadow"}

        Klicken Sie auf die gewünschten Standorte, um die `.ovpn`-Datei(en) herunterzuladen.

        **Lassen Sie dieses Browserfenster geöffnet**. Sie benötigen diese Informationen später für die Einrichtung.

    [Referenzlink](https://www.expressvpn.com/support/vpn-setup/manual-config-for-linux-with-openvpn/#download){rel="sponsored" target="_blank"}

??? "FastestVPN"
    ### FastestVPN

    [Offizielle Website](https://go.fastestvpn.com/affiliate/pap?a_aid=5ffd2a3e9d687){target="_blank"}

    Laden Sie die FastestVPN-Konfigurationsdateien für OpenVPN TCP und UDP als ZIP [hier](https://support.fastestvpn.com/download/fastestvpn_ovpn/) herunter.

    Tipp: Wenn die ZIP-Datei zu groß ist, löschen Sie einige `.ovpn`-Dateien aus dem ZIP-Ordner oder laden Sie nur eine einzelne `.ovpn`-Datei hoch.

    [Referenzlink](https://support.fastestvpn.com/tutorials/routers/gl-inet/openvpn){target="_blank"}

??? "FinchVPN"
    ### FinchVPN

    [Offizielle Website](https://www.finchvpn.com/){target="_blank"}

    1. Melden Sie sich bei Ihrem FinchVPN-Konto an.

        ![finchvpn login](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn1.jpg){class="glboxshadow"}

    2. Gehen Sie zur Download-Seite und klicken Sie unter FinchVPN OpenVPN Config auf **Download**.

        ![finchvpn download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn2.jpg){class="glboxshadow"}

    3. Wählen Sie **Linux**.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn3.jpg){class="glboxshadow"}

    4. Wählen Sie das Protokoll entsprechend Ihrer bevorzugten Verbindung. In der Regel können Sie die erste Option **Port 8484 over UDP** wählen.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn4.jpg){class="glboxshadow"}

    5. Denken Sie daran, das Kontrollkästchen zu aktivieren, damit Benutzername und Passwort vor dem Download in die Datei aufgenommen werden.

        ![finchvpn](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/finchvpn/finchvpn5.jpg){class="glboxshadow"}

??? "HideIPVPN"
    ### HideIPVPN

    [Offizielle Website](https://www.hideipvpn.com/){target="_blank"}

    1. Melden Sie sich bei Ihrem HideIPVPN-Konto an.

    2. Gehen Sie links zu **Package**, klicken Sie auf Ihr Paket und stellen Sie sicher, dass es aktiv ist.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/package.jpg){class="glboxshadow"}

    3. Auf der Registerkarte **VPN** finden Sie unter VPN Login Details den Benutzernamen und das Passwort, die für die OpenVPN-Verbindung verwendet werden.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/vpn_username_password.jpg){class="glboxshadow"}

    4. Scrollen Sie nach unten, um die OpenVPN-Konfigurationsdateien herunterzuladen.

        ![hideipvpn client area](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideipvpn/openvpn_config_files.jpg){class="glboxshadow"}

??? "Hide.me VPN"
    ### Hide.me VPN

    [Offizielle Website](https://hide.me/?friend=glinet){target="_blank"}

    1. Melden Sie sich bei Ihrem Hide.me-Konto an und suchen Sie links die **Server Locations**.

    2. Laden Sie die OpenVPN-Konfiguration für Windows herunter.

        ![hide.me vpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/hideme/hideme_dashboard.jpg){class="glboxshadow"}

??? "Hotspot Shield"
    ### Hotspot Shield

    [Offizielle Website](https://trk.aclktrkr.com/aff_c?offer_id=59&aff_id=3722){target="_blank"}

    **Hinweis: Die Router-Konfigurationsdateien von Hotspot Shield sind nicht mehr verfügbar bzw. werden nicht mehr unterstützt. Die folgenden Schritte dienen nur noch als Altanleitung für Benutzer, die diese Dateien bereits installiert haben.**

    1. Gehen Sie zu [https://www.hotspotshield.com/](https://www.hotspotshield.com/) und klicken Sie auf **Account**. Melden Sie sich an, falls Sie dazu aufgefordert werden.

        ![hotspot shield login](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/hotspotshield_front_page.png){class="glboxshadow"}

    2. Gehen Sie zu [https://app.hotspotshield.com/app/hotspotshield/router](https://app.hotspotshield.com/app/hotspotshield/router)

        Wählen Sie im Dropdown **Select location** den virtuellen Standort aus, den der Router verwenden soll. Klicken Sie anschließend auf **Download file**. Die Konfigurationsdatei (`config.ovpn`) wird auf Ihren Computer heruntergeladen. Benutzername und Passwort müssen bei der Einrichtung des OpenVPN-Clients auf dem Router eingegeben werden.

        ![hotspot shield link router](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/hotspot_shield/link_router.png){class="glboxshadow"}

    [Referenzlink](https://support.hotspotshield.com/hc/en-us/articles/360038538012-How-do-I-install-Hotspot-Shield-on-my-GL-iNet-router)

??? "IPVANISH"
    ### IPVANISH

    [Offizielle Website](https://affiliate.ipvanish.com/aff_c?offer_id=1&aff_id=3073){target="_blank"}

    - Sie können alle Konfigurationsdateien für sämtliche Server [hier](https://configs.ipvanish.com/configs/configs.zip) herunterladen. Die ZIP-Datei enthält alle Server-Konfigurationsdateien (`.ovpn`) sowie eine Zertifikatsdatei (`.crt`). Die ZIP-Datei ist für einige Modelle möglicherweise etwas groß. Löschen Sie daher bitte die Server-Konfigurationen (`.ovpn`), die Sie nicht verwenden werden.

        ![ipvanish all openvpn configs](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_all_openvpn_configs.png){class="glboxshadow"}

    - Sie können einzelne Server-Konfigurationsdateien auch [hier](https://www.ipvanish.com/software/configs/) herunterladen, müssen dann aber zusätzlich **ca.ipvanish.com.crt** herunterladen. Bevor Sie die Dateien auf den Router hochladen, müssen Sie **ca.ipvanish.com.crt** und die `.ovpn`-Dateien zusammen in ein `.zip`-Archiv packen.

        ![ipvanish openvpn config file with certificate file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ipvanish/ipvanish_openvpn_config_file_with_certificate_file.png){class="glboxshadow"}

    [Referenzlink](https://support.ipvanish.com/hc/en-us/articles/360001329813-Android-OpenVPN-Setup)

??? "IVACY"
    ### IVACY

    [Offizielle Website](https://billing.ivacy.com/page/22852){target="_blank"}

    Für die Einrichtung eines OpenVPN-Clients mit Ivacy benötigen Sie Folgendes:

    - Ihren Benutzernamen für die manuelle OpenVPN-Konfiguration, der in der Eingabeaufforderung „Download Configuration“ angezeigt wird
      ![ivacy openvpn username](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ivacy-username.png){class="glboxshadow"}
    - Ihr Passwort (dasselbe, das Sie für die Anmeldung bei Ihrem Ivacy-Konto verwenden)
    - Eine OpenVPN-Konfigurationsdatei

    [Referenzlink](https://support.ivacy.com/setup_guide/how-to-setup-ivacy-on-gl-inet-router/)

??? "IVPN"
    ### IVPN

    [Offizielle Website](https://www.ivpn.net/){target="_blank"}

    1. Laden Sie die [OpenVPN-Konfigurationsdateien](https://www.ivpn.net/releases/config/ivpn-openvpn-config.zip) herunter.

    2. Suchen Sie die Account ID im [IVPN-Kundenbereich](https://www.ivpn.net/clientarea/login){target="_blank"}.

    3. Wenn Sie die Konfigurationsdatei in **Add a New OpenVPN Configuration** ziehen, werden Sie aufgefordert, Benutzername und Passwort einzugeben. Der Benutzername ist Ihre Account ID, die mit **ivpn** beginnt. Das Passwort kann beliebig sein, zum Beispiel **ivpn**.

        ![ivpn set up on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ivpn/ivpn_set_up_openvpn_client.png){class="glboxshadow"}

    [Referenzlink](https://www.ivpn.net/setup/gnu-linux-terminal.html)

??? "Mullvad"
    ### Mullvad

    [Offizielle Website](https://mullvad.net/en){target="_blank"}

    1. Besuchen Sie die [Mullvad](https://mullvad.net/en){rel="sponsored" target="_blank"}-Website und melden Sie sich mit Ihren Mullvad-Zugangsdaten an.

    2. Wählen Sie **OpenVPN Configuration**.

    ![ovpnconfig](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/ovpnconfig.jpg){class="glboxshadow"}

    3. Wählen Sie **Linux** und anschließend den gewünschten Serverstandort aus.

    ![linux](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/linux.jpg){class="glboxshadow"}

??? "OVPN"
    ### OVPN

    [Offizielle Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    Melden Sie sich einfach an. Anschließend können Sie die OpenVPN-Konfigurationsdatei über das unten gezeigte Menü abrufen.

    ![get ovpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/get_ovpn_configuration_files.jpg){class="glboxshadow"}

    Wählen Sie den Server und laden Sie ihn herunter.

    ![download ovpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/ovpn/download_configuration_files.jpg){class="glboxshadow"}

    Benutzername und Passwort sind dieselben wie für die Anmeldung bei OVPN.

??? "OysterVPN"
    ### OysterVPN

    [Offizielle Website](https://go.oystervpn.net?a_aid=glinet){target="_blank"}

    1. Öffnen Sie [die OysterVPN-Serverlistenseite](https://support.oystervpn.com/server-list/){target="_blank"} und klicken Sie auf **Download .ovpn file**, um die Konfigurationsdatei herunterzuladen.

        ![download oystervpn .ovpn file](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/oystervpn/download_ovpn_file.png){class="glboxshadow"}

    2. Benutzername und Passwort für die OpenVPN-Verbindung sind dieselben wie für die Anmeldung bei OysterVPN.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

??? "PIA (Private Internet Access)"
    ### PIA

    [Offizielle Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    [Download](https://www.privateinternetaccess.com/openvpn/openvpn.zip) direkt.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Offizielle Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Melden Sie sich einfach an. Anschließend finden Sie problemlos **Download VPN Configuration**.

    ![PrivadoVPN OpenVPN configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privadovpn/privadovpn_openvpn_configuration.png){class="glboxshadow"}

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

??? "PrivateVPN"
    ### PrivateVPN

    [Offizielle Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    [Download](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/privatevpn/PrivateVPN-TUN.zip){target="_blank} direkt.

    [Hier](https://privatevpn.com/client/PrivateVPN-TUN.zip) ist der offizielle Download-Link. Aufgrund eines Fehlers beim Import in den Router enthält der Dateiname in der Datei Sonderzeichen wie „Bogotá“. Wir haben die Datei umbenannt und den obigen Download-Link bereitgestellt. Dieser Fehler wird in zukünftigen Versionen behoben.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

??? "Proton VPN"
    ### Proton VPN

    [Offizielle Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    **Proton VPN bietet WireGuard an. Wir empfehlen daher die Verwendung von WireGuard. Mehr dazu [hier](wireguard_client.md#wireguard-providers).**

    1. Melden Sie sich bei Ihrem [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}-Konto an.

    2. Klicken Sie links auf **Download**.

    3. Wählen Sie die Plattform Router, das gewünschte Protokoll usw. aus und suchen Sie Ihr Zielland, um die Konfigurationsdatei herunterzuladen.

        ![protonvpn openvpn configuration file](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/proton_openvpn_configuration_file.jpg){class="glboxshadow"}

    4. Die Zugangsdaten für die OpenVPN-Verbindung sind nicht dieselben wie für die Anmeldung im Proton-Dashboard. Sie finden die Zugangsdaten unter **Account -> OpenVPN/IKEv2 username**.

        ![protonvpn openvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/protonvpn/protonvpn_openvpn_credential.jpg){class="glboxshadow"}

??? "PureVPN"
    ### PureVPN

    [Offizielle Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Für die Einrichtung eines OpenVPN-Clients mit PureVPN benötigen Sie Ihren OpenVPN-Benutzernamen, Ihr Passwort und eine Konfigurationsdatei, die Sie in Ihrem PureVPN-Konto finden.

    1. [Melden Sie sich bei Ihrem PureVPN-Konto an.](https://my.purevpn.com/)
    2. Klicken Sie in der linken Seitenleiste auf **Subscriptions**.
    3. Scrollen Sie nach unten, um Ihren OpenVPN-Benutzernamen und Ihr Passwort zu finden.
        ![purevpn username and password](https://static.gl-inet.com/docs/router/en/4/interface_guide/openvpn_client/purevpn-vpn-username-vpn-password.png){class="glboxshadow"}
    4. Klicken Sie in der linken Seitenleiste auf **Manual Configuration**.
    5. Wählen Sie einen VPN-Standort und klicken Sie auf **Download**, um die Konfigurationsdatei herunterzuladen.

    [Referenzlink](https://support.purevpn.com/openvpn-files)

    GL.iNet-Router unterstützen die [dedicated IP](https://www.purevpn.com/dedicated-ip){target="_blank"}-Funktion von PureVPN nicht, da sie PPTP benötigt.

??? "SaferVPN"
    ### SaferVPN

    [Offizielle Website](https://safervpn.com/?a_aid=563){target="_blank"}

    [Download](https://support.safervpn.com/hc/en-us/articles/360035425314-What-are-SaferVPN-s-OpenVPN-configuration-ovpn-files-for-manual-setup) direkt.

    ![safervpn openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/safervpn/safervpn1.png){class="glboxshadow"}

??? "StarVPN"
    ### StarVPN

    [Offizielle Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    StarVPN bietet auch WireGuard an. Wir empfehlen daher WireGuard. Mehr dazu [hier](wireguard_client.md#starvpn).

    1. **Ein Konto bei StarVPN registrieren**

        Besuchen Sie die [pricing plan](https://www.starvpn.com/#pricing){target="_blank"}-Seite, wählen Sie einen passenden VPN-Tarif und registrieren Sie sich beim Checkout oder direkt [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"}.

    2. VPN-Anmeldeinformationen

        Melden Sie sich im [Dashboard](https://www.starvpn.com/dashboard){target="_blank"} des StarVPN-Mitgliederbereichs an. Ihren VPN-Benutzernamen und Ihr Passwort für jeden Slot finden Sie im Bereich **Manage Slots** oder direkt im Dashboard.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_edited-2.jpg){class="glboxshadow"}

        Bei mehreren Slots finden Sie die VPN-Konfigurationseinstellungen und Zugangsdaten im Bereich **Manage Slots**.

        ![starvpn credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/vpn-username_slots_edited-1024x355.jpeg){class="glboxshadow"}

    3. OpenVPN-Konfigurationsdatei herunterladen

        Im nächsten Schritt müssen Sie die VPN-Server-Konfigurationsdateien herunterladen, damit die OpenVPN-Software weiß, wohin sie sich verbinden soll. Laden Sie die Konfigurationsdatei im Dashboard des Mitgliederbereichs herunter.

        ![download starvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/download-ovpn_edited.jpg){class="glboxshadow"}

        Einige GL.iNet-Router unterstützen kein IPv6 oder keinen DNS Leak Protection. Daher können IP- oder Verbindungsfehler auftreten. Bearbeiten Sie in diesem Fall die `.ovpn`-Datei und deaktivieren Sie IPv6.

        ![troubleshooting](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/starvpn/troubleshooting.jpg){class="glboxshadow"}

??? "StreamVPN"
    ### StreamVPN

    [Offizielle Website](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}

    1. Melden Sie sich mit Ihrem [StreamVPN](https://billing.streamvpn.com/account/signup?aff_t=aaf341756f7b94ed3f040f78292b80f1db1adf3318eacb87dd9c4ad4e08fde11a%3A2%3A%7Bs%3A6%3A%22aff_id%22%3Bs%3A6%3A%22645311%22%3Bs%3A6%3A%22off_id%22%3Bi%3A10%3B%7D){target="_blank"}-Konto an. Dort sehen Sie dann Ihre Abonnementinformationen. Klicken Sie auf **Install & Guides**.

        ![streamvpn subscription info](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_subscription.png){class="glboxshadow"}

    2. Klicken Sie auf **VPN Router**. Dadurch wird eine ZIP-Archivdatei mit dem Namen `StreamVPN.zip` heruntergeladen.

        ![streamvpn guide, vpn router](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/streamvpn/streamvpn_guide_router.png){class="glboxshadow"}

    **Hinweis:** Es funktionieren nur Konfigurationsdateien, deren Dateiname „Primary“ enthält.

??? "StrongVPN"
    ### StrongVPN

    [Offizielle Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Melden Sie sich mit Ihrem [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}-Konto an. Anschließend wird die Übersicht **VPN Accounts Summary** angezeigt. Klicken Sie auf **Account Setup Instructions**.

        ![strongvpn setup 1](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_01.jpg){class="glboxshadow"}

    2. Suchen Sie den Bereich **Manual setup** und folgen Sie den dortigen Schritten, um die Konfiguration abzurufen.

        ![strongvpn get config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/strongvpn/strong_vpn_setup_02.jpg){class="glboxshadow"}

??? "Surfshark"
    ### Surfshark

    [Offizielle Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. **Anmeldedaten finden**

        Die Surfshark-Service-Zugangsdaten unterscheiden sich von Ihren Surfshark-Kontodaten, also Ihrer E-Mail-Adresse und Ihrem Passwort. Für die manuelle OpenVPN-Konfiguration auf dem Router benötigen Sie die Surfshark-Service-Zugangsdaten.

        Melden Sie sich auf der [offiziellen Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} an und gehen Sie zu [dieser Seite](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}. Dort finden Sie alle Details, die für eine manuelle Verbindung erforderlich sind.

        ![surfshark service credential](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_service_credential.png){class="glboxshadow"}

    2. **Einen Surfshark-Server auswählen**

        Wählen Sie die Registerkarte **Locations** aus. Dort werden alle Surfshark-Server angezeigt.

        ![surfshark locations](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_locations.png){class="glboxshadow"}

        Anschließend werden Sie gefragt, ob Sie TCP oder UDP verwenden möchten. Die Unterschiede finden Sie [hier](../faq/openvpn_tcp_udp.md).

        ![surfshark tcp udp](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/surfshark/surfshark_udp_tcp.png){class="glboxshadow" width="400"}

    Sie können alle Konfigurationen direkt [hier](https://api.surfshark.com/v1/server/configurations) herunterladen.

    Tipp: Wenn die ZIP-Datei zu groß für den Upload ist, können Sie einige `.ovpn`-Dateien daraus löschen oder nur eine einzelne `.ovpn`-Datei hochladen.

    [Referenzlink](https://support.surfshark.com/hc/en-us/articles/360011856259-How-to-set-up-Surfshark-on-GL-iNet-router-3-x-firmware-){target="_blank"}

??? "VPN.AC"
    ### VPN.AC

    [Offizielle Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    [Download](https://vpn.ac/ovpn/).

    <img class="glboxshadow" alt="vpn.ac donwoad configuration" src="https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpn.ac/vpn.ac1.png" />

??? "VPNGate"
    ### VPNGate

    [Offizielle Website](https://www.vpngate.net/en/){target="_blank"}

    Die OpenVPN-Konfigurationsdateien werden auf der [VPN Gate-Website](https://www.vpngate.net/en/) entsprechend dem Serverstandort aufgeführt.

    1. Klicken Sie in der Spalte **OpenVPN** auf **OpenVPN Config file**.

        ![VPNGate server list](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate1.png){class="glboxshadow"}

    2. Danach wird die Download-Seite angezeigt.

        ![VPNGate download page](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpngate/vpngate2.png){class="glboxshadow"}

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Offizielle Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    Informationen zitiert aus der [VPN unlimited official instruction](https://www.vpnunlimitedapp.com/en/info/manuals/how-to-manually-create-vpn-conf){target="_blank"}

    Melden Sie sich zunächst in Ihrem User Office an, klicken Sie für den VPN-Unlimited-Dienst auf **Manage** und folgen Sie einigen einfachen Schritten:

    1. Ein Gerät auswählen

        Wählen Sie ein Gerät aus der Liste oder erstellen Sie ein neues. Wenn keine freien Slots mehr verfügbar sind, löschen Sie ein altes Gerät oder kaufen Sie zusätzliche Slots.

        ![vpn unlimited openvpn config](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid1.png){class="glboxshadow"}

    2. Den gewünschten Serverstandort wählen

        VPN Unlimited bietet eine große Auswahl an Servern, nämlich mehr als 400 in über 70 Standorten. In diesem Beispiel nehmen wir Deutschland.

    3. Das VPN-Protokoll auswählen

        Wählen Sie das Protokoll **OpenVPN**.

        ![vpn unlimited select protocol](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid2.png){class="glboxshadow"}

    4. Eine Konfiguration erstellen

        Klicken Sie auf **Generate**. Danach erhalten Sie alle Daten, die für die Einrichtung der VPN-Verbindung erforderlich sind.

        ![vpn unlimited generate configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/vpnunlimited/keepsolid3.png){class="glboxshadow"}

??? "VyprVPN"
    ### VyprVPN

    VyprVPN stellt die OpenVPN-Dateien hier bereit: [Where can I find the OpenVPN files? – VyprVPN Support](https://support.vyprvpn.com/hc/en-us/articles/360038096131-Where-can-I-find-the-OpenVPN-files-){target="_blank"}

    Die bereitgestellte ZIP-Datei enthält zwei Ordner mit `.ovpn`-Dateien: einen mit dem Namen `OpenVPN160` und einen mit dem Namen `OpenVPN256`. Löschen Sie einfach den Ordner `OpenVPN160` aus der ZIP-Datei und laden Sie die Datei dann wie gewohnt auf den GL.iNet-Router hoch.

??? "Windscribe"
    ### Windscribe

    [Offizielle Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Melden Sie sich [hier](https://windscribe.com/login?auth_required){target="_blank"} bei Ihrem Windscribe-Mitgliedskonto an und öffnen Sie dann den [OpenVPN Config Generator](https://windscribe.com/getconfig/openvpn){target="_blank"}.

    2. Wählen Sie den Serverstandort, das Protokoll (UDP/TCP), den Port (z. B. 1194) und die OpenVPN-Version aus, die Sie verwenden möchten – vorzugsweise die neuere – und klicken Sie dann auf **Download Config**. Danach wird eine Datei mit der Endung `.ovpn` auf Ihr lokales Gerät heruntergeladen.

        ![windscribe OpenVPN Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/windscribe/ovpn-config-generator.png){class="glboxshadow"}

    3. Klicken Sie auf derselben Seite auf die Schaltfläche **Get Credentials**. Anschließend erhalten Sie die zugehörigen Zugangsdaten, die später im webbasierten Admin Panel des Routers bei der Authentifizierung beim Hochladen der Konfigurationsdatei benötigt werden. Kopieren Sie die Zugangsdaten oder lassen Sie diese Webseite geöffnet.

    4. Folgen Sie anschließend [dieser Anleitung](../interface_guide/openvpn_client.md#set-up-openvpn-client-manually-for-other-providers), um fortzufahren.

??? "ZoogVPN"
    ### ZoogVPN

    [Offizielle Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"}

    Melden Sie sich auf der [offiziellen Website](https://zoogvpn.com/pricing?ref=xrsyzx){target="_blank"} an und öffnen Sie anschließend die [Seite für OpenVPN-Konfigurationsdateien](https://app.zoogvpn.com/setup/configuration-files){target="_blank"}. Dort finden Sie alle Server. Laden Sie die Konfigurationsdatei in der TCP- oder UDP-Spalte herunter.

    ![zoogvpn openvpn configuration files](https://static.gl-inet.com/docs/router/en/3/tutorials/openvpn_client/zoogvpn/zoogvpn_openvpn_config_files.png)

    Folgen Sie anschließend der [Anleitung zum Einrichten von OpenVPN Client auf einem GL.iNet-Router](#openvpn-client-auf-glinet-routern-einrichten). Benutzername und Passwort sind dieselben wie für die Anmeldung auf der ZoogVPN-Website.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
