# Anslut till internet via internetdelning med USB {#connect-to-the-internet-via-usb-tethering}

Att dela nätverket från en smartphone till routern med en USB-kabel kallas Tethering. Värdlösa modem använder också Tethering när modemet konfigureras.

**Obs!** Vissa mobiloperatörer begränsar eller tar extra betalt för internetdelning. Kontrollera villkoren med operatören.

## Setup {#setup}

=== "iPhone"

    1. Connect an iPhone to the router's USB port using a USB cable. A system dialog will appear asking whether to trust the device. Tap **Trust** to proceed.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Go to iPhone **Settings** -> **Personal Hotspot**. Enable **Allow Others to Join**.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Anslut en dator eller en annan telefon till routern, logga in på routerns webbadministrationspanel, öppna **INTERNET** -> avsnittet **Tethering** och klicka på **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connect.png){class="glboxshadow"}

        Om du behöver avancerade inställningar som TTL, HL och MTU klickar du på **Advanced**, anpassar inställningarna och klickar sedan på **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_advanced.png){class="glboxshadow"}

        It will start connecting.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. När anslutningen har upprättats visas status för personlig hotspot, till exempel antal anslutna enheter, i statusfältet högst upp på telefonskärmen.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        The web admin panel will also display the Tethering connection status.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Anslut en Android-telefon till routerns USB-port med en USB-kabel. En systemdialogruta för USB-inställningar kan visas. Välj **USB Tethering** eller **File Transfer** om du uppmanas att göra det.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Go to your phone's **Settings** -> **Network & Internet** -> **Personal Hotspot**. Enable **Personal Hotspot** or **USB Tethering**.

        (Stegen för att aktivera USB Tethering varierar efter märke. Kontrollera var inställningen finns på enheten och kontakta tillverkarens support vid behov.)

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Anslut en dator eller en annan telefon till routern, logga in på routerns webbadministrationspanel, öppna **INTERNET** -> avsnittet **Tethering** och klicka på **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connect.png){class="glboxshadow"}

        Om du behöver avancerade inställningar som TTL, HL och MTU klickar du på **Advanced**, anpassar inställningarna och klickar sedan på **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_advanced.png){class="glboxshadow"}

        It will start connecting.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. När anslutningen har upprättats visas status för personlig hotspot, till exempel antal anslutna enheter, i statusfältet högst upp på telefonskärmen.

        The web admin panel will also display the Tethering connection status.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connected.png){class="glboxshadow"}

    For the Android official documentation, refer to [Share a mobile connection by hotspot or tethering on Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}

## Warning {#warning}

När internetåtkomst saknas visas följande varning:

**"The interface is connected, but the Internet can't be accessed."**

Solutions:

1. Kontrollera att smarttelefonen har internetåtkomst.

2. Öppna sidan [Multi-WAN](multi-wan.md) och kontrollera om internet är åtkomligt.

## Troubleshooting {#troubleshooting}

Om anslutningen misslyckas provar du följande felsökningssteg:

- Use the original power supply for the router.
- Koppla från och anslut USB-kabeln igen.
- Use another USB cable. Ensure it supports data transfer (not just charging).
- Turn off and turn on "USB Tethering" for a few times (for Android Phone).
- Turn off and turn on "Allow Others to Join" for a few times (for iPhone).
- Starta om smarttelefonen och försök igen.

---

Related Articles

- [Internet page](internet.md)
- [Ange prioriteten för varje internetanslutningsmetod](multi-wan.md)
- [Ange lastbalansering när flera internetanslutningsmetoder används samtidigt](multi-wan.md)

---

Har du fortfarande frågor? Besök vårt [communityforum](https://forum.gl-inet.com){target="_blank"} eller [kontakta oss](https://www.gl-inet.com/contacts/){target="_blank"}.
