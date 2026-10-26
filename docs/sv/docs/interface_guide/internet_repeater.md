# Anslut till internet via ett befintligt Wi-Fi-nätverk med Repeater {#connect-to-the-internet-via-an-existing-wi-fi-by-repeater}

<iframe width="560" height="315" src="https://www.youtube.com/embed/7mZtz8u8--E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Repeater ansluter routern till ett befintligt trådlöst nätverk, till exempel kostnadsfritt Wi-Fi på ett hotell eller kafé.

Som standard används WISP-läge (Wireless Internet Service Provider). Routern skapar då ett eget subnät och fungerar som brandvägg mot det offentliga nätverket.

## Basic Steps {#basic-steps}

Log in to the router's web admin panel, navigate to **INTERNET** -> **Repeater** section, and click **Connect**.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

Välj Wi-Fi-nätverket som du vill ansluta till i listan över tillgängliga nätverk.

![join wifi 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_1.png){class="glboxshadow"}

!!! note

    1. Sidan visar Wi-Fi-kanalerna som routern stöder. Kontrollera att nätverket använder en av dessa kanaler, annars kanske det inte visas i listan.

    2. Håll iPhone-skärmen upplåst när du söker efter iPhone Personal Hotspot så att Wi-Fi-signalen sänds kontinuerligt. Annars kanske routern inte hittar hotspoten.

Ange rätt Wi-Fi-lösenord och klicka på **Apply**.

![join wifi 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_wifi_2.png){class="glboxshadow"}

