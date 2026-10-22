# Wireless (firmware v4.8 och tidigare) {#wireless-firmware-v48-and-earlier}

Innehållet bygger på firmware v4.8.x och tidigare. Använd väljaren för en annan version.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.8 and earlier" markdown="1">

- [Firmware v4.9 and above](wireless.md)

</div>

---

Öppna **WIRELESS**.

På sidan Wireless konfigurerar du separata nätverk på 2.4 GHz, 5 GHz, 6 GHz och MLO Wi-Fi. Varje band kan vara Main Wi‑Fi eller Guest Wi‑Fi.

**Obs!** GL-MT300N-V2, GL-X300B och GL-XE300 stöder inte 5 GHz. GL-MT5000 och GL-MT2500/GL-MT2500A saknar Wi‑Fi.

## MLO Wi-Fi {#mlo-wi-fi}

| Supported Models               |           |
| :----------------------------- | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)       | √         |
| Beryl 7 (GL-MT3600BE)          | √         |
| Flint 3e (GL-BE6500)           | √         |
| Flint 3 (GL-BE9300)            | √         |
| Slate 7 (GL-BE3600)            | √         |

MLO (Multi-Link Operation) är en central Wi-Fi 7-funktion som använder flera band samtidigt för högre prestanda, lägre latens och stabilare anslutning.

Klicka på flikarna nedan för inställningar för MLO Main Wi-Fi och MLO Guest Wi-Fi.

=== "MLO Wi-Fi"

    MLO Main Wi-Fi konfigurerar Wi-Fi, minst två band, slumpmässig BSSID, SSID, säkerhet, lösenord och SSID-synlighet.

    ![MLO Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_mlo.png){class="glboxshadow"}

    - Om MLO omfattar 6 GHz synkroniseras MLO BSSID när 6GHz BSSID ändras.

    - WPA3-SAE är standard för MLO och passar de flesta MLO-enheter.

=== "MLO Guest Wi-Fi"

    MLO Guest Wi-Fi konfigurerar Wi-Fi, minst två band, SSID, säkerhet, lösenord och synlighet.

    ![MLO Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_mlo.png){class="glboxshadow"}

## 6 GHz Wi-Fi {#6-ghz-wi-fi}

| Supported Models               |           |
| :----------------------------- | :-------: |
| Flint 4 (GL-BE14000)           | √         |
| Slate 7 Pro (GL-BE10000)       | √         |
| Mudi 7 (GL-E5800)              | √         |
| Flint 3 (GL-BE9300)            | √         |

6 GHz Wi-Fi ger snabbare och stabilare anslutning med mindre överbelastning än 2.4 GHz och 5 GHz.

Klicka på flikarna för inställningar för 6 GHz Main Wi-Fi och Guest Wi-Fi.

=== "6 GHz Wi-Fi"

    6 GHz Main Wi-Fi konfigurerar Wi-Fi, TX-effekt, slumpmässig BSSID, SSID, säkerhet, lösenord, synlighet, läge, bandbredd och kanal.

    ![6G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_6g.png){class="glboxshadow"}

    - Enable PSC: PSC (Preferred Scanning Channel) reserverar kanaler med bättre anslutning för 6 GHz-enheter.

=== "6 GHz Guest Wi-Fi"

    6 GHz Guest Wi-Fi konfigurerar Wi-Fi, SSID, säkerhet, lösenord och synlighet.

    ![6G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_6g.png){class="glboxshadow"}

## 5 GHz Wi-Fi {#5-ghz-wi-fi}

Klicka på flikarna för inställningar för 5 GHz Main Wi-Fi och Guest Wi-Fi.

=== "5 GHz Wi-Fi"

    5 GHz Main Wi-Fi konfigurerar Wi-Fi, TX-effekt, slumpmässig BSSID, SSID, säkerhet, lösenord, synlighet, läge, bandbredd och kanal.

    ![5G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_5g.jpg){class="glboxshadow"}

