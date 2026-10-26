# Je router herstellen met U-Boot {#using-uboot-to-unbrick-your-router}

Als je router door een eigen aanpassing of verkeerde firmware niet meer toegankelijk is, kun je de firmware opnieuw installeren via U-Boot failsafe.

**Opmerking:** bij de U-Boot-procedure worden de routerinstellingen en geïnstalleerde plug-ins verwijderd.

---

## Preparation {#preparation}

Gebruik een computer met een Ethernetpoort. Als deze ontbreekt, heb je een USB-Ethernetadapter nodig.

**Note**: GL-E5800 (Mudi 7) currently does not support firmware flashing via U-Boot.

## Unbrick Steps {#unbrick-steps}

Bekijk de video of volg de onderstaande procedure om de U-Boot Web UI te openen en de firmware opnieuw te installeren.

<iframe width="560" height="315" src="https://www.youtube.com/embed/pz0DidfIXRk" title="YouTube-videospeler" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<small>De stappen voor herinstallatie via U-Boot zijn vrijwel gelijk. De video gebruikt Mudi/Mudi V2 als voorbeeld. Volg voor andere modellen de onderstaande procedure.</small>

1. Download U-Boot firmware [here](https://dl.gl-inet.com/){target="_blank"} to your computer.

    Sommige modellen hebben twee firmwarevarianten. Download de firmware die compatibel is met U-Boot.

2. Schakel de router uit. Sluit een computer aan op de **Ethernet LAN port** en laat alle andere poorten ongebruikt.

    !!! note

        Bij sommige modellen kan één LAN-poort als WAN worden gebruikt. Gebruik die poort niet voor de firmware-installatie. Gebruik op GL-MT6000 (Flint 2) bijvoorbeeld LAN 2, LAN 3 of LAN 4 in plaats van LAN 1.

3. Houd de Reset-knop stevig ingedrukt terwijl je **tegelijk de router inschakelt**. Zonder aan-uitknop wordt de router automatisch ingeschakeld wanneer je de voeding aansluit.

    Wacht tot de led enkele keren in een vast patroon knippert. Laat de Reset-knop pas los **nadat** het patroon verandert.

    !!! note "LED Flashing Patterns by Device Model"

        **Opmerking:** hetzelfde routermodel kan per productiebatch andere ledkleuren of knipperpatronen hebben. Dit beïnvloedt U-Boot-herstel niet. Let op de verandering van het knipperpatroon.

        - Voor **GL-MT6000 (Fortify)**: de blauwe led knippert 6 keer en brandt daarna continu wit.

        - Voor **GL-MG1300 (Mango 2)**: de blauwe led knippert 7 keer en brandt daarna continu wit.

        - Voor **GL-BE14000 (Flint 4), GL-BE10000 (Slate 7 Pro) en GL-BE3600 (Slate 7)**: nadat je Reset ongeveer 5 seconden ingedrukt houdt, verschijnt op het touchscreen een aftelling van 5 seconden. Blijf drukken tot de volgende melding verschijnt, bijvoorbeeld om het IP-adres van je computer handmatig in te stellen op 192.168.1.2 en http://192.168.1.1 in een browser te openen. Ga verder met stap 4.

        - Voor **GL-MT3600BE (Beryl 7)**: de blauwe led knippert 7 keer en brandt daarna continu wit.

        - Voor **GL-MT5000 (Brume 3)**: de Power-led knippert 7 keer blauw en brandt daarna continu wit.

        - Voor **GL-BE6500 (Flint 3e)**: de blauwe led knippert 6 keer en brandt daarna continu wit.

        - Voor **GL-BE9300 (Flint 3)**: de blauwe led knippert 6 keer en brandt daarna continu wit.

        - Voor **GL-X2000 (Spitz Plus)**: de Internet-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - Voor **GL-B3000 (Marble)**: de blauwe led knippert 7 keer en brandt daarna continu wit.

        - Voor **GL-MT6000 (Flint 2)**: de blauwe led knippert 6 keer en brandt daarna continu wit.

        - Voor **GL-MT3000 (Beryl AX)**: de blauwe led knippert 6 keer en brandt daarna continu wit.

        - Voor **GL-MT2500/GL-MT2500A (Brume 2)**: de Power-led knippert 5 keer blauw en brandt daarna continu wit.

        - Voor **GL-X3000 (Spitz AX)**: de Internet-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - Voor **GL-XE3000 (Puli AX)**: de Internet-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - Voor **GL-XE300 (Puli)**: de LAN-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - For **GL-E750 (Mudi)**: Its screen will first display "Booting", followed by "Reset Counting 1 to 4", and finally "Please Open Web 192.168.1.1".

        - Voor **GL-X750 (Spitz)**: de Internet-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - Voor **GL-AX1800 (Flint)**: de blauwe led knippert 5 keer en brandt daarna continu wit.

        - Voor **GL-AXT1800 (Slate AX)**: de blauwe led knippert 5 keer en brandt daarna continu wit.

        - Voor **GL-SFT1200 (Opal)**: de blauwe led knippert 5 keer en brandt daarna continu wit.

        - Voor **GL-MT1300 (Beryl)**: de blauwe led knippert 2 keer langzaam, daarna 5 keer sneller en brandt vervolgens continu wit.

        - Voor **GL-A1300 (Slate Plus)**: de led knippert 5 keer langzaam, blijft kort branden en knippert daarna continu snel.

        - For **GL-MT300N-V2 (Mango)** and **GL-AR300M (Shadow)**: The LED flashes 5 times.

        - Voor **GL-X300B (Collie)**: de WAN-led knippert 5 keer en daarna blijft de Wi-Fi-led branden.

        - Voor **GL-AP1300 (Cirrus)**: de Power-led knippert 5 keer langzaam, blijft kort branden en knippert daarna continu snel.

        - For **GL-B1300 (Convexa-B)** and **GL-S1300 (Convexa-S, EOL)**: The LED flashes 4 times.

            De linker Power-led blijft branden terwijl de rechter Wi-Fi-led 4 keer knippert. Daarna gaat de middelste Mesh-led continu branden.

            (Bij sommige oudere GL-B1300-modellen blijft de linker Power-led branden en knipperen de middelste en rechter led gelijktijdig 5 keer, waarna ze blijven branden.)

        - Voor **GL-B2200 (Velica)**: de twee leds zijn eerst blauw, worden wit en knipperen 5 keer, en branden daarna continu blauw.

        - Voor **GL-SF1200**: de 5G-led knippert 5 keer en blijft daarna branden.

        - Voor **GL-S200**: de cyaankleurige led knippert 5 keer, wordt kort paars en brandt daarna continu cyaan.

        - For **GL-AR750 (Creta)** and **GL-AR750S-EXT (Slate)**: The LED flashes 5 times.

        - For **GL-USB150 (Microuter)**, **microuter-N300** and **GL-AR150 (White)**: The LED flashes 5 times.

        - Voor **GL-MV1000/GL-MV1000W (Brume)**: er is geen herhaald knippersignaal. De Power- en WAN-led blijven continu branden.

        - For **GL-MiFi**: The LED flashes 6 times.

        - For **GL-MT300N** and **GL-MT300A**: The LED flashes 3 times.

4. Stel het IP-adres van je computer handmatig in op **192.168.1.2**. Volg hieronder de stappen voor je besturingssysteem:

    ??? "Windows 7 / Windows 10"

        1. Go to **Control Panel** -> **Network and Internet** -> **Network and Sharing Center** -> **Change adapter settings**.

        2. Right click **Local Area Connection** -> **Properties**.

        3. Click **Internet Protocol Version 4 (TCP/IPv4)** -> **Properties**.

        4. Set the **IP address** to `192.168.1.2` manually.

        5. Set the **Subnet mask** to `255.255.255.0`.

            ![ipv4 properties](https://static.gl-inet.com/docs/router/en/4/faq/debrick/set_ip.jpg){class="glboxshadow"}

        6. Click the **OK** button.

    ??? "Windows 11"

        1. Open Settings.

        2. Klik op **Network & Internet**.

        3. Klik op het tabblad **Ethernet**.

            ![windows 11 ethernet](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windwos11_ethernet.png){class="glboxshadow"}

        4. Klik onder "IP assignment" op **Edit**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_ip_assignment_edit.png){class="glboxshadow"}

        5. Select the **Manual** option.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_edit_ip_settings.png){class="glboxshadow"}

        6. Turn on the **IPv4 toggle** switch.

        7. Set the static **IP address** as **192.168.1.2**.

            ![windows 11 ethernet edit](https://static.gl-inet.com/docs/router/en/4/faq/debrick/windows11_ethernet_edit_ip_settings_2.png){class="glboxshadow"}

        8. Specify the **Subnet mask** as **255.255.255.0**.

        9. Click the **Save** button.

    ??? "macOS"

        1. Klik linksboven op het **Apple**-pictogram en selecteer **System Preferences**.

            ![macos system preferences](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_system_preferences.png){class="glboxshadow"}

        2. Click **Network**.

            ![macos system preferences network](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_system_preferences_network.png){class="glboxshadow"}

        3. Klik links op **Ethernet**, open de keuzelijst naast **Configure IPv4** en selecteer **Manually**. Bij een USB-Ethernetadapter kan de interface onder de naam van de adapter verschijnen.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_ip_manually_1.png){class="glboxshadow"}

        4. Stel **IPv4 Address** in op `192.168.1.2`, **Subnet Mask** op `255.255.255.0` en **Router** op `192.168.1.1`. Klik daarna rechtsonder op Apply.

            ![macos ip manually](https://static.gl-inet.com/docs/router/en/4/faq/debrick/macos_ip_manually_2.png){class="glboxshadow"}

5. Open **http://192.168.1.1** in je webbrowser. Dit is de U-Boot Web UI.

    ![Uboot web ui](https://static.gl-inet.com/docs/router/en/4/faq/debrick/uboot_ui.png){class="glboxshadow" width="700"}

    !!! Note

        - Als de U-Boot Web UI niet opent, controleer je of VPN- of proxysoftware actief is. Schakel deze uit, inclusief Tailscale en ZeroTier.

        - De U-Boot Web UI kan door verschillen in productiedatum en U-Boot-versie afwijken. In uitzonderlijke gevallen raden we een U-Boot-upgrade aan. Raadpleeg [deze handleiding](upgrade_uboot_version.md).

6. Klik op **Choose file**, selecteer het firmwarebestand en klik op **Update firmware**.

7. Wacht ongeveer 3 minuten. Schakel het apparaat tijdens de firmware-update niet uit.

    De router is gereed wanneer de led blauw blijft knipperen. Bij sommige mobiele modellen zijn zowel de Power- als Wi-Fi-led continu aan.

8. Zet de IP-instellingen uit stap 4 terug en verbind je computer met LAN of wifi van de router. Je kunt het webbeheerpaneel weer via **192.168.8.1** openen.

    **Opmerking:** mogelijk moet je de incognitomodus gebruiken of de browsercache en cookies verwijderen om de router te openen.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
