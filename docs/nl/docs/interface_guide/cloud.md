# GL.iNet GoodCloud {#glinet-goodcloud}

## Inleiding {#introduction}

GL.iNet [GoodCloud](https://www.goodcloud.xyz){target="_blank"} is een platform dat de implementatie en het beheer van verbonden apparaten op afstand vereenvoudigt. Het biedt eenvoudige externe toegang tot GL.iNet-routers en beheer ervan. Door netwerkapparaten centraal in de cloud te beheren, kun je efficiënt batchtaken uitvoeren, zoals netwerkconfiguraties implementeren en software upgraden. Je kunt ook op afstand het webbeheerpaneel of via SSH de terminal van de router openen, voor end-to-end apparaatbeheer over verschillende regio's.

Met GoodCloud kun je:

1. De realtime status van de router controleren
    - Online- en offlinestatus bewaken
    - Realtime RAM-gebruik en gemiddelde belasting bekijken
    - E-mailwaarschuwingen ontvangen bij wijzigingen in de online- of offlinestatus

2. Routers op afstand instellen
    - Routerinstellingen configureren, zoals SSID en wachtwoord
    - Externe SSH-toegang
    - Externe toegang tot de WebUI
    - Routertoegang met anderen delen

3. Verbonden clients op afstand bewaken
    - Apparaten bekijken die met je netwerk zijn verbonden
    - Realtime verkeer bewaken en clients blokkeren
    - E-mailwaarschuwingen ontvangen voor nieuwe verbindingen en blokkeergebeurtenissen

4. Batchbewerkingen uitvoeren
    - Batchherstart
    - Batchgewijze firmware-upgrade

5. Site-to-Site-connectiviteit instellen
    - Virtual Office: breid je kantoornetwerk uit naar andere vestigingen
    - Business Travel: krijg op afstand toegang tot kantoorsystemen, zoals OA, CRM en MySQL
    - Smart Home: krijg op afstand toegang tot thuisapparaten, zoals IP-camera's en NAS

Kies onze abonnementen met toegevoegde waarde als je meerdere apparaten wilt beheren en geavanceerde functies nodig hebt, zoals bulkbewerkingen, beheer van meerdere accounts en aangepaste oplossingen. Klik [hier](https://www.gl-inet.com/solutions/goodcloud/){target="_blank"} voor meer informatie of neem contact op via [support@gl-inet.com](mailto:support@gl-inet.com).

## Apparaten aan de cloud koppelen {#bind-devices-to-cloud}

Selecteer voor de stappen om een apparaat te koppelen het gedeelte dat bij de firmwareversie van je apparaat hoort.

### Voor firmware v4.10 en hoger {#for-firmware-v410-and-above}

1. Schakel GoodCloud in.

    Meld je aan bij het webbeheerpaneel van je router, ga naar **CLOUD SERVICE** -> **GoodCloud** en klik op **Get Started**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind1.png){class="glboxshadow"}

    De pagina **GL.iNet Account** wordt geopend. Klik op **Bind GL.iNet Account via URL**.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind2.png){class="glboxshadow"}

    Klik in het pop-upvenster op **Continue**. Je wordt naar de GoodCloud-website doorgestuurd om de koppeling te voltooien.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind3.png){class="glboxshadow"}

2. Meld je aan om je apparaat te koppelen.

    Meld je aan bij je GL.iNet-account. Maak een account als je er nog geen hebt en meld je vervolgens aan.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind4.png){class="glboxshadow"}

    Controleer na het aanmelden je account- en apparaatgegevens, waaronder Device ID, model en MAC-adres. Stel een apparaatnaam in en klik op **Bind**. De router wordt aan je account gekoppeld.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind5.png){class="glboxshadow" width="423"}

    Als je de verificatiemail niet ontvangt, controleer je de map met ongewenste e-mail of wacht je enkele minuten en probeer je het opnieuw. Stuur voor verdere hulp een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com).

3. Koppelingsgegevens.

    Ga na een geslaagde koppeling terug naar het webbeheerpaneel en ga naar **CLOUD SERVICES** -> **GoodCloud**. De pagina toont een link naar het GoodCloud-platform, identificatiegegevens van het apparaat en recente cloudlogboeken.

    ![bind device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_bind6.png){class="glboxshadow"}

4. Externe toegang.

    In firmware v4.10 wordt externe toegang tot het webbeheerpaneel en de terminal van de router standaard ingeschakeld nadat de router aan GoodCloud is gekoppeld.

5. Apparaat ontkoppelen.

    Meld je aan bij het webbeheerpaneel en ga naar **CLOUD SERVICES** -> **GL.iNet Account** om de router te ontkoppelen. Klik op **Unbind**.

    ![unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/4.10_unbind.png){class="glboxshadow"}

    Je kunt het apparaat ook verwijderen uit de lijst Bound Devices op het GoodCloud-platform. Het webbeheerpaneel van de router synchroniseert en toont de nieuwste koppelingsstatus.

    Stuur bij problemen een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com) voor hulp.

