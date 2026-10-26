# Tor {#tor}

Tor (från **The Onion Router**) är kostnadsfri programvara med öppen källkod för anonym kommunikation och privat internetanvändning. [Läs mer om Tor](https://www.torproject.org/){target="_blank"}.

**Obs!** Funktionen är i betaversion och kan ha problem i vissa länder. När Tor är aktiverat fungerar följande funktioner inte korrekt:

  - VPN
  - DNS
  - IPv6
  - ADGuard Home.

## Supported models {#supported-models}

??? "Supported Models"

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

    **Obs!** Modeller markerade med * har inte inbyggt Tor-stöd, men Tor kan installeras manuellt via ett insticksprogram. Klicka [här](#manual-install) för mer information.

??? "Unsupported Models"
    - GL-MG1300 (Mango 2)
    - GL-X2000 (Spitz Plus)
    - GL-AR750S (Slate)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Quick Setup {#quick-setup}

Öppna **VPN** -> **Tor** på vänster sida i webbadministrationspanelen.

For firmware v4.8.4 and later, go to **APPLICATIONS** -> **Tor**.

Aktivera med reglaget, aktivera **Custom Exit Nodes** vid behov och klicka på **Apply**.

![enable tor](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/enable_tor.png){class="glboxshadow"}

Anslutningen startar. Om nätverket uppfyller kraven visas ansluten status.

![tor connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/connected.png){class="glboxshadow" width="672"}

## Manual Install {#manual-install}

**Obs!** På vissa modeller kan Tor installeras manuellt via insticksprogram, men det kan öka processorbelastningen och göra systemet långsammare.

Öppna **APPLICATIONS** -> **Plug-ins** på vänster sida i webbadministrationspanelen.

Search **gl-sdk4-ui-torview** and install.

![torview](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torview.jpg){class="glboxshadow"}

![torpage](https://static.gl-inet.com/docs/router/en/4/interface_guide/tor/torpage.jpg){class="glboxshadow"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
