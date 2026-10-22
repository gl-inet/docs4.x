# Data Statistics {#data-statistics}

**Opmerking**: deze functie is geïntroduceerd in firmware v4.9.

Sommige modellen, zoals Mango 2 (GL-MG1300), ondersteunen Data Statistics wegens onvoldoende geheugen niet, ook niet met firmware v4.9 of hoger. Raadpleeg [Ondersteunde modellen](#supported-models) voor meer informatie.

---

Ga links in het webbeheerpaneel naar **FLOW CONTROL** -> **Data Statistics**.

Data Statistics biedt een overzichtelijk verkeersdashboard dat het netwerkgebruik per toepassing en protocol identificeert. Je kunt historische trends over 1 uur, 1 dag en 7 dagen bekijken, gebruiksranglijsten weergeven, verkeer per apparaat bewaken en ongewenste apps met één klik blokkeren.

**Note**:

1. Data Statistics werkt niet wanneer de router in de modus Drop-in Gateway staat.
2. Data Statistics kan niet samen met Network Acceleration worden gebruikt. Wanneer je Data Statistics inschakelt, wordt Network Acceleration automatisch uitgeschakeld voor stabiele prestaties.
3. Data Statistics houdt alleen het verkeersgebruik bij van apparaten op de pagina Client. Als een apparaat via een tunnelinterface, zoals VPN Client, Tailscale of AstroWarp, verbinding maakt met de router, wordt verkeer van dat apparaat dat via de router wordt doorgestuurd niet in deze statistieken opgenomen.

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

## Voor firmware v4.11 en hoger {#for-firmware-v411-and-above}

Zet de schakelaar rechtsboven om om **Application Total Data** te bekijken.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Deze pagina bestaat uit twee onderdelen:

- **Top 10 Apps by Bandwidth Usage**: toont een tijdgebaseerde trendgrafiek, bijvoorbeeld van de afgelopen dag, met het bandbreedtegebruik van de tien belangrijkste toepassingen in de geselecteerde periode.

    Beweeg de muis over de grafiek om op een bepaald tijdstip het datagebruik van de tien apps met het hoogste bandbreedtegebruik te bekijken.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: toont uitgebreide verkeersgegevens voor elke toepassing, waaronder Download, Upload en Total Bandwidth. Zoek zo nodig met de zoekbalk naar specifieke apps.

    Klik op de sorteerpijl naast de kolomkop om de lijst oplopend of aflopend te sorteren.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Regels voor gegevensopslag {#data-storage-rules}

1. Verkeersstatistieken worden elke 15 seconden in het RAM opgeslagen en elk uur in de flashopslag bewaard. Regelmatig schrijven naar de flashopslag wordt vermeden om de levensduur ervan te beschermen.

2. Een zachte herstart veroorzaakt geen gegevensverlies. Het systeem schrijft gegevens eerst van het RAM naar de flashopslag voordat het opnieuw opstart.

3. Een harde herstart, waarbij de voeding wordt losgekoppeld en opnieuw aangesloten, of een firmware-upgrade met behoud van instellingen kan leiden tot verlies van gegevens uit maximaal het laatste uur.

### Clientselectie {#client-selector}

Met Client Selector kun je een specifieke client selecteren of de standaardoptie All clients behouden. De grafiek en tabel met statistieken worden automatisch vernieuwd en tonen alleen verkeersgegevens van het geselecteerde apparaat.

**Opmerking**: deze functie is geïntroduceerd in firmware v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Grafiekweergave wijzigen {#switch-chart-views}

Bij het bekijken van App Traffic Statistics kun je het grafiektype naar behoefte wijzigen.

**Opmerking**: deze functie is geïntroduceerd in firmware v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: volgt het bandbreedtegebruik over de geselecteerde periode. Doorlopende lijnen tonen hoe het verkeer in de loop van de tijd verandert, zodat stijgende en dalende gebruikstrends zichtbaar zijn.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: vergelijkt het bandbreedtegebruik van toepassingen naast elkaar. Afzonderlijke balken laten in één oogopslag zien welke apps meer bandbreedte gebruiken.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: verdeelt het totale bandbreedtegebruik in percentages. Segmenten tonen het relatieve aandeel van het verkeer dat elke toepassing gebruikt.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Periode wijzigen {#switch-time-range}

Je kunt de periode naar behoefte wijzigen tussen Past hour, Past day en Past week.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

De geselecteerde periode bepaalt hoe de gegevens worden weergegeven:

- **Voor een gedetailleerd overzicht, zoals Past Hour**: de grafiek toont fijnmazige realtime schommelingen. Pieken zijn hoger en dalingen steiler, waardoor plotselinge stijgingen in het bandbreedtegebruik eenvoudig zichtbaar zijn.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **Voor een breed overzicht, zoals Past Day of Past Week**: de grafiek vat de gegevens samen over een langere tijdlijn. De lijnen worden vloeiender en tonen de algemene verkeerstrend in plaats van elke kleine verandering.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Statistieken wissen {#clear-statistics}

Klik linksboven op het bezempictogram om de statistieken zo nodig te wissen.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Na het wissen wordt de pagina zoals hieronder bijgewerkt. Het kan even duren voordat nieuwe statistieken worden geladen.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## Voor firmware v4.9 tot v4.10 {#for-firmware-v49-to-v410}

Zet de schakelaar rechtsboven om om **Application Total Data** te bekijken.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Deze pagina bestaat uit twee onderdelen:

- **Top 10 Apps by Bandwidth Usage**: toont een tijdgebaseerde trendgrafiek, bijvoorbeeld van de afgelopen dag, met het bandbreedtegebruik van de tien belangrijkste toepassingen in de geselecteerde periode.

    Beweeg de muis over de grafiek om op een bepaald tijdstip het datagebruik van de tien apps met het hoogste bandbreedtegebruik te bekijken.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: toont uitgebreide verkeersgegevens voor elke toepassing, waaronder Download, Upload en Total Bandwidth. Zoek zo nodig met de zoekbalk naar specifieke apps.

    Klik op de sorteerpijl naast de kolomkop om de lijst oplopend of aflopend te sorteren.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Regels voor gegevensopslag {#data-storage-rules_1}

1. Verkeersstatistieken worden elke 15 seconden in het RAM opgeslagen en elk uur in de flashopslag bewaard. Regelmatig schrijven naar de flashopslag wordt vermeden om de levensduur ervan te beschermen.

2. Een zachte herstart veroorzaakt geen gegevensverlies. Het systeem schrijft gegevens eerst van het RAM naar de flashopslag voordat het opnieuw opstart.

3. Een harde herstart, waarbij de voeding wordt losgekoppeld en opnieuw aangesloten, of een firmware-upgrade met behoud van instellingen kan leiden tot verlies van gegevens uit maximaal het laatste uur.

### Periode wijzigen {#switch-time-range_1}

Je kunt de periode naar behoefte wijzigen tussen Past hour, Past day en Past week.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

De geselecteerde periode bepaalt hoe de gegevens worden weergegeven:

- **Voor een gedetailleerd overzicht, zoals Past Hour**: de grafiek toont fijnmazige realtime schommelingen. Pieken zijn hoger en dalingen steiler, waardoor plotselinge stijgingen in het bandbreedtegebruik eenvoudig zichtbaar zijn.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **Voor een breed overzicht, zoals Past Day of Past Week**: de grafiek vat de gegevens samen over een langere tijdlijn. De lijnen worden vloeiender en tonen de algemene verkeerstrend in plaats van elke kleine verandering.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Statistieken wissen {#clear-statistics_1}

Klik linksboven op het bezempictogram om de statistieken zo nodig te wissen.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Na het wissen wordt de pagina zoals hieronder bijgewerkt. Het kan even duren voordat nieuwe statistieken worden geladen.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
