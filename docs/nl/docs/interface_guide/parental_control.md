# Parental Control {#parental-control}

**Opmerking**: deze handleiding geldt voor firmware v4.8 en ouder. Klik voor nieuwere versies [hier](parental_control_v4.9.md).

---

Ga links in het webbeheerpaneel naar **APPLICATIONS** -> **Parental Control**.

Ouderlijk toezicht beschermt kinderen online door ongeschikte websites te blokkeren en apparaatgebruik te beperken. Het voorkomt toegang tot schadelijke inhoud, beheert schermtijd en stimuleert verantwoord internetgebruik.

**Opmerking**: sommige modellen, zoals Mango (GL-MT300N-V2) en Shadow (GL-AR300M-serie), ondersteunen Parental Control wegens onvoldoende geheugen niet.

Bekijk deze video of volg de onderstaande stappen om Parental Control in te stellen.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Lokale versie {#local-version}

De lokale versie wordt door GL.iNet geleverd, is momenteel in bèta en kost niets extra. Voer domeinen handmatig in om verzoeken per toepassing te filteren.

### Supported Models {#supported-models}

??? "Ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)

??? "Niet-ondersteunde modellen"
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

### Installatiestappen {#setup-steps}

Meld je aan bij het webbeheerpaneel en ga naar **APPLICATIONS** -> **Parental Control**.

Controleer of de routertijd klopt. Ga anders eerst naar **SYSTEM** -> **Time Zone** om deze te synchroniseren.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Schakel Parental Control in en klik op **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: blokkeert internettoegang voor alle apparaten die niet in de Parental Control-lijst staan.

Volg vervolgens de installatiewizard om Parental Control in te stellen.

---

Hieronder staat een voorbeeldsituatie. Pas de instellingen naar behoefte aan.


**Situatie**: apparaten in het profiel mogen op weekdagen van 8:00 tot 11:00 internet gebruiken voor studie en in het weekend van 18:00 tot 20:00 voor games. Op andere tijden is internet standaard geblokkeerd.

Volg de onderstaande stappen om Parental Control in te stellen.

1. Maak een profiel en stel een naam in.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Selecteer de apparaten die je wilt beheren. Verbind ze eerst met de router of voeg ze handmatig via hun MAC-adres toe.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Stel de toegangslimiet in.

    Er zijn twee standaardregelsets: **Block Internet Access** en **No Limit**.

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Klik op **Add a New Ruleset** om voor later gebruik **Learning** en **Play** te maken.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Geef de naam en kleur van de regelset op, voer de te blokkeren websites in en klik op **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Opmerking**: domeinnamen in de blokkeerlijst moeten hun subdomeinen omvatten. "example.com" omvat bijvoorbeeld ook "subdomain.example.com".

    Maak op dezelfde manier een tweede regelset, geef naam en kleur op, voer websites in en klik op **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    Na toepassing zijn er vier regelsets. Selecteer **Block Internet Access** als **Default Ruleset** en klik op **Finish**.

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Stel vervolgens een schema voor het profiel in. Klik op **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    Voeg **Learning** aan het schema toe. Stel **Execution Time** op weekdagen in van 8:00 tot 11:00 en klik op **Apply**.

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. De bewerkingspagina van het nieuwe profiel wordt geopend.

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Onderaan zie je het gemaakte schema. Klik rechtsboven op het tandwielpictogram en selecteer **Add Schedule**.

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Voeg **Play** aan het schema toe. Stel **Execution Time** in het weekend in van 18:00 tot 20:00 en klik op **Apply**.

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    De regelset Play wordt aan het schema toegevoegd.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Opmerking**: de rode stippellijn geeft de huidige tijd aan.

    Klik op een regelset in het schema om de uitvoeringstijd te wijzigen.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Klik bovenaan op **Parental Control** om naar de pagina terug te keren.

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    De uiteindelijke configuratie wordt weergegeven. Parental Control werkt nu volgens het schema. Je kunt profielen en regelsets wijzigen of toevoegen.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Troubleshooting {#troubleshooting}

Controleer de volgende mogelijke oorzaken als instellingen niet werken.

1. Probleem met DNS-cache.

    Browsers en besturingssystemen bewaren een DNS-cache, waardoor wijzigingen vertraagd kunnen worden toegepast. Wis de cache om wijzigingen direct toe te passen.

2. Het profielschema is nog niet begonnen.

3. De ingevoerde domeinnaam is mogelijk onjuist.

    Het openbare domein van een website is eenvoudig te vinden, maar API-domeinen van apps zijn vaak niet openbaar. Gebruik Wireshark of zoek de domeingegevens op.

    Bij het blokkeren van `www.google.com` geeft `google.com` bijvoorbeeld betere resultaten.

4. Het doelapparaat gebruikt per netwerkverbinding een willekeurig MAC-adres, waardoor toegangsregels niet werken. Schakel dit uit en voeg het apparaat opnieuw toe.

## Bark-versie {#bark-version}

Deze handleiding geldt voor firmware v4.8 en ouder. Klik voor nieuwere versies [hier](bark.md).

De dienst [Bark](https://www.bark.us/){target="_blank"} helpt de digitale wereld van je kind te beschermen en biedt uitgebreide online beveiliging. Normaal is hiervoor een betaald abonnement vereist. Door onze samenwerking met Bark biedt GL.iNet het Bark Home-abonnement echter gratis aan **op bepaalde routermodellen**, met geavanceerde bewaking en waarschuwingen zonder extra kosten.

**Note**:

1. De Bark-dienst is **alleen beschikbaar in de Verenigde Staten, Australië en Zuid-Afrika**. Klik [hier](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} voor meer informatie.

2. De twee versies van Parental Control kunnen niet tegelijk actief zijn. Bij inschakeling van één wordt de andere uitgeschakeld.

### Supported Models {#supported-models_1}

??? "Ondersteunde modellen"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)

??? "Niet-ondersteunde modellen"
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

### Installatiestappen {#setup-steps_1}

Meld je aan bij het webbeheerpaneel, ga naar **APPLICATIONS** -> **Parental Control** en selecteer Bark.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

Zet de schakelaar om om Bark in te schakelen en klik op **Apply**.

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

Koppel vervolgens het apparaat aan je Bark-account. Klik op **Device Pairing Link** of [hier](https://www.bark.us/app/signup/?ref=glinet&home=glinet).

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Je wordt doorgestuurd naar de Bark-website. Volg de instructies op het scherm om je aan te melden, het apparaat te koppelen, een profiel te maken en de eerste installatie te voltooien.

![bark_welcome_page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_welcome.png){class="glboxshadow"}
<small>(Aanmelden bij Bark)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow"}
<small>(Apparaat gekoppeld)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_create_profile.png){class="glboxshadow"}
<small>(Een profiel maken)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_get_started.png){class="glboxshadow"}
<small>(Eerste installatie)</small>

Nadat je apparaat verbinding heeft gemaakt met de Bark-clouddiensten en aan je account is gekoppeld, wordt het webbeheerpaneel van de router als volgt weergegeven.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Klik op **Go to Bark** of [hier](https://www.bark.us/app/children/?ref=glinet&home=glinet){target="_blank"} om je aan te melden bij het Bark-dashboard en regels voor ouderlijk toezicht in te stellen.

GL.iNet is niet de aanbieder van deze dienst. Neem bij problemen met Bark rechtstreeks contact op met de [technische ondersteuning van Bark](https://www.bark.us/contact-us/?ref=glinet&home=glinet){target="_blank"}.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
