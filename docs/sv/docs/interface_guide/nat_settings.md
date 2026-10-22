# NAT Settings {#nat-settings}

Funktionen är tillgänglig från firmware v4.5 och bytte namn till NAT Mode i v4.9.

---

Öppna **NETWORK** -> **NAT Settings** eller **SECURITY** -> **NAT Mode**.

På sidan kan du aktivera **Full Cone NAT** för stabilare peer-to-peer-anslutningar vid spel och strömning samt **SIP ALG** för kompatibilitetsproblem med VoIP/SIP-telefoni.

![nat settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/nat_settings/nat_settings.png){class="glboxshadow"}

## Supported Models {#supported-models}

??? "Supported Models"
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

    **Obs!** GL-SFT1200 (Opal) och GL-E750/E750V2 (Mudi) stöder funktionen i firmware v4.7 och senare.

??? "Unsupported Models"
    - GL-MT1300 (Beryl)
    - GL-AR750 (Creta)
    - GL-AR750S (Slate)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-XE300 (Puli)
    - GL-B1300 (Convexa-B)

## Full Cone NAT {#full-cone-nat}

Full Cone NAT acts as a "direct shortcut" for devices like game consoles or phones when connecting to others online (e.g., in multiplayer games or video calls).

By allowing external devices to directly reach local devices through the router — instead of hiding them behind multiple layers — it enhances peer-to-peer (P2P) connection stability, reduces latency, and resolves connection failures in P2P applications.

**Obs!** Funktionen kan ge lägre säkerhet än andra NAT-typer eftersom enhetsportar exponeras mot det offentliga nätverket.

## SIP ALG {#sip-alg}

SIP ALG (Application Layer Gateway) functions as a router "translator" for VoIP/SIP-based communication services, such as business desk phones or app-based calls.

Funktionen hanterar NAT-traverseringsproblem genom att justera samtalsdata för överföring genom flera NAT-lager och motverkar konflikter och samtalsavbrott.

**Note**: Incompatible or poorly implemented SIP ALG may degrade call quality, leading to issues including one-way audio, unresponsive ringing, dropped calls, or calls being routed directly to voicemail.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
