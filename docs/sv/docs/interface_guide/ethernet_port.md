# Ethernet Port {#ethernet-port}

Innehållet på sidan bygger på firmwareversion v4.7-4.9. Om enheten kör en annan firmwareversion använder du väljaren nedan för att byta till motsvarande guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.9 and earlier" markdown="1">

- [Firmware v4.10 och senare](ethernet_port_v4.10.md)

</div>

---

Öppna **NETWORK** -> **Ethernet Port** eller **Port Management** på vänster sida i webbadministrationspanelen.

Här kan du hantera Ethernet-portarnas roller (WAN/LAN) och visa portinformation som MAC-adress och förhandlad hastighet.

## WAN {#wan}

Avsnittet visar portroll (WAN eller LAN), MAC-adress och förhandlad hastighet.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/wan.png){class="glboxshadow"}

- **WAN/LAN**: Aktuellt driftläge för den fysiska WAN-porten. Du kan ändra det till LAN vid behov.

- **MAC Mode**: Factory Mode används som standard. Du kan byta till Clone Mode eller Random Mode.

- **MAC Address**: WAN-gränssnittets MAC-adress.

- **Negotiated Network Port Rate**: WAN-gränssnittets förhandlade länkhastighet. Visas endast när en giltig länk identifieras.

## LAN {#lan}

Avsnittet visar LAN-portens förhandlade hastighet. Den visas endast när en giltig länk identifieras.

![lan1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/lan1.png){class="glboxshadow"}

Some models support switching LAN 1 to a WAN port for dual-Ethernet WAN scenario. Click [Dual-Ethernet WAN](#dual-ethernet-wan) for details.

## Dual-Ethernet WAN {#dual-ethernet-wan}

Med Dual-Ethernet WAN kan du ändra en Ethernet-port som normalt är LAN till en sekundär WAN-port för internetåtkomst via två Ethernet-anslutningar. Det ger en tillförlitlig reservanslutning och stöder bandbreddsaggregering där det är kompatibelt. Du kan även ansluta till två oberoende nätverk, till exempel arbete och privat, samtidigt utan extra maskinvara.

??? "Supported Models"

    - GL-BE14000 (Flint 4)
    - GL-BE10000 (Slate 7 Pro)
    - GL-MG1300 (Mango 2)
    - ※GL-E5800 (Mudi 7)
    - GL-MT3600BE (Beryl 7)
    - GL-MT5000 (Brume 3)
    - GL-BE6500 (Flint 3e)
    - GL-BE9300 (Flint 3)
    - GL-BE3600 (Slate 7)
    - GL-X2000 (Spitz Plus)
    - GL-MT6000 (Flint 2)
    - GL-X3000 (Spitz AX)
    - GL-XE3000 (Puli AX)

    **Obs!** GL-E5800 (Mudi 7) har en Ethernet-port (LAN som standard, kan ändras till WAN) och en **OTG-aktiverad USB-C-port**. Lägg till en andra Ethernet-port för Dual-Ethernet WAN genom att ansluta en separat såld USB‑C-till-Ethernet-adapter till USB‑C-porten.

??? "Unsupported Models"
    - GL-B3000 (Marble)
    - GL-AX1800 (Flint)
    - GL-MT2500/GL-MT2500A (Brume 2)
    - GL-MT3000 (Beryl AX)
    - GL-AXT1800 (Slate AX)
    - GL-SFT1200 (Opal)
    - GL-A1300 (Slate Plus)
    - GL-MT1300 (Beryl)
    - GL-E750/E750V2 (Mudi)
    - GL-AR750S (Slate)
    - GL-XE300 (Puli)
    - GL-X750 (Spitz)
    - GL-MT300N-V2 (Mango)
    - GL-AR300M Series (Shadow)
    - GL-B1300 (Convexa-B)
    - GL-X300B (Collie)

Follow the steps below to switch a LAN port to a WAN port.

1. Klicka på fliken **LAN** på sidan **Port Management** eller **Ethernet Port**, ändra portrollen till WAN och klicka sedan på **Apply**.

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_1.png){class="glboxshadow"}

2. Klicka på **Apply** i popup-fönstret.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ethernet_port/dual_ethernet_2.png){class="glboxshadow"}

3. Den valda porten fungerar nu som WAN-port. Fortsätt med att konfigurera Multi-WAN [här](multi-wan.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
