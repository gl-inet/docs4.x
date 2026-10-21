# De fysieke eSIM-kaart gebruiken met GL.iNet-routers {#how-to-use-the-esim-physical-card-with-glinet-routers}

In deze handleiding lees je hoe je de fysieke eSIM-kaart uit de GL.iNet-webwinkel gebruikt met GL.iNet-routers.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Functies {#features}

De fysieke eSIM-kaart heeft de volgende belangrijke functies:

- Ondersteunt 4G- en 5G-netwerken voor betrouwbare en snelle verbindingen.
- Beheer je eSIM-profielen eenvoudig door ze toe te voegen, te verwijderen of in te schakelen.
- Selecteer en koop op elk moment de gewenste databundels bij de meeste eSIM-winkels wereldwijd.
- Werkt met eSIM-profielen van de meeste wereldwijde eSIM-winkels.
- Koop eSIM-profielen online zonder persoonlijke gegevens te verstrekken, waardoor het risico op privacyschendingen afneemt.
- Wordt geleverd met een startprofiel met 1GB gratis data voor de Verenigde Staten en Europa, plus 100MB Global Data. Dit is 1 jaar geldig vanaf de activeringsdatum.
- Compatibel met geselecteerde GL.iNet-apparaten.

## Ondersteunde modellen {#supported-models}

!!! note "Ondersteunde modellen"

    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750V2 (Mudi V2)
    - ※ GL-E750 (Mudi)
    - ※ GL-XE300 (Puli)
    - ※ GL-X750 (Spitz)
    - ※ GL-X300B (Collie)

    **Opmerking**:

    1. **Voor modellen gemarkeerd met ※** hangt ondersteuning voor fysieke eSIM-kaarten af van de gebruikte module.

        - Als je een **EC25-AF**-, **EC25-E**- of **EG25-G**-module gebruikt, installeer je de firmware met eSIM-ondersteuning voordat je deze met de fysieke eSIM-kaart gebruikt. [Neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"} voor verdere instructies.

        - Als je een **EP06-E**-module gebruikt, volg je eerst [deze handleiding](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} om de firmware van de module te upgraden. Installeer daarna de firmware met eSIM-ondersteuning.

        - **EP06-A**-modules ondersteunen de fysieke eSIM-kaart niet, omdat de Qualcomm-software de vereiste AT-opdrachten niet ondersteunt.

    2. **GL-E750V2 <u>vSIM</u>** ondersteunt de fysieke eSIM-kaart niet.

    3. **GL-E5800 (Mudi 7)** heeft een ingebouwde eSIM. De fysieke eSIM-kaart wordt op Mudi 7 daarom als een gewone simkaart zonder eSIM-functionaliteit herkend.

## De fysieke eSIM-kaart instellen {#set-up-esim-physical-card}

Bekijk deze configuratievideo of volg de onderstaande stappen om de fysieke eSIM-kaart bij het eerste gebruik op je GL.iNet-router in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Stap 1:** plaats de fysieke eSIM-kaart in je router. Raadpleeg de onderstaande afbeeldingen voor meer informatie.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Stap 2:** open een browser en voer `192.168.8.1` in de adresbalk in om je aan te melden bij het GL.iNet Admin Panel.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Stap 3:** verbind je apparaat met internet.

Ga na het aanmelden naar **INTERNET** -> **Cellular**.

Zorg bij routers met twee simkaarten dat de sleuf met de fysieke eSIM-kaart is ingesteld als **Active SIM Card**. Klik anders op **SIM Card Switch** en selecteer de simkaartsleuf waarin de fysieke eSIM-kaart is geplaatst.

Klik vervolgens op **Connect**, of op **Auto Setup** in een oudere firmwareversie, om via het cellulaire netwerk verbinding met internet te maken.

*Deze fysieke eSIM-kaart wordt geleverd met een startprofiel met 1GB gratis data voor de Verenigde Staten en Europa, plus 100MB Global Data. Dit is 1 jaar geldig vanaf de activeringsdatum. Deze data is uitsluitend bedoeld voor het kopen en downloaden van eSIM-profielen en niet voor algemene internettoegang.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

Na een geslaagde verbinding ziet het scherm er als volgt uit.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Je eSIM-profiel beheren {#manage-your-esim-profile}

**Stap 1:** zorg dat de nieuwste firmware op je GL.iNet-apparaat is geïnstalleerd.

Zorg dat Version 4.0 of nieuwer is en dat het Firmware Type-nummer 0319 of hoger is.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Als je firmware **niet actueel** is, kun je deze automatisch online of handmatig upgraden.

<u>Optie 1</u>: online firmware-upgrade

1. Zorg dat je apparaat met internet is verbonden.

2. Ga in het webbeheerpaneel naar **SYSTEM** -> **Upgrade** -> **Online Upgrade** en klik op **Install** om automatisch naar de nieuwste firmware bij te werken.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Optie 2</u>: handmatige firmware-update

1. Download [hier](https://dl.gl-inet.com/){target="_blank"} firmware met eSIM-functionaliteit voor het betreffende model.

2. Ga in het webbeheerpaneel naar **SYSTEM** -> **Upgrade** -> **Local Upgrade**. Selecteer het firmwarebestand of sleep het naar het aangegeven gebied om naar de nieuwste versie te upgraden.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Sommige modellen, zoals Mudi (GL-E750), Puli (GL-XE300) en Spitz (GL-X750), ondersteunen eSIM niet als ze een Quectel EP06-A-module hebben, omdat de Qualcomm-software bepaalde AT-opdrachten niet ondersteunt.

    2. Als een EP06-E-module is geïnstalleerd, volg je [deze handleiding](https://forum.gl-inet.com/t/48907){target="_blank"} om de module bij te werken naar de nieuwste software met eSIM-functionaliteit.

**Stap 2:** ga naar eSIM Management.

Wacht na het bijwerken van de firmware tot je apparaat opnieuw is opgestart en meld je vervolgens aan bij het GL.iNet Admin Panel.

Ga naar **APPLICATIONS** -> **eSIM Management**. Hier kun je de eSIM-status bekijken en eSIM-profielen beheren.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Er kan slechts één eSIM-profiel tegelijk actief zijn. Een groene stip geeft aan dat het geselecteerde eSIM-profiel actief is.

---

Gerelateerd artikel:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Heb je nog vragen? Bezoek ons [communityforum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
