# Via USB-tethering verbinding maken met internet {#connect-to-the-internet-via-usb-tethering}

Het delen van de netwerkverbinding van je smartphone met de router via een USB-kabel heet Tethering. Een host-less modem werkt tijdens de installatie ook via Tethering.

**Opmerking:** sommige mobiele providers beperken tethering of brengen extra kosten in rekening. Vraag dit na bij je provider.

## Instellen {#setup}

=== "iPhone"

    1. Sluit een iPhone met een USB-kabel aan op de USB-poort van de router. Er verschijnt een systeemvenster waarin wordt gevraagd of je het apparaat vertrouwt. Tik op **Trust** om door te gaan.

        ![ios trust device](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_trust_this_computer.png){class="glboxshadow"}

    2. Ga op de iPhone naar **Settings** -> **Personal Hotspot**. Schakel **Allow Others to Join** in.

        ![ios allow others to join](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_allow_others_to_join.png){class="glboxshadow" width=400}

    3. Verbind een computer of andere telefoon met de router, meld je aan bij het webbeheerpaneel, ga naar **INTERNET** -> het gedeelte **Tethering** en klik op **Connect**.

        ![ios connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connect.png){class="glboxshadow"}

        Klik op **Advanced** als je geavanceerde instellingen, zoals TTL, HL en MTU, wilt aanpassen en klik vervolgens op **Connect**.

        ![ios advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_advanced.png){class="glboxshadow"}

        De verbinding wordt tot stand gebracht.

        ![ios connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connecting.png){class="glboxshadow"}

    4. Nadat de verbinding tot stand is gebracht, verschijnt de status van de persoonlijke hotspot, zoals het aantal verbonden apparaten, in de statusbalk bovenaan het telefoonscherm.

        ![personal hotspot status](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/iphone_hotspot_1_connection.png){class="glboxshadow" width=400}

        Het webbeheerpaneel toont ook de status van de Tethering-verbinding.

        ![ios tethering connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/ios_connected.png){class="glboxshadow"}

=== "Android"

    1. Sluit een Android-telefoon met een USB-kabel aan op de USB-poort van de router. Er kan een systeemvenster met USB-voorkeuren verschijnen. Selecteer **USB Tethering** of **File Transfer** als daarom wordt gevraagd.

        ![android usb purpose](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_usb_preference.png){class="glboxshadow" width=400}

    2. Ga op je telefoon naar **Settings** -> **Network & Internet** -> **Personal Hotspot**. Schakel **Personal Hotspot** of **USB Tethering** in.

        (De stappen om USB Tethering in te schakelen verschillen per merk. Controleer de instellingen van je apparaat voor de exacte locatie en neem zo nodig contact op met de ondersteuning van de fabrikant.)

        ![android personal hotspot](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_personal_hotspot.png){class="glboxshadow"}

    3. Verbind een computer of andere telefoon met de router, meld je aan bij het webbeheerpaneel, ga naar **INTERNET** -> het gedeelte **Tethering** en klik op **Connect**.

        ![android connect](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connect.png){class="glboxshadow"}

        Klik op **Advanced** als je geavanceerde instellingen, zoals TTL, HL en MTU, wilt aanpassen en klik vervolgens op **Connect**.

        ![android advanced](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_advanced.png){class="glboxshadow"}

        De verbinding wordt tot stand gebracht.

        ![android connecting](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connecting.png){class="glboxshadow"}

    4. Nadat de verbinding tot stand is gebracht, verschijnt de status van de persoonlijke hotspot, zoals het aantal verbonden apparaten, in de statusbalk bovenaan het telefoonscherm.

        Het webbeheerpaneel toont ook de status van de Tethering-verbinding.

        ![android connected](https://static.gl-inet.com/docs/router/en/4/interface_guide/internet_tethering/android_connected.png){class="glboxshadow"}

    Raadpleeg voor de officiële Android-documentatie [Een mobiele verbinding delen via een hotspot of tethering op Android](https://support.google.com/android/answer/9059108?hl=en#zippy=%2Ctether-by-usb-cable){target="_blank"}.

## Waarschuwing {#warning}

Wanneer internettoegang niet beschikbaar is, verschijnt de bijbehorende waarschuwing:

**"De interface is verbonden, maar internet is niet toegankelijk."**

Oplossingen:

1. Controleer of de smartphone internettoegang heeft.

2. Ga naar de pagina [Multi-WAN](multi-wan.md) om te controleren of internet toegankelijk is.

## Probleemoplossing {#troubleshooting}

Voer bij een mislukte verbinding de volgende stappen uit:

- Gebruik de oorspronkelijke voeding van de router.
- Koppel de USB-kabel los en sluit deze opnieuw aan.
- Gebruik een andere USB-kabel. Controleer of deze gegevensoverdracht ondersteunt en niet alleen opladen.
- Schakel "USB Tethering" enkele keren uit en weer in op een Android-telefoon.
- Schakel "Allow Others to Join" enkele keren uit en weer in op een iPhone.
- Start je smartphone opnieuw op en probeer het opnieuw.

---

Gerelateerde artikelen

- [Internetpagina](internet.md)
- [Hoe stel je de prioriteit van elke methode voor internettoegang in?](multi-wan.md)
- [Hoe stel je load balancing in wanneer meerdere methoden voor internettoegang tegelijk worden gebruikt?](multi-wan.md)

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