Om önskat Wi-Fi SSID inte finns i Available Network klickar du på **Join Other Network** uppe till höger och anger SSID och övriga uppgifter manuellt. Detaljerade steg finns [här](#join-other-network).

![join other network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

For connecting to a public hotspot, such as those provided by hotels/airports/malls, please refer to  [For Public Hotspot](#for-public-hotspot).

For other settings, please refer to [Advanced Settings](#advanced-settings).

Om lösenordet är korrekt upprättas anslutningen efter en stund.

![repeater connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

## For Public Hotspot {#for-public-hotspot}

När routern ansluts till en offentlig hotspot med captive portal kan följande funktioner förbättra anslutningsresultatet.

![repeater settings for public hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_settings_for_public_hotspot.png){class="glboxshadow"}

- **Auto-Enable Login Mode for Public Hotspots**

    This feature is available since v4.6

    När alternativet är aktiverat går routern automatiskt in i Login Mode for Public Hotspots om den ansluter till en hotspot men inte till internet. **Vissa tjänster pausas och DNS-läget ändras till automatiskt**, vilket kan röja nätverksaktivitet för hotspotleverantören.

    Även om alternativet är inaktiverat uppmanar routern dig att använda läget när den upptäcker en captive portal och inloggningen misslyckas.

    ![login mode for public hotspots](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/login_mode_for_public_hotspots.png){class="glboxshadow"}

- **Enable Camouflage**

    När alternativet är aktiverat imiterar routern klientenheten som används för administratörspanelen genom att efterlikna dess MAC-adress.

- **MAC Mode**

    Du kan välja vilken MAC-adress routern använder för den offentliga hotspoten.

    - **Factory**: Uses the device's original factory-assigned MAC address.

    - **Clone**: Klonar en klientenhets MAC-adress. Om adressen saknas i listan anger du den manuellt.

        **Obs!** Många moderna enheter använder slumpmässiga MAC-adresser, ofta kallade Private Wi-Fi Address eller random hardware address. Adressen som visas här kanske därför inte motsvarar enhetens fysiska MAC-adress.

    - **Random**: Automatically generates a random MAC address for connection.

    När nätverkskonfigurationen sparas kopplas MAC Mode, inklusive klonad eller slumpmässig adress, till det aktuella SSID:t. Inställningarna kan ändras manuellt för varje SSID.

- **Auto Update MAC**: När alternativet är aktiverat kan MAC-adressen uppdateras automatiskt.

## Advanced Settings {#advanced-settings}

Fler alternativ finns när du ansluter till nätverket.

![advanced settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_advanced_settings.png){class="glboxshadow"}

* **Remember**: Aktivera för att komma ihåg aktuellt repeateranslutet Wi-Fi-nätverk.

* **Lock BSSID**: Routern ansluter endast till åtkomstpunkten som motsvarar valt BSSID, även om andra åtkomstpunkter har samma SSID.

* **Manually Set Static IP**: Konfigurera en fast IPv4-adress, nätmask, gateway och DNS-servrar manuellt för repeateranslutningen i stället för automatisk hämtning.

    ![set static ip](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manually_set_static_ip.png){class="glboxshadow"}

* **TTL**: TTL (Time To Live) anger den maximala tiden för paket i nätverket och fylls i enligt operatörens krav. Som standard vidarebefordrar routern klientenhetens inkommande TTL minus ett. TTL gäller endast IPv4.

    **Obs!** För kamouflering kan du ange ett fast värde. På de flesta modeller anger du önskad effektiv TTL plus 1. Mudi 7 (GL‑E5800) använder värdet utan ändring.

* **HL**: I IPv6 begränsar HL (Hop Limit) antalet överföringshopp för datapaket och motsvarar TTL i IPv4.

* **MTU**: The default value is 1500.

## Repeater Options {#repeater-options}

Klicka på kugghjulsikonen uppe till höger för att konfigurera Repeater-alternativ.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

The page may vary due to different firmware versions.

![repeater options](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_options.png){class="glboxshadow"}

* **Allow Switching to Other Saved Networks**: Routern ansluter automatiskt till andra sparade nätverk när aktuellt Wi-Fi-nätverk inte är tillgängligt.

* **Band Selection**: Om du väljer ett band manuellt söker routern endast efter nätverk på detta frekvensband.

## Manage Known Network {#manage-known-network}

To manage known networks, click **Switch Network**.

![switch network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_connected.png){class="glboxshadow"}

Du kan även klicka på **Connect** i avsnittet Repeater om inget nätverk är anslutet.

![repeater section](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/repeater_section.png){class="glboxshadow"}

I **Known Networks** klickar du på papperskorgsikonen för att radera ett nätverk eller kugghjulet för att konfigurera det.

![manage known network](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/manage_known_networks.png){class="glboxshadow"}

## Join Other Network {#join-other-network}

Om SSID saknas i Available Networks eller är dolt klickar du på **Join Other Network**.

![join other network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_1.png){class="glboxshadow"}

Ange SSID, välj Security och ange lösenordet vid behov.

![join other network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_2.png){class="glboxshadow"}

För **Security** finns två eller tre alternativ beroende på modell.

* None, which means no password is required.
* WPA/WPA2/WPA3, som är vanligt och stöds av nästan alla Wi-Fi-nätverk.
* WPA/WPA2/WPA3 Enterprise, som kräver Extensible Authentication Protocol (EAP). Ett giltigt användarnamn och lösenord krävs, vanligen i företags- eller campusnätverk.

    ![join other network, eap](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/join_other_network_eap.jpg){class="glboxshadow"}

    En detaljerad guide för EAP-nätverk finns [här](../tutorials/eap.md){target="_blank"}.

## Reconnection {#reconnection}

I följande fall försöker routern regelbundet återansluta till Wi-Fi. Det kan inaktiveras manuellt. Vid SSID- eller lösenordsfel tar du bort nätverket från Known Networks.

1. Incorrect SSID/password entered during Repeater setup.

2. Routern har flyttats utanför den uppströms routerns räckvidd efter första anslutningen.

3. Upstream router changes SSID/password or restricts access post-connection.

Återanslutningen har tre faser: väntan, sökning och anslutning.

1. Waiting Phase: No issues - router waits for reconnection conditions.

2. Scanning Phase: Packet loss may occur on the scanned frequency band. New devices might face connection problems. For models GL-AXT1800/GL-AX1800, Guest Wi-Fi will be temporarily disabled.

3. Connecting Phase: Main Wi-Fi on the target band may drop for a few seconds during re-establishment.

**Obs!** Problem uppstår vanligtvis under söknings- och anslutningsfaserna.

## Troubleshooting {#troubleshooting}

När routern är ansluten som repeater men internet saknas visas ett gult meddelande enligt nedan.

**"The interface is connected, but the Internet can't be accessed."**

![connect but no internet](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_repeater/interface_connected_no_internet.png){class="glboxshadow"}

To fix this issue:

1. Kontrollera att det uppströms Wi-Fi-nätverket har internetåtkomst.

2. Go to [Multi-WAN](multi-wan.md) page to check the repeater interface status.

## DFS {#dfs}

**DFS** (Dynamic Frequency Selection) växlar automatiskt Wi-Fi-kanal för att undvika radarstörningar. Vid anslutning till uppströms 5G Wi-Fi följer routern dess användning av DFS-kanal.

* Om uppströms Wi-Fi använder en sökbar DFS-kanal använder routerns 5G Wi-Fi samma kanal.

* Routerns 5G Wi-Fi växlar till en kanal utan DFS om det uppströms nätverket inte kan hittas eller anslutningen misslyckas.

??? "Supported Models"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)

??? "Unsupported Models"

    - GL-MT5000 (Brume 3)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-AR750 (Creta)
    - GL-AR300M Series (Shadow)
    - GL-MT300N-V2 (Mango)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-X300B (Collie)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-AP1300 (Cirrus)
    - GL-MV1000/GL-MV1000W (Brume)

---

Related Articles

- [Internet page](internet.md)
- [Ange prioriteten för varje internetanslutningsmetod](multi-wan.md)
- [Ange lastbalansering när flera internetanslutningsmetoder används samtidigt](multi-wan.md)
- [Hitta LAN- och Wi-Fi-MAC-adresser](../faq/how_can_i_know_the_lan_wifi_mac.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
