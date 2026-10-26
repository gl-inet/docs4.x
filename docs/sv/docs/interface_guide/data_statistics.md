# Data Statistics {#data-statistics}

**Note**: This feature was introduced in firmware v4.9.

Vissa modeller, till exempel Mango 2 (GL-MG1300), stöder inte Data Statistics på grund av otillräckligt minne, även med firmware v4.9 eller senare. Mer information finns i [Supported Models](#supported-models).

---

Öppna **FLOW CONTROL** -> **Data Statistics** på vänster sida i webbadministrationspanelen.

Data Statistics ger en intuitiv trafikinstrumentpanel som visar nätverksanvändning efter program och protokoll. Den visar historiska trender för 1 timme, 1 dag och 7 dagar, användningsrankning och trafik per enhet samt blockerar oönskade program med ett klick.

**Note**:

1. Data Statistics får ingen effekt när routern är i Drop-in Gateway-läge.
2. Data Statistics cannot work with Network Acceleration. Enabling Data Statistics will automatically disable Network Acceleration to ensure stable performance.
3. Data Statistics spårar endast trafikanvändning för enheter på sidan Client. Om en enhet ansluter via ett tunnelgränssnitt, till exempel VPN Client, Tailscale eller AstroWarp, tas trafik från enheten som vidarebefordras genom routern inte med i statistiken.

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

## För firmware v4.11 och senare {#for-firmware-v411-and-above}

Toggle the switch in the upper right corner to view the **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_statistics.png){class="glboxshadow"}

Sidan består av två delar:

- **Top 10 Apps by Bandwidth Usage**: Visar ett tidsbaserat trenddiagram, till exempel för det senaste dygnet, över bandbreddsförbrukningen för de 10 främsta programmen under vald period.

    Håll pekaren över diagrammet för att visa dataanvändningen vid en viss tidpunkt för de 10 program som förbrukar mest bandbredd.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Visar detaljerade trafikmätvärden för varje program, däribland Download, Upload och Total Bandwidth. Sök efter program i sökfältet vid behov.

    Klicka på sorteringspilen bredvid kolumnrubriken för att sortera listan stigande eller fallande.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat.png){class="glboxshadow"}

### Data Storage Rules {#data-storage-rules}

1. Trafikstatistik sparas i RAM var 15:e sekund och i flashminnet varje timme. Täta skrivningar undviks för att skydda flashminnets livslängd.

2. En mjuk omstart orsakar ingen dataförlust. Systemet skriver först data från RAM till flashminnet före omstart.

3. En hård omstart eller firmwareuppgradering med behållna inställningar kan medföra förlust av data från den senaste timmen.

### Client Selector {#client-selector}

Med Client Selector kan du välja en viss klient eller behålla standardalternativet All clients. Diagrammet och statistiktabellen uppdateras automatiskt och visar endast trafikdata för vald enhet.

**Note**: This feature was introduced in firmware v4.11.

![client selector](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/client_selector.png){class="glboxshadow"}

### Switch Chart Views {#switch-chart-views}

Du kan byta diagramtyp efter behov när App Traffic Statistics visas.

**Note**: This feature was introduced in firmware v4.11.

![switch chart views](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/switch_chart_views.png){class="glboxshadow"}

- **Line chart**: Spårar bandbreddsanvändning under valt tidsintervall. Kontinuerliga kurvor visar trafikförändringar över tid och gör det enkelt att se stigande och fallande trender.

    ![Line chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/line_chart.png){class="glboxshadow"}

- **Bar chart**: Jämför programmens bandbreddsanvändning sida vid sida. Staplar visar tydligt vilka program som förbrukar mest bandbredd.

    ![Bar chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/bar_chart.png){class="glboxshadow"}

- **Pie chart**: Delar upp den totala bandbreddsanvändningen i procentandelar. Tårtbitar visar den relativa andelen trafik för varje program.

    ![pie chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/pie_chart.png){class="glboxshadow"}

### Switch Time Range {#switch-time-range}

Du kan växla tidsintervall mellan Past hour, Past day och Past week.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select-time-range.png){class="glboxshadow"}

Valt tidsintervall avgör hur data visas:

- **For a closer look (e.g., Past Hour)**: Diagrammet visar detaljerade variationer i realtid. Högre toppar och brantare fall gör plötsliga ökningar i bandbreddsanvändningen lätta att se.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-hour.png){class="glboxshadow"}

- **For a broad overview (e.g., Past Day or Past Week)**: The chart condenses the data into a longer timeline. The curves become smoother, showing the general traffic trend rather than every small change.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past-week.png){class="glboxshadow"}

### Clear Statistics {#clear-statistics}

Klicka på kvastikonen uppe till vänster för att rensa statistiken.

![clear data 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_1.png){class="glboxshadow"}

Efter rensningen uppdateras sidan enligt bilden nedan. Du kan behöva vänta en stund innan ny statistik börjar läsas in.

![clear data 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data_2.png){class="glboxshadow"}

## For firmware v4.9 to v4.10 {#for-firmware-v49-to-v410}

Toggle the switch in the upper right corner to view the **Application Total Data**.

![data statistics](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/data_stat.png){class="glboxshadow"}

Sidan består av två delar:

- **Top 10 Apps by Bandwidth Usage**: Visar ett tidsbaserat trenddiagram, till exempel för det senaste dygnet, över bandbreddsförbrukningen för de 10 främsta programmen under vald period.

    Håll pekaren över diagrammet för att visa dataanvändningen vid en viss tidpunkt för de 10 program som förbrukar mest bandbredd.

    ![top10 apps chart](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/top10_apps_chart.png){class="glboxshadow"}

- **App Traffic Statistics**: Visar detaljerade trafikmätvärden för varje program, däribland Download, Upload och Total Bandwidth. Sök efter program i sökfältet vid behov.

    Klicka på sorteringspilen bredvid kolumnrubriken för att sortera listan stigande eller fallande.

    ![app traffic stat](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/app_traffic_stat1.png){class="glboxshadow"}

### Data Storage Rules {#data-storage-rules_1}

1. Trafikstatistik sparas i RAM var 15:e sekund och i flashminnet varje timme. Täta skrivningar undviks för att skydda flashminnets livslängd.

2. En mjuk omstart orsakar ingen dataförlust. Systemet skriver först data från RAM till flashminnet före omstart.

3. En hård omstart eller firmwareuppgradering med behållna inställningar kan medföra förlust av data från den senaste timmen.

### Switch Time Range {#switch-time-range_1}

Du kan växla tidsintervall mellan Past hour, Past day och Past week.

![select time range](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/select_time_range.jpg){class="glboxshadow"}

Valt tidsintervall avgör hur data visas:

- **For a closer look (e.g., Past Hour)**: Diagrammet visar detaljerade variationer i realtid. Högre toppar och brantare fall gör plötsliga ökningar i bandbreddsanvändningen lätta att se.

    ![past hour](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_hour.png){class="glboxshadow"}

- **For a broad overview (e.g., Past Day or Past Week)**: The chart condenses the data into a longer timeline. The curves become smoother, showing the general traffic trend rather than every small change.

    ![past week](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/past_week.png){class="glboxshadow"}

### Clear Statistics {#clear-statistics_1}

Klicka på kvastikonen uppe till vänster för att rensa statistiken.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data1.png){class="glboxshadow"}

Efter rensningen uppdateras sidan enligt bilden nedan. Du kan behöva vänta en stund innan ny statistik börjar läsas in.

![clear data](https://static.gl-inet.com/docs/router/en/4/interface_guide/data_statistics/clear_data2.png){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
