# eSIM Management {#esim-management}

**Note**:

1. Deze handleiding geldt voor modellen die de fysieke eSIM-kaart van GL.iNet ondersteunen.

2. GL-E5800 (Mudi 7) heeft een ingebouwde eSIM en ondersteunt de fysieke eSIM-kaart van GL.iNet niet. Een fysieke eSIM-kaart wordt op Mudi 7 herkend als een gewone simkaart zonder eSIM-functionaliteit.

## Ondersteunde modellen {#supported-models}

!!! note "Supported Models"

    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750V2 (Mudi V2)
    - ※ GL-E750 (Mudi)
    - ※ GL-XE300 (Puli)
    - ※ GL-X750 (Spitz)
    - ※ GL-X300B (Collie)

    **Note**:

    1. **Voor modellen met ※** hangt ondersteuning voor fysieke eSIM-kaarten af van de gebruikte module.

        - Installeer bij een **EC25-AF**-, **EC25-E**- of **EG25-G**-module eerst firmware met eSIM-ondersteuning. [Neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"} voor verdere instructies.

        - Raadpleeg bij een **EP06-E**-module [deze link](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} om eerst de firmware van de module bij te werken en installeer daarna firmware met eSIM-ondersteuning.

        - Een **EP06-A**-module ondersteunt geen fysieke eSIM-kaart omdat de Qualcomm-software de vereiste AT-opdrachten niet ondersteunt.

    2. **GL-E750V2 <u>vSIM</u>** ondersteunt geen fysieke eSIM-kaart.

    3. **GL-E5800 (Mudi 7)** heeft een ingebouwde eSIM. De fysieke eSIM-kaart wordt daarom op Mudi 7 herkend als een gewone simkaart zonder eSIM-functionaliteit.

## eSIM Management {#esim-management_1}

Ga links in het webbeheerpaneel naar **APPLICATIONS** -> **eSIM Management**.

Op deze pagina kun je de status van de fysieke eSIM-kaart controleren en eSIM-profielen beheren. De pagina bestaat uit **Current eSIM Status** en **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Huidige eSIM-status {#current-esim-status}

Dit gedeelte toont basisinformatie en details over het actieve eSIM-profiel.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** de wereldwijd unieke id van de eUICC (eSIM-chip), gebruikt voor identificatie en profielbeheer.
- **ICCID:** de Integrated Circuit Card Identifier van het actieve eSIM-profiel.
- **IMSI:** de International Mobile Subscriber Identity van het actieve eSIM-profiel.
- **eSIM OS Version:** de besturingssysteemversie van de eUICC, die de compatibiliteit en ondersteunde functies bepaalt.
- **eSIM Storage (remain/total):** de beschikbare en totale opslagcapaciteit op de eUICC voor eSIM-profielen.
- **eSIM Profile Number:** het aantal eSIM-profielen dat op de eUICC is opgeslagen. Profielen van verschillende providers verschillen in grootte, waardoor ook het aantal profielen dat kan worden opgeslagen verschilt.

## Lijst met eSIM-profielen {#esim-profile-list}

Dit gedeelte toont informatie over het seed-profiel en normale eSIM-profielen.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: het seed-profiel bevat vooraf 1GB gratis data voor de VS en Europa en 100MB wereldwijde data, geldig tot 1 jaar na activering. Hiermee kun je wereldwijd andere profielen downloaden. Je kunt het resterende en totale datategoed en de vervaldatum bewaken.

- **Normal Profile**: een gekocht eSIM-profiel dat je via een QR-code of activeringscode uploadt, wordt hier weergegeven.

### Seed-profiel aanvullen {#top-up-seed-profile}

GL.iNet levert een vooraf geïnstalleerd seed-profiel met 100MB wereldwijde data en 1GB data voor Europa en de VS voor de eerste installatie en activering van eSIM-profielen. Hiermee kun je op een bestemming zonder internettoegang nieuwe eSIM-profielen downloaden.

Als de vooraf geïnstalleerde gratis data op of verlopen is, kun je het seed-profiel aanvullen om de dienst te blijven gebruiken.

Klik in het gedeelte Seed Profile rechts op **Top-up**.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Scan in het pop-upvenster de QR-code en volg de instructies om het aanvullen te voltooien.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### eSIM-profiel kopen {#purchase-esim-profile}

Je kunt eSIM-profielen kopen bij aanbevolen winkels, geteste winkels of andere eSIM-providers.

??? note "Optie 1: kopen bij aanbevolen winkels"

    Er zijn twee aanbevolen winkels: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} en [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Klik in het gedeelte Normal Profile rechts op **eSIM Profile Recommended Store**.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Scan de QR-code of klik op de links om eSIM-profielen te kopen.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Opmerking**: alle eSIM-pakketten van deze twee winkels zijn volledig compatibel met GL.iNet-routers. Neem bij vragen contact op met ons ondersteuningsteam via [support@gl-inet.com](mailto:support@gl-inet.com).

??? note "Optie 2: kopen bij geteste winkels"

    Raadpleeg [deze link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} voor een lijst met door GL.iNet geteste winkels.

    **Opmerking**: we kunnen niet garanderen dat alle profielen of pakketten van deze winkels volledig compatibel zijn met GL.iNet-routers. Omdat GL.iNet geen samenwerking met deze winkels heeft, kunnen we geen ondersteuning na aankoop of hulp bij terugbetalingen bieden.

??? note "Optie 3: kopen bij andere eSIM-providers"

    Je kunt ook eSIM-profielen bij een andere provider kopen.

    We kunnen niet garanderen dat eSIM-profielen van andere providers volledig compatibel zijn met GL.iNet-routers. Koop deze naar eigen inzicht. GL.iNet is niet verantwoordelijk voor compatibiliteitsproblemen.

    Neem voor ondersteuning na aankoop of terugbetalingen contact op met de betreffende eSIM-provider.

### eSIM-profiel uploaden {#upload-esim-profile}

Na aankoop van een eSIM-profiel ontvang je gewoonlijk een QR-code of activeringscode. Sla de QR-code lokaal op en volg de onderstaande stappen om het profiel te uploaden.

1. Klik onderaan het gedeelte Normal Profile op **Add eSIM Profile**.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Upload de eSIM-QR-code of voer de activeringscode in en klik op **Install**. Het eSIM-profiel wordt op de router gedownload en geïnstalleerd.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Note:**

    1. De meeste eSIM-profielen kunnen slechts eenmaal worden gedownload en geïnstalleerd.

    2. Een correct opgemaakte QR-code toont een activeringscode die met **LPA:** begint. Sommige niet-standaard QR-codes bevatten alleen een onbewerkte activeringscode zonder LPA-voorvoegsel. Voeg in dat geval handmatig `LPA:` aan het begin toe voordat je op Install klikt.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Als je nog geen eSIM-profiel hebt gekocht, kun je er een kopen via eSIM Profile Recommended Store. Klik [hier](#purchase-esim-profile) voor meer informatie.

3. Schakel je eSIM-profiel in.

    Na een geslaagde upload verschijnt je nieuwe eSIM-profiel in de lijst **Normal Profile**. Klik op **Enable** om het te activeren.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Maak verbinding met internet.

    Ga na het inschakelen van je eSIM-profiel naar **INTERNET** -> **Cellular**. Klik op **Connect** om via het profiel verbinding met internet te maken.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Opmerking**: sommige eSIM-profielen vereisen aanvullende configuratie, zoals APN-, PIN- of TTL-instellingen. Klik zo nodig op **Manual Setup** of **SIM Card Settings** om deze parameters aan te passen. Soms moet je het apparaat opnieuw opstarten om verbinding met internet te maken.

5. Nadat de router via het eSIM-profiel verbinding heeft gemaakt, wordt de pagina als volgt weergegeven:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Logboek voor ondersteuning exporteren {#export-log-for-support}

Klik op **Export Log for Support** om alle eSIM-logboeken te bekijken. Exporteer bij problemen de eSIM-logboeken en stuur ze per e-mail naar ons ondersteuningsteam via [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Gerelateerde artikelen:

- [Een fysieke eSIM-kaart gebruiken met GL.iNet-routers](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Een fysieke eSIM-kaart gebruiken met Android-apparaten](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
