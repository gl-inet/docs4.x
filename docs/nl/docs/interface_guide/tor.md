# Tor {#tor}

Tor, afgeleid van **The Onion Router**, is gratis opensourcesoftware voor anonieme communicatie en meer privacy op internet. [Lees meer over Tor](https://www.torproject.org/){target="_blank"}.

**Opmerking**: deze functie is momenteel in bèta en kan in sommige landen problemen veroorzaken. Wanneer Tor is ingeschakeld, werken de volgende functies niet goed:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"

    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MT3600BE (Beryl 7)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-AP1300 (Cirrus)
    - GL-S1300 (Convexa-S)
    - *GL-SFT1200 (Opal)
    - *GL-MT1300 (Beryl)
    - *GL-E750/E750V2 (Mudi)

    **Opmerking**: modellen met * ondersteunen Tor niet standaard, maar je kunt Tor handmatig via een plug-in installeren. Klik [hier](#manual-install) voor meer informatie.

??? "Niet-ondersteunde modellen"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Snelle installatie {#quick-setup}

Ga links in het webbeheerpaneel naar **VPN** -> **Tor**.

Ga in firmware v4.8.4 en hoger naar **APPLICATIONS** -> **Tor**.

Zet de schakelaar om om Tor in te schakelen, schakel zo nodig **Custom Exit Nodes** in en klik op **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/enable_tor.png){class="glboxshadow"}

Tor begint verbinding te maken. Als je netwerk aan de vereisten voldoet, verschijnt de status verbonden.

![tor connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/connected.png){class="glboxshadow" width="672"}

## Handmatig installeren {#manual-install}

**Opmerking**: op sommige modellen kan Tor handmatig via een plug-in worden geïnstalleerd. Dit kan de CPU-belasting verhogen en de systeemrespons vertragen.

Ga links in het webbeheerpaneel naar **APPLICATIONS** -> **Plug-ins**.

Zoek naar **gl-sdk4-ui-torview** en installeer het.

![torview](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torpage.jpg){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
