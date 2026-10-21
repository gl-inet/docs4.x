# Så använder du det fysiska eSIM-kortet med GL.iNet-routrar {#how-to-use-the-esim-physical-card-with-glinet-routers}

Den här guiden visar hur du använder det fysiska eSIM-kortet som köpts i GL.iNets webbutik med GL.iNet-routrar.

![eSIM Physical Card](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/simpoyo-esim-physical-card.png){class="glboxshadow"}

## Funktioner {#features}

Det fysiska eSIM-kortet har följande fördelar:

- Stöder 4G- och 5G-nätverk för tillförlitliga och snabba anslutningar.
- Gör det enkelt att hantera eSIM-profiler genom att lägga till, ta bort eller aktivera dem.
- Låter dig när som helst välja och köpa önskat datapaket från de flesta eSIM-butiker i världen.
- Fungerar med eSIM-profiler från de flesta globala eSIM-butiker.
- Låter dig köpa eSIM-profiler online utan att lämna personuppgifter, vilket minskar risken för integritetsintrång.
- Levereras med en startprofil som innehåller 1GB kostnadsfri data för USA och Europa samt 100MB global data, giltig i 1 år från aktiveringsdatumet.
- Är kompatibelt med utvalda GL.iNet-enheter.

## Modeller som stöds {#supported-models}

!!! note "Modeller som stöds"

    - GL-X2000 (Spitz Plus)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-E750V2 (Mudi V2)
    - ※ GL-E750 (Mudi)
    - ※ GL-XE300 (Puli)
    - ※ GL-X750 (Spitz)
    - ※ GL-X300B (Collie)

    **Obs!**

    1. **För modeller markerade med ※** beror stödet för fysiska eSIM-kort på vilken modul som används.

        - Om enheten använder modulen **EC25-AF**, **EC25-E** eller **EG25-G** installerar du firmware med eSIM-stöd innan du använder ett fysiskt eSIM-kort. [Kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"} för mer information.

        - Om enheten använder modulen **EP06-E** följer du först [den här länken](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} för att uppgradera modulens firmware. Installera därefter firmware med eSIM-stöd.

        - Modulen **EP06-A** stöder inte fysiska eSIM-kort eftersom Qualcomm-programvaran saknar stöd för de AT-kommandon som krävs.

    2. **GL-E750V2 <u>vSIM</u>** stöder inte fysiska eSIM-kort.

    3. **GL-E5800 (Mudi 7)** har ett inbyggt eSIM. Det fysiska eSIM-kortet identifieras därför som ett vanligt SIM-kort utan eSIM-funktioner på Mudi 7.

## Konfigurera det fysiska eSIM-kortet {#set-up-esim-physical-card}

Om du använder det fysiska eSIM-kortet för första gången kan du titta på konfigurationsvideon eller följa stegen nedan för att konfigurera det på din GL.iNet-router.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SCex_vuvgNQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

**Steg 1:** Sätt i det fysiska eSIM-kortet i routern. Bilderna nedan visar hur du gör.

![E750V2](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/e750v2-sim-card.jpg){class="glboxshadow"}

![X3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/x3000-sim-card.jpg){class="glboxshadow"}

![XE3000](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/xe3000-sim-card.jpg){class="glboxshadow"}

**Steg 2:** Öppna en webbläsare och ange `192.168.8.1` i adressfältet för att logga in på GL.iNet-administrationspanelen.

![log in](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/login-admin-panel.jpg){class="glboxshadow"}

**Steg 3:** Anslut enheten till internet.

När du har loggat in går du till **INTERNET** -> **Cellular**.

På routrar med dubbla SIM-kortplatser kontrollerar du att kortplatsen med det fysiska eSIM-kortet är inställd som **Active SIM Card**. Klicka annars på **SIM Card Switch** och välj SIM-kortplatsen där det fysiska eSIM-kortet sitter.

Klicka sedan på **Connect** (eller **Auto Setup** i äldre firmwareversioner) för att ansluta till internet via mobilnätet.

*Det fysiska eSIM-kortet levereras med en startprofil som innehåller 1GB kostnadsfri data för USA och Europa samt 100MB global data, giltig i 1 år från aktiveringsdatumet. Observera att denna data endast är avsedd för köp och hämtning av eSIM-profiler och inte för vanlig internetåtkomst.*

![initial setup connect](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connect.jpg){class="glboxshadow"}

När anslutningen har upprättats visas följande skärm.

![initial setup connected](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/initial-setup-connected.jpg){class="glboxshadow"}

## Hantera din eSIM-profil {#manage-your-esim-profile}

**Steg 1:** Kontrollera att den senaste firmwareversionen är installerad på GL.iNet-enheten.

Kontrollera att Version är 4.0 eller senare och att Firmware Type-numret är 0319 eller högre.

![auto setup successfully](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/latest-firmware.png){class="glboxshadow"}

Om din firmware **inte är uppdaterad** kan du uppgradera den automatiskt online eller manuellt.

<u>Alternativ 1</u>: Uppgradering av firmware online

1. Kontrollera att enheten är ansluten till internet.

2. Gå till **SYSTEM** -> **Upgrade** -> **Online Upgrade** i webbadministrationspanelen och klicka på **Install** för att uppdatera automatiskt till den senaste firmwareversionen.

    ![online upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/online-upgrade.png){class="glboxshadow"}

<u>Alternativ 2</u>: Manuell firmwareuppdatering

1. Hämta firmware med eSIM-stöd för rätt modell [här](https://dl.gl-inet.com/){target="_blank"}.

2. Gå till **SYSTEM** -> **Upgrade** -> **Local Upgrade** i webbadministrationspanelen. Välj firmwarefilen eller dra den till det angivna området för att uppgradera till den senaste versionen.

    ![local upgrade](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/local-upgrade.png){class="glboxshadow"}

!!! Note

    1. Vissa modeller, till exempel Mudi (GL-E750), Puli (GL-XE300) och Spitz (GL-X750), stöder inte eSIM om de är utrustade med Quectel EP06-A-moduler, eftersom Qualcomm-programvaran saknar stöd för vissa AT-kommandon.

    2. Om enheterna har EP06-E-moduler följer du [den här länken](https://forum.gl-inet.com/t/48907){target="_blank"} för att uppgradera modulen till den senaste programvaran med eSIM-stöd.

**Steg 2:** Gå till eSIM Management.

Vänta tills enheten har startats om efter firmwareuppdateringen och logga sedan in på GL.iNet-administrationspanelen.

Gå till **APPLICATIONS** -> **eSIM Management**. Här kan du visa eSIM-statusen och hantera eSIM-profiler.

![eSIM manage](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_set_up_the_esim/esim-manage-status.jpg){class="glboxshadow"}

Endast en eSIM-profil kan vara aktiv åt gången. En grön punkt visar att den valda eSIM-profilen är aktiv.

---

Relaterad artikel:

- [eSIM Management](../interface_guide/esim_management.md){target="_blank"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
