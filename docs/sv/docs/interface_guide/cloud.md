# GL.iNet GoodCloud {#glinet-goodcloud}

## Introduction {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} är en plattform som förenklar fjärrdistribution och hantering av anslutna enheter. Den ger enkel fjärråtkomst till GL.iNet-routrar. Genom att samla nätverksenheter i molnet kan du effektivt utföra batchåtgärder som distribution av nätverkskonfigurationer och programvaruuppgraderingar. Du kan även fjärransluta till routerns webbadministrationspanel eller terminal via SSH och hantera nätverksenheter mellan regioner från ände till ände.

Med GoodCloud kan du:

1. Check the router's real-time status
    - Monitor online-offline status
    - View real-time RAM usage and load average
    - Receive email alerts for online-offline status changes

2. Set up routers remotely
    - configure router settings (e.g. SSID and password)
    - Remote SSH access
    - Remote access to the WebUI
    - Share router access with others

3. Monitor connected clients remotely
    - View devices connected to your network
    - Monitor real-time traffic and block clients
    - Receive email alerts for new connections and block events

4. Perform batch operations
    - Batch reboot
    - Batch firmware upgrade

5. Establish Site-to-Site connectivity
    - Virtual Office: Extend your office network to other branch offices
    - Business Travel: Remotely access office systems (e.g., OA, CRM, MySQL)
    - Smart Home: Remotely access home devices (e.g., IP cameras, NAS)

Om du behöver hantera flera enheter och använda avancerade funktioner som massåtgärder, hantering av flera konton och anpassade lösningar väljer du våra tilläggsabonnemang. Mer information finns [här](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"}. Kontakta gärna [support@gl-inet.com](mailto:support@gl-inet.com).

## Bind Devices to Cloud {#bind-devices-to-cloud}

Välj avsnittet som motsvarar enhetens firmwareversion för steg om enhetskoppling.

### För firmware v4.10 och senare {#for-firmware-v410-and-above}

1. Enable GoodCloud.

    Log in to your router's web Admin Panel, navigate to **CLOUD SERVICE** -> **GoodCloud** and click **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    Sidan **GL.iNet Account** öppnas. Klicka på **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    Klicka på **Continue** i popup-fönstret. Du omdirigeras till GoodCloud-webbplatsen för att slutföra kopplingen.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Log in to bind your device.

    Logga in på GL.iNet-kontot. Om du saknar konto registrerar du ett och loggar in.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Bekräfta konto- och enhetsinformationen efter inloggning, däribland Device ID, modell och MAC-adress. Ange ett enhetsnamn och klicka på **Bind** för att koppla routern till kontot.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Om verifieringsmeddelandet inte kommer kontrollerar du skräppostmappen eller väntar några minuter och försöker igen. Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) för mer hjälp.

3. Binding details.

    När kopplingen är klar återgår du till routerns webbadministrationspanel och öppnar **CLOUD SERVICES** -> **GoodCloud**. Sidan visar en omdirigeringspost till GoodCloud-plattformen, enhetsidentitet och senaste molnloggar.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Remote Access.

    I firmware v4.10 aktiveras fjärråtkomst till routerns webbadministrationspanel och terminal som standard när routern kopplas till GoodCloud.

5. Unbind device.

    Koppla bort routern genom att logga in på webbadministrationspanelen, öppna **CLOUD SERVICES** -> **GL.iNet Account** och klicka på **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    Du kan även ta bort enheten från listan Bound Devices på GoodCloud-plattformen. Routerns webbadministrationspanel synkroniseras och visar aktuell kopplingsstatus.

    Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) om problem uppstår.

### For firmware v4.7 to v4.9 {#for-firmware-v47-to-v49}

1. Enable GoodCloud.

    Logga in på routerns webbadministrationspanel och öppna **CLOUD SERVICE** -> **GoodCloud**.

    Klicka på **Get Started**. Popup-fönstret Cloud Service visas uppe till höger. Klicka på **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. Log in to bind your device.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Om du saknar konto registrerar du ett och loggar in. När registreringen är klar kopplas routern automatiskt till kontot.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Om verifieringsmeddelandet inte kommer kontrollerar du skräppostmappen eller väntar några minuter och försöker igen. Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) för mer hjälp.

