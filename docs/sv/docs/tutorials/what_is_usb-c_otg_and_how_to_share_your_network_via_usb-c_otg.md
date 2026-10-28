# Vad är USB-C OTG och hur delar du nätverket via USB-C OTG? {#what-is-usb-c-otg-and-how-to-share-your-network-via-usb-c-otg}

## USB OTG {#usb-otg}
**USB OTG** (On-The-Go) är en USB-standard som gör att kompatibla enheter, till exempel routrar, kan växla mellan rollerna **Host** och **Device**. Det möjliggör direkt dataöverföring och strömutbyte utan en separat värdenhet.

Följande två lägen kan väljas via **USB OTG**:

- När en enhet växlar till **Host mode** via USB OTG fungerar den som USB-värd. Den initierar dataöverföringen, levererar ström och styr alla läs- och skrivåtgärder mellan de två anslutna enheterna.

- I **Device mode** fungerar enheten som kringutrustning, får ström från värden och svarar passivt på dess kommandon utan att kunna initiera kommunikation på egen hand.

## Nätverksdelning via USB-C OTG på Mudi 7 {#network-sharing-via-usbc-otg-on-mudi-7}

Den OTG-kompatibla USB-C-porten på Mudi 7 fungerar i antingen **Device**- eller **Host**-läge för flexibel nätverksdelning med externa enheter. Följande scenarier är möjliga:

### Ansluta till en dator {#connect-to-a-computer}

De flesta datorer fungerar endast som värdar och stöder inte OTG. När en dator ansluts till routern via USB visar routern ett fönster för val av läge. Du kan välja valfritt läge. Mudi 7 försöker automatiskt förhandla om rollen, beroende på den anslutna enhetens system- och drivrutinsstöd. När förhandlingen har lyckats identifierar datorn Mudi 7 som en USB-nätverksadapter för internetåtkomst. I de flesta fall behövs inga ytterligare drivrutiner.

### Ansluta till en smarttelefon {#connect-to-a-smartphone}

- **Device Mode**: Mudi 7 fungerar som en USB-enhet och delar sitt nätverk med telefonen.

- **Host Mode**: När du aktiverar USB Tethering på telefonen kan den dela sitt mobilnät med Mudi 7 via USB. USB-länken kan fungera som ett separat WAN-gränssnitt och möjliggöra Multi-WAN-anslutning.

!!! Note

    1. När du använder telefonens OTG-funktion för anslutningen kontrollerar du att telefonen stöder OTG och använder en USB-kabel som kan överföra data. Kablar som endast kan ladda kan inte överföra nätverkssignaler.

    2. När Device Mode är aktiverat kanske telefonen inte visar någon avisering om nätverksanslutningen. Kontrollera nätverksstatusen i telefonens inställningar eller kör ett anslutningstest för att verifiera funktionen.

        Om du till exempel delar nätverket från Mudi 7 till en telefon via **Device Mode** (t.ex. iPhone 17 Pro) kontrollerar du att Device Mode är aktivt genom att följa stegen nedan.

        1. Använd en USB-kabel som stöder OTG för att ansluta USB 3.1-porten på Mudi 7 till din iPhone 17 Pro.

        2. Välj **Device Mode** på Mudi 7.

            ![usb mode selection](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_mode_selection.png){class="glboxshadow" width="250"}

        3. I telefonens inställningar visas att Mudi 7 ger telefonen nätverksåtkomst enligt skärmbilden nedan.

            ![usb device mode](https://static.gl-inet.com/docs/router/en/4/tutorials/how_to_share_your_Network_via_USB-C_OTG/e5800_usb_device_mode.png){class="glboxshadow" width="600"}

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
