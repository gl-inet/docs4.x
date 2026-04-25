# So erhalten Sie Konfigurationsdateien von WireGuard-Dienstanbietern

??? "AzireVPN"
    ### AzireVPN

    [Offizielle Website](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"}

    1. Rufen Sie die [offizielle Website von AzireVPN](https://www.azirevpn.com/aff/9x7wisg4){target="_blank"} auf und melden Sie sich an. Öffnen Sie anschließend den [WireGuard-Konfigurationsgenerator](https://www.azirevpn.com/cfg/wireguard){target="_blank"}.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator.png){class="glboxshadow"}

    2. Wählen Sie bei der IP-Option bitte **IPv4** aus. Klicken Sie dann auf **Download Configuration**.

        ![azirevpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/azirevpn/azirevpn_wireguard_generator_ip.png){class="glboxshadow"}

    3. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-azirevpn), um fortzufahren.

    4. Sie können AzireVPN auch über die [Mobile App](../faq/mobile_app.md) einrichten.

??? "Hide.me VPN"
    ### Hide.me VPN

    [Offizielle Website](https://hide.me/?friend=glinet){target="_blank"}

    Hide.me VPN bietet eine einfache Möglichkeit, den WireGuard-Dienst auf einem GL.iNet-Router zu verwenden.

    1. Verbinden Sie sich per [SSH](https://docs.gl-inet.com/router/en/3/tutorials/ssh/){target="_blank"} mit dem Router.

    2. Kopieren Sie die folgende Installations-URL, fügen Sie sie im Terminal ein und drücken Sie die Eingabetaste. (Mit einem Rechtsklick wird sie eingefügt.)

        `curl -fsSL https://raw.githubusercontent.com/eventure/hide.client.routers/master/glinet_v4/hidemevpn | sh -s install`

    3. Die Installation startet anschließend und fragt dann nach Benutzername und Passwort. Beim Eingeben oder Einfügen des Passworts ist im Terminal keine Änderung sichtbar. Drücken Sie nach der Eingabe einfach die Eingabetaste.

    4. Wenn Sie fertig sind, öffnen Sie das Web-Admin-Panel. Dort sehen Sie, dass bereits eine hide.me-VPN-Gruppe mit den Konfigurationsdateien erstellt wurde. Verbinden Sie sich damit wie mit jeder anderen Konfigurationsdatei.

    **Hinweis:** Der Schlüssel in der Hide.me-VPN-Konfigurationsdatei wird vor jeder Verbindung neu erzeugt und nach dem Trennen ungültig. Wenn Sie diese Konfigurationsdatei daher auf andere Geräte kopieren, kann die Verbindung nicht erfolgreich hergestellt werden.

    [Weiterführender Link](https://github.com/eventure/hide.client.routers){target="_blank"}

??? "Mullvad"
    ### Mullvad

    [Offizielle Website](https://mullvad.net/){target="_blank"}

    1. Rufen Sie die [offizielle Website von Mullvad](https://mullvad.net/){target="_blank"} auf und melden Sie sich an. Öffnen Sie anschließend den [Generator für WireGuard-Konfigurationsdateien](https://mullvad.net/en/account/#/wireguard-config){target="_blank"}.

    2. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md/#set-up-mullvad), um fortzufahren.

    3. Sie können Mullvad auch über die [Mobile App](../faq/mobile_app.md) einrichten.

??? "PIA (Private Internet Access)"
    ### PIA (Private Internet Access)

    [Offizielle Website](https://privateinternetaccess.com/offer/GLiNET_71dx4t8bl){target="_blank"}

    WireGuard-Konfigurationen können nicht über die Website heruntergeladen werden. Bitte verwenden Sie die [Mobile App](../faq/mobile_app.md), um PIA VPN einzurichten.

    <iframe width="560" height="315" src="https://www.youtube.com/embed/Fc7NTdQ9QFo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

??? "Surfshark"
    ### Surfshark

    [Offizielle Website](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"}

    1. Wenn Sie [Surfshark](https://get.surfshark.net/aff_c?offer_id=926&aff_id=1400){target="_blank"} verwenden, melden Sie sich an und öffnen Sie dann [diese Seite](https://my.surfshark.com/vpn/manual-setup/router){target="_blank"}. Klicken Sie auf **Router** und wählen Sie **WireGuard** aus.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_1.png){class="glboxshadow"}

    2. Wählen Sie im nächsten Fenster **I don't have a key pair** aus.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_2.png){class="glboxshadow"}

    3. Wählen Sie **Generate a new key pair**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_3.png){class="glboxshadow"}

    4. Sobald das Schlüsselpaar erzeugt wurde, wählen Sie **Choose a location**.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_4.png){class="glboxshadow"}

    5. Wählen Sie abschließend den Standort aus, den Sie einrichten möchten, und klicken Sie neben dem Standort auf die Schaltfläche **download**. Danach können Sie die Konfigurationsdateien herunterladen.

        ![surfshark wireguard manual setup](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/surfshark/surfshark_wireguard_manual_setup_5.png){class="glboxshadow"}

    6. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-surfshark), um fortzufahren.

    [Weiterführender Link](https://support.surfshark.com/hc/en-us/articles/6585805139474-How-to-set-up-a-manual-WireGuard-connection-on-Android-){target="_blank"}

??? "AirVPN"
    ### AirVPN

    [Offizielle Website](https://airvpn.org/?referred_by=402389){target="_blank"}

    1. Wenn Sie [AirVPN](https://airvpn.org/?referred_by=402389){target="_blank"} verwenden, melden Sie sich auf der Website an, öffnen den [Client Area](https://airvpn.org/client/){target="_blank"} und klicken dann auf den [Config Generator](https://airvpn.org/generator/){target="_blank"}.

        ![airvpn configuration generator](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_config_generator.png){class="glboxshadow" width="400"}

    2. Wählen Sie auf der Seite Config Generator im Bereich Protocols **WireGuard** aus.

        ![airvpn protocols](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_protocols.png){class="glboxshadow" width="600"}

    3. Wählen Sie einen Server aus, scrollen Sie dann bis zum Ende der Seite und klicken Sie auf die Schaltfläche **Generate**. Dadurch wird die Konfigurationsdatei heruntergeladen.

        ![airvpn select server](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/airvpn/airvpn_select_server.png){class="glboxshadow" width="600"}

    4. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "Astrill"
    ### Astrill

    [Offizielle Website](https://www.astrill.com/a/dik2masnw6ig){target="_blank"}

    Wenn Sie [Astrill](https://www.astrill.com/a/dik2masnw6ig){target="_blank"} verwenden, melden Sie sich bitte an und öffnen dann [diese Seite](https://www.astrill.com/member-zone/tools/wireguard-configuration){target="_blank"}, um WireGuard-Konfigurationen zu erzeugen.

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "IVPN"
    ### IVPN

    [Offizielle Website](https://www.ivpn.net/){target="_blank"}

    Wenn Sie [IVPN](https://www.ivpn.net/){target="_blank"} verwenden, müssen Sie die WireGuard-Konfiguration manuell erzeugen. Folgen Sie der Anleitung passend zu Ihrem Betriebssystem.

    [Windows](https://www.ivpn.net/setup/windows-10-wireguard/){target="_blank"}, [macOS](https://www.ivpn.net/setup/macos-wireguard/){target="_blank"}, [Linux](https://www.ivpn.net/setup/linux-wireguard/){target="_blank"}

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "NVPN"
    ### NVPN

    [Offizielle Website](https://www.nvpn.net/){target="_blank"}

    Folgen Sie der Anleitung [hier](https://support.nvpn.net/Knowledgebase/Article/View/428/0/how-to-use-our-wireguard#windows){target="_blank"}, um die Konfiguration zu erstellen.

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "OVPN"
    ### OVPN

    [Offizielle Website](https://www.ovpn.com/en?ref=glinet){target="_blank"}

    1. Melden Sie sich bei [www.ovpn.com](https://www.ovpn.com/en?ref=glinet){target="_blank"} an und suchen Sie im unten gezeigten Menü nach den WireGuard-Konfigurationsdateien.

        ![ovpn dashboard](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/get_wireguard_configuration_files.jpg){class="glboxshadow"}

    2. Klicken Sie auf **Generate WireGuard keys**, wählen Sie den gewünschten Server aus und laden Sie dann die Konfiguration herunter.

        ![ovpn generate wireguard keys](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/download_wireguard_configuration_files.jpg){class="glboxshadow"}

    3. Öffnen Sie die Konfiguration mit einem Texteditor und kopieren Sie den Inhalt.

        Die Konfiguration kann IPv6-Inhalte enthalten. Da GL.iNet-Router IPv6 noch nicht ausreichend unterstützen, entfernen Sie bitte die IPv6-Inhalte. Unten sehen Sie ein Beispiel; der markierte Bereich enthält den IPv6-Inhalt.

        ![remove wireguard ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/ovpn/remove_wireguard_ipv6_content.jpg){class="glboxshadow"}

    4. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

    5. Sie können OVPN auch über die [Mobile App](../faq/mobile_app.md) einrichten.

??? "PrivateVPN"
    ### PrivateVPN

    [Offizielle Website](https://affiliate.privatevpn.com/scripts/click.php?a_aid=5e3a511658bc3){target="_blank"}

    1. Melden Sie sich an und öffnen Sie dann das [Control panel](https://privatevpn.com/control-panel){target="_blank"}.

        ![PrivateVPN Control panel](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_1.jpg){class="glboxshadow"}

    2. Wählen Sie einen Server aus.

        ![select a server](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_2.jpg){class="glboxshadow"}

    3. Klicken Sie auf **GENERATE CONFIG** und kopieren Sie anschließend die Konfiguration.

        ![generate config](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/privatevpn/privatevpn_wireguard_3.jpg){class="glboxshadow"}

    4. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "PrivadoVPN"
    ### PrivadoVPN

    [Offizielle Website](https://privadovpn.com/#a_aid=GLINET){target="_blank"}

    Rufen Sie die Website von PrivadoVPN auf und melden Sie sich an.

    Suchen Sie im Dashboard den Abschnitt Manual Configuration, klicken Sie auf WireGuard, wählen Sie den Server aus, mit dem Sie sich verbinden möchten, und klicken Sie dann auf Download Configration.

    ![privadovpn wireguard manual configuration](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration.png){class="glboxshadow"}

    ![privadovpn wireguard manual configuration download](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/privadovpn/privadovpn_wireguard_manual_configuration_download.png){class="glboxshadow"}

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "Proton VPN"
    ### Proton VPN

    [Offizielle Website](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"}

    Wenn Sie [Proton VPN](https://go.getproton.me/aff_c?offer_id=26&aff_id=1612){target="_blank"} verwenden, folgen Sie bitte der Anleitung [hier](https://protonvpn.com/support/wireguard-configurations/){target="_blank"}, um die WireGuard-Konfigurationsdatei zu erzeugen.

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "PureVPN"
    ### PureVPN

    [Offizielle Website](https://billing.purevpn.com/aff.php?aff=35535){target="_blank"}

    Bitte lesen Sie [diese Anleitung](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"} oder folgen Sie den untenstehenden Schritten, um die PureVPN-Konfigurationsdatei manuell zu erhalten.

    1. Melden Sie sich mit Ihrem Konto im [PureVPN Member Area](https://my.puremember.com/){target="_blank"} an. Klicken Sie nach der Anmeldung im linken Menü auf **Manual Configuration**.

        ![purevpn manual1](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-1.png){class="glboxshadow"}

    2. Wählen Sie die Zielstadt aus und klicken Sie rechts auf **Download**.

        ![purevpn manual2](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-2.png){class="glboxshadow"}

    3. Wählen Sie im Pop-up-Fenster **WireGuard** als Protokoll aus.

        ![purevpn manual3](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-3.png){class="glboxshadow"}

    4. Wählen Sie **Linux** als Gerätetyp aus und klicken Sie dann auf **Generate Configuration**. Die Konfigurationsdatei wird auf Ihr lokales Gerät heruntergeladen.

        ![purevpn manual4](https://static.gl-inet.com/docs/router/en/4/tutorials/get_wg_configs/purevpn/purevpn-manual-4.png){class="glboxshadow"}

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um die Einrichtung abzuschließen.

    [Weiterführender Link](https://support.purevpn.com/router/how-to-setup-purevpn-on-glinet-router){target="_blank"}

??? "SpiderVPN"
    ### SpiderVPN

    [Offizielle Website](https://spidervpn.org/#a_aid=5ddfa0372e7ff){target="_blank"}

    1. Melden Sie sich bei [www.spidervpn.org](https://spidervpn.org/#a_aid=5ddfa0372e7ff) an, suchen Sie den Abschnitt zum Abrufen Ihrer VPN-Konfiguration und folgen Sie den dortigen Schritten.

        ![get spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_1.jpg){class="glboxshadow"}

    2. Laden Sie die VPN-Konfiguration herunter.

        ![download spider vpn configuration](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/spidervpn/spidervpn_config_2.jpg){class="glboxshadow"}

    3. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "StarVPN"
    ### StarVPN

    [Offizielle Website](https://www.starvpn.com/dashboard/aff.php?aff=91){target="_blank"}

    1. **Registrieren Sie ein Konto bei StarVPN**

        Rufen Sie die Optionen des [Tarifplans](https://www.starvpn.com/#pricing){target="_blank"} auf und wählen Sie einen VPN-Tarif, der zu Ihren Anforderungen passt. Sie können sich beim Checkout oder direkt [hier](https://www.starvpn.com/dashboard/register.php){target="_blank"} registrieren.

    2. **WireGuard-Konfiguration herunterladen**

        Melden Sie sich im StarVPN-Mitgliederbereich [dashboard](https://www.starvpn.com/dashboard){target="_blank"} an. Klicken Sie auf **Wireguard Config**, um die Konfigurationsdatei herunterzuladen. Jeder Slot enthält eine eindeutige WireGuard-Konfigurationsdatei.

        ![starvpn wireguard config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/wgconfigdl.png){class="glboxshadow"}

        **Tipp**: Wenn Sie die AmneziaWG-Verschleierung verwenden möchten, klicken Sie auf **AmneziaWG Config**, um die Konfigurationsdatei herunterzuladen. Jeder Slot enthält eine eindeutige AmneziaWG-Konfigurationsdatei.

        ![starvpn amneziawg config download](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/amneziawgdl.png){class="glboxshadow"}

    3. **Konfigurationsdatei bearbeiten (optional)**

        Die Konfiguration kann eine IPv6-Adresse enthalten. Um Kompatibilitäts- und Verbindungsprobleme zu vermeiden, öffnen Sie die `.conf`-Datei und entfernen Sie die IPv6-Adresse wie unten gezeigt.

        ![startvpn wireguard configuration remove ipv6 content](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/starvpn/remove_ipv6.jpg){class="glboxshadow"}

    4. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um die Konfigurationsdatei auf Ihren GL.iNet-Router hochzuladen.

    Weiterführende Links:

    - [WireGuard VPN Setup with StarVPN on GL.iNet Router](https://www.starvpn.com/wireguard-setup-on-gl-inet-router/){target="_blank"}
    - [AmneziaWG VPN Setup with StarVPN](https://www.starvpn.com/amnezia-vpn-setup-with-starvpn){target="_blank"}

??? "StrongVPN"
    ### StrongVPN

    [Offizielle Website](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"}

    1. Wenn Sie [StrongVPN](https://strongvpn.com/?tr_aid=5ac44bd241ca7){target="_blank"} verwenden, melden Sie sich unter [https://wg.strongvpn.com](https://wg.strongvpn.com){target="_blank"} an.

    2. Wählen Sie im Dropdown-Menü einen Standort aus, klicken Sie auf **GENERATE** und öffnen Sie die heruntergeladene Textdatei.

        ![strongvpn wireguard configuration generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/strongvpn/strongvpn_wireguard_configuration_generator.png){class="glboxshadow"}

    3. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

    4. Sie können StrongVPN auch über die [Mobile App](../faq/mobile_app.md) einrichten.

??? "TRUST.ZONE"
    ### TRUST.ZONE

    [Offizielle Website](https://trustzonevpn.info/r.php?RID=B-byr1v-MDAxNzE3NjgxMjM4){target="_blank"}

    1. Rufen Sie [https://trust.zone/setup](https://trust.zone/setup) auf und melden Sie sich an.

    2. Scrollen Sie zum Abschnitt WireGuard, wählen Sie den gewünschten Port aus und laden Sie dann entweder die Konfiguration für einen bestimmten Server oder eine ZIP-Datei mit allen Konfigurationen herunter.

    3. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "VPN.AC"
    ### VPN.AC

    [Offizielle Website](https://vpn.ac/aff.php?aff=1424){target="_blank"}

    1. Wenn Sie [VPN.AC](https://vpn.ac/aff.php?aff=1424){target="_blank"} verwenden, müssen Sie sich im Control Panel anmelden und im Menü "Services" den WireGuard Manager finden.

        ![VPN.AC WireGuard Manager](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_wireguard_manager.jpg){class="glboxshadow"}

    2. Erstellen Sie die Konfiguration und laden Sie sie herunter.

        ![VPN.AC create wireguard profiles](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnac/vpn.ac_create_wireguard_profiles.jpg){class="glboxshadow"}

    3. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "VPN Unlimited(KeepSolid)"
    ### VPN Unlimited(KeepSolid)

    [Offizielle Website](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"}

    1. Wenn Sie [VPN Unlimited](https://keepsolid.g2afse.com/click?pid=270&offer_id=7){target="_blank"} verwenden, melden Sie sich bei Ihrem [User Office](https://my.keepsolid.com/){target="_blank"} an, wählen Sie die Anwendung VPN Unlimited® aus und klicken Sie auf **Manage**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/01.jpg){class="glboxshadow"}

    2. Klicken Sie auf das Feld unter **Device** und wählen Sie **Manually create a new device…** > vergeben Sie einen benutzerdefinierten Namen, z. B. WireGuard > wählen Sie unter **Server** einen passenden Standort > wählen Sie im Dropdown-Menü das Protokoll **WireGuard**® aus > klicken Sie auf **Generate**.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/02.jpg){class="glboxshadow"}

    3. Die Konfigurationsparameter werden anschließend unten im Textformat angezeigt.

        ![vpn unlimited setup on gl.inet router](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/vpnunlimited/03.jpg){class="glboxshadow"}

        Kombinieren Sie die Konfiguration wie unten gezeigt.

        <p>
        [Interface]</br>
        PrivateKey = <i>Fügen Sie den PrivateKey aus Ihrem User Office ein</i></br>
        ListenPort = <i>Fügen Sie die Angaben für ListenPort ein</i></br>
        Address = <i>Fügen Sie die Adressinformationen ein</i></br>
        DNS = <i>Fügen Sie die DNS-Angaben aus dem User Office ein</i></br>
        </br>
        [Peer]</br>
        PublicKey = <i>Fügen Sie den PublicKey aus Ihrem User Office ein</i></br>
        PresharedKey = <i>Fügen Sie die Angaben für PresharedKey ein</i></br>
        AllowedIPs = <i>Fügen Sie die Angaben für AllowedIPs ein</i></br>
        Endpoint = <i>Fügen Sie die Endpoint-Informationen ein</i></br>
        </p>

    4. Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

    [Weiterführender Link 1](https://www.vpnunlimited.com/help/manuals/wireguard-setup-on-glinet-router){target="_blank"}

    [Weiterführender Link 2](https://www.vpnunlimited.com/help/manuals/wireguard/windows){target="_blank"}

??? "Windscribe"
    ### Windscribe

    [Offizielle Website](https://windscribe.com/yo/1u2h9ndl){target="_blank"}

    1. Melden Sie sich [hier](https://windscribe.com/login?auth_required){target="_blank"} bei Ihrem Windscribe-Konto an und öffnen Sie anschließend den [WireGuard Config Generator](https://windscribe.com/getconfig/wireguard){target="_blank"}.

    2. Wählen Sie den gewünschten Serverstandort und Port aus und klicken Sie dann auf **Download Config**.

        ![windscribe WireGuard Config Generator](https://static.gl-inet.com/docs/router/en/3/tutorials/wireguard_client/windscribe/windscribe_01.jpg){class="glboxshadow"}

    3. Folgen Sie [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

??? "12VPX"
    ### 12VPX

    [Offizielle Website](https://12vpx.com/?aff=1174){target="_blank"}

    Wenn Sie [12VPX](https://12vpx.com/?aff=1174){target="_blank"} verwenden, melden Sie sich an und öffnen dann [diese Seite](https://12vpx.com/setup/wireguard){target="_blank"}. Dort sehen Sie die Konfigurationen aller Server.

    Folgen Sie dann [dieser Anleitung](../interface_guide/wireguard_client.md#set-up-wireguard-client-manually-for-other-providers), um fortzufahren.

---

Haben Sie noch Fragen? Besuchen Sie unser [Community Forum](https://forum.gl-inet.com){target="_blank"} oder [kontaktieren Sie uns](https://www.gl-inet.com/contacts/){target="_blank"}.
