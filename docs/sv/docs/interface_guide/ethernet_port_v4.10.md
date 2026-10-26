# Ethernet Port (Firmware v4.10) {#ethernet-port-firmware-v410}

**Obs!** Innehållet på sidan introducerades först i Flint 4 (GL-BE14000) och lanseras för andra modeller i firmware v4.10.

Om enheten kör en annan firmwareversion använder du väljaren nedan för att byta till motsvarande guide.

<div class="gl-link-select" data-label="Firmware version" data-placeholder="Firmware v4.10" markdown="1">

- [Firmware v4.9 and earlier](ethernet_port.md)

</div>

---

Öppna **NETWORK** -> **Ethernet Port** på vänster sida i webbadministrationspanelen.

Sidan visar alla routergränssnitt. Du kan visa anslutningsstatus för varje gränssnitt, hantera Ethernet-portroller (WAN eller LAN) och visa information som MAC-adress, förhandlad hastighet och aktuell länkstatus. Du kan dessutom tilldela fysiska gränssnitt till skapade subnät.

![ethernet port](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/ethernet_port.png){class="glboxshadow"}

- **Link Up**: När portikonen är blå är den fysiska länken aktiv.

- **Link Down**: När portikonen är grå är den fysiska länken inaktiv.

- **Speed**: Ethernet-portens förhandlade överföringshastighet.

- **MAC**: Portens MAC-adress.

- **VLAN Mode**: LAN-portarnas driftläge kan anges till Standard eller Multiple VLANs.

- **Native Network**:  Default untagged subnet assigned to the LAN port.

- **Allowed VLANs**: Specifies tagged VLANs permitted to pass through this port under Multiple VLANs mode.

- **Settings**: Klicka för att öppna konfigurationssidan för respektive port.

## WAN {#wan}

Avsnittet visar Port Mode (WAN eller LAN), MAC-adress och förhandlad hastighet.

![wan](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/wan_1.png){class="glboxshadow" width=600}

- **Port Mode**: Aktuellt driftläge för den fysiska WAN-porten. Du kan ändra det till LAN vid behov.

- **MAC Mode**: Factory Mode används som standard. Du kan byta till Clone Mode eller Random Mode.

- **MAC Address**: WAN-gränssnittets MAC-adress.

- **Negotiated Network Port Rate**: WAN-gränssnittets förhandlade länkhastighet. Visas endast när en giltig länk identifieras.

## LAN {#lan}

Avsnittet visar LAN-portkonfigurationen. Ange Ethernet Mode till **Standard** eller **Multiple VLANs** efter behov.

### Standard Mode {#standard-mode}

Standard Mode allows only one VLAN (Untagged), used for connecting end devices.

![lan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan1.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: LAN-gränssnittets förhandlade länkhastighet. Visas endast när en giltig länk identifieras.

- **Ethernet Mode**: Defaults to Standard Mode.

- **Access Network**: Isolera nätverk genom att tilldela LAN-portar till olika subnät.

När konfigurationen är klar återgår du till sidan Ethernet Port och kontrollerar inställningarna.

### Multiple VLANs Mode {#multiple-vlans-mode}

Multiple VLANs mode allows multiple VLANs (Tagged) on one port, typically for connecting APs or other switches.

![lan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/lan2.png){class="glboxshadow" width=600}

- **Negotiated Network Port Rate**: LAN-gränssnittets förhandlade länkhastighet. Visas endast när en giltig länk identifieras.

- **VLAN Mode**: Växla till Multiple VLANs genom att klicka på fliken Multiple VLANs.

- **Untagged Traffic Handling**: Konfigurera hantering av otaggade paket för porten. Du kan kassera dem direkt eller vidarebefordra dem till ett annat subnät som inbyggt PVID-nätverk.

- **Allowed Tagged Networks**: Anger vilka VLAN som får passera porten i taggat läge. Välj VLAN-nätverk i listan; endast matchande trafik vidarebefordras.

När konfigurationen är klar återgår du till sidan Ethernet Port och kontrollerar inställningarna.

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

Follow the steps below to switch a LAN port to a WAN port, using the Flint 3 (GL-BE9300) as an example.

1. Klicka på inställningen **LAN1** på sidan **Ethernet Port** för att öppna Configuration. Ändra sedan portrollen till WAN och klicka på **Apply**.

    ![dual ethernet wan ](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan.png){class="glboxshadow"}

    ![dual ethernet wan 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_1.png){class="glboxshadow" width=600}

2. Återgå till sidan Ethernet Port och kontrollera att portrollen har ändrats till WAN.

    ![dual ethernet wan 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/ehternet_port_v4.10/dual_ethernet_wan_2.png){class="glboxshadow"}

3. Den valda porten fungerar nu som WAN-port. Fortsätt med att konfigurera Multi-WAN [här](multi-wan.md).

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
