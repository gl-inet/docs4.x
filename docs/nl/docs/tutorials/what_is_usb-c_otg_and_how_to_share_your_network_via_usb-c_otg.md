# Wat is USB-C OTG en hoe deel je een netwerk via USB-C OTG? {#what-is-usb-c-otg-and-how-to-share-your-network-via-usb-c-otg}

## USB OTG {#usb-otg}
**USB OTG** (On-The-Go) is een USB-standaard waarmee compatibele apparaten zoals routers tussen **Host** en **Device** kunnen wisselen. Hierdoor zijn rechtstreekse gegevensoverdracht en voeding zonder afzonderlijk hostapparaat mogelijk.

Via **USB OTG** kun je tussen twee modi schakelen:

- In **Host mode** fungeert het apparaat als USB-host. Het start gegevensoverdracht, levert voeding en beheert alle lees- en schrijfbewerkingen tussen de twee apparaten.

- In **Device mode** werkt het apparaat als randapparaat. Het ontvangt voeding van de host en reageert op opdrachten, maar kan zelf geen communicatie starten.

## Network sharing via USB‑C OTG on Mudi 7 {#network-sharing-via-usbc-otg-on-mudi-7}

De USB-C-poort met OTG van Mudi 7 werkt in **Device**- of **Host**-modus voor flexibele netwerkdeling met externe apparaten:

### Connect to a Computer {#connect-to-a-computer}

De meeste computers werken alleen als host en ondersteunen geen OTG. Wanneer je een computer via USB verbindt, toont de router een moduskeuze. Je kunt elke modus selecteren. Mudi 7 probeert automatisch over de rol te onderhandelen, afhankelijk van de ondersteuning door het systeem en de stuurprogramma’s van het aangesloten apparaat. Na een geslaagde onderhandeling herkent de computer Mudi 7 als een USB-netwerkadapter voor internettoegang. In de meeste gevallen zijn geen extra stuurprogramma’s nodig.

### Connect to a Smartphone {#connect-to-a-smartphone}

- **Device Mode**: Mudi 7 werkt als USB-apparaat en deelt zijn netwerk met de telefoon.

- **Host Mode**: als je USB Tethering op de telefoon inschakelt, deelt deze het mobiele netwerk via USB met Mudi 7. De USB-verbinding kan als afzonderlijke WAN-interface voor Multi-WAN dienen.

!!! Note

    1. Controleer bij gebruik van OTG op de telefoon of deze OTG ondersteunt en gebruik een USB-datakabel. Kabels die alleen opladen kunnen geen netwerksignalen verzenden.

    2. In Device Mode toont de telefoon mogelijk geen melding over de netwerkverbinding. Controleer de netwerkstatus in de instellingen of voer een verbindingstest uit.

        Als je het netwerk van Mudi 7 via **Device Mode** met een telefoon deelt, bijvoorbeeld iPhone 17 Pro, controleer je als volgt of Device Mode actief is.

        1. Verbind de USB 3.1-poort van Mudi 7 met je iPhone 17 Pro via een USB-kabel die OTG ondersteunt.

        2. On the Mudi 7, select **Device Mode**.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. In de telefooninstellingen zie je dat Mudi 7 netwerktoegang aan de telefoon biedt.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Still have questions? Visit our [Community Forum](https://forum.gl-inet.com){target="_blank"} or [Contact us](https://www.gl-inet.com/contacts/){target="_blank"}.
