# Subnet {#subnet}

**Opmerking**: deze pagina is momenteel beschikbaar op Flint 4 (GL-BE14000) en wordt met firmware v4.10 voor andere modellen uitgerold.

---

Ga links in het webbeheerpaneel naar **NETWORK** -> **Subnet**.

Op deze pagina kun je **Main Network**, **Guest Network**, **IoT Network** en aangepaste **VLAN Networks** centraal configureren en beheren. Je kunt meerdere subnetten maken en beheren om verschillende soorten apparaten of verkeer te isoleren.

## Main Network {#main-network}

**Main Network** is het netwerk waarmee je apparaat via de hoofd-Wi-Fi of een Ethernet-kabel is verbonden.

In Main Network kun je de status van alle interfaces, VLAN ID, het IP-adres van de router en DHCP Range bekijken.

![main network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit** om Main Network te configureren.

![main network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-2.png){class="glboxshadow"}

De configuratiepagina bevat Basic Settings, DHCP Server Settings en Address Reservation.

### Basic Settings {#basic-settings}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![main network basic settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-basic.png){class="glboxshadow" width=650}

- **Router IP Address**

    Dit is het adres dat je in de adresbalk van je browser invoert om de beheerpagina van de router te openen.

    De standaardwaarde is **192.168.8.1**. Je kunt het adres wijzigen als er een conflict met je netwerk optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De standaard-VLAN ID van Main Network is **1** en kan niet worden gewijzigd.

- **AP Isolation**

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

### DHCP Server {#dhcp-server}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters aan elk clientapparaat toe.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![main network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klik zo nodig op **Advanced** voor verdere configuratie.

![main network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-2.png){class="glboxshadow" width=650}

![main network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/main-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het lokale netwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server): een dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat verzenden. Je kunt meerdere LPR-printerpoorten configureren.

### Address Reservation {#address-reservation}

Wanneer je binnen het LAN een IP-adres voor een client reserveert, ontvangt de client telkens hetzelfde IP-adres wanneer deze de DHCP-server van de router gebruikt. Je kunt gereserveerde IP-adressen toewijzen aan computers of servers die permanente IP-instellingen nodig hebben.

**Opmerking:** geconfigureerde clients moeten opnieuw verbinding maken met de router om de instelling te activeren.

Klik op **Add** om een IP-adres te reserveren.

![main network address Reservation 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-1.png){class="glboxshadow" width=650}

Er verschijnt een pop-upvenster.

![main network address Reservation 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-2.png){class="glboxshadow" width=650}

Selecteer **MAC** in de vervolgkeuzelijst. Het beschikbare **IP** wordt automatisch ingevuld. Voer eventueel een **hostname** en aangepaste **name** in en klik op **Submit**.

![main network address Reservation 3](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-3.png){class="glboxshadow" width=650}

Nadat je een nieuwe IP-adresreservering hebt toegevoegd, verschijnt de onderstaande pagina. Dit betekent dat de instelling is geslaagd.

![main network address Reservation 4](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/address-reservation-4.png){class="glboxshadow" width=650}

## Guest Network {#guest-network}

**Guest Network** biedt een speciaal Wi-Fi-netwerk voor bezoekers. Het is van het primaire netwerk gescheiden voor betere beveiliging en eenvoudige internettoegang.

**Opmerking**: sommige modellen, zoals GL-MT5000 en GL-MT2500/GL-MT2500A, hebben geen Wi-Fi-functie. De instellingen voor Guest Network zijn daarom niet beschikbaar in hun webbeheerpaneel.

In Guest Network kun je de interfacestatus, VLAN ID, Gateway en DHCP Range bekijken.

![guest network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit**. Het configuratiepaneel van Guest Network wordt rechts geopend.

![guest network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-2.png){class="glboxshadow"}

De configuratiepagina bevat Basic Settings en DHCP Server Settings.

### Basic Settings {#basic-settings_1}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![guest network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    De **standaardgateway** van Guest Network is **192.168.9.1**. Wijzig deze als er een conflict met je lokale netwerk optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De standaard-VLAN ID van Guest Network is **9** en kan worden gewijzigd.

- **AP Isolation**

    Deze functie is beschikbaar sinds firmware v4.5.

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

- **WAN Access Control**

    WAN Access Control beheert toegang van het lokale subnet tot WAN-netwerken, waaronder internet en andere WAN-subnets.

    Er zijn drie modi voor WAN Access Control:

    - **Unrestricted**: geeft het subnet onbeperkte toegang tot internet en andere WAN-subnets.

    - **Block WAN Subnet**: blokkeert andere WAN-subnets; internet blijft beschikbaar.

    - **Block Internet Access**: blokkeert alle uitgaande toegang, waaronder internet en WAN-subnets.

### DHCP Server {#dhcp-server_1}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters aan elk clientapparaat toe.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![guest network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klik zo nodig op **Advanced** voor verdere configuratie.

![guest network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-2.png){class="glboxshadow" width=650}

![guest network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/guest-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het lokale netwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server): een dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat sturen. Je kunt meerdere LPR-printerpoorten configureren.

## IoT Network {#iot-network}

IoT Network maakt een speciaal Wi-Fi-netwerk voor IoT-apparaten. Het is van het primaire netwerk gescheiden voor betere compatibiliteit en beveiliging.

**Opmerking**: sommige modellen, zoals GL-MT5000 en GL-MT2500/GL-MT2500A, hebben geen Wi-Fi-functie. De instellingen voor IoT Network zijn daarom niet beschikbaar in hun webbeheerpaneel.

In IoT Network kun je de interfacestatus, VLAN ID, Gateway en DHCP Range bekijken.

![iot network 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-1.png){class="glboxshadow"}

Klik rechtsonder op **Edit**. Het configuratiepaneel van IoT Network wordt rechts geopend. Hier kun je Basic Settings en DHCP Server Settings configureren.

![iot network 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_2}

Je kunt het subnet instellen binnen de privé-IPv4-adresbereiken `192.168.0.0/16`, `172.16.0.0/12` en `10.0.0.0/8`.

![iot network basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-basic.png){class="glboxshadow" width=650}

- **Gateway**

    De **standaardgateway** van IoT Network is **192.168.10.1**. Wijzig deze als er een conflict met je lokale netwerk optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    De standaard-VLAN ID van IoT Network is **10** en kan worden gewijzigd.

- **AP Isolation**

    Deze functie is beschikbaar sinds firmware v4.5.

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

- **WAN Access Control**

    WAN Access Control beheert toegang van het lokale subnet tot WAN-netwerken, waaronder internet en andere WAN-subnets.

    Er zijn drie modi voor WAN Access Control:

    - **Unrestricted**: geeft het subnet onbeperkte toegang tot internet en andere WAN-subnets.

    - **Block WAN Subnet**: blokkeert andere WAN-subnets; internet blijft beschikbaar.

    - **Block Internet Access**: blokkeert alle uitgaande toegang, waaronder internet en WAN-subnets.

### DHCP Server {#dhcp-server_2}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters aan elk clientapparaat toe.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![iot network dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-1.png){class="glboxshadow" width=650}

Klik zo nodig op **Advanced** voor verdere configuratie.

![iot network dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-2.png){class="glboxshadow" width=650}

![iot network dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/iot-network-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het lokale netwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server): een dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat verzenden. Je kunt meerdere LPR-printerpoorten configureren.

## VLAN-netwerken {#vlan-networks}

Bovenaan de hoofdpagina kun je extra **VLAN networks** maken om apparaten of bezoekersverkeer te isoleren.

![vlan networks 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-1.png){class="glboxshadow"}

Klik rechts op **+ Add** om een nieuw netwerk te configureren.

![vlan networks 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-2.png){class="glboxshadow"}

### Basic Settings {#basic-settings_3}

Op deze pagina kun je de basisgegevens van **VLAN Networks** configureren.

![vlan networks basic setting](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-basic-settings.png){class="glboxshadow" width=650}

- **Name**

    Geef het nieuwe subnet een aangepaste herkenbare naam.

- **Gateway**

    Configureer handmatig de gateway voor het nieuwe subnet. Wijzig deze als er een conflict met het bestaande LAN-segment optreedt.

- **Netmask**

    De standaardwaarde is **255.255.255.0**. Je kunt ook **255.255.0.0** selecteren als je een groter subnet met meer IP-adressen nodig hebt.

- **VLAN ID**

    Wijs bij het maken van een subnet een VLAN ID tussen **9** en **4000** toe. Gebruik geen reeds bezette id om conflicten te voorkomen.

- **AP Isolation**

    Deze functie is beschikbaar sinds firmware v4.5.

    Je kunt clientapparaten in een afzonderlijk netwerksegment isoleren. Deze apparaten kunnen dan niet met andere apparaten in hetzelfde netwerk communiceren.

- **WAN Access Control**

    WAN Access Control beheert toegang van het lokale subnet tot WAN-netwerken, waaronder internet en andere WAN-subnets.

    Er zijn drie modi voor WAN Access Control:

    - **Unrestricted**: geeft het subnet onbeperkte toegang tot internet en andere WAN-subnets.

    - **Block WAN Subnet**: blokkeert andere WAN-subnets; internet blijft beschikbaar.

    - **Block Internet Access**: blokkeert alle uitgaande toegang, waaronder internet en WAN-subnets.

### DHCP Server {#dhcp-server_3}

De **DHCP Server** is standaard ingeschakeld. De DHCP-server wijst automatisch IP-adressen en andere communicatieparameters aan elk clientapparaat toe.

Als de DHCP-server is uitgeschakeld, moet je de netwerkinstellingen voor clientapparaten handmatig configureren. Klik [hier](../tutorials/manually_configure_static_ip.md) om te lezen hoe je handmatig een statisch IP-adres configureert.

Je kunt de begin- en eind-IP-adressen aanpassen, bijvoorbeeld wanneer je netwerk groter of kleiner wordt, IP-adresconflicten optreden of het bereik van het subnetmasker wordt gewijzigd.

![vlan networks dhcp simple settings](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-1.png){class="glboxshadow" width=650}

Klik zo nodig op **Advanced** voor verdere configuratie.

![vlan networks dhcp advanced settings 1](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-2.png){class="glboxshadow" width=650}

![vlan networks dhcp advanced settings 2](https://static.gl-inet.com/docs/router/en/4/interface_guide/subnet/vlan-networks-dhcp-server-3.png){class="glboxshadow" width=650}

- **Lease Time**: de periode waarin een door DHCP toegewezen IP-adres geldig is voor een apparaat.

- **Gateway**: het apparaat dat verkeer tussen het lokale netwerk en externe netwerken, zoals internet, routeert.

- **DNS Server 1**: de primaire server die domeinnamen in IP-adressen omzet.

- **DNS Server 2**: de secundaire server voor domeinnaamomzetting wanneer de primaire DNS-server niet beschikbaar is.

- **LPR Server** (Line Printer Remote Server): een dienst die afdruktaken beheert en netwerkapparaten afdrukverzoeken naar externe printers laat verzenden. Je kunt meerdere LPR-printerpoorten configureren.

Na de configuratie verschijnt het nieuwe VLAN-netwerk met subnetinformatie op de huidige pagina.

---

Heb je nog vragen? Bezoek ons [Community Forum](https://forum.gl-inet.com){target="_blank"} of [neem contact met ons op](https://www.gl-inet.com/contacts/){target="_blank"}.