=== "5 GHz Guest Wi-Fi"

    5 GHz Guest Wi-Fi konfigurerar Wi-Fi, SSID, säkerhet, lösenord och synlighet.

    ![5G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_5g.png){class="glboxshadow"}

## 2.4 GHz Wi-Fi {#24-ghz-wi-fi}

Klicka på flikarna för inställningar för 2.4 GHz Main Wi-Fi och Guest Wi-Fi.

=== "2.4 GHz Wi-Fi"

    2.4 GHz Main Wi-Fi konfigurerar Wi-Fi, TX-effekt, slumpmässig BSSID, SSID, säkerhet, lösenord, synlighet, läge, bandbredd och kanal.

    ![2.4G Main Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/main_wifi_2.4g.png){class="glboxshadow"}

=== "2.4 GHz Guest Wi-Fi"

    2.4 GHz Guest Wi-Fi konfigurerar Wi-Fi, SSID, säkerhet, lösenord och synlighet.

    ![2.4G Guest Wi-Fi](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/guest_wifi_2.4g.png){class="glboxshadow"}

## General Wi-Fi Settings {#general-wi-fi-settings}

* Håll pekaren över QR-kodikonen bredvid SSID för att visa Wi-Fi-QR-koden och skanna den med telefon eller surfplatta.

    ![wifi qr code](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/wifi_ssid_qr_code.png){class="glboxshadow"}

* **Randomized BSSID**: Aktiverat som standard och förhindrar spårning via fast BSSID. Se [Randomized BSSID](#randomized-bssid).

* **Bandwidth** och **Channel** kan inte ändras i [Repeater](internet_repeater.md) eftersom de följer det upprepade nätverket.

* Med **Channel** på **Auto** växlar Wi-Fi inte automatiskt till DFS-kanal.

* Vid byte från kanal utan DFS till DFS visas följande varning.

    ![dfs channel caution](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/switch_to_dfs_caution.png){class="glboxshadow"}

* Med **Bandwidth** på **160 MHz** används alltid DFS-kanal, även om Channel är Auto eller en kanal utan DFS.

## Randomized BSSID {#randomized-bssid}

Randomized BSSID är en integritetsfunktion från firmware v4.6 som förhindrar lokalisering och spårning via fast Wi-Fi BSSID.

**Why a fixed BSSID is a privacy risk**

Mobile operating systems (e.g., Android and iOS) rely on crowd-sourced Wi-Fi positioning to provide location services:

1. Klientenheter laddar regelbundet upp synliga BSSID och GPS-baserad plats till operativsystems- eller enhetsleverantören.

2. Vendors aggregate this data into a global BSSID-to-location database.

3. Enheter med Wi-Fi kan även utan GPS uppskatta sin plats via omgivande BSSID i databasen.

![randomized bssid](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless/randomized-bssid-new.jpg){class="glboxshadow"}

En router med fast BSSID fungerar därför som en platsfyr och kan lokaliseras och spåras över tid. Angripare kan använda databaserna för att hitta eller identifiera routrar via leverantörsinformation (OUI).

**How Randomized BSSID protects you**

När funktionen är aktiverad genererar routern ett nytt slumpmässigt BSSID vid varje start. Det kan då inte kopplas till en fast plats i leverantörsdatabaser.

| Status | Behavior |
| ----------------- | ---------------------- |
| Enabled (default) | A new random BSSID is generated and renewed at each boot |
| Disabled | The router uses its real factory MAC address as the BSSID |

**Notes**:

1. BSSID ändras endast när routern startas om och är oförändrat under sessionen.
2. Guest Wi-Fi BSSID motsvarar Main Wi-Fi BSSID på samma band.
3. Om MLO omfattar 6 GHz synkroniseras MLO BSSID med 6 GHz BSSID.
4. Randomized BSSID förhindrar spårning via routerns BSSID men hindrar inte klienter från att rapportera sin plats. SSID, kanal och signalegenskaper kan fortfarande observeras.

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