### Voor firmware v4.7 tot v4.9 {#for-firmware-v47-to-v49}

1. Schakel GoodCloud in.

    Meld je aan bij het webbeheerpaneel van je router en ga naar **CLOUD SERVICE** -> **GoodCloud**.

    Klik op **Get Started**. Rechtsboven verschijnt een pop-upvenster van Cloud Service. Klik op **Enable**.

    ![enable cloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_cloud_service.png){class="glboxshadow"}

2. Meld je aan om je apparaat te koppelen.

    ![log in goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_login.png){class="glboxshadow"}

    Maak een account als je er nog geen hebt en meld je aan. Na de registratie wordt de router automatisch aan je account gekoppeld.

    ![sign up goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/sign_up.png){class="glboxshadow"}

    Als je de verificatiemail niet ontvangt, controleer je de map met ongewenste e-mail of wacht je enkele minuten en probeer je het opnieuw. Stuur voor verdere hulp een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com).

3. Koppelingsgegevens.

    Ga na een geslaagde koppeling terug naar het webbeheerpaneel en klik rechtsboven op het Cloud-pictogram. De koppelingsgegevens worden weergegeven, waaronder gebruikersnaam, koppeltijd, Device ID, Device MAC en Device S/N.

    ![binding details](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/binding_details.png){class="glboxshadow"}

4. Externe toegang inschakelen.

    Ga in het webbeheerpaneel naar **CLOUD SERVICES** -> **GoodCloud** om externe toegang voor je router in te schakelen.

    ![enable remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_remote_access.png){class="glboxshadow"}

    - **Remote SSH**: om vanaf het GoodCloud-platform via SSH op afstand de terminal van de router te openen.

    - **Remote Web Access**: om vanaf het GoodCloud-platform via HTTP/HTTPS op afstand het webbeheerpaneel van de router te openen.

    - **View Logs**: toont logboeken van API-aanroepen door GoodCloud.

5. Apparaat ontkoppelen.

    Meld je aan bij het webbeheerpaneel om de router te ontkoppelen. Klik rechtsboven op het cloudpictogram en vervolgens op **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_2.png){class="glboxshadow"}

    Je kunt het apparaat ook verwijderen uit de lijst Bound Devices op het GoodCloud-platform. Het webbeheerpaneel van de router synchroniseert en toont de nieuwste koppelingsstatus.

    Stuur bij problemen een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com) voor hulp.

### Voor firmware v4.6 of ouder {#for-firmware-v46-or-earlier}

1. Schakel GoodCloud in.

    Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **GoodCloud**. Zet de schakelaar om om GoodCloud in te schakelen.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_1.png){class="glboxshadow"}

    Schakel zo nodig **Remote SSH** en **Remote Web Access** in, selecteer de dichtstbijzijnde server, lees en accepteer **Terms of Service & Privacy Policy** en klik op **Apply**.

    ![enable goodcloud](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/enable_goodcloud_2.png){class="glboxshadow"}

    - **Remote SSH**: om vanaf het GoodCloud-platform via SSH op afstand de terminal van de router te openen.

    - **Remote Web Access**: om vanaf het GoodCloud-platform via HTTP/HTTPS op afstand het webbeheerpaneel van de router te openen.

    - **Data Server**: kies de server die het dichtst bij je apparaat ligt. De opties zijn Asia Pacific (Japan), America (Oregon) en Europe (Ireland).

2. Maak een account.

    Ga naar [GoodCloud](https://www.goodcloud.xyz){target="_blank"}, maak een account en meld je aan.

    Als je de verificatiemail niet ontvangt, controleer je de map met ongewenste e-mail of wacht je enkele minuten en probeer je het opnieuw. Stuur voor verdere hulp een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com).

3. Voeg apparaten toe.

    Ga op het cloudplatform naar **Devices** -> **Bound Devices** -> **Add Devices**.

    ![add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_1.png){class="glboxshadow"}

    Er zijn drie methoden om een apparaat aan je GoodCloud-account te koppelen: Auto Discover, Manually Add en Bulk Import.

    ??? "Auto Discover"

        Probeer **Auto discover** als je router en het apparaat waarmee je de GoodCloud-website opent zich in hetzelfde netwerk bevinden.

        Selecteer je apparaat in de vervolgkeuzelijst en voer **DDNS / Device ID** in. Dit staat op de onderkant van de router of op de GoodCloud-pagina in het webbeheerpaneel.

        ![add device, auto discover](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_auto.jpg){class="glboxshadow"}

        Raadpleeg [deze link](../faq/where_to_find_the_device_id_mac_sn.md) om de Device ID te vinden.

    ??? "Manually Add"

        Als je apparaat niet in de lijst staat, klik je op **Manually add** en voer je de gegevens van de router in. Alle gevraagde informatie staat op de onderkant van de router of op de GoodCloud-pagina in het webbeheerpaneel.

        ![manually add device](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_manual.jpg){class="glboxshadow"}

    ??? "Bulk Import"

        **Bulk Import** is bedoeld voor gebruikers die veel apparaten beheren. Je kunt meerdere apparaten via een Microsoft Excel-bestand importeren.

        ![bulk import](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/add_devices_bulk.jpg){class="glboxshadow"}

