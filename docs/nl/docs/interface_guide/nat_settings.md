# NAT Settings {#nat-settings}

Deze functie is beschikbaar sinds firmware v4.5 en is in v4.9 hernoemd naar NAT Mode.

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **NAT Settings** of **SECURITY** -> **NAT Mode**.

Op deze pagina kun je **Full Cone NAT** inschakelen om peer-to-peerverbindingen voor games en streaming te stabiliseren en **SIP ALG** om compatibiliteitsproblemen met VoIP/SIP-telefonie op te lossen.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Ondersteunde modellen {#supported-models}

??? "Ondersteunde modellen"
    - GL-MT6000 (Fortify)
    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - GL-E5800 (Mudi 7)
    - GL-MT5000 (Brume 3)
    - GL-MT3600BE (Beryl 7)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-B3000 (Marble)
    - GL-MT6000 (Flint 2)
    - GL-AX1800 (Flint)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-A1300 (Slate Plus)
    - GL-X300B (Collie)
    - ※GL-SFT1200 (Opal)
    - ※GL-E750/E750V2 (Mudi)

    **Opmerking**: GL-SFT1200 (Opal) en GL-E750/E750V2 (Mudi) ondersteunen deze functie in firmware v4.7 en hoger.

??? "Niet-ondersteunde modellen"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT {#full-cone-nat}

Full Cone NAT werkt als een rechtstreekse route voor apparaten zoals gameconsoles of telefoons bij online verbindingen, bijvoorbeeld voor multiplayergames of videogesprekken.

Doordat externe apparaten lokale apparaten rechtstreeks via de router kunnen bereiken in plaats van achter meerdere lagen te worden verborgen, verbetert de stabiliteit van peer-to-peerverbindingen (P2P), daalt de latentie en worden verbindingsproblemen in P2P-toepassingen opgelost.

**Opmerking**: deze functie kan minder veilig zijn dan andere NAT-typen, omdat apparaatpoorten aan het openbare netwerk worden blootgesteld.

## SIP ALG {#sip-alg}

SIP ALG (Application Layer Gateway) werkt als vertaler voor VoIP/SIP-communicatiediensten, zoals zakelijke telefoons en oproepen via apps.

SIP ALG past gespreksgegevens aan om problemen met NAT traversal op te lossen en overdracht via meerdere NAT-lagen mogelijk te maken, zoals in netwerken met een primaire en een GL.iNet-router. Hierdoor worden conflicten en gespreksonderbrekingen beperkt.

**Opmerking**: incompatibele of slecht geïmplementeerde SIP ALG kan de gesprekskwaliteit verminderen en eenzijdig geluid, niet-overgaande telefoons, verbroken gesprekken of rechtstreeks doorgestuurde voicemail veroorzaken.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
