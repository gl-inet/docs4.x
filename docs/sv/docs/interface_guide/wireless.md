# Wireless {#wireless}

Innehållet bygger på firmware v4.9 och senare. Om enheten kör en annan version använder du väljaren nedan.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.9 and above" markdown="1">

- [Firmware v4.8 and earlier](wireless_v4.8.md)

</div>

---

Öppna **WIRELESS** på vänster sida i webbadministrationspanelen.

På sidan Wireless konfigurerar du MLO Wi-Fi (utvalda modeller), Main Network, Guest Network och IoT Network. Band som stöds varierar efter modell.

## Multi-Link Operation (MLO) {#multi-link-operation-mlo}

??? "Supported Models"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Unsupported Models"
    - GL-MT6000 (Fortify)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

MLO (Multi-Link Operation) är en central Wi-Fi 7-funktion (802.11be) som använder flera band samtidigt för högre prestanda, lägre latens och stabilare anslutning.

Wi-Fi 7-klienter rekommenderas att använda MLO Wi-Fi för högre kapacitet och tillförlitlighet.

Klicka på **Add** för MLO Wi-Fi och sedan på **Apply**. Tillgängliga band varierar efter modell.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: Select at least two radio bands.
- Wi-Fi Security: Om 6 GHz väljs är WPA3-SAE det enda och rekommenderade alternativet.
- Enable Randomized BSSID: När 6 GHz väljs synkroniseras MLO Wi-Fi BSSID med Main Wi-Fi.

Once enabled, the page appears as shown below.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Main Network {#main-network}

Main Network är det primära Wi-Fi-nätverket och sänder samtidigt på flera band. Inställningar som SSID, säkerhetsläge, lösenord, slumpmässig BSSID, TX-effekt, bandbredd och kanal kan anges separat.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

Klicka på kugghjulet till höger för att visa eller ändra bandinställningar.

**Note**: The available Wi-Fi bands vary by model.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Guest Network {#guest-network}

Guest Network är ett Wi-Fi-nätverk för besökare med alla band inaktiverade som standard. Du kan konfigurera SSID, säkerhetsläge, lösenord och slumpmässig BSSID.

Klicka på **Add** för Guest Wi-Fi och sedan på **Apply**.

**Note**: The available Wi-Fi bands vary by model.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

Once enabled, the page appears as shown below.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## IoT Network {#iot-network}

IoT Network är ett Wi-Fi-nätverk för smarta enheter med alla band inaktiverade som standard. Du kan konfigurera SSID, säkerhetsläge, lösenord och slumpmässig BSSID.

Klicka på **Add** för IoT Wi-Fi och sedan på **Apply**.

**Obs!** IoT Network omfattar inte 6 GHz. Tillgängliga band varierar efter modell.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

Once enabled, the page appears as shown below.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"}.
