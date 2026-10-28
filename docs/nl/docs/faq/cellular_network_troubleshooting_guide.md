# Cellular Network Troubleshooting Guide {#cellular-network-troubleshooting-guide}

Controleer de volgende punten als je geen mobiele verbinding kunt maken.

??? "Check device hardware"

    **1.1** Gebruik een standaardvoedingsadapter. Andere adapters leveren mogelijk onvoldoende vermogen.

    **1.2** Controleer of **Modem name**, **IMEI** en **SIM ICCID** in het webbeheerpaneel worden weergegeven.

    ![modem name](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/no_sim.png){class="glboxshadow"}

    Klik in firmware v4.8 en hoger op **View More Information** om SIM ICCID te vinden.

    Start de router opnieuw op als de gegevens ontbreken. Neem via [support@gl-inet.com](mailto:support@gl-inet.com) contact met ons op als Modem name en IMEI nog steeds niet worden herkend.

    **1.3** Klik op **View More**, controleer **Cells Info** en bevestig dat het signaal stabiel is. Controleer bij een zeer zwak signaal de antennes of verplaats de router naar een plaats met beter bereik.

    ![cells info](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/cells_info.png){class="glboxshadow"}

    **1.4** Klik op **View More** en controleer of de ondersteunde frequentieband geschikt is voor je regio.

    ![frequency band](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/frequency_band.png){class="glboxshadow"}

??? "Check software settings"

    **2.1** Meld je aan bij het webbeheerpaneel en controleer of het programma voor de mobiele verbinding is gestart. Je kunt ook op **Abort** en daarna op **Connect** klikken.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/2.png){class="glboxshadow gl-90-desktop"}

    **2.2** Sommige providers vereisen het **3G protocol**. Schakel over naar 3G en test opnieuw.

    Ga in firmware v4.7 en ouder naar **Manual Setup** -> **Protocol**, selecteer **3G** en klik op **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/3.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/4.png){class="glboxshadow gl-90-desktop"}

    Ga in firmware v4.8 en hoger naar **SIM Card Settings** -> **Protocol**, selecteer **3G** en klik op **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_protocol.png){class="glboxshadow gl-90-desktop"}

    Het apparaat maakt automatisch opnieuw verbinding. Wacht enkele minuten en controleer of de verbinding tot stand komt.

    **2.3** Sommige simkaarten vereisen een specifieke APN. Neem bij een mislukte registratie contact op met je provider over beperkingen. Configureer zo nodig de juiste APN en klik op **Apply**.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/sim_settings_apn.png){class="glboxshadow gl-90-desktop"}

    **2.4** Schakel **Band Masking** in en test opnieuw. Raadpleeg voor firmware v4.7 en ouder [deze pagina](../interface_guide/internet_cellular_v4.7.md#band-masking) en voor v4.8 en hoger [deze pagina](../interface_guide/internet_cellular.md#band-masking).

    **2.5** Vergrendel of ontgrendel een zendmast en test opnieuw. Deze functie is beschikbaar op GL-E5800 (Mudi 7), GL-X3000 (Spitz AX), GL-XE3000 (Puli AX) en GL-X2000 (Spitz Plus). GL-X2000 (Spitz Plus) ondersteunt deze functie vanaf firmware v4.7. Raadpleeg [deze instructies](../interface_guide/internet_cellular.md#lock-tower).

    Vergrendeling op een specifieke zendmast kan de router een stabiele mobiele verbinding van goede kwaliteit bieden.

    Na vergrendeling blijft de router ook op een nieuwe locatie na een herstart met deze mast proberen te verbinden. Hierdoor kan automatische mobiele verbinding mislukken. Ontgrendel de mast via het webbeheerpaneel of vergrendel de router handmatig op een nieuwe mast.

    **Opmerking:**
    1. De vergrendelde mast moet frequentiebanden gebruiken die door je provider en apparaat worden ondersteund. Anders kan de verbinding mislukken.
    2. International Data Roaming is standaard ingeschakeld op de mobiele module. Als je deze optie uitschakelt, kan de simkaart internettoegang verliezen. Laat de functie ingeschakeld.

??? "Check SIM compatibility"

    **3.1** Controleer de compatibiliteit van de simkaart. De Noord-Amerikaanse modellen van GL.iNet-cellulaire routers zijn IoT-gecertificeerd. Dit betekent echter niet dat IoT-simkaarten verplicht zijn: standaard simkaarten voor consumenten kunnen ook compatibel zijn. Neem contact op met je provider als je niet zeker weet welk type simkaart je moet gebruiken.

    Veelvoorkomende typen zijn data-only, data-only + voice, IoT en hotspot. We raden IoT- of hotspotsimkaarten aan. Voor data-only en data-only + voice wordt werking niet gegarandeerd.

    **3.2** Sommige simkaarten moeten eerst worden geactiveerd. Controleer internettoegang in een telefoon en plaats de kaart daarna in de router.

    **3.3** Sommige aangepaste simkaarten werken alleen in telefoons of specifieke apparaten. Controleer of de kaart aan een bepaald apparaat is gekoppeld.

    **3.4** In sommige Amerikaanse staten of steden, bijvoorbeeld bij AT&T in Seattle, moet je mogelijk de IMEI bij de provider registreren. Neem bij twijfel contact op met je provider.

    **3.5** Als het webbeheerpaneel "SIM card not registered" toont, probeer je eerst de bovenstaande stappen.

    Schakel de router uit, plaats de simkaart en start de router opnieuw. Sommige modellen ondersteunen geen hot-swapping en herkennen een kaart mogelijk niet wanneer deze ingeschakeld wordt geplaatst.

    Controleer of alle antennes correct zijn geïnstalleerd en test buiten op een plaats met een sterk mobiel signaal. Een zwak signaal kan registratie verhinderen.

    Als het probleem aanhoudt, is de simkaart mogelijk niet compatibel met de router. Neem contact op met je provider.

    Als je provider bevestigt dat het probleem niet aan de simkaart ligt, neem je contact op via [support@gl-inet.com](mailto:support@gl-inet.com).

    **3.6** Als de simkaart zich registreert en een IP-adres krijgt maar geen internettoegang heeft, terwijl upload wel en download niet werkt, heeft de provider waarschijnlijk een beperking ingesteld. Vraag de provider deze te verwijderen of stel TTL in op 65 en test opnieuw.

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/5.png){class="glboxshadow gl-90-desktop"}

    ![](https://static.gl-inet.com/docs/router/en/4/faq/cellular_troubleshoot/6.png){class="glboxshadow gl-90-desktop"}

    Vermeld bij contact met de provider Modem name, IMEI, SIM ICCID en het routermodel.

Als geen van de bovenstaande stappen helpt, neem je contact op via [support@gl-inet.com](mailto:support@gl-inet.com).
