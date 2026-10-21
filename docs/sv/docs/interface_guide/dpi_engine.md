# DPI Engine {#dpi-engine}

**Note**: This feature was introduced in firmware v4.9.

Vissa modeller, till exempel Mango 2 (GL-MG1300), stöder inte DPI Engine på grund av otillräckligt minne, även med firmware v4.9 eller senare. Mer information finns i [Supported Models](#supported-models).

---

DPI (Deep Packet Inspection) är en central teknik för intelligent nätverkshantering. Till skillnad från traditionella routrar, som endast identifierar käll- och destinationsadresser, analyserar DPI paketens nyttolast på djupet och identifierar program och webbplatser exakt med ett bibliotek för funktionsmatchning. Det möjliggör detaljerad klassificering och styrning av trafiken.

GL.iNet DPI Engine körs lokalt på routern och ger intelligent nätverkshantering med fullständig integritet. Den ger full åtkomst till trafikstatistik, innehållsfiltrering och QoS för heltäckande trafikstyrning.

GL.iNet DPI är integrerat med [Netify](https://www.netify.ai/){target="_blank"} och använder ett resurssnålt inbäddat insticksprogram för effektiv distribution. Netifys signaturdatabas uppdateras online och möjliggör tillförlitlig hantering, vilket gör nätverksstyrningen mer exakt och effektiv.

**Note**:

1. När routern är i Drop-in Gateway-läge får DPI-funktionerna (Data Statistics, Content Filter och QoS) och SQM ingen effekt.
2. När DPI aktiveras inaktiveras Network Acceleration automatiskt för stabil prestanda.

## Supported Models {#supported-models}

??? "Supported Models"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-MT6000 (Flint 2)
    - GL-MT3000 (Beryl AX)

??? "Unsupported Models"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)

## Quick Setup {#quick-setup}

Öppna **FLOW CONTROL** -> **DPI Engine** på vänster sida i webbadministrationspanelen och klicka på **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Läs och godkänn Terms of Service & Privacy Policy i popup-fönstret och klicka sedan på **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Vänta medan routern utför systemåtgärder. Network Acceleration inaktiveras och Data Statistics och Content Filter aktiveras.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Once activated, click **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Du omdirigeras till **DPI Engine Version Center**, där du kan visa versionerna för DPI Program och Database.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Obs!** Sidan visar endast centrala systemstatusindikatorer. Trafikbearbetningen startar när de relevanta funktionerna har aktiverats.

## Database Upgrade {#database-upgrade}

Om en nyare databasversion är tillgänglig klickar du på **Upgrade** för att uppdatera databasen.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
