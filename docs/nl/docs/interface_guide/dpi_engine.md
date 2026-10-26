# DPI Engine {#dpi-engine}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Sommige modellen, zoals Mango 2 (GL-MG1300), ondersteunen DPI Engine wegens onvoldoende geheugen niet, ook niet met firmware v4.9 of hoger. Raadpleeg [Ondersteunde modellen](#supported-models) voor meer informatie.

---

DPI (Deep Packet Inspection) is een kerntechnologie voor intelligent netwerkbeheer. Traditionele routers identificeren alleen bron- en bestemmingsadressen. DPI analyseert daarentegen de inhoud van pakketten grondig en identificeert toepassingen en websites nauwkeurig met een bibliotheek voor kenmerkherkenning. Hierdoor zijn fijnmazige verkeersclassificatie en -regeling mogelijk.

GL.iNet DPI Engine wordt lokaal op je router uitgevoerd en biedt intelligent netwerkbeheer met volledige privacy. Je hebt volledige toegang tot verkeersstatistieken, inhoudsfiltering en QoS voor uitgebreid verkeersbeheer.

GL.iNet DPI is geïntegreerd met [Netify](https://www.netify.ai/){target="_blank"} en gebruikt een lichte ingebouwde plug-in voor efficiënte implementatie. Dankzij de online bijgewerkte kenmerkendatabase van Netify biedt het betrouwbaar beheer, waardoor netwerkregeling nauwkeuriger en efficiënter wordt.

**Note**:

1. Wanneer de router in de modus Drop-in Gateway staat, werken DPI-functies, waaronder Data Statistics, Content Filter en QoS, en SQM niet.
2. Wanneer DPI is ingeschakeld, wordt Network Acceleration automatisch uitgeschakeld voor stabiele prestaties.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
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

??? "Niet-ondersteunde modellen"
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

## Snelle installatie {#quick-setup}

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **DPI Engine** en klik op **Enable DPI Engine**.

![dpi engine initial](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_engine_initial.png){class="glboxshadow"}

Lees in het pop-upvenster Terms of Service & Privacy Policy, ga ermee akkoord en klik op **Apply**.

![activate 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate1.png){class="glboxshadow"}

Wacht terwijl de router systeembewerkingen uitvoert. Network Acceleration wordt uitgeschakeld en Data Statistics en Content Filter worden ingeschakeld.

![activate 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activate2.png){class="glboxshadow"}

Klik na activering op **Done**.

![activated](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/activated_success.png){class="glboxshadow"}

Je wordt doorgestuurd naar **DPI Engine Version Center**, waar je de DPI Program-versie en Database-versie kunt bekijken.

![dpi version center](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/dpi_version_center.png){class="glboxshadow"}

**Opmerking**: deze pagina toont alleen kernindicatoren voor de systeemstatus. De verwerking van verkeer begint zodra de bijbehorende functies zijn ingeschakeld.

## Database upgraden {#database-upgrade}

Als een nieuwere databaseversie beschikbaar is, klik je op **Upgrade** om de database bij te werken.

![database upgrade](https://static.gl-inet.com/docs/router/en/4/interface_guide/dpi_engine/database_upgrade.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