4. Binding details.

    Ga na een geslaagde koppeling terug naar het webbeheerpaneel en ga naar **APPLICATIONS** -> **GoodCloud**. De pagina toont de koppelingsgegevens, waaronder gebruikersnaam en koppeltijd.

    ![goodcloud bound](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/bind_info.png){class="glboxshadow"}

5. Apparaat ontkoppelen.

    Meld je aan bij het webbeheerpaneel om de router te ontkoppelen, ga naar **APPLICATION** -> **GoodCloud** en klik op **Unbind**.

    ![goodcloud unbind](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/unbind_router_1.png){class="glboxshadow"}

    Je kunt het apparaat ook verwijderen uit de lijst Bound Devices op het GoodCloud-platform. Het webbeheerpaneel van de router synchroniseert en toont de nieuwste koppelingsstatus.

    Stuur bij problemen een e-mail naar [support@gl-inet.com](mailto:support@gl-inet.com) voor hulp.

## Apparaten beheren {#manage-devices}

### Systeeminformatie en handelingen {#system-info-and-actions}

Onder [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** kun je de systeeminformatie, zoals model, versie, MAC- en IP-adres, en de online- of offlinestatus van alle gekoppelde apparaten bekijken.

![devices info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/devices_info.png){class="glboxshadow"}

Selecteer een apparaat. Rechtsboven kun je instellingen wijzigen, firmware bijwerken, het apparaat op afstand openen, opnieuw opstarten of resetten.

![device actions1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions1.png){class="glboxshadow"}

![device actions2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_actions2.jpg){class="glboxshadow"}

Klik helemaal rechts in de lijstkop op het tandwielpictogram om de weergegeven kolommen en hun volgorde aan te passen.

![column display](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/column_display.png){class="glboxshadow"}

### Apparaatgegevens {#device-details}

Klik onder [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** op een apparaatnaam om de detailpagina te openen. Deze toont basisinformatie, statistieken, netwerkinstellingen, de clientlijst en meer.

![Device detail info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_details.png){class="glboxshadow"}

#### Basisinformatie {#basic-info}

![basic info](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/basic_info.png){class="glboxshadow"}

#### Statistieken {#statistics}

![statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/statistics.png){class="glboxshadow"}

#### Netwerkinstellingen {#network-settings}

Deze pagina toont de netwerkconfiguraties en Wi-Fi-instellingen van je router.

![status overview](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/device_overview.png){class="glboxshadow"}

#### Clientlijst {#clients-list}

![clients list](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/clients_list.png){class="glboxshadow"}

## Externe toegang {#remote-access}

Klik onder [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** op de naam van het apparaat dat je wilt openen. Op de detailpagina staan rechtsboven de externe handelingen.

![remote access](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_access.png){class="glboxshadow"}

### Remote GUI {#remote-gui}

Klik op **Remote GUI** om op afstand het webbeheerpaneel van je router te openen.

![remote access web admin panel](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_web_admin_panel.png){class="glboxshadow"}

Als deze optie grijs of niet beschikbaar is, is de functie waarschijnlijk uitgeschakeld. Schakel deze eerst in het webbeheerpaneel in voordat je deze via GoodCloud gebruikt.

Als je op deze optie kunt klikken maar deze niet reageert, gebruik je de incognito- of InPrivate-modus van je browser.

### Remote SSH {#remote-ssh}

Klik op **Remote SSH** om via SSH op afstand de terminal van je router te openen.

![remote access device terminal](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/remote_terminal.png){class="glboxshadow"}

Als deze optie grijs of niet beschikbaar is, is de functie waarschijnlijk uitgeschakeld. Schakel deze eerst in het webbeheerpaneel in voordat je deze via GoodCloud gebruikt.

Als je op deze optie kunt klikken maar deze niet reageert, gebruik je de incognito- of InPrivate-modus van je browser.

## Instellingen wijzigen {#modify-settings}

Je kunt meerdere parameters voor één of meerdere apparaten configureren.

Selecteer onder [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Bound Devices** het apparaat dat je wilt configureren en klik rechtsboven op **Settings** -> **Modify Settings**.

![device settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_1.png){class="glboxshadow"}

Hier kun je de netwerkinstellingen van de router bekijken en wijzigen, waaronder Wireless, Ethernet, beveiliging, port forwarding, LAN en systeeminstellingen.

![device settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/modify_settings_2.png){class="glboxshadow"}

## E-mailwaarschuwingen {#email-alarm}

Je kunt e-mailwaarschuwingen instellen voor wijzigingen in de online- of offlinestatus en nieuwe clientverbindingen.

Klik onder [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Notifications** rechtsboven op **Add Rule**.

![notifications 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications1.png){class="glboxshadow"}

Selecteer het apparaat dat je wilt bewaken en klik op **Next**.

![notifications 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications2.png){class="glboxshadow"}

Selecteer de activeringsgebeurtenis, zoals de online- of offlinestatus, en klik op **Next**.

![notifications 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications3.png){class="glboxshadow"}

![notifications 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications4.png){class="glboxshadow"}

Controleer de regelinstellingen en klik op **Apply**.

![notifications 5](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications5.png){class="glboxshadow"}

In de lijst Notifications kun je gemaakte waarschuwingsregels bekijken. Individuele gebruikers kunnen één waarschuwingsregel maken. Neem contact met ons op om je abonnement te upgraden als je apparaten in bulk wilt beheren.

![notifications 6](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/notifications6.png){class="glboxshadow"}

## Site to Site {#site-to-site}

Raadpleeg [GoodCloud Site to Site](../tutorials/goodcloud_site_to_site.md).

## GoodCloud en VPN {#goodcloud-and-vpn}

Als je **GoodCloud** en **VPN client** tegelijk inschakelt, loopt de verbinding tussen de router en GoodCloud-server standaard niet via de VPN. Dit zorgt voor een stabielere verbinding met GoodCloud-diensten.

Als je de GoodCloud-verbinding via de VPN wilt laten lopen, wijzig je dit in het webbeheerpaneel. Ga naar VPN -> VPN Dashboard -> VPN Client -> Options en schakel "Services from GL.iNet Use VPN" in.

![Services from GL.iNet use VPN](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/goodcloud_vpn.png){class="glboxshadow"}

Het routeren van GoodCloud via VPN kan de stabiliteit van de cloudverbinding beïnvloeden, vooral wanneer:

* De VPN-verbinding instabiel is
* De VPN-provider GoodCloud-verkeer filtert of blokkeert
* De VPN aanzienlijke latentie aan de verbinding toevoegt

Voor optimale prestaties en betrouwbaarheid raden we doorgaans de standaardinstelling aan waarbij GoodCloud de VPN omzeilt.

## Logboeken bekijken {#view-logs}

Je kunt naar behoefte GoodCloud-logboeken bekijken, waaronder Activity Logs, Device Logs, Upgrade Logs, Alert Logs en Device Settings Logs.

Ga naar [GoodCloud](https://www.goodcloud.xyz){target="_blank"} -> **Logs** en selecteer in de vervolgkeuzelijst de gewenste logboeken.

![View Logs](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/view_logs.png){class="glboxshadow"}

## Cloud uitschakelen {#disable-cloud}

Als je het apparaat niet meer met het cloudplatform wilt verbinden, kun je de clouddienst in het webbeheerpaneel uitschakelen.

??? "Voor firmware v4.6 of ouder"

    Meld je aan bij het webbeheerpaneel, ga naar **APPLICATIONS** -> **GoodCloud**, zet de schakelaar om om GoodCloud uit te schakelen en klik op **Apply**.

    ![disable cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_1.jpg){class="glboxshadow"}

    Na uitschakeling wordt de interface als volgt weergegeven.

    ![disabled cloud 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud.png){class="glboxshadow"}

??? "Voor firmware v4.7 of hoger"

    Meld je aan bij het webbeheerpaneel en klik rechtsboven op het cloudpictogram. Klik in het pop-upvenster **Cloud Service** op het tandwielpictogram en selecteer **Disable**.

    ![disable cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disable_cloud_2.png){class="glboxshadow"}

    Na uitschakeling wordt de interface als volgt weergegeven.

    ![disabled cloud 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/disabled_cloud_2.png){class="glboxshadow"}

## Account verwijderen {#delete-account}

Om veiligheidsredenen kun je een account verwijderen als je het niet meer gebruikt.

Klik op het [GoodCloud](https://www.goodcloud.xyz){target="_blank"}-platform rechtsboven op de gebruikersnaam en selecteer **Personal Center**. Scrol naar de onderkant en klik op **Delete Account**.

![delete account](https://static.gl-inet.com/docs/router/en/4/interface_guide/cloud/delete_account.png){class="glboxshadow"}

!!! Note

    Verwijdering wist alle bijbehorende diensten, gegevens en persoonlijke informatie permanent. Herstel is niet mogelijk.

    Als je account bij een organisatie hoort, moet je alle organisaties verlaten voordat je het account verwijdert.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
