# LAN {#lan}

Ga links in het webbeheerpaneel naar **NETWORK** -> **LAN**.

LAN is het netwerk waarmee je apparaat is verbonden via de hoofd-Wi-Fi of een Ethernet-kabel.

De pagina bevat Basic Settings, DHCP Server Settings en Address Reservation.

## Basisinstellingen {#basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![lan basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/basic_settings.jpg){class="glboxshadow"}

- **Router IP Address**

    Dit is het adres dat je in de adresbalk van je browser invoert om de beheerpagina van de router te openen.

    De standaardwaarde is **192.168.8.1**. Je kunt het adres wijzigen als er een conflict met je netwerk optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

## DHCP-server {#dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters aan elk clientapparaat toe.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_server.png){class="glboxshadow"}

Klik zo nodig op **Advanced** voor verdere configuratie.

![dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_1.png){class="glboxshadow"}

![dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/dhcp_advanced_2.png){class="glboxshadow"}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het lokale netwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server): een dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat verzenden. Je kunt meerdere LPR-printerpoorten configureren.

## Adresreservering {#address-reservation}

Wanneer je binnen het LAN een IP-adres voor een client reserveert, ontvangt de client telkens hetzelfde IP-adres wanneer deze de DHCP-server van de router gebruikt. Je kunt gereserveerde IP-adressen toewijzen aan computers of servers die permanente IP-instellingen nodig hebben.

**Opmerking:** geconfigureerde clients moeten opnieuw verbinding maken met de router om de instelling te activeren.

Klik op **Add** om een IP-adres te reserveren.

![Address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_1.png){class="glboxshadow"}

Er verschijnt een pop-upvenster.

![Address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_2.png){class="glboxshadow"}

Selecteer de **MAC** in de vervolgkeuzelijst. Het **IP** dat bij de geselecteerde MAC hoort, wordt automatisch ingevuld. Geef het een beschrijvende naam en klik op **Submit**.

![Address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_3.png){class="glboxshadow"}

Nadat je een nieuwe IP-adresreservering hebt toegevoegd, verschijnt de onderstaande pagina. Dit betekent dat de instelling is geslaagd.

![Address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/lan/address_reservation_4.jpg){class="glboxshadow"}

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
