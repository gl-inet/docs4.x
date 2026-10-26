# Network Acceleration {#network-acceleration}

Nätverksacceleration minskar processorbelastningen och påskyndar paketvidarebefordran men kan stå i konflikt med vissa funktioner.

När Network Acceleration är aktiverat fungerar Client Speed and Traffic Statistics och Client Speed Limit inte korrekt.

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
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)
    - GL-MT3000 (Beryl AX)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-SFT1200 (Opal)
    - GL-MT1300 (Beryl)

??? "Unsupported Models"
    - GL-AXT1800 (Slate AX)
    - GL-AX1800 (Flint)
    - GL-A1300 (Slate Plus)
    - GL-E750/E750V2 (Mudi)
    - GL-X750/GL-X750V2 (Spitz)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

## Setup {#setup}

Öppna **NETWORK** -> **Network Acceleration** på vänster sida i webbadministrationspanelen.

![Network Acceleration](https://static.gl-inet.com/docs/router/en/4/interface_guide/network_acceleration/network_acceleration.png){class="glboxshadow"}

There are three modes.

- **Auto**

    Auto mode will automatically switch between the two acceleration modes based on actual usage.

- **Hardware Acceleration**

    Hardware acceleration works on <u>Ethernet</u> and <u>Repeater</u>.

    Maskinvaruacceleration flyttar nätverksuppgifter som NAT, paketvidarebefordran och kontrollsummor till särskild maskinvara som NPU- eller HWNAT-chip. Den fungerar för Ethernet- och Repeater-anslutningar och ger hög kapacitet, låg latens och låg processorbelastning.

- **Software Acceleration**

    Software acceleration works on <u>Cellular</u>.

    Programvaruacceleration använder routerns processor med optimerade kärnor eller drivrutiner, till exempel SWNAT. Den fungerar för Cellular (4G/5G) när maskinvaruacceleration saknas och stöder komplexa protokoll, men kan begränsas av processorn vid hög bandbredd och funktioner som DPI, QoS eller portvidarebefordran.

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
