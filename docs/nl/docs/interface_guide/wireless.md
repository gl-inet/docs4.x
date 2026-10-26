# Wireless {#wireless}

De inhoud van deze pagina is gebaseerd op firmwareversie v4.9 en hoger. Als je apparaat een andere firmwareversie gebruikt, selecteer je hieronder de bijbehorende handleiding.

<div class="gl-link-select" data-label="Firmwareversie" data-placeholder="Firmware v4.9 en hoger" markdown="1">

- [Firmware v4.8 en ouder](wireless_v4.8.md)

</div>

---

Ga links in het webbeheerpaneel naar **WIRELESS**.

Op de pagina Wireless kun je verschillende Wi-Fi-netwerken configureren, waaronder MLO Wi-Fi op bepaalde modellen, Main Network, Guest Network en IoT Network. De ondersteunde banden verschillen per model.

## Multi-Link Operation (MLO) {#multi-link-operation-mlo}

??? "Ondersteunde modellen"
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)

??? "Niet-ondersteunde modellen"
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

MLO (Multi-Link Operation) is een kernfunctie van Wi-Fi 7 (802.11be) die netwerkprestaties verbetert, latentie verlaagt en verbindingen stabiliseert door meerdere frequentiebanden tegelijk te gebruiken, zoals 2.4 GHz, 5 GHz en 6 GHz.

We raden aan Wi-Fi 7-clients met MLO Wi-Fi te verbinden voor een veel hogere doorvoer en betrouwbaarheid via meerdere banden.

Klik op **Add** om een MLO Wi-Fi-netwerk in te stellen en klik op **Apply**. De beschikbare banden verschillen per model.

![mlo1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo1.png){class="glboxshadow"}

![mlo2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo2.png){class="glboxshadow"}

- Wi-Fi Band: selecteer ten minste twee radiobanden.
- Wi-Fi Security: als de 6 GHz-band is geselecteerd, is WPA3-SAE de enige beschikbare en aanbevolen optie. Deze werkt het best met de meeste MLO-apparaten.
- Enable Randomized BSSID: wanneer de 6 GHz-band is geselecteerd, wordt de 6 GHz-BSSID van MLO Wi-Fi met Main Wi-Fi gesynchroniseerd.

Na inschakeling ziet de pagina er als volgt uit.

![mlo3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/mlo3.png){class="glboxshadow"}

## Main Network {#main-network}

Main Network is je primaire Wi-Fi-netwerk en zendt tegelijk op verschillende banden uit, die standaard allemaal zijn ingeschakeld. Je kunt per band de Wi-Fi-SSID, beveiligingsmodus, het wachtwoord, willekeurige BSSID, TX-vermogen, bandbreedte en kanaal configureren.

![main](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main.png){class="glboxshadow"}

Klik rechts op het tandwielpictogram om de Wi-Fi-instellingen per band te bekijken of wijzigen.

**Opmerking**: de beschikbare Wi-Fi-banden verschillen per model.

- 6 GHz

    ![main 6g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_6g.png){class="glboxshadow"}

- 5 GHz

    ![main 5g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_5g.png){class="glboxshadow"}

- 2.4 GHz

    ![main 2.4g](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/main_2.4g.png){class="glboxshadow"}

## Guest Network {#guest-network}

Guest Network is een speciaal Wi-Fi-netwerk voor bezoekers waarvan alle banden standaard zijn uitgeschakeld. Je kunt per band de Wi-Fi-SSID, beveiligingsmodus, het wachtwoord en een willekeurige BSSID configureren.

Klik op **Add** om een Guest Wi-Fi-netwerk in te stellen en klik op **Apply**.

**Opmerking**: de beschikbare Wi-Fi-banden verschillen per model.

![guest1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest1.png){class="glboxshadow"}

![guest2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest2.png){class="glboxshadow"}

Na inschakeling ziet de pagina er als volgt uit.

![guest3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/guest3.png){class="glboxshadow"}

## IoT Network {#iot-network}

IoT Network is een speciaal Wi-Fi-netwerk voor slimme apparaten waarvan alle banden standaard zijn uitgeschakeld. Je kunt per band de Wi-Fi-SSID, beveiligingsmodus, het wachtwoord en een willekeurige BSSID configureren.

Klik op **Add** om een IoT Wi-Fi-netwerk in te stellen en klik op **Apply**.

**Opmerking**: IoT Network bevat geen 6 GHz-band. De beschikbare Wi-Fi-banden verschillen per model.

![iot1](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot1.png){class="glboxshadow"}

![iot2](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot2.png){class="glboxshadow"}

Na inschakeling ziet de pagina er als volgt uit.

![iot3](https://static.gl-inet.com/docs/router/en/4/interface_guide/wireless_v4.9/iot3.png){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"}.
