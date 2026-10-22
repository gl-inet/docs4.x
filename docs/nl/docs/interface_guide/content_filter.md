# Content Filter {#content-filter}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Sommige modellen, zoals Mango 2 (GL-MG1300), ondersteunen Content Filter wegens onvoldoende geheugen niet, ook niet met firmware v4.9 of hoger. Raadpleeg [Ondersteunde modellen](#supported-models) voor meer informatie.

---

Content Filter is een intelligente online beveiligingsfunctie op basis van DPI-classificatie. De functie blokkeert automatisch schadelijke en kwaadaardige websites om je netwerk schoon en veilig te houden. Ook worden aangepaste regels ondersteund om specifieke apps, domeinen of IP-adressen te blokkeren.

**Note**:

1. Content Filter werkt niet wanneer de router in de modus Drop-in Gateway staat.
2. Content Filter kan niet samen met Network Acceleration worden gebruikt. Wanneer je Content Filter inschakelt, wordt Network Acceleration automatisch uitgeschakeld voor stabiele prestaties.

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

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **Content Filter**.

Zet de schakelaar rechtsboven om, pas de geblokkeerde inhoud aan, zoals apps, domeinen of IP-adressen, en klik op **Apply**.

![content filter](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/content-filter.png){class="glboxshadow"}

Deze pagina bestaat uit twee onderdelen:

- **Blocked Apps List**: dit gedeelte bevat drie vooraf geselecteerde categorieën: Gambling, Adult en Malware. Wanneer deze zijn ingeschakeld, worden alle bijbehorende websites, diensten en apps geblokkeerd.

    Je kunt ook op **Edit App** klikken om zo nodig meer categorieën toe te voegen, zoals Game en Social Media.

    ![edit app 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app1.jpg){class="glboxshadow"}

    Selecteer in het pop-upvenster de categorieën die je wilt blokkeren. De drie standaardcategorieën zijn leeg; alle andere categorieën bevatten een lijst met apps.

    ![edit app 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app2.png){class="glboxshadow" width="667"}

    Klik op een categorie om de apps te bekijken en te selecteren die je wilt blokkeren. Klik rechtsboven op **Select All** om alle apps in die categorie tegelijk te blokkeren en klik vervolgens op **Confirm**.

    ![edit app 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/edit_app3.png){class="glboxshadow" width="667"}

    De geselecteerde apps verschijnen vervolgens in de Blocked App List.

    ![blocked app list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_app_list.jpg){class="glboxshadow"}

- **Blocked Domain / IP List**: in dit gedeelte kun je specifieke domeinen, zoals google.com, CIDR-bereiken, zoals 192.168.8.0/24, of IP-adressen, zoals 192.168.10.10, handmatig invoeren om de toegang ertoe te blokkeren. De lijst ondersteunt maximaal 10000 vermeldingen.

    Voer de domeinen of IP-adressen in die je wilt blokkeren en klik op **Apply**.

    ![domain ip list](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/blocked_domain_ip.jpg){class="glboxshadow"}

## Content Filter testen {#content-filter-test}

In dit voorbeeld is de categorie **Game** geselecteerd, die Nintendo bevat.

![filter test1](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test1.png){class="glboxshadow"}

Op een laptop die met je router is verbonden, is de website `nintendo.com` niet meer toegankelijk. Voor het inschakelen van Content Filter was deze wel bereikbaar.

![filter test2](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test2.png){class="glboxshadow"}

In het webbeheerpaneel van de router kun je het aantal geblokkeerde toegangsverzoeken bekijken.

![filter test3](https://static.gl-inet.com/docs/router/en/4/interface_guide/content_filter/nintendo_test3.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
