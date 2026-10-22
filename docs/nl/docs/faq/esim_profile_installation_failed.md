# Wat moet ik doen als de installatie van een eSIM-profiel mislukt? {#what-should-i-do-if-esim-profile-installation-fails}

Volg de onderstaande stappen als de installatie van een eSIM-profiel op je GL.iNet-router mislukt:

1. Make sure the router is connected to the Internet.

    Controleer of de router verbinding met internet heeft. Een instabiel netwerk kan het uploaden van het eSIM-profiel verstoren, waardoor de router het profiel niet kan ophalen en installeren.

    Verbind de router indien mogelijk met een andere netwerkbron, zoals de hotspot van je smartphone of een openbaar wifinetwerk, en upload het eSIM-profiel opnieuw.

2. Change DNS settings.

    Als internet goed werkt, meld je je aan bij het webbeheerpaneel en ga je naar **NETWORK** -> **DNS**.

    Stel DNS Mode in op **Manual DNS** en test met andere openbare DNS-servers, zoals Google DNS (`8.8.8.8`, `8.8.4.4`) of Cloudflare DNS (`1.1.1.1`, `1.0.0.1`).

    Klik op **Apply** om de wijzigingen op te slaan en upload het eSIM-profiel opnieuw.

    ![manual dns](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/manual_dns.jpg){class="glboxshadow"}

3. Disable AdGuard Home.

    Als AdGuard Home beschikbaar en ingeschakeld is, schakel je het uit en probeer je het eSIM-profiel opnieuw te installeren.

4. Check the eSIM profile availability.

    Controleer of dit eSIM-profiel of de QR-code al op een ander apparaat is geactiveerd of geïnstalleerd.

    De meeste eSIM-profielen kunnen slechts eenmaal worden geïnstalleerd en niet op meerdere apparaten worden geactiveerd. Vraag je eSIM-provider of het profiel nog beschikbaar is. Vraag bij een verlopen QR- of activeringscode een nieuwe aan en upload deze opnieuw naar de router.

5. Check the activation code.

    Een correct opgemaakte QR-code toont een activeringscode die begint met **LPA:**. Sommige niet-standaardcodes bevatten alleen een activeringscode zonder dit voorvoegsel. Voeg in dat geval handmatig `LPA:` aan het begin toe voordat je op Install klikt.

    ![activation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/activation_code.jpg){class="glboxshadow" width="600"}

6. Check if a confirmation code is required.

    Voor sommige eSIM-profielen, zoals Smarty eSIM, moet je tijdens de installatie een bevestigingscode invoeren. Controleer het eSIM-pakket of de installatiehandleiding en voer zo nodig de juiste code in.

    ![confirmation code](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/confirmation_code.jpg){class="glboxshadow" width="600"}

7. Als de bovenstaande stappen het probleem niet oplossen, exporteer je het eSIM-logboek via de pagina eSIM Management.

    ![export log](https://static.gl-inet.com/docs/router/en/4/faq/esim_profile_installation_failed/export_log.png){class="glboxshadow"}

    Stuur het logboek met de onderstaande informatie naar [support@gl-inet.com](mailto:support@gl-inet.com) voor verdere hulp.

    - Het probleem dat je hebt ondervonden
    - De oplossingsmethoden die je hebt geprobeerd, indien van toepassing
    - Your eSIM provider

---