3. Binding details.

    När kopplingen är klar återgår du till webbadministrationspanelen och klickar på Cloud-ikonen uppe till höger. Kopplingsinformationen visas, däribland användarnamn, tid, Device ID, Device MAC och Device S/N.

    ![binding details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. Enable Remote Access.

    Öppna **CLOUD SERVICES** -> **GoodCloud** i webbadministrationspanelen för att aktivera fjärråtkomst.

    ![enable remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: Fjärråtkomst till routerns terminal via SSH från GoodCloud-plattformen.

    - **Remote Web Access**: Fjärråtkomst till routerns webbadministrationspanel via HTTP/HTTPS från GoodCloud-plattformen.

    - **View Logs**: It will show API call logs by GoodCloud.

5. Unbind device.

    Koppla bort routern genom att logga in på webbadministrationspanelen, klicka på molnikonen uppe till höger och sedan på **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    Du kan även ta bort enheten från listan Bound Devices på GoodCloud-plattformen. Routerns webbadministrationspanel synkroniseras och visar aktuell kopplingsstatus.

    Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) om problem uppstår.

### For firmware v4.6 or earlier {#for-firmware-v46-or-earlier}

1. Enable GoodCloud.

    Logga in på routerns webbadministrationspanel, öppna **APPLICATIONS** -> **GoodCloud** och aktivera GoodCloud med reglaget.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    Aktivera **Remote SSH** och **Remote Web Access** vid behov, välj närmaste server, läs och godkänn **Terms of Service & Privacy Policy** och klicka på **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: Fjärråtkomst till routerns terminal via SSH från GoodCloud-plattformen.

    - **Remote Web Access**: Fjärråtkomst till routerns webbadministrationspanel via HTTP/HTTPS från GoodCloud-plattformen.

    - **Data Server**: Välj servern närmast enheten. Alternativen är Asia Pacific (Japan), America (Oregon) och Europe (Ireland).

2. Sign up an account.

    Visit the [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, sign up and log in.

    Om verifieringsmeddelandet inte kommer kontrollerar du skräppostmappen eller väntar några minuter och försöker igen. Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) för mer hjälp.

3. Add devices.

    On the Cloud platform, navigate to **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Enheter kan kopplas till GoodCloud-kontot med Auto Discover, Manually Add eller Bulk Import.

    ??? "Auto Discover"

        Prova **Auto discover** om routern och enheten som används för GoodCloud-webbplatsen finns i samma nätverk.

        Välj enheten i listrutan och ange **DDNS / Device ID**, som finns på routerns undersida eller sidan GoodCloud i webbadministrationspanelen.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Se [den här länken](../faq/where_to_find_the_device_id_mac_sn.md) för att hitta Device ID.

    ??? "Manually Add"

        Om enheten saknas i listan klickar du på **Manually add** och anger routerinformationen. Uppgifterna finns på routerns undersida eller sidan GoodCloud i webbadministrationspanelen.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** är avsett för hantering av många enheter. Flera enheter kan importeras via en Microsoft Excel-fil.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Binding details.

    När kopplingen är klar återgår du till webbadministrationspanelen och öppnar **APPLICATIONS** -> **GoodCloud**. Sidan visar kopplingsinformationen, däribland användarnamn och tid.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. Unbind device.

    Koppla bort routern genom att logga in på webbadministrationspanelen, öppna **APPLICATION** -> **GoodCloud** och klicka på **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    Du kan även ta bort enheten från listan Bound Devices på GoodCloud-plattformen. Routerns webbadministrationspanel synkroniseras och visar aktuell kopplingsstatus.

    Kontakta [support@gl-inet.com](mailto:support@gl-inet.com) om problem uppstår.

## Manage Devices {#manage-devices}

### Systeminformation och åtgärder {#system-info-and-actions}

På [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kan du visa systeminformation, till exempel modell, version, MAC- och IP-adress, samt status för alla enheter som är kopplade till kontot.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Välj en enhet för att ändra inställningar, uppdatera firmware, fjärransluta, starta om eller återställa via det övre högra hörnet.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Klicka på kugghjulsikonen längst till höger i listrubriken för att anpassa kolumner och ordning.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Device details {#device-details}

Klicka på ett enhetsnamn under [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** för att öppna enhetssidan med grundinformation, statistik, nätverksinställningar och klientlista.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Basic info {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistics {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Network settings {#network-settings}

Sidan visar routerns nätverkskonfigurationer och Wi-Fi-inställningar.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Clients list {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Remote Access {#remote-access}

Öppna [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices**, klicka på enhetsnamnet och använd fjärråtgärderna uppe till höger.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

Klicka på **Remote GUI** för fjärråtkomst till routerns webbadministrationspanel.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Om alternativet är grått eller otillgängligt är funktionen troligen inaktiverad. Aktivera den först i routerns webbadministrationspanel.

Om alternativet kan klickas men inte svarar provar du webbläsarens inkognito- eller InPrivate-läge.

### Remote SSH {#remote-ssh}

Klicka på **Remote SSH** för fjärråtkomst till routerns terminal via SSH.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Om alternativet är grått eller otillgängligt är funktionen troligen inaktiverad. Aktivera den först i routerns webbadministrationspanel.

Om alternativet kan klickas men inte svarar provar du webbläsarens inkognito- eller InPrivate-läge.

## Modify Settings {#modify-settings}

Du kan konfigurera flera parametrar för en eller flera enheter.

Välj enheten under [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** och klicka på **Settings** -> **Modify Settings** uppe till höger.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Här kan du kontrollera och ändra routerns inställningar för trådlöst nätverk, Ethernet, säkerhet, portvidarebefordran, LAN och system.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## Email Alarm {#email-alarm}

Du kan konfigurera e-postvarningar när enhetens status ändras eller nya klienter ansluter.

Klicka på **Add Rule** uppe till höger under [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications**.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Välj enheten som ska övervakas och klicka på **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Välj utlösande händelse, till exempel online/offline-status, och klicka på **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Kontrollera regelinställningarna och klicka på **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

Listan Notifications visar skapade varningsregler. Enskilda användare kan skapa en regel. Kontakta oss för abonnemangsuppgradering om du behöver masshantering.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site {#site-to-site}

Please refer to [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud och VPN {#goodcloud-and-vpn}

Om **GoodCloud** och **VPN client** aktiveras samtidigt går anslutningen mellan routern och GoodCloud-servern som standard inte genom VPN. Det ger en stabilare anslutning.

Om GoodCloud-anslutningen ska gå genom VPN ändrar du inställningen i webbadministrationspanelen. Öppna VPN -> VPN Dashboard -> VPN Client -> Options och aktivera "Services from GL.iNet Use VPN".

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Observera att GoodCloud via VPN kan påverka molnanslutningens stabilitet, särskilt om:

* The VPN connection is unstable
* The VPN provider filters or blocks GoodCloud traffic
* The VPN adds significant latency to the connection

Vi rekommenderar standardinställningen där GoodCloud kringgår VPN för optimal prestanda och tillförlitlighet.

## View Logs {#view-logs}

Du kan visa GoodCloud-loggar som Activity Logs, Device Logs, Upgrade Logs, Alert Logs och Device Settings Logs.

Öppna [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** och välj loggar i listrutan.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Disable Cloud {#disable-cloud}

Om enheten inte längre ska vara ansluten till molnplattformen inaktiverar du molntjänsten i webbadministrationspanelen.

??? "For firmware v4.6 or earlier"

    Logga in på webbadministrationspanelen, öppna **APPLICATIONS** -> **GoodCloud**, inaktivera GoodCloud med reglaget och klicka på **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Once disabled, the interface will display as follows.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "For firmware v4.7 or later"

    Logga in på webbadministrationspanelen och klicka på molnikonen uppe till höger. Klicka på kugghjulet i popup-fönstret **Cloud Service** och välj **Disable**.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Once disabled, the interface will display as follows.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Delete Account {#delete-account}

Av säkerhetsskäl kan du radera ett konto som inte längre används.

Klicka på användarnamnet uppe till höger på [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, välj **Personal Center**, bläddra längst ned och klicka på **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Radering tar permanent bort alla relaterade tjänster, data och personuppgifter utan möjlighet till återställning.

    Om kontot tillhör en organisation måste du först lämna alla organisationer.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
