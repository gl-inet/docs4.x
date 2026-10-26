# eSIM Management {#esim-management}

**Note**:

1. Guiden gäller modeller som stöder GL.iNets fysiska eSIM-kort.

2. GL-E5800 (Mudi 7) har ett inbyggt eSIM och stöder inte GL.iNets fysiska eSIM-kort. Ett fysiskt eSIM-kort identifieras som ett vanligt SIM-kort utan eSIM-funktioner på Mudi 7.

## Supported Models {#supported-models}

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

    1. **For models marked with ※**, support for physical eSIM cards depends on the module in use.

        - Om du använder modulen **EC25-AF**, **EC25-E** eller **EG25-G** installerar du firmware med eSIM-stöd innan ett fysiskt eSIM-kort används. [Kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"} för fler anvisningar.

        - Om du använder modulen **EP06-E** följer du [den här länken](https://forum.gl-inet.com/t/upgrade-ep06-e-firmware-to-support-esim/48907){target="_blank"} för att först uppgradera modulens firmware och sedan installera firmware med eSIM-stöd.

        - Modulen **EP06-A** stöder inte fysiska eSIM-kort eftersom Qualcomms programvara saknar stöd för nödvändiga AT-kommandon.

    2. **GL-E750V2 <u>vSIM</u>** does not support eSIM physical card.

    3. **GL-E5800 (Mudi 7)** har ett inbyggt eSIM. Ett fysiskt eSIM-kort identifieras därför som ett vanligt SIM-kort utan eSIM-funktioner på Mudi 7.

## eSIM Management {#esim-management_1}

Öppna **APPLICATIONS** -> **eSIM Management** på vänster sida i webbadministrationspanelen.

På sidan kan du kontrollera statusen för det fysiska eSIM-kortet och hantera eSIM-profiler. Den består av **Current eSIM Status** och **eSIM Profile List**.

![esim detected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_detected.png){class="glboxshadow"}

## Current eSIM Status {#current-esim-status}

Avsnittet visar grundläggande och detaljerad information om den aktiva eSIM-profilen.

![esim status](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_status.png){class="glboxshadow"}

- **EID:** Globalt unik identifierare för eUICC (eSIM-chip), som används för identifiering och profilhantering.
- **ICCID:** Integrated Circuit Card Identifier för den aktiva eSIM-profilen.
- **IMSI:** International Mobile Subscriber Identity för den aktiva eSIM-profilen.
- **eSIM OS Version:** Operativsystemsversionen för eUICC, som avgör kompatibilitet och funktioner som stöds.
- **eSIM Storage (remain/total):** Tillgänglig och total lagringskapacitet på eUICC för eSIM-profiler.
- **eSIM Profile Number:** Antal eSIM-profiler som lagras på eUICC. Profilernas storlek varierar mellan operatörer, så antalet som kan lagras varierar också.

## eSIM Profile List {#esim-profile-list}

Avsnittet visar information om eSIM-startprofilen och vanliga profiler.

![esim profile list](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_profile_list.png){class="glboxshadow"}

- **Seed Profile**: Startprofilen innehåller 1GB kostnadsfri data för USA och Europa samt 100MB global data, giltig i 1 år från aktiveringen. Med denna data kan du hämta andra profiler över hela världen. Du kan övervaka återstående data, total datamängd och utgångsdatum.

- **Normal Profile**: När du köper en eSIM-profil och laddar upp den via QR-kod eller aktiveringskod visas den här.

### Top-up Seed Profile {#top-up-seed-profile}

GL.iNet tillhandahåller en förinstallerad startprofil med 100MB global data och 1GB data för Europa och USA för första konfiguration och aktivering. Abonnemanget är avsett för hämtning av nya eSIM-profiler när internetåtkomst saknas på destinationen.

Om den kostnadsfria datan är slut eller har gått ut kan du fylla på startprofilen.

Klicka på **Top-up** till höger i avsnittet Seed Profile.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed1.png){class="glboxshadow"}

Skanna QR-koden i popup-fönstret och följ anvisningarna för att slutföra påfyllningen.

![top-up seed profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/top-up_seed2.png){class="glboxshadow" width="400"}

### Purchase eSIM Profile {#purchase-esim-profile}

Du kan köpa eSIM-profiler från rekommenderade eller testade butiker eller andra tredjepartsleverantörer.

??? note "Option 1: Purchase from our recommended stores"

    There are two recommended stores: [EIOTCLUB eSIM Store](https://www.eiotclub.com/pages/esim){target="_blank"} and [Tuge eSIM Store](https://esim_store.gl-inet.com){target="_blank"}.

    Klicka på **eSIM Profile Recommended Store** till höger i avsnittet Normal Profile.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store1.png){class="glboxshadow"}

    Skanna QR-koden eller klicka på länkarna för att köpa eSIM-profiler.

    ![esim recommended store](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/recommended_store2.png){class="glboxshadow"}

    **Obs!** Alla paket från dessa två butiker är helt kompatibla med GL.iNet-routrar. Kontakta supporten på [support@gl-inet.com](mailto:support@gl-inet.com) om du har frågor.

??? note "Option 2: Purchase from tested stores"

    Refer to [this link](https://forum.gl-inet.com/t/carriers-supported-by-gl-inet-physical-esim/54164){target="_blank"} to view a list of stores tested by GL.iNet.

    **Obs!** Vi kan inte garantera full kompatibilitet för alla profiler eller paket från dessa butiker. GL.iNet samarbetar inte med dem och kan inte ge eftermarknadssupport eller hjälpa till med återbetalningar.

??? note "Option 3: Purchase from other third-party eSIM providers"

    Du kan även köpa eSIM-profiler från andra tredjepartsleverantörer.

    Vi kan dock inte garantera full kompatibilitet för profiler från andra tredjepartsleverantörer. Köp efter eget omdöme. GL.iNet ansvarar inte för kompatibilitetsproblem.

    Kontakta eSIM-leverantören för eftermarknadssupport eller återbetalning.

### Upload eSIM Profile {#upload-esim-profile}

När du köper en eSIM-profil får du vanligtvis en QR-kod eller aktiveringskod. Spara QR-koden lokalt och följ stegen nedan för att ladda upp profilen.

1. Klicka på **Add eSIM Profile** längst ned i avsnittet Normal Profile.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile1.png){class="glboxshadow"}

2. Ladda upp eSIM-QR-koden eller ange aktiveringskoden och klicka på **Install**. Profilen hämtas och installeras på routern.

    ![add esim profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/add_esim_profile2.png){class="glboxshadow"}

    **Note:**

    1. De flesta eSIM-profiler kan endast hämtas och installeras en gång.

    2. En korrekt formaterad QR-kod visar en aktiveringskod som börjar med **LPA:**. Vissa icke-standardiserade koder visar endast en rå kod utan prefixet. Lägg då till `LPA:` i början innan du klickar på Install.

        ![esim activation code](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/activation_code.jpg){class="glboxshadow" width="550"}

    3. Om du saknar eSIM-profil kan du köpa en från eSIM Profile Recommended Store. Klicka [här](#purchase-esim-profile) för mer information.

3. Enable your eSIM Profile.

    Efter uppladdningen visas den nya profilen i listan **Normal Profile**. Klicka på **Enable** för att aktivera den.

    ![enable profile](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/enable_profile.jpg){class="glboxshadow"}

4. Connect to the Internet.

    När profilen har aktiverats öppnar du **INTERNET** -> **Cellular**. Klicka på **Connect** för att ansluta via profilen.

    ![esim connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connect.png){class="glboxshadow"}

    **Obs!** Vissa profiler kräver ytterligare inställningar, till exempel APN, PIN eller TTL. Klicka vid behov på **Manual Setup** eller **SIM Card Settings**. I vissa fall måste enheten startas om.

5. Once the router connects successfully via the eSIM profile, the page will display as follows:

    ![esim connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/esim_connected.png){class="glboxshadow"}

### Export Log for Support {#export-log-for-support}

Klicka på **Export Log for Support** för att visa alla eSIM-loggar. Vid problem exporterar du loggarna och skickar dem till supporten på [support@gl-inet.com](mailto:support@gl-inet.com).

![export log](https://static.gl-inet.com/docs/router/en/4/interface_guide/esim_management/export_log.png){class="glboxshadow"}

---

Related Articles:

- [Använd ett fysiskt eSIM-kort med GL.iNet-routrar](../tutorials/how_to_use_esim_physical_card_with_glinet_routers.md)
- [Använd ett fysiskt eSIM-kort med Android-enheter](../tutorials/how_to_use_the_esim_physical_card_with_android_devices.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
