# Parental Control {#parental-control}

**Obs!** Guiden gäller firmware v4.8 och tidigare. För senare versioner, klicka [här](parental_control_v4.9.md).

---

Öppna **APPLICATIONS** -> **Parental Control**.

Föräldrakontroll skyddar barn online genom att blockera olämpliga webbplatser och begränsa skärmtid.

**Obs!** Vissa modeller, till exempel Mango (GL-MT300N-V2) och Shadow (GL-AR300M-serien), stöder inte Parental Control på grund av otillräckligt minne.

Titta på videon eller följ stegen nedan för att konfigurera Parental Control.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pOyDwQRc3io" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Local Version {#local-version}

Den lokala versionen från GL.iNet är kostnadsfri och i beta. För programbaserad filtrering måste domänen anges manuellt.

### Supported Models {#supported-models}

??? "Supported Models"
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

??? "Unsupported Models"
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

### Setup Steps {#setup-steps}

Logga in på webbadministrationspanelen och öppna **APPLICATIONS** -> **Parental Control**.

Kontrollera routerns tid och synkronisera vid behov under **SYSTEM** -> **Time Zone**.

![router time](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_time.png){class="glboxshadow"}

Aktivera Parental Control och klicka på **Apply**.

![parental control, enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/parental_control_enable.png){class="glboxshadow"}

- **Block WAN for Unmanaged Devices**: Blockerar internet för enheter utanför Parental Control-listan.

Följ konfigurationsguiden.

---

Följande exempel kan anpassas efter behov.


**Scenario**: Profilens enheter får internet för studier 8–11 på vardagar och spel 18–20 på helger. Övrig tid blockeras internet.

Follow the steps below to set up Parental Control.

1. Create a profile and customize a name.

    ![create a profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_1_create_profile.png){class="glboxshadow"}

2. Välj enheter. Anslut dem först till routern eller lägg till deras MAC-adresser manuellt.

    ![select devices](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_2_select_device.png){class="glboxshadow"}

3. Set access limit.

    There are two default rulesets: **Block Internet Access** and **No Limit**.

    ![default rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_3_default_rulesets.png){class="glboxshadow"}

    Click **Add a New Ruleset** to create two more rulesets for later use: **Learning** and **Play**.

    ![add new ruleset](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_4_add_ruleset.png){class="glboxshadow"}

    Ange namn, till exempel Learning, och färg, ange webbplatser som ska blockeras och klicka på **Apply**.

    ![create a ruleset 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_5_add_ruleset_learning.png){class="glboxshadow"}

    **Obs!** Domäner i blockeringslistan omfattar underdomäner. `example.com` omfattar exempelvis `subdomain.example.com`.

    Skapa på samma sätt en regeluppsättning, till exempel Play, ange färg och webbplatser och klicka på **Apply**.

    ![create a ruleset 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_6_add_ruleset_play.png){class="glboxshadow"}

    När fyra regeluppsättningar finns väljer du **Block Internet Access** som **Default Ruleset** och klickar på **Finish**.

    ![four rulesets](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_7_four_rulesets.png){class="glboxshadow"}

4. Schemalägg profilen genom att klicka på **Go to Set**.

    ![set schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_8_set_schedule.png){class="glboxshadow"}

    Lägg till **Learning**, ange **Execution Time** 8–11 på vardagar och klicka på **Apply**.

    ![add schedule learning](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_9_schedule_learning.png){class="glboxshadow"}

5. Redigeringssidan för den nya profilen öppnas.

    ![profile created](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_10_profile_created.png){class="glboxshadow"}

    Bläddra längst ned, klicka på kugghjulet och välj **Add Schedule**.

    ![profile add schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_11_add_schedule.png){class="glboxshadow"}

6. Lägg till **Play**, ange **Execution Time** 18–20 på helger och klicka på **Apply**.

    ![add schedule play](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_12_schedule_play.png){class="glboxshadow"}

    Play läggs till i schemat.

    ![schedules](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_13_schedules.png){class="glboxshadow"}

    **Note**: The red dashed line indicates the current time.

    Klicka på en regeluppsättning för att ändra körningstiden.

    ![edit schedule](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_14_schedule_edit.jpg){class="glboxshadow"}

7. Klicka på **Parental Control** högst upp för att återgå.

    ![parental control page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_15_parental_control.png){class="glboxshadow"}

    Den slutliga konfigurationen visas och schemat tillämpas. Profiler och regler kan ändras eller läggas till.

    ![final configuration](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/guide/guide_16_final_config.png){class="glboxshadow"}

### Troubleshooting {#troubleshooting}

Om inställningarna inte får effekt kontrollerar du följande orsaker.

1. DNS cache issue.

    DNS-cache i webbläsare och operativsystem kan fördröja ändringar. Rensa cachen.

2. Profilschemat har inte börjat.

3. The entered domain name may be incorrect.

    Programs använder ofta icke-offentliga API-domäner. Hitta rätt domän med exempelvis Wireshark eller domäninformation.

    For example, when blocking `www.google.com`, entering `google.com` delivers better results than `www.google.com`.

4. Målenheten använder slumpmässig MAC-adress. Inaktivera den och lägg till enheten i profilen igen.

## Bark Version {#bark-version}

Guiden gäller firmware v4.8 och tidigare. För senare versioner, klicka [här](bark.md).

Tjänsten [Bark](https://www.bark.us/){target="_blank"} kan skydda ditt barns digitala miljö och ge heltäckande skydd online. Den kräver vanligtvis en betalprenumeration. Genom vårt samarbete med Bark erbjuder GL.iNet dock abonnemanget Bark Home utan kostnad **på utvalda routermodeller**, med avancerad övervakning och varningar utan extra kostnad.

**Note**:

1. Bark-tjänsten är **endast tillgänglig i USA, Australien och Sydafrika**. Klicka [här](https://support.bark.us/hc/en-us/articles/360049965072-International-availability){target="_blank"} för mer information.

2. The two Parental Control versions cannot be enabled at the same time. Enabling one will automatically disable the other.

### Supported Models {#supported-models_1}

??? "Supported Models"
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)

??? "Unsupported Models"
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

### Setup Steps {#setup-steps_1}

Logga in, öppna **APPLICATIONS** -> **Parental Control** och välj Bark-versionen.

![switch_versions](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/switch_versions.png){class="glboxshadow"}

Aktivera Bark med reglaget och klicka sedan på **Apply**.

![bark_enable](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_enable.png){class="glboxshadow"}

Parkoppla enheten med Bark-kontot via **Device Pairing Link** eller [den här länken](https://www.bark.us/app/signup/?ref=glinet&home=glinet).

![bark_pairing_link](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_pairing.png){class="glboxshadow"}

Du omdirigeras till Barks webbplats. Följ anvisningarna på skärmen för att logga in, parkoppla enheten, skapa en profil och slutföra den första konfigurationen.

![bark_welcome_page](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_welcome.png){class="glboxshadow"}
<small>(Bark login)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_setup.png){class="glboxshadow"}
<small>(Device paired)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_create_profile.png){class="glboxshadow"}
<small>(Create a profile)</small>

![bark_set_up](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_get_started.png){class="glboxshadow"}
<small>(Initial setup)</small>

När enheten har anslutits till Bark Cloud-tjänsterna och parkopplats med kontot visas routerns webbadministrationspanel enligt följande.

![bark_paired](https://static.gl-inet.com/docs/router/en/4/interface_guide/parental_control/bark_paired.png){class="glboxshadow"}

Klicka på **Go to Bark** eller [här](https://www.bark.us/app/children/?ref=glinet&home=glinet){target="_blank"} för att logga in på Bark-instrumentpanelen och konfigurera regler för föräldrakontroll.

Eftersom GL.iNet inte tillhandahåller tjänsten bör du kontakta [Barks tekniska support](https://www.bark.us/contact-us/?ref=glinet&home=glinet){target="_blank"} direkt om problem uppstår när du använder Bark.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
